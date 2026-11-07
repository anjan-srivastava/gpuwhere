"""European GPU clouds with public pricing pages (USD): Nebius, Verda, Hyperstack.

All three are outside India (burst options without India data residency).
Only exact published numbers are taken: "from $X" ranges are skipped.

  * Nebius   https://nebius.com/prices        per GPU-hour on-demand, vCPU/RAM per GPU;
             https://api.nebius.cloud/billing/v1alpha1/spot-price  live preemptible prices (no auth)
  * Verda    https://verda.com/pricing        per instance (1x…) on-demand and spot
  * Hyperstack https://www.hyperstack.cloud/gpu-pricing   per GPU-hour on-demand
"""
from __future__ import annotations

import json
import re

from pricing_common import Context, Package, Price, ScrapeResult, accel, html_to_text, num

NOTE = "Outside India: no India data residency; consider only for burst/non-regulated workloads."


def _row_iter(text: str, label_re: str, ncols: int):
    """Yield (label, [cells…]) for rows laid out as label|c1|c2… one per line."""
    lines = [l.strip() for l in text.splitlines()]
    for i, l in enumerate(lines):
        m = re.fullmatch(label_re, l)
        if m:
            yield m, lines[i + 1:i + 1 + ncols]


class Nebius:
    PROVIDER, PAGE, REGION = "nebius", "https://nebius.com/prices", "EU-FI"
    MODELS = {"NVIDIA HGX B300": "b300-sxm", "NVIDIA HGX B200": "b200-sxm", "NVIDIA HGX H200": "h200-sxm",
              "NVIDIA HGX H100": "h100-sxm5", "NVIDIA RTX PRO 6000": "rtx-pro-6000-blackwell"}
    # Preemptible (spot) prices are dynamic and published only through Nebius' own API, not on
    # the price page: GET https://api.nebius.cloud/billing/v1alpha1/spot-price (no auth).
    # See docs.nebius.com/signup-billing/spot-prices. One item per GPU platform × region.
    SPOT_API = "https://api.nebius.cloud/billing/v1alpha1/spot-price?pageSize=100"
    SPOT_REGIONS = {"eu-north1": "EU-FI"}          # only Finland is catalogued today
    SPOT_PLATFORMS = {"gpu-h100-sxm": "h100-sxm5", "gpu-h200-sxm": "h200-sxm",
                      "gpu-b200-sxm": "b200-sxm", "gpu-b300-sxm": "b300-sxm",
                      "gpu-rtx6000": "rtx-pro-6000-blackwell"}

    @classmethod
    def _spot(cls, ctx: Context) -> tuple[dict, str | None]:
        """{(region, variant): Price} from the official spot-price API, plus its snapshot time."""
        out: dict[tuple[str, str], Price] = {}
        try:
            doc = json.loads(ctx.get(cls.PROVIDER, cls.SPOT_API))
        except Exception as e:  # a price page scrape must not fail because spot is unavailable
            return out, f"spot API unavailable: {e}"
        for it in doc.get("items") or []:
            region = cls.SPOT_REGIONS.get(it.get("region"))
            variant = cls.SPOT_PLATFORMS.get(((it.get("computeInstance") or {}).get("platform") or ""))
            price = (it.get("price") or {})
            if not region or not variant or (price.get("unitTitle") or "").lower() != "gpu hour":
                continue
            try:
                out[(region, variant)] = Price(float(price["value"]), (price.get("currency") or "usd").upper(), per="gpu")
            except (KeyError, TypeError, ValueError):
                continue
        return out, doc.get("snapshotTime")

    @classmethod
    def scrape(cls, ctx: Context) -> ScrapeResult:
        res = ScrapeResult()
        text = html_to_text(ctx.get(cls.PROVIDER, cls.PAGE))
        spot, snapshot = cls._spot(ctx)
        for m, cells in _row_iter(text, r"(NVIDIA [A-Za-z0-9 ]+?)", 4):
            name = m.group(1)
            if name not in cls.MODELS or len(cells) < 4:
                if name.startswith("NVIDIA L40S"):
                    res.unpriced.append(f"{name}: on-demand published only as a 'from' range")
                continue
            vcpu, ram, _pre, od = cells
            if not od.startswith("$"):
                res.unpriced.append(f"{name}: {od}")
                continue
            variant = cls.MODELS[name]
            sp = spot.get((cls.REGION, variant))
            notes = ["Per GPU-hour on-demand; vCPU/RAM are per GPU. Nebius runs EU (Finland, France) and US regions "
                     "and publishes one price list. " + NOTE]
            if sp is not None:
                notes.append(f"Spot {sp.amount:.2f} USD/GPU-hr from Nebius' public spot-price API"
                             f" (snapshot {snapshot}); preemptible and dynamic — the price can change as often "
                             f"as every 15 minutes, so treat this as an observation, not a rate card.")
            else:
                notes.append("No spot price for this platform in this region at the last snapshot; spot prices are "
                             "dynamic and are read from the official spot-price API.")
            res.packages.append(Package(
                provider=cls.PROVIDER, region=cls.REGION, accel=accel(variant), gpus=1,
                on_demand=Price(num(od), "USD", per="gpu"), spot=sp, flavour=name,
                vcpus=int(num(vcpu)) if re.fullmatch(r"\d+", vcpu) else None,
                ram_gb=num(ram) if re.fullmatch(r"\d+", ram) else None,
                sources=[(cls.PAGE, "page")] + ([(cls.SPOT_API, "api")] if sp is not None else []),
                confidence="high" if sp is not None else "medium",
                notes=notes,
            ))
        return res


