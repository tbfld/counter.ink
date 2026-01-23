#!/usr/bin/env python3
"""
Check for broken image links in markdown files.
Looks for Obsidian-style image embeds: ![[image.jpg|...]]
"""

import re
from pathlib import Path

def find_image_links(content):
    """Extract image links from markdown content"""
    # Match: ![[path/to/image.jpg|attributes]]
    pattern = r'!\[\[([^\]|]+)'
    return re.findall(pattern, content)

def main():
    content_dir = Path("content")
    broken_links = []
    
    # Find all markdown files
    md_files = list(content_dir.rglob("*.md"))
    print(f"Checking {len(md_files)} markdown files...")
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            image_links = find_image_links(content)
            
            for img_path in image_links:
                # Try different path resolutions
                resolved = False
                
                # Try as absolute from content/
                abs_path = content_dir / img_path
                if abs_path.exists():
                    resolved = True
                    continue
                
                # Try relative to markdown file's directory
                rel_path = md_file.parent / img_path
                if rel_path.exists():
                    resolved = True
                    continue
                
                # Try stripping "content/" prefix if present
                if img_path.startswith("content/"):
                    stripped = Path(img_path.replace("content/", "", 1))
                    if stripped.exists():
                        resolved = True
                        continue
                
                if not resolved:
                    broken_links.append({
                        'file': str(md_file),
                        'image': img_path,
                        'line_context': content.split(f'![[{img_path}')[0][-50:] if f'![[{img_path}' in content else ''
                    })
        
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
    
    # Report findings
    if broken_links:
        print(f"\n Found {len(broken_links)} broken image links:\n")
        for link in broken_links[:20]:  # Show first 20
            print(f"  File: {link['file']}")
            print(f"  Image: {link['image']}")
            print()
    else:
        print("\n✓ No broken image links found!")

if __name__ == "__main__":
    main()
