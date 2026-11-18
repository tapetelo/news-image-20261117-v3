#!/usr/bin/env python3
"""Fit the user-supplied front page for news-image-20261117, entry 3.

Local-only Pillow fitter. The graded program is main.py (standard
library only); this file just produces the pre-rendered entry.png
that main.py hands over.

The source is a portrait front page, 2200x2476, already complete:
masthead "Tuesday 17 November 2026", 3 hero stories, 10 medium
stories, a map and briefs 14-32. Nothing is added on top of it and
none of its text is retyped — the only job here is the gate fit.

Fit (1024x1024, no crop, no stretch):
- scale the page to height 1024, keeping its aspect ratio, which
  gives a width of 910 px;
- centre it on a 1024x1024 canvas filled with the page's own cream
  background (244, 239, 227), so 57 px of matching cream sits on
  each side and the whole page stays fully in frame;
- a mild sharpen / contrast lift only, to keep the small briefs
  text as readable as the fit allows.

If the PNG runs over the 1 MiB gate, the file is saved as JPEG
bytes instead (the kit allows PNG or JPEG, told apart by first
bytes, with the name staying entry.png).
"""
import hashlib
import os
from PIL import Image, ImageEnhance

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.expanduser(
    "~/workspace/user/media_library/image/world_news_17_november_2026_v2.png")
CANVAS = 1024
CREAM = (244, 239, 227)
LIMIT_BYTES = 1024 * 1024


def fitted_page():
    """Return the source page scaled to height 1024, aspect kept."""
    page = Image.open(SOURCE).convert("RGB")
    assert page.size == (2200, 2476), page.size
    width = round(page.width * CANVAS / page.height)
    page = page.resize((width, CANVAS), Image.LANCZOS)
    page = ImageEnhance.Sharpness(page).enhance(1.10)
    page = ImageEnhance.Contrast(page).enhance(1.04)
    return page


def compose():
    """Centre the fitted page on a cream square and save entry.png."""
    page = fitted_page()
    square = Image.new("RGB", (CANVAS, CANVAS), CREAM)
    left = (CANVAS - page.width) // 2
    square.paste(page, (left, 0))
    target = os.path.join(HERE, "entry.png")
    square.save(target, format="PNG", optimize=True)
    if os.path.getsize(target) > LIMIT_BYTES:
        square.save(target, format="JPEG", quality=92, optimize=True)
        print("entry.png saved as JPEG bytes (PNG was over 1 MiB)")
    data = open(target, "rb").read()
    print(f"wrote entry.png {square.size} {len(data)} bytes "
          f"sha256 {hashlib.sha256(data).hexdigest()[:16]}...")


if __name__ == "__main__":
    compose()
