"""Cyfuture AI — official GPU pricing page (INR per instance-hour).

Table columns: instance name, compute unit model, GPU memory (GB), FP32, FP16,
vCPU, instance memory (GB), P2P BW, network BW, memory BW, on-demand/hr,
1/6/12-month reserved per hour. The INR table is static HTML.
"""
from __future__ import annotations

import html as htmlmod
import re

from pricing_common import Context, Package, Price, ScrapeResult, accel, num

PROVIDER = "cyfuture-ai"
PAGE = "https://cyfuture.ai/pricing"
REGION = "IN"
MODELS = [
    (r"B300", "b300-sxm"), (r"RTX PRO 6000", "rtx-pro-6000-blackwell"), (r"L40S", "l40s-pcie"),
    (r"MI325X", "mi325x-oam"), (r"MI300X", "mi300x-oam"), (r"H100 SXM", "h100-sxm5"), (r"V100", "v100-sxm2-32gb"),
    (r"A100", "a100-sxm4-80gb"), (r"Gaudi ?2", "gaudi2-oam"),
]


def _cells(tr: str) -> list[str]:
    cells = re.findall(r"(?is)<td[^>]*>(.*?)</td>", tr)
    out = []
    for c in cells:
        c = re.sub(r"(?is)\(\s*[\d.]+\s*%?\s*Discount\s*\)", "", c)
        out.append(re.sub(r"\s+", " ", htmlmod.unescape(re.sub(r"<[^>]+>", " ", c))).strip())
    return out


def _same(a: list[str], b: list[str]) -> bool:
    """Equal on vCPU, RAM and prices within 1% (copies differ in rounding)."""
    for x, y in zip(a[5:7] + a[10:14], b[5:7] + b[10:14]):
        if ("$" in x) != ("$" in y):
            return True  # one copy is the USD view of the same table
        try:
            fx, fy = num(x), num(y)
        except ValueError:
            if x != y:
                return False
            continue
        if abs(fx - fy) > 0.01 * max(fx, fy):
            return False
    return True


def scrape(ctx: Context) -> ScrapeResult:
    res = ScrapeResult()
    h = ctx.get(PROVIDER, PAGE)
    seen: dict[str, list[str]] = {}
    for tr in re.findall(r"(?is)<tr[^>]*>(.*?)</tr>", h):
        c = _cells(tr)
        if len(c) < 14 or not re.match(r"(?i)^(NVIDIA|AMD|Intel) \d+ ?x", c[1]):
            continue
        # The page renders each table twice; keep one copy, flag disagreements.
        if c[0] in seen:
            if not _same(seen[c[0]], c[:14]):
                res.warnings.append(f"duplicate tables disagree for {c[0]}: kept {seen[c[0]][5:14]}, other {c[5:14]}")
            continue
        seen[c[0]] = c[:14]
        name, model = c[0], c[1]
        n = int(re.match(r"(?i)^\w+ (\d+) ?x", model).group(1))
        variant = next((v for pat, v in MODELS if re.search(pat, model, re.I)), None)
        if variant is None:
            res.warnings.append(f"unmapped Cyfuture model {model!r}")
            continue
        if n not in (1, 2, 4, 8):
            continue
        od, m1, m6, m12 = c[10:14]
        def price(s: str) -> Price | None:
            if not re.search(r"\d", s):
                return None
            return Price(num(s), "USD" if "$" in s else "INR")
        committed = {t: price(p) for t, p in ((1, m1), (6, m6), (12, m12)) if price(p)}
        notes = ["Rates are INR per instance-hour; USD at the ECB reference rate."]
        vcpus, ram = int(num(c[5])), num(c[6])
        named = re.search(r"(\d+)v\.(\d+)m", name)
        if named and (int(named.group(1)) != vcpus or float(named.group(2)) != ram):
            notes.append(f"Plan name implies {named.group(1)} vCPU / {named.group(2)} GB; the table lists "
                         f"{vcpus} vCPU / {ram:g} GB (table used).")
        if variant in ("a100-sxm4-80gb", "v100-sxm2-32gb"):
            notes.append("Form factor not published; SXM assumed.")
        pkg = Package(
            provider=PROVIDER, region=REGION, accel=accel(variant), gpus=n,
            on_demand=price(od), committed=committed, flavour=name,
            vcpus=vcpus, ram_gb=ram, vram_gb=num(c[2]) / n,
            sources=[(PAGE, "page")], confidence="medium", notes=notes,
        )
        if pkg.on_demand is None:
            pkg.price_note = ("Reserved only; no on-demand rate published. "
                              + ", ".join(f"{t}-month ₹{p.amount:g}/hr" for t, p in sorted(committed.items())) + ".")
        res.packages.append(pkg)
    if not res.packages and not res.unpriced:
        res.warnings.append("no rows parsed")
    return res
