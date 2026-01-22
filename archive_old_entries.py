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
    
    # Read recent.md
    with open(recent_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # TODO: Implement the filtering logic
    # This is a skeleton - you'll need to:
    # 1. Find the <!-- RECENT_POSTS_START --> marker
    # 2. Process each entry, checking its date
    # 3. Collect old micro entries for archiving
    # 4. Build new content without old entries
    # 5. Append old micros to micro.md
    # 6. Write updated recent.md
    
    print("Script skeleton created. Implementation needed:")
    print("1. Parse entries between YAML and identify dates")
    print("2. Filter entries by age")
    print("3. Archive micros to micro.md")
    print("4. Write filtered recent.md")

if __name__ == "__main__":
    main()
