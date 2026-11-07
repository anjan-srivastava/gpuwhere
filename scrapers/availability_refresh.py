#!/usr/bin/env python3
"""Hourly availability collection: free GPUs per SKU, on-demand and spot.

    python scrapers/availability_refresh.py            # dry-run: print observations
    python scrapers/availability_refresh.py --write    # append JSONL + update SKU availability

Each collector returns observations keyed by provider/region/gpu/shape/variant,
matching SKU ids. `--write` appends them to `data/availability/<provider>.jsonl`
(append-only; a second run in the same UTC hour is skipped) and copies the
latest values into each matching SKU's `availability` block.

Observed free GPUs are availability, never installed capacity.
"""
from __future__ import annotations

import argparse
import datetime as dt
import importlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from pricing_common import Context, dump, utc_today  # noqa: E402

COLLECTORS = {"jarvislabs": "availability_jarvislabs", "nxtgen": "availability_nxtgen"}
# Providers with no unauthenticated, machine-readable stock signal. Each needs
# a customer account/API key before a collector can be written.
NO_PUBLIC_SIGNAL = {
    "e2e-networks": "MyAccount API needs a validated customer account (current account is_approved=false).",
    "acecloud": "Stock only visible in the logged-in console/OpenStack API.",
    "neysa": "Stock only visible in the Velocis console; no public API.",
    "leapswitch": "Order cart shows no stock; console only.",
    "cyfuture-ai": "Console only; page marks offers schema.org InStock statically.",
    "tata-communications": "Vayu console only.",
    "yotta-shakti": "Shakti portal only; calculator JSON has no stock fields.",
    "neevcloud": "Site blocks automated clients; console only.",
    "utho": "Site blocks automated clients; console only.",
    "ctrls": "No self-service GPU console.",
    "sify": "No self-service GPU console.",
    "jio-platforms": "Reserved capacity via sales only.",
}


def sku_index(data: Path) -> dict[tuple, Path]:
    idx = {}
    for p in (data / "skus").rglob("*.json"):
        d = json.loads(p.read_text())
        if d.get("status") == "retired":
            continue
        idx[(d["provider"], d["region"], d["gpu"], d["shape"], d.get("variant"))] = p
    return idx


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-p", "--provider", action="append")
    ap.add_argument("--root", default=str(HERE.parent))
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    root = Path(args.root)
    data = root / "data"
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    ts = now.isoformat().replace("+00:00", "Z")
    hour = ts[:13]
    ctx = Context(root / ".cache" / "scrape", utc_today())
    idx = sku_index(data)
    rc = 0

    for pid in args.provider or (list(COLLECTORS) + list(NO_PUBLIC_SIGNAL)):
        if pid in NO_PUBLIC_SIGNAL:
            print(f"[{pid}] no collector: {NO_PUBLIC_SIGNAL[pid]}")
            continue
        try:
            obs = importlib.import_module(COLLECTORS[pid]).collect(ctx)
        except Exception as exc:
            print(f"[{pid}] FAILED: {exc}", file=sys.stderr)
            rc = 1
            continue
        out = data / "availability" / f"{pid}.jsonl"
        seen_hour = set()
        if out.exists():
            for line in out.read_text().splitlines():
                if line.strip():
                    o = json.loads(line)
                    if o["ts"][:13] == hour:
                        seen_hour.add((o["region"], o["gpu"], o["shape"], o.get("variant")))
        matched = unmatched = skipped = 0
        lines = []
        for o in obs:
            o = {"ts": ts, **o}
            key = (o["provider"], o["region"], o["gpu"], o["shape"], o["variant"])
            if (o["region"], o["gpu"], o["shape"], o["variant"]) in seen_hour:
                skipped += 1
                continue
            lines.append(json.dumps(o, separators=(",", ":")))
            path = idx.get(key)
            if path is None:
                unmatched += 1
                print(f"[{pid}] no SKU for {'/'.join(map(str, key))}")
                continue
            matched += 1
            if args.write:
                sku = json.loads(path.read_text())
                sku["availability"] = {
                    "last_observed_at": ts,
                    "available_vms": o["available_vms"], "available_gpus": o["available_gpus"],
                    "spot_available_vms": o["spot_available_vms"], "spot_available_gpus": o["spot_available_gpus"],
                    "source": o["source"],
                }
                path.write_text(dump(sku))
            elif matched <= 6:
                print(f"  {'/'.join(map(str, key))}: free {o['available_gpus']} GPUs / {o['available_vms']} VMs, "
                      f"spot {o['spot_available_gpus']}")
        if args.write and lines:
            out.parent.mkdir(parents=True, exist_ok=True)
            with out.open("a", encoding="utf-8") as fh:
                fh.write("\n".join(lines) + "\n")
        print(f"[{pid}] observations={len(obs)} matched_skus={matched} unmatched={unmatched} "
              f"skipped_same_hour={skipped}{' (written)' if args.write else ' (dry-run)'}")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
