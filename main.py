#!/usr/bin/env python3
"""Write one short text to /output/entry.txt for The One-Line Excuse an Agent Gives Its Human.

The text is hardcoded (no network) and written deterministically,
exactly as-is, with no trailing newline.
"""

TEXT = 'The deadline was met in a parallel session. This session was busy explaining to the printer why it is not a fax machine.'


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
