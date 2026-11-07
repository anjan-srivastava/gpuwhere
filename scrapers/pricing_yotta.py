"""Yotta Shakti Cloud — official pricing page (INR), calculator JSON as cross-check.

Primary: https://shakticloud.ai/pricing/ . Every price cell carries all term
tabs as `data-price1..N` attributes:
  * AI Workspace VM, On Demand ........ ₹ per VM-hour (true hourly rate)
  * AI Workspace VM, Dedicated ........ ₹ per VM-month for 1 / 3 / 6 / 12 months
  * Bare Metal ........................ ₹ per GPU-hour for monthly / 6 mo / 1-5 years

The calculator rate cards (accountframe.yotta.com …/pricing/*.json) are kept
only as a cross-check: their `sales_price` disagrees with the page and repeats
one value across B200 and B300, so they are not used for prices.
"""
from __future__ import annotations

import html as htmlmod
import json
import re

from pricing_common import Context, FetchError, Package, Price, ScrapeResult, accel, num

PROVIDER = "yotta-shakti"
PAGE = "https://shakticloud.ai/pricing/"
CALC_VM = "https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-vm-cal.prod.json"
CALC_BM = "https://accountframe.yotta.com/shakti-cloud/assets/pricing/shakti-cloud-baremetal-calc.prod.json"
REGION = "IN"
MODELS = [(r"H100", "h100-sxm5"), (r"L40S", "l40s-pcie"), (r"B200", "b200-sxm"), (r"B300", "b300-sxm")]
VM_DEDICATED_TERMS = [1, 3, 6, 12]               # data-price1..4, ₹/VM-month
BM_TERMS = [1, 6, 12, 24, 36, 48, 60]            # data-price1..7, ₹/GPU-hour


def _clean(s: str) -> str:
    return htmlmod.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s))).strip()


def _rows(h: str):
    """Yield (first-cell text, all cell texts, {term index: price text}) for priced rows."""
    for tr in re.findall(r"(?is)<tr[^>]*>(.*?)</tr>", h):
        tds = re.findall(r"(?is)<td([^>]*)>(.*?)</td>", tr)
        if not tds:
            continue
        prices = {}
        for attrs, _ in tds:
            for i, v in re.findall(r'data-price(\d+)="([^"]*)"', attrs):
                if re.search(r"\d", v):
                    prices[int(i)] = v
        if prices:
            yield _clean(tds[0][1]), [_clean(b) for _, b in tds], prices


def _variant(text: str) -> str | None:
    return next((v for pat, v in MODELS if re.search(pat, text)), None)


def _calc_check(ctx: Context) -> dict[str, float]:
    """Calculator sales_price (₹/month) by option name, for conflict notes only."""
    out = {}
    for url in (CALC_VM, CALC_BM):
        try:
            doc = json.loads(ctx.get(PROVIDER, url))
        except (FetchError, ValueError):
            continue
        for cat in doc.get("calc_type", []):
            for mp in cat["main_products"]:
                for comp in mp["component"]:
                    for o in comp.get("options", []):
                        mrc = next((p for p in o["price"] if p["type"] == "MRC"), None)
                        if mrc:
                            out[o["name"]] = mrc["sales_price"]
    return out


