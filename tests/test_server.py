"""HTTP surface tests: the dev server and the published artifact must agree.

Runs the server as a subprocess on a free port, so the test exercises the same code path a
consumer hits (including ETag/CORS/HEAD), not the handler in-process.
"""
from __future__ import annotations

import json
import os
import socket
import subprocess
import sys
import time
import unittest
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from helpers import ROOT, load_json, provider_files, sku_files  # noqa: E402


def free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


class Server(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.port = free_port()
        cls.proc = subprocess.Popen(
            [sys.executable, str(ROOT / "scripts" / "serve_catalog.py"),
             "--data-dir", str(ROOT / "data"), "--assets-dir", str(ROOT / "assets"),
             "--port", str(cls.port)],
            cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        deadline = time.time() + 10
        while time.time() < deadline:
            try:
                urllib.request.urlopen(f"http://127.0.0.1:{cls.port}/api/keys", timeout=1).read()
                return
            except Exception:
                time.sleep(0.1)
        cls.proc.kill()
        raise RuntimeError("server did not start")

    @classmethod
    def tearDownClass(cls):
        cls.proc.terminate()
        cls.proc.wait(timeout=5)

    def url(self, path: str) -> str:
        return f"http://127.0.0.1:{self.port}{path}"

    def get(self, path: str, *, headers=None):
        req = urllib.request.Request(self.url(path), headers=headers or {})
        try:
            with urllib.request.urlopen(req, timeout=5) as r:
                return r.status, dict(r.headers), r.read()
        except urllib.error.HTTPError as e:
            return e.code, dict(e.headers), e.read()

    def test_index_is_html(self):
        status, headers, body = self.get("/")
        self.assertEqual(200, status)
        self.assertIn("text/html", headers["Content-Type"])
        self.assertIn(b"GPU", body)

    def test_api_catalog_matches_files(self):
        status, headers, body = self.get("/api/catalog")
        self.assertEqual(200, status)
        self.assertEqual("*", headers.get("Access-Control-Allow-Origin"))
        payload = json.loads(body)
        served = [load_json(f) for f in sku_files()]
        live = [s for s in served if s.get("status") != "retired"]
        self.assertEqual(len(provider_files()), payload["counts"]["providers"])
        # Retired packages stay in the repo for history but are never served.
        self.assertEqual(len(live), payload["counts"]["skus"])
        self.assertEqual(payload["counts"]["skus"], len(payload["skus"]))

    def test_etag_and_conditional_get(self):
        status, headers, _ = self.get("/api/catalog")
        etag = headers.get("ETag")
        self.assertTrue(etag, "no ETag on /api/catalog")
        status, _, body = self.get("/api/catalog", headers={"If-None-Match": etag})
        self.assertEqual(304, status)
        self.assertEqual(b"", body)

    def test_head_has_headers_and_no_body(self):
        status, headers, body = self.get("/api/keys")  # urllib always GETs
        self.assertEqual(200, status)
        req = urllib.request.Request(self.url("/api/keys"), method="HEAD")
        with urllib.request.urlopen(req, timeout=5) as r:
            self.assertEqual(200, r.status)
            self.assertGreater(int(r.headers["Content-Length"]), 0)
            self.assertEqual(b"", r.read())

    def test_published_artifact_when_present(self):
        dist = ROOT / "dist" / "v1" / "catalog.json"
        if not dist.exists():
            self.skipTest("no export yet; run scripts/export_api.py")
        status, headers, body = self.get("/v1/catalog.json")
        self.assertEqual(200, status)
        self.assertEqual("*", headers.get("Access-Control-Allow-Origin"))
        payload = json.loads(body)
        self.assertIn("schema_version", payload)
        self.assertIn("generated_at", payload)
        live = [f for f in sku_files() if load_json(f).get("status") != "retired"]
        self.assertEqual(len(live), len(payload["skus"]))

    def test_unknown_path_is_json_404(self):
        status, headers, _ = self.get("/v1/does-not-exist.json")
        self.assertEqual(404, status)
        self.assertIn("application/json", headers.get("Content-Type", ""))


if __name__ == "__main__":
    unittest.main()
