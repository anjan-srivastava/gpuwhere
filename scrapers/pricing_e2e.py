"""E2E Networks — official machine-readable pricing feed.

Source: https://www.e2enetworks.com/pricing.json (precedence: feed).
The feed lists one row per GPU model (a 1-GPU instance). It publishes USD and
INR on-demand prices as two independently set price lists, plus INR-only
committed (3+ month) and spot rates. Multi-GPU shapes are not published.
"""
from __future__ import annotations

import json
import re

from pricing_common import Context, FetchError, Package, Price, ScrapeResult, accel

PROVIDER = "e2e-networks"
FEED = "https://www.e2enetworks.com/pricing.json"
REGION = "IN-DEL"

# feed id → accelerator variant. Form factor is not published by E2E for
# A100/V100; SXM is assumed (AGENTS.md) and noted.
VARIANTS = {
    "b200": ("b200-sxm", True),
    "h200": ("h200-sxm", True),
    "h100": ("h100-sxm5", True),
    "rtx-pro-6000": ("rtx-pro-6000-blackwell", False),
    "a100-80gb": ("a100-sxm4-80gb", True),
    "a100-40gb": ("a100-sxm4-40gb", True),
    "a40": ("a40-pcie", False),
    "l40s": ("l40s-pcie", False),
    "v100": ("v100-sxm2-32gb", True),
    "a30": ("a30-pcie", False),
    "l4": ("l4-pcie", False),
    "t4": ("t4-pcie", False),
}


def scrape(ctx: Context) -> ScrapeResult:
    res = ScrapeResult()
    feed = json.loads(ctx.get(PROVIDER, FEED))
    for row in feed["gpuInstances"]:
        if row["id"] not in VARIANTS:
            res.warnings.append(f"unmapped E2E GPU id {row['id']!r} ({row.get('model')})")
            continue
        variant, assumed_sxm = VARIANTS[row["id"]]
        usd = row["pricing"]["usd"]["hourly"]
        inr = row["pricing"]["inr"]["hourly"]
        notes = [
            "E2E publishes USD and INR as independent price lists (not an FX conversion); "
            f"INR list price ₹{inr}/hr. INR is E2E's billing currency.",
        ]
        if assumed_sxm:
            notes.append("E2E does not publish the form factor; SXM assumed.")
        committed = {}
        if row.get("commitmentPricePerHourINR"):
            # Feed: committed-use rate for 3+ month contracts arranged with sales.
            committed[3] = Price(float(row["commitmentPricePerHourINR"]), "INR")
            notes.append("Committed (3+ month) and spot rates are INR-only in the feed; USD converted at the ECB reference rate.")
        spot = None
        if row.get("spotPricePerHourINR"):
            spot = Price(float(row["spotPricePerHourINR"]), "INR")
        sources = [(FEED, "feed")]
        if row.get("url"):
            sources.append((row["url"], "page"))
        res.packages.append(Package(
            provider=PROVIDER, region=REGION, accel=accel(variant), gpus=1,
            variant="a100-40gb" if row["id"] == "a100-40gb" else ("standard" if row["id"].startswith("a100") else None),
            on_demand=Price(usd, "USD"), spot=spot, committed=committed,
            vcpus=row.get("vcpus"), ram_gb=row.get("ramGB"), vram_gb=row.get("vramGB"),
            sources=sources, confidence="high", notes=notes,
            native_extra={"inr_list_per_vm_hr": inr},
        ))
        # Each GPU page states which multi-GPU configurations exist
        # ("8-GPU — configurations available") but publishes no price for them.
        if row.get("url"):
            try:
                md = ctx.get(PROVIDER, row["url"] + ".md")
            except FetchError as exc:
                res.warnings.append(str(exc))
                continue
            for n in sorted({int(x) for x in re.findall(r"\*\*[^*]*\*\*\s*(\d)-GPU\s*[—-]\s*configurations", md)}):
                if n in (2, 4, 8):
                    res.packages.append(Package(
                        provider=PROVIDER, region=REGION, accel=accel(variant), gpus=n, on_demand=None,
                        variant="a100-40gb" if row["id"] == "a100-40gb" else ("standard" if row["id"].startswith("a100") else None),
                        vram_gb=row.get("vramGB"), sources=[(row["url"] + ".md", "page")], confidence="medium",
                        price_note=f"E2E GPU page states '{n}-GPU configurations available' but publishes no price; "
                                   "per-GPU list rate applies to the 1-GPU instance only. Contact sales.",
                        notes=["vCPU/RAM for this configuration are not published."],
                    ))
    res.unpriced.append("Monthly/annual GPU plans: 'Contact Sales' (feed termPricing).")
    return res
