#!/usr/bin/env python3
"""Serve the GPU provider catalog over HTTP.

Usage:
    python scripts/serve_catalog.py --data-dir data --assets-dir assets --port 8080

Routes:
    GET /                        GPUs tab / Providers tab / GPU detail / provider detail
    GET /api/docs                API reference (same page as production)
    GET /api/openapi.json        OpenAPI 3.1 spec
    GET /api/v1/*                keyed API (API_KEYS; open when unset in dev)
    POST /a                      analytics beacon sink (dev log)
    GET /api/catalog             providers + accelerator SKUs + host packages + channels + capacities
    GET /api/keys                availability series keys
    GET /api/availability        filtered availability time series
    GET /assets/logos/<id>.png   provider logos
"""
from __future__ import annotations
from datetime import datetime, timedelta, timezone

import argparse
import hashlib
import hmac
import json
import os
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SERVER_DIR = os.path.join(ROOT, "server")


def _load_json_dir(path: str) -> list[dict]:
    out: list[dict] = []
    if not os.path.isdir(path):
        return out
    for fn in sorted(os.listdir(path)):
        if fn.endswith(".json"):
            with open(os.path.join(path, fn), "r", encoding="utf-8") as fh:
                out.append(json.load(fh))
    return out


def _load_skus(root: str) -> list[dict]:
    out: list[dict] = []
    base = os.path.join(root, "skus")
    for dirpath, _, filenames in os.walk(base):
        for fn in filenames:
            if fn.endswith(".json"):
                with open(os.path.join(dirpath, fn), "r", encoding="utf-8") as fh:
                    sku = json.load(fh)
                # Retired packages stay on disk for audit but are not offered.
                if sku.get("status") != "retired":
                    out.append(sku)
    return out


def _load_gpus(root: str) -> list[dict]:
    out: list[dict] = []
    base = os.path.join(root, "gpus")
    for dirpath, _, filenames in os.walk(base):
        for fn in sorted(filenames):
            if not fn.endswith(".json"):
                continue
            with open(os.path.join(dirpath, fn), "r", encoding="utf-8") as fh:
                out.append(json.load(fh))
    return out


