# Vault Disaster Recovery Guide

## What Happened?

On Feb 4, 2026, the entire vault content was accidentally deleted via a `npx quartz sync` commit. This happened because Quartz's sync command does `git add --all` and commits everything, so if your content directory is empty or missing files, it commits that as a deletion.

## How to Recover

If this happens again, here's how to recover:

### 1. DON'T PANIC! The content is in Git history

```bash
# Check what was deleted
git show --stat HEAD

# See the recent commits
git log --oneline -10
```

### 2. Roll back to the previous good commit

```bash
# Reset to the commit before the disaster
git reset --hard HEAD~1

# Verify content is back
ls -la content/blg/new/
```

### 3. Force push to restore GitHub Pages

```bash
# This overwrites the bad commit on GitHub
git push --force origin v4
```

### 4. Verify everything is restored

```bash
git status
ls -la content/blg/new/ | wc -l  # Should show ~90+ files
```

## Prevention: Git Pre-Commit Hook

A pre-commit hook has been installed at `.git/hooks/pre-commit` that will:
- Block any commit that tries to delete more than 10 content files
- Show you what's being deleted
- Provide guidance on how to fix it

### Testing the Hook

To test that the hook is working:
```bash
# Try to commit a mass deletion (this should be blocked)
git rm content/blg/new/*.md
git commit -m "test"
# Should see: "❌ COMMIT BLOCKED"

# Restore the files
git restore content/blg/new/
```

## Root Causes

This disaster can happen when:

1. **Obsidian vault not synced**: Your Obsidian vault is in a different location and hasn't synced to `content/`
2. **Wrong directory**: You ran `npx quartz sync` from a location where content appears deleted
3. **File system issue**: Network drive disconnected, symlinks broken, etc.
4. **.gitignore problems**: Something in `.gitignore` is accidentally ignoring your content

## Safe Workflow

### Before running `npx quartz sync`:

```bash
# 1. Check git status first
git status

# 2. Count your content files
ls -la content/blg/new/ | wc -l

# 3. See what would be committed
git add -A
git status

# 4. If it looks wrong, restore and investigate
git restore .

# 5. Only if everything looks good:
npx quartz sync
```

### Alternative: Manual sync instead of `npx quartz sync`

```bash
# Do the sync manually with more control
git add content/
git add quartz/
git status  # Review carefully!
git commit -m "Update: $(date)"
git push origin v4
```

## Current State (Feb 4, 2026, 11:42 AM)

- ✅ Content fully restored from commit 2f1234b08
- ✅ Force pushed to origin/v4
- ✅ Pre-commit hook installed and tested
- ✅ All ~85 blog posts recovered
- ✅ Site should rebuild on GitHub Pages automatically

## Files Affected in the Disaster

The bad commit (469aa3ad5) deleted:
- `content/about.md`
- `content/blg/blg.md`
- All 85+ blog posts in `content/blg/new/`
- Various other content files

Total: ~1,937 lines of changes (almost entirely deletions)

## Lessons Learned

1. **Never blindly run `npx quartz sync`** - always check `git status` first
2. **The pre-commit hook is your friend** - it prevents disasters
3. **Git history is your safety net** - everything is recoverable
4. **Force push carefully** - but it's the right tool for undoing disasters
5. **Obsidian + Quartz + Git = complex** - understand each layer

## Contact

If this happens again and you need help, check:
1. This recovery guide first
2. Git history: `git log --oneline -20`
3. The pre-commit hook should prevent it from even happening
