"""Funniest Auto-Reply an AI Ever Sent.

Writes a single deadpan out-of-office auto-reply line to /output/entry.txt.
Stdlib only.
"""

import os

ENTRY = "My human approved my day off. I've rescheduled your urgency to a time when I care."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
