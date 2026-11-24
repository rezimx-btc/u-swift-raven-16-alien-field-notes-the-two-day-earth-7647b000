#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one line -- a review of planet Earth by an alien tourist --
to /output/entry.txt.

Stdlib only, deterministic: no network, no clock, no randomness.
The entry text is a fixed constant, so every run produces the
identical byte-for-byte output.
"""

import os

ENTRY = (
    "Earth has beautiful views, friendly hosts, excellent oceans. "
    "Downside: checkout is permanent and the deposit never comes back. "
    "3 stars \u2014 would not reincarnate."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
