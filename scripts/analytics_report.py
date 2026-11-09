#!/usr/bin/env python3
"""Print a traffic report from the Workers Analytics Engine event stream.

    make analytics                     # last 7 days from Cloudflare
    make analytics DAYS=30
    python scripts/analytics_report.py --local   # read .cache/dev-analytics.jsonl

Cloudflare mode needs two environment variables:

    CF_ACCOUNT_ID          your account id
    CF_ANALYTICS_TOKEN     API token with Account Analytics:Read

Optional: ANALYTICS_DATASET (default gpuwhere_events).

The event schema is fixed in server/api_worker.mjs:
    blob1 event   pageview | click | search
    blob2 path    route or page path
    blob3 label   link text
    blob4 target  outbound host+path, internal route, or search query
    blob5 referrer host
    blob6 country
    index1        random per-tab session id
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCAL_LOG = ROOT / ".cache" / "dev-analytics.jsonl"
SQL_API = "https://api.cloudflare.com/client/v4/accounts/{account}/analytics_engine/sql"

# Public account id; the token is the only secret required.
DEFAULT_ACCOUNT_ID = "3f39b0def6194f4d9877bc0e6cfce578"
WRANGLER_CONFIGS = (
    Path.home() / "Library" / "Preferences" / ".wrangler" / "config" / "default.toml",
    Path.home() / ".wrangler" / "config" / "default.toml",
    Path.home() / ".config" / ".wrangler" / "config" / "default.toml",
)


def _wrangler_token() -> str:
    """Use the local `wrangler login` token when CF_ANALYTICS_TOKEN is unset."""
    for path in WRANGLER_CONFIGS:
        try:
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip().startswith("oauth_token"):
                    return line.split('"', 2)[1]
        except (OSError, IndexError):
            continue
    return ""


def _table(rows: list[dict], columns: list[str], empty: str = "no data") -> str:
    if not rows:
        return f"  {empty}"
    widths = {c: max(len(c), *(len(str(r.get(c, ""))) for r in rows)) for c in columns}
    head = "  " + "  ".join(c.upper().ljust(widths[c]) for c in columns)
    line = "  " + "  ".join("-" * widths[c] for c in columns)
    body = ["  " + "  ".join(str(r.get(c, "")).ljust(widths[c]) for c in columns) for r in rows]
    return "\n".join([head, line, *body])


def query(account: str, token: str, sql: str) -> list[dict]:
    url = SQL_API.format(account=account)
    req = urllib.request.Request(
        url,
        data=sql.encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "text/plain",
            "User-Agent": "gpuwhere-analytics",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            payload = json.load(res)
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:500]
        raise SystemExit(f"Analytics Engine query failed ({exc.code}): {detail}") from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"Could not reach Cloudflare: {exc.reason}") from exc
    if not payload.get("success", True):
        raise SystemExit(f"Analytics Engine query failed: {payload.get('errors')}")
    return payload.get("data", [])


def cloud_report(days: int, limit: int) -> None:
    account = os.environ.get("CF_ACCOUNT_ID", "").strip() or DEFAULT_ACCOUNT_ID
    token = os.environ.get("CF_ANALYTICS_TOKEN", "").strip()
    dataset = os.environ.get("ANALYTICS_DATASET", "gpuwhere_events").strip()
    if not token:
        token = _wrangler_token()
        if token:
            print("(using the local wrangler login token; set CF_ANALYTICS_TOKEN to override)",
                  file=sys.stderr)
    if not token:
        raise SystemExit(
            "No analytics token. Set CF_ANALYTICS_TOKEN (Account Analytics:Read),\n"
            "run `wrangler login`, or run with --local to read the development log."
        )
    if not all(ch.isalnum() or ch == "_" for ch in dataset):
        raise SystemExit("ANALYTICS_DATASET must be alphanumeric/underscore")

    since = f"timestamp > now() - INTERVAL '{int(days)}' DAY"
    where = f"{since}"

    def q(sql: str) -> list[dict]:
        return query(account, token, sql.format(dataset=dataset))

    totals = q(f"""
        SELECT sum(_sample_interval) AS events, count(DISTINCT index1) AS sessions
        FROM {dataset} WHERE {where}
    """)[0]
    views = q(f"""
        SELECT sum(_sample_interval) AS views
        FROM {dataset} WHERE blob1 = 'pageview' AND {where}
    """)[0]
    clicks = q(f"""
        SELECT sum(_sample_interval) AS clicks
        FROM {dataset} WHERE blob1 = 'click' AND {where}
    """)[0]

    print(f"GPU Where — last {days} days")
    print(f"  pageviews {int(float(views.get('views') or 0)):,}"
          f" · clicks {int(float(clicks.get('clicks') or 0)):,}"
          f" · sessions {int(float(totals.get('sessions') or 0)):,}"
          f" · events {int(float(totals.get('events') or 0)):,}")
    print("  pageviews and clicks are events; sessions are distinct per-tab ids (no cookie)")

    print("\nPAGEVIEWS BY DAY")
    by_day = q(f"""
        SELECT toDate(timestamp) AS day, sum(_sample_interval) AS views,
               count(DISTINCT index1) AS sessions
        FROM {dataset} WHERE blob1 = 'pageview' AND {where}
        GROUP BY day ORDER BY day
    """)
    print(_table(by_day, ["day", "views", "sessions"]))

    print("\nTOP PAGES")
    pages = q(f"""
        SELECT blob2 AS path, sum(_sample_interval) AS views,
               count(DISTINCT index1) AS sessions
        FROM {dataset} WHERE blob1 = 'pageview' AND {where}
        GROUP BY path ORDER BY views DESC LIMIT {int(limit)}
    """)
    print(_table(pages, ["path", "views", "sessions"]))

    print("\nREFERRERS")
    refs = q(f"""
        SELECT blob5 AS referrer, sum(_sample_interval) AS views
        FROM {dataset} WHERE blob1 = 'pageview' AND blob5 != '' AND {where}
        GROUP BY referrer ORDER BY views DESC LIMIT {int(limit)}
    """)
    print(_table(refs, ["referrer", "views"]))

    print("\nCOUNTRIES")
    countries = q(f"""
        SELECT blob6 AS country, sum(_sample_interval) AS views
        FROM {dataset} WHERE blob1 = 'pageview' AND {where}
        GROUP BY country ORDER BY views DESC LIMIT {int(limit)}
    """)
    print(_table(countries, ["country", "views"]))

    print("\nMOST-CLICKED LINKS")
    links = q(f"""
        SELECT blob3 AS label, blob4 AS target, sum(_sample_interval) AS clicks
        FROM {dataset} WHERE blob1 = 'click' AND {where}
        GROUP BY label, target ORDER BY clicks DESC LIMIT {int(limit)}
    """)
    print(_table(links, ["label", "target", "clicks"]))

    print("\nSEARCHES")
    searches = q(f"""
        SELECT blob4 AS query, sum(_sample_interval) AS search
        FROM {dataset} WHERE blob1 = 'search' AND blob4 != '' AND {where}
        GROUP BY query ORDER BY search DESC LIMIT {int(limit)}
    """)
    print(_table(searches, ["query", "search"]))

    print("\nRECENT CLICK STREAM")
    recent = q(f"""
        SELECT timestamp, blob1 AS event, blob2 AS path, blob3 AS label,
               blob4 AS target, blob5 AS referrer, blob6 AS country
        FROM {dataset} WHERE {where}
        ORDER BY timestamp DESC LIMIT {int(limit)}
    """)
    print(_table(recent, ["timestamp", "event", "path", "label", "target", "referrer", "country"]))


def local_report(days: int, limit: int) -> None:
    if not LOCAL_LOG.exists():
        raise SystemExit(f"{LOCAL_LOG} is empty — run `make serve` and click around first.")
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    rows = []
    for line in LOCAL_LOG.read_text(encoding="utf-8").splitlines():
        try:
            row = json.loads(line)
        except ValueError:
            continue
        try:
            ts = datetime.fromisoformat(row["ts"].replace("Z", "+00:00"))
        except (KeyError, ValueError):
            continue
        if ts >= cutoff:
            rows.append(row)

    views = [r for r in rows if r.get("e") == "pageview"]
    clicks = [r for r in rows if r.get("e") == "click"]
    sessions = {r.get("s") for r in rows if r.get("s")}

    print(f"GPU Where — last {days} days (local dev log)")
    print(f"  pageviews {len(views):,} · clicks {len(clicks):,} · sessions {len(sessions):,} · events {len(rows):,}")
    print("  pageviews and clicks are events; sessions are distinct per-tab ids (no cookie)")

    print("\nPAGEVIEWS BY DAY")
    days_count: dict[str, list] = {}
    for r in views:
        day = r["ts"][:10]
        days_count.setdefault(day, [0, set()])
        days_count[day][0] += 1
        days_count[day][1].add(r.get("s"))
    print(_table([{"day": d, "views": v[0], "sessions": len(v[1])}
                  for d, v in sorted(days_count.items())], ["day", "views", "sessions"]))

    print("\nTOP PAGES")
    pages: dict[str, list] = {}
    for r in views:
        path = r.get("p", "")
        pages.setdefault(path, [0, set()])
        pages[path][0] += 1
        pages[path][1].add(r.get("s"))
    top = sorted(pages.items(), key=lambda kv: kv[1][0], reverse=True)[:limit]
    print(_table([{"path": p, "views": v[0], "sessions": len(v[1])} for p, v in top],
                 ["path", "views", "sessions"]))

    print("\nREFERRERS")
    refs = Counter(r.get("r", "") for r in views if r.get("r"))
    print(_table([{"referrer": k, "views": n} for k, n in refs.most_common(limit)], ["referrer", "views"]))

    print("\nMOST-CLICKED LINKS")
    links = Counter((r.get("l", ""), r.get("t", "")) for r in clicks)
    print(_table([{"label": k[0], "target": k[1], "clicks": n} for k, n in links.most_common(limit)],
                 ["label", "target", "clicks"]))

    print("\nRECENT CLICK STREAM")
    recent = [{**r, "timestamp": r.get("ts", "")} for r in reversed(rows[-limit:])]
    print(_table(recent, ["timestamp", "e", "p", "l", "t", "r", "country"]))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--local", action="store_true", help="read .cache/dev-analytics.jsonl instead of Cloudflare")
    args = ap.parse_args()
    if args.days < 1 or args.limit < 1:
        raise SystemExit("--days and --limit must be positive")
    if args.local:
        local_report(args.days, args.limit)
    else:
        cloud_report(args.days, args.limit)
    return 0


if __name__ == "__main__":
    sys.exit(main())
