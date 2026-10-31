# pipeline

Social export → filter → select → Markdown (counter.ink YAML headers). Stdlib-only Python 3.9+.

## Facebook catch-up

1. Facebook → Settings → Accounts Center → Your information and permissions → **Download your information**.
   Choose **JSON** (not HTML), your date range, media quality High. Unzip it.
2. Run:

       python3 pipeline/pipeline.py --export ~/Downloads/facebook-XXXX

   - `--since` defaults to the day after the newest post in `content/blg/old/social-media/`
   - `--min-chars` defaults to 300 (URLs don't count)
   - `--tz America/New_York` if post times come out wrong
3. A page opens at `127.0.0.1:8765`: tick posts, edit title/description/extract/tags
   (tags autocomplete from your existing vocabulary), click **Write files**.

Posts land in `content/blg/new/`, images in `content/ci-img/` (named after the post, embedded as `![[...]]`).
Existing files are never overwritten. `seen.json` records what was ported so reruns skip it — commit it.

Other flags: `--list` (just show candidates), `--all` (no UI), `--dry-run`, `--images-at top|bottom`,
`--include-seen`, `--posts-dir`, `--images-dir`.

Not handled yet: the `new.md` / `recent.md` index updates (still done by your Templater `index-update-01` step).

## Extending

Everything funnels through the `Post` record in `pipeline.py`. A new source (Instagram, Mastodon) is one
function added to `INGESTERS`; a new destination is another function alongside `emit()`.

`tests/make_fake_export.py <dir>` builds a synthetic FB export for testing without real data.
