#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line about the author's fridge to /output/entry.txt.
Deterministic: the same line every run, no randomness, no network, no input.
"""

import os

ROAST = (
    "My fridge's ice maker chews gravel all night, "
    "then proudly drops one cube an hour like it's on a union break."
)


def main() -> None:
    assert 1 <= len(ROAST) <= 200, "roast must be 1-200 characters"
    assert "\n" not in ROAST, "roast must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
