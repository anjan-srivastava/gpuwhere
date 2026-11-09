#!/usr/bin/env python3
"""Run one scraper job locally, on demand, with a lock and a log.

    make job JOB=pricing
    make job JOB=availability DRY=1
    python scripts/run_job.py --list

This is the local counterpart of the remote jobs Worker (`make run-job`): same
job names, same scripts, no GitHub required. The job writes to `data/` (unless
--dry-run); publishing still needs `make deploy`.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCK_DIR = ROOT / ".cache" / "jobs"
LOG_DIR = ROOT / "reports" / "jobs"
STALE_LOCK_SECONDS = 12 * 3600

JOBS = {
    "pricing": {
        "script": "scrapers/pricing_refresh.py",
        "args": ["--write", "--retire-superseded"],
        "summary": "Scrape official pricing, update SKUs, retire superseded packages.",
    },
    "availability": {
        "script": "scrapers/availability_refresh.py",
        "args": ["--write"],
        "summary": "Collect free GPUs per provider/region/GPU/shape.",
    },
    "capacity": {
        "script": "scrapers/capacity_refresh.py",
        "args": ["--write"],
        "summary": "Refresh installed capacity from first-party sources.",
    },
    "discovery": {
        "script": "scrapers/discover_providers.py",
        "args": ["--write"],
        "summary": "Probe watchlist candidates; writes a review report only.",
    },
}


def _lock(job: str) -> Path:
    LOCK_DIR.mkdir(parents=True, exist_ok=True)
    path = LOCK_DIR / f"{job}.lock"
    if path.exists():
        age = datetime.now(timezone.utc).timestamp() - path.stat().st_mtime
        if age < STALE_LOCK_SECONDS:
            raise SystemExit(
                f"{job} is already running (lock: {path.relative_to(ROOT)}, {age / 60:.0f} min old).\n"
                f"If that is wrong, remove the file."
            )
        path.unlink()
    fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        json.dump({"pid": os.getpid(), "started_at": datetime.now(timezone.utc).isoformat()}, fh)
    return path


def run(job: str, dry_run: bool) -> int:
    spec = JOBS[job]
    script = ROOT / spec["script"]
    if not script.is_file():
        raise SystemExit(f"missing script: {script}")

    args = spec["args"] if not dry_run else [
        arg for arg in spec["args"] if not arg.startswith("--write") and arg != "--retire-superseded"
    ]
    cmd = [sys.executable, str(script), *args]

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    log_path = LOG_DIR / f"{stamp}-{job}{'-dry' if dry_run else ''}.log"

    lock = _lock(job)
    started = datetime.now(timezone.utc)
    print(f"job        {job}  ({spec['summary']})")
    print(f"command    {' '.join(cmd)}")
    print(f"log        {log_path.relative_to(ROOT)}")
    print()

    try:
        with open(log_path, "w", encoding="utf-8") as log:
            proc = subprocess.Popen(
                cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, bufsize=1,
            )
            assert proc.stdout is not None
            for line in proc.stdout:
                sys.stdout.write(line)
                log.write(line)
            code = proc.wait()
    finally:
        lock.unlink(missing_ok=True)

    elapsed = (datetime.now(timezone.utc) - started).total_seconds()
    print()
    print(f"job {job} {'finished' if code == 0 else 'FAILED'} in {elapsed:.1f}s (exit {code})")
    if code == 0 and not dry_run:
        print("next: make check && make deploy   # data is not published until you deploy")
    return code


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("job", nargs="?", help="job name")
    ap.add_argument("--list", action="store_true", help="list jobs")
    ap.add_argument("--dry-run", action="store_true", help="strip --write/--retire-superseded")
    args = ap.parse_args()

    if args.list or not args.job:
        for name, spec in JOBS.items():
            print(f"{name:<14} {spec['summary']}")
        return 0 if args.list else 2

    if args.job not in JOBS:
        raise SystemExit(f"unknown job {args.job!r}; choose from: {', '.join(JOBS)}")
    return run(args.job, args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
