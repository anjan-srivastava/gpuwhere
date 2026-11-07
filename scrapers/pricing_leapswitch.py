"""Leapswitch — official GPU server table and GPU cloud cart (INR per month).

Two official pages:
  * https://leapswitch.com/gpu-cloud/ — GPU | VRAM | vCPU | RAM | Disk | ₹/GPU/month
  * https://service.leapswitch.com/cart/gpu-cloud-servers-inr — 1-GPU VM plans
Prices are monthly and exclude GST (the cart adds 18% at checkout).
"""
from __future__ import annotations

import re

from pricing_common import Context, Package, Price, ScrapeResult, accel, html_to_text, num

PROVIDER = "leapswitch"
GPU_PAGE = "https://leapswitch.com/gpu-cloud/"
CART = "https://service.leapswitch.com/cart/gpu-cloud-servers-inr"
REGION = "IN"
MODELS = {
    "Nvidia H200": "h200-sxm", "Nvidia RTX PRO 6000": "rtx-pro-6000-blackwell", "Nvidia L4": "l4-pcie",
    "Nvidia RTX A4000": "rtx-a4000-pcie", "Nvidia RTX A5000": "rtx-a5000-pcie", "Nvidia RTX A6000": "rtx-a6000-pcie",
    "Nvidia A100": "a100-pcie-80gb", "Nvidia RTX A40": "a40-pcie",
}
TABLE_ROW = re.compile(r"^(Nvidia [A-Za-z0-9 ]+?)\n(\d+)GB\n(\d+)\n(\d+)GB\n(\d+)GB\n(₹[\d,]+|On CloudPe)", re.M)
CART_ROW = re.compile(
    r"^([A-Z0-9]+ VM)\nRs\. ([\d,.]+)\n/ Monthly\nProcessor\n([^\n]+)\nGPU\n(Nvidia [^\n]+)\nGPU RAM\n([^\n]+)\n"
    r"Cores\n(\d+)(?: vCPU)?\nRAM\n(\d+) GB\nStorage\n(\d+) GB", re.M)


def scrape(ctx: Context) -> ScrapeResult:
    res = ScrapeResult()
    text = html_to_text(ctx.get(PROVIDER, GPU_PAGE))
    for name, vram, vcpu, ram, disk, price in TABLE_ROW.findall(text):
        if price == "On CloudPe":
            res.packages.append(Package(
                provider=PROVIDER, region=REGION, accel=accel(MODELS[name]), gpus=1, on_demand=None,
                variant="cloudpe-quote", vcpus=int(vcpu), ram_gb=float(ram), disk_gb=float(disk),
                vram_gb=float(vram), sources=[(GPU_PAGE, "page")], confidence="medium",
                price_note="Listed on the Leapswitch GPU page as 'On CloudPe' (deploy via CloudPe); no Leapswitch price.",
            ))
            continue
        notes = ["Price per GPU per month, excl. GST."]
        if name == "Nvidia H200":
            notes.append("Form factor not published; SXM assumed.")
        res.packages.append(Package(
            provider=PROVIDER, region=REGION, accel=accel(MODELS[name]), gpus=1,
            on_demand=Price(num(price), "INR", unit="month", per="gpu"),
            vcpus=int(vcpu), ram_gb=float(ram), disk_gb=float(disk), vram_gb=float(vram),
            sources=[(GPU_PAGE, "page")], confidence="medium", notes=notes,
        ))
    cart = html_to_text(ctx.get(PROVIDER, CART))
    for plan, price, cpu, gpu, gpu_ram, cores, ram, disk in CART_ROW.findall(cart):
        if gpu not in MODELS:
            res.warnings.append(f"unmapped Leapswitch GPU {gpu!r}")
            continue
        notes = [f"Cart plan '{plan}' ({cpu}); price per VM per month, excl. GST; 10 TB bandwidth."]
        if gpu == "Nvidia A100":
            notes.append(f"Cart lists GPU RAM as '{gpu_ram}' (A100 80GB uses HBM2e); form factor not published, PCIe assumed for a single-GPU VM.")
        if gpu == "Nvidia RTX A40":
            notes.append("Cart names it 'RTX A40'; NVIDIA's product is the A40.")
        vram = re.search(r"(\d+)\s*GB", gpu_ram)
        res.packages.append(Package(
            provider=PROVIDER, region=REGION, accel=accel(MODELS[gpu]), gpus=1,
            on_demand=Price(num(price), "INR", unit="month"), flavour=plan,
            vcpus=int(cores), ram_gb=float(ram), disk_gb=float(disk),
            vram_gb=float(vram.group(1)) if vram else None,
            sources=[(CART, "page")], confidence="medium", notes=notes,
        ))
    return res
