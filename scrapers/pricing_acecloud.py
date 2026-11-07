"""AceCloud — official per-GPU plan pages (USD list), Noida and Mumbai.

Each page lists flavours: GPUs, vCPUs, RAM, Hourly (or '---' where hourly
billing is not offered in that region), Monthly, 6-month total, 12-month total.
Atlanta is out of scope (India catalogue).
"""
from __future__ import annotations

import re

from pricing_common import Context, FetchError, Package, Price, ScrapeResult, accel, html_to_text, num, slug

PROVIDER = "acecloud"
BASE = "https://acecloud.ai/pricing/linux/usd/{region}/{page}/"
REGIONS = {"noida": "IN-NOI", "mumbai": "IN-BOM"}
PAGES = {
    "nvidia-h200-nvl": "h200-nvl",
    "nvidia-h100-hgx": "h100-sxm5",
    "nvidia-a100-80gb": "a100-sxm4-80gb",
    "nvidia-l40s-48gb": "l40s-pcie",
    "nvidia-l4-24gb": "l4-pcie",
    "nvidia-a30-24gb": "a30-pcie",
    "nvidia-a2-16gb": "a2-pcie",
    "rtx-pro-6000-96gb": "rtx-pro-6000-blackwell",
    "rtx-pro-4500": "rtx-pro-4500-blackwell",
    "nvidia-rtx-6000-ada-48gb": "rtx-6000-ada-pcie",
    "rtx-a6000-48gb": "rtx-a6000-pcie",
}
ROW = re.compile(
    r"(N\.[A-Z0-9.]+)\n(\d)x\n(\d+)\n(\d+)\n(\$[\d.,]+|-+)\n\$([\d,]+)\n\$([\d,]+)\n\$([\d,]+)"
)


def scrape(ctx: Context) -> ScrapeResult:
    res = ScrapeResult()
    for rslug, region in REGIONS.items():
        for page, variant in PAGES.items():
            url = BASE.format(region=rslug, page=page)
            try:
                text = html_to_text(ctx.get(PROVIDER, url))
            except FetchError as exc:
                res.warnings.append(str(exc))
                continue
            rows = ROW.findall(text)
            if not rows:
                res.warnings.append(f"no plan rows parsed from {url}")
            for flavour, gpus, vcpus, ram, hourly, monthly, m6, m12 in rows:
                gpus = int(gpus)
                if gpus not in (1, 2, 4, 8):
                    continue
                monthly_p = Price(num(monthly), "USD", unit="month")
                committed = {6: Price(num(m6), "USD", unit="total", months=6),
                             12: Price(num(m12), "USD", unit="total", months=12)}
                notes = []
                if hourly.startswith("$"):
                    od = Price(num(hourly), "USD")
                    committed[1] = monthly_p
                else:
                    od = monthly_p
                    notes.append(f"Hourly billing not offered for this flavour in {rslug.title()}.")
                if variant == "a100-sxm4-80gb":
                    notes.append("AceCloud does not publish the A100 form factor; SXM assumed.")
                res.packages.append(Package(
                    provider=PROVIDER, region=region, accel=accel(variant), gpus=gpus,
                    on_demand=od, committed=committed, flavour=flavour,
                    variant=slug(flavour), vcpus=int(vcpus), ram_gb=float(ram),
                    sources=[(url, "page")], confidence="medium", notes=notes,
                ))
    res.unpriced.append("RTX 8000 is listed in the AceCloud GPU menu without a plan page or specs; "
                        "no accelerator file, so not modelled.")
    return res
