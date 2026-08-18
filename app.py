"""demo-service — now a tiny web service.

Run it:        python3 app.py          (serves on port 8000)
Run its tests: python3 -m unittest app
"""
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

VERSION = "0.2.0"
# Baked into the package at build time; "dev" when running from source.
GIT_SHA = os.environ.get("GIT_SHA", "dev")


def status():
    """What the service says about itself — the proof at every pipeline step."""
    return {"service": "demo-service", "version": VERSION, "git_sha": GIT_SHA}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps(status()).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass  # keep server logs quiet


# --- tests live in the same file to keep the demo to one .py file ---
import unittest


class TestStatus(unittest.TestCase):
    def test_status_reports_identity(self):
        s = status()
        self.assertEqual(s["service"], "demo-service")
        self.assertEqual(s["version"], VERSION)
        self.assertTrue(s["git_sha"])


if __name__ == "__main__":
    print(f"demo-service {VERSION} ({GIT_SHA}) listening on :8000")
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
