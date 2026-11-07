"""JarvisLabs — official CLI (`jl gpus --json`) plus the public pricing page.

Precedence: the CLI (official API) is primary for regions, per-GPU vCPU/RAM
and INR prices. The CLI reports `cpus_per_gpu` / `ram_per_gpu`, so an n-GPU
instance gets n× those. The pricing page states instances come in 1, 2, 4 or 8
GPUs and publishes USD per GPU-hour; it is recorded for cross-checking.
"""
from __future__ import annotations

import json
import re

from pricing_common import Context, Package, Price, ScrapeResult, accel, html_to_text

PROVIDER = "jarvislabs"
PAGE = "https://jarvislabs.ai/pricing"
CLI = "jl gpus --json"
COUNTS = (1, 2, 4, 8)

VARIANTS = {
    "H100": "h100-sxm5",
    "H200": "h200-sxm",
    "A100": "a100-sxm4-40gb",
    "A100-80GB": "a100-sxm4-80gb",
    "A30": "a30-pcie",
    "L4": "l4-pcie",
    "RTX-PRO6000": "rtx-pro-6000-blackwell",
}
PAGE_NAMES = {
    "NVIDIA H200 SXM": "H200", "NVIDIA H100 SXM": "H100",
    "NVIDIA RTX Pro 6000 Blackwell": "RTX-PRO6000", "NVIDIA A100 80GB": "A100-80GB",
    "NVIDIA A100 40GB": "A100", "NVIDIA A30": "A30", "NVIDIA L4": "L4",
}


def _page_usd(ctx: Context) -> dict[str, tuple[float, float | None]]:
    try:
        text = html_to_text(ctx.get(PROVIDER, PAGE))
    except Exception:
        return {}
    out = {}
    for name, key in PAGE_NAMES.items():
        m = re.search(re.escape(name) + r"\n[^\n]*VRAM[^\n]*\nOn-demand / hr\n\$([\d.]+)\nSpot / hr\n\$([\d.]+)", text)
        if m:
            out[key] = (float(m.group(1)), float(m.group(2)))
    return out


def scrape(ctx: Context) -> ScrapeResult:
    res = ScrapeResult()
    rows = json.loads(ctx.run(PROVIDER, CLI, ["jl", "gpus", "--json"]))
    page = _page_usd(ctx)
    seen = {}
    for r in rows:
        key = (r["region"], r["gpu_type"])
        # VM and container rows share a GPU pool and price; prefer the VM row.
        if key in seen and r.get("workload_type") != "vm":
            continue
        seen[key] = r
    for (region, gpu_type), r in sorted(seen.items()):
        if gpu_type not in VARIANTS:
            res.warnings.append(f"unmapped JarvisLabs GPU {gpu_type!r}")
            continue
        a = accel(VARIANTS[gpu_type])
        inr_od, inr_sp = r["price_per_hour"], r.get("spot_price")
        # JarvisLabs publishes one USD list on its pricing page, and it matches the
        # CLI's India-region INR prices. Use the provider's own USD there; convert
        # INR at the ECB rate only where no USD price is published (EU1).
        if gpu_type in page and region.startswith("IN"):
            usd_od, usd_sp = page[gpu_type]
            od = Price(usd_od, "USD", per="gpu")
            sp = Price(usd_sp, "USD", per="gpu") if inr_sp else None
            notes = [f"USD from jarvislabs.ai/pricing; `jl gpus --json` lists ₹{inr_od}/GPU-hr on-demand"
                     + (f", ₹{inr_sp} spot." if inr_sp else ".")]
            native = {"inr_per_gpu_hr_cli": inr_od}
        else:
            od = Price(inr_od, "INR", per="gpu")
            sp = Price(inr_sp, "INR", per="gpu") if inr_sp else None
            notes = ["No USD price published for this region; `jl gpus --json` INR converted at the ECB reference rate."]
            native = {}
        if a.variant.startswith("a100"):
            notes.append("Form factor not published; SXM assumed.")
        if r.get("workload_type") is None:
            notes.append("CLI row has no workload_type.")
        for n in COUNTS:
            res.packages.append(Package(
                provider=PROVIDER, region=region, accel=a, gpus=n,
                on_demand=od, spot=sp, native_extra=dict(native),
                variant=("a100-40gb" if a.variant == "a100-sxm4-40gb" else "standard") if a.gpu == "A100" else None,
                vcpus=r["cpus_per_gpu"] * n if r.get("cpus_per_gpu") else None,
                ram_gb=r["ram_per_gpu"] * n if r.get("ram_per_gpu") else None,
                vram_gb=float(r["vram"]) if r.get("vram") else None,
                sources=[(CLI, "api"), (PAGE, "page")], confidence="high", notes=list(notes),
            ))
    return res
