# Exile's Codex

A searchable PoE2 1.0 league-start library and item-mod database. Installable as an app (PWA), works offline after the first visit.

## How it's built

```
kb/            library: one topic per file, structured entries (format: SCHEMA.md). Source of truth.
sources.yaml   source registry ([Sxxx] ids); poe2db:<Page> refs point at the PoE2DB crawl
conflicts.yaml source disagreements, both sides kept
CHANGELOG.md   pre-migration history; after 2026-11-27 see git log
data/mods      item-class mod data parsed from a poe2db.tw crawl
data/prices    dated price snapshots (append-only)
data/uniques.csv, data/unique_mods.csv, data/poe2db/  generated from the PoE2DB crawl
notes/         other notes and files kept as-is
app/           the web app (index.html, db.js, service worker, manifest, icons)
tools/         lint.py, kbschema.py, kbsearch.py, build_index.py (kb/ -> site/kb.json, index.jsonl, coverage.json/.html), build_data.py,
               gen_uniques.py + gen_poe2db_refs.py (crawl -> data/), crawl_diff.py (1.0 refresh worklist)
legacy/        frozen copy of the old claude.ai Project docs (tag pre-migration)
```

Every push to `main` runs `.github/workflows/deploy.yml`: lint (errors block the deploy), copy `app/`, build `kb.json` / `index.jsonl` / `coverage.json` from `kb/`, copy `data/mods`, deploy to GitHub Pages.

### Refresh the mod data

```
py poe2db_crawl.py --pack-only                        # on the PC that ran the crawl
python tools/build_data.py poe2db_dump_<date>_part*.zip  # writes data/mods/
git add data/mods && git commit -m "Update mod data" && git push
```

### Build locally

```
python tools/lint.py . && mkdir -p site && cp -r app/. site/ && python tools/build_index.py && mkdir -p site/data && cp -r data/mods site/data/
python -m http.server -d site 8000
```

## Credits and licence

- Mod data from [poe2db.tw](https://poe2db.tw/us/), licensed [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/). Only extracted fields are stored here, each linked back to its source page. This site is non-commercial and carries no ads.
- Library docs are paraphrased research notes with sources linked per entry.
- Not affiliated with or endorsed by Grinding Gear Games.
