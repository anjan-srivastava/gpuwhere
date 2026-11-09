"""Scraper tests: parser regressions, output contract, and pure-helper logic.

Two layers:

* Unit tests for `pricing_common` (parsing numbers, HTML flattening, FX maths, SKU assembly)
  that never touch the network or the cache.
* Replay tests that run each provider's scraper against the last on-disk snapshot in
  `.cache/scrape` in offline mode. These are skipped when no snapshot is present, so a fresh
  clone still gets a green suite; CI refreshes the cache before running them.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import jsonschema

from helpers import CACHE, ROOT, schemas  # noqa: E402

import pricing_common as pc  # noqa: E402
import pricing_refresh as pr  # noqa: E402


class PureHelpers(unittest.TestCase):
    def test_num_parses_published_forms(self):
        self.assertEqual(4.5, pc.num("$4.50"))
        self.assertEqual(3784.0, pc.num("₹3,784.00"))
        self.assertEqual(2.89, pc.num("2.89/h"))
        self.assertEqual(93.9225, pc.num("93.9225"))
        with self.assertRaises(ValueError):
            pc.num("Contact us")

    def test_html_to_text_drops_markup_and_scripts(self):
        text = pc.html_to_text("<div>H100 <b>SXM5</b></div><script>x=1</script><style>.a{}</style>")
        self.assertIn("H100", text)
        self.assertIn("SXM5", text)
        self.assertNotIn("x=1", text)
        self.assertNotIn(".a", text)

    def test_vm_price_is_gpu_price_times_count(self):
        pkg = pc.Package(
            provider="x", region="IN", accel=pc.accel("h100-sxm5"), gpus=4,
            on_demand=pc.Price(2.5, "USD", per="gpu"),
            sources=[("https://example.test", "page")], confidence="high",
        )
        sku = pc.package_to_sku(pkg, "standard", None, "2026-11-08")
        od = sku["pricing"]["on_demand"]
        self.assertAlmostEqual(od["usd_per_vm_hr"], od["usd_per_gpu_hr"] * 4, places=2)

    def test_inr_convert_records_native_and_fx_date(self):
        fx = pc.Fx(usd_inr=90.0, date="2026-11-07", source="ecb")
        pkg = pc.Package(
            provider="x", region="IN", accel=pc.accel("a100-sxm4-80gb"), gpus=1,
            on_demand=pc.Price(900.0, "INR", per="gpu"),
            sources=[("https://example.test", "page")], confidence="medium",
        )
        sku = pc.package_to_sku(pkg, "standard", fx, "2026-11-08")
        od = sku["pricing"]["on_demand"]
        self.assertAlmostEqual(od["usd_per_gpu_hr"], 10.0, places=2)
        self.assertEqual(90.0, od["native"]["fx_usd_inr"])


class ScraperReplay(unittest.TestCase):
    """Run each scraper against its newest cached snapshot; assert it still parses."""

    @classmethod
    def setUpClass(cls):
        cls.schemas = schemas()
        cls.sku_validator = jsonschema.Draft202012Validator(cls.schemas["sku"])

    def _cache_days(self, provider: str):
        base = CACHE / provider
        if not base.is_dir():
            return []
        return [(base / d.name, d.name) for d in sorted(base.iterdir(), reverse=True) if d.is_dir()]

    def _fx(self, ctx):
        snap = CACHE / "_fx"
        if not snap.is_dir():
            return None
        days = sorted(d.name for d in snap.iterdir() if d.is_dir())
        if not days:
            return None
        # Point the context at the FX snapshot day, then load it offline.
        old = ctx.today
        ctx.today = days[-1]
        try:
            return ctx.fx
        except Exception:
            return None
        finally:
            ctx.today = old

    def test_every_scraper_parses_its_snapshot(self):
        from helpers import load_json  # noqa: F401

        checked = 0
        for provider, module_name in sorted(pr.SCRAPERS.items()):
            with self.subTest(provider=provider):
                days = self._cache_days(provider)
                if not days:
                    self.skipTest(f"no cached snapshot for {provider}")
                mod = __import__(module_name)
                res = None
                # Availability collectors write into the same day directory, so the newest
                # day can be a partial page set. Walk back to the newest day the pricing
                # scraper can actually parse offline.
                for day_dir, day in days:
                    ctx = pc.Context(CACHE, day, offline=True)
                    try:
                        res = mod.scrape(ctx)
                    except pc.FetchError:
                        continue
                    if res.packages:
                        break
                if res is None or not res.packages:
                    self.skipTest(f"{provider}: no complete pricing snapshot")
                fx = self._fx(ctx) if any(pr._needs_fx(p) for p in res.packages) else None
                if fx is None and any(pr._needs_fx(p) for p in res.packages):
                    self.skipTest(f"{provider}: needs an FX snapshot to convert INR prices")

                seen = set()
                for pkg, variant in pc.assign_variants(res.packages):
                    sku = pc.package_to_sku(pkg, variant, fx, day)
                    key = (sku["region"], sku["gpu"], sku["shape"], sku["variant"])
                    self.assertNotIn(key, seen, f"{provider}: duplicate package {key}")
                    seen.add(key)
                    errors = list(self.sku_validator.iter_errors(sku))
                    self.assertEqual([], [e.message for e in errors], f"{provider}: invalid SKU {sku['id']}")
                    for mode in ("on_demand", "spot"):
                        v = (sku.get("pricing", {}).get(mode) or {}).get("usd_per_gpu_hr")
                        if v is not None:
                            self.assertGreater(v, 0, f"{provider} {sku['id']} {mode}")
                            self.assertLess(v, 1000, f"{provider} {sku['id']} {mode}")
                    self.assertTrue(sku.get("sources"), f"{provider} {sku['id']} has no source")
                checked += 1
        self.assertGreater(checked, 0, "no provider snapshots available to replay")


if __name__ == "__main__":
    unittest.main()
