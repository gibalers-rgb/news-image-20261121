# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/gibalers-rgb/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/gibalers-rgb/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One image that sums up the world news of Saturday, 21 November 2026: a
newspaper front page led by the day's biggest story — Russian Kh-101
missiles landing in NATO member Poland during the war's largest barrage on
Ukraine (400+ drones, 110+ missiles, 8 killed), with PM Tusk calling it an
intentional provocation and NATO chief Rutte calling it a "grave violation".
Five more stories from five other regions and fields fill the page: tankers
hit in the Strait of Hormuz, the Nasdaq erasing its 2026 gains, a strong
earthquake in central Peru, Mexico's army capturing FBI most-wanted cartel
boss "El Chapo Isidro", and the EU–Indonesia trade deal after a decade of
talks. The image is drawn once (AI illustration + sharp rendered text) and
the program copies it to the output, byte for byte, every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

This writes `out/entry.png` (1024×1024 PNG, under 1 MiB) — the whole entry.

## How the image was made

`compose.py` builds `entry.png`: it takes the AI-generated hero illustration
in `assets/` (a cruise missile over south-east Poland at night, no text) and
lays out the masthead, date, lead story and five story cards with PIL, so
every word is crisp and legible. Rebuild it with `python3 compose.py`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
