#!/usr/bin/env python3
"""
Rebuild recent.md from backups with month headers for TOC
Note: This script is deprecated as recent.md is now the primary source.
"""

import re
from datetime import datetime
from pathlib import Path

def extract_micro_entries(filepath):
    """Extract timestamped entries from original micro backup"""
    if not Path(filepath).exists():
        return []
    with open(filepath, 'r') as f:
        content = f.read()
    
    entries = []
    # Match entries like: ***2026-01-20:*** content
    pattern = r'\*\*\*(\d{4}-\d{2}-\d{2}):\*\*\* (.+?)(?=\n\*\*\*|\n\n#|$)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    for date_str, entry_content in matches:
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            entries.append({
                'date': date,
                'type': 'micro',
                'content': f'***{date_str}:*** {entry_content.strip()}'
            })
        except ValueError:
            continue
    
    return entries

def extract_recent_entries(filepath):
    """Extract blog post entries from recent backup"""
    if not Path(filepath).exists():
        return []
    with open(filepath, 'r') as f:
        content = f.read()
    
    entries = []
    # Match callout boxes
    pattern = r'(> \[![^\]]+\]\+ \[\[(\d{4}-\d{2}-\d{2})[^\]]*\]\][^\n]*\n(?:> [^\n]*\n)*)'
    matches = re.findall(pattern, content, re.MULTILINE)
    
    for full_box, date_str in matches:
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            entries.append({
                'date': date,
                'type': 'recent',
                'content': full_box.strip()
            })
        except ValueError:
            continue
    
    return entries

def main():
    # Check if backup file exists - if not, script is deprecated
    backup_file = Path('content/recent_backup.md')
    if not backup_file.exists():
        print("Note: This script is deprecated. recent_backup.md not found.")
        print("The recent.md file is now maintained directly.")
        return
    
    # Check for original micro file or use a marker file
    micro_file = Path('content/micro_original.md')
    if not micro_file.exists():
        print("Warning: micro_original.md not found, using empty micro entries")
        micro_entries = []
    else:
        micro_entries = extract_micro_entries(micro_file)
    
    recent_entries = extract_recent_entries('content/recent_backup.md')
    
    # Combine and deduplicate
    seen = set()
    all_entries = []
    for entry in micro_entries + recent_entries:
        key = (entry['date'].strftime('%Y-%m-%d'), entry['content'][:100])
        if key not in seen:
            seen.add(key)
            all_entries.append(entry)
    
    # Sort by date (newest first)
    all_entries.sort(key=lambda x: x['date'], reverse=True)
    
    # Build output with headers
    with open('content/recent_backup.md', 'r') as f:
        backup_content = f.read()
    
    header_end = backup_content.find('<!-- RECENT_POSTS_START -->')
    if header_end == -1:
        header_end = backup_content.find('> [!')
    header = backup_content[:header_end].strip()
    
    # Remove micro reference from header
    header = header.replace('For nimbler things, see [[micro]]\n> \n> Or', 'Or')
    
    merged = [header, '', '<!-- RECENT_POSTS_START -->', '', '']
    
    current_month = None
    current_year = None
    
    for entry in all_entries:
        entry_date = entry['date']
        entry_month = entry_date.strftime('%Y-%m')
        entry_year = entry_date.strftime('%Y')
        
        # Add year header
        if current_year != entry_year:
            if current_year is not None:
                merged.append('')
            merged.append(f'## {entry_year}')
            merged.append('')
            current_year = entry_year
            current_month = None
        
        # Add month header
        if current_month != entry_month:
            merged.append(f'### {entry_month}')
            merged.append('')
            current_month = entry_month
        
        merged.append(entry['content'])
        merged.append('')
    
    # Write output
    output = '\n'.join(merged)
    with open('content/recent.md', 'w') as f:
        f.write(output)
    
    print(f"Rebuilt recent.md with {len(all_entries)} entries")
    print(f"  - {len(micro_entries)} micro entries")
    print(f"  - {len(recent_entries)} blog post entries")

if __name__ == '__main__':
    main()
