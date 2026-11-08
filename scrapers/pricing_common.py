"""Shared plumbing for the per-provider pricing scrapers.

Each provider module exposes:

    PROVIDER = "<provider-id>"
    def scrape(ctx: Context) -> ScrapeResult

and returns host packages (`Package`) exactly as the source publishes them.
This module turns packages into SKU files, merges them into the existing
catalogue and produces a review report. It never invents values: a field the
source does not publish stays `None`, and the writer keeps whatever the file
already had for that field.
"""
from __future__ import annotations

import dataclasses
import datetime as dt
import hashlib
import html as htmlmod
import json
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
from pathlib import Path
from typing import Any

HOURS_PER_MONTH = 730
SHAPES = {1: "1x", 2: "2x", 4: "4x", 8: "8x"}
USER_AGENT = "gpu-catalog-pricing/0.2 (provider price catalogue; respects robots.txt)"
ECB_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"


# ---------------------------------------------------------------------------
# Accelerator mapping. One place maps provider naming to the accelerator SKU
# (`gpu_variant`) that `data/gpus/<supplier>/<family>.json` describes.
# `assumed` marks form factors the provider does not publish (AGENTS.md: assume
# SXM where unpublished, and say so).
# ---------------------------------------------------------------------------
@dataclasses.dataclass(frozen=True)
class Accel:
    gpu: str            # family name used in SKU `gpu` and in the SKU path
    variant: str        # accelerator SKU id (`gpu_variant`)
    form_factor: str    # sxm | nvl | pcie | generic
    vram_gb: float
    supplier: str = "nvidia"


ACCEL: dict[str, Accel] = {
    "h100-sxm5": Accel("H100", "h100-sxm5", "sxm", 80),
    "h100-nvl": Accel("H100", "h100-nvl", "nvl", 94),
    "h100-pcie": Accel("H100", "h100-pcie", "pcie", 80),
    "h200-sxm": Accel("H200", "h200-sxm", "sxm", 141),
    "h200-nvl": Accel("H200", "h200-nvl", "nvl", 141),
    "b200-sxm": Accel("B200", "b200-sxm", "sxm", 192),
    "b300-sxm": Accel("B300", "b300-sxm", "sxm", 288),
    "a100-sxm4-80gb": Accel("A100", "a100-sxm4-80gb", "sxm", 80),
    "a100-sxm4-40gb": Accel("A100", "a100-sxm4-40gb", "sxm", 40),
    "a100-pcie-80gb": Accel("A100", "a100-pcie-80gb", "pcie", 80),
    "l40s-pcie": Accel("L40S", "l40s-pcie", "pcie", 48),
    "l4-pcie": Accel("L4", "l4-pcie", "pcie", 24),
    "a40-pcie": Accel("A40", "a40-pcie", "pcie", 48),
    "a30-pcie": Accel("A30", "a30-pcie", "pcie", 24),
    "a2-pcie": Accel("A2", "a2-pcie", "pcie", 16),
    "t4-pcie": Accel("T4", "t4-pcie", "pcie", 16),
    "v100-sxm2-32gb": Accel("V100", "v100-sxm2-32gb", "sxm", 32),
    "rtx-pro-6000-blackwell": Accel("RTX PRO 6000", "rtx-pro-6000-blackwell", "pcie", 96),
    "rtx-pro-4500-blackwell": Accel("RTX PRO 4500", "rtx-pro-4500-blackwell", "pcie", 32),
    "rtx-6000-ada-pcie": Accel("RTX 6000 Ada", "rtx-6000-ada-pcie", "pcie", 48),
    "rtx-a6000-pcie": Accel("RTX A6000", "rtx-a6000-pcie", "pcie", 48),
    "rtx-a5000-pcie": Accel("RTX A5000", "rtx-a5000-pcie", "pcie", 24),
    "rtx-a4000-pcie": Accel("RTX A4000", "rtx-a4000-pcie", "pcie", 16),
    "mi300x-oam": Accel("MI300X", "mi300x-oam", "generic", 192, "amd"),
    "mi325x-oam": Accel("MI325X", "mi325x-oam", "generic", 256, "amd"),
    "gaudi2-oam": Accel("Gaudi 2", "gaudi2-oam", "generic", 96, "intel"),
}


