SHELL := /bin/bash
ROOT := $(realpath $(dir $(lastword $(MAKEFILE_LIST))))

.PHONY: all check build graph deploy serve clean

all: check build graph

# ── Health checks ──
check: check-yaml lint

check-yaml:
	@echo "=== YAML Integrity Check ==="
	@python3 $(ROOT)/site/check-yaml.py && echo "OK"

lint:
	@echo "=== Wiki Lint ==="
	@bash $(ROOT)/scripts/lint-runner.sh $(ROOT)

# ── Site build ──
build: check-yaml
	@echo "=== Site Build ==="
	@python3 $(ROOT)/site/site_builder.py

# ── Knowledge graph (post-build) ──
graph:
	@echo "=== Knowledge Graph ==="
	@bash $(ROOT)/scripts/graph-html.sh $(ROOT)

# ── Deploy ──
deploy: all
	@echo "=== Deploy to Cloudflare ==="
	@cd $(ROOT) && wrangler pages deploy --commit-message "EN"
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
	@echo "  make build   — Build the site (YAML check + conversion + mkdocs)"
	@echo "  make check   — Health check only (lint + YAML)"
	@echo "  make graph   — Generate interactive knowledge graph"
	@echo "  make all     — Build + graph"
	@echo "  make deploy  — All of the above + deploy to Cloudflare"
	@echo "  make serve   — Local mkdocs preview at http://localhost:8000"
	@echo "  make clean   — Remove build artifacts"
