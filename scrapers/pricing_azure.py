"""Microsoft Azure India regions — Azure Retail Prices API (public, no auth).

Source: https://prices.azure.com/api/retail/prices (precedence: official API).
Linux pay-as-you-go rows (`type == "Consumption"`, product name without
"Windows") give on-demand; "<sku> Spot" rows give spot; `Reservation` rows give
1- and 3-year totals. Prices are per VM-hour in USD.

GPU VM sizes are mapped to accelerators explicitly. Any GPU-looking SKU that is
not in the map is reported as a warning so new sizes are noticed, never guessed.
vCPU count follows Azure's size naming (NC40 → 40 vCPU); host RAM is not in the
price API and stays null.
"""
from __future__ import annotations

import json
import re
import urllib.parse

from pricing_common import Context, Package, Price, ScrapeResult, accel

PROVIDER = "microsoft-azure"
API = "https://prices.azure.com/api/retail/prices"
REGIONS = {"centralindia": "IN-PNQ", "southindia": "IN-MAA", "westindia": "IN-BOM",
           "jioindiawest": "IN-JAM", "jioindiacentral": "IN-NAG"}  # Jio India West = Jamnagar, Central = Nagpur
GPU_TOKENS = ("H100", "H200", "A100", "MI300", "T4", "A10", "L40", "B200", "GB200", "V100")
# arm SKU → (accelerator variant, GPUs per VM)
SKUS = {
    "Standard_NC40ads_H100_v5": ("h100-nvl", 1),
    "Standard_NC80adis_H100_v5": ("h100-nvl", 2),
    "Standard_NC24ads_A100_v4": ("a100-pcie-80gb", 1),
    "Standard_NC48ads_A100_v4": ("a100-pcie-80gb", 2),
    "Standard_NC96ads_A100_v4": ("a100-pcie-80gb", 4),
    "Standard_ND96asr_v4": ("a100-sxm4-40gb", 8),
    "Standard_ND96amsr_A100_v4": ("a100-sxm4-80gb", 8),
    "Standard_ND96ams_A100_v4": ("a100-sxm4-80gb", 8),
    "Standard_ND96isr_H100_v5": ("h100-sxm5", 8),
    "Standard_ND96isr_H200_v5": ("h200-sxm", 8),
    "Standard_ND96isr_MI300X_v5": ("mi300x-oam", 8),
    "Standard_NC4as_T4_v3": ("t4-pcie", 1),
    "Standard_NC8as_T4_v3": ("t4-pcie", 1),
    "Standard_NC16as_T4_v3": ("t4-pcie", 1),
    "Standard_NC64as_T4_v3": ("t4-pcie", 4),
}
# Fractional-GPU sizes (A10 partitions) are not whole 1/2/4/8 shapes; reported, not modelled.
FRACTIONAL = re.compile(r"NV\d+adm?s_A10_v5|NVadsA10v5")


def _items(ctx: Context, region: str) -> list[dict]:
    flt = (f"armRegionName eq '{region}' and serviceName eq 'Virtual Machines' and ("
           + " or ".join(f"contains(armSkuName,'{t}')" for t in GPU_TOKENS) + ")")
    url = f"{API}?$filter={urllib.parse.quote(flt)}"
    out = []
    while url:
        d = json.loads(ctx.get(PROVIDER, url))
        out += d.get("Items", [])
        url = d.get("NextPageLink")
    return out


def scrape(ctx: Context) -> ScrapeResult:
    res = ScrapeResult()
    for region, code in REGIONS.items():
        items = [i for i in _items(ctx, region) if "Windows" not in i.get("productName", "")]
        by_sku: dict[str, dict] = {}
        for i in items:
            sku = i["armSkuName"]
            e = by_sku.setdefault(sku, {"od": None, "spot": None, "res": {}})
            name = i.get("skuName", "")
            if i.get("type") == "Consumption" and name.endswith(" Spot"):
                e["spot"] = i["retailPrice"]
            elif i.get("type") == "Consumption" and "Low Priority" not in name:
                e["od"] = i["retailPrice"]
            elif i.get("type") == "Reservation":
                months = {"1 Year": 12, "3 Years": 36}.get(i.get("reservationTerm"))
                if months:
                    e["res"][months] = i["retailPrice"]
        for sku, e in sorted(by_sku.items()):
            if sku not in SKUS:
                if FRACTIONAL.search(sku):
                    res.unpriced.append(f"{sku} ({region}): A10 size (fractional or no A10 accelerator spec), not modelled")
                else:
                    res.warnings.append(f"unmapped Azure GPU size {sku} in {region}; add it to SKUS")
                continue
            if e["od"] is None:
                continue
            variant, n = SKUS[sku]
            vcpu = re.search(r"_N[CDV](\d+)", sku)
            res.packages.append(Package(
                provider=PROVIDER, region=code, accel=accel(variant), gpus=n,
                on_demand=Price(e["od"], "USD"),
                spot=Price(e["spot"], "USD") if e["spot"] else None,
                committed={m: Price(t, "USD", unit="total", months=m) for m, t in e["res"].items()},
                flavour=sku, variant=re.sub(r"[^a-z0-9]+", "-", sku.lower().replace("standard_", "")).strip("-"),
                vcpus=int(vcpu.group(1)) if vcpu else None,
                sources=[(API, "api"), (f"https://azure.microsoft.com/pricing/details/virtual-machines/linux/#{region}", "page")],
                confidence="high",
                notes=[f"Azure region {region}. Linux pay-as-you-go; spot is evictable; reservations are 1/3-year totals. "
                       "vCPU from the size name; host RAM not in the price API."]
                      + (["Azure Jio India region (in Jio data centres; access aimed at Jio-partnership customers); no spot or reservation rates are listed."]
                         if region.startswith("jio") else []),
            ))
    return res
