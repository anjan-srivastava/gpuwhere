"""Data-contract and quality gates for the catalogue.

These are the checks a human reviewer would otherwise do by hand. They run in CI on every
push, so a bad merge fails before it reaches the published API.
"""
from __future__ import annotations

import datetime as dt
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import re
import unittest
from collections import Counter
from pathlib import Path

import jsonschema

from helpers import (DATA, ROOT, availability_files, availability_rows, capacity_files,
                     channel_files, gpu_files, incident_files, iter_records, load_json,
                     provider_files, rel, schemas, sku_files)


class SchemaContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schemas = schemas()

    def test_every_record_matches_its_schema(self):
        validator = {k: jsonschema.Draft202012Validator(v) for k, v in self.schemas.items()}
        failures = []
        for kind, path, record in iter_records():
            for err in validator[kind].iter_errors(record):
                failures.append(f"{rel(path)}: {err.message} at {list(err.path)}")
        self.assertEqual([], failures[:20], f"{len(failures)} schema failures")

    def test_schemas_reject_unknown_fields(self):
        """additionalProperties:false is the contract; without it typos silently disappear."""
        def walk(node, path):
            if isinstance(node, dict):
                if "properties" in node:
                    yield path, node.get("additionalProperties")
                for k, v in node.items():
                    yield from walk(v, f"{path}/{k}")
            elif isinstance(node, list):
                for i, v in enumerate(node):
                    yield from walk(v, f"{path}[{i}]")
        missing = [p for name, sch in self.schemas.items() for p, ap in walk(sch, name) if ap is not False]
        self.assertEqual([], missing, "objects without additionalProperties:false")


class ReferentialIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.providers = {load_json(p)["id"]: load_json(p) for p in provider_files()}
        cls.skus = [load_json(p) for p in sku_files()]
        cls.gpus = [load_json(p) for p in gpu_files()]
        cls.variants = {}
        for g in cls.gpus:
            for v in g.get("variants", []):
                vid = v.get("id", "")
                cls.variants[f"{g['supplier']}/{vid.split('/')[-1]}"] = (g, v)

    def test_sku_provider_exists(self):
        orphans = sorted({s["provider"] for s in self.skus} - set(self.providers))
        self.assertEqual([], orphans)

    def test_sku_id_matches_path(self):
        bad = []
        for f in sku_files():
            expected = str(f.relative_to(DATA / "skus")).removesuffix(".json").replace("\\", "/")
            if load_json(f)["id"] != expected:
                bad.append(f"{rel(f)}: id={load_json(f)['id']} path={expected}")
        self.assertEqual([], bad)

    def test_gpu_variant_resolves(self):
        bad = sorted({s["gpu_variant"] for s in self.skus} - {k.split("/")[-1] for k in self.variants})
        self.assertEqual([], bad)

    def test_unique_ids(self):
        dupes = [k for k, n in Counter(s["id"] for s in self.skus).items() if n > 1]
        self.assertEqual([], dupes)

    def test_capacity_and_incidents_reference_known_providers(self):
        bad = [rel(p) for p in capacity_files() + incident_files() if load_json(p).get("provider") not in self.providers]
        self.assertEqual([], bad)


class PricingMathematics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skus = [load_json(p) for p in sku_files()]

    def test_vm_price_equals_gpu_price_times_count(self):
        bad = []
        for s in self.skus:
            od = (s.get("pricing") or {}).get("on_demand") or {}
            gpu, vm, n = od.get("usd_per_gpu_hr"), od.get("usd_per_vm_hr"), s.get("gpus_per_vm")
            if gpu is None or vm is None or not n:
                continue
            if abs(vm - gpu * n) > max(0.05, 0.01 * vm):
                bad.append(f"{s['id']}: {gpu} x {n} != {vm}")
        self.assertEqual([], bad)

    def test_prices_are_positive_and_plausible(self):
        bad = []
        for s in self.skus:
            p = s.get("pricing") or {}
            for mode in ("on_demand", "spot"):
                v = (p.get(mode) or {}).get("usd_per_gpu_hr")
                if v is not None and not (0 < v < 1000):
                    bad.append(f"{s['id']} {mode}={v}")
            for c in p.get("committed") or []:
                v = c.get("usd_per_gpu_hr")
                if v is not None and not (0 < v < 1000):
                    bad.append(f"{s['id']} committed {c.get('term_months')}mo={v}")
        self.assertEqual([], bad)

    def test_discounts_never_exceed_on_demand(self):
        bad = []
        for s in self.skus:
            p = s.get("pricing") or {}
            od = (p.get("on_demand") or {}).get("usd_per_gpu_hr")
            if od is None:
                continue
            for mode in ("spot",):
                v = (p.get(mode) or {}).get("usd_per_gpu_hr")
                if v is not None and v > od * 1.05:
                    bad.append(f"{s['id']} {mode} {v} > on-demand {od}")
            for c in p.get("committed") or []:
                v = c.get("usd_per_gpu_hr")
                if v is not None and v > od * 1.05:
                    bad.append(f"{s['id']} committed {v} > on-demand {od}")
        self.assertEqual([], bad)

    def test_monthly_prices_say_so(self):
        """A monthly-converted rate without a note is indistinguishable from an hourly list price."""
        bad = []
        for s in self.skus:
            if s.get("billing_model") != "monthly":
                continue
            note = (s.get("notes") or "") + (s.get("price_note") or "")
            if "month" not in note.lower():
                bad.append(s["id"])
        self.assertEqual([], bad)


