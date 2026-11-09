/**
 * GPU Where jobs Worker — a separate deployment that runs the Python scrapers
 * as on-demand jobs, with an optional configurable schedule.
 *
 * The scrapers themselves run in GitHub Actions (free for public repositories);
 * this Worker is the token-protected control plane. It is not part of the Pages
 * site deployment.
 *
 *   GET  /health                 liveness, no auth
 *   GET  /jobs                   job list + latest GitHub run (auth)
 *   POST /run?job=pricing        dispatch a workflow now (auth)
 *   POST /run  {"job":"pricing"} same, JSON body
 *   GET  /schedule               effective schedule (auth)
 *   PUT  /schedule               change it at runtime (auth, needs KV)
 *
 * Scheduling is opt-in and configurable:
 *   - the cron tick is daily at 00:00 UTC (`0 0 * * *`) and dispatches the jobs
 *     listed in DAILY_JOBS, once per UTC day;
 *   - bind JOBS_CONFIG (KV) to change the enabled/jobs list at runtime with
 *     PUT /schedule without redeploying;
 *   - SCHEDULE_ENABLED=false is a kill switch that leaves on-demand runs working.
 *
 * Secrets: JOB_TOKEN, GITHUB_TOKEN (Actions: write), GITHUB_REPO ("owner/repo").
 * Vars: GITHUB_REF, SCHEDULE_ENABLED, DAILY_JOBS.
 *
 * There is no cron entry in the site's Pages project. This Worker and Pages are
 * deployed separately: `make deploy-jobs` vs `make deploy`.
 */

const JOBS = {
  availability: {
    workflow: "refresh-availability.yml",
    summary: "Collect free GPUs per provider/region/GPU/shape and commit observations.",
  },
  pricing: {
    workflow: "refresh-pricing.yml",
    summary: "Scrape official pricing, update SKUs and retire superseded packages.",
  },
};

const DEFAULTS = {
  enabled: true,
  jobs: ["availability", "pricing"],
};

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.pathname === "/health") {
      return json({ ok: true, service: "gpuwhere-jobs", jobs: Object.keys(JOBS) }, 200, false);
    }

    if (url.pathname === "/" || url.pathname === "") {
      return json({
        service: "gpuwhere-jobs",
        scheduled: scheduleEnabled(env),
        usage: {
          jobs: "GET /jobs (Authorization: Bearer <JOB_TOKEN>)",
          run: "POST /run?job=pricing (Authorization: Bearer <JOB_TOKEN>)",
          schedule: "GET|PUT /schedule (Authorization: Bearer <JOB_TOKEN>)",
        },
        jobs: Object.keys(JOBS),
      }, 200, false);
    }

    if (url.pathname === "/jobs" && request.method === "GET") {
      const denied = authorize(request, env);
      if (denied) return denied;
      return listJobs(env);
    }

    if (url.pathname === "/schedule" && (request.method === "GET" || request.method === "PUT")) {
      const denied = authorize(request, env);
      if (denied) return denied;
      return request.method === "GET" ? getSchedule(env) : putSchedule(request, env);
    }

    if (url.pathname === "/run" && request.method === "POST") {
      const denied = authorize(request, env);
      if (denied) return denied;

      if (env.JOB_RATE_LIMITER && typeof env.JOB_RATE_LIMITER.limit === "function") {
        const ip = request.headers.get("cf-connecting-ip") || "unknown";
        const { success } = await env.JOB_RATE_LIMITER.limit({ key: `run:${ip}` });
        if (success === false) {
          return json({ error: "rate_limited", message: "Try again in a minute." }, 429);
        }
      }

      return runJob(request, env, url);
    }

    return json({ error: "not_found", message: "GET /health, GET /jobs, POST /run, GET|PUT /schedule." }, 404);
  },

  /**
   * Cloudflare cron entry point: once a day at 00:00 UTC. Every configured job
   * runs once per UTC day; a KV guard stops a retried tick from dispatching twice.
   */
  async scheduled(controller, env) {
    if (!scheduleEnabled(env)) return;
    const config = await effectiveSchedule(env);
    if (!config.enabled) return;
    const day = new Date().toISOString().slice(0, 10);
    for (const name of config.jobs) {
      await dispatchOnce(env, name, `guard:${name}:${day}`, 90000);
    }
  },
};

/* ------------------------------------------------------------------ helpers */

