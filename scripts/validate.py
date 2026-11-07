#!/usr/bin/env python3
"""Validate catalog files against their JSON Schemas.

Usage:
    python scripts/validate.py [--root .]
"""
from __future__ import annotations

import argparse
import json
import os
import sys

try:
    import jsonschema
except ImportError:
    print("jsonschema is not installed. Run: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(2)


def load(path: str):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def iter_files(root: str, pattern: str):
    base = os.path.join(root, "data")
    for dirpath, _, filenames in os.walk(base):
        for fn in filenames:
            if fn.endswith(pattern):
                yield os.path.join(dirpath, fn)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    root = args.root

    schemas = {
        "provider": load(os.path.join(root, "schema/provider.schema.json")),
        "sku": load(os.path.join(root, "schema/sku.schema.json")),
        "availability": load(os.path.join(root, "schema/availability.schema.json")),
        "incident": load(os.path.join(root, "schema/incident.schema.json")),
        "channel": load(os.path.join(root, "schema/channel.schema.json")),
        "capacity": load(os.path.join(root, "schema/capacity.schema.json")),
        "gpu": load(os.path.join(root, "schema/gpu.schema.json")),
    }

    errors = 0
    checked = 0

    def check(obj, schema, label):
        nonlocal errors, checked
        checked += 1
        try:
            jsonschema.validate(obj, schema)
        except jsonschema.ValidationError as exc:
            errors += 1
            print(f"FAIL {label}: {exc.message}")
            print(f"     at {list(exc.path)}")

    for path in iter_files(root, ".json"):
        rel = os.path.relpath(path, root)
        if "/providers/" in path:
            check(load(path), schemas["provider"], rel)
        elif "/skus/" in path:
            check(load(path), schemas["sku"], rel)
        elif "/incidents/" in path:
            check(load(path), schemas["incident"], rel)
        elif "/capacity/" in path:
            check(load(path), schemas["capacity"], rel)
        elif "/gpus/" in path:
            check(load(path), schemas["gpu"], rel)
        elif "/channels/" in path:
            check(load(path), schemas["channel"], rel)

    for path in iter_files(root, ".jsonl"):
        rel = os.path.relpath(path, root)
        with open(path, "r", encoding="utf-8") as fh:
            for n, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError as exc:
                    errors += 1
                    print(f"FAIL {rel}:{n}: invalid JSON: {exc}")
                    continue
                check(obj, schemas["availability"], f"{rel}:{n}")

    print(f"\nchecked {checked} records, {errors} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