def accel(variant: str) -> Accel:
    return ACCEL[variant]


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------
@dataclasses.dataclass
class Price:
    """A price exactly as published: amount, currency, unit and basis."""
    amount: float
    currency: str            # "USD" | "INR"
    unit: str = "hour"       # "hour" | "month" | "total"
    per: str = "vm"          # "vm" | "gpu"
    months: int | None = None  # only for unit == "total": the term length


@dataclasses.dataclass
class Package:
    provider: str
    region: str
    accel: Accel
    gpus: int
    on_demand: Price | None
    sources: list[tuple[str, str]]          # (url, kind)
    confidence: str
    spot: Price | None = None
    committed: dict[int, Price] = dataclasses.field(default_factory=dict)
    variant: str | None = None               # None → auto ("standard" unless ambiguous)
    flavour: str | None = None               # provider's own plan name
    vcpus: int | None = None
    ram_gb: float | None = None
    disk_gb: float | None = None
    disk_type: str | None = None
    vram_gb: float | None = None             # as published by the provider
    interconnect: dict | None = None
    status: str = "active"
    price_note: str | None = None            # why there is no on-demand price (quote_only)
    # Can the package be ordered through the provider's self-serve path?
    # None = unverified. False = listed but needs sales; excluded from min prices.
    self_serve: bool | None = None
    billing: str | None = None               # "hourly" | "monthly"; None → from on_demand.unit
    notes: list[str] = dataclasses.field(default_factory=list)
    native_extra: dict = dataclasses.field(default_factory=dict)

    @property
    def shape(self) -> str:
        return SHAPES[self.gpus]

    @property
    def pricing_status(self) -> str:
        return "published" if self.on_demand is not None else "quote_only"


@dataclasses.dataclass
class ScrapeResult:
    # Priced packages and quote-only packages (on_demand None + price_note).
    packages: list[Package] = dataclasses.field(default_factory=list)
    # Free-text notes about offerings that cannot be a package at all.
    unpriced: list[str] = dataclasses.field(default_factory=list)
    warnings: list[str] = dataclasses.field(default_factory=list)


# ---------------------------------------------------------------------------
# HTTP, snapshots, text helpers
# ---------------------------------------------------------------------------
class FetchError(RuntimeError):
    pass


