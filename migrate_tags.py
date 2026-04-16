#!/usr/bin/env python3
"""
Tag migration script for counter.ink vault.
Remaps flat tags to hierarchical notation per the approved mapping in meta/tag-migration-mapping.md.

Usage:
    python3 migrate_tags.py --dry-run    # report changes without writing
    python3 migrate_tags.py              # apply changes

The script rewrites only files that have at least one tag change.
All other content (including all other frontmatter fields) is preserved exactly.
"""

import argparse
import os
import re
import sys
from collections import defaultdict

VAULT = os.path.join(os.path.dirname(__file__), "content")

# ─── MAPPING ────────────────────────────────────────────────────────────────
# Each entry: "flat_tag": "hierarchical/tag"
# For tags that expand to multiple: "flat_tag": ["tag/one", "tag/two"]
# For tags to drop: "flat_tag": None
# Tags not listed here are left unchanged.

MAPPING = {
    # Part 1: clear mappings to existing ontology
    "fascism":          "politics/fascism",
    "right":            "politics/right",
    "left":             "politics/leftism",
    "national":         "politics/national",
    "liberalism":       "politics/liberalism",
    "libertarianism":   "politics/libertarianism",
    "centrism":         "politics/centrism",
    "communism":        "politics/communism",
    "anarchism":        "politics/anarchism",
    "1980s":            "history/1980s",
    "1970s":            "history/1970s",
    "1960s":            "history/1960s",
    "1990s":            "history/1990s",
    "19c":              "history/19c",
    "law":              "governance/law",
    "crime":            "governance/crime",
    "corporation":      "governance/corporation",
    "institution":      "governance/institution",
    "war":              "governance/war",
    "finance":          "economics/finance",
    "academia":         "education/academia",
    "internet":         "technology/internet",
    "security":         "technology/security",
    "software":         "technology/software",
    "aviation":         "technology/aviation",
    "visualization":    "information/visualization",
    "data":             "information/data",
    # "information" stays as top-level "information" — no change needed
    "meme":             "media/meme",
    "news":             "media/news",
    "publishing":       "media/publishing",
    "advertising":      "design/advertising",
    "interface":        "design/interface",
    "literature":       "language/literature",
    "europe":           "international/europe",
    "africa":           "international/africa",
    "asia":             "international/asia",
    "theory":           "philosophy/theory",
    "space":            "science/space",
    "nature":           "science/nature",
    "sculpture":        "art/sculpture",
    "dance":            "art/dance",
    "music":            "art/music",
    "architecture":     "art/architecture",
    "society":          "culture/society",
    "pop":              "culture/pop",
    "healthcare":       "health/care",
    # "religion" stays as top-level "religion" — no change needed
    "theology":         "religion/theology",
    # "sexuality" stays as top-level "sexuality" — no change needed

    # Part 2: ontology extensions — art & visual culture
    "photography":      "art/photography",
    "film":             "art/film",
    "cinema":           "art/cinema",
    "aesthetics":       "art/aesthetics",
    "visual-culture":   "art/visual-culture",
    "image":            "art/image",
    "typography":       "design/typography",
    "graffiti":         "art/graffiti",
    "illustration":     "art/illustration",
    "performance":      "art/performance",
    "theater":          "art/theater",
    "poetry":           "language/poetry",

    # Part 2: language & rhetoric
    "trope":            "language/rhetoric",
    "idiom":            "language/rhetoric",
    "rhetoric":         "language/rhetoric",
    "satire":           "language/satire",
    "genre":            "language/genre",
    # "neologism": N — keep flat, not listed
    "metaphor":         "language/rhetoric",
    "orthography":      "language/orthography",

    # Part 2: media & journalism
    "journalism":       "media/journalism",
    "media-analysis":   "media/analysis",
    "television":       "media/tv-radio",
    "social-media":     "media/social",
    "email":            "media/email",
    "fashion":          "culture/fashion",
    "magazines":        "media/publishing",
    "video":            "media/video",

    # Part 2: politics (specific)
    "gop":              "politics/gop",
    "democrats":        "politics/democrats",
    "elections":        "politics/elections",
    # "activism": N — keep flat
    "violence":         "governance/violence",
    "corruption":       "governance/corruption",
    "military":         "governance/military",
    "police":           "governance/police",
    "policy":           "governance/policy",
    "judiciary":        "governance/judiciary",
    "jurisprudence":    "governance/law",
    "intellectual-property": "governance/ip",
    # "protest": N — keep flat
    "cryptography":     "technology/security",
    "democracy":        "politics/democracy",
    "antifascism":      "politics/antifascism",
    # "leaks": N — keep flat

    # Part 2: culture & society
    "gender":           "culture/gender",
    "race":             "culture/race",
    "labor":            "economics/labor",
    "parenting":        "culture/parenting",
    "food":             "culture/food",
    "masculinity":      "culture/gender",
    "feminism":         "politics/feminism",
    "animals":          "science/nature",
    "cartoons":         "art/cartoons",
    "humor":            "culture/humor",
    "consumerism":      "economics/consumerism",
    "class":            "politics/class",
    "ethics":           "philosophy/ethics",

    # Part 2: technology (specific)
    "computation":      "technology/computation",
    "ai":               "technology/ai",
    "device":           "technology/hardware",
    "web":              "technology/internet",
    "ui":               "design/interface",
    "algorithm":        "technology/software",
    "automation":       "technology/automation",
    "ml":               "technology/ai",
    "dataviz":          "information/visualization",
    "protocol":         "technology/internet",

    # Part 2: history & geography
    # "nyc": flat — not listed
    "uk":               "international/uk",
    "france":           "international/france",
    "usa":              "international/usa",
    "turkey":           "international/turkey",
    "south":            "international/south",
    "brexit":           "politics/brexit",
    "china":            "international/asia",
    "states":           "politics/states",

    # Part 2: health
    "covid":            "health/covid",
    "environment":      "science/environment",
    "medicine":         "health/medicine",
    "nuclear":          "governance/nuclear",
    "ecocide":          "governance/ecocide",

    # Part 5: resolved
    "nyt":              "media/news/nyt",
    "books":            "media/publishing",
    "icann":            "governance/internet",
    "sci-fi":           ["language/genre", "art/film"],  # expands to two tags
    "disciplinarity":   "education/disciplinarity",
    "real-estate":      "urbanism/real-estate",
    "intellectualism":  "culture/intellectualism",
    "cultural-commentary": "culture",
    "social-commentary":   "culture",
    "forensics":        "technology/forensics",
    "disinformation":   "politics/disinformation",
    "conspiracy":       "politics/conspiracy",
    "infrastructure":   "governance/infrastructure",
    "anthropology":     "culture/anthropology",
    "capitalism":       "economics/capitalism",
    "civil-society":    "governance/civil-society",
    "statistics":       "science/statistics",
    "cybernetics":      "technology/cybernetics",
    "cartography":      "science/cartography",

    # Part 4: drop (errors and artifacts)
    '<% tp.system.prompt("Primary tag") %>':             None,
    '<% tp.system.prompt("Secondary tag (optional)", "") %>': None,
    "#media-analysis":  None,
    "#internet":        None,
    "#media":           None,
    "#politics":        None,
    "#communication":   None,
    "#cyberspace":      None,
}


