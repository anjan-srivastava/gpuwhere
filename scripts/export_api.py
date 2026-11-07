#!/usr/bin/env python3
"""Build the publishable static API (Cloudflare Pages / any static host).

    python scripts/export_api.py                # writes dist/
    python scripts/export_api.py --out dist --base-url https://gpus.io

Output is deterministic apart from `generated_at`: the same data produces byte-identical
files, so a rebuild without data changes is a no-op in git and on the CDN.

Layout:
    dist/index.html                 the UI, pointed at /v1/catalog.json
    dist/assets/...                 logos
    dist/v1/catalog.json            everything, one request
    dist/v1/providers.json          split resources for consumers that want less
    dist/v1/gpus.json
    dist/v1/skus.json
    dist/v1/availability/latest.json
    dist/v1/index.json              endpoint directory + counts
    dist/v1/schema/*.json           the same JSON Schemas the repo validates against
    dist/_headers                   Cloudflare Pages headers (CORS, cache)
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from serve_catalog import (HTML, _latest_availability, _load_availability, _load_gpus,  # noqa: E402
                           _load_json_dir, _load_skus)

SCHEMA_VERSION = "1"


def dump(path: Path, obj) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    body = json.dumps(obj, indent=1, ensure_ascii=False, sort_keys=False) + "\n"
    path.write_text(body, encoding="utf-8")
    return len(body.encode("utf-8"))


def build(data: Path) -> tuple[dict, dict]:
    inventory = {r.get("provider"): r for r in _load_json_dir(data / "inventory")}
    providers = [dict(p, inventory_check=inventory.get(p.get("id"))) for p in _load_json_dir(data / "providers")]
    skus = _load_skus(str(data))
    gpus = _load_gpus(str(data))
    channels = _load_json_dir(data / "channels")
    capacities = _load_json_dir(data / "capacity")
    availability = _load_availability(str(data))
    latest = _latest_availability(availability)

    enriched = []
    for s in skus:
        key = (s.get("provider"), s.get("region"), s.get("gpu"), s.get("shape"),
               (s.get("variant") or "standard"))
        s = dict(s)
        s["latest_availability"] = latest.get(key)
        enriched.append(s)

    generated = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    counts = {
        "providers": len(providers),
        "skus": len(skus),
        "active_skus": sum(1 for s in skus if s.get("status") == "active"),
        "gpus": len(gpus),
        "accelerator_variants": sum(len(g.get("variants", [])) for g in gpus),
        "channels": len(channels),
        "capacities": len(capacities),
        "availability_observations": len(availability),
    }
    catalog = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": generated.isoformat().replace("+00:00", "Z"),
        "counts": counts,
        "providers": providers,
        "gpus": gpus,
        "skus": enriched,
        "channels": channels,
        "capacities": capacities,
        "latest_availability": list(latest.values()),
    }
    split = {
        "providers": {"schema_version": SCHEMA_VERSION, "generated_at": catalog["generated_at"], "providers": providers},
        "gpus": {"schema_version": SCHEMA_VERSION, "generated_at": catalog["generated_at"], "gpus": gpus},
        "skus": {"schema_version": SCHEMA_VERSION, "generated_at": catalog["generated_at"], "skus": enriched},
        "availability/latest": {"schema_version": SCHEMA_VERSION, "generated_at": catalog["generated_at"],
                                 "observations": list(latest.values())},
    }
    return catalog, split


HEADERS = """# Cloudflare Pages headers. Keep CORS open: this is a public catalogue.
/v1/*
  Access-Control-Allow-Origin: *
  Access-Control-Allow-Methods: GET, HEAD, OPTIONS
  Cache-Control: public, max-age=300, must-revalidate
  X-Content-Type-Options: nosniff
/v1/schema/*
  Access-Control-Allow-Origin: *
  Cache-Control: public, max-age=86400
/assets/*
  Cache-Control: public, max-age=604800
/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data-dir", default=str(ROOT / "data"))
    ap.add_argument("--assets-dir", default=str(ROOT / "assets"))
    ap.add_argument("--out", default=str(ROOT / "dist"))
    args = ap.parse_args()

    data, out = Path(args.data_dir), Path(args.out)
    catalog, split = build(data)
    if out.exists():
        shutil.rmtree(out)
    (out / "v1" / "availability").mkdir(parents=True)

    (out / "index.html").write_text(HTML, encoding="utf-8")
    if Path(args.assets_dir).is_dir():
        shutil.copytree(args.assets_dir, out / "assets")

    sizes = {"v1/catalog.json": dump(out / "v1" / "catalog.json", catalog)}
    for name, payload in split.items():
        sizes[f"v1/{name}.json"] = dump(out / "v1" / f"{name}.json", payload)

    (out / "v1" / "schema").mkdir(parents=True, exist_ok=True)
    schemas = sorted((ROOT / "schema").glob("*.json"))
    for s in schemas:
        shutil.copy2(s, out / "v1" / "schema" / s.name)

    index = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": catalog["generated_at"],
        "counts": catalog["counts"],
        "resources": {
            "catalog": "/v1/catalog.json",
            "providers": "/v1/providers.json",
            "gpus": "/v1/gpus.json",
            "skus": "/v1/skus.json",
            "availability_latest": "/v1/availability/latest.json",
            "schemas": [f"/v1/schema/{s.name}" for s in schemas],
        },
    }
    sizes["v1/index.json"] = dump(out / "v1" / "index.json", index)
    (out / "_headers").write_text(HEADERS, encoding="utf-8")

    print(f"wrote {out}")
    for name, n in sorted(sizes.items()):
        print(f"  {name:32s} {n/1024:8.1f} KB")
    print(f"  {'assets/':32s} {sum(f.stat().st_size for f in (out/'assets').rglob('*') if f.is_file())/1024:8.1f} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