class Context:
    def __init__(self, cache_dir: Path, today: str, fx: "Fx | None" = None, offline: bool = False):
        self.cache_dir = cache_dir
        self.today = today
        self.offline = offline
        self._robots: dict[str, urllib.robotparser.RobotFileParser | None] = {}
        self._fx = fx
        self.fetched: list[dict] = []
        self._last_hit: dict[str, float] = {}

    # -- robots.txt -------------------------------------------------------
    def _allowed(self, url: str) -> bool:
        parts = urllib.parse.urlsplit(url)
        base = f"{parts.scheme}://{parts.netloc}"
        if base not in self._robots:
            rp = urllib.robotparser.RobotFileParser()
            try:
                req = urllib.request.Request(base + "/robots.txt", headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(req, timeout=20) as resp:
                    rp.parse(resp.read().decode("utf-8", "ignore").splitlines())
                self._robots[base] = rp
            except Exception:
                self._robots[base] = None  # no robots.txt reachable → allowed
        rp = self._robots[base]
        return True if rp is None else rp.can_fetch(USER_AGENT, url)

    def _snapshot_path(self, provider: str, url: str) -> Path:
        h = hashlib.sha1(url.encode()).hexdigest()[:12]
        tail = re.sub(r"[^A-Za-z0-9._-]+", "_", urllib.parse.urlsplit(url).path.strip("/"))[-60:] or "index"
        return self.cache_dir / provider / self.today / f"{tail}.{h}"

    def get(self, provider: str, url: str, *, binary: bool = False, retries: int = 3) -> bytes | str:
        snap = self._snapshot_path(provider, url)
        if self.offline:
            if not snap.exists():
                raise FetchError(f"offline and no snapshot for {url}")
            data = snap.read_bytes()
            return data if binary else data.decode("utf-8", "ignore")
        if not self._allowed(url):
            raise FetchError(f"robots.txt disallows {url}")
        host = urllib.parse.urlsplit(url).netloc
        wait = self._last_hit.get(host, 0) + 1.0 - time.monotonic()  # ≤1 request/s per host
        if wait > 0:
            time.sleep(wait)
        self._last_hit[host] = time.monotonic()
        delay = 2.0
        for attempt in range(retries):
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    data = resp.read()
                break
            except urllib.error.HTTPError as exc:
                if exc.code == 429 and attempt + 1 < retries:
                    retry_after = exc.headers.get("Retry-After")
                    time.sleep(float(retry_after) if retry_after and retry_after.isdigit() else delay)
                    delay *= 2
                    continue
                if exc.code in (401, 403):
                    # Bot protection or auth wall. Do not try to get around it.
                    raise FetchError(f"HTTP {exc.code} (blocked; not bypassing) for {url}") from exc
                raise FetchError(f"HTTP {exc.code} for {url}") from exc
            except (urllib.error.URLError, ConnectionError, TimeoutError) as exc:
                # Transient network errors (resets, timeouts): back off and retry.
                if attempt + 1 < retries:
                    time.sleep(delay)
                    delay *= 2
                    continue
                raise FetchError(f"{getattr(exc, 'reason', exc)} for {url}") from exc
        snap.parent.mkdir(parents=True, exist_ok=True)
        snap.write_bytes(data)
        self.fetched.append({"provider": provider, "url": url, "bytes": len(data),
                             "sha1": hashlib.sha1(data).hexdigest(), "snapshot": str(snap)})
        return data if binary else data.decode("utf-8", "ignore")

    def run(self, provider: str, label: str, argv: list[str]) -> str:
        """Run an official CLI (e.g. `jl gpus --json`) and snapshot its output."""
        snap = self._snapshot_path(provider, "cli:" + " ".join(argv))
        if self.offline:
            return snap.read_text()
        out = subprocess.check_output(argv, text=True, timeout=120)
        snap.parent.mkdir(parents=True, exist_ok=True)
        snap.write_text(out)
        self.fetched.append({"provider": provider, "url": label, "bytes": len(out),
                             "sha1": hashlib.sha1(out.encode()).hexdigest(), "snapshot": str(snap)})
        return out

    @property
    def fx(self) -> "Fx":
        if self._fx is None:
            self._fx = Fx.from_ecb(self)
        return self._fx


@dataclasses.dataclass
class Fx:
    usd_inr: float
    date: str
    source: str
    eur_usd: float | None = None   # USD per 1 EUR

    @classmethod
    def from_ecb(cls, ctx: Context) -> "Fx":
        xml = ctx.get("_fx", ECB_URL)
        # Fixed-format ECB file; regex avoids depending on a working pyexpat.
        m = re.search(r"time=['\"](\d{4}-\d{2}-\d{2})['\"]", xml)
        date = m.group(1) if m else None
        rates = {c: float(r) for c, r in re.findall(r"currency=['\"]([A-Z]{3})['\"]\s+rate=['\"]([\d.]+)['\"]", xml)}
        if "USD" not in rates or "INR" not in rates:
            raise FetchError("ECB feed missing USD or INR")
        return cls(round(rates["INR"] / rates["USD"], 4), date, ECB_URL, round(rates["USD"], 4))


def html_to_text(h: str) -> str:
    h = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?i)<(br|/p|/div|/tr|/li|/h\d|/td|/th|/dd|/dt|/span)[^>]*>", "\n", h)
    t = htmlmod.unescape(re.sub(r"<[^>]+>", " ", h))
    t = re.sub(r"[ \t\xa0]+", " ", t)
    return "\n".join(line.strip() for line in t.splitlines() if line.strip())


