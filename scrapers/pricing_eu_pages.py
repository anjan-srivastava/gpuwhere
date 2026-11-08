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
    """Nebius — public price list × console platform/region matrix.

    The price page publishes one per-GPU-hour rate per platform (no region, no
    shape). The capacity dashboard shows which regions carry each platform and
    that every GPU platform is sold as a 1-GPU or 8-GPU preset, so that matrix is
    a dated observation (2026-11-09), not a scrape. Region codes are the
    provider's own, uppercased: EU-NORTH1 is the Finnish region, EU-FI in older
    catalogue rows. Spot comes from the public spot-price API per platform × region.
    """
    PROVIDER, PAGE = "nebius", "https://nebius.com/prices"
    # page name -> (accelerator variant, {region: (platform id, shapes)})
    PLATFORMS = {
        "NVIDIA HGX B300": ("b300-sxm", {
            "EU-WEST2": ("gpu-b300-sxm", (1, 8)),
            "UK-SOUTH1": ("gpu-b300-sxm", (1, 8)),
            "US-NORTH1": ("gpu-b300-sxm", (1, 8)),
        }),
        "NVIDIA HGX B200": ("b200-sxm", {
            "US-CENTRAL1": ("gpu-b200-sxm", (1, 8)),
            "ME-WEST1": ("gpu-b200-sxm-a", (1, 8)),
        }),
        "NVIDIA HGX H200": ("h200-sxm", {
            "EU-NORTH1": ("gpu-h200-sxm", (1, 8)),
            "EU-WEST1": ("gpu-h200-sxm", (1, 8)),
            "US-CENTRAL1": ("gpu-h200-sxm", (1, 8)),
        }),
        "NVIDIA HGX H100": ("h100-sxm5", {"EU-NORTH1": ("gpu-h100-sxm", (1, 8))}),
        "NVIDIA RTX PRO 6000": ("rtx-pro-6000-blackwell", {
            "US-CENTRAL1": ("gpu-rtx6000", (1, 8)),
            "EU-SOUTH1": ("gpu-rtx6000-a", (1, 8)),
            "UK-SOUTH2": ("gpu-rtx6000-a", (1, 8)),
        }),
    }
    # Preemptible (spot) prices are dynamic and published only through Nebius' own API.
    # GET https://api.nebius.cloud/billing/v1alpha1/spot-price (no auth), keyed by region.
    SPOT_API = "https://api.nebius.cloud/billing/v1alpha1/spot-price?pageSize=100"

    @classmethod
    def _spot(cls, ctx: Context) -> tuple[dict, str | None]:
        """{(region, platform): Price} from the official spot-price API, plus its snapshot time."""
        out: dict[tuple[str, str], Price] = {}
        try:
            doc = json.loads(ctx.get(cls.PROVIDER, cls.SPOT_API))
        except Exception as e:  # a price page scrape must not fail because spot is unavailable
            return out, f"spot API unavailable: {e}"
        for it in doc.get("items") or []:
            region = (it.get("region") or "").upper()
            platform = (it.get("computeInstance") or {}).get("platform") or ""
            price = (it.get("price") or {})
            if not region or not platform or (price.get("unitTitle") or "").lower() != "gpu hour":
                continue
            try:
                out[(region, platform)] = Price(float(price["value"]),
                                                (price.get("currency") or "usd").upper(), per="gpu")
            except (KeyError, TypeError, ValueError):
                continue
        return out, doc.get("snapshotTime")

    @classmethod
    def scrape(cls, ctx: Context) -> ScrapeResult:
        res = ScrapeResult()
        text = html_to_text(ctx.get(cls.PROVIDER, cls.PAGE))
        spot, snapshot = cls._spot(ctx)
        prices: dict[str, tuple[float, str, str]] = {}
        for m, cells in _row_iter(text, r"(NVIDIA [A-Za-z0-9 ]+?)", 4):
            name = m.group(1)
            if name not in cls.PLATFORMS or len(cells) < 4 or name in prices:
                if name.startswith("NVIDIA L40S"):
                    res.unpriced.append(f"{name}: on-demand published only as a 'from' range")
                continue
            vcpu, ram, _pre, od = cells
            if not od.startswith("$"):
                res.unpriced.append(f"{name}: {od}")
                continue
            prices[name] = (num(od), vcpu, ram)

        for name, (variant, regions) in cls.PLATFORMS.items():
            if name not in prices:
                res.warnings.append(f"{name}: no row on the price page")
                continue
            per_gpu, vcpu_s, ram_s = prices[name]
            vcpu1 = int(num(vcpu_s)) if re.fullmatch(r"\d+", vcpu_s) else None
            ram1 = num(ram_s) if re.fullmatch(r"\d+", ram_s) else None
            for region, (platform, shapes) in regions.items():
                sp = spot.get((region, platform))
                for n in shapes:
                    notes = ["Per GPU-hour on-demand; vCPU/RAM are per GPU. Region and shape list from the "
                             "signed-in capacity dashboard (2026-11-09); the price list is per platform. " + NOTE]
                    if sp is not None:
                        notes.append(f"Spot {sp.amount:.2f} USD/GPU-hr from Nebius' public spot-price API "
                                     f"(snapshot {snapshot}); preemptible and dynamic — an observation, not a "
                                     "rate card.")
                    else:
                        notes.append("No spot price for this platform in this region at the last snapshot; spot "
                                     "prices are dynamic and read from the official spot-price API.")
                    res.packages.append(Package(
                        provider=cls.PROVIDER, region=region, accel=accel(variant), gpus=n,
                        on_demand=Price(per_gpu * n, "USD", per="gpu"),
                        spot=(Price(sp.amount * n, "USD", per="gpu") if sp is not None else None),
                        flavour=f"{name} {n}x",
                        variant=re.sub(r"[^a-z0-9]+", "-", f"{name} {n}x".lower().replace("nvidia ", "")).strip("-"),
                        vcpus=(vcpu1 * n) if vcpu1 else None, ram_gb=(ram1 * n) if ram1 else None,
                        sources=[(cls.PAGE, "page")] + ([(cls.SPOT_API, "api")] if sp is not None else []),
                        confidence="high" if sp is not None else "medium",
                        notes=notes,
                    ))
        return res

