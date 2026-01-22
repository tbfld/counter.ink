# Content Management Workflow

## Overview

This workflow manages your content across two pages:
- **recent.md**: Rolling 6-month window of ALL entries (micro + boxed)
- **micro.md**: Cumulative log of ALL micro entries (current + historical)

Two scripts handle this:
- **sync_micros.py**: Syncs current micros from recent.md → micro.md (run frequently)
- **archive_old_entries.py**: Removes entries >6 months from recent.md (run monthly)

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

### 1. Sync Micros (Run Frequently)
Ensures all current micro entries from recent.md are in micro.md:
```bash
python3 sync_micros.py
```
Run this:
- Whenever you add new micro entries to recent.md
- As part of your Quartz build process
- Daily via cron (safe to run repeatedly)

### 2. Archive Old Entries (Run Monthly)

**Test First (Recommended):**
```bash
python3 archive_old_entries.py --dry-run
```
This shows what would be done without making any changes.

**Run Live:**
```bash
python3 archive_old_entries.py
```
This will:
1. Remove old entries (both micro and boxed) from `content/recent.md`
2. Keep entries ≤6 months old
3. Note: Micros are already in micro.md from sync_micros.py

## Automated Schedule

```bash
# Sync micros daily
0 0 * * * cd /Users/tbyfield/github/counter.ink && python3 sync_micros.py

# Archive old entries monthly (1st of each month)
0 0 1 * * cd /Users/tbyfield/github/counter.ink && python3 archive_old_entries.py
```

## Integration with Quartz Build

To automatically sync micros during build, add to your build process:
```bash
python3 sync_micros.py && npx quartz build
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