function json(body, status = 200, cors = true) {
  const headers = { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" };
  if (cors) headers["access-control-allow-origin"] = "*";
  return new Response(JSON.stringify(body, null, 2) + "\n", { status, headers });
}

function sameSecret(a, b) {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i += 1) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

/** Returns a Response when the request is not authorised, otherwise null. */
function authorize(request, env) {
  const token = String(env.JOB_TOKEN || "").trim();
  if (!token) {
    return json({ error: "not_configured", message: "JOB_TOKEN is not set on this deployment." }, 503);
  }
  const header = request.headers.get("authorization") || "";
  const provided = header.toLowerCase().startsWith("bearer ") ? header.slice(7).trim() : "";
  if (!provided || !sameSecret(token, provided)) {
    return json({ error: "unauthorized", message: "Authorization: Bearer <JOB_TOKEN>." }, 401);
  }
  return null;
}

function github(env, path, init = {}) {
  return fetch(`https://api.github.com/repos/${env.GITHUB_REPO}${path}`, {
    ...init,
    headers: {
      Authorization: `Bearer ${env.GITHUB_TOKEN}`,
      Accept: "application/vnd.github+json",
      "X-GitHub-Api-Version": "2022-11-28",
      "User-Agent": "gpuwhere-jobs",
      "Content-Type": "application/json",
      ...(init.headers || {}),
    },
  });
}

function scheduleEnabled(env) {
  return String(env.SCHEDULE_ENABLED ?? "true").toLowerCase() !== "false";
}

function normalize(raw = {}) {
  const listed = Array.isArray(raw.jobs)
    ? raw.jobs
    : String(raw.jobs ?? DEFAULTS.jobs.join(",")).split(",");
  const jobs = [...new Set(listed.map((name) => String(name).trim()).filter((name) => JOBS[name]))];
  return { enabled: raw.enabled !== false, jobs };
}

async function effectiveSchedule(env) {
  const fromVars = normalize({
    enabled: scheduleEnabled(env),
    jobs: String(env.DAILY_JOBS || DEFAULTS.jobs.join(",")).split(","),
  });
  if (!env.JOBS_CONFIG || typeof env.JOBS_CONFIG.get !== "function") return fromVars;
  try {
    const stored = await env.JOBS_CONFIG.get("schedule", "json");
    if (!stored) return fromVars;
    const merged = normalize({ ...fromVars, ...stored });
    return { ...merged, enabled: scheduleEnabled(env) && merged.enabled };
  } catch (err) {
    return fromVars;
  }
}

async function getSchedule(env) {
  const config = await effectiveSchedule(env);
  return json({
    schedule_enabled: scheduleEnabled(env),
    source: env.JOBS_CONFIG ? "kv" : "vars",
    editable: Boolean(env.JOBS_CONFIG),
    cron: "0 0 * * *",
    timezone: "UTC",
    runs: "daily at 00:00 UTC",
    config,
  });
}

async function putSchedule(request, env) {
  if (!env.JOBS_CONFIG || typeof env.JOBS_CONFIG.put !== "function") {
    return json({
      error: "not_editable",
      message: "Bind JOBS_CONFIG (KV) to change the schedule at runtime; otherwise edit the vars in wrangler.toml and redeploy.",
    }, 409);
  }
  let body;
  try {
    body = await request.json();
  } catch (err) {
    return json({ error: "bad_request", message: "Body must be JSON." }, 400);
  }
  const config = normalize(body);
  await env.JOBS_CONFIG.put("schedule", JSON.stringify(config));
  return json({ saved: true, config });
}

/* --------------------------------------------------------------------- jobs */

async function listJobs(env) {
  if (!env.GITHUB_REPO || !env.GITHUB_TOKEN) {
    return json({ error: "not_configured", message: "GITHUB_REPO and GITHUB_TOKEN are required." }, 503);
  }
  const jobs = await Promise.all(Object.entries(JOBS).map(async ([name, job]) => {
    let latest = null;
    try {
      const res = await github(env, `/actions/workflows/${job.workflow}/runs?per_page=1`);
      if (res.ok) {
        const run = (await res.json()).workflow_runs?.[0];
        if (run) {
          latest = {
            status: run.status,
            conclusion: run.conclusion,
            created_at: run.created_at,
            updated_at: run.updated_at,
            html_url: run.html_url,
          };
        }
      }
    } catch (err) {
      // The list is still useful without GitHub reachability.
    }
    return { name, workflow: job.workflow, summary: job.summary, latest_run: latest };
  }));
  return json({ repo: env.GITHUB_REPO, ref: env.GITHUB_REF || "main", jobs });
}

async function runJob(request, env, url) {
  let body = {};
  try {
    const text = await request.text();
    if (text) body = JSON.parse(text);
  } catch (err) {
    return json({ error: "bad_request", message: "Body must be JSON: {\"job\":\"pricing\"}." }, 400);
  }

  const name = String(body.job || url.searchParams.get("job") || "").trim();
  const job = JOBS[name];
  if (!job) {
    return json({ error: "unknown_job", message: `Job must be one of: ${Object.keys(JOBS).join(", ")}.` }, 400);
  }

  const result = await dispatch(env, name, body.ref || env.GITHUB_REF || "main");
  if (!result.ok) return json(result, 502);

  return json({ dispatched: true, job: name, ...result }, 202);
}

async function dispatch(env, name, ref) {
  const job = JOBS[name];
  const res = await github(env, `/actions/workflows/${job.workflow}/dispatches`, {
    method: "POST",
    body: JSON.stringify({ ref }),
  });
  if (res.status !== 204) {
    const detail = await res.text();
    return {
      ok: false,
      error: "dispatch_failed",
      status: res.status,
      message: detail.slice(0, 500) || "GitHub rejected the dispatch.",
    };
  }
  return {
    ok: true,
    workflow: job.workflow,
    ref,
    run_url: `https://github.com/${env.GITHUB_REPO}/actions/workflows/${job.workflow}`,
  };
}

/** Dispatch at most once per guard key when KV is bound. */
async function dispatchOnce(env, name, guardKey, ttl) {
  if (env.JOBS_CONFIG && typeof env.JOBS_CONFIG.get === "function") {
    try {
      if (await env.JOBS_CONFIG.get(guardKey)) return;
    } catch (err) {
      // Fall through and dispatch; a missed guard is better than a missed run.
    }
  }
  await dispatch(env, name, env.GITHUB_REF || "main");
  if (env.JOBS_CONFIG && typeof env.JOBS_CONFIG.put === "function") {
    try {
      await env.JOBS_CONFIG.put(guardKey, new Date().toISOString(), { expirationTtl: ttl });
    } catch (err) {
      // Best effort.
    }
  }
}
