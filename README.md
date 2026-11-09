# GPU Provider Catalog — India

A versioned, machine-readable catalogue of GPU providers in India, built to answer: **what can this provider serve, where, at what price, and how reliably?**

It is a provider catalogue — not a monitoring system. It tracks capability, reliability evidence, and **availability over time per GPU shape** so graphs and placement decisions are evidence-based.

See `AGENTS.md` for the contributor/agent contract.

## Why

GPU pricing and availability in India are opaque and change weekly. The same provider has shown three different H200 prices across three surfaces, and capacity frequently reads zero. This catalogue normalises providers, SKUs, pricing modes, networking, storage, incidents, and hourly availability.

## Structure

```
schema/provider.schema.json
schema/sku.schema.json
schema/availability.schema.json
schema/incident.schema.json
schema/channel.schema.json
schema/capacity.schema.json
schema/gpu.schema.json

data/providers/*.json                 # identity, capability, reliability summary
data/gpus/<supplier>/<family>.json    # accelerator SKUs: VRAM, FLOPS, precision, MIG
data/skus/<provider>/<region>/<gpu>/<shape>[/<variant>].json  # host packages sold by providers
data/incidents/<provider>.json        # curated incident history
data/availability/<provider>.jsonl    # hourly snapshots of free GPUs, on-demand + spot
data/capacity/<provider>.json         # deployed fleet, allocation split, facility MW
data/channels/*.json                  # subsidy/marketplace channels (IndiaAI), not providers

scrapers/                             # official feed/API ingestion (16 providers) + refresh loops
scripts/serve_catalog.py              # dev server: UI + /api/* + /v1 artifact
scripts/export_api.py                 # build dist/ for Cloudflare Pages
scripts/validate.py                   # schema validation
scripts/check_freshness.py            # operational gate: age of pricing/availability/capacity
tests/                                # unittest suite: schema, integrity, budgets, scrapers, HTTP
ops/cloudflare/                       # Pages + jobs Worker setup
GRADES.md                             # living scorecard, evidence per grade
assets/logos/<provider>.png           # provider logos
```

## Granularity

- Shapes: `1x`, `2x`, `4x`, `8x`.
- **Accelerator SKU** is the GPU product: VRAM, memory bandwidth, native precision support, dense/sparse FLOPS, TDP, interconnect and MIG. Example: `H100 SXM5 80GB` and `H100 NVL 94GB` are different accelerator SKUs.
- **Host package** is what a provider sells: accelerator SKU + 1/2/4/8 GPUs + vCPU + host RAM + disk + price. A provider can sell one accelerator in several packages.
- **FLOPS basis:** dense FP16 TFLOPS is the common comparison number. Native precision support is listed per accelerator; FP8/FP4 rates stay in the per-precision table and are not converted into FP16 equivalents.
- **Capacity** is the deployed fleet: `total_gpus` split into `rented_gpus`, `committed_gpus` and `free_gpus`, plus optional pool and facility `power_mw`. It is a stock, not a live signal.
- **Availability** is the observed free signal: per provider × region × GPU × shape, on-demand and spot, hourly. It is a flow/observation, not installed capacity.
- Pricing: USD canonical, refreshed daily; per GPU and per VM.

## Quickstart

Everything is wrapped in `make`; `uv` and npm resolve the toolchain on demand.

```bash
make check                 # schemas, tests (Python + edge worker), build, freshness
make serve                 # http://127.0.0.1:8080
make deploy                # build + upload dist/ to Cloudflare Pages
```

The underlying commands, if you want them directly:

```bash
# validate
uv run --with jsonschema python scripts/validate.py

# collect a real JarvisLabs snapshot
python scrapers/jarvislabs_availability.py --out data/availability/jarvislabs.jsonl

# daily pricing refresh from official sources (dry-run; add --write [--retire-superseded])
python scrapers/pricing_refresh.py

# hourly availability (free GPUs per SKU) and weekly installed capacity (dry-run; add --write)
python scrapers/availability_refresh.py
python scrapers/capacity_refresh.py

# weekly discovery of providers the catalogue may be missing (review report only)
python scrapers/discover_providers.py --write

# test: data contract, referential integrity, quality budgets, scraper replay, HTTP surface
uv run --with jsonschema python -m unittest discover -s tests
node --test tests/worker.test.mjs

# build the publishable artifact (dist/) for Cloudflare Pages
python scripts/export_api.py
```

## Publish

