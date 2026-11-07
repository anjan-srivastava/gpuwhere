# Catalogue audit — 2026-11-08

Scope: schemas, data, scrapers, serving API. SkyPilot integration is a separate discussion and is not covered here.
All numbers measured against the working tree on 2026-11-08.

## Scorecard

| Area | Grade | One line |
|---|---|---|
| Data model / schemas | **B−** | Good coverage and vocabulary, but permissive: unknown fields pass, almost nothing is cross-checked. |
| Data quality | **B** | Provenance is excellent (every SKU has sources); coverage is uneven (vCPU 88%, disk 11%, capacity 0%, availability 2/21). |
| Scrapers | **B−** | Well-behaved crawlers with robots/rate limits/caching, but no tests, no CI, no scheduler, and HTML-regex fragility. |
| Serving API | **C** | Works, but it is a dev server: one 721 KB dynamic blob, no CORS/ETag/HEAD, no versioning, no schema endpoint. |
| Versioning / ops | **D** | The directory is not a git repository. No CI, no scheduled runs, no release artifact. |

## Inventory (measured)

| Thing | Count | Note vs `AGENTS.md` |
|---|---|---|
| Providers | 21 | doc says 14 |
| Host packages (SKUs) | 435 (415 active, 15 retired, 5 unavailable) | doc says 303 active |
| Accelerator families / variants | 24 / 29 | doc says 29 SKUs (still true for variants) |
| Capacity files | 21, **0 with `total_gpus`** | all fleet sizes unpublished |
| Availability observations | **102 rows, 2 providers**, newest 2026-11-07T18:10Z | doc implies hourly coverage for launch candidates |
| Incidents | 21 files | — |
| Channels | 1 (IndiaAI) | — |

The gap between the doc's "definition of done" and the tree is the first finding: the README/AGENTS status text is stale by roughly a month of work.

## Schemas

**Strengths.** Enums are used where they matter (`status`, `shape`, `form_factor`, `residency`, `confidence`, `observed_via`, `pricing_status`). Every record carries `sources`, `confidence`, `verified_at`. Naming is consistent across provider/SKU/GPU.

**Weaknesses (ordered by risk):**

1. **`additionalProperties` is unset in all seven schemas.** A typo like `"billling_model"` validates cleanly and silently disappears from the UI. This is the cheapest fix with the largest payoff.
2. **No cross-file invariants.** `scripts/validate.py` validates each file in isolation. It does not check that `sku.provider` exists, that `sku.gpu_variant` resolves in `data/gpus`, that `sku.id` matches its path, that `usd_per_vm_hr == usd_per_gpu_hr × gpus_per_vm`, or that an availability key matches a SKU. (Manual check today: all of these currently pass — but nothing enforces them.)
3. **No `format` / `pattern` on dates and regions.** `verified_at` is a free string; region codes (`IN-DEL`, `EU-FI`) have no vocabulary.
4. **Shared `$defs` are duplicated** in each file (the `source` object exists five times). One `common.schema.json` with `$ref` would prevent drift.
5. **Partial optionality.** 54 SKUs (12%) have no `billing_model` or `residency`; 18 (4%) have no `pricing_status`. Today the UI treats absence as a fallback; the schema should either require them or make the fallback explicit.
6. **No `schema_version`** anywhere in the data or the API payload.

## Data quality

- **Provenance:** 100% of SKUs have at least one source; referential integrity is currently clean (no orphan provider, GPU variant or duplicate SKU id).
- **Confidence:** SKUs 177 high / 258 medium / 0 low; providers 8 high / 12 medium / 1 low.
- **Spec gaps:** `vcpus` missing on 52 SKUs (12%), `disk_gb` missing on 389 (89%), `ram_gb` complete.
- **Capacity:** 21 files, all `total_gpus: null`. Honest, but it means the capacity column is inert for every provider.
- **Availability:** 2 providers only (JarvisLabs, NxtGen), 102 rows, already ~3 h stale at audit time. The hourly loop is not scheduled anywhere (no cron, no launchd).
- **Pricing mix:** 367 published, 50 quote-only, 60 with spot, 254 with committed terms.

