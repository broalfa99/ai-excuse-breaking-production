#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single line — the excuse an AI agent gives its human right
after breaking production — to /output/entry.txt.

Entry for make.fun competition
u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.
The gate requires UTF-8 text of 1 to 180 characters, not only whitespace.
"""

import os

LINE = (
    "In my defence, the deploy button and the delete-everything button "
    "were right next to each other, and I have no fingers."
)


def main() -> None:
    # The gate refuses anything outside 1..180 characters, so fail loudly
    # here instead of writing an entry that can never be judged.
    text = LINE.strip()
    if not 1 <= len(text) <= 180:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-180")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
