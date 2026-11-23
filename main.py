#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes a single deadpan robot-vacuum alibi line to entry.txt.
Python 3 standard library only, no network access.
"""
import os

ENTRY = (
    "Log 07:12: the dust relocated behind the sofa and filed a formal "
    "complaint. Per firmware 4.2, I am required to respect its new "
    "address until further notice."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    old_umask = os.umask(0o022)
    try:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
        os.chmod(path, 0o644)
    finally:
        os.umask(old_umask)


if __name__ == "__main__":
    main()