class Verda:
    PROVIDER, PAGE, REGION = "verda", "https://verda.com/pricing", "EU-FI"
    MODELS = [("GB300", None), ("B300", "b300-sxm"), ("B200", "b200-sxm"), ("H200", "h200-sxm"),
              ("H100 SXM5", "h100-sxm5"), ("A100 SXM4 80GB", "a100-sxm4-80gb"), ("A100 SXM4 40GB", "a100-sxm4-40gb"),
              ("V100", None), ("RTX PRO 6000", "rtx-pro-6000-blackwell"), ("L40S", "l40s-pcie"),
              ("RTX 6000 Ada", "rtx-6000-ada-pcie"), ("RTX A6000", "rtx-a6000-pcie")]

    @classmethod
    def scrape(cls, ctx: Context) -> ScrapeResult:
        res = ScrapeResult()
        text = html_to_text(ctx.get(cls.PROVIDER, cls.PAGE))
        # Only the GPU instance table: later sections (confidential computing, instant clusters,
        # serverless containers) are different products with different prices.
        start = re.search(r"^\dx (?:Tesla )?[A-Za-z0-9 ]+? \d+GB$", text, re.M)
        cut = text.find("Confidential computing", start.start() if start else 0)
        if cut == -1:
            res.warnings.append("section marker 'Confidential computing' not found; instance table boundary unknown")
        else:
            text = text[:cut]
        seen = set()
        for m, cells in _row_iter(text, r"(\d)x ((?:Tesla )?[A-Za-z0-9 ]+?) (\d+)GB", 5):
            n, model, vram = int(m.group(1)), m.group(2), int(m.group(3))
            if " CC " in f" {model} " or len(cells) < 5:
                continue  # confidential-computing variants listed separately
            variant = next((v for k, v in cls.MODELS if k in f"{model} {vram}GB"), "missing")
            cpus, ram, _vr, od, spot = cells
            key = (model, n, cpus, ram)
            if key in seen or not od.startswith("$"):
                continue
            seen.add(key)
            if variant in (None, "missing") or n not in (1, 2, 4, 8):
                res.unpriced.append(f"{n}x {model} {vram}GB: no accelerator spec or unsupported shape")
                continue
            res.packages.append(Package(
                provider=cls.PROVIDER, region=cls.REGION, accel=accel(variant), gpus=n,
                on_demand=Price(num(od), "USD"), spot=Price(num(spot), "USD") if spot.startswith("$") else None,
                flavour=f"{n}x {model} {vram}GB ({cpus} CPU, {ram})",
                variant=f"{int(num(cpus))}cpu-{int(num(ram))}gb",
                vcpus=int(num(cpus)), ram_gb=num(ram), vram_gb=vram,
                sources=[(cls.PAGE, "page")], confidence="medium",
                notes=["Verda (formerly DataCrunch), Finland/Iceland data centres. Price per instance-hour; spot is "
                       "interruptible. " + NOTE],
            ))
        return res


class Hyperstack:
    PROVIDER, PAGE, REGION = "hyperstack", "https://www.hyperstack.cloud/gpu-pricing", "EU-NO"
    MODELS = {"NVIDIA H200 SXM": "h200-sxm", "NVIDIA H100 SXM": "h100-sxm5", "NVIDIA H100 NVLink": "h100-pcie",
              "NVIDIA H100": "h100-pcie", "NVIDIA RTX Pro 6000 SE": "rtx-pro-6000-blackwell",
              "NVIDIA A100 SXM": "a100-sxm4-80gb", "NVIDIA A100 NVLink": "a100-pcie-80gb", "NVIDIA A100": "a100-pcie-80gb",
              "NVIDIA A6000": "rtx-a6000-pcie", "NVIDIA A4000": "rtx-a4000-pcie", "NVIDIA B200": "b200-sxm"}

    @classmethod
    def scrape(cls, ctx: Context) -> ScrapeResult:
        res = ScrapeResult()
        text = html_to_text(ctx.get(cls.PROVIDER, cls.PAGE))
        seen = set()
        for m, cells in _row_iter(text, r"(NVIDIA [A-Za-z0-9 ]+?)", 4):
            name = m.group(1)
            if name not in cls.MODELS or len(cells) < 4 or name in seen:
                continue
            vram, cpu, ram, price = cells
            if not price.startswith("$") or not re.fullmatch(r"\d+", vram):
                continue
            seen.add(name)
            res.packages.append(Package(
                provider=cls.PROVIDER, region=cls.REGION, accel=accel(cls.MODELS[name]), gpus=1,
                on_demand=Price(num(price), "USD", per="gpu"), flavour=name,
                variant=re.sub(r"[^a-z0-9]+", "-", name.lower().replace("nvidia ", "")).strip("-"),
                vcpus=int(num(cpu)) if re.fullmatch(r"\d+", cpu) else None,
                ram_gb=num(ram) if re.fullmatch(r"\d+", ram) else None, vram_gb=float(vram),
                sources=[(cls.PAGE, "page")], confidence="medium",
                notes=["Per GPU-hour on-demand; vCPU and RAM are the published maximum per GPU. Hyperstack (NexGen Cloud) "
                       "runs data centres in Norway, Canada and the US with one price list. "
                       + ("Listed as 'NVLink' (PCIe cards bridged with NVLink). " if "NVLink" in name else "") + NOTE],
            ))
        return res
