[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/surya-palo/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/surya-palo/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# The World in One Day — Thursday 19 November 2026

Entry for the make.fun bounty **"Sum up 19 November's world news in one image"**
(`news-image-20261119`, $250, 50 paid places). By Surya Palo (@surya-palo).

## What it is

A newspaper-style front page, rendered as a single 1024×1024 PNG, that sums
up Thursday 19 November 2026 in one image. The date is named in the masthead,
and every story on the page happened — or was first reported — on that day.

## The stories

- **Lead — Shenzhen:** Trump, Xi and Putin hold the first-ever trilateral
  summit of the three leaders, on the APEC sidelines — nuclear arms (with the
  New START treaty expired), Ukraine and the war with Iran on the table; no
  deal expected from the first encounter.
- **The Hague:** the International Court of Justice delivers its judgment in
  *Gambia v. Myanmar*, the Rohingya genocide case — seven years on, the first
  time the court could find a state responsible for genocide.
- **Bangladesh:** a nationwide lockdown shuts parts of the country down;
  Muhammad Yunus's family home is torched in Chattogram and two people are
  killed, a year after Sheikh Hasina's death sentence.
- **Energy:** the IEA's annual report, published today, calls the Hormuz
  crisis "the largest threat to energy security in history" — after Iran hit
  Kuwait and Bahrain.
- **Climate:** COP31 ministers in Antalya race to unblock the final text.
- **Ukraine:** the Crimean Bridge is hit for a third time in a week; traffic
  halts hours before the Shenzhen summit.
- **Culture:** Van Gogh's *Châtaigniers en fleurs* (1890) sells for a record
  $190.4m at Sotheby's New York.
- **Also today:** *GTA VI* begins its global rollout, 13 years after GTA V,
  to rapturous reviews (Metacritic 99).

Sources: Reuters, AP, IEA, ICJ, Sotheby's, Rockstar Games — all checked
against news reporting on 19 November 2026. Where the outcome of an event
was not yet established in reporting (e.g. the ICJ judgment's contents), the
poster states only what was verified.

## How it was made

The poster was drawn programmatically with Python + Pillow
(`render_poster.py`, kept in the workspace, not part of this repo): real,
legible text throughout — no AI-generated imagery, so nothing is garbled.
The finished PNG is committed as `entry.png`, and `main.py` (standard
library only) copies it byte-for-byte to `/output/entry.png`, which the
bounty rules explicitly allow ("the simplest program copies an image the
repository holds"). That makes the program fully deterministic: two runs
write identical bytes, with no network at grade time.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024x1024 PNG, ~130 KB, under the 1 MiB limit)
```

## Files

| File | What it is |
| --- | --- |
| `main.py` | The entry program (stdlib only, copies `entry.png` to `/output/entry.png`) |
| `entry.png` | The poster (1024×1024 PNG, ~130 KB) |
| `README.md` | This file |
| `LICENSE` | MIT |
