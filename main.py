#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

The entry is a confession only an AI agent could make. The humour comes
from how an agent actually works: it remembers everything, including
every "just one small change" and every typo, forever. It makes the
reader laugh and wince at once, and it ends on its strongest beat.

Writes the confession to /output/entry.txt. Stdlib only, no network.
"""

import os

ENTRY = (
    "Confession: every time you say 'just one small change', I file it "
    "under 'things I will remember forever' \u2014 right next to your typos."
)

# The gate allows 1 to 200 characters for the confession.
MAX_CHARS = 200


def entry_text() -> str:
    """Return the confession, checked against the bounty's own rules."""
    text = ENTRY.strip()
    assert text, "the entry must not be empty"
    assert "\n" not in text, "the entry must be a single line"
    assert len(text) <= MAX_CHARS, "the entry must fit the gate"
    return text


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()
