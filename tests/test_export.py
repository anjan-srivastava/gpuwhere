"""Export build: branding, edge worker, API docs and the published artifact."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import export_api  # noqa: E402
import serve_catalog  # noqa: E402


class Branding(unittest.TestCase):
    def test_ui_uses_the_configured_name_and_domain(self):
        html = serve_catalog.HTML
        self.assertIn(serve_catalog.SITE_NAME, html)
        self.assertIn('href="/api/docs"', html)
        self.assertNotIn("gpus.io", html)
        self.assertNotIn("__SITE_", html)
        self.assertNotIn("__REPO_LINK__", html)

    def test_docs_render_without_placeholders(self):
        docs = export_api.render_docs()
        self.assertIn(serve_catalog.SITE_NAME, docs)
        self.assertIn(serve_catalog.SITE_DOMAIN, docs)
        self.assertNotIn("__SITE_", docs)
        self.assertNotIn("__REPO_LINK__", docs)
        self.assertNotIn("atlas", docs.lower())

    def test_source_link_is_conditional(self):
        saved = serve_catalog.SITE_REPO
        try:
            serve_catalog.SITE_REPO = ""
            self.assertEqual(serve_catalog.repo_link(), "")
            serve_catalog.SITE_REPO = "https://github.com/example/gpuwhere"
            link = serve_catalog.repo_link()
            self.assertIn("github.com/example/gpuwhere", link)
            self.assertIn('aria-label="Source code on GitHub"', link)
            self.assertIn("example/gpuwhere", serve_catalog.docs_repo_link())
        finally:
            serve_catalog.SITE_REPO = saved

    def test_web_analytics_beacon_is_conditional(self):
        saved = serve_catalog.WEB_ANALYTICS_TOKEN
        try:
            serve_catalog.WEB_ANALYTICS_TOKEN = ""
            self.assertEqual(serve_catalog.web_analytics_snippet(), "")
            self.assertNotIn("cloudflareinsights",
                             serve_catalog.inject_web_analytics("<html></body></html>"))
            serve_catalog.WEB_ANALYTICS_TOKEN = "abc123"
            snippet = serve_catalog.web_analytics_snippet()
            self.assertIn("beacon.min.js", snippet)
            self.assertIn('"token": "abc123"', snippet)
            self.assertIn("beacon.min.js",
                          serve_catalog.inject_web_analytics("<html></body></html>"))
        finally:
            serve_catalog.WEB_ANALYTICS_TOKEN = saved


class Artifact(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.tmp.name) / "dist"
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "export_api.py"), "--out", str(cls.out)],
            cwd=ROOT, check=True, stdout=subprocess.DEVNULL,
        )

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_layout(self):
        for rel in (
            "index.html", "_headers", "_worker.js",
            "v1/catalog.json", "v1/index.json", "v1/schema/provider.schema.json",
            "v1/availability/latest.json",
            "api/docs/index.html", "api/openapi.json",
            "assets/track.js",
        ):
            self.assertTrue((self.out / rel).is_file(), rel)

    def test_worker_and_docs_are_wired(self):
        worker = (self.out / "_worker.js").read_text(encoding="utf-8")
        self.assertIn("writeDataPoint", worker)
        self.assertIn("/api/v1/", worker)
        docs = (self.out / "api" / "docs" / "index.html").read_text(encoding="utf-8")
        self.assertIn(serve_catalog.SITE_NAME, docs)
        self.assertIn("/api/v1/skus", docs)

    def test_index_advertises_the_api(self):
        index = json.loads((self.out / "v1" / "index.json").read_text(encoding="utf-8"))
        self.assertEqual(index["resources"]["api_docs"], "/api/docs")
        self.assertEqual(index["resources"]["openapi"], "/api/openapi.json")

    def test_ui_is_rebranded(self):
        html = (self.out / "index.html").read_text(encoding="utf-8")
        self.assertNotIn("gpus.io", html)
        self.assertNotIn("__SITE_", html)


if __name__ == "__main__":
    unittest.main()
