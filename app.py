"""Tiny demo service.

One endpoint that reports its own version and the git commit it was built
from. That endpoint is the proof at every later step of the pipeline:
if staging answers with a new SHA two minutes after a merge, the pipeline
works.
"""
import os
from pathlib import Path

from flask import Flask, jsonify

app = Flask(__name__)

VERSION = Path(__file__).with_name("VERSION").read_text().strip()
# Baked into the container at build time; "dev" when running from source.
GIT_SHA = os.environ.get("GIT_SHA", "dev")


@app.get("/")
def whoami():
    return jsonify(service="demo-service", version=VERSION, git_sha=GIT_SHA)


@app.get("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
