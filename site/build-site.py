#!/usr/bin/env python3
"""Backward-compat wrapper — delegates to site_builder.py."""
from pathlib import Path
exec(open(Path(__file__).parent / "site_builder.py").read())
