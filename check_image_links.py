#!/usr/bin/env python3
"""
Check for broken image links in markdown files.
Looks for Obsidian-style image embeds: ![[image.jpg|...]]

Resolution order mirrors how Obsidian/Quartz resolves wikilinks:
  1. Vault-root-relative path  (content/path/given)
  2. File-relative path        (sibling to the .md file)
  3. Vault-wide filename search (Obsidian's fallback: find by bare filename anywhere)
"""

import re
import sys
from pathlib import Path


def find_image_links(content):
    """Extract image link targets from Obsidian wikilink embeds."""
    # Match ![[path/to/image.jpg]] and ![[path/to/image.jpg|caption|align]]
    return re.findall(r'!\[\[([^\]|]+)', content)


def build_filename_index(content_dir: Path) -> dict[str, list[Path]]:
    """
    Build a map of bare filename -> list of matching paths across the entire vault.
    This is how Obsidian resolves bare filenames like ![[rubio-shoes.jpg]] when
    the file lives in a subdirectory (e.g. ci-img/rubio-memes/rubio-shoes.jpg).
    """
    index: dict[str, list[Path]] = {}
    for p in content_dir.rglob("*"):
        if p.is_file():
            index.setdefault(p.name, []).append(p)
    return index


def resolve(img_path: str, md_file: Path, content_dir: Path,
            filename_index: dict[str, list[Path]]) -> bool:
    """
    Return True if the image reference can be resolved by any of the three strategies.
    """
    # 1. Vault-root-relative: treat the path as relative to content/
    if (content_dir / img_path).exists():
        return True

    # 2. File-relative: treat the path as relative to the .md file's directory
    if (md_file.parent / img_path).exists():
        return True

    # 3. Vault-wide filename search (bare name or last path component)
    basename = Path(img_path).name
    if basename in filename_index:
        return True

    return False


def main():
    content_dir = Path("content")
    if not content_dir.exists():
        sys.exit("Run this script from the repo root (where 'content/' lives).")

    print("Building vault filename index...")
    filename_index = build_filename_index(content_dir)

    md_files = list(content_dir.rglob("*.md"))
    print(f"Checking {len(md_files)} markdown files...\n")

    broken_links = []

    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8', errors='replace')
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
            continue

        for img_path in find_image_links(content):
            img_path = img_path.strip()
            if not resolve(img_path, md_file, content_dir, filename_index):
                broken_links.append((str(md_file), img_path))

    if broken_links:
        print(f"Found {len(broken_links)} broken image link(s):\n")
        for filepath, img in broken_links:
            print(f"  {filepath}")
            print(f"    ![[{img}]]")
            print()
    else:
        print("✓ No broken image links found!")


if __name__ == "__main__":
    main()
