"""Amazon Web Services India regions — AWS public pricing JSON (Linux on-demand).

Source: the static per-region price maps behind aws.amazon.com/ec2/pricing/on-demand
(b0.p.awsstatic.com, gzip JSON). Prices are USD per instance-hour, Linux, shared
tenancy, on-demand. GPU instance types are mapped to accelerators explicitly; any
unmapped accelerated type is reported so new sizes are noticed, never guessed.
Spot and Savings Plans are not taken from this source.
"""
from __future__ import annotations

import gzip
import json
import re
import urllib.parse

from pricing_common import Context, Package, Price, ScrapeResult, accel

PROVIDER = "aws"
BASE = ("https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/"
        "ec2-ondemand-without-sec-sel/{region}/Linux/index.json")
REGIONS = {"Asia Pacific (Mumbai)": "IN-BOM", "Asia Pacific (Hyderabad)": "IN-HYD"}
PAGE = "https://aws.amazon.com/ec2/pricing/on-demand/"


def _gpu_map(itype: str) -> tuple[str, int] | None:
    fam, _, size = itype.partition(".")
    fixed = {
        "p5.48xlarge": ("h100-sxm5", 8), "p5.4xlarge": ("h100-sxm5", 1), "p5e.48xlarge": ("h200-sxm", 8),
        "p5en.48xlarge": ("h200-sxm", 8), "p6-b200.48xlarge": ("b200-sxm", 8), "p6-b300.48xlarge": ("b300-sxm", 8),
        "p4d.24xlarge": ("a100-sxm4-40gb", 8), "p4de.24xlarge": ("a100-sxm4-80gb", 8),
        "g4dn.metal": ("t4-pcie", 8),
    }
    if itype in fixed:
        return fixed[itype]
    multi = {"12xlarge": 4, "24xlarge": 4, "48xlarge": 8}
    single = {"xlarge", "2xlarge", "4xlarge", "8xlarge", "16xlarge"}
    variant = {"g6e": "l40s-pcie", "g6": "l4-pcie", "gr6": "l4-pcie", "g4dn": "t4-pcie"}.get(fam)
    if not variant:
        return None
    if size in single:
        return variant, 1
    if size in multi:
        return variant, multi[size]
    return None


ACCEL_FAMILIES = re.compile(r"^(p\d|g\d|gr\d|inf\d|trn\d|dl\d)")


def scrape(ctx: Context) -> ScrapeResult:
    res = ScrapeResult()
    for region, code in REGIONS.items():
        url = BASE.format(region=urllib.parse.quote(region))
        raw = ctx.get(PROVIDER, url, binary=True)
        data = json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)
        items = next(iter(data["regions"].values()))
        for v in items.values():
            itype = v.get("Instance Type", "")
            if not ACCEL_FAMILIES.match(itype):
                continue
            m = _gpu_map(itype)
            if m is None:
                fam = itype.split(".")[0]
                if fam in ("g5", "g6f", "gr6f", "inf1", "inf2", "trn1", "trn2", "g5g", "dl1", "p2", "p3", "g4ad"):
                    res.unpriced.append(f"{itype} ({code}): {fam} (A10G/fractional/Trainium/Inferentia) not modelled")
                else:
                    res.warnings.append(f"unmapped AWS accelerated type {itype} in {region}; add it to _gpu_map")
                continue
            variant, n = m
            mem = re.match(r"([\d.]+)\s*GiB", v.get("Memory", ""))
            res.packages.append(Package(
                provider=PROVIDER, region=code, accel=accel(variant), gpus=n,
                on_demand=Price(float(v["price"]), "USD"), flavour=itype,
                variant=re.sub(r"[^a-z0-9]+", "-", itype.lower()).strip("-"),
                vcpus=int(v["vCPU"]) if v.get("vCPU", "").isdigit() else None,
                ram_gb=round(float(mem.group(1)) * 1.073741824, 1) if mem else None,
                sources=[(url, "feed"), (PAGE, "page")], confidence="high",
                notes=[f"AWS {region}, Linux on-demand (shared tenancy). Memory converted from GiB. "
                       "Spot and Savings Plans not included from this source."],
            ))
    return res
