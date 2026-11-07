#!/usr/bin/env python3
"""Operational freshness gate — run by the scheduler, not by the unit tests.

Unit tests must pass on an old checkout, so they only check that timestamps are real.
This script answers the other question: *is the data still being refreshed?*

    python scripts/check_freshness.py                 # exit 1 when a threshold is breached
    python scripts/check_freshness.py --warn-only     # report, always exit 0

Thresholds (per AGENTS.md cadence):
  pricing      daily   -> fail when the newest verified_at is older than 3 days
  availability hourly  -> fail when a tracked series is older than 6 hours
  capacity     weekly  -> fail when the newest as_of/verified_at is older than 14 days
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def newest_dates(files, keys):
    out = []
    for f in files:
        d = json.loads(f.read_text())
        for k in keys:
            v = d.get(k)
            if v:
                try:
                    out.append((f, dt.date.fromisoformat(v[:10])))
                except ValueError:
                    pass
                break
    return out


def check_pricing(today):
    files = [f for f in (DATA / "skus").rglob("*.json")
             if json.loads(f.read_text()).get("status") != "retired"]
    dates = newest_dates(files, ("verified_at",))
    if not dates:
        return "FAIL", "no dated SKUs"
    newest = max(d for _, d in dates)
    age = (today - newest).days
    stale = sum(1 for _, d in dates if (today - d).days > 45)
    status = "OK" if age <= 3 else "FAIL"
    return status, f"newest SKU verified {newest} ({age}d ago), {stale}/{len(dates)} older than 45d"


def check_capacity(today):
    files = list((DATA / "capacity").glob("*.json"))
    dates = newest_dates(files, ("as_of", "verified_at"))
    if not dates:
        return "WARN", "no dated capacity files"
    newest = max(d for _, d in dates)
    age = (today - newest).days
    return ("OK" if age <= 14 else "FAIL"), f"newest capacity as_of {newest} ({age}d ago)"


def check_availability(today):
    files = list((DATA / "availability").glob("*.jsonl"))
    if not files:
        return "WARN", "no availability series yet"
    worst = []
    for f in files:
        last = None
        for line in f.read_text().splitlines():
            if line.strip():
                ts = json.loads(line).get("ts")
                if ts and (last is None or ts > last):
                    last = ts
        if last:
            t = dt.datetime.fromisoformat(last.replace("Z", "+00:00"))
            age = dt.datetime.now(dt.timezone.utc) - t
            worst.append((f.stem, age))
    if not worst:
        return "WARN", "availability files have no timestamps"
    name, age = max(worst, key=lambda x: x[1])
    hours = age.total_seconds() / 3600
    return ("OK" if hours <= 6 else "FAIL"), f"stalest series {name} {hours:.1f}h old"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--warn-only", action="store_true")
    args = ap.parse_args()
    today = dt.date.today()
    results = [("pricing",) + check_pricing(today),
               ("capacity",) + check_capacity(today),
               ("availability",) + check_availability(today)]
    width = max(len(n) for n, _, _ in results)
    for name, status, detail in results:
        print(f"{name:<{width}}  {status:4s}  {detail}")
    failed = [n for n, s, _ in results if s == "FAIL"]
    if failed and not args.warn_only:
        print(f"\nfreshness gate failed: {', '.join(failed)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
