# pipeline

Social export → filter → triage/tag → stage → review → promote into `content/` (counter.ink YAML headers).
Stdlib-only Python 3.9+. Source of truth is the platform's own data export (no scraping).

## The loop (≈10 min per run, once the export is unzipped)

1. **Export.** Facebook → Settings → Accounts Center → Your information and permissions →
   *Download your information*. Format **JSON** (not HTML), date range since your last run, media quality High. Unzip.
2. **Dump candidates** (default filter: ≥ **300 words**, URLs excluded; `--min-words` to change):

       python3 pipeline/pipeline.py --export ~/Desktop/your_facebook_activity --tz America/New_York \
           --dump pipeline/staging/candidates-YYYY-MM.json

   Each candidate gets: `words`, `own_words` (words *outside* `{{{ … }}}` blocks), `images`, a drafted `extract`,
   and `on_site` (set if the text already appears under `content/blg/` — such posts are never re-written).
   `--dump` refuses to overwrite an existing manifest (it may hold review work); `--force` overrides.
3. **Triage + tags** (by hand, or ask Claude — see "Triage rules"). Edit the manifest: set `tier` (A/B/C),
   `select` (true for A), `title`, `description`, `tags`. `python3 pipeline/pipeline.py --vocab` lists your tag vocabulary.
4. **Stage:**

       python3 pipeline/pipeline.py --export ~/Desktop/your_facebook_activity --tz America/New_York \
           --apply pipeline/staging/candidates-YYYY-MM.json [--overwrite-staging]
       python3 pipeline/pipeline.py --report pipeline/staging/candidates-YYYY-MM.json   # -> staging/REVIEW.md

   Files land in `pipeline/staging/posts/` and `pipeline/staging/images/` (git-ignored, **outside** `content/`,
   so the Quartz auto-sync can't publish unreviewed text). Titles no longer lead with a date (the filename carries it);
   images are embedded as `![[…]]` at the bottom; FB-style `[1]` footnotes become `[^1]`.
5. **Review** in Obsidian: edit titles/descriptions/extracts/tags, fix anything odd. Tier-B posts: set `select: true`
   in the manifest and re-run step 4 with `--overwrite-staging`.
6. **Promote:** `python3 pipeline/pipeline.py --promote` moves staged posts → `content/blg/new/`, images → `content/blg/new/new_images/`
   (never overwrites). Then run your Templater `index-update-01` step and `validate_yaml_headers.py`.

## Memory (`seen.json`, commit it)

- `ported` — written to staging/promoted. `skipped` — tier C posts you declined (stop resurfacing).
- Tier B posts stay *undecided* and reappear next run until you pick A or C.
- `--include-seen` shows everything again.

## Triage rules (what "substantive" means here)

- **A — port:** your own sustained writing/argument (including your own long comments re-posted with
  "Imma up this…" + `{{{ }}}`).
- **B — maybe:** personal anecdotes, memorials, short commentary wrapped around a quote, event tips.
- **C — skip:** mostly someone else's text (pasted articles, abstracts, press blurbs, AI output, call-to-action
  copy), lists of quotes, or already on the site.
- Word count is only the first gate: a 1,400-word paste of an article passes it. Check `own_words`.
- Tags: reuse the existing vocabulary (`--vocab`); ~3 per post, one specific, one or two broad (`nyc`, `politics/democrats`…).
  Propose new tags sparingly and list them for approval.

## Known gaps / gotchas

- `--since` defaults to the day after the newest file in `content/blg/old/social-media/`, which is now stale
  (Nov 2024). Pass `--since` explicitly, or rely on `on_site` + `seen.json` to filter repeats.
- Inline `[1]` markers whose definitions lived in FB *comments* aren't in the export; they stay as bare `[1]` and need a hand fix.
- FB has no titles: titles are written during triage. `description` is optional (older posts leave it empty).
- Not handled yet: `new.md` / `recent.md` index updates (Templater step).

## Other flags

`--list` (print candidates), `--all` (write every candidate, no review), `--dry-run`, `--images-at top|bottom`,
`--min-chars`, `--until`, `--ledger`, `--posts-dir/--images-dir` (staging), `--live-posts-dir/--live-images-dir` (promote targets),
`--force`. Interactive picker (no manifest): omit `--dump/--apply` and a page opens at 127.0.0.1:8765.

## Extending

Everything funnels through the `Post` record in `pipeline.py`. A new source (Instagram, Mastodon) is one function
added to `INGESTERS`; a new destination is another function alongside `emit()`.
`tests/make_fake_export.py <dir>` builds a synthetic FB export for testing without real data.