# ─── YAML TAG PARSING ───────────────────────────────────────────────────────

def parse_frontmatter(content):
    """Return (frontmatter_str, body_str) or (None, content) if no frontmatter."""
    if not content.startswith("---"):
        return None, content
    end = content.find("\n---", 3)
    if end < 0:
        return None, content
    return content[3:end], content[end + 4:]  # +4 skips \n---


def get_tags_from_fm(fm):
    """Extract list of tags from frontmatter string. Returns (tags, style) where
    style is 'list' (multiline) or 'inline' (bracket)."""
    # Multiline: tags:\n  - foo\n  - bar
    tags_block = re.search(r'(?m)^tags:\s*\n((?:[ \t]+-[ \t]+.+\n?)*)', fm)
    if tags_block:
        lines = tags_block.group(1)
        tags = []
        for line in lines.splitlines():
            tag = re.sub(r'^[ \t]+-[ \t]+', '', line).strip().strip('"\'')
            if tag:
                tags.append(tag)
        return tags, 'list', tags_block
    # Inline: tags: [foo, bar]
    inline = re.search(r'(?m)^tags:\s*\[([^\]]*)\]', fm)
    if inline:
        tags = [t.strip().strip('"\'') for t in inline.group(1).split(',') if t.strip()]
        return tags, 'inline', inline
    return [], None, None


