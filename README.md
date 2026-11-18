# The World Today — Tuesday 17 November 2026 (entry 3)

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/tapetelo/news-image-20261117-v3/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/tapetelo/news-image-20261117-v3/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

A one-page newspaper front page summing up Tuesday 17 November 2026 in a
single image, for the make.fun competition `news-image-20261117`
(@tapetelo). Entry 3 of 3 — the user-supplied front page, fitted to the
1024×1024 gate with no crop and no stretch.

## What's on the page

- **Masthead** — "Tuesday 17 November 2026", "32 STORIES • ALL FROM
  TUESDAY".
- **3 hero stories** — Ukraine strikes the Kerch bridge again; Iran
  launches a third drone attack on a US radar in Bahrain; Trump opens
  his Asia tour in Manila with the Quad leaders.
- **10 medium stories** — Nvidia beats forecasts; Congo Ebola outbreak
  hits 11,254 cases; outages keep hitting US systems; opposition wins
  the Knesset speaker vote; Mongolia's president announces resignation;
  police seize opposition channel Sözcü TV; Serbia's new parliament
  opens; Eurozone inflation hits 4.0% in October; data centres draw
  82 TWh a year in the US; Israel is behind on Gaza ceasefire aid.
- **Where it happened** — a map pinning stories 1 to 13, and "ALSO ON
  TUESDAY 17 NOVEMBER", briefs 14 to 32.

## How it was built

`entry.png` (1024×1024; JPEG bytes — the kit allows PNG or JPEG,
told apart by first bytes, name stays `entry.png`, since a PNG of
this page was over the 1 MiB gate) was fitted locally by `render.py`
with Pillow: the portrait source (2200×2476) scaled to height 1024
(910 wide, aspect kept) and centred on a square of the page's own
cream background, so the whole page stays fully in frame. No text
was added and none of the page's text was retyped.

The graded program, `main.py`, uses only the Python standard library
(`os`, `shutil`, `sys`). The grader runs in an environment with nothing
installed, so `main.py` never imports Pillow: it simply copies the
pre-rendered `entry.png` from beside itself into
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `./out`).

## Reproduce

```sh
python3 render.py        # regenerates entry.png (needs Pillow, local only)
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
