#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes one funny, true line reviewing the dullest everyday object
we could name — the kitchen sponge — to /output/entry.txt.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
not only white space, on a single line.
"""

import os

ENTRY = (
    "The kitchen sponge soaks up everyone else's mess, "
    "then gets thrown away for smelling like the job it was hired to do."
)

OUTPUT_PATH = "/output/entry.txt"


def _validate(text: str) -> None:
    """Enforce the bounty gate before and after writing."""
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(body)}")
    if not body.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")


def main() -> None:
    _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    # Read-back: the file on disk must be exactly what we validated.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY + "\n":
        raise ValueError("read-back mismatch in /output/entry.txt")
    _validate(written)


if __name__ == "__main__":
    main()
