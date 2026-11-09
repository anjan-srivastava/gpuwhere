# GPU Where — verify, build, publish.
#
#   make                 list targets
#   make check           the four gates: schemas, tests, dist/, freshness
#   make deploy          build dist/ and upload it to Cloudflare Pages
#   make analytics       traffic report from Workers Analytics Engine
#   make deploy-jobs     deploy the separate jobs Worker in ops/cloudflare
#
# Nothing is installed globally. wrangler (the Cloudflare CLI) is downloaded into
# .tools/npm/ by `make tools`; Python dependencies are resolved by uv on demand.
# `make nix-shell` gives the same toolchain from a pinned flake instead.
#
# Environment:
#   CLOUDFLARE_API_TOKEN   Pages:Edit + Account:Read (or run `wrangler login` once)
#   CF_PROJECT             Pages project name       (default gpuwhere)
#   CF_BRANCH              production branch        (default main)
#   CF_ACCOUNT_ID          analytics reports
#   CF_ANALYTICS_TOKEN     analytics reports (Account Analytics:Read)

SHELL   := /bin/bash
.DEFAULT_GOAL := help

PY      ?= python3
UV      := $(shell command -v uv 2>/dev/null)
RUN     := $(if $(UV),$(UV) run --with jsonschema python,$(PY))

TOOLS    := .tools
NPM_DIR  := $(TOOLS)/npm
WRANGLER := $(shell command -v wrangler 2>/dev/null || echo $(NPM_DIR)/node_modules/.bin/wrangler)
WRANGLER_SPEC ?= wrangler@4

CF_PROJECT ?= gpuwhere
CF_BRANCH  ?= main
PORT       ?= 8080
DAYS       ?= 7
JOBS_URL   ?=
JOB_TOKEN  ?=
JOB        ?=

.PHONY: help tools validate test build freshness check serve deploy deploy-jobs run-job jobs schedule job whoami analytics api-key nix-shell release clean

help: ## List targets
	@grep -hE '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[1m%-15s\033[0m %s\n", $$1, $$2}'

tools: ## Download the Cloudflare CLI (wrangler) into .tools/npm
	@if command -v wrangler >/dev/null 2>&1; then \
	  echo "using $$(command -v wrangler)"; wrangler --version; \
	elif [ -x $(NPM_DIR)/node_modules/.bin/wrangler ]; then \
	  $(NPM_DIR)/node_modules/.bin/wrangler --version; \
	else \
	  command -v node >/dev/null 2>&1 || { echo "node is required (brew install node)"; exit 1; }; \
	  mkdir -p $(NPM_DIR); \
	  npm install --prefix $(NPM_DIR) --no-audit --no-fund --no-save $(WRANGLER_SPEC); \
	  $(NPM_DIR)/node_modules/.bin/wrangler --version; \
	fi

validate: ## Validate every JSON file against the schemas
	$(RUN) scripts/validate.py

test: ## Run the Python data/HTTP suite and the edge/jobs worker tests
	$(RUN) -m unittest discover -s tests
	node --test tests/*.test.mjs

build: ## Build the publishable site/API into dist/
	$(RUN) scripts/export_api.py

freshness: ## Fail if pricing/availability/capacity are stale
	$(RUN) scripts/check_freshness.py

check: validate test build freshness ## All four gates (what CI runs)
	@echo "all gates passed"

serve: ## Serve the catalogue at http://127.0.0.1:PORT
	$(RUN) scripts/serve_catalog.py --port $(PORT)

deploy: build tools ## Build and upload dist/ to Cloudflare Pages
	CF_PROJECT=$(CF_PROJECT) CF_BRANCH=$(CF_BRANCH) WRANGLER=$(WRANGLER) ./scripts/deploy_cloudflare.sh

deploy-jobs: tools ## Deploy the separate jobs Worker (on-demand + schedule)
	$(WRANGLER) deploy --config ops/cloudflare/wrangler.toml

run-job: ## Trigger a job remotely: make run-job JOB=pricing
	@test -n "$(JOB)" || { echo "usage: make run-job JOB=pricing"; exit 1; }
	@test -n "$(JOBS_URL)" || { echo "set JOBS_URL=https://gpuwhere-jobs.<subdomain>.workers.dev"; exit 1; }
	@test -n "$(JOB_TOKEN)" || { echo "set JOB_TOKEN"; exit 1; }
	curl -fsS -X POST "$(JOBS_URL)/run?job=$(JOB)" -H "Authorization: Bearer $(JOB_TOKEN)" | $(PY) -m json.tool

jobs: ## Show the latest run of each job
	@test -n "$(JOBS_URL)" -a -n "$(JOB_TOKEN)" || { echo "set JOBS_URL and JOB_TOKEN"; exit 1; }
	curl -fsS "$(JOBS_URL)/jobs" -H "Authorization: Bearer $(JOB_TOKEN)" | $(PY) -m json.tool

schedule: ## Show the effective scraper schedule
	@test -n "$(JOBS_URL)" -a -n "$(JOB_TOKEN)" || { echo "set JOBS_URL and JOB_TOKEN"; exit 1; }
	curl -fsS "$(JOBS_URL)/schedule" -H "Authorization: Bearer $(JOB_TOKEN)" | $(PY) -m json.tool

job: ## Run a job locally: make job JOB=pricing [DRY=1]
	@test -n "$(JOB)" || { echo "usage: make job JOB=pricing"; exit 1; }
	$(PY) scripts/run_job.py $(JOB) $(if $(DRY),--dry-run,)

whoami: tools ## Show which Cloudflare account wrangler is using
	$(WRANGLER) whoami

analytics: ## Traffic report; DAYS=7 by default, add LOCAL=1 for the dev log
	$(RUN) scripts/analytics_report.py --days $(DAYS) $(if $(LOCAL),--local,)

api-key: ## Generate an API key to store as the API_KEYS secret
	@$(PY) -c "import secrets; print(secrets.token_urlsafe(32))"
	@echo
	@echo "set it: $(WRANGLER) pages secret put API_KEYS --project-name $(CF_PROJECT)"

nix-shell: ## Enter the pinned dev shell (requires nix with flakes)
	nix develop

release: ## Tag a release: make release VERSION=0.2.0
	@test -n "$(VERSION)" || { echo "usage: make release VERSION=0.2.0"; exit 1; }
	git tag -a "v$(VERSION)" -m "GPU Where v$(VERSION)"
	@echo "tagged v$(VERSION) — push with: git push origin v$(VERSION)"

clean: ## Remove dist/, downloaded tools and Python caches
	rm -rf dist $(TOOLS)
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
