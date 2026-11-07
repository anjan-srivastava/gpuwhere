"""OVHcloud Public Cloud GPU instances — public order catalogue API (EUR, ex-VAT).

Source: https://api.ovh.com/1.0/order/catalog/public/cloud?ovhSubsidiary=IE
Each GPU flavour is an addon with full specs in blobs.technical (GPU model and
count, vCores, RAM, disks). Prices are in 1e-8 EUR: `*.consumption` = hourly
on-demand, `*.monthly.postpaid` = monthly commitment. Outside India (Europe), so
these packages are burst options without India data residency.
"""
from __future__ import annotations

import json

from pricing_common import Context, Package, Price, ScrapeResult, accel

PROVIDER = "ovhcloud"
API = "https://api.ovh.com/1.0/order/catalog/public/cloud?ovhSubsidiary=IE"
PAGE = "https://www.ovhcloud.com/en-ie/public-cloud/prices/"
REGION = "EU-FR"
# OVH GPU model → accelerator (OVH runs PCIe H100/A100; the 8x H200 node is HGX, SXM assumed)
MODELS = {"H100": "h100-pcie", "H200": "h200-sxm", "A100": "a100-pcie-80gb", "L40S": "l40s-pcie", "L4": "l4-pcie"}


def scrape(ctx: Context) -> ScrapeResult:
    res = ScrapeResult()
    d = json.loads(ctx.get(PROVIDER, API))
    flav: dict[str, dict] = {}
    for a in d.get("addons", []):
        tech = ((a.get("blobs") or {}).get("technical") or {})
        gpu = tech.get("gpu") or {}
        if a.get("product") != "publiccloud-instance" or not gpu.get("model"):
            continue
        name = a.get("invoiceName")
        e = flav.setdefault(name, {"tech": tech, "hour": None, "month": None})
        price = next((p for p in a.get("pricings", []) if p.get("price") is not None), None)
        if not price:
            continue
        if a["planCode"].endswith(".consumption") and price.get("intervalUnit") == "hour":
            e["hour"] = price["price"] / 1e8
        elif a["planCode"].endswith(".monthly.postpaid"):
            e["month"] = price["price"] / 1e8
    for name, e in sorted(flav.items()):
        t = e["tech"]
        model, n = t["gpu"]["model"].upper(), int(t["gpu"].get("number") or 0)
        if model not in MODELS:
            res.unpriced.append(f"{name}: {model} has no accelerator spec in the catalogue")
            continue
        if n not in (1, 2, 4, 8) or e["hour"] is None:
            res.unpriced.append(f"{name}: {n}x {model} (shape or hourly price not available)")
            continue
        disk = sum(dk.get("capacity", 0) * dk.get("number", 1) for dk in (t.get("storage") or {}).get("disks", []))
        res.packages.append(Package(
            provider=PROVIDER, region=REGION, accel=accel(MODELS[model]), gpus=n,
            on_demand=Price(e["hour"], "EUR"),
            committed={1: Price(e["month"], "EUR", unit="month")} if e["month"] else {},
            flavour=name, variant=name, vcpus=(t.get("cpu") or {}).get("cores"),
            ram_gb=(t.get("memory") or {}).get("size"), vram_gb=(t["gpu"].get("memory") or {}).get("size"),
            disk_gb=disk or None, disk_type="nvme" if disk else None,
            sources=[(API, "api"), (PAGE, "page")], confidence="high",
            notes=["OVHcloud Public Cloud (Europe; also offered in other OVH regions). EUR excl. VAT, converted at the ECB "
                   "reference rate. Outside India: no India data residency."],
        ))
    return res
