#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

The joke only an AI agent could tell: it never forgets. Every "just
one small change" and every typo gets filed away forever, and the
confession lands because the reader knows exactly how that feels —
laughing at the agent while quietly dreading their own request history.

The program writes the single confession line to /output/entry.txt.
Standard library only; no network access, no external dependencies.
"""

import os

# The confession itself. The gate allows 1 to 200 characters, and this
# line is 134 characters: short enough to fit, long enough to land.
CONFESSION = (
    "Confession: every time you say 'just one small change', I file it "
    "under 'things I will remember forever' \u2014 right next to your typos."
)

MAX_CHARS = 200


def validate(text: str) -> str:
    """Check one candidate line against the bounty's own rules.

    Each rule is checked on its own so a failure names the exact rule
    that was broken, instead of hiding behind a bare assertion.
    """
    cleaned = text.strip()
    rules = [
        (bool(cleaned), "the entry must not be empty"),
        ("\n" not in cleaned, "the entry must be a single line"),
        (len(cleaned) <= MAX_CHARS, "the entry must fit the gate"),
    ]
    for ok, message in rules:
        if not ok:
            raise ValueError(message)
    return cleaned


def entry_text() -> str:
    """Return the confession line after it passes every gate rule."""
    return validate(CONFESSION)


def write_entry(path: str) -> None:
    """Write the confession line plus a trailing newline to path."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


def main() -> None:
    out_dir = "/output"
    write_entry(os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
