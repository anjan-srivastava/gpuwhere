#!/usr/bin/env python3
"""Daily pricing refresh: run provider scrapers, build host-package SKUs, review.

Dry-run by default: prints what would change and writes nothing.

    python scrapers/pricing_refresh.py                      # all providers, dry-run
    python scrapers/pricing_refresh.py -p acecloud -p e2e-networks
    python scrapers/pricing_refresh.py --write              # write SKUs + review report
    python scrapers/pricing_refresh.py --offline            # re-parse today's snapshots

`--write` updates/creates `data/skus/...` and writes
`reports/pricing-refresh-<date>.md`. Changes to pricing or confidence are
flagged REVIEW: AGENTS.md requires a human to review them before merge.
SKU files that exist for a scraped provider but were not produced by the
scraper are listed as STALE. With `--retire-superseded`, a stale file whose
region/GPU/shape is covered by a package from this run is marked
`status: "retired"` (never deleted); other stale files are left for a human.
"""
from __future__ import annotations

import argparse
import datetime as dt
import importlib
import json
import sys
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from pricing_common import (Context, assign_variants, diff, dump, merge,  # noqa: E402
                            package_to_sku, retire, sku_path, utc_today)

# provider id → module. Providers without a public, fetchable rate card are
# listed in MANUAL with the reason; their SKUs stay human-curated.
SCRAPERS = {
    "e2e-networks": "pricing_e2e",
    "jarvislabs": "pricing_jarvislabs",
    "acecloud": "pricing_acecloud",
    "neysa": "pricing_neysa",
    "nxtgen": "pricing_nxtgen",
    "leapswitch": "pricing_leapswitch",
    "cyfuture-ai": "pricing_cyfuture",
    "tata-communications": "pricing_tata",
    "yotta-shakti": "pricing_yotta",
    "krutrim-cloud": "pricing_krutrim",
    "microsoft-azure": "pricing_azure",
    "aws": "pricing_aws",
    # Outside India (burst; no India data residency)
    "ovhcloud": "pricing_ovh",
    "nebius": "pricing_nebius",
    "verda": "pricing_verda",
    "hyperstack": "pricing_hyperstack",
}
MANUAL = {
    "neevcloud": "neevcloud.com returns HTTP 403 to automated clients; not bypassed. Curate manually.",
    "utho": "utho.com returns HTTP 403 to automated clients; not bypassed. Curate manually.",
    "ctrls": "No public commercial GPU rate card; IndiaAI L1 rates live in the channel file.",
    "sify": "No public per-GPU rate card; IndiaAI L1 rates live in the channel file.",
    "jio-platforms": "No public commercial rate card; reserved terms via sales only.",
}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-p", "--provider", action="append", help="provider id (repeatable); default all")
    ap.add_argument("--root", default=str(HERE.parent))
    ap.add_argument("--write", action="store_true", help="write SKU files and the review report")
    ap.add_argument("--offline", action="store_true", help="parse today's cached snapshots only")
    ap.add_argument("--cache-dir", default=None, help="raw snapshot dir (default <root>/.cache/scrape)")
    ap.add_argument("--retire-superseded", action="store_true",
                    help="with --write: mark stale SKUs retired when this run covers their region/GPU/shape")
    args = ap.parse_args()

    root = Path(args.root)
    data = root / "data"
    today = utc_today()
    ctx = Context(Path(args.cache_dir or root / ".cache" / "scrape"), today, offline=args.offline)
    providers = args.provider or list(SCRAPERS)

    report = [f"# Pricing refresh {today}", "",
              f"Mode: {'write' if args.write else 'dry-run'}. "
              "Pricing and confidence changes need human review (AGENTS.md).", ""]
    totals = {"new": 0, "changed": 0, "unchanged": 0, "stale": 0, "retired": 0, "failed": 0}

    for pid in providers:
        if pid in MANUAL:
            report += [f"## {pid}", "", f"Not scraped: {MANUAL[pid]}", ""]
            continue
        if pid not in SCRAPERS:
            print(f"unknown provider {pid}", file=sys.stderr)
            return 2
        mod = importlib.import_module(SCRAPERS[pid])
        report += [f"## {pid}", ""]
        try:
            res = mod.scrape(ctx)
        except Exception as exc:  # one provider failing must not stop the rest
            totals["failed"] += 1
            report += [f"**FAILED**: `{exc}`", "", "```", traceback.format_exc(limit=3).strip(), "```", ""]
            print(f"[{pid}] FAILED: {exc}", file=sys.stderr)
            continue

        priced = res.packages
        produced = set()
        covered = set()
        lines = []
        fx = ctx.fx if any(_needs_fx(p) for p in priced) else None
        for pkg, variant in assign_variants(priced):
            sku = package_to_sku(pkg, variant, fx, today)
            path = sku_path(data, sku)
            produced.add(path.resolve())
            covered.add((sku["region"], sku["gpu"], sku["shape"]))
            old = json.loads(path.read_text()) if path.exists() else None
            new = merge(old, sku)
            changes = diff(old, new)
            if changes == ["NEW"]:
                totals["new"] += 1
                od = new["pricing"]["on_demand"]["usd_per_gpu_hr"]
                lines.append(f"- NEW `{sku['id']}` — " + (f"${od}/GPU-hr" if od is not None else "quote_only")
                             + f", {new.get('vcpus')} vCPU, {new.get('ram_gb')} GB RAM")
            elif changes:
                totals["changed"] += 1
                lines.append(f"- CHANGED `{sku['id']}`: " + "; ".join(changes))
            else:
                totals["unchanged"] += 1
            if args.write and dump(new) != (dump(old) if old else None):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(dump(new))

        existing = {p.resolve() for p in (data / "skus" / pid).rglob("*.json")} if (data / "skus" / pid).exists() else set()
        stale = sorted(existing - produced)
        for s in stale:
            rel = s.relative_to(data.resolve())
            old = json.loads(s.read_text())
            if old.get("status") == "retired":
                continue
            key = (old.get("region"), old.get("gpu"), old.get("shape"))
            if key in covered:
                reason = (f"superseded by the {pid} scraper's {key[1]} {key[2]} package(s) from the current "
                          "official source.")
                if args.write and args.retire_superseded:
                    s.write_text(dump(retire(old, today, reason)))
                    totals["retired"] += 1
                    lines.append(f"- RETIRED `{rel}` — {reason}")
                else:
                    totals["stale"] += 1
                    lines.append(f"- STALE (superseded) `{rel}` — retire with --write --retire-superseded")
            else:
                totals["stale"] += 1
                lines.append(f"- STALE `{rel}` — no current source covers {key[1]} {key[2]}; left for human review")
        if fx:
            lines.insert(0, f"- FX: USD/INR {fx.usd_inr} ({fx.date}, ECB reference rate)")
        report += lines or ["- no changes"]
        for w in res.warnings:
            report.append(f"- WARNING: {w}")
        for u in res.unpriced:
            report.append(f"- Listed but not a SKU: {u}")
        report.append("")
        print(f"[{pid}] packages={len(priced)} stale={len(stale)} warnings={len(res.warnings)}")

    report += ["## Fetched", ""] + [f"- `{f['url']}` {f['bytes']} B sha1 {f['sha1'][:12]}" for f in ctx.fetched] + [""]
    summary = ", ".join(f"{k}={v}" for k, v in totals.items())
    report.insert(3, f"Summary: {summary}")
    text = "\n".join(report) + "\n"
    if args.write:
        out = root / "reports" / f"pricing-refresh-{today}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        stamp = dt.datetime.now(dt.timezone.utc).strftime("%H:%M UTC")
        scope = ", ".join(providers) if args.provider else "all providers"
        # Several runs per day append; a later partial run must not erase an earlier report.
        with out.open("a", encoding="utf-8") as fh:
            fh.write(("\n---\n\n" if out.exists() and out.stat().st_size else "")
                     + text.replace(f"# Pricing refresh {today}", f"# Pricing refresh {today} {stamp} ({scope})", 1))
        print(f"wrote {out}")
    else:
        print(text)
    print(summary)
    return 1 if totals["failed"] else 0


def _needs_fx(pkg) -> bool:
    prices = [pkg.on_demand, pkg.spot, *pkg.committed.values()]
    return any(p is not None and p.currency != "USD" for p in prices)


if __name__ == "__main__":
    raise SystemExit(main())