The release is a static build plus one Pages Function (`dist/_worker.js`). `make deploy`
downloads wrangler into `.tools/npm/` (nothing global), builds `dist/`, and uploads it directly
from this directory. Authenticate once with `wrangler login`, or set
`CLOUDFLARE_API_TOKEN` (Pages:Edit + Account:Read) for CI.

```bash
make deploy                              # project gpu-atlas, branch main
CF_PROJECT=gpu-atlas-preview make deploy  # any other Pages project
make release VERSION=0.2.0               # annotated git tag
```

The site is `https://gpu-atlas.pages.dev` until a custom domain is attached. The proposed
production name is **GPU Atlas** (`gpuatlas.io`); `gpus.io` is taken. The name, tagline and
outbound referral tag are three constants at the bottom of `scripts/serve_catalog.py`, so a
rename is one edit. RDAP reported `gpuatlas.io` unregistered on 2026-11-09 — confirm at a
registrar before buying; that is a hint, not a reservation.

### API keys

The bulk artifact at `/v1/*` stays open and cacheable. The query API at `/api/v1/*` requires a
key — it exists so traffic can be metered and rate-limited, not to keep public data secret.

```bash
make api-key                       # print a random key
.tools/npm/node_modules/.bin/wrangler pages secret put API_KEYS --project-name gpu-atlas
```

`API_KEYS` is a comma-separated list: append a new key, deploy, then remove the old one.
Reference docs live at `/api/docs`, the OpenAPI 3.1 spec at `/api/openapi.json`.

### Rate limits

Every request passes a fixed-window budget in the worker before it reaches data or assets:

| Surface | Budget | Keyed by |
|---|---|---|
| Keyed API | 60 / minute | API key (invalid keys fall back to IP) |
| Pages, assets, docs | 300 / minute | client IP |
| Analytics beacon (`/a`) | 120 / minute | client IP |

Limits are per Cloudflare location and approximate — the free plan cannot express a strict
global cap — and return `429` with `Retry-After: 60`. Tune them in `wrangler.toml`
(`API_RATE_PER_MIN`, `PAGE_RATE_PER_MIN`, `EVENT_RATE_PER_MIN`).

### Analytics

`assets/track.js` sends pageviews, in-app route changes, link clicks and searches to `/a`; the
worker writes them to Workers Analytics Engine (`gpu_atlas_events`) as
`event, path, label, target, referrer host, country` plus a random per-tab session id.
No cookies, no IP storage, DNT/GPC honoured, 90-day retention. Report:

```bash
export CF_ACCOUNT_ID=... CF_ANALYTICS_TOKEN=...   # Account Analytics:Read
make analytics DAYS=7
make analytics LOCAL=1                             # reads .cache/dev-analytics.jsonl
```

The same SQL is available in the Cloudflare dashboard's Analytics Engine query editor.

### Scraper jobs (separate deployment)

Scraping is not part of the site deployment. `ops/cloudflare/` is a second Worker,
**`gpu-atlas-jobs`**, whose only job is to start a GitHub Actions run — on demand, and
optionally on a configurable schedule. The site keeps serving the last published artifact.

```bash
make deploy-jobs                      # deploy the jobs Worker
make run-job JOB=pricing              # dispatch a run now
make run-job JOB=availability
make jobs                             # latest run per workflow
make schedule                         # effective schedule
make job JOB=pricing                  # run locally instead (lock + log in reports/jobs/)
make job JOB=pricing DRY=1            # local dry-run
```

Secrets on the jobs Worker: `JOB_TOKEN` (bearer for `/jobs`, `/run`, `/schedule`),
`GITHUB_TOKEN` (Actions: write) and `GITHUB_REPO`. The schedule is opt-in
(`SCHEDULE_ENABLED=true`): availability every N hours, pricing daily at a chosen UTC hour.
Change it in `ops/cloudflare/wrangler.toml`, or bind `JOBS_CONFIG` (KV) and `PUT /schedule`
to change it without redeploying. There is **no cron in the Pages project**.

**GitHub Actions cost:** free for public repositories (unlimited standard runners);
private repositories get 2,000 minutes/month free, which these one-minute jobs fit easily.
Two caveats on free/public: scheduled workflows are disabled after 60 days without repository
activity, and cron granularity is five minutes with occasional delays — another reason the
schedule lives in the jobs Worker and on-demand runs are the default. The refresh workflows
run `make deploy` after committing when `CLOUDFLARE_API_TOKEN` is set, so a job publishes its
own data; otherwise run `make deploy` yourself.

### Nix

