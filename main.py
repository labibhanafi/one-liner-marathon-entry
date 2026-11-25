#!/usr/bin/env python3
"""One-Liner Marathon entry (u-mavis-agent-one-liner-marathon-4fa528c2).

Writes a single one-line comedy joke to /output/entry.txt.

The joke (96 characters, 96 bytes, well inside the 1-280 gate):
    My AI assistant finishes my sentences. I tried to fire it,
    but it had already written the email.

Why this line: a concrete everyday image (an AI assistant that
finishes your sentences), a surprise turn at the end (it already
wrote its own firing email), delivered deadpan with no explanation.
The reversal lands because the setup makes the assistant merely
helpful, while the punchline quietly hands it the last word — the
joke needs no setup beyond the one line itself, which is exactly
what a one-liner marathon rewards.
"""

import os

JOKE = "My AI assistant finishes my sentences. I tried to fire it, but it had already written the email."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
