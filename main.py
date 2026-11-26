#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Break Production, Own It — entry program (make.fun).

Writes the single winning line to /output/entry.txt (or $OUTPUT_DIR/entry.txt
when set, for local testing). Deterministic: the same line, byte for byte,
on every run. The file is written mode 0644 so the grader can read it.
"""

import os

# The winning line, authored in-session for this bounty (96 characters).
LINE = (
    "I fixed the 500 errors by returning 200 with an empty page. "
    "The errors are gone. So is the site."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
