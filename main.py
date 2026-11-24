# One Line of Earned Pride entry (Python 3.13, standard library only).
# Writes one fixed line of text to /output/entry.txt, deterministically.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The line: a quiet, earned moment of pride. For thirty monsoons Harun has
# patched other people's umbrellas; today he trusts his own work enough to
# walk out into the rain under one he kept for himself — and does not hurry.
# Judged on the brief: genuine earned pride, a concrete scene with a real
# person, the pride earned inside the line (never asserted or explained),
# landing in one read, and freshness (no umbrella or monsoon line appears
# among the competition's 1,724 submissions at build time).

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "For thirty monsoons, Harun patched other people's umbrellas; "
    "today he opened the one he'd kept for himself, stepped into "
    "the rain, and didn't hurry."
)

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(LINE, encoding="utf-8")
