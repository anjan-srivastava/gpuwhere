"""Append-only price ledger and refresh-run log.

Why JSONL and not DuckDB as the store:

* the repository's rule is PR review for every pricing change, so the history has
  to be a text diff;
* an append-only JSONL line survives a crashed job and can be read with no
  dependency;
* DuckDB is a *derived* query layer (``scripts/build_warehouse.py``) rebuilt from
  these files, never the only copy of a price.

Files
-----
``data/price-history/<provider>.jsonl``
    One line per price *change* (and the first observation of a package). A
    refresh that finds the same price appends nothing; ``data/runs`` proves the
    refresh did run, so "unchanged" and "we did not look" stay distinguishable.
``data/runs/refresh.jsonl``
    One line per provider per refresh invocation, including failures.
"""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
from typing import Iterable

PRICE_DIR = Path("data") / "price-history"
RUN_FILE = Path("data") / "runs" / "refresh.jsonl"

# Fields whose change means the ledger needs a new row. The price itself is
# compared through `terms()` (native amount where published, USD otherwise).
# `verified_at` and `sources[].fetched_at` move on every successful refresh even
# when the price is identical, so they are deliberately excluded.
FINGERPRINT_FIELDS = (
    "pricing_status",
    "billing_model",
    "self_serve",
    "status",
    "confidence",
    "gpu_variant",
)


def utc_now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def terms(sku: dict) -> dict:
    """The provider's economic terms, with FX-only movement removed.

    USD is canonical in the catalogue, but an INR-only provider does not change
    its price when the ECB rate moves. Compare the native amount when one is
    published, and only fall back to USD for USD-priced packages.
    """
    pricing = sku.get("pricing") or {}
    out: dict[str, object] = {}
    for mode in ("on_demand", "spot"):
        block = pricing.get(mode)
        if not block:
            continue
        native = {k: v for k, v in (block.get("native") or {}).items() if not k.startswith("fx_")}
        if native:
            out[mode] = {"native": native}
        else:
            out[mode] = {k: block.get(k)
                         for k in ("usd_per_gpu_hr", "usd_per_vm_hr", "notice_sec")
                         if k in block}
    out["committed"] = pricing.get("committed")
    return out


def fingerprint(sku: dict) -> str:
    payload = {field: sku.get(field) for field in FINGERPRINT_FIELDS}
    payload["terms"] = terms(sku)
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def primary_source(sku: dict) -> str:
    for source in sku.get("sources") or []:
        url = source.get("url")
        if url:
            return url
    raise ValueError(f"{sku.get('id')}: cannot record a price observation without a source URL")


def observation(sku: dict, ts: str, *, origin: str = "scrape", notes: str | None = None) -> dict:
    """The historical record of one SKU's current economic terms."""
    return {
        "ts": ts,
        "sku_id": sku["id"],
        "provider": sku["provider"],
        "region": sku["region"],
        "gpu": sku["gpu"],
        "gpu_variant": sku.get("gpu_variant"),
        "shape": sku["shape"],
        "variant": sku.get("variant"),
        "pricing": sku["pricing"],
        "pricing_status": sku.get("pricing_status"),
        "billing_model": sku.get("billing_model"),
        "self_serve": sku.get("self_serve"),
        "status": sku.get("status"),
        "confidence": sku.get("confidence"),
        "source": primary_source(sku),
        "verified_at": sku.get("verified_at"),
        "origin": origin,
        "notes": notes,
    }


def read_observations(path: Path) -> list[dict]:
    rows = []
    if not path.exists():
        return rows
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def latest_fingerprints(path: Path) -> dict[str, str]:
    """sku_id -> fingerprint from the last row written for that package."""
    latest: dict[str, str] = {}
    for row in read_observations(path):
        latest[row["sku_id"]] = fingerprint(row)
    return latest


def changed_observations(path: Path, skus: Iterable[dict], ts: str, *, origin: str = "scrape",
                         notes: str | None = None) -> list[dict]:
    """Rows worth appending: first sight of a package, or changed economic terms."""
    latest = latest_fingerprints(path)
    out = []
    for sku in skus:
        if latest.get(sku["id"]) != fingerprint(sku):
            out.append(observation(sku, ts, origin=origin, notes=notes))
    out.sort(key=lambda row: row["sku_id"])
    return out


def append_observations(root: Path, provider: str, skus: Iterable[dict], ts: str, *,
                        origin: str = "scrape", notes: str | None = None) -> dict:
    """Append changed prices for one provider. Returns counts, writes only if needed."""
    path = root / PRICE_DIR / f"{provider}.jsonl"
    observed = list(skus)
    rows = changed_observations(path, observed, ts, origin=origin, notes=notes)
    if rows:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as fh:
            for row in rows:
                fh.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")
    return {"observed": len(observed), "price_rows": len(rows), "unchanged": len(observed) - len(rows)}


def record_run(root: Path, *, job: str, provider: str, status: str, ts: str | None = None,
               duration_sec: float | None = None, counts: dict | None = None,
               error: str | None = None) -> dict:
    """Append one line to the refresh-run log (a heartbeat for the series)."""
    row = {
        "ts": ts or utc_now_iso(),
        "job": job,
        "provider": provider,
        "status": status,
        "duration_sec": None if duration_sec is None else round(duration_sec, 2),
        "counts": {k: v for k, v in (counts or {}).items() if isinstance(v, int) and not isinstance(v, bool)},
        "error": None if error is None else error[:500],
    }
    path = root / RUN_FILE
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")
    return row
