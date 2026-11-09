"""Keyed API, docs route and the dev analytics sink, exercised over HTTP.

Runs `scripts/serve_catalog.py` as a subprocess, the same way a client hits it.
"""
from __future__ import annotations

import json
import os
import socket
import subprocess
import sys
import tempfile
import time
import unittest
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KEY = "test-key"


def free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


class Api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.log = Path(cls.tmp.name) / "events.jsonl"
        cls.port = free_port()
        env = dict(
            os.environ,
            API_KEYS=KEY,
            PAGE_RATE_PER_MIN="10000",
            API_RATE_PER_MIN="10000",
            EVENT_RATE_PER_MIN="10000",
            DEV_ANALYTICS_LOG=str(cls.log),
        )
        cls.proc = subprocess.Popen(
            [sys.executable, str(ROOT / "scripts" / "serve_catalog.py"),
             "--data-dir", str(ROOT / "data"), "--assets-dir", str(ROOT / "assets"),
             "--port", str(cls.port)],
            cwd=ROOT, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        deadline = time.time() + 10
        while time.time() < deadline:
            try:
                urllib.request.urlopen(f"http://127.0.0.1:{cls.port}/api/openapi.json", timeout=1).read()
                return
            except Exception:
                time.sleep(0.1)
        cls.proc.kill()
        raise RuntimeError("server did not start")

    @classmethod
    def tearDownClass(cls):
        cls.proc.terminate()
        cls.proc.wait(timeout=5)
        cls.tmp.cleanup()

    def call(self, path, *, key=KEY, method="GET", body=None, headers=None):
        req = urllib.request.Request(
            f"http://127.0.0.1:{self.port}{path}",
            method=method,
            data=body,
            headers=headers or {},
        )
        if key:
            req.add_header("Authorization", f"Bearer {key}")
        try:
            with urllib.request.urlopen(req, timeout=10) as res:
                return res.status, res.read(), dict(res.headers)
        except urllib.error.HTTPError as exc:
            return exc.code, exc.read(), dict(exc.headers)

    def payload(self, path, **kwargs):
        status, body, headers = self.call(path, **kwargs)
        return status, json.loads(body or b"{}"), headers

    # --- auth ---------------------------------------------------------------
    def test_missing_key_is_401(self):
        status, data, headers = self.payload("/api/v1/index", key=None)
        self.assertEqual(status, 401)
        self.assertEqual(data["error"]["code"], "unauthorized")
        self.assertIn("Bearer", headers.get("WWW-Authenticate", ""))

    def test_wrong_key_is_401(self):
        status, data, _ = self.payload("/api/v1/index", key="nope")
        self.assertEqual((status, data["error"]["code"]), (401, "unauthorized"))

    def test_bearer_and_header_key_both_work(self):
        status, data, _ = self.payload("/api/v1/index")
        self.assertEqual(status, 200)
        self.assertEqual(data["api"]["base"], "/api/v1")
        status, _, _ = self.call("/api/v1/index", key=None, headers={"X-API-Key": KEY})
        self.assertEqual(status, 200)

    # --- data ---------------------------------------------------------------
    def test_skus_are_filtered(self):
        status, data, _ = self.payload("/api/v1/skus?gpu=H100&provider=e2e-networks")
        self.assertEqual(status, 200)
        self.assertGreater(data["count"], 0)
        for sku in data["skus"]:
            self.assertEqual(sku["gpu"], "H100")
            self.assertEqual(sku["provider"], "e2e-networks")
        self.assertEqual(data["filters"], {"provider": "e2e-networks", "gpu": "H100"})

    def test_availability_is_filtered(self):
        status, data, _ = self.payload("/api/v1/availability/latest?provider=jarvislabs")
        self.assertEqual(status, 200)
        self.assertGreater(data["count"], 0)
        self.assertTrue(all(o["provider"] == "jarvislabs" for o in data["observations"]))

    def test_unknown_endpoint_is_404(self):
        status, data, _ = self.payload("/api/v1/nope")
        self.assertEqual((status, data["error"]["code"]), (404, "not_found"))

    # --- docs ---------------------------------------------------------------
    def test_docs_and_openapi_are_public(self):
        status, body, _ = self.call("/api/docs", key=None)
        self.assertEqual(status, 200)
        self.assertIn(b"/api/v1/skus", body)
        status, spec, _ = self.payload("/api/openapi.json", key=None)
        self.assertEqual(status, 200)
        self.assertIn("/api/v1/skus", spec["paths"])

    # --- analytics ----------------------------------------------------------
    def test_event_is_written(self):
        event = {
            "e": "click", "s": "abc", "p": "#/gpu/nvidia/h100",
            "l": "E2E Networks", "t": "https://www.e2enetworks.com/gpu",
            "r": "https://news.ycombinator.com/item?id=1",
        }
        status, _, _ = self.call("/a", key=None, method="POST",
                                 body=json.dumps(event).encode(),
                                 headers={"Content-Type": "text/plain;charset=UTF-8"})
        self.assertEqual(status, 204)
        rows = [json.loads(line) for line in self.log.read_text(encoding="utf-8").splitlines()]
        row = rows[-1]
        self.assertEqual(row["e"], "click")
        self.assertEqual(row["p"], "#/gpu/nvidia/h100")
        self.assertEqual(row["t"], "www.e2enetworks.com/gpu")
        self.assertEqual(row["r"], "news.ycombinator.com")
        self.assertEqual(row["s"], "abc")

    def test_invalid_event_is_dropped(self):
        before = self.log.read_text(encoding="utf-8") if self.log.exists() else ""
        status, _, _ = self.call("/a", key=None, method="POST", body=b'{"e":"rm -rf"}')
        self.assertEqual(status, 204)
        after = self.log.read_text(encoding="utf-8") if self.log.exists() else ""
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