class DatesAndFreshness(unittest.TestCase):
    def test_verified_at_is_iso_date_and_not_in_the_future(self):
        today = dt.date.today()
        bad = []
        for s in [load_json(p) for p in sku_files() + provider_files() + gpu_files() + capacity_files()]:
            v = s.get("verified_at") or ""
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", v):
                bad.append(f"{s.get('id') or s.get('provider')}: verified_at={v!r}")
                continue
            if dt.date.fromisoformat(v) > today:
                bad.append(f"{s.get('id') or s.get('provider')}: verified_at in the future ({v})")
        self.assertEqual([], bad)


class AvailabilityIntegrity(unittest.TestCase):
    def test_rows_are_monotonic_per_provider_and_unique(self):
        bad = []
        for f in availability_files():
            rows = availability_rows(f)
            seen = set()
            last = ""
            for n, r in rows:
                ts = r.get("ts", "")
                if ts < last:
                    bad.append(f"{rel(f)}:{n} out of order ({ts} < {last})")
                last = ts
                key = (ts, r.get("provider"), r.get("region"), r.get("gpu"), r.get("shape"), r.get("variant"))
                if key in seen:
                    bad.append(f"{rel(f)}:{n} duplicate observation {key}")
                seen.add(key)
        self.assertEqual([], bad)

    def test_availability_points_at_real_skus(self):
        # Legacy rows may predate the canonical GPU spelling; compare through the same alias map
        # the server uses to join availability onto SKUs.
        alias = {"RTX-PRO6000": "RTX PRO 6000"}
        norm = lambda g: alias.get((g or "").strip(), (g or "").strip())
        skus = {(s["provider"], s["region"], norm(s["gpu"]), s["shape"]) for s in (load_json(p) for p in sku_files())}
        bad = []
        for f in availability_files():
            for n, r in availability_rows(f):
                if (r.get("provider"), r.get("region"), norm(r.get("gpu")), r.get("shape")) not in skus:
                    bad.append(f"{rel(f)}:{n} {r.get('provider')}/{r.get('region')}/{r.get('gpu')}/{r.get('shape')}")
        self.assertEqual([], bad[:10], f"{len(bad)} observations without a matching SKU")


class QualityBudgets(unittest.TestCase):
    """Evals: fail when coverage regresses, not when a single field is unknown."""

    @classmethod
    def setUpClass(cls):
        cls.skus = [load_json(p) for p in sku_files()]

    def test_every_sku_has_provenance(self):
        bad = [s["id"] for s in self.skus if not s.get("sources")]
        self.assertEqual([], bad)

    def test_spec_coverage_budget(self):
        n = len(self.skus)
        vcpu_missing = sum(1 for s in self.skus if s.get("vcpus") is None)
        self.assertLessEqual(vcpu_missing / n, 0.20, f"{vcpu_missing}/{n} SKUs without vCPU count")

    def test_status_and_pricing_status_are_set(self):
        bad = [s["id"] for s in self.skus if not s.get("pricing_status")]
        self.assertLessEqual(len(bad), int(0.02 * len(self.skus)), f"{len(bad)} SKUs without pricing_status: {bad[:5]}")

    def test_quote_only_offers_have_no_price(self):
        bad = [s["id"] for s in self.skus
               if s.get("pricing_status") == "quote_only"
               and ((s.get("pricing") or {}).get("on_demand") or {}).get("usd_per_gpu_hr") is not None]
        self.assertEqual([], bad)

    def test_residency_matches_region(self):
        bad = []
        for s in self.skus:
            r = s.get("region") or ""
            india = r == "IN" or r.startswith("IN-") or bool(re.match(r"^IN\d", r))
            want = "india" if india else "outside-india"
            if s.get("residency") not in (None, want):
                bad.append(f"{s['id']}: residency={s.get('residency')} region={r}")
        self.assertEqual([], bad)


if __name__ == "__main__":
    unittest.main()
