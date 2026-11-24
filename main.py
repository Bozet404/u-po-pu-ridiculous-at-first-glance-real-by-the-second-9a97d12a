#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes a single-sentence startup pitch (at most 200 characters) to
/output/entry.txt, the way the bounty gate expects it.
"""

import os

SENTENCE = (
    "We sell naming rights to potholes: drivers pay $5 a month to name "
    "the pothole that wrecked their suspension, and cities take a cut "
    "because a named pothole is a scandal they must fix first."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = SENTENCE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-200")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {path} ({len(text)} characters)")


if __name__ == "__main__":
    main()
