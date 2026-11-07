#!/usr/bin/env python3
"""Serve GPU availability JSONL as an HTTP dashboard + JSON API.

Usage:
    python scripts/serve_availability.py --data-dir data/availability --port 8080

Endpoints:
    GET /                       HTML dashboard (Chart.js)
    GET /api/keys               list of provider/gpu/shape/variant keys
    GET /api/availability       filtered time series
        query: provider, gpu, shape, variant (all optional)
"""
from __future__ import annotations

import argparse
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse


def load_rows(data_dir: str) -> list[dict]:
    rows: list[dict] = []
    if not os.path.isdir(data_dir):
        return rows
    for fn in sorted(os.listdir(data_dir)):
        if not fn.endswith(".jsonl"):
            continue
        path = os.path.join(data_dir, fn)
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    rows.sort(key=lambda r: r.get("ts", ""))
    return rows


class Handler(BaseHTTPRequestHandler):
    data_dir = "data/availability"

    def _send(self, body: bytes, content_type: str, code: int = 200) -> None:
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, obj, code: int = 200) -> None:
        self._send(json.dumps(obj).encode("utf-8"), "application/json", code)

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        rows = load_rows(self.data_dir)

        if parsed.path in ("/", "/index.html"):
            self._send(HTML.encode("utf-8"), "text/html; charset=utf-8")
            return

        if parsed.path == "/api/keys":
            keys = sorted({
                (r.get("provider", ""), r.get("gpu", ""), r.get("shape", ""), r.get("variant") or "")
                for r in rows
            })
            self._json([
                {"provider": k[0], "gpu": k[1], "shape": k[2], "variant": k[3]}
                for k in keys
            ])
            return

        if parsed.path == "/api/availability":
            q = parse_qs(parsed.query)

            def one(name: str):
                return q.get(name, [None])[0]

            provider = one("provider")
            gpu = one("gpu")
            shape = one("shape")
            variant = one("variant")

            out = [
                r for r in rows
                if (not provider or r.get("provider") == provider)
                and (not gpu or r.get("gpu") == gpu)
                and (not shape or r.get("shape") == shape)
                and (not variant or (r.get("variant") or "") == variant)
            ]
            self._json(out)
            return

        self._json({"error": "not found"}, 404)

    def log_message(self, fmt: str, *args) -> None:  # keep the console quiet
        pass


HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>GPU Availability</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<style>
  :root { color-scheme: light dark; }
  body { font-family: ui-sans-serif, system-ui, -apple-system, sans-serif; margin: 24px; max-width: 1100px; }
  h1 { font-size: 18px; font-weight: 600; margin: 0 0 16px; }
  .row { display: flex; gap: 16px; align-items: end; flex-wrap: wrap; margin-bottom: 16px; }
  label { display: flex; flex-direction: column; font-size: 12px; gap: 4px; color: #666; }
  select { padding: 6px 8px; font-size: 14px; min-width: 140px; }
  .stats { display: flex; gap: 24px; margin: 12px 0 20px; font-size: 13px; }
  .stat b { display: block; font-size: 20px; }
  .muted { color: #888; }
  canvas { width: 100% !important; height: 420px !important; }
  .legend { font-size: 12px; color: #666; margin-top: 8px; }
</style>
</head>
<body>
<h1>GPU Availability — observations per shape</h1>

<div class="row">
  <label>Provider<select id="provider"></select></label>
  <label>GPU<select id="gpu"></select></label>
  <label>Shape<select id="shape"></select></label>
  <label>Variant<select id="variant"></select></label>
</div>

<div class="stats">
  <div class="stat">Samples<b id="samples">–</b></div>
  <div class="stat">On-demand zero<b id="zero">–</b></div>
  <div class="stat">Spot zero<b id="spotzero">–</b></div>
  <div class="stat">Last observed<b id="last">–</b></div>
</div>

<canvas id="chart"></canvas>
<div class="legend">Solid = on-demand available VMs · Dashed = spot available VMs. Derived VMs are floor(available GPUs / shape).</div>

<script>
const sel = { provider: document.getElementById('provider'), gpu: document.getElementById('gpu'), shape: document.getElementById('shape'), variant: document.getElementById('variant') };
const el = { samples: document.getElementById('samples'), zero: document.getElementById('zero'), spotzero: document.getElementById('spotzero'), last: document.getElementById('last') };
let chart;

async function getJSON(url) { const r = await fetch(url); return r.json(); }

function fill(select, values, keep) {
  const current = keep ? select.value : null;
  select.innerHTML = '';
  values.forEach(v => {
    const o = document.createElement('option');
    o.value = v; o.textContent = v || '(none)';
    select.appendChild(o);
  });
  if (current && values.includes(current)) select.value = current;
}

async function init() {
  const keys = await getJSON('/api/keys');
  const providers = [...new Set(keys.map(k => k.provider))].sort();
  fill(sel.provider, providers);
  await refreshOptions();
  for (const k of Object.keys(sel)) sel[k].addEventListener('change', onSelect);
  await load();
}

async function refreshOptions() {
  const keys = await getJSON('/api/keys');
  const p = sel.provider.value;
  const gp = [...new Set(keys.filter(k => k.provider === p).map(k => k.gpu))].sort();
  fill(sel.gpu, gp, true);
  const s = [...new Set(keys.filter(k => k.provider === p && k.gpu === sel.gpu.value).map(k => k.shape))].sort();
  fill(sel.shape, s, true);
  const v = [...new Set(keys.filter(k => k.provider === p && k.gpu === sel.gpu.value && k.shape === sel.shape.value).map(k => k.variant))].sort();
  fill(sel.variant, v, true);
}

async function onSelect() { await refreshOptions(); await load(); }

async function load() {
  const q = new URLSearchParams({ provider: sel.provider.value, gpu: sel.gpu.value, shape: sel.shape.value, variant: sel.variant.value || '' });
  const rows = await getJSON('/api/availability?' + q.toString());
  const labels = rows.map(r => new Date(r.ts).toLocaleString());
  const ondemand = rows.map(r => r.available_vms);
  const spot = rows.map(r => r.spot_available_vms);

  el.samples.textContent = rows.length;
  el.zero.textContent = rows.length ? Math.round(100 * rows.filter(r => !r.available_vms).length / rows.length) + '%' : '–';
  el.spotzero.textContent = rows.length ? Math.round(100 * rows.filter(r => !r.spot_available_vms).length / rows.length) + '%' : '–';
  el.last.textContent = rows.length ? new Date(rows[rows.length - 1].ts).toLocaleString() : '–';

  if (chart) chart.destroy();
  chart = new Chart(document.getElementById('chart'), {
    type: 'line',
    data: {
      labels,
      datasets: [
        { label: 'On-demand VMs', data: ondemand, borderColor: '#2563eb', backgroundColor: 'rgba(37,99,235,.12)', tension: .2, pointRadius: 2, fill: true },
        { label: 'Spot VMs', data: spot, borderColor: '#f59e0b', borderDash: [6,4], tension: .2, pointRadius: 2, fill: false }
      ]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      interaction: { mode: 'index', intersect: false },
      scales: { y: { beginAtZero: true, title: { display: true, text: 'Available VMs' } }, x: { ticks: { maxTicksLimit: 12 } } },
      plugins: { legend: { position: 'bottom' } }
    }
  });
}

init().catch(err => {
  document.body.insertAdjacentHTML('beforeend', '<pre style="color:#b91c1c">' + err + '</pre>');
});
</script>
</body>
</html>
"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-dir", default="data/availability")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=8080)
    args = ap.parse_args()
    Handler.data_dir = args.data_dir
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"Serving {args.data_dir} at http://{args.host}:{args.port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
