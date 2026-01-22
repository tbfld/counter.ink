#!/usr/bin/env python3
"""
Archive old entries from recent.md:

WORKFLOW:
1. recent.md shows ALL entries (micro + boxed) ≤6 months old
2. Boxed entries >6 months: DELETE from recent.md (linked pages remain)
3. Micro entries:
   - ALL micros (current + future) are logged to micro.md
   - Micros >6 months: DELETE from recent.md, KEEP in micro.md

Usage: python3 archive_old_entries.py [--dry-run]
"""

import re
from datetime import datetime, timedelta
from pathlib import Path
import argparse

def parse_date(date_str):
    """Parse dates in format: 2026-01-22, 2025-12, 2025"""
    try:
        if len(date_str) == 10:  # YYYY-MM-DD
            return datetime.strptime(date_str, "%Y-%m-%d")
        elif len(date_str) == 7:  # YYYY-MM
            return datetime.strptime(date_str + "-01", "%Y-%m-%d")
        elif len(date_str) == 4:  # YYYY
            return datetime.strptime(date_str + "-01-01", "%Y-%m-%d")
    except ValueError:
        return None
    return None

def is_micro_entry(line):
    """Check if line is a micro entry (not a callout box)"""
    # Micro entries: ***2026-01-22:*** ...
    # Not boxes: > [!note]+ or > [!warning]+ etc
    return line.strip().startswith("***") and not line.strip().startswith(">")

def extract_date_from_entry(line):
    """Extract date from entry line"""
    # Match: ***2026-01-22:*** or ***2025-12-31***
    match = re.search(r'\*\*\*(\d{4}-\d{2}-\d{2})\*\*\*', line)
    if match:
        return match.group(1)
    return None

def is_boxed_entry_start(line):
    """Check if line starts a boxed entry (callout)"""
    return line.strip().startswith("> [!")

def process_entries(lines, cutoff_date):
    """Process entries and return filtered content and archived micros"""
    kept_lines = []
    archived_micros = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for boxed entry (callout)
        if is_boxed_entry_start(line):
            # Extract date from the callout title
            # Format: > [!note]+ [[2026-01-20-title|2026-01-20 title]]
            date_match = re.search(r'\[\[(\d{4}-\d{2}-\d{2})', line)
            if date_match:
                entry_date_str = date_match.group(1)
                entry_date = parse_date(entry_date_str)
                
                # Collect the entire boxed entry (until next non-indented line)
                boxed_lines = [line]
                i += 1
                while i < len(lines) and (lines[i].startswith(">") or lines[i].strip() == ""):
                    boxed_lines.append(lines[i])
                    i += 1
                
                # Check age and keep/discard
                if entry_date and entry_date < cutoff_date:
                    print(f"  Deleting boxed entry from {entry_date_str}")
                    # Don't add to kept_lines (delete it)
                else:
                    kept_lines.extend(boxed_lines)
                continue
        
        # Check for micro entry
        elif is_micro_entry(line):
            date_str = extract_date_from_entry(line)
            if date_str:
                entry_date = parse_date(date_str)
                if entry_date and entry_date < cutoff_date:
                    print(f"  Archiving micro entry from {date_str}")
                    archived_micros.append(line)
                    # Don't add to kept_lines (delete from recent)
                else:
                    kept_lines.append(line)
            else:
                kept_lines.append(line)
        else:
            kept_lines.append(line)
        
        i += 1
    
    return kept_lines, archived_micros

def main():
    parser = argparse.ArgumentParser(description='Archive old entries from recent.md')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be done without making changes')
    args = parser.parse_args()
    
    recent_path = Path("content/recent.md")
    micro_path = Path("content/micro.md")
    
    if not recent_path.exists():
        print(f"Error: {recent_path} not found")
        return
    
    # Calculate 6 months ago
    cutoff_date = datetime.now() - timedelta(days=180)
    print(f"Cutoff date: {cutoff_date.strftime('%Y-%m-%d')}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print()
    
    # Read recent.md
    with open(recent_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find YAML header end
    yaml_end = 0
    in_yaml = False
    for i, line in enumerate(lines):
        if line.strip() == '---' and not in_yaml:
            in_yaml = True
        elif line.strip().startswith('yaml_end:') and in_yaml:
            yaml_end = i + 1
            break
    
    # Split into header and content
    header_lines = lines[:yaml_end]
    content_lines = lines[yaml_end:]
    
    # Process entries
    print("Processing entries...")
    kept_content, archived_micros = process_entries(content_lines, cutoff_date)
    
    print(f"\nSummary:")
    print(f"  Archived {len(archived_micros)} micro entries")
    print(f"  Kept {len([l for l in kept_content if is_micro_entry(l)])} recent micro entries")
    
    if args.dry_run:
        print("\n[DRY RUN] No files modified")
        if archived_micros:
            print("\nWould archive these micros to micro.md:")
            for micro in archived_micros[:5]:  # Show first 5
                print(f"  {micro.strip()[:80]}...")
    else:
        # Append archived micros to micro.md
        if archived_micros:
            print(f"\nAppending {len(archived_micros)} micros to {micro_path}...")
            with open(micro_path, 'a', encoding='utf-8') as f:
                if micro_path.exists() and micro_path.stat().st_size > 0:
                    f.write("\n")  # Add newline before appending
                for micro in archived_micros:
                    f.write(micro)
        
        # Write updated recent.md
        print(f"Writing updated {recent_path}...")
        with open(recent_path, 'w', encoding='utf-8') as f:
            f.writelines(header_lines)
            f.writelines(kept_content)
        
        print("Done!")

if __name__ == "__main__":
    main()
