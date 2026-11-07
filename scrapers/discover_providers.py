#!/usr/bin/env python3
"""Weekly provider discovery: find GPU providers in India that the catalogue may be missing.

    python scrapers/discover_providers.py            # print the report
    python scrapers/discover_providers.py --write    # also write reports/discovery-<date>.md

Never edits catalogue data. It produces a review list for a human, from:

  1. IndiaAI empanelled-GPU PDF: every bidder that is neither a catalogue provider
     nor on the watchlist is flagged NEW.
  2. Watchlist (data/discovery/candidates.json): each URL is probed (robots.txt
     respected, no bypassing blocks) for evidence — GPU models, INR/hourly prices,
     self-serve hints (sign up, console, API, SDK, Terraform) and India locations —
     and given a suggested verdict.
  3. Global clouds via public sources: Vultr plans API (GPU plans in Indian
     locations?) and Google Cloud's GPU regions page (GPUs in asia-south1/2?).

Inclusion rule (AGENTS.md): GPUs in Indian data centres AND either API/Console
provisioning (any size) or Sales-led with evidence of seriousness.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from pricing_common import Context, FetchError, html_to_text, utc_today  # noqa: E402

INDIAAI_PDF = "https://compute.indiaai.gov.in/files/empanelled-gpus.pdf"
VULTR_PLANS = "https://api.vultr.com/v2/plans?type=all&per_page=500"
VULTR_REGIONS = "https://api.vultr.com/v2/regions"
GCP_GPU_ZONES = "https://cloud.google.com/compute/docs/gpus/gpu-regions-zones"

GPU_RE = re.compile(r"\b(H100|H200|B200|B300|GB200|A100|L40S|L40|L4|A30|A40|MI300X|MI325X|RTX\s?PRO\s?6000|V100|T4)\b", re.I)
SELF_SERVE_RE = re.compile(r"\b(sign\s?up|create (an )?account|launch (an )?instance|console|dashboard|api key|api docs|terraform|sdk|cli)\b", re.I)
PRICE_RE = re.compile(r"(₹\s?[\d,]+(\.\d+)?|rs\.?\s?[\d,]+|inr\s?[\d,]+|\$\s?\d+(\.\d+)?)\s*(/|per)\s*(hr|hour|gpu)", re.I)
INDIA_RE = re.compile(r"\b(india|mumbai|bengaluru|bangalore|chennai|hyderabad|pune|noida|delhi|ncr|raipur|navi mumbai)\b", re.I)


def pdf_text(data: bytes) -> str:
    with tempfile.NamedTemporaryFile(suffix=".pdf") as fh:
        fh.write(data)
        fh.flush()
        return subprocess.check_output(["pdftotext", "-layout", fh.name, "-"], text=True)


def known_names(root: Path) -> list[str]:
    names = []
    for p in (root / "data" / "providers").glob("*.json"):
        d = json.loads(p.read_text())
        names += [d["id"], d["name"]]
    return [n.lower() for n in names]


def indiaai_bidders(ctx: Context) -> list[dict]:
    """Bidders (with GPU counts) from the official empanelled-GPU table."""
    import indiaai_common as ic
    return ic.parse(ic.pdf_text(ctx.get("_discovery", ic.URL, binary=True)))

def probe(ctx: Context, cid: str, urls: list[str]) -> dict:
    sig = {"fetched": [], "blocked": [], "gpus": set(), "self_serve": set(), "prices": 0, "india": False}
    for u in urls:
        try:
            body = ctx.get(f"_discovery/{cid}", u)
        except FetchError as exc:
            sig["blocked"].append(f"{u}: {exc}")
            continue
        text = html_to_text(body) if "<html" in body[:2000].lower() else body
        sig["fetched"].append(u)
        sig["gpus"] |= {re.sub(r"\s", " ", g.upper()) for g in GPU_RE.findall(text)}
        sig["self_serve"] |= {m[0].lower() for m in SELF_SERVE_RE.findall(text)}
        sig["prices"] += len(PRICE_RE.findall(text))
        sig["india"] |= bool(INDIA_RE.search(text))
    return sig


def verdict(kind: str, sig: dict) -> str:
    if kind == "reseller":
        return "reseller / MSP: track, do not add"
    if not sig["fetched"] and sig["blocked"]:
        return "blocked to automated clients: check manually"
    if not sig["fetched"]:
        return "no URL yet: find the official domain"
    if sig["gpus"] and sig["india"] and sig["self_serve"] and sig["prices"]:
        return "LIKELY QUALIFIES (self-serve + published prices): review and add"
    if sig["gpus"] and sig["india"] and sig["self_serve"]:
        return "likely qualifies (self-serve, prices not found): review"
    if sig["gpus"] and sig["india"]:
        return "possible (sales-led?): needs seriousness evidence"
    return "no India GPU evidence found"


def global_checks(ctx: Context) -> list[str]:
    out = []
    try:
        regions = {r["id"]: r["city"] for r in json.loads(ctx.get("_discovery", VULTR_REGIONS))["regions"] if r["country"] == "IN"}
        plans = json.loads(ctx.get("_discovery", VULTR_PLANS))["plans"]
        india_gpu = [(p["id"], p.get("gpu_type"), [regions[l] for l in p["locations"] if l in regions])
                     for p in plans if p.get("gpu_type") and any(l in regions for l in p["locations"])]
        out.append(f"Vultr: India regions {sorted(regions.values())}; GPU plans available there: "
                   + (", ".join(f"{i} ({g}) in {', '.join(c)}" for i, g, c in india_gpu) if india_gpu else "none → does not qualify yet"))
    except Exception as exc:  # noqa: BLE001
        out.append(f"Vultr: automated check not possible ({exc}); check vultr.com manually")
    try:
        text = html_to_text(ctx.get("_discovery", GCP_GPU_ZONES))
        hits = sorted({m.group(0) for m in re.finditer(r"asia-south[12]-[abc]", text)})
        out.append(f"Google Cloud: India GPU zones listed on the GPU regions page: {', '.join(hits) if hits else 'none found'}"
                   + (" → review for addition" if hits else ""))
    except Exception as exc:  # noqa: BLE001
        out.append(f"Google Cloud check failed: {exc}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(HERE.parent))
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    root = Path(args.root)
    today = utc_today()
    ctx = Context(root / ".cache" / "scrape", today)
    watch = json.loads((root / "data" / "discovery" / "candidates.json").read_text())["candidates"]
    known = known_names(root)
    watch_names = [c["name"].lower() for c in watch] + [c["id"] for c in watch]

    lines = [f"# Provider discovery {today}", "",
             "Review list only; nothing here is added to the catalogue automatically.", ""]

    lines += ["## IndiaAI empanelled bidders", ""]
    try:
        for row in indiaai_bidders(ctx):
            b = row["name"]
            # ignore bracketed qualifiers ("[CSP: Google Cloud Platform]") and generic company words
            base = re.sub(r"\[[^\]]*\]", "", b.lower())
            key = re.sub(r"\b(pvt|private|ltd|limited|technologies|technology|india|services|consortium|solutions|"
                         r"enterprise|datacenter|cloud|digital|it|platforms?|networks?|data|infotech|systems|computers?|&)\b\.?", "", base)
            words = [w for w in re.findall(r"[a-z0-9]+", key) if len(w) > 2]
            in_cat = any(w in n for w in words for n in known)
            in_watch = any(w in n for w in words for n in watch_names)
            status = "catalogue" if in_cat else "watchlist" if in_watch else "**NEW — not in catalogue or watchlist**"
            lines.append(f"- {b} ({row['total']:,} GPUs): {status}")
    except Exception as exc:  # noqa: BLE001
        lines.append(f"- FAILED to read the IndiaAI PDF: {exc}")
    lines.append("")

    lines += ["## Watchlist probes", "", "| Candidate | Kind | GPUs seen | Self-serve hints | Price hits | India | Suggested verdict |",
              "|---|---|---|---|---|---|---|"]
    for c in watch:
        sig = probe(ctx, c["id"], c.get("urls") or []) if c["kind"] != "reseller" else {
            "fetched": [], "blocked": [], "gpus": set(), "self_serve": set(), "prices": 0, "india": False}
        lines.append(f"| {c['name']} | {c['kind']} | {', '.join(sorted(sig['gpus'])) or '—'} | "
                     f"{', '.join(sorted(sig['self_serve'])) or '—'} | {sig['prices']} | {'yes' if sig['india'] else '—'} | "
                     f"{verdict(c['kind'], sig)} |")
        for b in sig["blocked"]:
            lines.append(f"|  ↳ {b} | | | | | | |")
    lines.append("")

    lines += ["## Global clouds (India regions)", ""] + [f"- {x}" for x in global_checks(ctx)] + [""]
    text = "\n".join(lines) + "\n"
    print(text)
    if args.write:
        out = root / "reports" / f"discovery-{today}.md"
        out.write_text(text)
        print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