def num(s: str) -> float:
    """Parse '₹ 2,95,200', '$1,865.12', '1,024' → float."""
    s = re.sub(r"[^\d.]", "", s)
    if not s:
        raise ValueError("no number")
    return float(s)


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


# ---------------------------------------------------------------------------
# Normalisation: Package → SKU dict
# ---------------------------------------------------------------------------
def _to_vm_hour(p: Price, gpus: int) -> tuple[float, str]:
    """Return (amount per VM-hour in the price's own currency, derivation note)."""
    amt = p.amount * (gpus if p.per == "gpu" else 1)
    if p.unit == "hour":
        return amt, ""
    if p.unit == "month":
        return amt / HOURS_PER_MONTH, f"monthly/{HOURS_PER_MONTH}h"
    if p.unit == "total":
        return amt / (p.months * HOURS_PER_MONTH), f"term total/({p.months}×{HOURS_PER_MONTH}h)"
    raise ValueError(p.unit)


def _usd(amount: float, currency: str, fx: Fx | None) -> float:
    if currency == "USD":
        return amount
    if currency == "INR":
        assert fx is not None
        return amount / fx.usd_inr
    if currency == "EUR":
        assert fx is not None and fx.eur_usd
        return amount * fx.eur_usd
    raise ValueError(currency)


def _price_block(p: Price, gpus: int, fx: Fx | None) -> tuple[dict, dict]:
    vm_hr_native, how = _to_vm_hour(p, gpus)
    vm_usd = _usd(vm_hr_native, p.currency, fx)
    block = {"usd_per_gpu_hr": round(vm_usd / gpus, 2), "usd_per_vm_hr": round(vm_usd, 2)}
    native: dict[str, Any] = {}
    if p.currency != "USD":
        key = p.currency.lower()
        native[f"{key}_per_vm_hr"] = round(vm_hr_native, 2)
        native[f"{key}_per_gpu_hr"] = round(vm_hr_native / gpus, 2)
        if p.currency == "INR":
            native["fx_usd_inr"] = fx.usd_inr
        elif p.currency == "EUR":
            native["fx_eur_usd"] = fx.eur_usd
        native["fx_date"] = fx.date
    if p.unit != "hour":
        native[f"published_{p.unit}_{p.currency.lower()}"] = p.amount
        native["published_per"] = p.per
        native["derivation"] = how
    return block, native


def _n(x: float | None) -> float | int | None:
    """Store whole numbers as ints (384 not 384.0)."""
    return int(x) if isinstance(x, float) and x.is_integer() else x