def _load_availability(root: str) -> list[dict]:
    out: list[dict] = []
    base = os.path.join(root, "availability")
    if not os.path.isdir(base):
        return out
    for fn in sorted(os.listdir(base)):
        if not fn.endswith(".jsonl"):
            continue
        with open(os.path.join(base, fn), "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    out.sort(key=lambda r: r.get("ts", ""))
    return out


def _norm_variant(v) -> str:
    return "" if v in (None, "", "standard") else str(v)


# Availability is append-only, so older rows can carry a GPU name that predates the
# accelerator catalogue's spelling. Normalise when joining; never rewrite history.
GPU_KEY_ALIASES = {"RTX-PRO6000": "RTX PRO 6000"}


def _norm_gpu(gpu: str | None) -> str | None:
    if gpu is None:
        return None
    g = gpu.strip()
    return GPU_KEY_ALIASES.get(g, g)


def _latest_availability(rows: list[dict]) -> dict:
    latest: dict[tuple, dict] = {}
    for r in rows:
        key = (r.get("provider"), r.get("region"), _norm_gpu(r.get("gpu")), r.get("shape"), _norm_variant(r.get("variant")))
        cur = latest.get(key)
        if cur is None or r.get("ts", "") > cur.get("ts", ""):
            latest[key] = r
    # A series missing from a provider's newest snapshot is no longer reported
    # (e.g. renamed GPU keys); keep it in history but not as "live".
    newest: dict[str, datetime] = {}
    for r in latest.values():
        t = _parse_ts(r.get("ts"))
        if t and (r.get("provider") not in newest or t > newest[r.get("provider")]):
            newest[r.get("provider")] = t
    return {k: r for k, r in latest.items()
            if (t := _parse_ts(r.get("ts"))) and newest[r.get("provider")] - t <= timedelta(hours=2)}


def _parse_ts(ts: str | None) -> datetime | None:
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00")) if ts else None
    except ValueError:
        return None


def _api_keys() -> list[str]:
    return [k.strip() for k in os.environ.get("API_KEYS", "").split(",") if k.strip()]


def _render_api_docs() -> str:
    with open(os.path.join(SERVER_DIR, "api_docs.html"), encoding="utf-8") as fh:
        template = fh.read()
    return (template.replace("__SITE_NAME__", SITE_NAME)
                    .replace("__SITE_DOMAIN__", SITE_DOMAIN)
                    .replace("__REPO_LINK__", docs_repo_link()))


def _clean(value, max_len: int) -> str:
    if not isinstance(value, str):
        return ""
    return "".join(ch for ch in value if ch >= " " and ch != "\x7f").strip()[:max_len]


def _filter(items: list[dict], query: dict, fields: tuple[str, ...]) -> list[dict]:
    def want(name: str):
        values = query.get(name) or [None]
        return values[0].lower() if values[0] else None

    wanted = {field: want(field) for field in fields}
    return [item for item in items
            if all(not value or str(item.get(field) or "").lower() == value
                   for field, value in wanted.items())]


class Handler(BaseHTTPRequestHandler):
    data_root = "data"
    assets_dir = "assets"
    dist_dir = "dist"

    def _send(self, body: bytes, content_type: str, code: int = 200, *, cache: str = "no-store",
              extra: dict[str, str] | None = None) -> None:
        etag = '"' + hashlib.sha1(body).hexdigest()[:16] + '"'
        if code == 200 and self.headers.get("If-None-Match") == etag:
            self.send_response(304)
            self.send_header("ETag", etag)
            self.send_header("Cache-Control", cache)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            return
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("ETag", etag)
        self.send_header("Cache-Control", cache)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, HEAD, OPTIONS")
        for key, value in (extra or {}).items():
            self.send_header(key, value)
        self.end_headers()
        if not getattr(self, "_head", False):
            self.wfile.write(body)

    def do_HEAD(self) -> None:  # noqa: N802
        self._head = True
        self.do_GET()

    def do_OPTIONS(self) -> None:  # noqa: N802
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, HEAD, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Authorization, X-API-Key, Content-Type, If-None-Match")
        self.send_header("Access-Control-Max-Age", "86400")
        self.end_headers()

    _rate: dict[tuple[str, str, int], int] = {}

    def _client_ip(self) -> str:
        return (self.headers.get("CF-Connecting-IP")
                or self.headers.get("X-Forwarded-For", "").split(",")[0].strip()
                or (self.client_address[0] if self.client_address else "unknown"))

    def _allow(self, bucket: str, key: str, limit: int, period: int = 60) -> bool:
        """Fixed-window limiter mirroring the edge worker (approximate, per process)."""
        slot = int(time.time() // period)
        cache_key = (bucket, key, slot)
        count = self._rate.get(cache_key, 0) + 1
        self._rate[cache_key] = count
        if len(self._rate) > 5000:
            self._rate = {k: v for k, v in self._rate.items() if k[2] >= slot - 1}
        return count <= limit

    def _api_auth(self) -> tuple[bool, str]:
        keys = _api_keys()
        if not keys:
            return True, "dev-open"
        header = self.headers.get("Authorization", "")
        provided = header[7:].strip() if header.lower().startswith("bearer ") else ""
        provided = provided or (self.headers.get("X-API-Key") or "").strip()
        ok = any(hmac.compare_digest(key, provided) for key in keys)
        return ok, (provided or "anonymous")

    def _json(self, obj, code: int = 200, extra: dict[str, str] | None = None) -> None:
        self._send(json.dumps(obj).encode("utf-8"), "application/json", code, extra=extra)

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)

        if not self._allow("page", self._client_ip(), int(os.environ.get("PAGE_RATE_PER_MIN", "300"))):
            self._send(b"Too many requests\n", "text/plain; charset=utf-8", 429,
                       extra={"Retry-After": "60"})
            return

        if parsed.path in ("/api", "/api/"):
            self.send_response(302)
            self.send_header("Location", "/api/docs")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            return

        if parsed.path in ("/api/docs", "/api/docs/"):
            self._send(_render_api_docs().encode("utf-8"), "text/html; charset=utf-8",
                       cache="public, max-age=300")
            return

        if parsed.path == "/api/openapi.json":
            with open(os.path.join(SERVER_DIR, "openapi.json"), "rb") as fh:
                self._send(fh.read(), "application/json", cache="public, max-age=300")
            return

        if parsed.path == "/api/v1" or parsed.path.startswith("/api/v1/"):
            self._handle_api(parsed)
            return

        # Published artifact (Cloudflare Pages layout): serve it when an export exists.
        if parsed.path.startswith("/v1/"):
            root = os.path.abspath(self.dist_dir)
            full = os.path.abspath(os.path.join(root, parsed.path.lstrip("/")))
            if not full.startswith(root + os.sep) or not os.path.isfile(full):
                self._json({"error": "not found", "hint": "run scripts/export_api.py"}, 404)
                return
            ctype = "application/json" if full.endswith(".json") else "application/octet-stream"
            with open(full, "rb") as fh:
                self._send(fh.read(), ctype, cache="public, max-age=300, must-revalidate")
            return

        if parsed.path.startswith("/assets/"):
            rel = parsed.path[len("/assets/"):]
            root = os.path.abspath(self.assets_dir)
            full = os.path.abspath(os.path.join(root, rel))
            if not full.startswith(root + os.sep) or not os.path.isfile(full):
                self._json({"error": "not found"}, 404)
                return
            ext = os.path.splitext(full)[1].lower()
            ctype = {
                ".png": "image/png", ".svg": "image/svg+xml", ".jpg": "image/jpeg",
                ".jpeg": "image/jpeg", ".webp": "image/webp", ".ico": "image/x-icon",
            }.get(ext, "application/octet-stream")
            with open(full, "rb") as fh:
                self._send(fh.read(), ctype)
            return

        providers = _load_json_dir(os.path.join(self.data_root, "providers"))
        skus = _load_skus(self.data_root)
        availability = _load_availability(self.data_root)
        channels = _load_json_dir(os.path.join(self.data_root, "channels"))
        capacities = _load_json_dir(os.path.join(self.data_root, "capacity"))
        inventory = {r.get("provider"): r for r in _load_json_dir(os.path.join(self.data_root, "inventory"))}
        gpus = _load_gpus(self.data_root)
        latest = _latest_availability(availability)

        if parsed.path in ("/", "/index.html"):
            self._send(HTML.encode("utf-8"), "text/html; charset=utf-8")
            return

        if parsed.path == "/api/catalog":
            enriched = []
            for s in skus:
                key = (s.get("provider"), s.get("region"), s.get("gpu"), s.get("shape"), _norm_variant(s.get("variant")))
                s = dict(s)
                s["latest_availability"] = latest.get(key)
                enriched.append(s)
            self._json({
                "providers": [dict(p, inventory_check=inventory.get(p.get("id"))) for p in providers],
                "skus": enriched,
                "channels": channels,
                "capacities": capacities,
                "gpus": gpus,
                "latest_availability": list(latest.values()),
                "counts": {
                    "providers": len(providers),
                    "skus": len(skus),
                    "channels": len(channels),
                    "capacities": len(capacities),
                    "gpus": len(gpus),
                    "accelerator_variants": sum(len(g.get("variants", [])) for g in gpus),
                    "availability_observations": len(availability),
                },
            })
            return

        if parsed.path == "/api/keys":
            keys = sorted({
                (r.get("provider", ""), r.get("region", ""), r.get("gpu", ""), r.get("shape", ""), r.get("variant") or "")
                for r in availability
            })
            self._json([
                {"provider": k[0], "region": k[1], "gpu": k[2], "shape": k[3], "variant": k[4]}
                for k in keys
            ])
            return

        if parsed.path == "/api/availability":
            q = parse_qs(parsed.query)

            def one(name: str):
                return q.get(name, [None])[0]

            provider = one("provider")
            region = one("region")
            gpu = one("gpu")
            shape = one("shape")
            variant = one("variant")

            out = [
                r for r in availability
                if (not provider or r.get("provider") == provider)
                and (not region or r.get("region") == region)
                and (not gpu or r.get("gpu") == gpu)
                and (not shape or r.get("shape") == shape)
                and (not variant or (r.get("variant") or "") == variant)
            ]
            self._json(out)
            return

        self._json({"error": "not found"}, 404)

    def _handle_api(self, parsed) -> None:
        ok, actor = self._api_auth()
        limit = int(os.environ.get("API_RATE_PER_MIN", "60"))
        if not self._allow("api", actor if ok else self._client_ip(), limit):
            self._json({"error": {"code": "rate_limited", "message": "Too many requests for this key."}},
                       429, {"Retry-After": "60"})
            return
        if not ok:
            self._json({"error": {"code": "unauthorized",
                                  "message": "Send a valid key as `Authorization: Bearer <key>` or `X-API-Key: <key>`."}},
                       401, {"WWW-Authenticate": 'Bearer realm="api"'})
            return

        sys.path.insert(0, HERE)
        import export_api  # local import: export_api imports this module

        catalog, split = export_api.build(Path(self.data_root))
        endpoint = parsed.path[len("/api/v1"):].strip("/") or "index"
        query = parse_qs(parsed.query)

        if endpoint == "index":
            schemas = sorted(p.name for p in (Path(ROOT) / "schema").glob("*.json"))
            self._json({
                "schema_version": catalog["schema_version"],
                "generated_at": catalog["generated_at"],
                "counts": catalog["counts"],
                "resources": {
                    "catalog": "/v1/catalog.json",
                    "providers": "/v1/providers.json",
                    "gpus": "/v1/gpus.json",
                    "skus": "/v1/skus.json",
                    "availability_latest": "/v1/availability/latest.json",
                    "schemas": [f"/v1/schema/{name}" for name in schemas],
                    "api_docs": "/api/docs",
                    "openapi": "/api/openapi.json",
                },
                "api_version": 1,
                "authenticated": True,
                "api": {
                    "base": "/api/v1",
                    "docs": "/api/docs",
                    "openapi": "/api/openapi.json",
                    "rate_limit_per_min": limit,
                    "endpoints": {
                        "index": "/api/v1/index",
                        "catalog": "/api/v1/catalog",
                        "providers": "/api/v1/providers",
                        "gpus": "/api/v1/gpus",
                        "skus": "/api/v1/skus?provider=&region=&gpu=&shape=&variant=&status=",
                        "availability_latest": "/api/v1/availability/latest?provider=&gpu=&shape=&variant=",
                    },
                },
            })
            return

        if endpoint == "catalog":
            self._json(catalog)
            return
        if endpoint in ("providers", "gpus"):
            self._json(split[endpoint])
            return
        if endpoint == "skus":
            fields = ("provider", "region", "gpu", "shape", "variant", "status", "pricing_status")
            skus = _filter(split["skus"]["skus"], query, fields)
            self._json({
                "api_version": 1,
                "schema_version": split["skus"]["schema_version"],
                "generated_at": split["skus"]["generated_at"],
                "count": len(skus),
                "filters": {f: query.get(f, [""])[0] for f in fields if query.get(f, [""])[0]},
                "skus": skus,
            })
            return
        if endpoint == "availability/latest":
            fields = ("provider", "region", "gpu", "shape", "variant")
            observations = _filter(split["availability/latest"]["observations"], query, fields)
            self._json({
                "api_version": 1,
                "schema_version": split["availability/latest"]["schema_version"],
                "generated_at": split["availability/latest"]["generated_at"],
                "count": len(observations),
                "observations": observations,
            })
            return

        self._json({"error": {"code": "not_found", "message": f"Unknown endpoint /api/v1/{endpoint}."},
                    "endpoints": ["index", "catalog", "providers", "gpus", "skus", "availability/latest"]},
                   404)

    def do_POST(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path != "/a":
            self._json({"error": "not found"}, 404)
            return
        if not self._allow("event", self._client_ip(), int(os.environ.get("EVENT_RATE_PER_MIN", "120"))):
            self._send(b"", "text/plain; charset=utf-8", 429, extra={"Retry-After": "60"})
            return
        try:
            length = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            length = 0
        if length <= 0 or length > 4096:
            self._send(b"", "text/plain; charset=utf-8", 204)
            return
        try:
            event = json.loads(self.rfile.read(length))
        except (ValueError, UnicodeDecodeError):
            self._send(b"", "text/plain; charset=utf-8", 204)
            return
        if not isinstance(event, dict) or event.get("e") not in ("pageview", "click", "search"):
            self._send(b"", "text/plain; charset=utf-8", 204)
            return

        target = _clean(event.get("t"), 400)
        if target and not target.startswith("#/"):
            try:
                parsed_target = urlparse(target)
                target = ((parsed_target.hostname or "") + (parsed_target.path or "")
                          if parsed_target.scheme in ("http", "https") else "")
            except ValueError:
                target = ""
        try:
            referrer = (urlparse(str(event.get("r") or "")).hostname or "")[:120]
        except ValueError:
            referrer = ""

        row = {
            "ts": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
            "e": event["e"],
            "p": _clean(event.get("p"), 200) or "/",
            "l": _clean(event.get("l"), 120),
            "t": target[:200],
            "r": referrer,
            "country": (self.headers.get("CF-IPCountry") or "")[:2],
            "s": _clean(event.get("s"), 96),
        }
        log_path = os.environ.get("DEV_ANALYTICS_LOG") or os.path.join(ROOT, ".cache", "dev-analytics.jsonl")
        os.makedirs(os.path.dirname(log_path) or ".", exist_ok=True)
        with open(log_path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(row) + "\n")
        self._send(b"", "text/plain; charset=utf-8", 204)

    def log_message(self, fmt: str, *args) -> None:
        pass


HTML_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>__SITE_NAME__ — __SITE_TAGLINE__</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Rubik:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    /* ink: --strong for key numbers/titles, --fg body, --muted secondary, --faint placeholders */
    --bg: #fbfaf7; --card: #ffffff; --strong: #141414; --fg: #34322e; --muted: #6d6a64; --faint: #a6a29a;
    --line: #e2dfd8; --line-soft: #ece9e3; --soft: #f3f1ec; --hover: #f6f4ef;
    /* accent = interaction + the single headline price on a detail page; nothing else */
    --accent: #d9480f; --accent-soft: #fff1ea;
    /* semantic: ok = available/high, warn = medium/derived/quote, bad = sold out/low/zero */
    --ok: #0f7b4d; --ok-soft: #e8f5ee; --warn: #a15c07; --warn-soft: #fdf3e3;
    --bad: #b42318; --bad-soft: #fdecea; --info: #1d4ed8; --info-soft: #eaf0fe;
    --font: "Rubik", ui-sans-serif, system-ui, -apple-system, sans-serif;
    --mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --bg: #111214; --card: #16171a; --strong: #f4f4f5; --fg: #d4d4d8; --muted: #9a9aa3; --faint: #6b6b73;
      --line: #2a2b30; --line-soft: #222328; --soft: #1d1e22; --hover: #18191c;
      --accent: #ff7a3d; --accent-soft: #2a1a12;
      --ok: #34c77b; --ok-soft: #12261b; --warn: #f0a23b; --warn-soft: #2a2010;
      --bad: #f2685c; --bad-soft: #2c1513; --info: #7aa2ff; --info-soft: #151d33;
    }
  }
  :root[data-theme="dark"] {
    --bg: #111214; --card: #16171a; --strong: #f4f4f5; --fg: #d4d4d8; --muted: #9a9aa3; --faint: #6b6b73;
    --line: #2a2b30; --line-soft: #222328; --soft: #1d1e22; --hover: #18191c;
    --accent: #ff7a3d; --accent-soft: #2a1a12;
    --ok: #34c77b; --ok-soft: #12261b; --warn: #f0a23b; --warn-soft: #2a2010;
    --bad: #f2685c; --bad-soft: #2c1513; --info: #7aa2ff; --info-soft: #151d33;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; background: var(--bg); color: var(--fg); }
  body { font-family: var(--font); font-size: 14px; line-height: 1.5; -webkit-font-smoothing: antialiased; }
  a { color: inherit; text-decoration: none; }
  .wrap { max-width: 1200px; margin: 0 auto; padding: 0 32px; }
  header { position: sticky; top: 0; z-index: 20; background: color-mix(in srgb, var(--bg) 92%, transparent); backdrop-filter: saturate(1.2) blur(8px); border-bottom: 1px solid var(--line-soft); }
  .theme-btn { width: 32px; height: 32px; display: inline-flex; align-items: center; justify-content: center; border: 1px solid var(--line); border-radius: 6px; background: var(--card); color: var(--muted); cursor: pointer; font-size: 14px; }
  .theme-btn:hover { color: var(--strong); border-color: var(--faint); }
  .gh-btn { width: 32px; height: 32px; display: inline-flex; align-items: center; justify-content: center; border: 1px solid var(--line); border-radius: 6px; background: var(--card); color: var(--muted); }
  .gh-btn:hover { color: var(--strong); border-color: var(--faint); }
  .gh-btn svg { width: 16px; height: 16px; }
  .api-btn { height: 32px; display: inline-flex; align-items: center; padding: 0 9px; border: 1px solid var(--line); border-radius: 6px; background: var(--card); color: var(--muted); font: 500 11px/1 var(--mono); letter-spacing: .08em; }
  .api-btn:hover { color: var(--strong); border-color: var(--faint); }
  .bar { display: flex; align-items: center; gap: 16px; height: 56px; }
  .brand { display: flex; align-items: baseline; gap: 6px; font-size: 15px; white-space: nowrap; }
  .brand b { font-weight: 600; letter-spacing: .02em; }
  .brand .slash, .brand .tagline { color: var(--muted); font-weight: 400; }
  .tabs { display: flex; gap: 2px; }
  .tabs button { background: none; border: 0; padding: 6px 8px; border-radius: 4px; font: inherit; font-size: 13px; color: var(--muted); cursor: pointer; }
  .tabs button:hover { color: var(--fg); background: var(--soft); }
  .tabs button.active { color: var(--strong); background: var(--soft); font-weight: 500; box-shadow: inset 0 -2px 0 var(--accent); border-radius: 4px 4px 0 0; }
  .grow { flex: 1; }
  .search-trigger { display: flex; align-items: center; gap: 8px; width: 280px; height: 34px; padding: 0 6px 0 10px; font: inherit; font-size: 13px; color: var(--faint); background: var(--bg); border: 1px solid var(--line); border-radius: 4px; cursor: text; text-align: left; transition: border-color .12s, box-shadow .12s; }
  .search-trigger:hover { border-color: var(--faint); }
  .search-trigger:focus-visible { outline: none; border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
  .search-trigger svg { width: 14px; height: 14px; color: var(--muted); flex: none; }
  .search-trigger span { flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .kbd { font-family: var(--mono); font-size: 10px; color: var(--faint); border: 1px solid var(--line); border-radius: 3px; padding: 1px 4px; background: var(--bg); line-height: 1.4; }
  .count { color: var(--muted); font-size: 12px; white-space: nowrap; }
  main.wrap { padding: 40px 32px 64px; }
  .toolbar { display: flex; gap: 10px; align-items: center; flex-wrap: wrap; }
  .filters { display: flex; flex-wrap: wrap; gap: 8px 14px; align-items: center; margin: -12px 0 18px; padding-bottom: 14px; border-bottom: 1px solid var(--line-soft); }
  .fgroup { display: inline-flex; align-items: center; gap: 6px; }
  .flabel { font-size: 11px; color: var(--muted); text-transform: uppercase; letter-spacing: .05em; }
  .seg { display: inline-flex; border: 1px solid var(--line); border-radius: 5px; overflow: hidden; }
  .seg button { font: inherit; font-size: 12px; padding: 4px 9px; background: var(--bg); color: var(--muted); border: 0; border-right: 1px solid var(--line); cursor: pointer; }
  .seg button:last-child { border-right: 0; }
  .seg button:hover { color: var(--strong); background: var(--soft); }
  .seg button.on { color: var(--strong); background: var(--soft); font-weight: 600; box-shadow: inset 0 -2px 0 var(--accent); }
  .fchip { font: inherit; font-size: 12px; padding: 3px 9px; border: 1px solid var(--line); border-radius: 999px; background: var(--bg); color: var(--muted); cursor: pointer; }
  .fchip:hover { color: var(--strong); border-color: var(--faint); }
  .fchip.on { color: var(--accent); border-color: var(--accent); background: var(--accent-soft); font-weight: 500; }
  .filters select { font-size: 12px; padding: 4px 6px; }
  .filters select.on { border-color: var(--accent); color: var(--accent); }
  .fmeta { margin-left: auto; display: inline-flex; gap: 10px; align-items: center; font-size: 12px; color: var(--muted); }
  .fclear { font: inherit; font-size: 12px; color: var(--accent); background: none; border: 0; cursor: pointer; padding: 0; }
  .fmore-wrap { position: relative; }
  .fmore { font: inherit; font-size: 12px; padding: 4px 10px; border: 1px solid var(--line); border-radius: 5px; background: var(--bg); color: var(--fg); cursor: pointer; }
  .fmore:hover { border-color: var(--faint); color: var(--strong); }
  .fmore.on { border-color: var(--accent); color: var(--accent); }
  .fpanel { position: absolute; top: calc(100% + 6px); left: 0; z-index: 30; width: 400px; max-width: calc(100vw - 32px); padding: 14px 16px; background: var(--card); border: 1px solid var(--line); border-radius: 8px; box-shadow: 0 12px 32px rgba(0, 0, 0, .14); display: flex; flex-direction: column; gap: 10px; }
  .frow { display: grid; grid-template-columns: 92px 1fr; align-items: start; column-gap: 10px; }
  .frow .flabel { padding-top: 5px; }
  .fopts { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }
  .fopts .fchip, .fopts .seg { margin: 0; }
  .fchip.removable { padding-right: 7px; }
  .fchip.removable span { margin-left: 2px; opacity: .7; }
  .fclear:hover { text-decoration: underline; }
  .toolbar label { display: flex; align-items: center; gap: 7px; color: var(--muted); font-size: 12px; }
  select { font: inherit; font-size: 12px; color: var(--fg); background: var(--bg); border: 1px solid var(--line); border-radius: 4px; padding: 6px 8px; outline: none; }
  select:focus { border-color: var(--accent); }

  .panel { background: transparent; border: 0; border-radius: 0; overflow: visible; }
  .table-scroll { overflow-x: auto; scrollbar-width: thin;
    /* scroll shadows: an edge shadow appears only when the table actually overflows */
    background:
      linear-gradient(to right, var(--bg) 30%, transparent) left / 24px 100% no-repeat local,
      linear-gradient(to left, var(--bg) 30%, transparent) right / 24px 100% no-repeat local,
      radial-gradient(farthest-side at 0 50%, rgba(0,0,0,.14), transparent) left / 10px 100% no-repeat scroll,
      radial-gradient(farthest-side at 100% 50%, rgba(0,0,0,.14), transparent) right / 10px 100% no-repeat scroll; }
  td.wrap { white-space: normal; }
  .host-spec { white-space: nowrap; }
  .pkg-line { white-space: normal; }
  table { width: 100%; border-collapse: collapse; font-size: 14px; }
  th { text-align: left; font-size: 11px; font-weight: 500; letter-spacing: .06em; text-transform: uppercase; color: var(--muted); padding: 9px 8px; border-bottom: 1px solid var(--line); white-space: nowrap; background: var(--bg); }
  th.sortable { cursor: pointer; user-select: none; }
  th.sortable:hover { color: var(--fg); }
  th .arrow { color: var(--accent); margin-left: 4px; }
  td { padding: 10px 8px; border-bottom: 1px solid var(--line-soft); white-space: nowrap; vertical-align: middle; }
  td.gpu-cell { white-space: normal; }
  th:first-child, td:first-child { padding-left: 0; }
  th:last-child, td:last-child { padding-right: 0; }
  tbody tr:hover { background: var(--hover); }
  tbody tr.clickable { cursor: pointer; }
  .num { text-align: right; font-variant-numeric: tabular-nums; }
  .strong { color: var(--strong); font-weight: 600; }          /* prices and key numbers */
  .accent { color: var(--accent); }                              /* headline price on detail pages */
  .stat b.accent { font-weight: 600; }
  .yes { color: var(--ok); font-weight: 500; }
  .val { color: var(--fg); font-weight: 400; }                   /* secondary numbers (FLOPS, vCPU) */
  .price-off { color: var(--faint); text-decoration: line-through; text-decoration-thickness: 1px; font-weight: 400; }
  .tag { display: inline-block; font-family: var(--font); font-size: 10.5px; font-weight: 500; letter-spacing: .02em; padding: 0 5px; border-radius: 3px; margin-top: 2px; }
  .tag.bad { color: var(--bad); background: var(--bad-soft); }
  .tag.warn { color: var(--warn); background: var(--warn-soft); }
  .quote { color: var(--muted); font-style: italic; font-weight: 400; }
  .unk { font-family: var(--font); font-size: 10.5px; font-weight: 400; color: var(--muted); letter-spacing: .01em; white-space: nowrap; font-style: normal; }
  .mono { font-family: var(--mono); font-size: 12.5px; }
  .muted { color: var(--muted); }
  .row-title { display: block; font-weight: 500; color: var(--strong); }
  /* Secondary information is always small and muted so primary values lead. */
  .row-sub { display: block; font-family: var(--mono); font-size: 11px; color: var(--muted); margin-top: 1px; font-weight: 400; }
  .spot-sub { color: var(--ok); font-weight: 500; }
  .meta { display: block; font-family: var(--font); font-size: 10.5px; line-height: 1.3; color: var(--muted); font-weight: 400; letter-spacing: .01em; margin-top: 1px; }
  .logo { width: 20px; height: 20px; border-radius: 4px; object-fit: contain; background: transparent; padding: 0; vertical-align: -5px; margin-right: 8px; }
  .provider-name { font-weight: 500; color: var(--strong); white-space: nowrap; }
  .provider-name:hover { text-decoration: underline; }
  .site-link { color: var(--accent); text-decoration: none; font-size: 11.5px; white-space: nowrap; }
  /* The provider cell must stay a table cell (display:table-cell) or its row border breaks;
     the flex layout lives on an inner wrapper instead. */
  .prov-wrap { display: flex; align-items: flex-start; gap: 8px; min-width: 250px; }
  .prov-wrap > .logo { flex: none; margin: 2px 0 0; }
  .prov-cell { display: flex; flex-direction: column; line-height: 1.35; min-width: 0; flex: 1 1 auto; }
  .taggroup { display: inline-flex; flex-wrap: nowrap; align-items: center; }
  /* Name + tags: wrap the tags to a second line instead of pushing the cell wider than the column. */
  .prov-cell > span:first-child { display: flex; flex-wrap: wrap; align-items: center; row-gap: 2px; min-width: 0; }
  .prov-sub { display: inline-flex; flex-wrap: wrap; align-items: baseline; gap: 0; }
  .prov-sub .regions { font-family: var(--mono); font-size: 10.5px; color: var(--muted); white-space: normal; }
  .mini { display: inline-block; margin-left: 6px; padding: 0 4px; border-radius: 3px; font-size: 10px; font-weight: 600; letter-spacing: .03em; line-height: 15px; vertical-align: 1px; text-transform: uppercase; }
  .mini.ok { color: var(--ok); background: var(--ok-soft); }
  .mini.warn { color: var(--warn); background: var(--warn-soft); }
  .mini.info { color: var(--info); background: var(--info-soft); }
  .mini.muted-tag { color: var(--muted); background: var(--soft); }
  .site-link:hover { text-decoration: underline; }
  .site-url { display: inline-block; font-size: 14px; color: var(--accent); text-decoration: none; margin-top: 4px; }
  .site-url:hover { color: var(--accent); text-decoration: underline; }
  .sku-link { color: inherit; }
  .sku-link:hover .row-title { color: var(--accent); text-decoration: underline; }
  .chip { display: inline-block; white-space: nowrap; font-family: var(--mono); font-size: 11px; padding: 1px 6px; border: 1px solid var(--line); border-radius: 4px; background: var(--bg); color: var(--muted); font-weight: 400; margin: 0 4px 4px 0; }
  .chip-out { opacity: .45; border-style: dashed; }
  .fnote { flex: 1 1 100%; order: 9; margin: 6px 0 0; font-size: 11.5px; color: var(--muted); line-height: 1.4; }
  .fnote span { text-decoration: underline dotted; cursor: help; }
  td.gpu-cell { min-width: 160px; max-width: 260px; line-height: 1.4; }
  td.feat-cell { white-space: normal; min-width: 110px; max-width: 170px; line-height: 1.7; }
  .cap-stack .meta { white-space: normal; max-width: 110px; margin-left: auto; text-align: right; }
  .pidx { font-weight: 600; font-variant-numeric: tabular-nums; }
  .pidx.ok { color: var(--ok); } .pidx.bad { color: var(--bad); } .pidx.muted { color: var(--muted); font-weight: 500; }
  /* Small i-in-a-circle hint next to a column label; the tooltip carries the method. */
  .th-info { display: inline-flex; align-items: center; justify-content: center; width: 13px; height: 13px; margin-left: 5px; color: var(--muted); cursor: default; vertical-align: -2px; }
  .th-info svg { display: block; }
  .th-info:hover, .th-info:focus-visible { color: var(--fg); outline: none; }
  .tip { position: fixed; z-index: 70; max-width: 250px; padding: 7px 9px; border: 1px solid var(--line); border-radius: 6px; background: var(--bg); color: var(--muted); font-size: 11.5px; line-height: 1.45; box-shadow: 0 10px 30px rgba(0, 0, 0, .16); pointer-events: none; }
  .tip.hidden { display: none; }
  .tip > div:first-child { color: var(--fg); }
  .tip > div + div { margin-top: 5px; }
  .feat { display: inline-block; font-size: 11px; font-weight: 500; color: var(--ok); background: var(--ok-soft); border-radius: 3px; padding: 0 5px; margin: 0 4px 2px 0; white-space: nowrap; }
  .pill { display: inline-flex; align-items: center; gap: 5px; padding: 2px 7px; border-radius: 4px; font-size: 11px; font-weight: 400; background: var(--soft); color: var(--muted); white-space: nowrap; }
  .pill.ok { color: var(--ok); background: var(--ok-soft); }
  .pill.warn { color: var(--warn); background: var(--warn-soft); }
  .pill.bad { color: var(--bad); background: var(--bad-soft); }
  .pill.info { color: var(--info); background: var(--info-soft); }
  .dot { width: 6px; height: 6px; border-radius: 50%; background: currentColor; display: inline-block; }
  .ok { color: var(--ok); }
  .warn { color: var(--warn); }
  .bad { color: var(--bad); }
  .info { color: var(--info); }
  .hidden { display: none !important; }
  .empty { padding: 60px 0; text-align: center; color: var(--muted); }
  .cap-link { color: var(--strong); font-weight: 600; }
  .cap-link:hover { color: var(--accent); text-decoration: underline; }
  .cap-stack { display: inline-block; text-align: right; line-height: 1.45; font-weight: 500; }
  .cap-total { font-weight: 600; }
  .pkg-line { font-family: var(--mono); font-size: 12px; color: var(--fg); line-height: 1.6; }
  .pkg-line.off { color: var(--faint); }
  .pkg-line .tag { margin: 0 0 0 6px; vertical-align: 1px; }
  .prec-cell { white-space: normal; line-height: 1.9; }
  .prec-compact { font-family: var(--mono); font-size: 11.5px; color: var(--fg); letter-spacing: .01em; white-space: nowrap; }
  .prec-cell .chip { margin-bottom: 3px; }
  #gpu-spec-table td { white-space: normal; }
  #gpu-spec-table td:first-child { width: 180px; }

  /* detail */
  .back { display: inline-flex; align-items: center; gap: 6px; color: var(--muted); font-size: 13px; margin-bottom: 18px; }
  .back:hover { color: var(--fg); }
  .detail-head { display: flex; align-items: center; gap: 14px; margin-bottom: 6px; }
  .logo-lg { width: 44px; height: 44px; border-radius: 6px; object-fit: contain; background: var(--soft); padding: 5px; }
  .detail-head h1 { font-size: 22px; font-weight: 600; letter-spacing: -.02em; margin: 0; color: var(--strong); }
  .detail-sub { color: var(--muted); font-size: 12px; margin-top: 2px; }
  .badges { display: flex; flex-wrap: wrap; gap: 6px; margin: 14px 0 20px; align-items: center; }
  .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; margin-bottom: 28px; }
  .stat { padding: 12px 14px; background: var(--card); border: 1px solid var(--line-soft); border-radius: 8px; }
  .stat span { display: block; color: var(--muted); font-size: 11px; margin-bottom: 3px; text-transform: uppercase; letter-spacing: .04em; }
  .stat span + b + span { text-transform: none; letter-spacing: .01em; margin: 3px 0 0; font-size: 10.5px; color: var(--muted); }
  .stat b { font-size: 20px; font-weight: 500; letter-spacing: -.01em; color: var(--strong); }
  .stat b.accent { color: var(--accent); } .stat b.ok { color: var(--ok); } .stat b.bad { color: var(--bad); } .stat b.none { color: var(--faint); font-weight: 400; }
  section { margin-bottom: 30px; }
  #inventory { scroll-margin-top: 68px; }
  section h2 { font-size: 12px; font-weight: 600; letter-spacing: .06em; text-transform: uppercase; color: var(--strong); margin: 0 0 10px; }
  .h2-note { font-weight: 400; letter-spacing: 0; text-transform: none; font-size: 11.5px; color: var(--muted); }
  .note { padding: 10px 0; color: var(--muted); font-size: 12px; }
  .note b { color: var(--fg); }
  .iai-note a { color: var(--accent); }
  .source-list { list-style: none; margin: 0; padding: 0; }
  .source-list li { display: flex; gap: 10px; align-items: baseline; padding: 10px 0; border-bottom: 1px solid var(--line-soft); font-size: 12px; }
  .source-list li:last-child { border-bottom: 0; }
  .source-list a { color: var(--fg); word-break: break-all; }
  .source-list a:hover { color: var(--accent); }
  footer { max-width: 1200px; margin: 0 auto; color: var(--muted); font-size: 11.5px; padding: 16px 32px 48px; }

  /* spotlight search */
  body.spotlight-open { overflow: hidden; }
  .spotlight { position: fixed; inset: 0; z-index: 60; display: flex; align-items: flex-start; justify-content: center; padding: 12vh 16px 16px; background: rgba(0, 0, 0, .32); }
  .spotlight-card { width: min(640px, 100%); background: var(--bg); border: 1px solid var(--line); border-radius: 8px; box-shadow: 0 18px 48px rgba(0, 0, 0, .18); overflow: hidden; }
  .spotlight-head { display: flex; align-items: center; gap: 10px; padding: 12px 14px; border-bottom: 1px solid var(--line); }
  .spotlight-head svg { width: 16px; height: 16px; color: var(--muted); flex: none; }
  .spotlight-head input { flex: 1; min-width: 0; border: 0; outline: none; background: transparent; color: var(--fg); font: inherit; font-size: 15px; }
  .spotlight-head input::placeholder { color: var(--faint); }
  .spotlight-results { max-height: min(60vh, 420px); overflow-y: auto; padding: 4px 0 6px; scrollbar-width: thin; }
  .spot-section { padding: 10px 14px 4px; font-size: 10.5px; letter-spacing: .06em; text-transform: uppercase; color: var(--muted); }
  .spot-item { display: flex; align-items: center; gap: 10px; width: 100%; padding: 9px 14px; border: 0; background: none; font: inherit; color: var(--fg); text-align: left; cursor: pointer; }
  .spot-item.active, .spot-item:hover { background: var(--soft); }
  .spot-glyph { height: 20px; min-width: 20px; padding: 0 4px; display: inline-flex; align-items: center; justify-content: center; border: 1px solid var(--line); border-radius: 4px; font-family: var(--mono); font-size: 9px; color: var(--muted); flex: none; }
  .spot-item .logo { margin: 0; flex: none; }
  .spot-main { display: flex; flex-direction: column; min-width: 0; flex: 1; }
  .spot-title, .spot-sub { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .spot-title { font-size: 13.5px; font-weight: 500; color: var(--strong); }
  .spot-sub { font-size: 11.5px; color: var(--muted); }
  .spot-meta { margin-left: auto; flex: none; max-width: 45%; overflow: hidden; text-overflow: ellipsis; color: var(--muted); font-size: 11.5px; white-space: nowrap; }
  .spotlight-results { overflow-x: hidden; }
  .spot-empty { padding: 32px 14px; text-align: center; color: var(--muted); font-size: 13px; }
  .spotlight-foot { display: flex; gap: 16px; padding: 8px 14px; border-top: 1px solid var(--line); color: var(--muted); font-size: 11px; }
  .spotlight-foot .kbd { margin-right: 3px; }
  @media (max-width: 760px) {
    /* keep the decision columns; drop secondary ones instead of scrolling sideways */
    #view-gpus th:nth-child(3), #view-gpus td:nth-child(3),
    #view-gpus th:nth-child(4), #view-gpus td:nth-child(4),
    #view-gpus th:nth-child(7), #view-gpus td:nth-child(7) { display: none; }
    #view-providers th:nth-child(2), #view-providers td:nth-child(2),
    #view-providers th:nth-child(4), #view-providers td:nth-child(4),
    #view-providers th:nth-child(n+7), #view-providers td:nth-child(n+7) { display: none; }
    .filters { margin-top: 0; }
    .fmeta { margin-left: 0; width: 100%; }
    .fpanel { left: auto; right: -40px; }
    .stats { grid-template-columns: repeat(2, 1fr); }
    .wrap { padding: 0 18px; }
    .search-trigger { width: 150px; }
    .search-trigger span { display: none; }
    .search-trigger .kbd { display: none; }
    .brand .slash, .brand .tagline { display: none; }
    .count { display: none; }
  }
</style>
</head>
<body>
<header>
  <div class="wrap bar">
    <a class="brand" href="#/gpus"><b>__SITE_NAME__</b><span class="slash">/</span><span class="tagline">India</span></a>
    <div class="grow"></div>
    <div class="tabs">
      <button id="tab-gpus" class="active" onclick="setView('gpus')">GPUs</button>
      <button id="tab-providers" onclick="setView('providers')">Providers</button>
    </div>
    <button class="search-trigger" id="search-trigger" type="button" aria-label="Search GPUs and providers">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
      <span>Search GPUs, providers…</span>
      <kbd class="kbd">⌘K</kbd>
    </button>
    <div class="count" id="count"></div>
    <a class="api-btn" href="/api/docs" title="API reference" aria-label="API reference">API</a>
    __REPO_LINK__
    <button class="theme-btn" id="theme-btn" type="button" aria-label="Toggle colour theme" title="Theme"></button>
  </div>
</header>
<main class="wrap">
  <div id="view-gpus">
    <div class="filters" id="filters-gpus"></div>
    <div class="panel">
      <div class="table-scroll">
        <table>
          <thead>
            <tr id="thead-gpus">
              <th class="sortable" data-sort="id">GPU</th>
              <th class="num sortable" data-sort="vram">VRAM</th>
              <th class="num sortable" data-sort="flops" title="Dense FP16 Tensor FLOPS per GPU. Common basis across all accelerator SKUs.">FP16 dense</th>
              <th title="Key native formats that differ between GPUs (FP64, BF16, FP8, FP6, FP4). Hover a cell for the full native list.">Precision</th>
              <th class="num sortable" data-sort="providers" title="Providers that can be ordered now (not retired, in stock, self-serve) out of those listing the GPU">Providers</th>
              <th class="num sortable" data-sort="avail" title="GPUs observed available right now, summed over the latest observation per provider. Blank when no provider publishes stock.">Available now</th>
              <th class="num sortable" data-sort="price" title="Cheapest hourly on-demand price per GPU-hour across every provider and region. A cheaper monthly-commitment rate, or an outside-India cheapest provider, is noted below the price.">Price (on-demand /GPU-hr)</th>
              <th class="sortable" data-sort="updated">Updated</th>
            </tr>
          </thead>
          <tbody id="tbody-gpus"></tbody>
        </table>
      </div>
    </div>
    <div class="empty hidden" id="empty-gpus">No GPUs match these filters.</div>
  </div>

  <div id="view-providers" class="hidden">
    <div class="filters" id="filters-providers"></div>
    <div class="panel">
      <div class="table-scroll">
        <table>
          <thead>
            <tr id="thead-providers">
              <th class="sortable" data-sort="name">Provider</th>
              <th class="sortable" data-sort="gpus">GPUs</th>
              <th class="num sortable" data-sort="pindex">Price vs market<span class="th-info" role="img" tabindex="0" aria-label="How Price vs market is calculated" data-tip="Cheapest price ÷ market median, averaged.|Models sold by 3+ providers; hourly vs hourly, monthly vs monthly.|Quote-only and sold-out excluded."><svg viewBox="0 0 16 16" width="12" height="12" aria-hidden="true"><circle cx="8" cy="8" r="6.6" fill="none" stroke="currentColor" stroke-width="1.3"/><path d="M8 7.1v4.2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="8" cy="4.7" r=".95" fill="currentColor"/></svg></span></th>
              <th class="sortable" data-sort="features" title="Platform features: VPC networking, mountable block/file storage, S3-compatible object storage, CPU VMs">Features</th>
              <th class="num sortable" data-sort="capacity" title="Deployed GPU capacity and power. Available GPUs are a separate column.">Capacity (GPUs)</th>
              <th class="num sortable" data-sort="free" title="Latest observation: GPUs that were available to start right now. Availability, not installed capacity.">Available now</th>
              <th class="num sortable" data-sort="sla">SLA</th>
              <th class="num sortable" data-sort="updated" title="When this provider's data was last verified">Updated</th>
            </tr>
          </thead>
          <tbody id="tbody-providers"></tbody>
        </table>
      </div>
    </div>
    <div class="empty hidden" id="empty-providers">No providers match these filters.</div>
  </div>

  <div id="view-gpu-detail" class="hidden"></div>
  <div id="view-provider-detail" class="hidden"></div>
</main>
<footer class="wrap">
  <span id="footer-count"></span> · Exact per-SKU prices. Capacity is installed fleet; availability counts are GPUs observed free at the last snapshot.
</footer>

<div id="spotlight" class="spotlight hidden" aria-hidden="true">
  <div class="spotlight-card" role="dialog" aria-modal="true" aria-label="Search GPUs and providers">
    <div class="spotlight-head">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
      <input id="spotlight-input" placeholder="Search GPUs, providers…" autocomplete="off" spellcheck="false" />
      <kbd class="kbd">esc</kbd>
    </div>
    <div id="spotlight-results" class="spotlight-results"></div>
    <div class="spotlight-foot">
      <span><kbd class="kbd">↑</kbd><kbd class="kbd">↓</kbd> navigate</span>
      <span><kbd class="kbd">↵</kbd> open</span>
      <span><kbd class="kbd">esc</kbd> close</span>
    </div>
  </div>
</div>

<script src="/assets/track.js?v=1"></script>
<script>
const $ = (id) => document.getElementById(id);
// Analytics is a progressive enhancement: if /assets/track.js did not load, calls are no-ops.
const TRACK = window.TRACK || { pageview() {}, click() {}, search() {} };
let CATALOG = null;
let VIEW = "gpus";
let SORT = { gpus: { key: "id", dir: 1 }, providers: { key: "name", dir: 1 } };

/* ---------------- Region & provider-origin scope ----------------
   Two shared filters (both pages): Region = where GPUs physically run (default India);
   Provider = Indian company vs global company. GPU views and minimum prices use only
   packages in scope; provider pages always show everything a provider sells. */
const regionIsIndia = (r) => !!r && (r === "IN" || r.startsWith("IN-") || /^IN\d/.test(r));
const isIndiaSku = (s) => s.residency ? s.residency === "india" : regionIsIndia(s.region);
const LOCATIONS = { "IN-BOM": "Mumbai", "IN-DEL": "Delhi NCR", "IN-NOI": "Noida", "IN-CHE": "Chennai", "IN-MAA": "Chennai",
  "IN-PNQ": "Pune", "IN-HYD": "Hyderabad", "IN-JAM": "Jamnagar", "IN-NAG": "Nagpur",
  "EU-FR": "France", "EU-FI": "Finland", "EU-NO": "Norway" };
const geoOf = (r) => regionIsIndia(r) ? "india" : /^EU/.test(r || "") ? "europe" : "other";
const locationOf = (r) => LOCATIONS[r] || (geoOf(r) === "india" ? "India, location not specified" : geoOf(r) === "europe" ? "Europe, location not specified" : r);
const COUNTRY_NAMES = { IN: "India", US: "United States", FR: "France", NL: "Netherlands", FI: "Finland", GB: "United Kingdom", DE: "Germany", NO: "Norway" };
const isIndianProvider = (p) => (p && p.country) === "IN";
function regionInScope(region) {
  const r = FILTERS.shared.region;
  if (r === "all") return true;
  if (r === "india" || r === "europe") return geoOf(region) === r;
  if (r.startsWith("loc:")) return locationOf(region) === r.slice(4);
  return true;
}
function originInScope(pid) {
  const o = FILTERS.shared.origin;
  return o === "all" || (o === "indian") === isIndianProvider(providerOf(pid));
}
const skuInScope = (s) => regionInScope(s.region) && originInScope(s.provider);
function applyScope() {
  if (CATALOG && CATALOG.allSkus) CATALOG.skus = CATALOG.allSkus.filter(skuInScope);
}
function regionOptions() {
  const all = (CATALOG && CATALOG.allSkus) || [];
  const locs = { india: new Map(), europe: new Map() };
  for (const s of all) {
    const g = geoOf(s.region);
    if (locs[g]) locs[g].set(locationOf(s.region), (locs[g].get(locationOf(s.region)) || 0) + 1);
  }
  const group = (g, label) => [[g, `${label} (all)`], ...[...locs[g].keys()].sort((a, b) => a.includes("not specified") - b.includes("not specified") || a.localeCompare(b)).map(l => [`loc:${l}`, `\u00a0\u00a0\u00a0${l}`])];
  return [...group("india", "India"), ...group("europe", "Europe — outside India"), ["all", "All regions"]];
}
// Country tag (provider origin, not where GPUs run): flag + ISO code.
// The flag is the fast read, the code survives platforms without flag glyphs
// (e.g. Windows) and the full country name goes to screen readers and the tooltip.
const flagOf = (cc) => /^[A-Z]{2}$/.test(cc || "") ? String.fromCodePoint(...[...cc].map(c => 0x1F1E6 + c.charCodeAt(0) - 65)) : "";
function countryTag(p) {
  if (!p || !p.country) return "";
  const name = COUNTRY_NAMES[p.country] || p.country;
  return `<span class="mini muted-tag" title="${esc("Headquartered in " + name)}" aria-label="${esc(name)}">${flagOf(p.country)} ${esc(p.country)}</span>`;
}

/* ---------------- Theme ----------------
   Two-way switch. Until the viewer clicks, follow the system setting; a click flips
   light <-> dark and is remembered (per-viewer, when storage is available). */
const darkQuery = window.matchMedia ? window.matchMedia("(prefers-color-scheme: dark)") : null;
let THEME = (() => { try { const t = localStorage.getItem("gpu-catalog-theme"); return t === "light" || t === "dark" ? t : null; } catch (e) { return null; } })();
const effectiveTheme = () => THEME || (darkQuery && darkQuery.matches ? "dark" : "light");
function applyTheme() {
  if (THEME) document.documentElement.dataset.theme = THEME; else delete document.documentElement.dataset.theme;
  const b = document.getElementById("theme-btn");
  if (!b) return;
  const dark = effectiveTheme() === "dark";
  b.textContent = dark ? "☀" : "☾";
  b.title = dark ? "Switch to light theme" : "Switch to dark theme";
  b.setAttribute("aria-label", b.title);
}
document.addEventListener("click", e => {
  if (!e.target.closest("#theme-btn")) return;
  THEME = effectiveTheme() === "dark" ? "light" : "dark";
  try { localStorage.setItem("gpu-catalog-theme", THEME); } catch (err) {}
  applyTheme();
});
if (darkQuery && darkQuery.addEventListener) darkQuery.addEventListener("change", () => { if (!THEME) applyTheme(); });

/* ---------------- Filters ----------------
   Per-viewer convenience: remembered in localStorage when available, never required. */
const FILTER_DEFAULTS = {
  gpus: { vendor: "all", klass: "all", vram: 0, maxPrice: 0, provider: "", hourly: false, fp8: false, fp4: false },
  providers: { pricing: "all", provisioning: [], gpu: "", hourly: false, free: false, capacity: false, vpc: false, storage: false, object: false },
  shared: { region: "india", origin: "all" },
};
let FILTERS = (() => {
  const base = JSON.parse(JSON.stringify(FILTER_DEFAULTS));
  try {
    const saved = JSON.parse(localStorage.getItem("gpu-catalog-filters") || "null");
    if (saved) for (const k of Object.keys(base)) Object.assign(base[k], saved[k] || {});
    // provisioning is a multi-select list; migrate older single-value saves
    const pv = base.providers.provisioning;
    base.providers.provisioning = Array.isArray(pv) ? pv.filter(x => ["api", "console", "sales"].includes(x))
      : ["api", "console", "sales"].includes(pv) ? [pv] : [];
    delete base.providers.api;
  } catch (e) { /* storage unavailable: defaults */ }
  return base;
})();
function saveFilters() { try { localStorage.setItem("gpu-catalog-filters", JSON.stringify(FILTERS)); } catch (e) {} }
function activeFilterCount(view) {
  const n = (v) => Object.keys(FILTER_DEFAULTS[v]).filter(k => JSON.stringify(FILTERS[v][k]) !== JSON.stringify(FILTER_DEFAULTS[v][k])).length;
  return n(view) + (view === "providers" ? n("shared") : 0);
}
const seg = (view, key, opts) => `<span class="seg">${opts.map(([v, l]) =>
  `<button data-f="${view}.${key}" data-v="${esc(v)}" class="${String(FILTERS[view][key]) === String(v) ? "on" : ""}">${esc(l)}</button>`).join("")}</span>`;
const chip = (view, key, label, title) =>
  `<button class="fchip${FILTERS[view][key] ? " on" : ""}" data-f="${view}.${key}" data-toggle="1" title="${esc(title || "")}">${esc(label)}</button>`;
// Multi-select chips: any combination may be on; none on = no filter.
const multi = (view, key, opts) => opts.map(([v, l]) =>
  `<button class="fchip${FILTERS[view][key].includes(v) ? " on" : ""}" data-f="${view}.${key}" data-multi="${esc(v)}">${esc(l)}</button>`).join("");
const sel = (view, key, opts) => `<select data-f="${view}.${key}" class="${String(FILTERS[view][key]) !== String(FILTER_DEFAULTS[view][key]) ? "on" : ""}">${opts.map(([v, l]) =>
  `<option value="${esc(v)}"${String(FILTERS[view][key]) === String(v) ? " selected" : ""}>${esc(l)}</option>`).join("")}</select>`;

// Primary filters sit in the bar; the rest live in a "More filters" popover.
// Active hidden filters still show as removable chips so nothing filters invisibly.
const MORE_OPEN = { gpus: false, providers: false };
const SECONDARY = {
  gpus: ["klass", "vram", "provider", "fp8", "fp4"],
  providers: ["provisioning", "hourly", "capacity", "vpc", "storage", "object"],
};
function filterLabel(view, key, v) {
  if (view === "gpus") return ({
    klass: () => ({ dc: "Data centre", rtx: "RTX" })[v],
    vram: () => `≥ ${v} GB VRAM`,
    provider: () => providerOf(v).name || v,
    fp8: () => "FP8", fp4: () => "FP4",
  })[key]();
  return ({
    provisioning: () => v.map(x => ({ api: "API", console: "Console", sales: "Sales" })[x]).join(" + "),
    hourly: () => "Billed hourly", capacity: () => "Capacity published",
    vpc: () => "VPC", storage: () => "Mountable storage", object: () => "Object storage",
  })[key]();
}
function renderFilterBar(view, shown, total, note = "") {
  const f = FILTERS[view], d = FILTER_DEFAULTS[view];
  let primary = "", more = "";
  if (view === "gpus") {
    const provs = [...new Set((CATALOG.allSkus || CATALOG.skus).map(s => s.provider))].map(id => [id, providerOf(id).name || id]).sort((a, b) => a[1].localeCompare(b[1]));
    primary = `
      <span class="fgroup">${seg("gpus", "vendor", [["all", "All vendors"], ["nvidia", "NVIDIA"], ["amd", "AMD"], ["intel", "Intel"]])}</span>
      <span class="fgroup">${sel("gpus", "maxPrice", [[0, "Any price"], [1, "≤ $1 /hr"], [2, "≤ $2 /hr"], [3, "≤ $3 /hr"], [5, "≤ $5 /hr"]])}</span>
      <span class="fgroup">${chip("gpus", "hourly", "Billed hourly", "At least one provider bills this GPU by the hour at a published rate, and it is not known to be out of stock")}</span>`;
    more = `
      <div class="frow"><span class="flabel">Class</span><span class="fopts">${seg("gpus", "klass", [["all", "All"], ["dc", "Data centre"], ["rtx", "RTX"]])}</span></div>
      <div class="frow"><span class="flabel">VRAM</span><span class="fopts">${sel("gpus", "vram", [[0, "Any"], [24, "≥ 24 GB"], [48, "≥ 48 GB"], [80, "≥ 80 GB"], [141, "≥ 141 GB"], [192, "≥ 192 GB"]])}</span></div>
      <div class="frow"><span class="flabel">Provider</span><span class="fopts">${sel("gpus", "provider", [["", "Any provider"], ...provs])}</span></div>
      <div class="frow"><span class="flabel">Precision</span><span class="fopts">${chip("gpus", "fp8", "FP8", "Native FP8 Tensor support")}${chip("gpus", "fp4", "FP4", "Native FP4 Tensor support")}</span></div>`;
  } else {
    const fams = [...new Set(CATALOG.skus.filter(s => s.status !== "retired").map(s => s.gpu))].sort().map(g => [g, g]);
    primary = `
      <span class="fgroup">${sel("providers", "gpu", [["", "Any GPU"], ...fams])}</span>
      <span class="fgroup">${seg("providers", "pricing", [["all", "All pricing"], ["published", "Published"], ["quote", "Quote"]])}</span>
      <span class="fgroup">${chip("providers", "free", "Available now", "Latest observation shows GPUs available to start")}</span>`;
    more = `
      <div class="frow"><span class="flabel">Provisioning</span><span class="fopts">${multi("providers", "provisioning", [["api", "API"], ["console", "Console"], ["sales", "Sales"]])}</span></div>
      <div class="frow"><span class="flabel">Features</span><span class="fopts">${chip("providers", "hourly", "Billed hourly", "At least one package is billed by the hour")}${chip("providers", "capacity", "Capacity published", "Installed fleet size is published")}</span></div>
      <div class="frow"><span class="flabel">Network</span><span class="fopts">${chip("providers", "vpc", "VPC")}</span></div>
      <div class="frow"><span class="flabel">Storage</span><span class="fopts">${chip("providers", "storage", "Mountable", "Block or file storage attached to a GPU VM — keeps downloaded model weights")}${chip("providers", "object", "Object storage", "S3-compatible object storage")}</span></div>`;
  }
  const hidden = SECONDARY[view].filter(k => JSON.stringify(f[k]) !== JSON.stringify(d[k]));
  const hiddenChips = hidden.map(k =>
    `<button class="fchip on removable" data-reset="${view}.${k}" title="Remove filter">${esc(filterLabel(view, k, f[k]))} <span aria-hidden="true">×</span></button>`).join("");
  const n = activeFilterCount(view);
  const shared = `
      <span class="fgroup" title="Where the GPUs physically run (data residency)"><span class="flabel">Region</span>${sel("shared", "region", regionOptions())}</span>
      <span class="fgroup" title="Indian company vs global company"><span class="flabel">Provider</span>${seg("shared", "origin", [["all", "All"], ["indian", "Indian"], ["global", "Global"]])}</span>`;
  $(`filters-${view}`).innerHTML = `
    ${view === "providers" ? shared : ""}
    ${primary}
    <span class="fgroup fmore-wrap">
      <button class="fmore${MORE_OPEN[view] || hidden.length ? " on" : ""}" data-more="${view}" aria-expanded="${MORE_OPEN[view]}">More filters${hidden.length ? ` · ${hidden.length}` : ""} <span aria-hidden="true">▾</span></button>
      ${MORE_OPEN[view] ? `<div class="fpanel" role="dialog" aria-label="More filters">${more}</div>` : ""}
    </span>
    ${hiddenChips}
    ${note ? `<span class="fnote">${note}</span>` : ""}
    <span class="fmeta">${shown === total ? `${total}` : `${shown} of ${total}`} ${view === "gpus" ? "GPUs" : "providers"}${n ? ` <button class="fclear" data-clear="${view}">Clear${n > 1 ? " all" : ""}</button>` : ""}</span>`;
}
function onFilterEvent(e) {
  const el = e.target.closest("[data-f],[data-clear],[data-reset],[data-more]");
  if (!el) return;
  if (el.dataset.more) { MORE_OPEN[el.dataset.more] = !MORE_OPEN[el.dataset.more]; return el.dataset.more === "gpus" ? renderGPUs() : renderProviders(); }
  if (el.dataset.reset) {
    const [v, k] = el.dataset.reset.split(".");
    FILTERS[v][k] = JSON.parse(JSON.stringify(FILTER_DEFAULTS[v][k]));
    saveFilters();
    return v === "gpus" ? renderGPUs() : renderProviders();
  }
  if (el.dataset.clear) {
    FILTERS[el.dataset.clear] = JSON.parse(JSON.stringify(FILTER_DEFAULTS[el.dataset.clear]));
    FILTERS.shared = JSON.parse(JSON.stringify(FILTER_DEFAULTS.shared));
    MORE_OPEN[el.dataset.clear] = false;
    applyScope();
  }
  else {
    const [view, key] = el.dataset.f.split(".");
    const def = FILTER_DEFAULTS[view][key];
    if (el.dataset.multi) {
      const cur = FILTERS[view][key], v = el.dataset.multi;
      FILTERS[view][key] = cur.includes(v) ? cur.filter(x => x !== v) : [...cur, v];
    } else if (el.dataset.toggle) FILTERS[view][key] = !FILTERS[view][key];
    else {
      const raw = el.tagName === "SELECT" ? el.value : el.dataset.v;
      FILTERS[view][key] = typeof def === "number" ? Number(raw) : raw;
    }
  }
  saveFilters();
  if (el.dataset.f && el.dataset.f.startsWith("shared.")) { applyScope(); return route(); }
  (el.dataset.clear || el.dataset.f.split(".")[0]) === "gpus" ? renderGPUs() : renderProviders();
}
document.addEventListener("click", e => {
  if (e.target.closest(".filters button")) return onFilterEvent(e);
  // click outside an open popover closes it
  for (const v of ["gpus", "providers"]) {
    if (MORE_OPEN[v] && !e.target.closest(`#filters-${v} .fmore-wrap`)) { MORE_OPEN[v] = false; v === "gpus" ? renderGPUs() : renderProviders(); }
  }
});
document.addEventListener("keydown", e => {
  if (e.key !== "Escape") return;
  for (const v of ["gpus", "providers"]) if (MORE_OPEN[v]) { MORE_OPEN[v] = false; v === "gpus" ? renderGPUs() : renderProviders(); }
});
document.addEventListener("change", e => { if (e.target.closest(".filters select")) onFilterEvent(e); });

function gpuMatches(g) {
  const f = FILTERS.gpus;
  const vendor = g.id.split("/")[0];
  const native = ((g.variant && g.variant.precision && g.variant.precision.native) || []);
  const isRtx = /^RTX/i.test(g.familyName || g.name);
  const best = bestOf(g.skus);
  if (f.vendor !== "all" && vendor !== f.vendor) return false;
  if (f.klass === "dc" && isRtx) return false;
  if (f.klass === "rtx" && !isRtx) return false;
  if (f.vram && !(g.vram >= f.vram)) return false;
  if (f.maxPrice && !(best.v != null && best.v <= f.maxPrice)) return false;
  if (f.provider && !g.skus.some(s => s.provider === f.provider && s.status !== "retired")) return false;
  if (f.hourly && !(best.v != null && !best.monthly)) return false;
  if (f.fp8 && !native.some(x => x.startsWith("fp8"))) return false;
  if (f.fp4 && !native.includes("fp4")) return false;
  return true;
}
function providerMatches(r) {
  const f = FILTERS.providers;
  if (!originInScope(r.p.id)) return false;
  if (r.skus.length && !r.skus.some(s => regionInScope(s.region))) return false;
  if (f.pricing !== "all" && r.access.pricing !== f.pricing) return false;
  if (f.provisioning.length && !f.provisioning.includes(r.access.provisioning)) return false;
  // A GPU filter is a "who can I rent this from now" question: out-of-stock and sales-only
  // packages do not count.
  if (f.gpu && !r.skus.some(s => s.gpu === f.gpu && orderablePrice(s) != null)) return false;
  if (f.hourly && !(r.access.hourly > 0)) return false;
  if (f.free && !(r.freeLive > 0)) return false;
  if (f.capacity && r.capacity == null) return false;
  if (f.vpc && !r.capVpc) return false;
  if (f.storage && !r.capMountable) return false;
  if (f.object && !r.capObject) return false;
  return true;
}

const SUPPLIER = {
  H100: "nvidia", H200: "nvidia", A100: "nvidia", B200: "nvidia", B300: "nvidia",
  L40S: "nvidia", L4: "nvidia", A30: "nvidia", A40: "nvidia", A2: "nvidia",
  T4: "nvidia", V100: "nvidia", "RTX A6000": "nvidia", "RTX 6000 Ada": "nvidia",
  "RTX PRO 4500": "nvidia", "RTX PRO 6000": "nvidia", "RTX A5000": "nvidia",
  "RTX 4090": "nvidia", "RTX 5090": "nvidia", "RTX 3090": "nvidia", "RTX A4000": "nvidia",
  MI300X: "amd", MI325X: "amd", "Gaudi 2": "intel",
};
const GPU_ALIASES = { "RTX-PRO6000": "RTX PRO 6000", RTXPRO6000: "RTX PRO 6000", "RTX PRO 6000": "RTX PRO 6000" };
function gpuName(g) {
  const u = String(g || "").toUpperCase();
  return GPU_ALIASES[u] || u;
}

const GPU_FAMILIES = new Map();
const GPU_VARIANTS = new Map();
const FEATURE_LABELS = {
  "transformer-engine": "Transformer Engine",
  "confidential-computing": "Confidential Computing",
  "nvlink": "NVLink",
  "nvswitch": "NVSwitch",
  "tf32": "TF32",
  "rocm": "ROCm",
  "infinity-fabric": "Infinity Fabric",
  "ecc": "ECC",
  "fp8": "FP8",
  "fp4": "FP4",
  "mig": "MIG",
  "sparsity": "Sparsity",
  "dpx": "DPX",
};
const PRECISION_LABELS = {
  "fp64": "FP64",
  "fp32": "FP32",
  "tf32": "TF32",
  "bf16": "BF16",
  "fp16": "FP16",
  "fp8-e4m3": "FP8 E4M3",
  "fp8-e5m2": "FP8 E5M2",
  "fp6": "FP6",
  "fp4": "FP4",
  "int8": "INT8",
};
function buildGPUIndex() {
  GPU_FAMILIES.clear(); GPU_VARIANTS.clear();
  for (const g of CATALOG.gpus || []) {
    GPU_FAMILIES.set(g.id, g);
    const supplier = String(g.id || "").split("/")[0];
    for (const v of (g.variants || [])) {
      GPU_VARIANTS.set(`${supplier}/${v.id}`, { key: `${supplier}/${v.id}`, family: g, variant: v });
    }
  }
}
function skuAccelId(s) {
  const v = s.gpu_variant || String(s.gpu).toLowerCase().replace(/\s+/g, "-");
  let supplier = SUPPLIER[s.gpu];
  if (!supplier) {  // fall back to the accelerator catalogue so new families never drop out
    const hit = [...GPU_VARIANTS.keys()].find(k => k.endsWith("/" + v));
    supplier = hit ? hit.split("/")[0] : "unknown";
  }
  return `${supplier}/${v}`;
}
function accelEntry(s) { return GPU_VARIANTS.get(skuAccelId(s)) || null; }
function accelName(s) {
  const e = accelEntry(s);
  return e ? e.variant.name : String(s.gpu).toUpperCase();
}
function fmtFlops(n) {
  if (n == null) return unk("not published");
  return Number(n).toLocaleString(undefined, { maximumFractionDigits: n < 100 ? 1 : 0 });
}
function fp16Dense(v) {
  const c = (v && v.compute) || {};
  return c.fp16_tensor_tflops_dense != null ? c.fp16_tensor_tflops_dense : null;
}
function precisionChips(v) {
  const native = (v && v.precision && v.precision.native) || [];
  return native.map(p => `<span class="chip">${esc(PRECISION_LABELS[p] || p)}</span>`).join("");
}
// Compact form for list tables: only the formats that differ between GPUs.
// FP32/FP16/TF32/INT8 are near-universal and stay on the GPU's own page.
const KEY_PRECISIONS = [["fp64", "FP64"], ["bf16", "BF16"], ["fp8", "FP8"], ["fp6", "FP6"], ["fp4", "FP4"]];
function precisionCompact(v) {
  const native = (v && v.precision && v.precision.native) || [];
  if (!native.length) return unk();
  const has = (k) => native.some(p => p === k || p.startsWith(k + "-"));
  const keys = KEY_PRECISIONS.filter(([k]) => has(k)).map(([, l]) => l);
  const full = native.map(p => PRECISION_LABELS[p] || p).join(", ");
  return `<span class="prec-compact" title="Native: ${esc(full)}">${keys.length ? keys.join(" · ") : `<span class="unk">FP32/FP16 only</span>`}</span>`;
}
function migLabel(mig) {
  if (!mig || mig.supported == null) return unk("not published");
  if (!mig.supported) return "No";
  const n = mig.max_slices == null ? "" : `${mig.max_slices} × `;
  const gb = mig.max_slice_memory_gb == null ? "" : `${mig.max_slice_memory_gb} GB`;
  return `${n}${gb}`.trim() || "Yes";
}
function featureLabel(f) {
  return FEATURE_LABELS[f] || f.replace(/-/g, " ").replace(/\b\w/g, ch => ch.toUpperCase());
}
function flopsCell(dense, sparse, unit = "TFLOPS") {
  if (dense == null && sparse == null) return unk("not published");
  if (dense != null && sparse != null) {
    return `${fmtFlops(dense)} / ${fmtFlops(sparse)} <span class="muted">${unit} dense / sparse</span>`;
  }
  return `${fmtFlops(dense ?? sparse)} <span class="muted">${unit}</span>`;
}
const SOURCE_META = {
  feed:   { label: "feed",      cls: "ok",   rank: 4 },
  api:    { label: "API",       cls: "ok",   rank: 4 },
  probe:  { label: "probe",     cls: "ok",   rank: 4 },
  page:   { label: "page",      cls: "warn", rank: 3 },
  datasheet: { label: "datasheet", cls: "info", rank: 3 },
  quote:  { label: "quote",     cls: "info", rank: 3 },
  tracker:{ label: "tracker",   cls: "bad",  rank: 2 },
  community: { label: "community", cls: "bad", rank: 1 },
  status_page: { label: "status", cls: "info", rank: 2 },
  postmortem: { label: "postmortem", cls: "info", rank: 2 },
};

const esc = (s) => String(s == null ? "" : s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;"}[c]));
// Missing values say why, in the small secondary style, instead of a bare dash.
const unk = (label = "not published", title = "") => `<span class="unk"${title ? ` title="${esc(title)}"` : ""}>${esc(label)}</span>`;
const money = (v) => v == null ? unk("no price") : "$" + Number(v).toFixed(2);
const num = (v) => v == null ? unk("not published") : v;
const siteHost = (u) => String(u || "").replace(/^https?:\/\/(www\.)?/, "").replace(/\/$/, "");
// Referral tag on every outbound link, so providers can attribute traffic back here.
// SITE_DOMAIN lives in serve_catalog.py and is substituted into this template at import.
const REFERRAL = "__SITE_DOMAIN__";
function refUrl(url) {
  if (!url || !/^https?:\/\//i.test(url)) return url;
  try {
    const u = new URL(url);
    if (!u.searchParams.has("utm_source")) u.searchParams.set("utm_source", REFERRAL);
    if (!u.searchParams.has("utm_medium")) u.searchParams.set("utm_medium", "referral");
    return u.toString();
  } catch (e) { return url; }
}
// One line per distinct package (same package in two regions shows once); out-of-stock lines dimmed.
function pkgLines(skus) {
  const seen = new Map();
  for (const s of skus.slice().sort((a, b) => (a.gpus_per_vm - b.gpus_per_vm) || String(a.variant || "").localeCompare(String(b.variant || "")))) {
    const t = packageLine(s);
    const cur = seen.get(t);
    seen.set(t, { off: cur ? cur.off && outOfStock(s) : outOfStock(s) });
  }
  return [...seen].map(([t, v]) => `<div class="pkg-line${v.off ? " off" : ""}">${esc(t)}${v.off ? `<span class="tag bad">sold out</span>` : ""}</div>`).join("");
}
// Two independent dimensions, never merged:
//   pricing       published (a rate card with on-demand prices exists) | quote (no published on-demand price)
//   provisioning  api (documented provisioning API) | console (web console / order flow) | sales (through sales)
function accessOf(p) {
  const skus = (CATALOG.allSkus || CATALOG.skus).filter(s => s.provider === p.id && s.status !== "retired");
  const priced = skus.filter(s => priceOf(s) != null);
  const quote = skus.length - priced.length;
  const soldOut = priced.filter(outOfStock).length;
  const hourly = priced.filter(s => billingOf(s) !== "monthly").length;
  const pricing = priced.length ? "published" : "quote";
  const api = p.api || {};
  const provisioning = api.provisioning === "sales" ? "sales"
    : api.provisioning === "api" && api.documented === true ? "api" : "console";
  const selfServe = provisioning !== "sales";
  const hasApi = provisioning === "api";
  return {
    pricing, provisioning, selfServe, hasApi, hourly, priced: priced.length, quote, soldOut,
    monthlyOnly: priced.length > 0 && hourly === 0,
    someMonthly: priced.length - hourly,
    provNote: api.notes || "",
  };
}
const PRICING_META = {
  published: { label: "Published rates", short: "Rate card", cls: "", title: "On-demand prices are published." },
  quote: { label: "Quote only", short: "Quote", cls: "warn", title: "No published on-demand price; contact sales for a quote or contract." },
};
const PROV_META = {
  api: { label: "API", cls: "ok", title: "Rent GPUs through a documented provisioning API (scripts, CLI, Terraform), or the console." },
  console: { label: "Console", cls: "", title: "Rent GPUs through the provider's web console or order flow; no documented provisioning API." },
  sales: { label: "Sales", cls: "", title: "No online ordering; GPU capacity is arranged through sales." },
};
const API_TITLE = "Documented provisioning API: instances can be created from scripts, CLI or Terraform.";
// Compact tags next to a provider name: always one pricing tag and one provisioning tag
// (defaults in neutral grey, exceptions coloured), plus MONTHLY when there is no hourly rental.
function accessTags(a) {
  const counts = [a.quote && a.pricing === "published" ? `${a.quote} on request` : "", a.soldOut ? `${a.soldOut} sold out` : ""].filter(Boolean).join(", ");
  const pm = PRICING_META[a.pricing], vm = PROV_META[a.provisioning];
  const t = [
    `<span class="mini ${a.pricing === "quote" ? "warn" : "muted-tag"}" title="${esc(pm.title + (counts ? " (" + counts + ")" : ""))}">${a.pricing === "quote" ? "Quote" : "Rate card"}</span>`,
    `<span class="mini ${a.provisioning === "api" ? "ok" : "muted-tag"}" title="${esc(a.provNote || vm.title)}">${vm.label}</span>`,
  ];
  if (a.monthlyOnly) t.push(`<span class="mini info" title="No hourly rental: every published price needs at least a one-month commitment.">Monthly</span>`);
  return t.join("");
}
// Relative "last checked" text for live numbers.
function ago(ts) {
  if (!ts) return "";
  const m = Math.max(0, Math.round((Date.now() - Date.parse(ts)) / 60000));
  return m < 1 ? "just now" : m < 60 ? `${m} min ago` : m < 1440 ? `${Math.round(m / 60)} h ago` : `${Math.round(m / 1440)} d ago`;
}
// Compact date for dense tables: "7 Nov" (adds the year only when it is not the current year).
function shortDate(d) {
  if (!d || d === "—") return "—";
  const dt = new Date(d + "T00:00:00Z");
  if (isNaN(dt)) return d;
  const opts = { day: "numeric", month: "short", timeZone: "UTC" };
  if (dt.getUTCFullYear() !== new Date().getUTCFullYear()) opts.year = "numeric";
  return dt.toLocaleDateString("en-GB", opts);
}
const dateOnly = (s) => (s || "").slice(0, 10) || "—";

function sourceInfo(s) {
  const sources = (s && s.sources) || [];
  if (!sources.length) return { label: "unknown", cls: "muted", rank: 0, title: "" };
  const best = sources.slice().sort((a, b) =>
    ((SOURCE_META[b.kind] || {}).rank || 0) - ((SOURCE_META[a.kind] || {}).rank || 0))[0];
  const meta = SOURCE_META[best.kind] || { label: best.kind || "unknown", cls: "muted", rank: 0 };
  return { ...meta, title: sources.map(x => `${x.kind}: ${x.url}`).join("\n") };
}
function obsInfo(a) {
  if (!a) return { label: "none", cls: "muted" };
  const via = a.observed_via || "unknown";
  if (via === "api" || via === "probe") return { label: via === "api" ? "API" : "probe", cls: "ok" };
  if (via === "console") return { label: "console", cls: "warn" };
  return { label: via, cls: "muted" };
}
const skusOf = (id) => (CATALOG.allSkus || CATALOG.skus).filter(s => s.provider === id);
const providerOf = (id) => CATALOG.providers.find(p => p.id === id) || {};
const priceOf = (s) => s.pricing && s.pricing.on_demand ? s.pricing.on_demand.usd_per_gpu_hr : null;
// Out-of-stock packages are listed but never set a "from"/min price: either the provider
// marks them sold out (status "unavailable") or the latest observation shows 0 free GPUs.
const latestObs = (s) => s.latest_availability || (s.availability && s.availability.last_observed_at ? s.availability : null);
const outOfStock = (s) => s.status === "unavailable" || (latestObs(s) != null && latestObs(s).available_gpus === 0);
const orderablePrice = (s) => s.status === "retired" || outOfStock(s) || s.self_serve === false ? null : priceOf(s);
// hourly = rentable by the hour; monthly = shortest commitment is a month (price shown per GPU-hour).
function billingOf(s) {
  if (s.billing_model) return s.billing_model;
  if (priceOf(s) == null) return null;
  const n = s.pricing.on_demand.native || {};
  if (n.derivation) return "monthly";
  const g = ((providerOf(s.provider).billing || {}).granularity || "").toLowerCase();
  return g === "month" ? "monthly" : "hourly";
}
// Cheapest orderable price: true hourly rates first; a monthly-commit rate only when no hourly one exists.
function bestOf(skus) {
  const ok = skus.filter(s => orderablePrice(s) != null);
  const pick = (list) => list.sort((a, b) => priceOf(a) - priceOf(b))[0];
  const h = pick(ok.filter(s => billingOf(s) !== "monthly"));
  if (h) return { v: priceOf(h), monthly: false, sku: h };
  const m = pick(ok.filter(s => billingOf(s) === "monthly"));
  if (m) return { v: priceOf(m), monthly: true, sku: m };
  const live = skus.filter(s => s.status !== "retired");
  const reason = live.some(s => priceOf(s) != null && outOfStock(s)) ? "sold out"
    : live.some(s => s.pricing_status === "quote_only") ? "on request" : "not published";
  return { v: null, monthly: false, sku: null, reason };
}
const MONTHLY_TAG = `<span class="tag warn" title="Shortest commitment is one month; shown as the per-GPU-hour equivalent. No hourly rental.">monthly</span>`;
const moneyBest = (b) => b.v == null ? unk(b.reason || "no price") : money(b.v) + (b.monthly ? " " + MONTHLY_TAG : "");
const vmOf = (s) => s.pricing && s.pricing.on_demand ? s.pricing.on_demand.usd_per_vm_hr : null;
// Host package spec in one cell: "104 vCPU · 1000 GB", per-GPU share as a small sub-line.
function hostSpec(s) {
  if (s.vcpus == null && s.ram_gb == null) return unk();
  const main = [s.vcpus != null ? `${s.vcpus} vCPU` : "vCPU n/p", s.ram_gb != null ? `${s.ram_gb} GB` : "RAM n/p"].join(" · ");
  const n = s.gpus_per_vm || 1;
  const per = n > 1 && s.vcpus != null && s.ram_gb != null ? `<span class="row-sub">${fmtFlops(s.vcpus / n)} vCPU · ${fmtFlops(s.ram_gb / n)} GB per GPU</span>` : "";
  return `<span class="host-spec">${main}</span>${per}`;
}
function priceCell(s, vm = false) {
  const v = vm ? vmOf(s) : priceOf(s);
  if (v != null && s.self_serve === false) return `${money(v)}<br><span class="tag warn" title="${esc(s.price_note || "Listed by the provider but not orderable self-serve; sales enquiry required.")}">sales only</span>`;
  if (v != null && outOfStock(s)) return `<span title="Listed price; currently out of stock. Not counted in minimum prices."><span class="price-off">${money(v)}</span><br><span class="tag bad">${s.status === "unavailable" ? "SOLD OUT" : "OUT OF STOCK"}</span></span>`;
  if (v != null) return money(v) + (billingOf(s) === "monthly" ? `<br>${MONTHLY_TAG}` : "");
  if (s.pricing_status === "quote_only") return unk("on request", s.price_note || "Price on request");
  return unk("not published");
}
// Spot/preemptible price shown as secondary metadata under the on-demand price.
function spotCell(s) {
  const sp = s.pricing && s.pricing.spot ? s.pricing.spot.usd_per_gpu_hr : null;
  if (sp == null) return "";
  const od = priceOf(s);
  const off = od ? Math.round((1 - sp / od) * 100) : null;
  const tip = `Spot price per GPU-hour${off != null && off > 0 ? `, ${off}% below on-demand` : ""}. Interruptible: capacity can be reclaimed.`;
  return `<span class="row-sub spot-sub" title="${esc(tip)}">spot ${money(sp)}${off != null && off > 0 ? ` · −${off}%` : ""}</span>`;
}
function committedOf(s) {
  const arr = (s.pricing && s.pricing.committed) || [];
  if (!arr.length) return null;
  return arr.slice().sort((a, b) => a.usd_per_gpu_hr - b.usd_per_gpu_hr)[0];
}
function skuId(s) {
  return skuAccelId(s);
}
function nvlinkOf(s) {
  if (s.form_factor === "sxm" || s.form_factor === "nvl") return true;
  if (s.form_factor === "pcie") return false;
  return null;
}
function capacityOfProvider(pid) {
  const c = (CATALOG.capacities || []).find(x => x.provider === pid) || null;
  const pools = (c && c.pools) || [];
  const sumField = (key) => {
    const vals = pools.map(p => p[key]).filter(v => v != null);
    return vals.length ? vals.reduce((a, b) => a + b, 0) : null;
  };
  const total = sumField("total_gpus");
  const rented = sumField("rented_gpus");
  const committed = sumField("committed_gpus");
  const freeReported = sumField("free_gpus");
  const poolPower = sumField("power_mw");
  const facility = (c && c.facility) || {};
  const power = poolPower != null ? poolPower
    : facility.gpu_power_mw != null ? facility.gpu_power_mw
    : facility.power_mw != null ? facility.power_mw : null;
  const allocKnown = rented != null || committed != null;
  const free = freeReported != null ? freeReported
    : (total != null && allocKnown ? Math.max(0, total - (rented || 0) - (committed || 0)) : null);
  // A total is partial when it covers only some GPU types, or a pool is itself a lower bound ("8,000+").
  const known = pools.filter(p => p.total_gpus != null);
  const unknown = pools.filter(p => p.total_gpus == null);
  const lowerBound = known.some(p => /\d\+|lower bound|minimum/i.test(p.notes || ""));
  const partial = total != null && (unknown.length > 0 || lowerBound);
  const partialNote = !partial ? "" : [
    known.length ? `${known.map(p => p.gpu).join(", ")} only` : "",
    unknown.length ? `${unknown.length} GPU ${unknown.length === 1 ? "type" : "types"} unpublished` : "",
  ].filter(Boolean).join(" · ");
  const indiaai = (c && c.indiaai_empanelled) || null;
  return { c, pools, total, rented, committed, free, power, partial, partialNote, indiaai, hasCapacity: total != null, notes: c && c.notes, capacityConfidence: c && c.confidence };
}
function liveFreeOf(pid) {
  // Availability is observed free capacity, not installed capacity.
  const rows = (CATALOG.latest_availability || []).filter(a => a.provider === pid && regionInScope(a.region) && originInScope(pid));
  const pools = new Map();
  for (const a of rows) {
    const shapeN = parseInt(a.shape, 10) || 1;
    const g = a.available_gpus != null ? a.available_gpus : (a.available_vms || 0) * shapeN;
    const key = `${String(a.gpu).toLowerCase()}|${a.region}`;
    if (!pools.has(key)) pools.set(key, { gpu: gpuName(a.gpu), region: a.region, shapes: new Set(), free: 0 });
    const pool = pools.get(key);
    if (a.shape) pool.shapes.add(a.shape);
    pool.free = Math.max(pool.free, g);
  }
  const poolRows = [...pools.values()].sort((a, b) => a.gpu.localeCompare(b.gpu) || a.region.localeCompare(b.region));
  const lastObserved = rows.reduce((t, r) => (r.ts && r.ts > t ? r.ts : t), "");
  return { rows: poolRows, total: poolRows.reduce((n, r) => n + r.free, 0), hasLive: poolRows.length > 0, poolCount: poolRows.length, lastObserved };
}

/* ---------------- GPUs ---------------- */
function gpuRows() {
  const map = new Map();
  for (const s of (CATALOG.allSkus || CATALOG.skus)) {
    const id = skuId(s);
    if (!map.has(id)) {
      const entry = GPU_VARIANTS.get(id);
      map.set(id, {
        id,
        name: entry ? entry.variant.name : String(s.gpu).toUpperCase(),
        familyId: entry ? entry.family.id : null,
        familyName: entry ? entry.family.name : String(s.gpu).toUpperCase(),
        familyArch: entry ? entry.family.architecture : null,
        variant: entry ? entry.variant : null,
        skus: [], providers: new Set(), orderable: new Set(), prices: [], updated: ""
      });
    }
    const g = map.get(id);
    g.skus.push(s);
    g.providers.add(s.provider);
    if (orderablePrice(s) != null) g.orderable.add(s.provider);
    const av = s.latest_availability;
    if (av && av.available_gpus != null) { g.avail = (g.avail || 0) + av.available_gpus; g.availObs = (g.availObs || 0) + 1; }
    if (orderablePrice(s) != null) g.prices.push(orderablePrice(s));
    const upd = dateOnly(s.verified_at);
    if (upd > g.updated) g.updated = upd;
  }
  return [...map.values()].map(g => ({
    ...g,
    vram: g.variant ? g.variant.vram_gb : (g.skus[0] ? g.skus[0].vram_gb_per_gpu : null),
    fp16: fp16Dense(g.variant),
    providerCount: g.orderable.size,
    providerTotal: g.providers.size,
    availNow: g.avail == null ? null : g.avail,
    availObs: g.availObs || 0,
    ...(() => {
      const b = bestOf(g.skus);
      // The headline is the cheapest hourly rate. Two things the headline alone hides:
      // a cheaper monthly-commitment rate, and that the cheapest rate may sit outside India.
      let alt = null;
      if (b.v != null && !b.monthly) {
        const m = g.skus
          .filter(s => orderablePrice(s) != null && billingOf(s) === "monthly")
          .sort((x, y) => orderablePrice(x) - orderablePrice(y))[0];
        if (m && orderablePrice(m) < b.v) alt = orderablePrice(m);
      }
      return { priceMin: b.v, priceMonthly: b.monthly, priceReason: b.reason, priceAltMonthly: alt,
               priceOutside: b.sku ? !isIndiaSku(b.sku) : false };
    })(),
    priceMax: g.prices.length ? Math.max(...g.prices) : null,
  }));
}
function priceRange(g) {
  return moneyBest({ v: g.priceMin, monthly: g.priceMonthly, reason: g.priceReason });
}
function gpuSortVal(g, key) {
  switch (key) {
    case "id": return g.name;
    case "vram": return g.vram == null ? -1 : g.vram;
    case "flops": return g.fp16 == null ? -1 : g.fp16;
    case "providers": return g.providerCount;
    case "avail": return g.availObs ? g.availNow : null;
    case "price": return g.priceMin == null ? Infinity : g.priceMin;
    case "updated": return g.updated;
    default: return "";
  }
}
function renderGPUs() {
  const all = gpuRows();
  let rows = all.filter(gpuMatches);
  renderFilterBar("gpus", rows.length, all.length);
  rows.sort((a, b) => {
    const x = gpuSortVal(a, SORT.gpus.key), y = gpuSortVal(b, SORT.gpus.key);
    if (typeof x === "number" && typeof y === "number") return (x - y) * SORT.gpus.dir;
    return String(x).localeCompare(String(y)) * SORT.gpus.dir;
  });

  $("count").textContent = `${all.length} GPU SKUs`;
  $("empty-gpus").classList.toggle("hidden", rows.length > 0);
  markArrows("thead-gpus", SORT.gpus);

  $("tbody-gpus").innerHTML = rows.map(g => {
    const href = `#/gpu/${encodeURIComponent(g.id)}`;
    const sub = [g.familyName, g.variant ? `${g.variant.vram_gb} GB ${g.variant.memory_type}` : null].filter(Boolean).join(" · ");
    return `
      <tr class="clickable" onclick="navigate('#/gpu/${encodeURIComponent(g.id)}')">
        <td><a class="sku-link" href="${href}"><span class="row-title">${esc(g.name)}</span><span class="row-sub">${esc(sub)}</span></a></td>
        <td class="num">${g.vram == null ? unk() : `${g.vram} GB`}</td>
        <td class="num val">${g.fp16 == null ? unk() : fmtFlops(g.fp16)}</td>
        <td>${precisionCompact(g.variant)}</td>
        <td class="num" title="${g.providerTotal > g.providerCount ? `${g.providerTotal} providers list this GPU; ${g.providerCount} can be ordered now` : ""}"><a class="sku-link" href="${href}">${g.providerCount}${g.providerTotal > g.providerCount ? `<span class="muted"> / ${g.providerTotal}</span>` : ""}</a></td>
        <td class="num" title="${g.availObs ? `${g.availObs} provider${g.availObs === 1 ? "" : "s"} publish stock for this GPU` : "No provider publishes stock for this GPU"}">${g.availObs ? g.availNow.toLocaleString() : unk("not published", "No provider publishes stock for this GPU")}</td>
        <td class="num strong">${priceRange(g)}${(() => {
          const parts = [];
          if (g.priceAltMonthly != null) parts.push(`or ${money(g.priceAltMonthly)} monthly`);
          if (g.priceOutside) parts.push("outside India");
          return parts.length ? `<span class="row-sub">${parts.join(" · ")}</span>` : "";
        })()}</td>
        <td class="num mono muted" title="${esc(g.updated)}">${esc(shortDate(g.updated))}</td>
      </tr>`;
  }).join("");
}

function renderGPUDetail(id) {
  const fam = GPU_FAMILIES.get(id);
  if (fam) return renderGPUFamily(fam);
  const entry = GPU_VARIANTS.get(id);
  showOnly("view-gpu-detail");
  window.scrollTo(0, 0);
  if (!entry) {
    $("view-gpu-detail").innerHTML = `<a class="back" href="#/gpus">← All GPUs</a><div class="empty">GPU SKU not found.</div>`;
    return;
  }
  renderGPUAccelerator(entry);
}

function shapeLabel(shape) { return String(shape || "").replace("x", "×"); }
function packageLine(s) {
  const vc = s.vcpus == null ? "vCPU n/p" : `${s.vcpus} vCPU`;
  const ram = s.ram_gb == null ? "RAM n/p" : `${s.ram_gb} GB`;
  const v = s.variant && s.variant !== "standard" ? ` · ${s.variant}` : "";
  return `${shapeLabel(s.shape)} · ${vc} / ${ram}${v}`;
}
function ratioPerGpu(value, n) {
  if (value == null || !n) return null;
  return value / n;
}

function renderGPUAccelerator(entry) {
  const { family, variant, key } = entry;
  const skus = (CATALOG.allSkus || CATALOG.skus).filter(s => skuId(s) === key);
  const best = bestOf(skus);
  const pmin = best.v;
  const updated = skus.map(s => dateOnly(s.verified_at)).sort().pop() || "—";
  const c = variant.compute || {};
  const fp16 = fp16Dense(variant);
  const features = variant.features || [];

  const byProvider = new Map();
  for (const s of skus) {
    if (!byProvider.has(s.provider)) byProvider.set(s.provider, {
      provider: s.provider, regions: new Set(), forms: new Set(), prices: [], skus: []
    });
    const g = byProvider.get(s.provider);
    g.regions.add(s.region);
    if (s.form_factor) g.forms.add(s.form_factor.toUpperCase());
    if (orderablePrice(s) != null) g.prices.push(orderablePrice(s));
    g.skus.push(s);
  }
  const rows = [...byProvider.values()].map(g => ({
    ...g,
    best: bestOf(g.skus),
    min: bestOf(g.skus).v,
    regionsText: [...g.regions].sort().join(", "),
    formsText: [...g.forms].sort().join(", "),
    packagesText: g.skus.slice().sort((a, b) => (a.gpus_per_vm - b.gpus_per_vm) || String(a.variant || "").localeCompare(String(b.variant || ""))).map(packageLine).join("; "),
  })).sort((a, b) => a.provider.localeCompare(b.provider));

  const pkgRows = skus.slice().sort((a, b) => a.provider.localeCompare(b.provider) || (a.gpus_per_vm - b.gpus_per_vm) || String(a.variant || "").localeCompare(String(b.variant || "")));

  // Providers that list this GPU but have nothing orderable right now, with the reason.
  const orderableProviders = rows.filter(g => g.skus.some(s => orderablePrice(s) != null));
  // Free GPUs actually reported for this accelerator; null everywhere else (unknown, not zero).
  const stockOf = (g) => g.skus.reduce((n, s) => n + ((latestObs(s) && latestObs(s).available_gpus) || 0), 0);
  const withStock = orderableProviders.filter(g => stockOf(g) > 0);
  const blockedProviders = rows.filter(g => !g.skus.some(s => orderablePrice(s) != null)).map(g => {
    const reasons = new Set();
    for (const s of g.skus) {
      if (s.status === "retired") continue;
      if (outOfStock(s)) reasons.add("out of stock");
      else if (s.self_serve === false) reasons.add("sales only");
      else if (s.pricing_status === "quote_only") reasons.add("on request");
      else reasons.add("no orderable package");
    }
    return { id: g.provider, name: (providerOf(g.provider).name || g.provider), why: [...reasons].join(", ") };
  });

  $("count").textContent = `${rows.length} ${rows.length === 1 ? "provider" : "providers"}`;
  $("view-gpu-detail").innerHTML = `
    <a class="back" href="#/gpus">← All GPUs</a>
    <div class="detail-head">
      <div style="flex:1">
        <h1>${esc(variant.name)}</h1>
        <div class="detail-sub">${esc(family.name)} family · ${esc((variant.form_factor || "—").toUpperCase())} · ${variant.vram_gb} GB ${esc(variant.memory_type || "")}</div>
      </div>
    </div>
    <div class="badges">
      <span class="pill">${esc(family.architecture || "—")}</span>
      <span class="pill">${esc(variant.memory_generation || variant.memory_type || "—")}</span>
      <span class="pill">Updated ${esc(updated)}</span>
      ${variant.mig && variant.mig.supported ? `<span class="pill">MIG ${esc(migLabel(variant.mig))}</span>` : ""}
    </div>
    <div class="stats">
      <div class="stat"><span>Price</span><b class="${pmin == null ? "none" : "accent"}">${money(pmin)}</b><span>${best.monthly ? "monthly commit /GPU-hr" : "on-demand /GPU-hr"}</span></div>
      <div class="stat"><span>FP16 dense</span><b>${fp16 == null ? "—" : fmtFlops(fp16)}</b><span>TFLOPS, common basis</span></div>
      <div class="stat"><span>VRAM / GPU</span><b>${variant.vram_gb}</b><span>GB ${esc(variant.memory_type || "")}</span></div>
      <div class="stat"><span>Memory bandwidth</span><b>${variant.memory_bandwidth_gbps == null ? "—" : fmtFlops(variant.memory_bandwidth_gbps) + " GB/s"}</b><span>per GPU</span></div>
      <div class="stat"><span>TDP</span><b>${variant.tdp_w == null ? "—" : variant.tdp_w + " W"}</b><span>per GPU</span></div>
      <div class="stat"><span>MIG</span><b>${esc(migLabel(variant.mig))}</b><span>${variant.mig && variant.mig.supported ? "slices" : "not supported"}</span></div>
    </div>

    <section>
      <h2>Specifications</h2>
      <div class="panel">
        <div class="table-scroll"><table id="gpu-spec-table">
          <tbody>
            <tr><td class="muted">Architecture</td><td>${esc(family.architecture || "—")}${family.generation && family.generation !== family.architecture ? ` · ${esc(family.generation)}` : ""}</td></tr>
            <tr><td class="muted">Form factor</td><td class="mono">${esc((variant.form_factor || "—").toUpperCase())}</td></tr>
            <tr><td class="muted">GPU VRAM</td><td>${variant.vram_gb} GB ${esc(variant.memory_type || "")}</td></tr>
            <tr><td class="muted">Memory bandwidth</td><td>${variant.memory_bandwidth_gbps == null ? unk() : fmtFlops(variant.memory_bandwidth_gbps) + " GB/s"}</td></tr>
            <tr><td class="muted">TDP</td><td>${variant.tdp_w == null ? unk() : variant.tdp_w + " W"}${variant.tdp_note ? ` <span class="muted">${esc(variant.tdp_note)}</span>` : ""}</td></tr>
            <tr><td class="muted">Interconnect</td><td>${variant.interconnect && variant.interconnect.type ? `${esc(String(variant.interconnect.type).toUpperCase())}${variant.interconnect.version ? " " + variant.interconnect.version : ""}${variant.interconnect.bandwidth_gbps ? " · " + fmtFlops(variant.interconnect.bandwidth_gbps) + " GB/s" : ""}` : "—"}${variant.interconnect && variant.interconnect.notes ? ` <span class="muted">${esc(variant.interconnect.notes)}</span>` : ""}</td></tr>
            <tr><td class="muted">MIG</td><td>${esc(migLabel(variant.mig))}${variant.mig && variant.mig.notes ? ` <span class="muted">${esc(variant.mig.notes)}</span>` : ""}</td></tr>
            <tr><td class="muted">Native precision</td><td>${precisionChips(variant) || unk()}${variant.precision && variant.precision.notes ? `<div class="note" style="padding:6px 0 0">${esc(variant.precision.notes)}</div>` : ""}</td></tr>
            <tr><td class="muted">FP64</td><td>${flopsCell(c.fp64_tflops, null)}</td></tr>
            <tr><td class="muted">FP64 Tensor</td><td>${flopsCell(c.fp64_tensor_tflops, null)}</td></tr>
            <tr><td class="muted">FP32</td><td>${flopsCell(c.fp32_tflops, null)}</td></tr>
            <tr><td class="muted">TF32 Tensor</td><td>${flopsCell(c.tf32_tensor_tflops_dense, c.tf32_tensor_tflops_sparse)}</td></tr>
            <tr><td class="muted">BF16 Tensor</td><td>${flopsCell(c.bf16_tensor_tflops_dense, c.bf16_tensor_tflops_sparse)}</td></tr>
            <tr><td class="muted">FP16 Tensor</td><td>${flopsCell(c.fp16_tensor_tflops_dense, c.fp16_tensor_tflops_sparse)}</td></tr>
            <tr><td class="muted">FP8 Tensor</td><td>${flopsCell(c.fp8_tensor_tflops_dense, c.fp8_tensor_tflops_sparse)}</td></tr>
            <tr><td class="muted">FP6 Tensor</td><td>${flopsCell(c.fp6_tflops_dense, c.fp6_tflops_sparse)}</td></tr>
            <tr><td class="muted">FP4 Tensor</td><td>${flopsCell(c.fp4_tops_dense, c.fp4_tops_sparse, "TOPS")}</td></tr>
            <tr><td class="muted">INT8 Tensor</td><td>${flopsCell(c.int8_tops_dense, c.int8_tops_sparse, "TOPS")}</td></tr>
            <tr><td class="muted">Capabilities</td><td>${features.map(f => `<span class="chip">${esc(featureLabel(f))}</span>`).join("") || unk()}</td></tr>
          </tbody>
        </table></div>
        <div class="note">FLOPS are per GPU. Where two numbers are shown, they are dense / sparse. Host vCPU and RAM are sold separately in provider packages.</div>
      </div>
    </section>

    <section>
      <h2>Providers <span class="h2-note muted">— ${orderableProviders.length} of ${rows.length} list ${esc(variant.name)} with an orderable price${withStock.length ? `, ${withStock.length} report free GPUs` : ""}</span></h2>
      <div class="panel">
        ${rows.length ? `
        <div class="table-scroll"><table id="gpu-provider-table">
          <thead><tr>
            <th data-sort="provider">Provider</th>
            <th data-sort="regions">Regions</th>
            <th data-sort="packages">Host packages</th>
            <th data-sort="form">Form</th>
            <th class="num" data-sort="price" data-type="num">From /GPU-hr</th>
          </tr></thead>
          <tbody>
            ${rows.map(g => {
              const p = providerOf(g.provider);
              return `<tr>
                <td data-v="${esc(p.name || g.provider)}"><img class="logo" src="/assets/logos/${esc(g.provider)}.png" alt="" onerror="this.style.visibility='hidden'"><a class="provider-name" href="#/provider/${esc(g.provider)}">${esc(p.name || g.provider)}</a></td>
                <td class="mono" data-v="${esc(g.regionsText)}">${esc(g.regionsText)}${g.skus.some(x => !isIndiaSku(x)) ? `<span class="tag warn" style="display:block;width:max-content" title="Runs outside India: no India data residency">outside India</span>` : ""}</td>
                <td data-v="${esc(g.packagesText)}">${pkgLines(g.skus)}</td>
                <td data-v="${esc(g.formsText)}">${[...g.forms].sort().map(f => `<span class="chip">${esc(f)}</span>`).join("") || unk()}</td>
                <td class="num strong" data-v="${g.min ?? 999999}">${moneyBest(g.best)}</td>
              </tr>`;
            }).join("")}
          </tbody>
        </table></div>` : `<div class="note">No provider sells this GPU SKU yet.</div>`}
        ${orderableProviders.length && withStock.length < orderableProviders.length ? `<div class="note" style="margin:8px 0 0">${withStock.length
          ? `Free GPUs are reported by ${withStock.length} of ${orderableProviders.length} (${withStock.map(g => esc(providerOf(g.provider).name || g.provider)).join(", ")}). The rest publish a rate but no stock numbers, so for them the price is verified and the availability is not.`
          : `No provider reports free ${esc(variant.name)}: the rates above are verified, the availability is not.`}</div>` : ""}
      </div>
    </section>

    <section>
      <h2>Host packages <span class="h2-note muted">— exact vCPU, host RAM and price per package</span></h2>
      <div class="panel">
        ${pkgRows.length ? `
        <div class="table-scroll"><table id="gpu-package-table">
          <thead><tr>
            <th data-sort="provider">Provider</th>
            <th data-sort="region">Region</th>
            <th data-sort="package">Package</th>
            <th class="num" data-sort="vcpu" data-type="num" title="Host vCPU and RAM for the whole VM; per-GPU share below">vCPU · RAM</th>
            <th class="num" data-sort="price" data-type="num">/GPU-hr</th>
            <th class="num" data-sort="vmprice" data-type="num">/VM-hr</th>
          </tr></thead>
          <tbody>
            ${pkgRows.map(s => {
              const p = providerOf(s.provider);
              const vcPer = ratioPerGpu(s.vcpus, s.gpus_per_vm);
              const ramPer = ratioPerGpu(s.ram_gb, s.gpus_per_vm);
              const pkg = `${shapeLabel(s.shape)}${s.variant && s.variant !== "standard" ? ` · ${s.variant}` : ""}`;
              return `<tr>
                <td data-v="${esc(p.name || s.provider)}"><img class="logo" src="/assets/logos/${esc(s.provider)}.png" alt="" onerror="this.style.visibility='hidden'"><a class="provider-name" href="#/provider/${esc(s.provider)}">${esc(p.name || s.provider)}</a></td>
                <td class="mono muted" data-v="${esc(s.region)}">${esc(s.region)}${isIndiaSku(s) ? "" : `<span class="tag warn" style="display:block;width:max-content" title="Runs outside India: no India data residency">outside India</span>`}</td>
                <td class="mono wrap" data-v="${esc(pkg)}">${esc(pkg)}</td>
                <td class="num" data-v="${s.vcpus ?? -1}">${hostSpec(s)}</td>
                <td class="num strong" data-v="${priceOf(s) ?? 999999}">${priceCell(s)}${spotCell(s)}</td>
                <td class="num" data-v="${vmOf(s) ?? 999999}">${priceCell(s, true)}</td>
              </tr>`;
            }).join("")}
          </tbody>
        </table></div>` : `<div class="note">No host package data yet.</div>`}
      </div>
      ${blockedProviders.length ? `<div class="panel" style="margin-top:10px">
        <div class="note" style="margin:0"><b>Listed but not orderable now</b> — ${blockedProviders.map(b => `<a class="provider-name" href="#/provider/${esc(b.id)}">${esc(b.name)}</a> <span class="muted">(${esc(b.why)})</span>`).join(" · ")}</div>
      </div>` : ""}
    </section>
  `;
  enableDomSort($("gpu-provider-table"));
  enableDomSort($("gpu-package-table"));
}

function renderGPUFamily(family) {
  showOnly("view-gpu-detail");
  window.scrollTo(0, 0);
  const supplier = String(family.id).split("/")[0];
  const variants = (family.variants || []).map(v => {
    const key = `${supplier}/${v.id}`;
    const skus = (CATALOG.allSkus || CATALOG.skus).filter(s => skuId(s) === key);
    const best = bestOf(skus);
    return {
      v, key, skus, best,
      providers: new Set(skus.map(s => s.provider)),
      min: best.v,
      fp16: fp16Dense(v),
    };
  });
  const allProviders = new Set(variants.flatMap(x => [...x.providers]));
  const from = bestOf(variants.flatMap(x => x.skus));
  $("count").textContent = `${variants.length} ${variants.length === 1 ? "GPU SKU" : "GPU SKUs"}`;
  $("view-gpu-detail").innerHTML = `
    <a class="back" href="#/gpus">← All GPUs</a>
    <div class="detail-head">
      <div style="flex:1">
        <h1>${esc(family.name)}</h1>
        <div class="detail-sub">${esc(family.architecture || "—")} · ${variants.length} accelerator ${variants.length === 1 ? "SKU" : "SKUs"}</div>
      </div>
    </div>
    <div class="stats">
      <div class="stat"><span>GPU SKUs</span><b>${variants.length}</b></div>
      <div class="stat"><span>Providers</span><b>${allProviders.size}</b></div>
      <div class="stat"><span>From</span><b class="${from.v == null ? "none" : "accent"}">${money(from.v)}</b><span>${from.monthly ? "monthly commit /GPU-hr" : "on-demand /GPU-hr"}</span></div>
    </div>
    <section>
      <h2>Accelerator SKUs</h2>
      <div class="panel">
        <div class="table-scroll"><table id="gpu-variant-table">
          <thead><tr>
            <th data-sort="name">GPU SKU</th>
            <th class="num" data-sort="vram" data-type="num">VRAM</th>
            <th data-sort="memory">Memory</th>
            <th class="num" data-sort="flops" data-type="num">FP16 dense</th>
            <th title="Key native formats; hover a cell for the full list">Precision</th>
            <th class="num" data-sort="tdp" data-type="num">TDP</th>
            <th data-sort="mig">MIG</th>
            <th class="num" data-sort="providers" data-type="num">Providers</th>
            <th class="num" data-sort="price" data-type="num">From</th>
          </tr></thead>
          <tbody>
            ${variants.map(({ v, key, providers, min, best, fp16 }) => `<tr class="clickable" onclick="navigate('#/gpu/${encodeURIComponent(key)}')">
              <td><a class="sku-link" href="#/gpu/${encodeURIComponent(key)}"><span class="row-title">${esc(v.name)}</span><span class="row-sub">${esc((v.form_factor || "").toUpperCase())} · ${v.vram_gb} GB</span></a></td>
              <td class="num" data-v="${v.vram_gb}">${v.vram_gb} GB</td>
              <td data-v="${esc(v.memory_type || "")}">${v.memory_type ? esc(v.memory_type) : unk()}</td>
              <td class="num val" data-v="${fp16 ?? -1}">${fp16 == null ? unk() : fmtFlops(fp16)}</td>
              <td>${precisionCompact(v)}</td>
              <td class="num" data-v="${v.tdp_w ?? -1}">${v.tdp_w == null ? unk() : v.tdp_w + " W"}</td>
              <td data-v="${esc(migLabel(v.mig))}">${esc(migLabel(v.mig))}</td>
              <td class="num" data-v="${providers.size}">${providers.size}</td>
              <td class="num strong" data-v="${min ?? 999999}">${moneyBest(best)}</td>
            </tr>`).join("")}
          </tbody>
        </table></div>
        <div class="note">An accelerator SKU owns VRAM, memory bandwidth, FLOPS and MIG. The same SKU can be sold by providers in different host packages; vCPU and host RAM live on those packages.</div>
      </div>
    </section>
  `;
  enableDomSort($("gpu-variant-table"));
}

/* ---------------- Providers ---------------- */
function providerRow(p) {
  const skus = skusOf(p.id);
  const capacity = capacityOfProvider(p.id);
  const live = liveFreeOf(p.id);
  const rel = p.reliability || {};
  const gpuModels = [...new Set(skus.map(s => accelName(s)))].sort();
  const gpuOrderable = new Set(skus.filter(s => orderablePrice(s) != null).map(s => accelName(s)));
  const updated = skus.map(s => dateOnly(s.verified_at)).sort().pop() || dateOnly(p.verified_at);
  const st = p.storage || {};
  return {
    p, skus,
    name: (p.name || p.id).toLowerCase(),
    regions: (p.regions || []).join(", "),
    gpuModels,
    gpuOrderable,
    gpus: gpuModels.join(", "),
    capVpc: !!(p.networking && p.networking.vpc),
    capMountable: st.mountable === true || st.block_usd_per_gb_mo != null || st.file_usd_per_gb_mo != null,
    capShared: st.shared === true,
    capPersistent: st.persistent === true,
    capObject: st.object_s3_compatible === true,
    capCpu: !!(p.capabilities && p.capabilities.cpu_vm === true),
    access: accessOf(p),
    pindex: priceIndex(p.id),
    capacity: capacity.total,
    capacityKnown: capacity.hasCapacity,
    capacityPartial: capacity.partial,
    indiaai: capacity.indiaai,
    capacityNote: capacity.partialNote,
    freeLive: live.hasLive ? live.total : null,
    power: capacity.power,
    poolCount: live.poolCount,
    lastObserved: live.lastObserved,
    capacityPoolCount: capacity.pools.length,
    sla: rel.sla_pct,
    updated,
  };
}
// One compact cell instead of four Yes/— columns: list only what the provider has.
function featureChips(r) {
  const f = [
    [r.capVpc, "VPC", "Private networking / VPC"],
    [r.capMountable, "Block/File", "Mountable block or file storage — where downloaded model weights are kept"],
    [r.capShared, "Shared FS", "File storage mountable on several nodes at once"],
    [r.capObject, "S3", "S3-compatible object storage"],
    [r.capCpu, "CPU VMs", "Also rents CPU-only VMs"],
  ].filter(x => x[0]);
  return f.length ? f.map(([, l, t]) => `<span class="feat" title="${esc(t)}">${l}</span>`).join("") : unk("none published", "None of VPC, mountable storage, object storage or CPU VMs is published");
}
// Price vs market. For every GPU model (accelerator SKU) in the current scope, the market
// median is taken over each provider's cheapest orderable price for that model. A provider's
// index is the geometric mean of (its price / market median) across its models.
let MARKET = null;
function marketMedians() {
  if (MARKET && MARKET.skus === CATALOG.skus) return MARKET.byKey;
  const per = new Map();   // key -> Map(provider -> best)
  for (const s of CATALOG.skus) {
    const k = skuId(s);
    if (!per.has(k)) per.set(k, new Map());
    const m = per.get(k);
    if (!m.has(s.provider)) m.set(s.provider, []);
    m.get(s.provider).push(s);
  }
  const byKey = new Map();
  for (const [k, provs] of per) {
    // A provider can price both markets: its cheapest hourly package feeds the hourly median,
    // its cheapest monthly package feeds the monthly median.
    const hourly = [], monthly = [];
    for (const list of provs.values()) {
      const ok = list.filter(s => orderablePrice(s) != null);
      const h = ok.filter(s => billingOf(s) !== "monthly").sort((a, b) => priceOf(a) - priceOf(b))[0];
      const m = ok.filter(s => billingOf(s) === "monthly").sort((a, b) => priceOf(a) - priceOf(b))[0];
      if (h) hourly.push(priceOf(h));
      if (m) monthly.push(priceOf(m));
    }
    const med = (a) => { if (!a.length) return null; const x = [...a].sort((p, q) => p - q), m = x.length >> 1; return x.length % 2 ? x[m] : (x[m - 1] + x[m]) / 2; };
    byKey.set(k, { hourly: med(hourly), nHourly: hourly.length, monthly: med(monthly), nMonthly: monthly.length });
  }
  MARKET = { skus: CATALOG.skus, byKey };
  return byKey;
}
function priceIndex(pid) {
  const med = marketMedians();
  const mine = CATALOG.skus.filter(s => s.provider === pid);
  if (!mine.length) return null;
  const byKey = new Map();
  for (const s of mine) { const k = skuId(s); if (!byKey.has(k)) byKey.set(k, []); byKey.get(k).push(s); }
  const rows = [];
  let monthlyBased = false;
  for (const [k, list] of byKey) {
    const b = bestOf(list), m = med.get(k);
    if (b.v == null || !m) continue;
    // compare like with like: hourly vs hourly market, monthly-only vs monthly market
    // Never price a monthly commitment against an hourly market.
    const ref = b.monthly ? (m.nMonthly >= 3 ? m.monthly : null) : (m.nHourly >= 3 ? m.hourly : null);
    if (!ref) continue;
    if (b.monthly) monthlyBased = true;
    const entry = GPU_VARIANTS.get(k);
    rows.push({ name: entry ? entry.variant.name : k, price: b.v, ref, ratio: b.v / ref, monthly: b.monthly });
  }
  if (!rows.length) return { index: null, rows, monthlyBased };
  const index = Math.exp(rows.reduce((a, r) => a + Math.log(r.ratio), 0) / rows.length);
  return { index, rows: rows.sort((a, b) => a.name.localeCompare(b.name)), monthlyBased };
}
function priceIndexCell(r) {
  const pi = r.pindex;
  if (!pi) return unk("none in region");
  if (pi.index == null) {
    const anyOrderable = (r.skus || []).some(s => orderablePrice(s) != null);
    const anySalesOnly = (r.skus || []).some(s => s.self_serve === false);
    if (!anyOrderable && anySalesOnly) return unk("sales only", "Every package is sold through sales, so there is no self-serve price to compare");
    return r.access && r.access.pricing === "quote" ? unk("quote only") : unk("too few comparable", "Its GPU models are offered by fewer than 3 providers in this region, or have no orderable price");
  }
  const pct = Math.round((pi.index - 1) * 100);
  const cls = pct <= -5 ? "ok" : pct >= 5 ? "bad" : "muted";
  const label = Math.abs(pct) < 5 ? "≈ market" : `${pct > 0 ? "+" : "−"}${Math.abs(pct)}%`;
  const tip = pi.rows.map(x => `${x.name}: ${money(x.price).replace(/<[^>]+>/g, "")}${x.monthly ? " (monthly)" : ""} vs median ${money(x.ref).replace(/<[^>]+>/g, "")} (${x.ratio >= 1 ? "+" : "−"}${Math.abs(Math.round((x.ratio - 1) * 100))}%)`).join("\n");
  return `<span class="pidx ${cls}" title="${esc(tip)}">${label}</span><span class="meta">${pi.rows.length} GPU${pi.rows.length === 1 ? "" : "s"}${pi.monthlyBased ? " · incl. monthly" : ""}</span>`;
}
function providerSortVal(r, key) {
  switch (key) {
    case "name": return r.name;
    case "regions": return r.regions.toLowerCase();
    case "gpus": return r.gpus.toLowerCase();
    case "vpc": return r.capVpc ? 1 : 0;
    case "mountable": return r.capMountable ? 1 : 0;
    case "object": return r.capObject ? 1 : 0;
    case "cpu": return r.capCpu ? 1 : 0;
    // null = unknown; unknown always sorts last, whichever direction is clicked
    case "pindex": return r.pindex && r.pindex.index != null ? r.pindex.index : null;
    case "features": return [r.capVpc, r.capMountable, r.capObject, r.capCpu].filter(Boolean).length;
    case "capacity": return r.capacity;
    case "free": return r.freeLive;
    case "pools": return r.poolCount;
    case "sla": return r.sla;
    case "updated": return r.updated;
    default: return "";
  }
}
// Tie-break for equal Price vs market results: the provider you can actually buy from now wins.
// Documented API first, then console, then sales; an hourly on-demand package before monthly-only.
function accessRank(r) {
  const a = r.access || {};
  const prov = a.provisioning === "api" ? 2 : a.provisioning === "console" ? 1 : 0;
  return prov * 2 + (a.hourly > 0 ? 1 : 0);
}
function renderProviders() {
  const all = CATALOG.providers.map(providerRow);
  let rows = all.filter(providerMatches);
  // With a GPU filter the list is availability-based, so say who sells the GPU but cannot
  // serve it right now - otherwise "why is provider X missing?" is unanswerable.
  const gpuFilter = FILTERS.providers.gpu;
  const listedOnly = gpuFilter
    ? all.filter(r => r.skus.some(s => s.gpu === gpuFilter && s.status !== "retired")
        && !r.skus.some(s => s.gpu === gpuFilter && orderablePrice(s) != null))
    : [];
  const gpuNote = !gpuFilter ? "" : listedOnly.length
    ? `${listedOnly.length} also list ${esc(gpuFilter)} but nothing is orderable now: <span title="${esc(listedOnly.map(r => r.p.name || r.p.id).join(", "))}">${esc(listedOnly.map(r => r.p.name || r.p.id).join(", "))}</span>`
    : (rows.length ? "" : `No provider has an orderable ${esc(gpuFilter)} right now.`);
  renderFilterBar("providers", rows.length, all.length, gpuNote);
  rows.sort((a, b) => {
    const key = SORT.providers.key, dir = SORT.providers.dir;
    const x = providerSortVal(a, key), y = providerSortVal(b, key);
    if (x == null || y == null) return (x == null) - (y == null);   // unknowns last in both directions
    if (key === "pindex") {
      // Same displayed result (the rounded %) → API + on-demand wins, then the finer index.
      const px = Math.round((x - 1) * 100), py = Math.round((y - 1) * 100);
      if (px !== py) return (px - py) * dir;
      const rx = accessRank(a), ry = accessRank(b);
      if (rx !== ry) return ry - rx;
      return (x - y) * dir;
    }
    if (typeof x === "number" && typeof y === "number") return (x - y) * dir;
    return String(x).localeCompare(String(y)) * dir;
  });

  $("count").textContent = `${all.length} providers`;
  $("empty-providers").classList.toggle("hidden", rows.length > 0);
  markArrows("thead-providers", SORT.providers);

  $("tbody-providers").innerHTML = rows.map(r => {
    const p = r.p;
    const iai = r.indiaai ? `<span class="meta" title="${esc("GPUs empanelled for the IndiaAI Mission (offered under the tender, not necessarily operational). Not installed fleet.")}">IndiaAI: ${r.indiaai.total.toLocaleString()}</span>` : "";
    const capLines = [];
    capLines.push(r.capacity == null
      ? `<span class="muted">—</span>`
      : `<span class="cap-total" title="${esc(r.capacityPartial ? "Partial: " + r.capacityNote : "Installed fleet")}">${r.capacity.toLocaleString()}${r.capacityPartial ? "+" : ""}</span>${r.capacityPartial ? `<span class="meta">${esc(r.capacityNote)}</span>` : ""}${iai}`);
    if (r.power != null) capLines.push(`<span class="muted">${r.power.toLocaleString()} MW</span>`);
    const cap = (r.capacity == null && r.power == null)
      ? unk("not published", "Fleet size not published by the provider") + iai
      : `<a class="cap-link cap-stack" href="#/provider/${esc(p.id)}/inventory" title="Deployed capacity and inventory.">${capLines.join("<br>")}</a>`;
    const inv = p.inventory_check;
    const invLabel = !inv || !inv.last_checked_at ? "no logged-in check"
      : inv.inventory === "visible" ? `checked ${ago(inv.last_checked_at)}`
      : inv.inventory === "empty" ? `checked ${ago(inv.last_checked_at)} · no inventory`
      : inv.inventory === "not-exposed" ? `checked ${ago(inv.last_checked_at)} · no stock shown`
      : `checked ${ago(inv.last_checked_at)} · unknown`;
    const invTip = inv ? `Last logged-in inventory check: ${inv.last_checked_at || "never"} (${inv.inventory}). ${inv.blockers || inv.notes || ""}`.trim() : "No logged-in inventory check recorded";
    const free = (r.freeLive == null
      ? unk("not published", "The provider doesn't publish stock. This is unknown, not zero.")
      : `<a class="cap-link" href="#/provider/${esc(p.id)}/inventory" title="Latest observation: GPUs available to start right now. Availability, not installed capacity.">${r.freeLive.toLocaleString()}</a><span class="meta">${esc(ago(r.lastObserved))}</span>`)
      + `<span class="meta" title="${esc(invTip)}">${esc(invLabel)}</span>`;
    const slaCls = r.sla == null ? "muted" : r.sla >= 99.9 ? "ok" : "warn";
    return `
      <tr>
        <td><div class="prov-wrap"><img class="logo" src="/assets/logos/${esc(p.id)}.png" alt="" onerror="this.style.visibility='hidden'"><span class="prov-cell"><span><a class="provider-name" href="#/provider/${esc(p.id)}">${esc(p.name || p.id)}</a><span class="taggroup">${accessTags(r.access)}${countryTag(p)}</span></span><span class="prov-sub">${p.website ? `<a class="site-link" href="${esc(refUrl(p.gpu_page || p.website))}" target="_blank" rel="noopener noreferrer" title="${esc(p.gpu_page ? "GPU offerings: " + p.gpu_page : p.website)}">${esc(siteHost(p.gpu_page || p.website))} ↗</a>` : ""}${r.regions ? `<span class="regions" title="Regions">${p.website ? " · " : ""}${esc(r.regions)}</span>` : ""}</span></span></div></td>
        <td class="gpu-cell">${r.gpuModels.length ? (() => {
          const ordered = [...r.gpuModels].sort((a, b) => (r.gpuOrderable.has(b) ? 1 : 0) - (r.gpuOrderable.has(a) ? 1 : 0) || a.localeCompare(b));
          const shown = ordered.slice(0, 4);
          const rest = ordered.slice(4);
          const chip = g => r.gpuOrderable.has(g)
            ? `<span class="chip" title="Orderable now">${esc(g)}</span>`
            : `<span class="chip chip-out" title="No orderable package right now (out of stock or sales only)">${esc(g)}</span>`;
          const more = rest.length ? `<span class="chip chip-out" title="${esc(rest.join(", "))}">+${rest.length}</span>` : "";
          return shown.map(chip).join("") + more;
        })() : `<span class="muted">—</span>`}</td>
        <td class="num">${priceIndexCell(r)}</td>
        <td class="feat-cell">${featureChips(r)}</td>
        <td class="num">${cap}</td>
        <td class="num">${free}</td>
        <td class="num ${slaCls}">${r.sla == null ? unk() : r.sla + "%"}</td>
        <td class="num mono muted" title="${esc(r.updated)}">${esc(shortDate(r.updated))}</td>
      </tr>`;
  }).join("");
}

/* ---------------- Provider detail ---------------- */
function renderProviderDetail(id) {
  const p = CATALOG.providers.find(x => x.id === id);
  showOnly("view-provider-detail");
  window.scrollTo(0, 0);
  if (!p) {
    $("view-provider-detail").innerHTML = `<a class="back" href="#/providers">← All providers</a><div class="empty">Provider not found.</div>`;
    return;
  }
  const skus = skusOf(id);
  const gpus = [...new Set(skus.map(s => accelName(s)))].sort();
  const src = skus.map(sourceInfo).sort((a, b) => b.rank - a.rank)[0] || sourceInfo(p);
  const capacity = capacityOfProvider(id);
  const live = liveFreeOf(id);
  const cheapestBest = bestOf(skus);
  const cheapest = cheapestBest.sku;
  const rel = p.reliability || {};
  const invRows = live.rows;

  $("count").textContent = `${skus.length} ${skus.length === 1 ? "host package" : "host packages"}`;
  $("view-provider-detail").innerHTML = `
    <a class="back" href="#/providers">← All providers</a>
    <div class="detail-head">
      <img class="logo-lg" src="/assets/logos/${esc(p.id)}.png" alt="" onerror="this.style.visibility='hidden'">
      <div style="flex:1">
        <h1>${esc(p.name || p.id)}${countryTag(p) ? ` <span style="font-size:12px;vertical-align:middle">${countryTag(p)}</span>` : ""}</h1>
        ${p.website ? `<a class="site-url" href="${esc(refUrl(p.gpu_page || p.website))}" target="_blank" rel="noopener noreferrer">${esc(siteHost(p.gpu_page || p.website))} ↗</a>` : ""}
        <div class="detail-sub">${esc((p.regions || []).join(", ") || "India")}${rel.sla_pct != null ? ` · ${rel.sla_pct}% SLA` : ""}</div>
      </div>
      <span class="pill ${p.status === "active" ? "ok" : p.status === "beta" ? "warn" : p.status === "deprecated" || p.status === "retired" ? "bad" : ""}">${esc(p.status || "—")}</span>
    </div>

    <div class="badges">
      ${(() => { const a = accessOf(p); const pm = PRICING_META[a.pricing], vm = PROV_META[a.provisioning];
        return `<span class="pill ${pm.cls}" title="${esc(pm.title)}">${pm.label}</span>`
        + `<span class="pill ${vm.cls}" title="${esc(a.provNote || vm.title)}">${vm.label}</span>`
        + (a.monthlyOnly ? `<span class="pill info" title="Every published price needs at least a one-month commitment.">monthly only</span>`
           : a.someMonthly ? `<span class="pill" title="${a.hourly} packages bill hourly; ${a.someMonthly} need a monthly commitment.">hourly + monthly</span>` : ""); })()}
      ${accessOf(p).pricing === "quote" ? "" : `<span class="pill" title="${esc(src.title)}">prices: ${src.label === "API" ? "provider API" : src.label}</span>`}
      <span class="pill ${p.confidence === "high" ? "ok" : p.confidence === "low" ? "warn" : ""}">${esc(p.confidence || "—")} confidence</span>
      ${p.compliance && p.compliance.meity ? `<span class="pill">MeitY</span>` : ""}
      ${p.compliance && p.compliance.dpdp ? `<span class="pill">DPDP</span>` : ""}
      ${p.networking && p.networking.vpc ? `<span class="pill">VPC</span>` : ""}
    </div>

    <div class="stats">
      <div class="stat"><span>SKUs</span><b>${skus.length}</b></div>
      <div class="stat"><span>GPU SKUs</span><b>${gpus.length || "—"}</b></div>
      ${(() => { const pi = priceIndex(id); if (!pi || pi.index == null) return ""; const pct = Math.round((pi.index - 1) * 100);
        return `<div class="stat"><span>Price vs market</span><b class="${pct <= -5 ? "ok" : pct >= 5 ? "bad" : ""}">${Math.abs(pct) < 5 ? "≈ market" : (pct > 0 ? "+" : "−") + Math.abs(pct) + "%"}</b><span>across ${pi.rows.length} GPU model${pi.rows.length === 1 ? "" : "s"} in region</span></div>`; })()}
      <div class="stat"><span>${cheapestBest.monthly ? "Cheapest (monthly)" : "Cheapest on-demand"}</span><b class="${cheapest ? "accent" : "none"}">${cheapest ? money(priceOf(cheapest)) : "—"}</b></div>
      <div class="stat"><span>Capacity</span><b class="${capacity.total == null ? "none" : ""}">${capacity.total == null ? "—" : capacity.total.toLocaleString() + (capacity.partial ? "+" : "")}</b><span>${capacity.total == null ? "fleet size not published" : capacity.partial ? esc(capacity.partialNote) : "GPUs deployed"}</span></div>
      <div class="stat"><span>Available now</span><b class="${!live.hasLive ? "none" : live.total > 0 ? "ok" : "bad"}">${live.hasLive ? live.total.toLocaleString() : "—"}</b><span>${live.hasLive ? `observed ${esc(ago(live.lastObserved))}` : "stock not published"}</span></div>
      <div class="stat"><span>Power</span><b class="${capacity.power == null ? "none" : ""}">${capacity.power == null ? "—" : capacity.power.toLocaleString() + " MW"}</b><span>${capacity.power == null ? "not published" : "GPU fleet"}</span></div>
    </div>

    <section>
      <h2>Host packages & pricing</h2>
      <div class="panel">
        ${skus.length ? `
        <div class="table-scroll"><table id="provider-sku-table">
          <thead><tr>
            <th data-sort="gpu">GPU SKU</th><th data-sort="shape">Shape</th><th data-sort="region">Region</th>
            <th class="num" data-sort="vcpus" data-type="num" title="Host vCPU and RAM for the whole VM; per-GPU share below">vCPU · RAM</th>
            <th class="num" data-sort="price" data-type="num">On-demand</th>
            <th class="num" data-sort="vm" data-type="num">Per VM</th>
            <th class="num" data-sort="committed" data-type="num">Committed</th>
            <th class="num" data-sort="freevms" data-type="num" title="Latest observation: on-demand VMs available to start right now. Availability, not capacity">Available VMs</th>
          </tr></thead>
          <tbody>
            ${skus.sort((a,b) => accelName(a).localeCompare(accelName(b)) || a.shape.localeCompare(b.shape)).map(s => {
              const a = s.latest_availability;
              const c = committedOf(s);
              const capTxt = a && a.available_vms != null ? `${a.available_vms}` : unk("not published", "The provider doesn't publish stock. This is unknown, not zero.");
              const vcPer = ratioPerGpu(s.vcpus, s.gpus_per_vm);
              const ramPer = ratioPerGpu(s.ram_gb, s.gpus_per_vm);
              return `<tr>
                <td class="mono" data-v="${esc(accelName(s))}">${GPU_VARIANTS.has(skuId(s)) ? `<a class="sku-link" href="#/gpu/${encodeURIComponent(skuId(s))}"><span class="row-title">${esc(accelName(s))}</span></a>` : esc(accelName(s))}<span class="row-sub">${s.vram_gb_per_gpu ?? "?"} GB${s.form_factor ? ` · ${esc(s.form_factor.toUpperCase())}` : ""}</span></td>
                <td class="mono" data-v="${esc(s.shape)}">${esc(s.shape)}${s.variant && s.variant !== "standard" ? `<span class="row-sub">${esc(s.variant)}</span>` : ""}</td>
                <td class="mono" data-v="${esc(s.region)}">${esc(s.region)}${isIndiaSku(s) ? "" : `<span class="tag warn" style="display:block;width:max-content" title="Runs outside India: no India data residency">outside India</span>`}</td>
                <td class="num" data-v="${s.vcpus ?? -1}">${hostSpec(s)}</td>
                <td class="num strong" data-v="${priceOf(s) ?? 999999}">${priceCell(s)}${spotCell(s)}</td>
                <td class="num strong" data-v="${vmOf(s) ?? 999999}">${priceCell(s, true)}</td>
                <td class="num" data-v="${c ? c.usd_per_gpu_hr : 999999}">${c ? money(c.usd_per_gpu_hr) + ` <span class="muted">/${c.term_months}mo</span>` : unk("none")}</td>
                <td class="num" data-v="${a && a.available_vms != null ? a.available_vms : -1}">${capTxt}</td>
              </tr>`;
            }).join("")}
          </tbody>
        </table></div>` : `<div class="note">No public SKU rate card yet. ${rel.notes ? esc(rel.notes) : ""}</div>`}
      </div>
    </section>

    <section id="inventory">
      <h2>Capacity <span class="h2-note muted">— deployed fleet and allocation, not availability</span></h2>
      ${capacity.indiaai ? `<div class="note iai-note">IndiaAI-empanelled: <b>${capacity.indiaai.total.toLocaleString()} GPUs</b>
        <span class="meta" style="display:inline">${esc(Object.entries(capacity.indiaai.by_gpu).map(([g, n]) => `${n.toLocaleString()} ${g}`).join(" · "))}
        — offered under the IndiaAI tender, not necessarily operational; not counted as installed fleet.
        ${capacity.indiaai.source ? `<a href="${esc(refUrl(capacity.indiaai.source.url))}" target="_blank" rel="noopener noreferrer">source ↗</a>` : ""}</span></div>` : ""}
      <div class="panel">
        ${capacity.pools.length ? `
        <div class="table-scroll"><table id="provider-capacity-table">
          <thead><tr>
            <th>GPU</th><th>Region</th>
            <th class="num">Total</th><th class="num">Rented</th><th class="num">Committed</th><th class="num" title="Provider-reported, or derived from total minus rented and committed; unrented stock, not availability">Unrented (reported)</th><th class="num">Power (MW)</th>
          </tr></thead>
          <tbody>
            ${capacity.pools.map(r => {
              const free = r.free_gpus != null ? r.free_gpus
                : (r.total_gpus != null && (r.rented_gpus != null || r.committed_gpus != null)
                  ? Math.max(0, r.total_gpus - (r.rented_gpus || 0) - (r.committed_gpus || 0)) : null);
              return `<tr>
                <td class="mono">${esc(gpuName(r.gpu))}</td>
                <td class="mono muted">${esc(r.region)}</td>
                <td class="num">${r.total_gpus == null ? unk() : r.total_gpus.toLocaleString()}</td>
                <td class="num">${r.rented_gpus == null ? unk() : r.rented_gpus.toLocaleString()}</td>
                <td class="num">${r.committed_gpus == null ? unk() : r.committed_gpus.toLocaleString()}</td>
                <td class="num">${free == null ? unk() : free.toLocaleString()}</td>
                <td class="num">${r.power_mw == null ? unk() : r.power_mw.toLocaleString()}</td>
              </tr>`;
            }).join("")}
          </tbody>
        </table></div>
        <div class="note">Unrented is provider-reported, or derived from total minus rented and committed. Observed availability is listed under Availability.</div>` : `<div class="note">${esc(capacity.notes || "Fleet size and facility power are not published.")}</div>`}
      </div>

      <h2 style="margin-top:30px">Availability <span class="h2-note muted">— GPUs observed available, grouped by GPU + region</span></h2>
      <div class="panel">
        ${invRows.length ? `
        <div class="table-scroll"><table id="provider-inventory-table">
          <thead><tr><th>GPU</th><th>Region</th><th>Shapes</th><th class="num">Available</th></tr></thead>
          <tbody>
            ${invRows.map(r => `<tr>
              <td class="mono">${esc(r.gpu)}</td>
              <td class="mono muted">${esc(r.region)}</td>
              <td>${[...r.shapes].sort().map(x => `<span class="chip">${esc(x)}</span>`).join("")}</td>
              <td class="num">${r.free}</td>
            </tr>`).join("")}
          </tbody>
        </table></div>
        ${live.lastObserved ? `<div class="note">Last observed ${esc(live.lastObserved)}. Shapes share one physical pool; counted once per GPU + region.</div>` : ""}` : `<div class="note">${(() => {
            const inv = p.inventory_check;
            if (!inv) return `No stock observations, and no logged-in inventory check yet.${rel.capacity_notes ? " " + esc(rel.capacity_notes) : ""}`;
            const when = inv.last_checked_at ? `${esc(inv.last_checked_at)} (${esc(ago(inv.last_checked_at))})` : "never";
            const what = inv.inventory === "visible" ? "stock numbers were visible"
              : inv.inventory === "empty" ? "the catalogue was empty for this account"
              : inv.inventory === "not-exposed" ? "the provider exposes no stock numbers" : "the inventory could not be inspected";
            return `No stock observations. Last logged-in check ${when} via ${esc(inv.access)}: ${what}.${inv.blockers ? " Blocker: " + esc(inv.blockers) + "." : ""}`;
          })()}</div>`}
      </div>
    </section>

    <section>
      <h2>Inventory check <span class="h2-note muted">— logged in, did we see real stock?</span></h2>
      <div class="panel">
        ${(() => {
          const inv = p.inventory_check;
          if (!inv) return `<div class="note">No logged-in inventory check recorded yet.</div>`;
          const yes = (v) => v === true ? `<span class="ok">yes</span>` : `<span class="muted">no</span>`;
          return `<div class="badges" style="margin:0 0 8px">
            <span class="pill ${inv.inventory === "visible" ? "ok" : inv.inventory === "unknown" ? "" : "warn"}">${esc(inv.inventory)}</span>
            <span class="pill">${esc(inv.access)}</span>
            <span class="pill">login: ${esc(inv.login)}</span>
            <span class="pill">${esc(inv.order_path)}</span>
          </div>
          <div class="note" style="margin:0">
            ${inv.last_checked_at ? `Last checked ${esc(inv.last_checked_at)} (${esc(ago(inv.last_checked_at))}).` : "Never checked while logged in."}
            Stock recorded: ${yes(inv.stock_recorded)}.
            ${inv.blockers ? `<div style="margin-top:6px">Blocker: ${esc(inv.blockers)}</div>` : ""}
            ${inv.notes ? `<div style="margin-top:6px">${esc(inv.notes)}</div>` : ""}
          </div>`;
        })()}
      </div>
    </section>

    <section>
      <h2>Storage <span class="h2-note muted">— where downloaded model weights live</span></h2>
      <div class="panel">
        ${(() => {
          const st = p.storage || {};
          const mount = st.mountable === true || st.block_usd_per_gb_mo != null || st.file_usd_per_gb_mo != null;
          const ok = (label, title) => `<span class="pill ok" title="${esc(title)}">${label}</span>`;
          const unknown = [];
          let caps = mount ? ok("Mountable storage", "Block/file storage attaches to a GPU VM, so model weights live outside the instance")
            : st.mountable === false ? `<span class="pill" title="No block or file storage that attaches to a GPU VM">No mountable storage</span>`
            : `<span class="pill" title="Not verified for this provider; unknown, not a no">Mountable storage ?</span>`;
          if (st.shared === true) caps += ok("Shared filesystem", "File storage mountable on several nodes at once");
          else if (st.shared == null) unknown.push("multi-node sharing");
          if (st.persistent === true) caps += ok("Outlives the instance", "Storage survives stopping or terminating the GPU VM");
          else if (st.persistent == null) unknown.push("persistence after a stop");
          if (st.object_s3_compatible === true) caps += ok("S3", "S3-compatible object storage");
          const gb = (v) => `$${v}/GB-mo`;
          const prices = [st.block_usd_per_gb_mo != null ? `block ${gb(st.block_usd_per_gb_mo)}` : "",
                          st.file_usd_per_gb_mo != null ? `file ${gb(st.file_usd_per_gb_mo)}` : "",
                          st.object_usd_per_gb_mo != null ? `object ${gb(st.object_usd_per_gb_mo)}` : ""].filter(Boolean);
          return `<div class="badges" style="margin:0 0 8px">${caps}</div>
          <div class="note" style="margin:0">${prices.length ? `${esc(prices.join(" · "))} <span class="muted">— prices are secondary; capability is what matters.</span>` : "No storage pricing published; capability is tracked separately from price."}${unknown.length ? ` <span class="muted">Not verified: ${esc(unknown.join(", "))}.</span>` : ""}</div>`;
        })()}
      </div>
    </section>

    <section>
      <h2>Regions</h2>
      <div>${(p.regions || []).map(r => `<span class="chip">${esc(r)}</span>`).join("") || `<span class="muted">—</span>`}</div>
    </section>

    <section>
      <h2>Reliability</h2>
      <div class="panel">
        <div class="note">
          ${rel.sla_pct != null ? `<div><b>${rel.sla_pct}%</b> SLA</div>` : ""}
          ${rel.incident_count_90d != null ? `<div>${rel.incident_count_90d} incidents in 90 days</div>` : ""}
          ${rel.capacity_notes ? `<div style="margin-top:6px">${esc(rel.capacity_notes)}</div>` : ""}
          ${rel.notes ? `<div style="margin-top:6px">${esc(rel.notes)}</div>` : ""}
          ${!rel.sla_pct && !rel.incident_count_90d && !rel.capacity_notes && !rel.notes ? "No reliability data yet." : ""}
        </div>
      </div>
    </section>

    <section>
      <h2>Sources</h2>
      <div class="panel">
        <ul class="source-list">
          ${(p.sources || []).map(s => `<li><span class="pill">${esc(s.kind)}</span><a href="${esc(refUrl(s.url))}" target="_blank" rel="noreferrer">${esc(s.url)}</a><span class="muted" style="margin-left:auto">${esc(s.fetched_at || "")}</span></li>`).join("") || `<li class="muted">No sources recorded.</li>`}
        </ul>
      </div>
    </section>
  `;
  enableDomSort($("provider-sku-table"));
}

/* ---------------- routing / view ---------------- */
function showOnly(id) {
  for (const v of ["view-gpus", "view-providers", "view-gpu-detail", "view-provider-detail"]) {
    $(v).classList.toggle("hidden", v !== id);
  }
}
function navigate(hash) {
  if (location.hash === hash) { route(); return; }
  // pushState (not location.hash) so the analytics beacon sees each route change.
  history.pushState(null, "", hash);
  route();
}
function setView(name) {
  navigate(name === "providers" ? "#/providers" : "#/gpus");
}
function route() {
  TRACK.pageview();
  const hash = location.hash || "#/gpus";
  const g = hash.match(/^#\/gpu\/(.+)$/);
  const p = hash.match(/^#\/provider\/([^/]+)(\/inventory)?$/);
  if (g) {
    $("tab-gpus").classList.add("active");
    $("tab-providers").classList.remove("active");
    renderGPUDetail(decodeURIComponent(g[1]));
    return;
  }
  if (p) {
    $("tab-providers").classList.add("active");
    $("tab-gpus").classList.remove("active");
    renderProviderDetail(decodeURIComponent(p[1]));
    if (p[2]) {
      const inv = $("inventory");
      if (inv) inv.scrollIntoView({ behavior: "smooth", block: "start" });
    }
    return;
  }
  const tab = hash === "#/providers" ? "providers" : "gpus";
  VIEW = tab;
  $("tab-gpus").classList.toggle("active", tab === "gpus");
  $("tab-providers").classList.toggle("active", tab === "providers");
  showOnly(tab === "gpus" ? "view-gpus" : "view-providers");
  if (tab === "gpus") renderGPUs(); else renderProviders();
}
function markArrows(theadId, sort) {
  document.querySelectorAll(`#${theadId} th`).forEach(th => {
    th.querySelector(".arrow")?.remove();
    if (th.dataset.sort === sort.key) {
      const s = document.createElement("span");
      s.className = "arrow";
      s.textContent = sort.dir > 0 ? "↑" : "↓";
      th.appendChild(s);
    }
  });
}
function enableDomSort(table) {
  if (!table) return;
  table.querySelectorAll("th[data-sort]").forEach((th, idx) => {
    th.classList.add("sortable");
    th.addEventListener("click", () => {
      const tbody = table.querySelector("tbody");
      const rows = [...tbody.querySelectorAll("tr")];
      const dir = th.dataset.dir === "asc" ? -1 : 1;
      table.querySelectorAll("th").forEach(h => { h.dataset.dir = ""; h.querySelector(".arrow")?.remove(); });
      th.dataset.dir = dir > 0 ? "asc" : "desc";
      const arrow = document.createElement("span");
      arrow.className = "arrow";
      arrow.textContent = dir > 0 ? "↑" : "↓";
      th.appendChild(arrow);
      const type = th.dataset.type || "text";
      rows.sort((a, b) => {
        const ac = a.children[idx], bc = b.children[idx];
        const av = ac?.dataset.v ?? ac?.textContent ?? "";
        const bv = bc?.dataset.v ?? bc?.textContent ?? "";
        if (type === "num") return (Number(av) - Number(bv)) * dir;
        return String(av).localeCompare(String(bv)) * dir;
      });
      rows.forEach(r => tbody.appendChild(r));
    });
  });
}

/* ---------------- Info tooltips ----------------
   Small i-in-a-circle hints (data-tip, "|"-separated lines). A fixed-position
   element, so it is never clipped by the scrolling table wrappers. */
let INFO_TIP = null;
function hideInfoTip() { if (INFO_TIP) INFO_TIP.classList.add("hidden"); }
function showInfoTip(el) {
  const text = el.dataset.tip;
  if (!text) return;
  if (!INFO_TIP) {
    INFO_TIP = document.createElement("div");
    INFO_TIP.className = "tip hidden";
    INFO_TIP.setAttribute("role", "tooltip");
    document.body.appendChild(INFO_TIP);
  }
  INFO_TIP.innerHTML = text.split("|").map(l => `<div>${esc(l)}</div>`).join("");
  INFO_TIP.classList.remove("hidden");
  const r = el.getBoundingClientRect(), t = INFO_TIP.getBoundingClientRect();
  const left = Math.min(Math.max(8, r.left + r.width / 2 - t.width / 2), window.innerWidth - t.width - 8);
  let top = r.bottom + 8;
  if (top + t.height > window.innerHeight - 8) top = r.top - t.height - 8;   // flip above near the bottom edge
  INFO_TIP.style.left = `${Math.round(left)}px`;
  INFO_TIP.style.top = `${Math.round(top)}px`;
}
document.addEventListener("mouseover", e => { const el = e.target.closest?.("[data-tip]"); if (el) showInfoTip(el); });
document.addEventListener("mouseout", e => { const el = e.target.closest?.("[data-tip]"); if (el && !el.contains(e.relatedTarget)) hideInfoTip(); });
document.addEventListener("focusin", e => { const el = e.target.closest?.("[data-tip]"); if (el) showInfoTip(el); });
document.addEventListener("focusout", hideInfoTip);
window.addEventListener("scroll", hideInfoTip, true);

window.addEventListener("hashchange", route);

// Route in-app links through pushState (so the analytics beacon sees each route change)
// and record every link click. Capture phase, so a row onclick cannot double-navigate.
document.addEventListener("click", (e) => {
  const a = e.target.closest?.("a[href]");
  if (!a) return;
  const href = a.getAttribute("href") || "";
  let target = href;
  if (/^https?:/i.test(href)) {
    try { const u = new URL(href); target = u.hostname + u.pathname; } catch (err) {}
  }
  TRACK.click((a.textContent || "").replace(/\s+/g, " ").trim(), target);
  if (href.startsWith("#/") && !a.target && !e.metaKey && !e.ctrlKey && !e.shiftKey && !e.altKey) {
    e.preventDefault();
    e.stopPropagation();
    navigate(href);
  }
}, true);

/* ---------------- Spotlight search ---------------- */
const spot = { open: false, index: 0, items: [] };
function spotlightData() {
  const gpus = gpuRows().map(g => ({
    title: g.name,
    sub: `${g.familyName}${g.variant ? ` · ${g.variant.vram_gb} GB ${g.variant.memory_type}` : ""}`,
    meta: `${g.providerTotal} ${g.providerTotal === 1 ? "provider" : "providers"} · ${g.priceMin == null ? "no orderable price" : `from ${money(g.priceMin)}${g.priceMonthly ? " (monthly)" : ""}`}`,
    href: `#/gpu/${encodeURIComponent(g.id)}`,
    logo: null,
    glyph: "GPU",
    hay: [g.name, g.familyName, g.id, g.variant ? `${g.variant.vram_gb} GB ${g.variant.memory_type}` : "", [...g.providers].join(" ")].join(" ").toLowerCase(),
  }));
  const providers = CATALOG.providers.map(p => {
    const skus = skusOf(p.id);
    const gs = [...new Set(skus.map(s => accelName(s)))].sort();
    const b = bestOf(skus);
    // Short summary only; the full GPU list stays searchable via `hay` and is shown on the provider page.
    const price = b.v != null ? `from ${money(b.v)}${b.monthly ? " (monthly)" : ""}` : (accessOf(p).pricing === "quote" ? "quote only" : "no orderable price");
    return {
      title: p.name || p.id,
      sub: (p.regions || []).join(", ") || p.id,
      meta: `${gs.length} ${gs.length === 1 ? "GPU" : "GPUs"} · ${price}`,
      href: `#/provider/${encodeURIComponent(p.id)}`,
      logo: `/assets/logos/${p.id}.png`,
      glyph: "P",
      hay: [p.id, p.name, (p.regions || []).join(" "), gs.join(" ")].join(" ").toLowerCase(),
    };
  });
  return { gpus, providers };
}
function renderSpotlight(q) {
  const { gpus, providers } = spotlightData();
  const query = q.trim().toLowerCase();
  const groups = [
    { label: "GPUs", items: gpus.filter(x => !query || x.hay.includes(query)) },
    { label: "Providers", items: providers.filter(x => !query || x.hay.includes(query)) },
  ];
  spot.items = groups.flatMap(g => g.items);
  if (spot.index >= spot.items.length) spot.index = 0;
  if (!spot.items.length) {
    $("spotlight-results").innerHTML = `<div class="spot-empty">No results for “${esc(q)}”.</div>`;
    return;
  }
  let idx = 0;
  $("spotlight-results").innerHTML = groups.filter(g => g.items.length).map(g => `
    <div class="spot-section">${g.label}</div>
    ${g.items.map(item => {
      const i = idx++;
      return `<button class="spot-item${i === spot.index ? " active" : ""}" data-i="${i}" data-href="${esc(item.href)}">
        ${item.logo
          ? `<img class="logo" src="${esc(item.logo)}" alt="" onerror="this.style.visibility='hidden'">`
          : `<span class="spot-glyph">${esc(item.glyph)}</span>`}
        <span class="spot-main"><span class="spot-title">${esc(item.title)}</span><span class="spot-sub mono">${esc(item.sub)}</span></span>
        <span class="spot-meta">${esc(item.meta)}</span>
      </button>`;
    }).join("")}
  `).join("");
  $("spotlight-results").querySelectorAll(".spot-item").forEach(btn => {
    btn.addEventListener("mouseenter", () => {
      spot.index = Number(btn.dataset.i);
      $("spotlight-results").querySelectorAll(".spot-item").forEach((el, i) => el.classList.toggle("active", i === spot.index));
    });
  });
  const active = $("spotlight-results").querySelector(".spot-item.active");
  if (active) active.scrollIntoView({ block: "nearest" });
}
function moveSpotlight(delta) {
  if (!spot.items.length) return;
  spot.index = (spot.index + delta + spot.items.length) % spot.items.length;
  const items = $("spotlight-results").querySelectorAll(".spot-item");
  items.forEach((el, i) => el.classList.toggle("active", i === spot.index));
  items[spot.index].scrollIntoView({ block: "nearest" });
}
function selectSpotlight(i) {
  const item = spot.items[i];
  if (!item) return;
  const query = ($("spotlight-input")?.value || "").trim();
  if (query) TRACK.search(query);
  closeSpotlight();
  navigate(item.href);
}
function openSpotlight() {
  spot.open = true;
  spot.index = 0;
  $("spotlight").classList.remove("hidden");
  $("spotlight").setAttribute("aria-hidden", "false");
  document.body.classList.add("spotlight-open");
  const input = $("spotlight-input");
  input.value = "";
  renderSpotlight("");
  input.focus();
}
function closeSpotlight() {
  spot.open = false;
  $("spotlight").classList.add("hidden");
  $("spotlight").setAttribute("aria-hidden", "true");
  document.body.classList.remove("spotlight-open");
  $("search-trigger").focus();
}
$("search-trigger").addEventListener("click", openSpotlight);
$("spotlight-input").addEventListener("input", (e) => {
  spot.index = 0;
  renderSpotlight(e.target.value);
});
$("spotlight").addEventListener("click", (e) => {
  if (e.target === $("spotlight")) closeSpotlight();
});
$("spotlight-results").addEventListener("click", (e) => {
  const btn = e.target.closest(".spot-item");
  if (btn) selectSpotlight(Number(btn.dataset.i));
});
document.addEventListener("keydown", (e) => {
  if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
    e.preventDefault();
    if (spot.open) closeSpotlight(); else openSpotlight();
    return;
  }
  if (!spot.open) return;
  if (e.key === "Escape") { e.preventDefault(); closeSpotlight(); }
  else if (e.key === "ArrowDown") { e.preventDefault(); moveSpotlight(1); }
  else if (e.key === "ArrowUp") { e.preventDefault(); moveSpotlight(-1); }
  else if (e.key === "Enter") { e.preventDefault(); selectSpotlight(spot.index); }
});
if (!/Mac|iPhone|iPad/.test(navigator.userAgent)) {
  document.querySelectorAll(".search-trigger .kbd").forEach(el => { el.textContent = "Ctrl K"; });
}
document.querySelectorAll("#thead-gpus th.sortable").forEach(th => {
  th.addEventListener("click", () => {
    const key = th.dataset.sort;
    if (SORT.gpus.key === key) SORT.gpus.dir *= -1; else SORT.gpus = { key, dir: 1 };
    renderGPUs();
  });
});
document.querySelectorAll("#thead-providers th.sortable").forEach(th => {
  th.addEventListener("click", () => {
    const key = th.dataset.sort;
    if (SORT.providers.key === key) SORT.providers.dir *= -1; else SORT.providers = { key, dir: 1 };
    renderProviders();
  });
});

(async function () {
  applyTheme();
  CATALOG = await firstJSON(["/api/catalog", "/v1/catalog.json"]);
  CATALOG.allSkus = CATALOG.skus;
  applyScope();
  buildGPUIndex();
  $("footer-count").textContent = `${CATALOG.counts.providers} providers · ${CATALOG.counts.accelerator_variants} GPU SKUs · ${CATALOG.counts.skus} host packages · ${CATALOG.counts.availability_observations} availability observations`;
  if (!location.hash) history.replaceState(null, "", "#/gpus");
  route();
})().catch(err => {
  document.body.insertAdjacentHTML("beforeend", `<pre style="color:#b91c1c;padding:20px">${err}</pre>`);
});

async function getJSON(url) { const r = await fetch(url); if (!r.ok) throw new Error(url + " " + r.status); return r.json(); }
async function firstJSON(urls) { let last; for (const u of urls) { try { return await getJSON(u); } catch (e) { last = e; } } throw last; }
</script>
</body>
</html>
"""

# Rename the site here, once. Both the dev server and `scripts/export_api.py` render this
# module's HTML, so the brand, page title and outbound referral tag stay in sync.
SITE_NAME = "GPU Where"
SITE_TAGLINE = "India GPU providers"
SITE_DOMAIN = "gpuwhere.io"
# Public source repository. Leave empty to hide the header link.
SITE_REPO = "https://github.com/anjan-srivastava/gpuwhere"

GITHUB_ICON = (
    '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
    '<path d="M12 .5C5.73.5.5 5.73.5 12c0 5.08 3.29 9.39 7.86 10.91.58.11.79-.25.79-.56 '
    '0-.28-.01-1.02-.02-2-3.2.7-3.88-1.54-3.88-1.54-.53-1.34-1.29-1.7-1.29-1.7-1.05-.72.08-.71.08-.71 '
    '1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.55-.29-5.23-1.28-5.23-5.68 '
    '0-1.26.45-2.29 1.19-3.1-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.18 1.18a11 11 0 0 1 5.8 0c2.2-1.49 '
    '3.17-1.18 3.17-1.18.63 1.59.23 2.76.11 3.05.74.81 1.19 1.84 1.19 3.1 0 4.41-2.69 5.38-5.25 5.67.41.35.78 '
    '1.04.78 2.1 0 1.52-.01 2.74-.01 3.11 0 .31.21.67.8.56A11.51 11.51 0 0 0 23.5 12C23.5 5.73 18.27.5 12 .5z"/>'
    '</svg>'
)


def repo_link() -> str:
    """The header source link, or nothing when SITE_REPO is unset."""
    if not SITE_REPO:
        return ""
    return (f'<a class="gh-btn" href="{SITE_REPO}" target="_blank" rel="noopener noreferrer" '
            f'aria-label="Source code on GitHub" title="Source code">{GITHUB_ICON}</a>')


def docs_repo_link() -> str:
    """A plain text source link for the API docs footer."""
    if not SITE_REPO:
        return ""
    return f'<a href="{SITE_REPO}" target="_blank" rel="noopener noreferrer">Source</a>'


HTML = (HTML_TEMPLATE
        .replace("__SITE_NAME__", SITE_NAME)
        .replace("__SITE_TAGLINE__", SITE_TAGLINE)
        .replace("__SITE_DOMAIN__", SITE_DOMAIN)
        .replace("__REPO_LINK__", repo_link()))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-dir", default="data")
    ap.add_argument("--assets-dir", default="assets")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=8080)
    args = ap.parse_args()
    Handler.data_root = args.data_dir
    Handler.assets_dir = args.assets_dir
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"GPU providers at http://{args.host}:{args.port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