class Verda:
    """Verda (formerly DataCrunch) — public instance-type catalogue.

    Source: https://api.verda.com/v1/instance-types (no auth, JSON). It lists every
    shape 1x/2x/4x/8x with an instance-hour price, spot price, vCPU and RAM, which
    the marketing page does not: the page only shows 1x, so we were missing 8-GPU
    H200/H100 and understating the fleet. Prices are per instance; pricing_common
    divides by the GPU count. Confidential-computing (" CC ") variants are a
    separate product and are skipped.
    """
    PROVIDER, REGION = "verda", "EU-FI"
    API = "https://api.verda.com/v1/instance-types"
    MODELS = {
        "A100 SXM4 40GB": "a100-sxm4-40gb",
        "A100 SXM4 80GB": "a100-sxm4-80gb",
        "B200 SXM6 180GB": "b200-sxm",
        "B300 SXM6 268GB": "b300-sxm",
        "H100 SXM5 80GB": "h100-sxm5",
        "H200 SXM5 141GB": "h200-sxm",
        "L40S 48GB": "l40s-pcie",
        "RTX 6000 Ada 48GB": "rtx-6000-ada-pcie",
        "RTX A6000 48GB": "rtx-a6000-pcie",
        "RTX PRO 6000 96GB": "rtx-pro-6000-blackwell",
    }

    @classmethod
    def scrape(cls, ctx: Context) -> ScrapeResult:
        res = ScrapeResult()
        rows = json.loads(ctx.get(cls.PROVIDER, cls.API))
        seen = set()
        for t in rows:
            gpu = t.get("gpu") or {}
            n = gpu.get("number_of_gpus") or 0
            name = (t.get("name") or "").strip()
            if not n or " CC " in f" {name} ":
                continue                      # CC = confidential computing, a different product
            if n not in (1, 2, 4, 8):
                res.unpriced.append(f"{n}x {name}: unsupported shape")
                continue
            variant = cls.MODELS.get(name)
            if variant is None:
                res.unpriced.append(f"{n}x {name}: no accelerator file for this SKU")
                continue
            key = (name, n, t.get("instance_type"))
            if key in seen:
                continue
            seen.add(key)
            od = t.get("price_per_hour")
            spot = t.get("spot_price")
            if od in (None, "", "0"):
                res.unpriced.append(f"{n}x {name}: no published instance price")
                continue
            vcpus = (t.get("cpu") or {}).get("number_of_cores")
            ram = (t.get("memory") or {}).get("size_in_gigabytes")
            vram = (t.get("gpu_memory") or {}).get("size_in_gigabytes")
            notes = ["Verda bills per instance-hour (10-minute granularity); the per-GPU rate is the "
                     "instance price divided by the GPU count. Spot is interruptible."]
            if t.get("deploy_warning"):
                notes.append(f"Provider warning: {t['deploy_warning']}")
            res.packages.append(Package(
                provider=cls.PROVIDER, region=cls.REGION, accel=accel(variant), gpus=n,
                on_demand=Price(float(od), "USD"),
                spot=Price(float(spot), "USD") if spot not in (None, "", "0") else None,
                flavour=f"{n}x {name} ({t.get('instance_type')})",
                variant=(f"{int(vcpus)}cpu-{int(ram)}gb-{int(vram)}gb" if vcpus and ram and vram else slug(name)),
                vcpus=int(vcpus) if vcpus else None, ram_gb=float(ram) if ram else None,
                vram_gb=float(vram) if vram else None,
                sources=[(cls.API, "api")], confidence="high",
                notes=notes + [NOTE],
            ))
        return res



