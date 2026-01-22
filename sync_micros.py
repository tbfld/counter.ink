#!/usr/bin/env python3
"""
Sync micro entries from recent.md to micro.md

This script ensures ALL micro entries from recent.md are also in micro.md.
Should be run:
- Manually when needed
- Automatically as part of the Quartz build process

Usage: python3 sync_micros.py
"""

import re
from pathlib import Path
from datetime import datetime

def is_micro_entry(line):
    """Check if line is a micro entry"""
    return line.strip().startswith("***") and not line.strip().startswith(">")

def extract_date_from_entry(line):
    """Extract date from entry line"""
    match = re.search(r'\*\*\*(\d{4}-\d{2}-\d{2})\*\*\*', line)
    if match:
        return match.group(1)
    return None

def main():
    recent_path = Path("content/recent.md")
    micro_path = Path("content/micro.md")
    
    if not recent_path.exists():
        print(f"Error: {recent_path} not found")
        return
    
    # Read recent.md and extract all micro entries
    print("Reading recent.md...")
    with open(recent_path, 'r', encoding='utf-8') as f:
        recent_lines = f.readlines()
    
    micros_from_recent = [line for line in recent_lines if is_micro_entry(line)]
    print(f"Found {len(micros_from_recent)} micro entries in recent.md")
    
    # Read existing micro.md
    existing_micros = set()
    if micro_path.exists():
        with open(micro_path, 'r', encoding='utf-8') as f:
            micro_lines = f.readlines()
        existing_micros = {line.strip() for line in micro_lines if is_micro_entry(line)}
        print(f"Found {len(existing_micros)} existing entries in micro.md")
    
    # Find new micros to add
    new_micros = []
    for micro in micros_from_recent:
        if micro.strip() not in existing_micros:
            new_micros.append(micro)
    
    if not new_micros:
        print("✓ micro.md is already up to date!")
        return
    
    print(f"Adding {len(new_micros)} new entries to micro.md...")
    
    # Append new micros to micro.md
    with open(micro_path, 'a', encoding='utf-8') as f:
        if micro_path.stat().st_size > 0:
            # Check if file ends with newline
            with open(micro_path, 'r', encoding='utf-8') as check:
                content = check.read()
                if not content.endswith('\n'):
                    f.write('\n')
        
        for micro in new_micros:
            f.write(micro)
            if not micro.endswith('\n'):
                f.write('\n')
    
    print(f"✓ Added {len(new_micros)} new micro entries to micro.md")

if __name__ == "__main__":
    main()
