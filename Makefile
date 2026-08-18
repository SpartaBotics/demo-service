# The four standard targets every company repo exposes, whatever the
# language, so one shared CI workflow serves all repos without special cases.
#
#   make lint      style and correctness checks
#   make test      unit tests
#   make build     the sealed package (container image), SHA baked in
#   make security  known vulnerabilities in dependencies

# Use the local venv when present (developer laptop), plain python3 otherwise (CI).
PY := $(shell [ -x .venv/bin/python ] && echo .venv/bin/python || echo python3)

IMAGE   ?= demo-service
GIT_SHA := $(shell git rev-parse --short HEAD)

.PHONY: lint test build security

lint:
	$(PY) -m ruff check .

test:
	$(PY) -m pytest tests/ -q

build:
	docker build --build-arg GIT_SHA=$(GIT_SHA) -t $(IMAGE):git-$(GIT_SHA) .

security:
	$(PY) -m pip_audit -r requirements.txt
