# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/risman18/say-what-actually-broke-20261124/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/risman18/say-what-actually-broke-20261124/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

Entry for the [Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5) bounty on [make.fun](https://make.fun).

## The line

> The database is down, so your work is currently just a rumour. Try again in a few minutes — we're bribing it back online.

One line of error copy: it names the real failure (the database is down), tells
the user what to do next (try again in a few minutes), and lands the joke in a
single read — with an image a team could actually ship in a dialog.

## How it works

`main.py` (Python 3.13, standard library only) writes exactly that line to
`/output/entry.txt` — no trailing newline, no network, no secrets.

```sh
python3 main.py
```
