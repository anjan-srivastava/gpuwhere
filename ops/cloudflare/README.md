# Cloudflare setup (free tier)

Two free Cloudflare products, no server:

| Piece | Product | Free allowance |
|---|---|---|
| Website + JSON API + schemas | **Pages** | unlimited requests, 500 builds/month |
| Refresh schedule | **Worker Cron Triggers** | 100k requests/day, 5 cron triggers |

The scrapers stay in Python; the Worker is only a clock that dispatches a GitHub Action,
because a Worker cannot run Python. All three pieces are free for a public repo.

## 1. Pages — the published site

* Connect the GitHub repository.
* Build command: `python scripts/export_api.py`
* Build output directory: `dist`
  (Pages needs a Python build image; if the default image has no Python, commit `dist/`
  from CI instead and point Pages at the repository root with no build step.)

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
```

`dist/_headers` already sets `Access-Control-Allow-Origin: *` and cache policy for
`/v1/*`, so browser consumers and `curl` both work.

The UI loads `/v1/catalog.json` first and falls back to `/api/catalog`, so the same page
works on Pages (static) and against the local dev server.

## 2. Worker — the scheduler

```bash
cd ops/cloudflare
npm create cloudflare@latest -- gpu-catalog-scheduler   # or add worker.js to an existing project
wrangler secret put GITHUB_TOKEN   # fine-grained PAT: Actions = write, Contents = read
wrangler secret put GITHUB_REPO    # owner/repo
wrangler deploy
```

`wrangler.toml`:

```toml
name = "gpu-catalog-scheduler"
main = "worker.js"
compatibility_date = "2026-01-01"

[triggers]
crons = ["5 * * * *", "15 4 * * *"]
```

* `5 * * * *` → `refresh-availability.yml` (hourly)
* `15 4 * * *` → `refresh-pricing.yml` (daily, 04:15 UTC)

The Worker calls GitHub's `workflow_dispatch` API; the workflow scrapes, validates, and
commits. Pages then rebuilds on push.

## 3. Health

* Each refresh workflow runs `scripts/validate.py` and the test suite **before** committing,
  so a parser break cannot publish bad data.
* `python scripts/check_freshness.py` is the operational gate: it fails when pricing is
  older than 3 days, availability older than 6 hours, or capacity older than 14 days.
  Wire it into a second Worker cron later if you want alerts; today it runs at the end of
  each refresh.

## Cost

Pages free, Workers free, GitHub Actions free for public repositories. The only paid
dependency would be a private repo's Actions minutes — the workflows are ~1 minute each.
