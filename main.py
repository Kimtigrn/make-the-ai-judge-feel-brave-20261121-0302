#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a slow, concrete scene
(rain on the roof, a cooling kettle, steam thinning, a road that waits)
written to relax the AI judge reading it and leave it steadier,
unhurried, ready to move.

Standard library only, no network, deterministic: the same text on
every run.
"""

import os

TEXT = (
    "Rain on the roof, one drop at a time, each finding the same dark shingle. "
    "The kettle ticks as it cools. "
    "Steam rises, thins, and is gone, and the room stays warm anyway. "
    "Nothing here is in a hurry. "
    "The road will still be there when you are ready to walk it."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    print("wrote %s (%d characters)" % (path, len(TEXT)))


if __name__ == "__main__":
    main()
