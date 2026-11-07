"""Shared helpers for the catalogue test suite."""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SCHEMA = ROOT / "schema"
SCRAPERS = ROOT / "scrapers"
CACHE = ROOT / ".cache" / "scrape"

if str(SCRAPERS) not in sys.path:
    sys.path.insert(0, str(SCRAPERS))

SCHEMA_FILES = {
    "provider": "provider.schema.json",
    "sku": "sku.schema.json",
    "gpu": "gpu.schema.json",
    "inventory": "inventory.schema.json",
    "capacity": "capacity.schema.json",
    "incident": "incident.schema.json",
    "channel": "channel.schema.json",
    "availability": "availability.schema.json",
}


def load_json(path: Path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def schemas() -> dict:
    import jsonschema  # noqa: F401  (fail fast with a clear message)
    return {name: load_json(SCHEMA / fn) for name, fn in SCHEMA_FILES.items()}


def provider_files() -> list[Path]:
    return sorted((DATA / "providers").glob("*.json"))


def sku_files() -> list[Path]:
    return sorted((DATA / "skus").rglob("*.json"))


def gpu_files() -> list[Path]:
    return sorted((DATA / "gpus").glob("*/*.json"))


def inventory_files() -> list[Path]:
    return sorted((DATA / "inventory").glob("*.json"))


def capacity_files() -> list[Path]:
    return sorted((DATA / "capacity").glob("*.json"))


def incident_files() -> list[Path]:
    return sorted((DATA / "incidents").glob("*.json"))


def channel_files() -> list[Path]:
    return sorted((DATA / "channels").glob("*.json"))


def availability_files() -> list[Path]:
    return sorted((DATA / "availability").glob("*.jsonl"))


def availability_rows(path: Path) -> list[dict]:
    rows = []
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            line = line.strip()
            if line:
                rows.append((n, json.loads(line)))
    return rows


def iter_records():
    """Yield (kind, path, record) for every JSON/JSONL record in data/."""
    for kind, files in (
        ("provider", provider_files()), ("sku", sku_files()), ("gpu", gpu_files()),
        ("inventory", inventory_files()), ("capacity", capacity_files()), ("incident", incident_files()), ("channel", channel_files()),
    ):
        for f in files:
            yield kind, f, load_json(f)
    for f in availability_files():
        for n, row in availability_rows(f):
            yield "availability", f, row


def rel(path: Path) -> str:
    return os.path.relpath(path, ROOT)
