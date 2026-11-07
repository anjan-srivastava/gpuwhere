#!/usr/bin/env python3
"""Deprecated entry point, kept so existing cron jobs keep working.

Delegates to `availability_refresh.py -p jarvislabs --write`, which maps
`jl gpus --json` rows onto SKU ids (gpu family + variant) and updates each SKU's
`availability` block. Earlier lines in jarvislabs.jsonl used raw CLI names
(e.g. "A100-80GB", variant null); they are history and are not rewritten.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import availability_refresh  # noqa: E402

if __name__ == "__main__":
    sys.argv = [sys.argv[0], "-p", "jarvislabs", "--write"]
    raise SystemExit(availability_refresh.main())
