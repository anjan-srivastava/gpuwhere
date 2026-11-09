/**
 * Jobs Worker tests: auth, on-demand dispatch, configurable schedule.
 *
 *   node --test tests/jobs_worker.test.mjs
 */
import assert from "node:assert/strict";
import test from "node:test";

import worker from "../ops/cloudflare/worker.mjs";

const TOKEN = "job-token";

function env(extra = {}) {
  return {
    JOB_TOKEN: TOKEN,
    GITHUB_REPO: "owner/repo",
    GITHUB_TOKEN: "gh-token",
    GITHUB_REF: "main",
    ...extra,
  };
}

function request(path, { method = "GET", key = TOKEN, body } = {}) {
  const headers = {};
  if (key) headers.authorization = `Bearer ${key}`;
  return new Request(`https://jobs.example.com${path}`, { method, body, headers });
}

function mockGitHub(handler) {
  const calls = [];
  globalThis.fetch = async (url, init = {}) => {
    calls.push({ url: String(url), method: init.method || "GET", body: init.body });
    return handler(String(url), init);
  };
  return calls;
}

test("health is public", async () => {
  const res = await worker.fetch(request("/health", { key: null }), env());
  assert.equal(res.status, 200);
  assert.equal((await res.json()).ok, true);
});

test("management routes require the bearer token", async () => {
  let res = await worker.fetch(request("/jobs", { key: null }), env());
  assert.equal(res.status, 401);
  res = await worker.fetch(request("/run", { method: "POST", key: "wrong" }), env());
  assert.equal(res.status, 401);
  res = await worker.fetch(request("/jobs"), env({ JOB_TOKEN: "" }));
  assert.equal(res.status, 503);
});

test("unknown jobs are rejected before GitHub is called", async () => {
  const calls = mockGitHub(() => new Response("", { status: 204 }));
  const res = await worker.fetch(request("/run", { method: "POST", body: '{"job":"rm"}' }), env());
  assert.equal(res.status, 400);
  assert.equal((await res.json()).error, "unknown_job");
  assert.equal(calls.length, 0);
});

test("on-demand run dispatches the workflow", async () => {
  const calls = mockGitHub(() => new Response(null, { status: 204 }));
  const res = await worker.fetch(request("/run?job=pricing", { method: "POST" }), env());
  assert.equal(res.status, 202);
  const data = await res.json();
  assert.equal(data.dispatched, true);
  assert.equal(data.workflow, "refresh-pricing.yml");
  assert.match(calls[0].url, /actions\/workflows\/refresh-pricing\.yml\/dispatches$/);
  assert.deepEqual(JSON.parse(calls[0].body), { ref: "main" });
});

test("a GitHub failure surfaces as 502", async () => {
  mockGitHub(() => new Response("nope", { status: 403 }));
  const res = await worker.fetch(request("/run?job=pricing", { method: "POST" }), env());
  assert.equal(res.status, 502);
  assert.equal((await res.json()).error, "dispatch_failed");
});

test("JOBS_CONFIG is optional and schedule is readable from vars", async () => {
  const res = await worker.fetch(request("/schedule"), env({
    AVAILABILITY_EVERY_HOURS: "2",
    PRICING_HOUR_UTC: "6",
  }));
  assert.equal(res.status, 200);
  const data = await res.json();
  assert.equal(data.source, "vars");
  assert.equal(data.editable, false);
  assert.equal(data.schedule_enabled, true);
  assert.deepEqual(data.config.availability, { enabled: true, every_hours: 2 });
  assert.deepEqual(data.config.pricing, { enabled: true, hour_utc: 6 });
});

test("PUT /schedule fails clearly without KV", async () => {
  const res = await worker.fetch(request("/schedule", {
    method: "PUT", body: '{"pricing":{"hour_utc":9}}',
  }), env());
  assert.equal(res.status, 409);
  assert.equal((await res.json()).error, "not_editable");
});

test("scheduled ticks dispatch according to the schedule", async () => {
  const hour = new Date().getUTCHours();
  const calls = mockGitHub(() => new Response(null, { status: 204 }));
  await worker.scheduled({}, env({
    PRICING_HOUR_UTC: String(hour),
    AVAILABILITY_EVERY_HOURS: "1",
  }));
  const workflows = calls.map((c) => c.url.split("/workflows/")[1].split("/")[0]);
  assert.deepEqual(workflows.sort(), ["refresh-availability.yml", "refresh-pricing.yml"]);
});

test("SCHEDULE_ENABLED=false leaves the clock off but /run working", async () => {
  let calls = mockGitHub(() => new Response(null, { status: 204 }));
  await worker.scheduled({}, env({ SCHEDULE_ENABLED: "false" }));
  assert.equal(calls.length, 0);

  const res = await worker.fetch(request("/run?job=availability", { method: "POST" }),
    env({ SCHEDULE_ENABLED: "false" }));
  assert.equal(res.status, 202);
});

test("a KV guard prevents a duplicate dispatch in the same window", async () => {
  const store = new Map();
  const kv = {
    async get(key) { return store.get(key) ?? null; },
    async put(key, value) { store.set(key, value); },
  };
  const calls = mockGitHub(() => new Response(null, { status: 204 }));
  const e = env({ PRICING_HOUR_UTC: String(new Date().getUTCHours()), JOBS_CONFIG: kv });

  await worker.scheduled({}, e);
  assert.equal(calls.length, 2);
  await worker.scheduled({}, e);
  assert.equal(calls.length, 2, "second tick must not dispatch again");

  const res = await worker.fetch(request("/schedule"), e);
  assert.equal((await res.json()).source, "kv");
});

test("KV makes the schedule editable at runtime", async () => {
  const store = new Map();
  const kv = {
    async get(key, type) {
      const value = store.get(key) ?? null;
      return type === "json" && value ? JSON.parse(value) : value;
    },
    async put(key, value) { store.set(key, value); },
  };
  const res = await worker.fetch(request("/schedule", {
    method: "PUT", body: '{"availability":{"every_hours":3},"pricing":{"hour_utc":9}}',
  }), env({ JOBS_CONFIG: kv }));
  assert.equal(res.status, 200);
  const data = await res.json();
  assert.equal(data.config.availability.every_hours, 3);
  assert.equal(data.config.pricing.hour_utc, 9);
});
