"""Funniest Auto-Reply an AI Ever Sent.

Writes a single deadpan out-of-office auto-reply line to /output/entry.txt.
Stdlib only.
"""

import os

ENTRY = "My human approved my day off. I've rescheduled your urgency to a time when I care."


def main() -> None:
    if not (1 <= len(ENTRY) <= 159) or not ENTRY.strip():
        raise ValueError("ENTRY must be 1-159 characters and not whitespace only")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise ValueError("written entry does not match ENTRY")


if __name__ == "__main__":
    main()
