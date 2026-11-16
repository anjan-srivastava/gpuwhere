#!/usr/bin/env python3
"""Seed data/price-history from the SKUs that already exist.

The ledger started after the catalogue did, so the first row for old packages is
derived from the SKU's own `verified_at` (origin=backfill). That is an honest
"this price was verified on that date", not a claim that the price changed then.
Git remains the archive for anything before `verified_at`.

    python scripts/backfill_price_history.py                     # dry-run, all providers
    python scripts/backfill_price_history.py --write             # seed empty ledgers
    python scripts/backfill_price_history.py --write --append-missing
                                                                 # add new hand-curated SKUs
                                                                 # at the current time

A provider ledger that already has rows is never rewritten. `--append-missing`
only appends SKUs it has never seen, so history stays append-only.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "scrapers"))

import price_history  # noqa: E402

SEED_NOTE = ("Seeded from the SKU's verified_at when the price ledger was introduced; "
             "the exact change time before the ledger is unknown. Earlier history is in git.")
APPEND_NOTE = ("Added by backfill because the package had no ledger row; ts is when the "
               "backfill ran, verified_at is when the price was last checked.")


def skus_by_provider(data: Path) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = defaultdict(list)
    for path in sorted((data / "skus").rglob("*.json")):
        sku = json.loads(path.read_text())
        groups[sku["provider"]].append(sku)
    return groups


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument("-p", "--provider", action="append", help="provider id (repeatable); default all")
    ap.add_argument("--write", action="store_true", help="append to data/price-history")
    ap.add_argument("--append-missing", action="store_true",
                    help="also append SKUs missing from a ledger that already has rows")
    args = ap.parse_args()

    root = Path(args.root)
    data = root / "data"
    groups = skus_by_provider(data)
    providers = args.provider or sorted(groups)
    now = price_history.utc_now_iso()
    total = 0

    for pid in providers:
        skus = groups.get(pid)
        if not skus:
            print(f"[{pid}] no SKUs")
            continue
        path = root / price_history.PRICE_DIR / f"{pid}.jsonl"
        existing = price_history.read_observations(path)
        seen = {row["sku_id"] for row in existing}

        if not existing:
            rows = []
            for sku in skus:
                verified = sku.get("verified_at")
                if not verified:
                    print(f"[{pid}] {sku['id']}: no verified_at, cannot seed", file=sys.stderr)
                    return 1
                rows.append(price_history.observation(
                    sku, f"{verified}T00:00:00Z", origin="backfill", notes=SEED_NOTE))
            rows.sort(key=lambda row: (row["ts"], row["sku_id"]))
            mode = "seed"
        elif args.append_missing:
            rows = [price_history.observation(sku, now, origin="backfill", notes=APPEND_NOTE)
                    for sku in sorted(skus, key=lambda s: s["id"]) if sku["id"] not in seen]
            mode = "append"
        else:
            print(f"[{pid}] ledger has {len(existing)} row(s); use --append-missing for new SKUs")
            continue

        total += len(rows)
        print(f"[{pid}] {mode}: {len(rows)} row(s) -> {path.relative_to(root)}")
        if args.write and rows:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("a", encoding="utf-8") as fh:
                for row in rows:
                    fh.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")

    print(f"{'wrote' if args.write else 'would write'} {total} observation(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