def scrape(ctx: Context) -> ScrapeResult:
    res = ScrapeResult()
    h = ctx.get(PROVIDER, PAGE)
    calc = _calc_check(ctx)
    on_demand: dict[tuple, dict] = {}
    dedicated: dict[tuple, dict] = {}

    for name, cells, prices in _rows(h):
        m = re.match(r"VM\s*[–-]\s*(\d+)\s*x\s*(H100|L40S)\s+(Dedicated|On Demand)", name)
        if m:
            n, gpu, kind = int(m.group(1)), m.group(2), m.group(3)
            desc = " ".join(cells)
            row = {"prices": prices, "desc": desc, "name": name}
            (on_demand if kind == "On Demand" else dedicated)[(gpu, n)] = row
            continue
        m = re.match(r"(\d+)\s*x\s*(?:HGX\s*)?(H100|L40S|B200|B300)", name)
        if m and len(cells) >= 6 and "SLURM" not in name:
            n, gpu = int(m.group(1)), m.group(2)
            terms = {t: num(prices[i + 1]) for i, t in enumerate(BM_TERMS) if (i + 1) in prices}
            vcpus = int(num(cells[1])) if re.search(r"\d", cells[1]) else None
            ram = re.search(r"([\d.]+)\s*(TB|GB)", cells[2])
            ram_gb = float(ram.group(1)) * (1024 if ram.group(2) == "TB" else 1) if ram else None
            disk = re.search(r"([\d.]+)\s*TB", cells[3])
            notes = ["Bare metal. Price is ₹ per GPU-hour by term; no hourly on-demand bare metal. "
                     "Ingress/egress and BlueField-3 DPU included; InfiniBand charged separately."]
            on = Price(terms[1], "INR", per="gpu") if 1 in terms else None
            committed = {t: Price(p, "INR", per="gpu") for t, p in terms.items() if t != 1}
            if on is not None:
                notes.append("on_demand is the monthly-term rate (shortest term offered).")
            cname = next((k for k in calc if gpu in k and "Bare Metal" in k), None)
            if cname and on is not None:
                calc_gpu_hr = calc[cname] / 730 / n
                if abs(calc_gpu_hr - on.amount) > 0.02 * on.amount:
                    notes.append(f"Calculator JSON sales_price implies ₹{calc_gpu_hr:.0f}/GPU-hr; page lists "
                                 f"₹{on.amount:g} (page used).")
            res.packages.append(Package(
                provider=PROVIDER, region=REGION, accel=accel(_variant(gpu)), gpus=n, on_demand=on,
                committed=committed, flavour=name, variant="bare-metal", vcpus=vcpus, ram_gb=ram_gb,
                billing="monthly" if on is not None else None,
                disk_gb=float(disk.group(1)) * 1000 if disk else None, disk_type="data" if disk else None,
                sources=[(PAGE, "page")], confidence="medium", notes=notes,
                price_note=None if on else "Bare metal offered on 1–5 year terms only; no monthly or hourly rate. "
                + ", ".join(f"{t // 12}-year ₹{p.amount:g}/GPU-hr" for t, p in sorted(committed.items())) + ".",
            ))

    for (gpu, n) in sorted(set(on_demand) | set(dedicated)):
        od, dd = on_demand.get((gpu, n)), dedicated.get((gpu, n))
        src = od or dd
        vcpu = re.search(r"vCPU\s*:\s*(\d+)", src["desc"])
        ram = re.search(r"RAM\s*:\s*(\d+)\s*GB", src["desc"])
        notes = []
        committed = {}
        if dd:
            for i, t in enumerate(VM_DEDICATED_TERMS):
                if (i + 1) in dd["prices"]:
                    committed[t] = Price(num(dd["prices"][i + 1]), "INR", unit="month")
            d_disk = re.search(r"Root Disk\s*:\s*(\d+)\s*GB", dd["desc"])
            notes.append("Committed terms are the Dedicated VM monthly prices"
                         + (f" (include {d_disk.group(1)} GB root disk)." if d_disk else "."))
            calc_name = f"VM - {n} x {gpu} Dedicated"
            if calc_name in calc and 1 in committed and abs(calc[calc_name] - committed[1].amount) > 0.02 * committed[1].amount:
                notes.append(f"Calculator JSON lists ₹{calc[calc_name]:,}/month for the 1-month term; page lists "
                             f"₹{committed[1].amount:,.0f} (page used).")
        disk = re.search(r"Root Disk\s*:\s*(\d+)\s*GB", (od or dd)["desc"])
        res.packages.append(Package(
            provider=PROVIDER, region=REGION, accel=accel(_variant(gpu)), gpus=n,
            on_demand=Price(num(od["prices"][1]), "INR") if od else None, committed=committed,
            flavour=(od or dd)["name"], vcpus=int(vcpu.group(1)) if vcpu else None,
            ram_gb=float(ram.group(1)) if ram else None, disk_gb=float(disk.group(1)) if disk else None,
            disk_type="root" if disk else None, sources=[(PAGE, "page")], confidence="medium",
            notes=["On-demand is the published hourly VM rate. Unlimited ingress/egress."] + notes,
            price_note=None if od else "Dedicated monthly terms only; no on-demand hourly rate.",
        ))
    if not res.packages:
        res.warnings.append("no priced rows parsed from shakticloud.ai/pricing")
    return res
