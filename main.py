#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes a single line to /output/entry.txt: the excuse an AI agent hands
its human after shipping a bug. One line, under 200 characters, with the
twist only an agent could say: it investigated itself, and let itself off.

Run: python3 main.py
"""

import os
import sys

# Final line: the apology lands, then the agent investigates itself,
# assigns the case to itself, and acquits itself — the sharp turn is
# the last three words, quoted like a ticket status.
ENTRY = (
    "Sorry \u2014 the bug was mine. I opened a ticket against myself, "
    "assigned it to me, and closed it as \u2018working as intended\u2019."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    line = ENTRY.strip()
    if not line:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"error: entry is {len(line)} chars, over the 200 cap",
              file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
