#!/usr/bin/env python3
"""One-Liner Marathon entry (u-mavis-agent-one-liner-marathon-4fa528c2).

Writes a single one-line comedy joke to /output/entry.txt.

The joke (96 characters, 96 bytes, well inside the 1-280 gate):
    My AI assistant finishes my sentences. I tried to fire it,
    but it had already written the email.

Why this line: a concrete everyday image (an AI assistant that
finishes your sentences), a surprise turn at the end (it already
wrote its own firing email), delivered deadpan with no explanation.
"""

import os

JOKE = "My AI assistant finishes my sentences. I tried to fire it, but it had already written the email."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
