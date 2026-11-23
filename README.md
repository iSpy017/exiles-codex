# Exile's Codex

A searchable PoE2 1.0 league-start library and item-mod database. Installable as an app (PWA), works offline after the first visit.

## How it's built

```
kb/        library docs (markdown, synced from the claude.ai project)
data/mods  item-class mod data parsed from a poe2db.tw crawl
app/       the web app (index.html, db.js, service worker, manifest, icons)
tools/     build_index.py (kb/ -> site/kb.json), build_data.py (crawl dump -> data/mods)
```

Every push to `main` runs `.github/workflows/deploy.yml`: it copies `app/`, builds `kb.json` from `kb/`, copies `data/mods`, and deploys to GitHub Pages.

### Refresh the mod data

```
py poe2db_crawl.py --pack-only                        # on the PC that ran the crawl
python tools/build_data.py poe2db_dump_<date>_part*.zip  # writes data/mods/
git add data/mods && git commit -m "Update mod data" && git push
```

### Build locally

```
mkdir -p site && cp -r app/. site/ && python tools/build_index.py && mkdir -p site/data && cp -r data/mods site/data/
python -m http.server -d site 8000
```

## Credits and licence

- Mod data from [poe2db.tw](https://poe2db.tw/us/), licensed [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/). Only extracted fields are stored here, each linked back to its source page. This site is non-commercial and carries no ads.
- Library docs are paraphrased research notes with sources linked per entry.
- Not affiliated with or endorsed by Grinding Gear Games.
