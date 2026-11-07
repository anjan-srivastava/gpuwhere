"""Neysa — official pricing page (USD).

The page lists per-GPU on-demand rates ("Starts at $X / hour") offered in 1x,
2x and 4x sizes, plus a 36-month reserved monthly rate per GPU. Every instance
includes 100 GB disk (50 GB OS + 50 GB data). vCPU/RAM are not published.
8-GPU bare-metal nodes are listed with 36-month reserved monthly prices only.
"""
from __future__ import annotations

import re

from pricing_common import Context, Package, Price, ScrapeResult, accel, html_to_text, num

PROVIDER = "neysa"
PAGE = "https://neysa.ai/pricing/"
REGION = "IN-BOM"
NAMES = {
    "H200 SXM": "h200-sxm", "H100 SXM": "h100-sxm5", "L40S": "l40s-pcie", "L4": "l4-pcie",
    "RTX Pro 6000": "rtx-pro-6000-blackwell", "B300": "b300-sxm", "MI300X": "mi300x-oam",
}
VM_ROW = re.compile(r"^(H200 SXM|H100 SXM|L40S|L4|RTX Pro 6000) \((\d+)GB\)\nStarts at\n?\s*\$([\d.,]+)\n?\s*/ hour\nFrom \$([\d.,]+)/month", re.M)
BM_ROW = re.compile(r"^8 x ([A-Za-z0-9 ]+?) \(([\d,]+)GB\)\n(?:\$([\d.,]+)\n?\s*/ month\n36-month reserved)?", re.M)


def scrape(ctx: Context) -> ScrapeResult:
    res = ScrapeResult()
    text = html_to_text(ctx.get(PROVIDER, PAGE))
    if "1x, 2x and 4x" not in text:
        res.warnings.append("shape statement '1x, 2x and 4x' not found; shapes may have changed")
    found = set()
    for name, vram, hourly, reserved in VM_ROW.findall(text):
        found.add(name)
        for n in (1, 2, 4):
            res.packages.append(Package(
                provider=PROVIDER, region=REGION, accel=accel(NAMES[name]), gpus=n,
                on_demand=Price(num(hourly), "USD", per="gpu"),
                committed={36: Price(num(reserved), "USD", unit="month", per="gpu")},
                vram_gb=float(vram), disk_gb=100, disk_type="instance",
                sources=[(PAGE, "page")], confidence="medium",
                notes=["'Starts at' per-GPU rate; 100 GB disk included (50 GB OS + 50 GB data)."],
            ))
    for name in ("RTX Pro 6000",):
        if name not in found and f"{name} (" in text:
            res.packages.append(Package(
                provider=PROVIDER, region=REGION, accel=accel(NAMES[name]), gpus=1, on_demand=None,
                variant="quote", disk_gb=100, disk_type="instance", sources=[(PAGE, "page")],
                confidence="medium", price_note=f"{name} is listed with 'Price on request'.",
            ))
    for name, mem, monthly in BM_ROW.findall(text):
        name = name.strip()
        if name not in NAMES:
            res.warnings.append(f"unmapped Neysa bare-metal GPU {name!r}")
            continue
        committed = {36: Price(num(monthly), "USD", unit="month")} if monthly else {}
        res.packages.append(Package(
            provider=PROVIDER, region=REGION, accel=accel(NAMES[name]), gpus=8, on_demand=None,
            committed=committed, variant="bare-metal-reserved" if monthly else "bare-metal-quote",
            sources=[(PAGE, "page")], confidence="medium",
            price_note=(f"8-GPU bare-metal node: ${monthly}/month on a 36-month reservation; no on-demand rate published."
                        if monthly else "8-GPU bare-metal node: price on request."),
            notes=[f"Page lists total node GPU memory as {mem} GB."],
        ))
    if not found:
        res.warnings.append("no per-GPU rows parsed")
    return res
