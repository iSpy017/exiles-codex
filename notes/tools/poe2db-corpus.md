# PoE2DB local corpus (crawl of 2026-11-23)

Status: done. Default first source for game-data lookups (David's preference, 2026-11-23: PoE2DB is the fullest and usually most accurate source).

## What it is
- A full crawl of PoE2DB's English pages (poe2db.tw/us/...), converted to plain text: 16,759 pages, ~102 million characters. Each table row is kept on one line, with cells separated by ` | `.
- Crawled 2026-11-23 by David and a friend on two PCs, with a fill-in run for gaps. Game data is from the 0.5.x era, plus whatever 1.0 pages PoE2DB had by that date (e.g. `Version_1.0.0`).
- Skipped on purpose: other languages; robots.txt-blocked paths (`/*/marked`, `/*/markdown_history`); URLs with `?query` strings (incl. `markdown_raw?oldid=` wiki-text pages); about 1,100 cosmetic pages (skins, pets, weapon/character effects, hideout decorations, stash-tab shop pages). 238 links were dead on PoE2DB's side (235 × 404, 3 × 403).
- Known empty: the passive-tree and atlas-tree pages, which PoE2DB draws with JavaScript. Use the RePoE game data for the trees ([[02-sources]]).
- About 3,300 pages hold under 300 characters of text: mostly stubs, NPC dialogue or cosmetic leftovers.

## Where it lives
- On David's PC: `C:\PoE2\poe2db\poe2db_corpus_2026-11-23.tar.xz` (4.9 MB; 150 MB unpacked). Raw HTML zips sit next to it (`…_part01.zip` = David's half, `…_part02.zip` = his friend's half, `…_fill_part01.zip` = gap fill).
- Each text file starts with `URL:`, `TITLE:` and `SOURCE:` lines. `_index.tsv` maps URL → file → title → character count.
- Crawler: `C:\PoE2\poe2db\poe2db_crawl.py` (resumable; `--shard K/N` + `--handoff`/`--import` to split across PCs; `--fill FILE` for gap runs; `--fresh` for a new dated copy).

## How Claude uses it (each session)
1. Stage `poe2db_corpus_2026-11-23.tar.xz` from the connected folder and unpack it in the workspace (seconds).
2. Search with grep / Python over the text files. Cite as: [PoE2DB <Page>](https://poe2db.tw/us/<Page>), tier 2, crawl 2026-11-23.
3. Use the browser or web fetch only for what PoE2DB doesn't have (official GGG pages, poe2wiki version history, prices).

## Refresh plan (1.0)
- When the 1.0 patch notes drop: David runs `py poe2db_crawl.py --fresh` (optionally split with his friend via `--shard`), then Claude builds a new corpus file with the date in its name. Keep the 2026-11-23 corpus as the 0.5 baseline for comparisons.
