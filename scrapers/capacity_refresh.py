#!/usr/bin/env python3
"""Weekly installed-capacity refresh from official documents.

    python scrapers/capacity_refresh.py            # dry-run: print extracted pools
    python scrapers/capacity_refresh.py --write    # rewrite data/capacity/<provider>.json

Capacity is installed fleet (`total_gpus` per pool), never observed free GPUs.
Only first-party or government sources are scripted; each figure keeps the
exact phrase it was read from. Providers without an official fleet figure keep
`total_gpus: null`. Extractors fail loudly when the wording changes, so a
silent wrong number cannot slip in.

Sources:
  e2e-networks   latest investor presentation PDF (via investor-presentations.md)
  yotta-shakti   shakticloud.ai homepage fleet claim
  (all)          IndiaAI compute-allocation table: allocations active today are
                 noted per provider; the table is a partial snapshot, so it is
                 not summed into committed_gpus.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html as htmlmod
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from pricing_common import Context, dump, html_to_text, utc_today  # noqa: E402

E2E_IP = "https://www.e2enetworks.com/investors/investor-presentations.md"
SHAKTI = "https://shakticloud.ai/"
INDIAAI = "https://indiaai.gov.in/hub/indiaai-compute-capacity"
INDIAAI_EMPANELLED = "https://compute.indiaai.gov.in/files/empanelled-gpus.pdf"
EMP_COLUMNS = ["H100", "H200", "L40S", "L4", "A100", "B200", "MI300X", "MI325X", "Gaudi 2", "Gaudi 3",
               "Trainium 1", "Inferentia 2", "Trillium"]
# bidder text → provider id (resellers/MSPs are intentionally absent; discovery lists them)
EMP_PROVIDERS = [("E2E", "e2e-networks"), ("Jio", "jio-platforms"), ("NxtGen", "nxtgen"),
                 ("Tata Communications", "tata-communications"), ("Yotta", "yotta-shakti"),
                 ("Cyfuture", "cyfuture-ai"), ("Sify", "sify"), ("Netmagic", "neysa"), ("Neysa", "neysa")]
INDIAAI_PROVIDERS = {
    "E2E Networks": "e2e-networks", "NxtGen": "nxtgen", "Yotta": "yotta-shakti", "Jio": "jio-platforms",
    "Tata Communications": "tata-communications", "CtrlS": "ctrls", "Sify": "sify", "Cyfuture": "cyfuture-ai",
    "Neysa": "neysa",
}


class ExtractError(RuntimeError):
    pass


def _int(s: str) -> int:
    return int(s.replace(",", ""))


def _pdf_text(data: bytes) -> str:
    with tempfile.NamedTemporaryFile(suffix=".pdf") as fh:
        fh.write(data)
        fh.flush()
        return subprocess.check_output(["pdftotext", "-layout", fh.name, "-"], text=True)


def _src(url: str, kind: str, today: str) -> dict:
    return {"url": url, "kind": kind, "fetched_at": today}


def e2e(ctx: Context, today: str) -> dict:
    md = ctx.get("e2e-networks", E2E_IP)
    pdfs = re.findall(r"\((https://[^)]+/Investor_Presentations/[^)]*IP[^)]*\.pdf)\)", md)
    if not pdfs:
        raise ExtractError("no investor presentation PDF link found")
    url = pdfs[0]  # page lists newest first
    text = re.sub(r"[ \t]+", " ", _pdf_text(ctx.get("e2e-networks", url, binary=True)))
    quarter = re.search(r"Q\d ?FY\d{2}", text)
    total = re.search(r"~\s*([\d,]+)\s*GPUs live", text) or re.search(r"~([\d,]+)\s*\n?\s*cloud GPUs live", text)
    b200 = re.search(r"including\s+([\d,]+)\s+(?:NVIDIA\s+)?B200s", text)
    hopper = re.search(r"nearly\s+([\d,]+)\s+Hopper", text)
    if not (total and b200):
        raise ExtractError("fleet phrases ('~N GPUs live', 'including N B200s') not found; wording changed")
    t, b = _int(total.group(1)), _int(b200.group(1))
    q = quarter.group(0).replace(" ", "") if quarter else "latest"
    src = _src(url, "page", today)
    pools = [{"gpu": "B200", "region": "IN", "form_factor": "sxm", "total_gpus": b, "rented_gpus": None,
              "committed_gpus": None, "free_gpus": None, "power_mw": None, "source": src,
              "notes": f"E2E {q} investor presentation: 'including {b200.group(1)} NVIDIA B200s'; "
                       "'Blackwell capacity now under multi-year contract' (count under contract not stated)."}]
    rest = t - b
    if hopper:
        h = _int(hopper.group(1))
        pools.append({"gpu": "H100/H200", "region": "IN", "form_factor": "sxm", "total_gpus": h,
                      "rented_gpus": None, "committed_gpus": None, "free_gpus": None, "power_mw": None,
                      "source": src, "notes": f"'nearly {hopper.group(1)} Hopper' GPUs; H100/H200 split not published."})
        rest -= h
    if rest > 0:
        pools.append({"gpu": "Other", "region": "IN", "form_factor": None, "total_gpus": rest,
                      "rented_gpus": None, "committed_gpus": None, "free_gpus": None, "power_mw": None,
                      "source": src, "notes": f"Derived: '~{total.group(1)} GPUs live' minus the pools above; approximate. "
                                              "Mix (A100/L40S/L4/…) not published."})
    return {
        "as_of": q, "pools": pools, "sources": [_src(E2E_IP, "page", today), src], "confidence": "medium",
        "notes": f"Installed fleet from E2E's {q} investor presentation (~{total.group(1)} GPUs live, Delhi NCR and "
                 "Chennai). Figures are rounded by E2E. JarvisLabs has been an E2E platform since Dec 2025; whether "
                 "its fleet is included is not stated.",
    }


def yotta(ctx: Context, today: str) -> dict:
    text = html_to_text(ctx.get("yotta-shakti", SHAKTI))
    m = re.search(r"([\d,]+)\+?\s*H100 GPUs", text)
    if not m:
        raise ExtractError("'N+ H100 GPUs' phrase not found on shakticloud.ai")
    n = _int(m.group(1))
    plus = "+" if re.search(re.escape(m.group(1)) + r"\+", text) else ""
    b200 = "B200s coming soon" if re.search(r"B200s?\s*\(?coming soon", text, re.I) else None
    return {
        "as_of": today, "confidence": "medium",
        "pools": [{"gpu": "H100", "region": "IN", "form_factor": "sxm", "total_gpus": n, "rented_gpus": None,
                   "committed_gpus": None, "free_gpus": None, "power_mw": None, "source": _src(SHAKTI, "page", today),
                   "notes": f"shakticloud.ai: '{m.group(1)}{plus} H100 GPUs' — a lower bound."
                            + (f" Same page: '{b200}'." if b200 else "")}],
        "sources": [_src(SHAKTI, "page", today)],
        "notes": "Yotta's own homepage states the H100 fleet as a lower bound; L40S/B200 fleet sizes are not "
                 "published there. NVIDIA's customer story claims '16,000+ H100' (vendor source, older); the "
                 "first-party figure is used.",
    }


def indiaai_active(ctx: Context, today: str) -> dict[str, list[str]]:
    h = ctx.get("_indiaai", INDIAAI)
    tables = re.findall(r"(?is)<table.*?</table>", h)
    if not tables:
        raise ExtractError("IndiaAI allocation table not found")
    out: dict[str, dict[str, int]] = {}
    d = dt.date.fromisoformat(today)
    for tr in re.findall(r"(?is)<tr[^>]*>(.*?)</tr>", tables[0])[1:]:
        c = [re.sub(r"\s+", " ", htmlmod.unescape(re.sub("<[^>]+>", " ", x))).strip()
             for x in re.findall(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>", tr)]
        if len(c) < 11:
            continue
        span = re.findall(r"(\d{4})/(\d{2})/(\d{2})", c[10])
        if len(span) != 2:
            continue
        start, end = (dt.date(*map(int, s)) for s in span)
        if not (start <= d <= end):
            continue
        pid = next((v for k, v in INDIAAI_PROVIDERS.items() if k.lower() in c[6].lower()), None)
        if pid:
            out.setdefault(pid, {}).setdefault(c[5], 0)
            out[pid][c[5]] += int(c[4])
    return {pid: [f"{n}× {g}" for g, n in sorted(v.items())] for pid, v in out.items()}


EXTRACTORS = {"e2e-networks": e2e, "yotta-shakti": yotta}


def indiaai_empanelled(ctx: Context, today: str) -> dict[str, dict]:
    """Per-provider GPU counts from the official IndiaAI empanelled-GPU table.

    These are GPUs empanelled (offered) under IndiaAI, some not yet operational,
    so they are stored separately and never summed into installed capacity."""
    import indiaai_common as ic
    out: dict[str, dict] = {}
    for row in ic.parse(ic.pdf_text(ctx.get("_indiaai", ic.URL, binary=True))):
        pid = next((v for k, v in EMP_PROVIDERS if k.lower() in row["name"].lower()), None)
        if not pid or pid in out:
            continue
        out[pid] = {"total": row["total"], "by_gpu": row["counts"],
                    "source": {"url": ic.URL, "kind": "page", "fetched_at": today},
                    "notes": "GPUs empanelled for the IndiaAI Mission (offered under the tender; some may not yet be operational). "
                             f"Not installed-fleet capacity. Listed as '{row['name']}'."}
    if not out:
        raise ExtractError("no catalogue providers matched in the IndiaAI empanelled-GPU PDF")
    return out

def _offered(root: Path, pid: str) -> dict[str, int]:
    """GPU family → number of non-retired host packages the provider lists."""
    out: dict[str, int] = {}
    base = root / "data" / "skus" / pid
    for f in base.rglob("*.json") if base.exists() else []:
        d = json.loads(f.read_text())
        if d.get("status") != "retired":
            out[d["gpu"]] = out.get(d["gpu"], 0) + 1
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(HERE.parent))
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    root = Path(args.root)
    today = utc_today()
    ctx = Context(root / ".cache" / "scrape", today)
    rc = 0
    try:
        active = indiaai_active(ctx, today)
    except Exception as exc:
        print(f"[indiaai] FAILED: {exc}", file=sys.stderr)
        active, rc = {}, 1
    try:
        empanelled = indiaai_empanelled(ctx, today)
    except Exception as exc:
        print(f"[indiaai-empanelled] FAILED: {exc}", file=sys.stderr)
        empanelled, rc = {}, 1

    for path in sorted((root / "data" / "capacity").glob("*.json")):
        old = json.loads(path.read_text())
        pid = old["provider"]
        new = dict(old)
        new["pools"] = [p for p in old.get("pools", []) if not (p.get("total_gpus") is None and p.get("source") is None)]
        if pid in EXTRACTORS:
            try:
                new.update(EXTRACTORS[pid](ctx, today))
            except Exception as exc:
                print(f"[{pid}] FAILED: {exc}", file=sys.stderr)
                rc = 1
                continue
        # Every GPU family the provider sells gets a pool row, so capacity never implies
        # that only the published family exists. Unpublished fleet size stays null.
        offered = _offered(root, pid)
        covered = {g for p in new["pools"] for g in p["gpu"].split("/")}
        if "Other" not in covered:
            for gpu in sorted(set(offered) - covered):
                new["pools"] = new["pools"] + [{
                    "gpu": gpu, "region": "IN", "form_factor": None, "total_gpus": None, "rented_gpus": None,
                    "committed_gpus": None, "free_gpus": None, "power_mw": None, "source": None,
                    "notes": f"Offered ({offered[gpu]} host packages); fleet size not published."}]
        if pid in empanelled:
            new["indiaai_empanelled"] = empanelled[pid]
        note = (f" IndiaAI allocation table lists active allocations on {today}: {', '.join(active[pid])} "
                "(partial public snapshot; not summed into committed_gpus).") if pid in active else ""
        base = re.sub(r" IndiaAI allocation table lists active allocations.*?committed_gpus\)\.", "", new.get("notes") or "")
        new["notes"] = (base + note).strip() or None
        new["verified_at"] = today
        if new == old:
            continue
        total = sum(p["total_gpus"] for p in new["pools"] if p.get("total_gpus") is not None) if new["pools"] else None
        print(f"[{pid}] pools={len(new['pools'])} total_gpus={total} confidence={new['confidence']}"
              + (" [REVIEW: confidence]" if new["confidence"] != old.get("confidence") else ""))
        for p in new["pools"]:
            print(f"    {p['gpu']:<10} {p['region']:<4} total={p['total_gpus']}  {p.get('notes', '')[:110]}")
        if args.write:
            path.write_text(dump(new))
    print("written" if args.write else "dry-run")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
