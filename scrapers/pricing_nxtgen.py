"""NxtGen SpeedCloud — official AI instance rate card (INR per instance-hour).

Columns: instance, compute units, GPU memory, FP32, FP16, vCPU, instance memory,
P2P bandwidth, network bandwidth, memory bandwidth, on-demand, 1/6/12 month.
B200 is sold as 1,024–4,096 GPU clusters only (not a 1/2/4/8 shape).
"""
from __future__ import annotations

import re

from pricing_common import Context, Package, Price, ScrapeResult, accel, html_to_text, num

PROVIDER = "nxtgen"
PAGE = "https://speedcloud.nxtgen.com/aiinstances.html"
HOME = "https://speedcloud.nxtgen.com/"  # product cards carry a "SOLD OUT" badge
CARD_MODELS = {"NVIDIA H100": "H100NVL", "NVIDIA H200": "H200SXM", "NVIDIA L40S": "L40S", "AMD MI325X": "MI325X"}
GPU_RAM = {"H100NVL": 94, "H200SXM": 141, "L40S": 48, "MI325X": 256}
REGION = "IN"
MODELS = {"H200SXM": "h200-sxm", "H100NVL": "h100-nvl", "L40S": "l40s-pcie", "MI325X": "mi325x-oam"}
PRICE = r"(₹ ?[\d,]+|N/A)"
ROW = re.compile(r"^([A-Z0-9]+)\.(\d)x\n" + r"\n".join([r"([\d.]+)"] * 9) + r"\n" + r"\n".join([PRICE] * 4), re.M)
CLUSTER = re.compile(r"^B200SXM Cluster (\d+)x\n(?:[\d.]+\n){9}" + r"\n".join([PRICE] * 4), re.M)


def cards(ctx: Context) -> dict[tuple[str, int], dict]:
    """(rate-card model, GPU count) → {"name", "sold_out"} from the SpeedCloud homepage cards.

    Each card shows the GPU model before its plan name (e.g. 'NVIDIA H200 | GPU | H4-Titan')
    and the total GPU RAM after it; GPU count = GPU RAM / per-GPU memory.
    """
    text = html_to_text(ctx.get(PROVIDER, HOME))
    out = {}
    card = re.compile(r"^(NVIDIA H100|NVIDIA H200|NVIDIA L40S|AMD MI325X|Intel Gaudi-\d) GPU\n"
                      r"(?:[^\n]*\n){0,3}?([A-Z]\d-[A-Z][a-z]+)\n", re.M)
    for m in card.finditer(text):
        label, name = m.group(1), m.group(2)
        body = text[m.end():m.end() + 600]
        head = body.split("vCPUs", 1)[0]          # badge sits between the plan name and the specs
        ram = re.search(r"([\d,]+)\nGB\nGPU RAM", body)
        model = CARD_MODELS.get(label)
        if not model or not ram:
            continue
        n = round(int(ram.group(1).replace(",", "")) / GPU_RAM[model])
        out[(model, n)] = {"name": name, "sold_out": bool(re.search(r"SOLD\s*OUT", head, re.I))}
    return out


def scrape(ctx: Context) -> ScrapeResult:
    res = ScrapeResult()
    try:
        stock = cards(ctx)
    except Exception as exc:  # stock badges are optional; prices still come from the rate card
        stock = {}
        res.warnings.append(f"could not read SpeedCloud product cards: {exc}")
    if not stock:
        res.warnings.append("no product cards parsed from the SpeedCloud homepage; sold-out status unknown")
    text = html_to_text(ctx.get(PROVIDER, PAGE))
    for m in ROW.finditer(text):
        model, n = m.group(1), int(m.group(2))
        if model not in MODELS:
            res.warnings.append(f"unmapped NxtGen model {model}")
            continue
        gpu_mem, vcpu, inst_mem = float(m.group(4)), int(float(m.group(7))), float(m.group(8))
        od, m1, m6, m12 = m.group(12, 13, 14, 15)
        committed = {t: Price(num(p), "INR") for t, p in ((1, m1), (6, m6), (12, m12)) if p != "N/A"}
        card = stock.get((model, n))
        status, extra, sources = "active", [], [(PAGE, "page")]
        if card:
            sources.append((HOME, "page"))
            if card["sold_out"]:
                status = "unavailable"
                extra.append(f"SpeedCloud homepage marks the matching plan '{card['name']}' SOLD OUT.")
            else:
                extra.append(f"Matching SpeedCloud plan '{card['name']}' is listed as available.")
        res.packages.append(Package(
            provider=PROVIDER, region=REGION, accel=accel(MODELS[model]), gpus=n,
            on_demand=Price(num(od), "INR") if od != "N/A" else None,
            committed=committed, flavour=f"{model}.{n}x",
            vcpus=vcpu, ram_gb=inst_mem, vram_gb=gpu_mem / n, status=status,
            sources=sources, confidence="medium",
            notes=["Rate card prices are INR per instance-hour for each term; USD at the ECB reference rate."] + extra,
        ))
    clusters = CLUSTER.findall(text)
    if clusters:
        parts = []
        for size, od, m1, m6, m12 in clusters:
            per_gpu = num(m1) / int(size) if m1 != "N/A" else None
            parts.append(f"{size}-GPU cluster ₹{m1.replace('₹', '').strip()}/hr on 1-month term"
                         + (f" (≈₹{per_gpu:.0f}/GPU-hr)" if per_gpu else ""))
        res.packages.append(Package(
            provider=PROVIDER, region=REGION, accel=accel("b200-sxm"), gpus=8, on_demand=None,
            variant="cluster-quote", sources=[(PAGE, "page")], confidence="medium",
            price_note="B200 is sold only as 1,024–4,096 GPU clusters with term pricing; no on-demand or 8-GPU rate. "
                       + "; ".join(parts) + ".",
            notes=["Modelled on the 8x shape (one HGX node) so the offering is visible; not separately rentable."],
        ))
    if not res.packages:
        res.warnings.append("no instance rows parsed")
    return res
