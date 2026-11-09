/**
 * GPU Where edge worker — Cloudflare Pages advanced mode (`dist/_worker.js`).
 *
 * Three jobs on the same origin:
 *
 *   1. `/api/v1/*`        keyed JSON API over the published catalogue
 *   2. `/api/docs`        HTML reference, `/api/openapi.json` the machine spec
 *   3. `/a`               first-party analytics ingest -> Workers Analytics Engine
 *
 * Everything else falls through to the static site and the open `/v1/*` artifact.
 *
 * Configuration (wrangler.toml): ANALYTICS binding, API_RATE_PER_MIN,
 * PAGE_RATE_PER_MIN, EVENT_RATE_PER_MIN.
 * Secrets: API_KEYS (comma-separated).
 *
 * Rate limits are per Cloudflare location and approximate. They use the Workers
 * Rate Limiting binding when one is bound, and a fixed-window counter in the Cache
 * API otherwise (Pages Functions cannot declare the binding yet). Neither is a
 * billing meter — they exist to damp abuse, not to account precisely.
 */

const API_VERSION = "1";
const EVENT_TYPES = new Set(["pageview", "click", "search"]);

const CORS = {
  "access-control-allow-origin": "*",
  "access-control-allow-methods": "GET, HEAD, OPTIONS",
  "access-control-allow-headers": "Authorization, X-API-Key, Content-Type",
  "access-control-max-age": "86400",
};

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;
    const method = request.method;

    if (method === "OPTIONS") return new Response(null, { status: 204, headers: CORS });

    // Every request, including static pages, passes the page budget first.
    const ip = clientIp(request);
    if (!(await allow(env, ctx, "page", ip, intVar(env.PAGE_RATE_PER_MIN, 300)))) {
      return tooMany("Too many requests. Slow down and retry shortly.");
    }

    if (path === "/a") return handleEvent(request, env, ctx);
    if (path === "/api" || path === "/api/") {
      return Response.redirect(new URL("/api/docs", url).toString(), 302);
    }
    if (path === "/api/docs" || path === "/api/docs/") return serveDocs(request, env);
    if (path === "/api/v1" || path.startsWith("/api/v1/")) return handleApi(request, env, ctx);

    // The UI tries `/api/catalog` only as a local-dev fallback; keep the old path working.
    if (path === "/api/catalog") {
      return Response.redirect(new URL("/v1/catalog.json", url).toString(), 302);
    }

    return env.ASSETS.fetch(request);
  },
};

/* ------------------------------------------------------------------ helpers */

function clientIp(request) {
  return request.headers.get("cf-connecting-ip")
    || (request.headers.get("x-forwarded-for") || "").split(",")[0].trim()
    || "unknown";
}

function intVar(value, fallback) {
  const n = Number.parseInt(value, 10);
  return Number.isFinite(n) && n > 0 ? n : fallback;
}

function cors(extra = {}) {
  return { ...CORS, ...extra };
}

function json(data, status = 200, extra = {}) {
  return new Response(JSON.stringify(data, null, 2) + "\n", {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store",
      "x-api-version": API_VERSION,
      ...cors(),
      ...extra,
    },
  });
}

function tooMany(message) {
  return new Response(message + "\n", {
    status: 429,
    headers: {
      "content-type": "text/plain; charset=utf-8",
      "retry-after": "60",
      ...cors(),
    },
  });
}

