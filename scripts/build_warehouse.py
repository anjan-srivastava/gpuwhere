#!/usr/bin/env python3
"""Build a DuckDB warehouse from the append-only ledgers and current catalogue.

The JSONL files remain the source of truth. This script is a rebuildable read
model: delete the .duckdb file and rebuild it from the ledgers at any time.
(`warehouse_meta.built_at` records when the rebuild happened.)

    python scripts/build_warehouse.py
    python scripts/build_warehouse.py --db .cache/warehouse/gpu.duckdb
    python scripts/build_warehouse.py --parquet dist/v1/warehouse

Requires duckdb: `make warehouse` installs it on demand through uv.

Tables
------
price_observation        one row per price change (data/price-history)
availability_observation one row per stock check (data/availability)
refresh_run              one row per provider per refresh (data/runs)
sku_current              current host packages (data/skus)
provider_current         provider identity/capability (data/providers)
capacity_pool            installed-capacity pools (data/capacity)
inventory_check          logged-in stock checks (data/inventory)
warehouse_meta           build time and row counts

Views
-----
price_latest, price_change, price_daily
availability_latest, availability_daily
refresh_health, sku_price_now
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

WAREHOUSE_SCHEMA_VERSION = "1"


def j(value) -> str | None:
    return None if value is None else json.dumps(value, ensure_ascii=False, sort_keys=True)


def ts(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is not None:
        parsed = parsed.astimezone(dt.timezone.utc).replace(tzinfo=None)
    return parsed


def date(value: str | None) -> dt.date | None:
    return None if not value else dt.date.fromisoformat(value[:10])


def read_jsonl(paths: list[Path]) -> list[dict]:
    rows = []
    for path in paths:
        with path.open(encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    rows.append(json.loads(line))
    return rows


def read_json_dir(path: Path) -> list[dict]:
    return [json.loads(p.read_text()) for p in sorted(path.glob("*.json"))] if path.exists() else []


def price_rows(root: Path) -> list[tuple]:
    rows = []
    for r in read_jsonl(sorted((root / "data" / "price-history").glob("*.jsonl"))):
        p = r.get("pricing") or {}
        od = p.get("on_demand") or {}
        sp = p.get("spot") or {}
        rows.append((
            ts(r["ts"]), r["sku_id"], r.get("provider"), r.get("region"), r.get("gpu"),
            r.get("gpu_variant"), r.get("shape"), r.get("variant"),
            od.get("usd_per_gpu_hr"), od.get("usd_per_vm_hr"),
            sp.get("usd_per_gpu_hr"), sp.get("usd_per_vm_hr"),
            j(p.get("committed")), j(p), r.get("pricing_status"), r.get("billing_model"),
            r.get("self_serve"), r.get("status"), r.get("confidence"), r.get("source"),
            date(r.get("verified_at")), r.get("origin"), r.get("notes"),
        ))
    return rows


def availability_rows(root: Path) -> list[tuple]:
    rows = []
    for r in read_jsonl(sorted((root / "data" / "availability").glob("*.jsonl"))):
        rows.append((
            ts(r["ts"]), r.get("provider"), r.get("region"), r.get("gpu"), r.get("shape"),
            r.get("variant"), r.get("available_gpus"), r.get("available_vms"),
            r.get("spot_available_gpus"), r.get("spot_available_vms"), r.get("total_gpus"),
            r.get("vms_derived"), r.get("observed_via"), r.get("source"), r.get("confidence"),
        ))
    return rows


def run_rows(root: Path) -> list[tuple]:
    rows = []
    for r in read_jsonl(sorted((root / "data" / "runs").glob("*.jsonl"))):
        rows.append((
            ts(r["ts"]), r.get("job"), r.get("provider"), r.get("status"),
            r.get("duration_sec"), j(r.get("counts")), r.get("error"),
        ))
    return rows


def sku_rows(root: Path) -> list[tuple]:
    rows = []
    for r in read_skus(root):
        p = r.get("pricing") or {}
        od = p.get("on_demand") or {}
        sp = p.get("spot") or {}
        rows.append((
            r["id"], r.get("provider"), r.get("region"), r.get("gpu"), r.get("gpu_variant"),
            r.get("form_factor"), r.get("shape"), r.get("variant"), r.get("gpus_per_vm"),
            r.get("vram_gb_per_gpu"), r.get("vcpus"), r.get("ram_gb"), r.get("disk_gb"),
            r.get("disk_type"), od.get("usd_per_gpu_hr"), od.get("usd_per_vm_hr"),
            sp.get("usd_per_gpu_hr"), sp.get("usd_per_vm_hr"), j(p.get("committed")),
            r.get("billing_model"), r.get("pricing_status"), r.get("self_serve"),
            r.get("residency"), r.get("status"), r.get("confidence"), date(r.get("verified_at")),
        ))
    return rows


def read_skus(root: Path) -> list[dict]:
    base = root / "data" / "skus"
    return [json.loads(p.read_text()) for p in sorted(base.rglob("*.json"))] if base.exists() else []


def provider_rows(root: Path) -> list[tuple]:
    rows = []
    for r in read_json_dir(root / "data" / "providers"):
        storage = r.get("storage") or {}
        api = r.get("api") or {}
        rows.append((
            r.get("id"), r.get("name"), r.get("country"), r.get("status"),
            api.get("provisioning"), j(r.get("regions")), storage.get("mountable"),
            storage.get("shared"), storage.get("persistent"), r.get("confidence"),
            date(r.get("verified_at")),
        ))
    return rows


def capacity_rows(root: Path) -> list[tuple]:
    rows = []
    for r in read_json_dir(root / "data" / "capacity"):
        for pool in r.get("pools") or []:
            rows.append((
                r.get("provider"), pool.get("region"), pool.get("gpu"), pool.get("form_factor"),
                pool.get("total_gpus"), pool.get("rented_gpus"), pool.get("committed_gpus"),
                pool.get("free_gpus"), pool.get("power_mw"), r.get("as_of"),
                date(r.get("verified_at")), r.get("confidence"),
            ))
    return rows


def inventory_rows(root: Path) -> list[tuple]:
    rows = []
    for r in read_json_dir(root / "data" / "inventory"):
        rows.append((
            r.get("provider"), r.get("access"), r.get("login"), r.get("inventory"),
            r.get("stock_recorded"), r.get("order_path"), ts(r.get("last_checked_at")),
            j(r.get("blockers")), r.get("notes"), r.get("confidence"),
        ))
    return rows


TABLES = {
    "price_observation": (
        """CREATE TABLE price_observation (
             ts TIMESTAMP, sku_id VARCHAR, provider VARCHAR, region VARCHAR, gpu VARCHAR,
             gpu_variant VARCHAR, shape VARCHAR, variant VARCHAR,
             on_demand_usd_per_gpu_hr DOUBLE, on_demand_usd_per_vm_hr DOUBLE,
             spot_usd_per_gpu_hr DOUBLE, spot_usd_per_vm_hr DOUBLE,
             committed JSON, pricing_json JSON, pricing_status VARCHAR, billing_model VARCHAR,
             self_serve BOOLEAN, status VARCHAR, confidence VARCHAR, source VARCHAR,
             verified_at DATE, origin VARCHAR, notes VARCHAR
           )""",
        price_rows,
    ),
    "availability_observation": (
        """CREATE TABLE availability_observation (
             ts TIMESTAMP, provider VARCHAR, region VARCHAR, gpu VARCHAR, shape VARCHAR,
             variant VARCHAR, available_gpus BIGINT, available_vms BIGINT,
             spot_available_gpus BIGINT, spot_available_vms BIGINT, total_gpus BIGINT,
             vms_derived BOOLEAN, observed_via VARCHAR, source VARCHAR, confidence VARCHAR
           )""",
        availability_rows,
    ),
    "refresh_run": (
        """CREATE TABLE refresh_run (
             ts TIMESTAMP, job VARCHAR, provider VARCHAR, status VARCHAR,
             duration_sec DOUBLE, counts JSON, error VARCHAR
           )""",
        run_rows,
    ),
    "sku_current": (
        """CREATE TABLE sku_current (
             sku_id VARCHAR, provider VARCHAR, region VARCHAR, gpu VARCHAR, gpu_variant VARCHAR,
             form_factor VARCHAR, shape VARCHAR, variant VARCHAR, gpus_per_vm BIGINT,
             vram_gb_per_gpu DOUBLE, vcpus BIGINT, ram_gb DOUBLE, disk_gb DOUBLE, disk_type VARCHAR,
             on_demand_usd_per_gpu_hr DOUBLE, on_demand_usd_per_vm_hr DOUBLE,
             spot_usd_per_gpu_hr DOUBLE, spot_usd_per_vm_hr DOUBLE, committed JSON,
             billing_model VARCHAR, pricing_status VARCHAR, self_serve BOOLEAN,
             residency VARCHAR, status VARCHAR, confidence VARCHAR, verified_at DATE
           )""",
        sku_rows,
    ),
    "provider_current": (
        """CREATE TABLE provider_current (
             provider VARCHAR, name VARCHAR, country VARCHAR, status VARCHAR,
             provisioning VARCHAR, regions JSON, storage_mountable BOOLEAN,
             storage_shared BOOLEAN, storage_persistent BOOLEAN, confidence VARCHAR,
             verified_at DATE
           )""",
        provider_rows,
    ),
    "capacity_pool": (
        """CREATE TABLE capacity_pool (
             provider VARCHAR, region VARCHAR, gpu VARCHAR, form_factor VARCHAR,
             total_gpus BIGINT, rented_gpus BIGINT, committed_gpus BIGINT, free_gpus BIGINT,
             power_mw DOUBLE, as_of VARCHAR, verified_at DATE, confidence VARCHAR
           )""",
        capacity_rows,
    ),
    "inventory_check": (
        """CREATE TABLE inventory_check (
             provider VARCHAR, access VARCHAR, login VARCHAR, inventory VARCHAR,
             stock_recorded BOOLEAN, order_path VARCHAR, last_checked_at TIMESTAMP,
             blockers JSON, notes VARCHAR, confidence VARCHAR
           )""",
        inventory_rows,
    ),
}

VIEWS = {
    "price_latest": """
        CREATE VIEW price_latest AS
        SELECT * EXCLUDE (rn) FROM (
          SELECT *, row_number() OVER (PARTITION BY sku_id ORDER BY ts DESC) AS rn
          FROM price_observation
        ) WHERE rn = 1""",
    "price_change": """
        CREATE VIEW price_change AS
        SELECT *,
               on_demand_usd_per_gpu_hr
                 - lag(on_demand_usd_per_gpu_hr) OVER (PARTITION BY sku_id ORDER BY ts)
                 AS on_demand_delta,
               spot_usd_per_gpu_hr
                 - lag(spot_usd_per_gpu_hr) OVER (PARTITION BY sku_id ORDER BY ts)
                 AS spot_delta
        FROM price_observation""",
    "price_daily": """
        CREATE VIEW price_daily AS
        WITH days AS (
          SELECT UNNEST(generate_series(
            (SELECT min(ts)::DATE FROM price_observation),
            (SELECT max(ts)::DATE FROM price_observation),
            INTERVAL 1 DAY))::DATE AS day
        ),
        packages AS (SELECT DISTINCT sku_id FROM price_observation)
        SELECT d.day, p.sku_id, p.provider, p.region, p.gpu, p.shape, p.variant,
               p.on_demand_usd_per_gpu_hr, p.spot_usd_per_gpu_hr,
               p.pricing_status, p.status, p.self_serve, p.confidence,
               p.ts::DATE AS last_observed_on
        FROM packages s
        CROSS JOIN days d
        LEFT JOIN LATERAL (
          SELECT * FROM price_observation p
          WHERE p.sku_id = s.sku_id AND p.ts::DATE <= d.day
          ORDER BY p.ts DESC LIMIT 1
        ) p ON true
        WHERE p.sku_id IS NOT NULL""",
    "availability_latest": """
        CREATE VIEW availability_latest AS
        SELECT * EXCLUDE (rn) FROM (
          SELECT *, row_number() OVER (
            PARTITION BY provider, region, gpu, shape, coalesce(variant, '')
            ORDER BY ts DESC) AS rn
          FROM availability_observation
        ) WHERE rn = 1""",
    "availability_daily": """
        CREATE VIEW availability_daily AS
        SELECT * EXCLUDE (rn) FROM (
          SELECT *, row_number() OVER (
            PARTITION BY provider, region, gpu, shape, coalesce(variant, ''), ts::DATE
            ORDER BY ts DESC) AS rn
          FROM availability_observation
        ) WHERE rn = 1""",
    "refresh_health": """
        CREATE VIEW refresh_health AS
        SELECT ts::DATE AS day, job, provider,
               count(*) AS runs,
               count(*) FILTER (WHERE status = 'failed') AS failures,
               max(ts) AS last_run
        FROM refresh_run
        GROUP BY 1, 2, 3""",
    "sku_price_now": """
        CREATE VIEW sku_price_now AS
        SELECT s.sku_id, s.provider, s.region, s.gpu, s.shape, s.variant,
               s.status, s.self_serve, s.on_demand_usd_per_gpu_hr AS list_on_demand_usd_per_gpu_hr,
               p.on_demand_usd_per_gpu_hr AS latest_on_demand_usd_per_gpu_hr,
               p.spot_usd_per_gpu_hr AS latest_spot_usd_per_gpu_hr,
               p.ts AS latest_observed_at
        FROM sku_current s
        LEFT JOIN price_latest p ON p.sku_id = s.sku_id""",
}


def build(root: Path, db_path: Path, parquet_dir: Path | None = None) -> dict:
    try:
        import duckdb
    except ImportError:
        print("duckdb is not installed. Run `make warehouse`, or `pip install duckdb`.",
              file=sys.stderr)
        raise SystemExit(2)

    db_path.parent.mkdir(parents=True, exist_ok=True)
    db_path.unlink(missing_ok=True)
    con = duckdb.connect(str(db_path))
    counts = {}

    for name, (ddl, loader) in TABLES.items():
        con.execute(ddl)
        rows = loader(root)
        if rows:
            placeholders = ", ".join("?" for _ in rows[0])
            con.executemany(f"INSERT INTO {name} VALUES ({placeholders})", rows)
        counts[name] = len(rows)

    for name, ddl in VIEWS.items():
        con.execute(ddl)

    con.execute("CREATE TABLE warehouse_meta (key VARCHAR, value VARCHAR)")
    meta = [
        ("schema_version", WAREHOUSE_SCHEMA_VERSION),
        ("built_at", dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
         .replace("+00:00", "Z")),
        *[(f"rows_{name}", str(n)) for name, n in counts.items()],
    ]
    con.executemany("INSERT INTO warehouse_meta VALUES (?, ?)", meta)

    if parquet_dir:
        parquet_dir.mkdir(parents=True, exist_ok=True)
        export = ["price_observation", "availability_observation", "refresh_run",
                  "sku_current", "provider_current", "capacity_pool", "inventory_check",
                  "price_latest", "availability_latest"]
        for name in export:
            con.execute(
                f"COPY (SELECT * FROM {name}) TO '{(parquet_dir / f'{name}.parquet').as_posix()}' "
                "(FORMAT PARQUET, COMPRESSION ZSTD)")
        print(f"parquet  {parquet_dir}  ({len(export)} files)")

    con.close()
    return counts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument("--db", default=None, help="default <root>/.cache/warehouse/gpu-catalog.duckdb")
    ap.add_argument("--parquet", default=None, help="also export parquet files to this directory")
    args = ap.parse_args()

    root = Path(args.root)
    db_path = Path(args.db) if args.db else root / ".cache" / "warehouse" / "gpu-catalog.duckdb"
    counts = build(root, db_path, Path(args.parquet) if args.parquet else None)
    print(f"warehouse {db_path}")
    print("  " + ", ".join(f"{name}={n}" for name, n in counts.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
