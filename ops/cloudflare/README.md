# Cloudflare setup (free tier)

Five free Cloudflare products, two separate deployments, no server:

| Piece | Product | Free allowance |
|---|---|---|
| Site, open `/v1` artifact, API docs | **Pages** (direct upload) | unlimited requests, 500 builds/month |
| Keyed API + analytics ingest (`_worker.js`) | **Pages Functions** | Workers free: 100k requests/day |
| Event storage | **Workers Analytics Engine** | 100k writes/day, 90-day retention |
| Jobs control plane | **Workers** (`gpuwhere-jobs`) | 100k requests/day |
| Optional schedule | **Worker Cron Triggers** | 5 cron triggers |

The site and the jobs service are deployed separately (`make deploy` vs `make deploy-jobs`).
The scrapers run as GitHub Actions jobs, which is free for public repositories.

## 1. Deploy from this directory

```bash
make deploy          # build dist/ + `wrangler pages deploy`
make whoami          # which account is wrangler using
```

`make deploy` downloads wrangler into `.tools/npm/` and uploads `dist/` directly; there is no
Git integration or build image to configure. `wrangler.toml` at the repo root is the source of
truth (project name, `pages_build_output_dir`, the `ANALYTICS` binding, rate-limit vars).

Authenticate once:

```bash
.tools/npm/node_modules/.bin/wrangler login
# or, for CI:
export CLOUDFLARE_API_TOKEN=...   # Pages:Edit + Account:Read
```

The project is **`gpuwhere`** → `https://gpuwhere.pages.dev`. Attach `gpuwhere.io` in
**Workers & Pages → gpuwhere → Custom domains** when the domain is bought.

Pages serves:

```
/                     the UI
/v1/catalog.json      everything (one request)
/v1/providers.json    split resources
/v1/gpus.json
/v1/skus.json
/v1/availability/latest.json
/v1/index.json        endpoint directory
/v1/schema/*.json     JSON Schemas
/api/docs             API reference (HTML)
/api/openapi.json     OpenAPI 3.1
/api/v1/*             keyed JSON API
/a                    analytics beacon ingest
```

`dist/_headers` sets `Access-Control-Allow-Origin: *` and cache policy for `/v1/*`, so browser
consumers and `curl` both work.

## 2. API keys and rate limits

```bash
make api-key
.tools/npm/node_modules/.bin/wrangler pages secret put API_KEYS --project-name gpuwhere
```

* `API_KEYS` — comma-separated. Rotation: append, deploy, remove, redeploy.
* The open bulk data at `/v1/*` stays public by design; keys gate `/api/v1/*` so it can be
  metered (`usage data`) and rate-limited.
* Budgets live in `wrangler.toml` vars: 60/min per API key, 300/min per IP for pages/assets,
  120/min per IP for the beacon. The worker uses the Workers Rate Limiting binding if one is
  ever bound, and a fixed-window Cache API counter otherwise (Pages Functions cannot declare
  the binding yet). Both are approximate and per-location; `429` carries `Retry-After: 60`.

## 3. Analytics

The worker writes one Analytics Engine data point per event:

```
blob1 event      pageview | click | search
blob2 path       #/gpu/nvidia/h100, /api/docs, …
blob3 label      link text
blob4 target     outbound host+path, internal route, or search query
blob5 referrer   hostname only
blob6 country    ISO-2 from request.cf
index1           random per-tab session id
```

No cookies, no IP stored, DNT/GPC and `navigator.webdriver` respected. Retention is 90 days.

```bash
make analytics DAYS=7
```

`scripts/analytics_report.py` prints pageviews by day, top pages, referrers, countries,
most-clicked links, searches and a recent click stream. It uses `CF_ANALYTICS_TOKEN`
(Account Analytics:Read) when set, and otherwise the local `wrangler login` token. The same
dataset is queryable in the dashboard's Analytics Engine SQL editor.

## 4. Jobs Worker (separate deployment)

`gpuwhere-jobs` is its own Worker. It starts scraper jobs on demand and, optionally, on a
configurable schedule. The scrapers run in GitHub Actions; this Worker is just the control
plane.

```bash
make deploy-jobs

WR=".tools/npm/node_modules/.bin/wrangler"
$WR secret put JOB_TOKEN     --config ops/cloudflare/wrangler.toml   # bearer for /jobs /run /schedule
$WR secret put GITHUB_TOKEN  --config ops/cloudflare/wrangler.toml   # Actions: write
$WR secret put GITHUB_REPO   --config ops/cloudflare/wrangler.toml   # owner/repo
```

Endpoints:

```
GET  /health            public
GET  /jobs              latest run per workflow          (bearer)
POST /run?job=pricing   dispatch now                     (bearer)
GET  /schedule          effective schedule               (bearer)
PUT  /schedule          edit it at runtime               (bearer, KV bound)
```

Schedule defaults, in `ops/cloudflare/wrangler.toml`:

* cron tick `0 0 * * *` — daily at 00:00 UTC;
* `DAILY_JOBS="availability,pricing"` — the jobs dispatched on each tick;
* `SCHEDULE_ENABLED=false` turns the clock off and leaves `/run` working.

For runtime edits, create a KV namespace and bind it as `JOBS_CONFIG`:

```bash
$WR kv namespace create JOBS_CONFIG      # paste the id into wrangler.toml
```

Then `PUT /schedule` with `{"enabled":true,"jobs":["pricing"]}`
(no redeploy). Without the binding the endpoint returns `409` and the vars are the source of
truth. A KV guard key stops two ticks on the same UTC day from dispatching twice.

Local alternative: `make job JOB=pricing` runs the same script under a lock and logs to
`reports/jobs/`.

## 5. Health

* `make check` runs schema validation, the Python suite, the edge-worker tests, the build and
  the freshness gate.
* Pages then rebuilds on the next `make deploy`; a no-op refresh produces byte-identical files.

## Cost

Pages free, Pages Functions and Workers free tier, Analytics Engine free tier, GitHub Actions
free for public repositories.
