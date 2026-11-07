"""Tata Communications Vayu AI Cloud — official GPUaaS price list (PDF, INR/hr).

Rows: GPU[.BM].<letter><vCPU>.<MODEL>.<n>X.OLU with on-demand and 3-month,
6-month, 1-, 3- and 4-year commit prices per instance-hour. The letter prefix
(D/H/E) distinguishes host configurations Tata does not describe in the PDF; it
is kept in the plan name. Needs `pdftotext` (poppler).
"""
from __future__ import annotations

import re
import subprocess
import tempfile

from pricing_common import Context, Package, Price, ScrapeResult, accel, num

PROVIDER = "tata-communications"
PDF = ("https://www.tatacommunications.com/hubfs/library/documents/"
       "Tata%20Communications%20Vayu%20AI%20Cloud%20GPU%20as%20a%20Service.pdf")
REGION = "IN"
MODELS = {"H100SXM": "h100-sxm5", "H200SXM": "h200-sxm", "H200NVL": "h200-nvl", "L40S": "l40s-pcie", "L4": "l4-pcie"}
TERMS = (3, 6, 12, 36, 48)
ROW = re.compile(r"(GPU\.(BM\.)?([A-Z])(\d+)\.([A-Z0-9]+)\.(\d)X\.OLU)\s+" + r"\s+".join([r"₹\s*([\d,]+)"] * 6))


def _pdf_text(data: bytes) -> str:
    with tempfile.NamedTemporaryFile(suffix=".pdf") as fh:
        fh.write(data)
        fh.flush()
        return subprocess.check_output(["pdftotext", "-layout", fh.name, "-"], text=True)


def scrape(ctx: Context) -> ScrapeResult:
    res = ScrapeResult()
    text = _pdf_text(ctx.get(PROVIDER, PDF, binary=True))
    if "hourly basis" not in text:
        res.warnings.append("'All prices are on an hourly basis' not found; check units")
    for m in ROW.finditer(text):
        flavour, bm, letter, vcpu, model, n = m.group(1, 2, 3, 4, 5, 6)
        n = int(n)
        if model not in MODELS:
            res.warnings.append(f"unmapped Tata model {model}")
            continue
        prices = [num(p) for p in m.groups()[6:12]]
        res.packages.append(Package(
            provider=PROVIDER, region=REGION, accel=accel(MODELS[model]), gpus=n,
            on_demand=Price(prices[0], "INR"),
            committed={t: Price(p, "INR") for t, p in zip(TERMS, prices[1:])},
            flavour=flavour, variant=re.sub(r"[^a-z0-9]+", "-", flavour.lower()).strip("-"),
            vcpus=int(vcpu), sources=[(PDF, "page")], confidence="medium",
            notes=[("Bare metal. " if bm else "VM. ")
                   + "Price list is INR per instance-hour; USD at the ECB reference rate. "
                   "vCPU count read from the plan name; RAM is not in the price list."],
        ))
    if not res.packages:
        res.warnings.append("no price rows parsed")
    return res
