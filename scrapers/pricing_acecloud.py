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

# Flavours the signed-in console actually offers, read from
# /api/v1/cloud/flavors per region on 2026-11-09 (CRN 41996). The rate card
# publishes many more packages than the order path does: H100, A100 and A30
# appear in no region, and multi-GPU shapes are absent everywhere except A2 in
# Mumbai. Anything not listed here is a reference rate, not an orderable package.
CONSOLE_FLAVOURS = {
    "IN-NOI": {"N.RTXA6000.128", "N.RTXA6000.64", "N.L4.32", "N.L4.64",
               "N.RTX6000ADA.64", "N.RTX6000ADA.128", "N.H200.28.282", "N.H200.24.192",
               "N.H200.16.128", "N.PRO6000.32.256", "N.PRO6000.16.128", "N.A2.32",
               "N.L40S.64", "N.L40S.128"},
    "IN-BOM": {"N.L4.32", "N.L4.64", "N.PRO4500.8.32", "N.PRO4500.16.64", "N.A2.32",
               "N.A2.64", "N.H200.16.128", "N.H200.24.192", "N.H200.28.282",
               "N.RTXA6000.64", "N.PRO6000.32.256", "N.PRO6000.16.128", "N.PRO6000.24.192"},
}
NOT_IN_CONSOLE = (
    "AceCloud's rate card lists this package, but the console flavour list "
    "(/api/v1/cloud/flavors, checked 2026-11-09) does not offer it, so it is not "
    "self-serve. No stock counts are published for any AceCloud GPU."
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
                self_serve = flavour in CONSOLE_FLAVOURS.get(region, set())
                if not self_serve:
                    notes.append(NOT_IN_CONSOLE)
                res.packages.append(Package(
                    provider=PROVIDER, region=region, accel=accel(variant), gpus=gpus,
                    on_demand=od, committed=committed, flavour=flavour,
                    variant=slug(flavour), vcpus=int(vcpus), ram_gb=float(ram),
                    sources=[(url, "page")], confidence="medium", notes=notes,
                    self_serve=self_serve,
                    price_note=None if self_serve else NOT_IN_CONSOLE,
                ))
    res.unpriced.append("RTX 8000 is listed in the AceCloud GPU menu without a plan page or specs; "
                        "no accelerator file, so not modelled.")
    return res
