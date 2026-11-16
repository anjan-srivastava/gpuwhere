"""The DuckDB warehouse must be rebuildable from the text ledgers alone.

Skipped when duckdb is not installed; CI installs it so the query layer cannot rot.
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from helpers import ROOT, availability_files, jsonl_rows, price_history_files, run_files  # noqa: E402

try:
    import duckdb
    import build_warehouse
except ImportError:  # pragma: no cover - local runs without the optional dependency
    duckdb = None
    build_warehouse = None


def rows(files):
    return sum(len(jsonl_rows(f)) for f in files)


def empty_data(root: Path) -> None:
    for name in ("price-history", "availability", "runs", "skus", "providers",
                 "capacity", "inventory"):
        (root / "data" / name).mkdir(parents=True, exist_ok=True)


@unittest.skipIf(duckdb is None, "duckdb not installed (make warehouse installs it)")
class WarehouseBuild(unittest.TestCase):
    def test_rows_match_the_text_ledgers(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "warehouse.duckdb"
            counts = build_warehouse.build(ROOT, db)

            con = duckdb.connect(str(db))
            try:
                def q(sql):
                    return con.execute(sql).fetchall()

                self.assertEqual(rows(price_history_files()), counts["price_observation"])
                self.assertEqual(rows(availability_files()), counts["availability_observation"])
                self.assertEqual(rows(run_files()), counts["refresh_run"])

                distinct_skus = q("SELECT count(DISTINCT sku_id) FROM price_observation")[0][0]
                self.assertEqual(distinct_skus, q("SELECT count(*) FROM price_latest")[0][0])

                # refresh_health is a view: it must bind even when the run log is empty.
                q("SELECT * FROM refresh_health")

                self.assertGreater(q("SELECT count(*) FROM sku_current")[0][0], 0)
                q("SELECT * FROM sku_price_now")
            finally:
                con.close()

    def test_an_empty_checkout_still_builds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            empty_data(root)
            db = root / ".cache" / "warehouse.duckdb"
            counts = build_warehouse.build(root, db)
            self.assertEqual(0, counts["price_observation"])
            con = duckdb.connect(str(db))
            try:
                for view in ("price_latest", "price_change", "price_daily",
                             "availability_latest", "availability_daily",
                             "refresh_health", "sku_price_now"):
                    con.execute(f"SELECT * FROM {view}").fetchall()
            finally:
                con.close()


if __name__ == "__main__":
    unittest.main()