def package_to_sku(pkg: Package, variant: str, fx: Fx | None, today: str) -> dict:
    a = pkg.accel
    if pkg.on_demand is None:
        if not pkg.price_note:
            raise ValueError("quote_only package needs a price_note")
        od = {"usd_per_gpu_hr": None, "usd_per_vm_hr": None}
    else:
        od, od_native = _price_block(pkg.on_demand, pkg.gpus, fx)
        if od_native:
            od["native"] = od_native
    pricing: dict[str, Any] = {"on_demand": od}
    if pkg.spot is not None:
        sp, sp_native = _price_block(pkg.spot, pkg.gpus, fx)
        sp["notice_sec"] = None
        if sp_native:
            sp["native"] = sp_native
        pricing["spot"] = sp
    pricing["committed"] = []
    for months in sorted(pkg.committed):
        c, _ = _price_block(pkg.committed[months], pkg.gpus, fx)
        pricing["committed"].append({"term_months": months, **c})

    notes = list(pkg.notes)
    if pkg.on_demand is not None and pkg.on_demand.unit != "hour":
        notes.append(f"No hourly rate published; on_demand is derived from the published "
                     f"{pkg.on_demand.unit}ly price ({_to_vm_hour(pkg.on_demand, pkg.gpus)[1]}) and is not "
                     f"directly comparable with true hourly rates.")
    if pkg.flavour:
        notes.insert(0, f"Provider plan: {pkg.flavour}.")
    if pkg.vram_gb is not None and abs(pkg.vram_gb - a.vram_gb) > 0.5:
        notes.append(f"Provider lists {pkg.vram_gb:g} GB VRAM per GPU; accelerator spec {a.variant} is {a.vram_gb:g} GB.")

    sku_id = f"{pkg.provider}/{pkg.region}/{a.gpu}/{pkg.shape}/{variant}"
    sku: dict[str, Any] = {
        "$schema": "../../../../schema/sku.schema.json",
        "id": sku_id,
        "provider": pkg.provider,
        "region": pkg.region,
        "status": pkg.status,
        "gpu": a.gpu,
        "gpu_variant": a.variant,
        "form_factor": a.form_factor,
        "shape": pkg.shape,
        "gpus_per_vm": pkg.gpus,
        "variant": variant,
        "vram_gb_per_gpu": _n(pkg.vram_gb if pkg.vram_gb is not None else a.vram_gb),
        "vcpus": pkg.vcpus,
        "ram_gb": _n(pkg.ram_gb),
        "disk_gb": _n(pkg.disk_gb),
        "disk_type": pkg.disk_type,
        "pricing": pricing,
        # hourly = can be rented and billed by the hour; monthly = shortest commitment is a month
        "billing_model": None if pkg.on_demand is None else (
            pkg.billing or ("monthly" if pkg.on_demand.unit in ("month", "total") else "hourly")),
        "pricing_status": pkg.pricing_status,
        # India data residency: the package runs in an Indian region (codes "IN" / "IN-*").
        "residency": "india" if pkg.region == "IN" or pkg.region.startswith("IN-") or pkg.region.startswith("IN") and pkg.region[2:3].isdigit() else "outside-india",
        "price_note": pkg.price_note,
        "self_serve": pkg.self_serve,
        "sources": [{"url": u, "kind": k, "fetched_at": today} for u, k in pkg.sources],
        "confidence": pkg.confidence,
        "verified_at": today,
        "notes": " ".join(notes) if notes else None,
    }
    if pkg.interconnect is not None:
        sku["interconnect"] = pkg.interconnect
    if pkg.native_extra and pkg.on_demand is not None:
        sku["pricing"]["on_demand"].setdefault("native", {}).update(pkg.native_extra)
    return sku


SALES_ONLY_NOTE = (
    "No self-serve GPU ordering: this provider sells through sales, so the published rate is "
    "a reference only. Excluded from minimum prices and the price-vs-market index."
)

_PROVISIONING: dict[str, str] = {}


def provider_provisioning(data_dir: Path, provider: str) -> str | None:
    """api | console | sales, read from the provider file (single source of truth)."""
    if provider not in _PROVISIONING:
        path = data_dir / "providers" / f"{provider}.json"
        value = None
        if path.exists():
            value = ((json.loads(path.read_text()).get("api") or {}).get("provisioning"))
        _PROVISIONING[provider] = value or ""
    return _PROVISIONING[provider] or None


def mark_sales_only(sku: dict, provisioning: str | None) -> dict:
    """A provider with no self-serve path cannot produce a self-serve package."""
    if provisioning == "sales":
        sku["self_serve"] = False
        if not sku.get("price_note"):
            sku["price_note"] = SALES_ONLY_NOTE
    return sku


