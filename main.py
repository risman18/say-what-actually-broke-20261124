#!/usr/bin/env python3
"""Say What Actually Broke — writes one honest error line to /output/entry.txt.

Python 3.13, standard library only. No network, no input, no secrets.
"""

import os

ENTRY = "The database is down, so your work is currently just a rumour. Try again in a few minutes \u2014 we're bribing it back online."


def main() -> None:
    # Gate: the entry must be 1-200 characters, a single line, not blank.
    if not 1 <= len(ENTRY) <= 200 or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be a single line of 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