class Hyperstack:
    """Hyperstack (NexGen Cloud) — global price list × console region/shape matrix.

    The public page publishes one per-GPU-hour rate per product (no region, no
    shape). The signed-in console shows which regions carry which product and
    which shapes each is sold as, so the region/shape matrix below is a dated
    observation, not a scrape; the prices are live. Verified 2026-11-09 against
    /api/core/flavors and the deploy page:

        NORWAY-1   RTX-A4000 only (no Hopper at all)
        CANADA-1   A100 PCIe / PCIe-NVLink, H100 PCIe / PCIe-NVLink, H200 SXM5,
                   B200 SXM, B300 SXM, RTX A6000, RTX PRO 6000 SE
        CANADA-2   H100 SXM5 (8x only)
        US-1       A100 SXM4, H100 SXM5 (8x only)

    Re-check this table on the next console audit. L40 is sold but has no
    accelerator file (L40 is not L40S), so it stays out.
    """
    PROVIDER, PAGE = "hyperstack", "https://www.hyperstack.cloud/gpu-pricing"
    PRODUCTS = {
        "NVIDIA A4000": ("rtx-a4000-pcie", {"EU-NO": (1, 2, 4, 8)}),
        "NVIDIA A6000": ("rtx-a6000-pcie", {"CA-1": (1, 2, 4, 8)}),
        "NVIDIA RTX Pro 6000 SE": ("rtx-pro-6000-blackwell", {"CA-1": (1, 2, 4, 8)}),
        "NVIDIA A100": ("a100-pcie-80gb", {"CA-1": (1, 2, 4, 8)}),
        "NVIDIA A100 NVLink": ("a100-pcie-80gb", {"CA-1": (8,)}),
        "NVIDIA A100 SXM": ("a100-sxm4-80gb", {"US-1": (8,)}),
        "NVIDIA H100": ("h100-pcie", {"CA-1": (1, 2, 4, 8)}),
        "NVIDIA H100 NVLink": ("h100-pcie", {"CA-1": (8,)}),
        "NVIDIA H100 SXM": ("h100-sxm5", {"CA-2": (8,), "US-1": (8,)}),
        "NVIDIA H200 SXM": ("h200-sxm", {"CA-1": (8,)}),
        "NVIDIA B200": ("b200-sxm", {"CA-1": (8,)}),
    }
    # On the console deploy page but not on the public price list.
    CONSOLE_ONLY = {"B300-SXM": ("b300-sxm", {"CA-1": (8,)}, 7.40)}

    @classmethod
    def scrape(cls, ctx: Context) -> ScrapeResult:
        res = ScrapeResult()
        text = html_to_text(ctx.get(cls.PROVIDER, cls.PAGE))
        prices: dict[str, tuple[float, str]] = {}
        for m, cells in _row_iter(text, r"(NVIDIA [A-Za-z0-9 ]+?)", 4):
            name = m.group(1)
            if name not in cls.PRODUCTS or len(cells) < 4 or name in prices:
                continue
            vram, _cpu, _ram, price = cells
            if not price.startswith("$") or not re.fullmatch(r"\d+", vram):
                continue
            prices[name] = (num(price), vram)

        for name, (variant, regions) in cls.PRODUCTS.items():
            if name not in prices:
                res.warnings.append(f"{name}: no row on the price page")
                continue
            per_gpu, vram = prices[name]
            for region, shapes in regions.items():
                for n in shapes:
                    res.packages.append(Package(
                        provider=cls.PROVIDER, region=region, accel=accel(variant), gpus=n,
                        on_demand=Price(per_gpu * n, "USD"), flavour=f"{name} {n}x",
                        variant=re.sub(r"[^a-z0-9]+", "-", f"{name} {n}x".lower().replace("nvidia ", "")).strip("-"),
                        vram_gb=float(vram), sources=[(cls.PAGE, "page")], confidence="medium",
                        notes=[f"Billed per GPU-hour (${per_gpu:g}); the {n}x package is {n} × that rate. "
                               "Region and shapes from the signed-in console (2026-11-09); the price list is global. "
                               + ("Listed as 'NVLink' (PCIe cards bridged with NVLink). " if "NVLink" in name else "")
                               + NOTE],
                    ))
        for console_name, (variant, regions, per_gpu) in cls.CONSOLE_ONLY.items():
            for region, shapes in regions.items():
                for n in shapes:
                    res.packages.append(Package(
                        provider=cls.PROVIDER, region=region, accel=accel(variant), gpus=n,
                        on_demand=Price(per_gpu * n, "USD"), flavour=f"{console_name} {n}x",
                        variant=re.sub(r"[^a-z0-9]+", "-", f"{console_name} {n}x".lower()).strip("-"),
                        sources=[(cls.PAGE, "page")], confidence="low",
                        notes=[f"Not on the public price list: ${per_gpu:g}/GPU-hour is read from the signed-in "
                               "console deploy page (2026-11-09) and needs re-checking. " + NOTE],
                    ))
        return res