def assign_variants(pkgs: list[Package]) -> list[tuple[Package, str]]:
    """'standard' when a (region, gpu, shape) has one package; else the plan slug."""
    groups: dict[tuple, list[Package]] = {}
    for p in pkgs:
        groups.setdefault((p.region, p.accel.gpu, p.gpus), []).append(p)
    out = []
    for group in groups.values():
        for p in group:
            if p.variant:
                v = p.variant
            elif len(group) == 1:
                v = "standard"
            else:
                v = slug(p.flavour or p.accel.variant)
            out.append((p, v))
    ids = [(p.region, p.accel.gpu, p.gpus, v) for p, v in out]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        raise ValueError(f"ambiguous SKU ids: {sorted(dupes)}")
    return out


# ---------------------------------------------------------------------------
# Writer + review report
# ---------------------------------------------------------------------------
# Fields owned by the scraper. Anything else in an existing file (availability
# block, hand-curated interconnect, ...) is preserved.
OWNED = ["id", "provider", "region", "status", "gpu", "gpu_variant", "form_factor", "shape",
         "gpus_per_vm", "variant", "vram_gb_per_gpu", "vcpus", "ram_gb", "disk_gb", "disk_type",
         "pricing", "billing_model", "pricing_status", "price_note", "self_serve", "residency", "sources", "confidence",
         "verified_at", "notes", "interconnect"]
KEEP_IF_NONE = {"vcpus", "ram_gb", "disk_gb", "disk_type", "interconnect", "notes", "self_serve"}
EMPTY_AVAILABILITY = {"last_observed_at": None, "available_vms": None, "available_gpus": None,
                      "spot_available_vms": None, "spot_available_gpus": None, "source": None}


def sku_path(data_dir: Path, sku: dict) -> Path:
    parts = sku["id"].split("/")
    return data_dir / "skus" / Path(*parts[:-1]) / (parts[-1] + ".json")


def merge(old: dict | None, new: dict) -> dict:
    if old is None:
        merged = dict(new)
        merged["availability"] = dict(EMPTY_AVAILABILITY)
        return {k: v for k, v in merged.items() if not (k == "notes" and v is None)}
    merged = dict(old)
    for k in OWNED:
        if k not in new:
            continue
        if new[k] is None and k in KEEP_IF_NONE:
            continue
        merged[k] = new[k]
    if merged.get("interconnect", {}).get("type") is None and "interconnect" in old:
        merged["interconnect"] = old["interconnect"]
    return {k: v for k, v in merged.items() if not (k == "notes" and v is None)}


def _p(sku: dict | None, mode: str) -> Any:
    if not sku:
        return None
    pr = sku.get("pricing", {})
    if mode == "committed":
        return {c["term_months"]: c["usd_per_gpu_hr"] for c in pr.get("committed", [])}
    blk = pr.get(mode)
    return None if not blk else blk.get("usd_per_gpu_hr")


def diff(old: dict | None, new: dict) -> list[str]:
    if old is None:
        return ["NEW"]
    out = []
    for mode in ("on_demand", "spot", "committed"):
        a, b = _p(old, mode), _p(new, mode)
        if a != b:
            out.append(f"{mode} {a} → {b}  [REVIEW: pricing]")
    if old.get("confidence") != new.get("confidence"):
        out.append(f"confidence {old.get('confidence')} → {new.get('confidence')}  [REVIEW: confidence]")
    for k in ("vcpus", "ram_gb", "disk_gb", "vram_gb_per_gpu", "gpu_variant", "status", "pricing_status", "billing_model"):
        if k in new and new[k] is not None and old.get(k) != new[k]:
            out.append(f"{k} {old.get(k)} → {new[k]}")
    return out


def dump(obj: dict) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False) + "\n"


def utc_today() -> str:
    return dt.datetime.now(dt.timezone.utc).date().isoformat()


def retire(old: dict, today: str, reason: str) -> dict:
    """Mark a superseded SKU retired (reversible; nothing is deleted)."""
    new = dict(old)
    new["status"] = "retired"
    note = f"Retired {today} by pricing refresh: {reason}"
    new["notes"] = (old.get("notes") + " " if old.get("notes") else "") + note
    return new
