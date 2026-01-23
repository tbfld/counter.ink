#!/usr/bin/env python3
"""
Fix image links with incorrect 'content/' prefix.
In Obsidian/Quartz, image paths should be relative, not start with 'content/'

Usage: python3 fix_content_prefix.py [--dry-run]
"""

import re
from pathlib import Path
import argparse

def fix_image_links(content, file_path, dry_run=False):
    """Fix image links that incorrectly start with 'content/'"""
    # Pattern to match: ![[content/path/to/image.jpg|attributes]]
    pattern = r'!\[\[(content/[^\]|]+)(\|[^\]]+)?\]\]'
    
    fixes = []
    
    def replace_fn(match):
        full_path = match.group(1)  # content/path/to/image.jpg
        attributes = match.group(2) or ''  # |wmed relative|center
        
        # Strip 'content/' prefix
        fixed_path = full_path.replace('content/', '', 1)
        
        # Verify the file exists after stripping
        if (Path('content') / fixed_path).exists():
            fixes.append({
                'old': full_path,
                'new': fixed_path,
                'exists': True
            })
            return f'![[{fixed_path}{attributes}]]'
        else:
            # File doesn't exist even after fixing, keep original
            fixes.append({
                'old': full_path,
                'new': fixed_path,
                'exists': False
            })
            return match.group(0)  # Return unchanged
    
    new_content = re.sub(pattern, replace_fn, content)
    
    return new_content, fixes

def main():
    parser = argparse.ArgumentParser(description='Fix content/ prefix in image links')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be changed without modifying files')
    args = parser.parse_args()
    
    content_dir = Path("content")
    md_files = list(content_dir.rglob("*.md"))
    
    total_fixes = 0
    files_modified = 0
    
    print(f"Scanning {len(md_files)} files for 'content/' prefix issues...")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}\n")
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if file has content/ prefix issues
            if 'content/' not in content or '![[content/' not in content:
                continue
            
            new_content, fixes = fix_image_links(content, md_file, args.dry_run)
            
            if fixes:
                verified_fixes = [f for f in fixes if f['exists']]
                unverified = [f for f in fixes if not f['exists']]
                
                if verified_fixes:
                    print(f"  {md_file}")
                    for fix in verified_fixes:
                        print(f"    ✓ {fix['old']} → {fix['new']}")
                    
                    total_fixes += len(verified_fixes)
                    files_modified += 1
                    
                    if not args.dry_run:
                        with open(md_file, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                
                if unverified:
                    print(f"  {md_file} (SKIPPED - files don't exist):")
                    for fix in unverified:
                        print(f"    ✗ {fix['old']} → {fix['new']}")
                
                print()
        
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print(f"\nSummary:")
    print(f"  Fixed {total_fixes} image links across {files_modified} files")
    
    if args.dry_run:
        print("\n[DRY RUN] No files were modified")
    else:
        print("\n✓ Files updated!")

if __name__ == "__main__":
    main()