## Scrapers

**Good.** `pricing_common.Context` enforces robots.txt, ≤1 req/s per host, retries and on-disk snapshots (`--offline` replay). Dry-run by default, `--write` emits a report where every pricing/confidence change is tagged `REVIEW`. Availability skips a second run inside the same UTC hour. Failures are explicit (`NO_PUBLIC_SIGNAL` documents why 12 providers cannot be polled).

**Weak.**

1. **No tests and no fixtures.** 26 modules, zero tests. HTML parsers are regex over rendered text (`_row_iter`), the most fragile possible shape; a provider restyling a table breaks silently until a human notices the diff.
2. **No scheduler and no run ledger.** Cadences are documented, not executed. Nothing records "last successful run per provider".
3. **No alerting.** A scraper that fails three days running looks identical to one that found no change.
4. **Coverage asymmetry.** 9 providers are scraped for pricing; 12 are hand-curated; 1 of 21 has availability.
5. **No schema-drift guard.** Scrapers call `package_to_sku` but nothing asserts the produced object against `sku.schema.json` before writing.

## API (current vs models.dev)

Current surface: `GET /` (UI), `/api/catalog`, `/api/keys`, `/api/availability?…`, `/assets/*`.

| | This catalogue | models.dev |
|---|---|---|
| Artifact | Dynamic, rebuilt per request | Static JSON (`/api.json`) |
| Size | 721 KB | 5.97 MB |
| Caching | `Cache-Control: no-store` | `ETag` + Cloudflare edge cache |
| CORS | none | `Access-Control-Allow-Origin: *` |
| Methods | GET only (`HEAD` → 501) | GET/HEAD |
| Versioning | none | ?param + repo history |
| Schema | JSON Schema files in repo, not served | schema in the repo |
| Hosting | local `BaseHTTPRequestHandler` (HTTP/1.0) | CDN |
| Source of truth | files in this directory (unversioned) | git repo |

What "same setup as models.dev" would require, in order:

1. **Put the directory under git**, tag releases, publish from CI. Without this nothing else is reproducible.
2. **Publish a static artifact** per release: `api/v1/catalog.json` (monolith) plus split files (`providers.json`, `gpus.json`, `skus.json`, `availability/latest.json`). Static means ETag, gzip, CDN and `If-None-Match` come for free; the current server can keep serving from the same artifact.
3. **Enable CORS (`*`), HEAD, gzip and a long cache TTL** with content-hashed filenames or an ETag.
4. **Version the payload**: `/v1/…`, a `schema_version` field, and a short changelog page.
5. **Serve the schemas** at `/v1/schema/*.json` (with `$id`) and a combined schema so consumers can validate; add an OpenAPI file for the query endpoints.
6. **Add `as_of` / `generated_at`** to every payload (availability already has per-row `ts`).
7. **Keep `/api/availability` dynamic** (it is a time series), but cache with `ETag` and cap the window.

## Recommended sequence

**Phase 1 — correctness (½ day).** `additionalProperties: false` + `format` on dates; extend `validate.py` with the cross-file invariants listed above; add npm-free CI (GitHub Actions or a pre-commit hook) running validator + a 10-line smoke test of the server.

**Phase 2 — publishable API (1 day).** Static exporter (`scripts/export_api.py`) writing `dist/v1/*.json` with `schema_version` and `generated_at`; server serves the artifact with ETag/CORS/HEAD; schema files served alongside.

**Phase 3 — operational honesty (1–2 days).** git + tags; a scheduler (cron/launchd/GitHub Actions) for pricing daily / availability hourly / capacity weekly; a per-provider run ledger (`reports/runs.jsonl`) so staleness is visible; fixtures from `.cache/scrape` replayed as parser tests; assert scraper output against the SKU schema before writing.

Phase 1 and 2 together turn this from "a good local tool" into "a catalogue other tools can depend on", which is the models.dev bar.
