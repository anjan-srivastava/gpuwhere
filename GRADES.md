# Catalogue grades

Living scorecard. Update it whenever a change is made that moves a grade — the evidence
column should always be checkable from the repo, not remembered.

Last reviewed: **2026-11-09** · schema_version `1`

| Area | Grade | Evidence | What moves it up |
|---|---|---|---|
| Data model / schemas | **B** | 7 schemas, all `additionalProperties:false`; enums for status/shape/form factor/residency/confidence/pricing_status; shared vocabulary duplicated per file | Extract a `common.schema.json` + `$ref`; add region vocabulary and `format: date` validation |
| Data quality | **B** | 437 packages (417 active, 15 retired, 5 unavailable), 21 providers, 29 accelerator variants; 100% have sources; vCPU 88%, disk 11%, capacity 0%, availability 5/21 | Fill capacity and availability; reduce vCPU gaps; keep quality budgets green |
| Scrapers | **B−** | 26 modules; 16 providers scraped for pricing, 5 hand-curated; availability covers 5 of 21; 15 inventory checks recorded (3 visible, 2 empty, 4 not-exposed, 6 unverified); replay tests parse every cached snapshot; no scheduler running yet | Run the cron for a week without a failure; add fixtures from each provider's page |
| Serving API | **B** | Static `/v1/*` export (catalog, split resources, schemas) with `schema_version` + `generated_at`; ETag/304, CORS `*`, HEAD; 826 KB catalog | Deploy to Pages; add an OpenAPI file for query endpoints |
| Versioning / ops | **C** | Git repository with tags; CI on push; refresh workflows for pricing/availability; freshness gate | One green week of scheduled runs; run ledger of last-success per provider |

## Gates that enforce the grades

| Gate | Command | Runs |
|---|---|---|
| Schema validation | `python scripts/validate.py` | CI, before every refresh commit |
| Data contract, integrity, quality budgets | `python -m unittest discover -s tests` | CI, before every refresh commit |
| Scraper replay (parsers still work) | same suite, `.cache/scrape` present | CI (skips when no snapshots) |
| Freshness | `python scripts/check_freshness.py` | end of each refresh workflow |
| Artifact build | `python scripts/export_api.py` | CI and Pages |

## Known gaps (deliberately not graded away)

- **Capacity is `null` for all 21 providers.** Honest per AGENTS.md, but the capacity column is inert.
- **Availability covers 5 of 21 providers** (JarvisLabs, Cyfuture, NeevCloud, NxtGen, E2E); the rest need a customer account or console session. E2E is signed in and orderable but publishes no stock counts.
- **`disk_gb` is missing on 89% of packages** — nobody publishes per-VM disk consistently.
- **16 providers scraped, 5 hand-curated**; hand-curated files can drift silently between reviews.
- **Cloudflare Worker cron is written but not deployed** (`ops/cloudflare/`), so scheduled refresh is still manual.

## How to update

1. Change the grade only together with the evidence in the same commit.
2. Keep numbers measured, not estimated (run the audit snippet or the tests).
3. If a gap closes, delete the row from *Known gaps* — do not leave a stale caveat.
