"""Shared parser for the official IndiaAI empanelled-GPU table (PDF).

Source: https://compute.indiaai.gov.in/files/empanelled-gpus.pdf

`pdftotext -layout` keeps one line per data row, but long bidder names wrap onto
the lines above and below. Each wrapped name line is assigned to the nearest data
row; on a tie it goes to the row whose own line carries no name (that row is the
one whose name was wrapped). Every row is checked against its printed total.
"""
from __future__ import annotations

import re
import subprocess
import tempfile

URL = "https://compute.indiaai.gov.in/files/empanelled-gpus.pdf"
COLUMNS = ["H100", "H200", "L40S", "L4", "A100", "B200", "MI300X", "MI325X", "Gaudi 2", "Gaudi 3",
           "Trainium 1", "Inferentia 2", "Trillium"]
_TOK = re.compile(r"(?:(?<=\s)|^)([\d,]+|-)(?=\s|$)")
_HEADER = re.compile(r"GPU OEMs|GPU Categories|Bidders|Nvidia|H100\s+H200|^\s*#", re.I)


def pdf_text(data: bytes) -> str:
    with tempfile.NamedTemporaryFile(suffix=".pdf") as fh:
        fh.write(data)
        fh.flush()
        return subprocess.check_output(["pdftotext", "-layout", fh.name, "-"], text=True)


def _is_row(line: str) -> bool:
    return len(_TOK.findall(line)) >= len(COLUMNS) + 1 and not line.strip().upper().startswith("TOTAL")


def parse(text: str) -> list[dict]:
    """→ [{"name", "counts": {gpu: n}, "total"}] in table order."""
    lines = text.splitlines()
    rows = []
    for i, line in enumerate(lines):
        if not _is_row(line):
            continue
        vals = _TOK.findall(line)[-(len(COLUMNS) + 1):]
        inline = re.sub(r"(\s+[\d,]+|\s+-)+\s*$", "", line)
        inline = re.sub(r"^\s*\d{1,2}\s+", "", inline).strip()
        inline = "" if re.fullmatch(r"\d{1,2}", inline) else inline
        counts = {c: int(v.replace(",", "")) for c, v in zip(COLUMNS, vals[:-1]) if v != "-"}
        total = int(vals[-1].replace(",", ""))
        if sum(counts.values()) != total:
            raise ValueError(f"IndiaAI row at line {i + 1} does not add up ({sum(counts.values())} vs {total})")
        rows.append({"line": i, "inline": inline, "frags": [], "counts": counts, "total": total})
    if not rows:
        raise ValueError("no data rows found in the IndiaAI empanelled-GPU table")
    first, last = rows[0]["line"], rows[-1]["line"]
    for j in range(max(0, first - 3), min(len(lines), last + 3)):
        line = lines[j]
        if _is_row(line) or not line.strip() or _HEADER.search(line) or line.strip().upper().startswith("TOTAL"):
            continue
        frag = line.strip()
        best = min(rows, key=lambda r: (abs(r["line"] - j), 0 if not r["inline"] else 1))
        if abs(best["line"] - j) <= 2:
            best["frags"].append((j, frag))
    out = []
    for r in rows:
        parts = [f for j, f in r["frags"] if j < r["line"]] + ([r["inline"]] if r["inline"] else []) \
            + [f for j, f in r["frags"] if j > r["line"]]
        out.append({"name": re.sub(r"\s+", " ", " ".join(parts)).strip(), "counts": r["counts"], "total": r["total"]})
    return out
