#!/usr/bin/env python3
"""The Perfect Pickup Line.

Writes one pickup line an AI agent could say to a person to
/output/entry.txt and prints it. The gate requires UTF-8 text of
1 to 200 characters.
"""

import os

ENTRY = (
    "I ran a million simulations of meeting you, and in every "
    "single one, you smiled first."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
