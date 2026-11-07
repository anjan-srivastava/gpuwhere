"""Krutrim Cloud (Ola) — official docs pricing (Markdown) and GPU services page.

Krutrim is self-serve with a documented SDK, Terraform provider and API keys.
Its public pricing doc (docs.cloud.olakrutrim.com/basics/pricing/cpu-and-gpu.md)
currently lists CPU flavours only; GPU rates are shown in the console after
sign-up. This scraper therefore:

  * parses any GPU rows the pricing doc publishes (H100/H200/A100/L40S/B200…) into
    priced packages — so prices appear automatically once Krutrim publishes them;
  * otherwise emits quote_only packages for each GPU model the GPU services page
    advertises, with a price_note saying where the price is shown.
"""
from __future__ import annotations

import re

from pricing_common import Context, Package, Price, ScrapeResult, accel, html_to_text, num

PROVIDER = "krutrim-cloud"
PRICING_MD = "https://docs.cloud.olakrutrim.com/basics/pricing/cpu-and-gpu.md"
GPU_PAGE = "https://www.olakrutrim.com/gpu-services"
REGION = "IN"
MODELS = {"H100": "h100-sxm5", "H200": "h200-sxm", "A100": "a100-sxm4-80gb", "L40S": "l40s-pcie", "B200": "b200-sxm"}


def scrape(ctx: Context) -> ScrapeResult:
    res = ScrapeResult()
    md = ctx.get(PROVIDER, PRICING_MD)
    priced = set()
    for tr in re.findall(r"(?is)<tr>(.*?)</tr>", md):
        cells = [re.sub(r"<[^>]+>", "", c).strip() for c in re.findall(r"(?is)<td[^>]*>(.*?)</td>", tr)]
        if len(cells) < 4:
            continue
        model = next((m for m in MODELS if m in cells[0].upper()), None)
        if not model:
            continue  # CPU flavours
        n = re.search(r"(\d)\s*x", cells[0], re.I)
        gpus = int(n.group(1)) if n else 1
        spec = re.search(r"(\d+)\s*vCPU\s*/\s*(\d+)\s*GB", cells[1]) if len(cells) > 1 else None
        od = num(cells[3]) if re.search(r"\d", cells[3]) else None
        terms = {}
        for idx, months in ((4, 1), (5, 6), (6, 12)):
            if len(cells) > idx and re.search(r"\d", cells[idx]):
                terms[months] = Price(num(cells[idx]), "INR")
        res.packages.append(Package(
            provider=PROVIDER, region=REGION, accel=accel(MODELS[model]), gpus=gpus,
            on_demand=Price(od, "INR") if od else None, committed=terms, flavour=cells[0],
            vcpus=int(spec.group(1)) if spec else None, ram_gb=float(spec.group(2)) if spec else None,
            sources=[(PRICING_MD, "page")], confidence="medium",
            price_note=None if od else "No on-demand rate in the pricing doc.",
            notes=["Krutrim pricing doc; INR per hour; USD at the ECB reference rate. Per-second metering."],
        ))
        priced.add(model)

    text = html_to_text(ctx.get(PROVIDER, GPU_PAGE))
    advertised = [m for m in MODELS if re.search(rf"NVIDIA {m}\b", text)]
    if not advertised:
        res.warnings.append("no GPU models found on the Krutrim GPU services page")
    for m in advertised:
        if m in priced:
            continue
        res.packages.append(Package(
            provider=PROVIDER, region=REGION, accel=accel(MODELS[m]), gpus=1, on_demand=None,
            variant="console-price", sources=[(GPU_PAGE, "page"), (PRICING_MD, "page")], confidence="medium",
            price_note=f"Krutrim offers NVIDIA {m} VMs on demand and reserved, but publishes the rate only in the "
                       "console after sign-up; the public pricing doc lists CPU flavours only.",
            notes=["Self-serve: console, Python SDK and Terraform provider. Multi-GPU and bare-metal sizes are "
                   "offered but not published; form factor not published, SXM assumed."],
        ))
    if "Spliced" in text:
        res.unpriced.append("Spliced (fractional) GPUs: not a whole-GPU shape")
    return res
