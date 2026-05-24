SHELL := /bin/bash
ROOT := $(realpath $(dir $(lastword $(MAKEFILE_LIST))))

.PHONY: all check build graph deploy serve clean stats

all: check build graph

# ── Stats auto-update (prerequisite for build + deploy) ──
stats:
	@echo "=== Updating Wiki Stats ==="
	@python3 $(ROOT)/scripts/update-stats.py

# ── Health checks ──
check: check-yaml lint

check-yaml:
	@echo "=== YAML Integrity Check ==="
	@python3 $(ROOT)/site/check-yaml.py && echo "OK"

lint:
	@echo "=== Wiki Lint ==="
	@bash $(ROOT)/scripts/lint-runner.sh $(ROOT)

# ── Site build (stats auto-update first) ──
build: stats check-yaml
	@echo "=== Site Build ==="
	@python3 $(ROOT)/site/site_builder.py

# ── Knowledge graph (post-build) ──
graph:
	@echo "=== Knowledge Graph ==="
	@bash $(ROOT)/scripts/graph-html.sh $(ROOT)

# ── Deploy — builds fresh, auto-updates stats, checks, then deploys ──
deploy: all
	@echo "=== Deploy to Cloudflare ==="
	@source ~/.bashrc && cd $(ROOT) && wrangler pages deploy --commit-message "EN" --commit-dirty=true
	@echo "✓ Deployed"

# ── Local preview ──
serve:
	@cd $(ROOT)/site && mkdocs serve -f mkdocs.yml

# ── Clean ──
clean:
	@echo "=== Clean Build Artifacts ==="
	@rm -rf $(ROOT)/site/content $(ROOT)/site/build
	@echo "✓ Cleaned"

# ── Help ──
help:
	@echo "MOSA Wiki Build System"
	@echo ""
	@echo "Targets:"
	@echo "  make stats    — Auto-update 概述.md + README.md with current counts"
	@echo "  make build    — stats + YAML check + site build"
	@echo "  make check    — Health check only (lint + YAML)"
	@echo "  make graph    — Generate interactive knowledge graph"
	@echo "  make all      — stats + check + build + graph"
	@echo "  make deploy   — all of the above + deploy to Cloudflare"
	@echo "  make serve    — Local mkdocs preview at http://localhost:8000"
	@echo "  make clean    — Remove build artifacts"
