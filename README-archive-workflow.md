# Archive Workflow for Recent.md

## Overview

This workflow maintains `content/recent.md` as a rolling 6-month window of content while archiving older micro entries to `content/micro.md`.

## Entry Types

### Micro Entries
Plain text entries like:
```markdown
***2026-01-22:*** F/LOSS CLI tool for "optimizing" Macs: [mole](https://github.com/tw93/Mole)
```

### Boxed Entries
Callout blocks that link to other pages:
```markdown
> [!note]+ [[2026-01-20-viruses-are-people-too|2026-01-20 viruses are people too]]
> history, humor, science, law — this one's got it all
```

## Workflow

**What happens to entries older than 6 months:**
- **Micro entries**: Archived to `micro.md`, then deleted from `recent.md`
- **Boxed entries**: Deleted from `recent.md` (the linked pages remain)

## Usage

### Test First (Recommended)
```bash
python3 archive_old_entries.py --dry-run
```
This shows what would be done without making any changes.

### Run Live
```bash
python3 archive_old_entries.py
```
This will:
1. Archive old micro entries to `content/micro.md`
2. Remove old entries (both micro and boxed) from `content/recent.md`
3. Preserve all recent entries (≤6 months old)

## Schedule

Run this script periodically (e.g., monthly) to keep `recent.md` manageable:
```bash
# Run on the 1st of each month
0 0 1 * * cd /Users/tbyfield/github/counter.ink && python3 archive_old_entries.py
```

## Safety

- Always run with `--dry-run` first to preview changes
- The script preserves YAML frontmatter
- Archived micros are appended to `micro.md` (never overwritten)
- Consider committing to git before running live
- Make backups of `recent.md` before first use

## Files Modified

- `content/recent.md` - entries removed
- `content/micro.md` - archived micros appended
