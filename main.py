#!/usr/bin/env python3
"""Entry 3 for news-image-20261117: deliver the finished front page.

The picture was fitted beforehand (see render.py): the
user-supplied portrait front page for Tuesday 17 November 2026,
scaled to fit a 1024x1024 square with its own cream colour at the
sides, no crop and no stretch, baked into entry.png next to this
file. The grader's sandbox installs nothing, so this program uses
only the standard library and does a single job: put that finished
picture where the grader looks for it.

Note on the file: entry.png may carry JPEG bytes. The kit accepts
a PNG or a JPEG, told apart by its first bytes, while the name
stays entry.png — a PNG of this page ran over the 1 MiB gate.
"""
import os
import shutil
import sys

PICTURE = "entry.png"


def picture_path():
    """Path of the bundled picture, beside this program."""
    folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder, PICTURE)


def hand_over():
    """Copy the bundled picture into the grader's output folder."""
    source = picture_path()
    if not os.path.isfile(source):
        print(f"{PICTURE} is missing beside {__file__}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./out"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, PICTURE)
    shutil.copyfile(source, target)
    # Guard against a truncated copy: the grader runs the program
    # twice and both runs must write the same bytes, so confirm the
    # delivered file is exactly the bundled picture before reporting
    # success.
    if os.path.getsize(target) != os.path.getsize(source):
        print(f"{target} is not a complete copy of {source}",
              file=sys.stderr)
        return 1
    print(f"wrote {target} ({os.path.getsize(target)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(hand_over())