def apply_mapping(tags):
    """Apply MAPPING to a list of tags. Returns (new_tags, changed) where
    new_tags preserves order and deduplicates."""
    new_tags = []
    changed = False
    seen = set()
    for tag in tags:
        if tag in MAPPING:
            mapped = MAPPING[tag]
            if mapped is None:
                # drop
                changed = True
                continue
            elif isinstance(mapped, list):
                # expand to multiple
                for m in mapped:
                    if m not in seen:
                        new_tags.append(m)
                        seen.add(m)
                changed = True
            else:
                if mapped != tag:
                    changed = True
                if mapped not in seen:
                    new_tags.append(mapped)
                    seen.add(mapped)
        else:
            if tag not in seen:
                new_tags.append(tag)
                seen.add(tag)
    return new_tags, changed


def rewrite_frontmatter(fm, new_tags, style, match):
    """Return updated frontmatter string with new_tags written in the original style."""
    if style == 'list':
        tag_lines = ''.join(f'  - {t}\n' for t in new_tags)
        new_block = f'tags:\n{tag_lines}'
        return fm[:match.start()] + new_block + fm[match.end():]
    else:  # inline
        inner = ', '.join(new_tags)
        new_inline = f'tags: [{inner}]'
        return fm[:match.start()] + new_inline + fm[match.end():]


# ─── MAIN ────────────────────────────────────────────────────────────────────

def process_vault(dry_run=True):
    stats = {
        'files_scanned': 0,
        'files_changed': 0,
        'tags_remapped': defaultdict(int),
        'tags_dropped': defaultdict(int),
        'tags_expanded': defaultdict(int),
    }
    changed_files = []

    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        for fname in sorted(files):
            if not fname.endswith('.md'):
                continue
            fpath = os.path.join(root, fname)
            stats['files_scanned'] += 1

            try:
                with open(fpath, encoding='utf-8', errors='ignore') as f:
                    content = f.read()
            except Exception as e:
                print(f"  ERROR reading {fpath}: {e}", file=sys.stderr)
                continue

            fm, body = parse_frontmatter(content)
            if fm is None:
                continue

            tags, style, match = get_tags_from_fm(fm)
            if not tags:
                continue

            new_tags, changed = apply_mapping(tags)
            if not changed:
                continue

            # Record what changed
            old_set = set(tags)
            new_set = set(new_tags)
            for old_tag in old_set - new_set:
                mapped = MAPPING.get(old_tag)
                if mapped is None:
                    stats['tags_dropped'][old_tag] += 1
                elif isinstance(mapped, list):
                    stats['tags_expanded'][f"{old_tag} → {', '.join(mapped)}"] += 1
                else:
                    stats['tags_remapped'][f"{old_tag} → {mapped}"] += 1

            rel = os.path.relpath(fpath, VAULT)
            changed_files.append((rel, tags, new_tags))
            stats['files_changed'] += 1

            if not dry_run:
                new_fm = rewrite_frontmatter(fm, new_tags, style, match)
                new_content = f"---{new_fm}\n---{body}"
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

    return stats, changed_files


def print_report(stats, changed_files, dry_run):
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"\n{'='*60}")
    print(f"  Tag migration — {mode}")
    print(f"{'='*60}")
    print(f"  Files scanned : {stats['files_scanned']}")
    print(f"  Files changed : {stats['files_changed']}")

    if stats['tags_remapped']:
        print(f"\n  Remapped ({len(stats['tags_remapped'])} distinct mappings):")
        for k, v in sorted(stats['tags_remapped'].items()):
            print(f"    {v:4d}x  {k}")

    if stats['tags_expanded']:
        print(f"\n  Expanded to multiple tags:")
        for k, v in sorted(stats['tags_expanded'].items()):
            print(f"    {v:4d}x  {k}")

    if stats['tags_dropped']:
        print(f"\n  Dropped:")
        for k, v in sorted(stats['tags_dropped'].items()):
            print(f"    {v:4d}x  {k}")

    if dry_run and changed_files:
        print(f"\n  Sample of files that would change (first 20):")
        for rel, old, new in changed_files[:20]:
            added   = set(new) - set(old)
            removed = set(old) - set(new)
            print(f"\n    {rel}")
            for t in sorted(removed):
                print(f"      - {t}")
            for t in sorted(added):
                print(f"      + {t}")

    print(f"\n{'='*60}\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', default=False,
                        help='Report changes without writing any files')
    args = parser.parse_args()

    if args.dry_run:
        print("Running in DRY RUN mode — no files will be modified.")
    else:
        print("Running in LIVE mode — files WILL be modified.")
        confirm = input("Type 'yes' to proceed: ").strip().lower()
        if confirm != 'yes':
            print("Aborted.")
            sys.exit(0)

    stats, changed_files = process_vault(dry_run=args.dry_run)
    print_report(stats, changed_files, dry_run=args.dry_run)