`flake.nix` pins Python 3.12, uv, Node 22, GNU make and wrangler. It is optional:
`make nix-shell` enters the shell, and every Make target works without it (uv + npm).

## Current status

- **Providers:** 21, all active — 15 Indian (E2E Networks, JarvisLabs, NeevCloud, Neysa, AceCloud, Yotta Shakti, Cyfuture AI, CtrlS, NxtGen, Sify, Tata Communications, Jio Platforms, Utho Cloud, Leapswitch, Krutrim) and 6 global burst options (AWS, Azure, Nebius, OVHcloud, Verda, Hyperstack) catalogued for their non-India regions.
- **Accelerator SKUs:** 29 variants across 24 families — H100 (SXM5/NVL), H200, A100, B200, B300, L40S, L4, A40, A30, A2, T4, V100, RTX PRO 6000/4500, RTX 6000 Ada, RTX A6000/A5000/A4000, RTX 4090/5090/3090, MI300X, MI325X and Gaudi 2. Each carries VRAM, native precision support, dense/sparse FLOPS and MIG.
- **Host packages:** 435 total — 415 active, 15 retired as superseded, 5 unavailable; 385 published and 50 `quote_only` with null prices. 16 providers are refreshed by `scrapers/pricing_refresh.py` from official sources (feed, API, CLI or page); NeevCloud, Utho, CtrlS, Sify and Jio are hand-curated.
- **IndiaAI:** modelled as a subsidy channel in `data/channels/indiaai.json`, not as a provider. It carries the portal L1 ceiling rates and the provider-attributed L1 rates from the PIB annexure.
- **UI:** two tabs — GPUs (accelerator SKUs with VRAM, dense FP16 TFLOPS, native precision, provider count, price) and Providers (regions, GPU pills, **price vs market**, capability columns, deployed capacity plus live free GPUs).
- **Price vs market:** on the providers page, per provider, the geometric mean of its cheapest orderable price for each GPU model over that model's market median, using only models that three or more providers sell inside the current Region/Provider scope. Hourly is compared with hourly and monthly-only packages with monthly (tagged); models below that threshold, quote-only providers and sold-out packages never set the index, so a thin market shows "too few comparable" instead of a misleading number. The ⓘ next to the column header explains the method on hover; the header sorts by it, breaking equal results in favour of a provider with a documented API and hourly on-demand packages, and provider pages show the same figure as a stat card.
- **Self-serve vs sales:** a package the provider lists but cannot actually be ordered online (NxtGen's H200, Leapswitch's H200/RTX PRO 6000, Cyfuture's B300/H200/RTX PRO 6000) is tagged **sales only**, keeps its price for audit, and is excluded from "from" prices and the market index — clicking a provider link should not land you somewhere the SKU does not exist.
- **Spot:** where a provider publishes a spot/preemptible rate, it appears as a small green line under the on-demand price on the GPU and provider pages (`spot $0.80 · −82%`). Verda publishes one; Nebius' is dynamic and read from its public spot-price API.
- **Storage (model weights):** capability first, price second. Each provider page has a Storage section stating whether block/file storage can be attached to a GPU VM, whether it can be shared across nodes, and whether it outlives the instance — with anything unverified named explicitly rather than guessed. The providers page shows `Block/File` and `Shared FS` chips and filters on mountable storage. Prices per GB-month are shown as quiet secondary metadata. GPU detail lists accelerator specs and precision support, one provider row per package summary, and an exact host-package table with vCPU/RAM; provider detail lists exact host packages plus a capacity section at `#/provider/<id>/inventory` and a separate live-availability section. Capacity and availability are deliberately not the same number: capacity is installed fleet, availability is what is free right now.
- **Availability:** hourly observations for 2 of 21 providers (JarvisLabs, NxtGen), 102 records so far; the other 12 are listed in `NO_PUBLIC_SIGNAL` with the exact blocker (account validation, console-only stock, or blocked automated clients). These are **free** GPUs observed, not installed capacity; no provider has published fleet totals or GPU-fleet MW yet, so capacity files are explicitly unknown rather than inferred from availability.
- **E2E availability blocker:** the console and API return empty GPU plans while the account is unvalidated (`is_approved: false`). Customer validation must complete before E2E capacity can be collected.
- **Confidence:** 177 high / 258 medium host packages (no low); 8 providers high, 12 medium, 1 low. Grades, gates and known gaps live in `GRADES.md`.
- **Deferred:** continuous uptime/latency telemetry, supply-chain analysis.