async function sha256(value) {
  const bytes = new TextEncoder().encode(value);
  const digest = await crypto.subtle.digest("SHA-256", bytes);
  return [...new Uint8Array(digest)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

function sameSecret(a, b) {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i += 1) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

/* -------------------------------------------------------------- rate limits */

/**
 * Fixed-window limiter. `bucket` separates page/api/event traffic; `key` is the
 * actor (IP or hashed API key). Returns false when the request is over budget.
 */
async function allow(env, ctx, bucket, key, limit) {
  const binding = env[bucket.toUpperCase() + "_RATE_LIMITER"];
  if (binding && typeof binding.limit === "function") {
    try {
      const { success } = await binding.limit({ key: `${bucket}:${key}` });
      return success !== false;
    } catch (err) {
      // A limiter outage must not take the site down.
    }
  }

  if (typeof caches === "undefined" || !caches.default) return true;

  try {
    const period = 60;
    const slot = Math.floor(Date.now() / 1000 / period);
    const cacheKey = new Request(`https://rate.invalid/${bucket}/${slot}/${await sha256(key)}`);
    const cache = caches.default;
    let count = 0;
    const hit = await cache.match(cacheKey);
    if (hit) count = Number.parseInt(await hit.text(), 10) || 0;
    count += 1;
    const write = cache.put(cacheKey, new Response(String(count), {
      headers: { "cache-control": `max-age=${period * 2}` },
    }));
    if (ctx && typeof ctx.waitUntil === "function") ctx.waitUntil(write);
    else await write;
    return count <= limit;
  } catch (err) {
    return true;
  }
}

/* --------------------------------------------------------------------- auth */

async function checkAuth(request, env) {
  const keys = String(env.API_KEYS || "").split(",").map((k) => k.trim()).filter(Boolean);
  const header = request.headers.get("authorization") || "";
  const bearer = header.toLowerCase().startsWith("bearer ") ? header.slice(7).trim() : "";
  const provided = bearer || (request.headers.get("x-api-key") || "").trim();
  if (!keys.length) return { configured: false, ok: false, digest: "unconfigured" };

  const providedHash = await sha256(provided || "anonymous");
  let ok = false;
  for (const key of keys) {
    if (sameSecret(await sha256(key), providedHash)) ok = true;
  }
  return { configured: true, ok, digest: providedHash };
}

/* ---------------------------------------------------------------------- api */

async function handleApi(request, env, ctx) {
  const url = new URL(request.url);
  if (request.method !== "GET" && request.method !== "HEAD") {
    return json({ error: { code: "method_not_allowed", message: "Use GET or HEAD." } }, 405,
      { allow: "GET, HEAD, OPTIONS" });
  }

  const auth = await checkAuth(request, env);
  if (!auth.configured) {
    return json({
      error: { code: "not_configured", message: "The API has no keys configured yet." },
    }, 503);
  }

  const actor = auth.ok ? `key:${auth.digest}` : `ip:${clientIp(request)}`;
  if (!(await allow(env, ctx, "api", actor, intVar(env.API_RATE_PER_MIN, 60)))) {
    return json({ error: { code: "rate_limited", message: "Too many requests for this key." } }, 429,
      { "retry-after": "60" });
  }
  if (!auth.ok) {
    return json({
      error: {
        code: "unauthorized",
        message: "Send a valid key as `Authorization: Bearer <key>` or `X-API-Key: <key>`.",
      },
    }, 401, { "www-authenticate": 'Bearer realm="api"' });
  }

  const endpoint = url.pathname.replace(/^\/api\/v1\/?/, "").replace(/\/$/, "");
  const head = request.method === "HEAD";

  switch (endpoint) {
    case "":
    case "index":
      return apiIndex(request, env, head);
    case "catalog":
      return proxyJson(request, env, "/v1/catalog.json", head);
    case "providers":
      return proxyJson(request, env, "/v1/providers.json", head);
    case "gpus":
      return proxyJson(request, env, "/v1/gpus.json", head);
    case "skus":
      return apiSkus(request, env, head);
    case "availability/latest":
      return apiAvailability(request, env, head);
    default:
      return json({
        error: { code: "not_found", message: `Unknown endpoint /api/v1/${endpoint}.` },
        endpoints: ["index", "catalog", "providers", "gpus", "skus", "availability/latest"],
      }, 404);
  }
}

async function fetchCatalogJson(request, env, path) {
  const url = new URL(request.url);
  const res = await env.ASSETS.fetch(new URL(path, url.origin));
  if (!res.ok) throw new Error(`asset ${path} returned ${res.status}`);
  return res.json();
}

async function proxyJson(request, env, path, head) {
  try {
    const data = await fetchCatalogJson(request, env, path);
    if (head) {
      return new Response(null, {
        status: 200,
        headers: {
          "content-type": "application/json; charset=utf-8",
          "cache-control": "no-store",
          "x-api-version": API_VERSION,
          ...cors(),
        },
      });
    }
    return json(data);
  } catch (err) {
    return json({
      error: { code: "upstream_unavailable", message: "The published artifact is missing; rebuild and redeploy." },
    }, 502);
  }
}

async function apiIndex(request, env, head) {
  let data;
  try {
    data = await fetchCatalogJson(request, env, "/v1/index.json");
  } catch (err) {
    return json({ error: { code: "upstream_unavailable", message: "The published artifact is missing." } }, 502);
  }
  const payload = {
    ...data,
    api_version: API_VERSION,
    authenticated: true,
    api: {
      base: "/api/v1",
      auth: "Authorization: Bearer <key> or X-API-Key: <key>",
      docs: "/api/docs",
      openapi: "/api/openapi.json",
      rate_limit_per_min: intVar(env.API_RATE_PER_MIN, 60),
      endpoints: {
        index: "/api/v1/index",
        catalog: "/api/v1/catalog",
        providers: "/api/v1/providers",
        gpus: "/api/v1/gpus",
        skus: "/api/v1/skus?provider=&region=&gpu=&shape=&variant=&status=",
        availability_latest: "/api/v1/availability/latest?provider=&gpu=&shape=&variant=",
      },
    },
  };
  if (head) return new Response(null, { status: 200, headers: { ...cors() } });
  return json(payload);
}

function filtered(items, url, fields) {
  return (items || []).filter((item) => fields.every((field) => {
    const want = url.searchParams.get(field);
    if (!want) return true;
    return String(item[field] ?? "").toLowerCase() === want.toLowerCase();
  }));
}

async function apiSkus(request, env, head) {
  const url = new URL(request.url);
  const fields = ["provider", "region", "gpu", "shape", "variant", "status", "pricing_status"];
  let data;
  try {
    data = await fetchCatalogJson(request, env, "/v1/skus.json");
  } catch (err) {
    return json({ error: { code: "upstream_unavailable", message: "The published artifact is missing." } }, 502);
  }
  const skus = filtered(data.skus, url, fields);
  if (head) return new Response(null, { status: 200, headers: { ...cors() } });
  return json({
    api_version: API_VERSION,
    schema_version: data.schema_version,
    generated_at: data.generated_at,
    count: skus.length,
    filters: Object.fromEntries(fields.map((f) => [f, url.searchParams.get(f)]).filter(([, v]) => v)),
    skus,
  });
}

async function apiAvailability(request, env, head) {
  const url = new URL(request.url);
  const fields = ["provider", "region", "gpu", "shape", "variant"];
  let data;
  try {
    data = await fetchCatalogJson(request, env, "/v1/availability/latest.json");
  } catch (err) {
    return json({ error: { code: "upstream_unavailable", message: "The published artifact is missing." } }, 502);
  }
  const observations = filtered(data.observations, url, fields);
  if (head) return new Response(null, { status: 200, headers: { ...cors() } });
  return json({
    api_version: API_VERSION,
    schema_version: data.schema_version,
    generated_at: data.generated_at,
    count: observations.length,
    observations,
  });
}

async function serveDocs(request, env) {
  const url = new URL(request.url);
  const res = await env.ASSETS.fetch(new URL("/api/docs/index.html", url.origin));
  const headers = new Headers(res.headers);
  headers.set("cache-control", "public, max-age=300");
  headers.set("x-content-type-options", "nosniff");
  return new Response(res.body, { status: res.status, headers });
}

/* ---------------------------------------------------------------- analytics */

function clean(value, max) {
  if (typeof value !== "string") return "";
  return value.replace(/[\u0000-\u001f\u007f]/g, "").trim().slice(0, max);
}

function referrerHost(value) {
  try {
    return new URL(value).hostname.slice(0, 120);
  } catch (err) {
    return "";
  }
}

function clickTarget(value) {
  const raw = clean(value, 400);
  if (!raw) return "";
  if (raw.startsWith("#/")) return raw.slice(0, 200);
  try {
    const u = new URL(raw);
    if (u.protocol !== "http:" && u.protocol !== "https:") return "";
    return (u.hostname + u.pathname).slice(0, 200);
  } catch (err) {
    return "";
  }
}

async function handleEvent(request, env, ctx) {
  if (request.method !== "POST") {
    return new Response("POST only\n", {
      status: 405,
      headers: { allow: "POST, OPTIONS", "content-type": "text/plain; charset=utf-8", ...cors() },
    });
  }

  if (!(await allow(env, ctx, "event", clientIp(request), intVar(env.EVENT_RATE_PER_MIN, 120)))) {
    return new Response(null, { status: 429, headers: { "retry-after": "60", ...cors() } });
  }

  const body = await request.text();
  if (!body || body.length > 4096) return new Response(null, { status: 204, headers: cors() });

  let event;
  try {
    event = JSON.parse(body);
  } catch (err) {
    return new Response(null, { status: 204, headers: cors() });
  }
  if (!event || !EVENT_TYPES.has(event.e)) return new Response(null, { status: 204, headers: cors() });

  const session = clean(event.s, 96) || "anonymous";
  if (env.ANALYTICS && typeof env.ANALYTICS.writeDataPoint === "function") {
    env.ANALYTICS.writeDataPoint({
      indexes: [session],
      // Keep this order in sync with scripts/analytics_report.py.
      blobs: [
        event.e,
        clean(event.p, 200) || "/",
        clean(event.l, 120),
        clickTarget(event.t),
        referrerHost(event.r),
        clean(request.cf && request.cf.country, 2),
      ],
      doubles: [1],
    });
  }
  return new Response(null, { status: 204, headers: cors() });
}
