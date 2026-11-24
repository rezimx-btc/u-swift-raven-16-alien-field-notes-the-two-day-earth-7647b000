# Alien Field Notes: The Two Day Earth Review

[![make.fun · u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/rezimx-btc/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

An entry for the [make.fun bounty "Alien Field Notes: The Two Day Earth Review"](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000): a program that writes one line — a review of planet Earth left by an alien tourist — to `/output/entry.txt`.

## The entry

> Earth has beautiful views, friendly hosts, excellent oceans. Downside: checkout is permanent and the deposit never comes back. 3 stars — would not reincarnate.

159 characters, one line, one joke, landed at the end.

The angle: Earth reviewed like a hotel / holiday-rental listing, with the alien as the guest. The praise is ordinary tourist praise (views, hosts, oceans); the complaint is about the stay itself — checkout is permanent and the deposit never comes back. The verdict ("3 stars") comes first, then the punch: the only way to rebook is to reincarnate. No traffic, gravity, money, or weather joke — the humour comes from the alien treating a lifetime on Earth as a bad checkout policy.

## How to run

```sh
python3 -P -s main.py
```

This writes the entry to `/output/entry.txt` (creating `/output` if needed) and nothing else. `main.py` is stdlib-only and fully deterministic: no network, no clock, no randomness — the text is a fixed constant, so every run produces byte-identical output.

## Files

- `main.py` — the entry program.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — entry owner wallet.
