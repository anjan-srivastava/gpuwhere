/**
 * Edge worker tests: auth, filtering, rate limits and analytics ingest.
 *
 *   node --test tests/worker.test.mjs
 */
import assert from "node:assert/strict";
import test from "node:test";

import worker from "../server/api_worker.mjs";

const KEY = "test-key";

function assets(extra = {}) {
  const files = {
    "/v1/index.json": {
      schema_version: "1",
      generated_at: "2026-11-09T00:00:00Z",
      counts: { providers: 2, skus: 2 },
      resources: {},
    },
    "/v1/skus.json": {
      schema_version: "1",
      generated_at: "2026-11-09T00:00:00Z",
      skus: [
        { provider: "e2e-networks", region: "IN-DEL", gpu: "H100", shape: "8x", status: "active" },
        { provider: "jarvislabs", region: "IN-EU", gpu: "A100", shape: "1x", status: "active" },
      ],
    },
    "/v1/availability/latest.json": {
      schema_version: "1",
      generated_at: "2026-11-09T00:00:00Z",
      observations: [
        { provider: "e2e-networks", gpu: "H100", shape: "8x", available_gpus: 0 },
        { provider: "jarvislabs", gpu: "A100", shape: "1x", available_gpus: 2 },
      ],
    },
    "/api/docs/index.html": "<!doctype html><p>/api/v1/skus</p>",
    ...extra,
  };
  return {
    async fetch(input) {
      const url = String(input.url ?? input);
      const path = new URL(url).pathname;
      if (!Object.hasOwn(files, path)) return new Response("not found", { status: 404 });
      const body = typeof files[path] === "string" ? files[path] : JSON.stringify(files[path]);
      const type = typeof files[path] === "string" ? "text/html" : "application/json";
      return new Response(body, { status: 200, headers: { "content-type": type } });
    },
  };
}

const okLimiter = { async limit() { return { success: true }; } };
const ctx = { waitUntil() {} };

function env(extra = {}) {
  return {
    API_KEYS: KEY,
    ASSETS: assets(),
    PAGE_RATE_LIMITER: okLimiter,
    API_RATE_LIMITER: okLimiter,
    EVENT_RATE_LIMITER: okLimiter,
    ...extra,
  };
}

function get(path, { key = KEY, method = "GET", body, environment = env(), headers = {} } = {}) {
  const h = { "cf-connecting-ip": "203.0.113.9", ...headers };
  if (key) h.authorization = `Bearer ${key}`;
  return worker.fetch(new Request(`https://gpuwhere.io${path}`, { method, body, headers: h }), environment, ctx);
}

test("no configured keys fails closed with 503", async () => {
  const res = await get("/api/v1/index", { environment: env({ API_KEYS: "" }) });
  assert.equal(res.status, 503);
  assert.equal((await res.json()).error.code, "not_configured");
});

test("missing and wrong keys are 401", async () => {
  let res = await get("/api/v1/index", { key: null });
  assert.equal(res.status, 401);
  assert.equal((await res.json()).error.code, "unauthorized");
  res = await get("/api/v1/index", { key: "wrong" });
  assert.equal(res.status, 401);
});

test("bearer and X-API-Key are both accepted", async () => {
  let res = await get("/api/v1/index");
  assert.equal(res.status, 200);
  assert.equal((await res.json()).api.base, "/api/v1");

  res = await get("/api/v1/index", {
    key: null,
    headers: { "x-api-key": KEY },
  });
  assert.equal(res.status, 200);
});

test("sku filters are exact and case-insensitive", async () => {
  const res = await get("/api/v1/skus?gpu=h100&provider=e2e-networks");
  assert.equal(res.status, 200);
  const data = await res.json();
  assert.equal(data.count, 1);
  assert.equal(data.skus[0].provider, "e2e-networks");
  assert.equal(data.filters.gpu, "h100");
});

test("availability filters work", async () => {
  const res = await get("/api/v1/availability/latest?provider=jarvislabs");
  const data = await res.json();
  assert.equal(data.count, 1);
  assert.equal(data.observations[0].available_gpus, 2);
});

test("unknown endpoints are 404 with the endpoint list", async () => {
  const res = await get("/api/v1/nope");
  assert.equal(res.status, 404);
  const data = await res.json();
  assert.equal(data.error.code, "not_found");
  assert.ok(data.endpoints.includes("skus"));
});

test("docs are public", async () => {
  const res = await get("/api/docs", { key: null });
  assert.equal(res.status, 200);
  assert.match(await res.text(), /\/api\/v1\/skus/);
});

test("non-GET API methods are 405", async () => {
  const res = await get("/api/v1/index", { method: "POST" });
  assert.equal(res.status, 405);
  assert.equal((await res.json()).error.code, "method_not_allowed");
});

test("OPTIONS answers CORS preflight", async () => {
  const res = await get("/api/v1/index", { key: null, method: "OPTIONS" });
  assert.equal(res.status, 204);
  assert.equal(res.headers.get("access-control-allow-origin"), "*");
});

test("HEAD returns headers without a body", async () => {
  const res = await get("/api/v1/index", { method: "HEAD" });
  assert.equal(res.status, 200);
  assert.equal(await res.text(), "");
});

test("over-budget API calls are 429", async () => {
  const res = await get("/api/v1/index", {
    environment: env({ API_RATE_LIMITER: { async limit() { return { success: false }; } } }),
  });
  assert.equal(res.status, 429);
  assert.equal((await res.json()).error.code, "rate_limited");
});

test("pages share the same limiter and get 429", async () => {
  const res = await get("/", {
    environment: env({ PAGE_RATE_LIMITER: { async limit() { return { success: false }; } } }),
  });
  assert.equal(res.status, 429);
  assert.equal(res.headers.get("retry-after"), "60");
});

test("pageviews and clicks reach Analytics Engine in a fixed blob order", async () => {
  const analytics = { points: [], writeDataPoint(point) { this.points.push(point); } };
  const environment = env({ ANALYTICS: analytics });

  let res = await get("/a", {
    key: null,
    method: "POST",
    environment,
    body: JSON.stringify({
      e: "click", s: "session-1", p: "#/gpu/nvidia/h100",
      l: "E2E Networks", t: "https://www.e2enetworks.com/gpu?ref=x",
      r: "https://news.ycombinator.com/item?id=1",
    }),
    headers: { "content-type": "text/plain;charset=UTF-8" },
  });
  assert.equal(res.status, 204);

  res = await get("/a", {
    key: null,
    method: "POST",
    environment,
    body: JSON.stringify({ e: "pageview", s: "session-1", p: "#/providers" }),
  });
  assert.equal(res.status, 204);

  assert.equal(analytics.points.length, 2);
  assert.deepEqual(analytics.points[0].blobs, [
    "click", "#/gpu/nvidia/h100", "E2E Networks",
    "www.e2enetworks.com/gpu", "news.ycombinator.com", "",
  ]);
  assert.deepEqual(analytics.points[1].blobs.slice(0, 2), ["pageview", "#/providers"]);
  assert.deepEqual(analytics.points[0].indexes, ["session-1"]);
});

test("invalid events are dropped silently", async () => {
  const analytics = { points: [], writeDataPoint(point) { this.points.push(point); } };
  const res = await get("/a", {
    key: null,
    method: "POST",
    environment: env({ ANALYTICS: analytics }),
    body: '{"e":"drop-table"}',
  });
  assert.equal(res.status, 204);
  assert.equal(analytics.points.length, 0);
});
