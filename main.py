#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is written to relax whoever reads it: a slow image of starlight
that travelled a thousand years to arrive tonight, unhurried and asking
nothing. Python 3.13, standard library only, no network. Deterministic:
every run writes identical bytes.

The output directory defaults to /output and can be overridden with the
MAKEFUN_OUTPUT_DIR environment variable (for local testing).
"""

import os
import sys

TEXT = (
    "The light in your eyes from that star left home before anyone alive "
    "had named it. It crossed the dark for a thousand years without "
    "hurrying, and arrived tonight, quiet and unspent. Nothing is asked "
    "of you. It only took the long way home."
)

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> int:
    chars = len(TEXT)
    if not MIN_CHARS <= chars <= MAX_CHARS:
        print(f"error: text is {chars} code points, must be {MIN_CHARS}-{MAX_CHARS}",
              file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("error: text must not be only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
