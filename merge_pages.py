#!/usr/bin/env python3
"""
Merge micro.md and recent.md chronologically
"""

import re
from datetime import datetime
from pathlib import Path

def extract_micro_entries(content):
    """Extract timestamped entries from micro.md"""
    entries = []
    # Match entries like: ***2026-01-20:*** content
    pattern = r'\*\*\*(\d{4}-\d{2}-\d{2}):\*\*\* (.+?)(?=\n\*\*\*|$)'
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

def extract_recent_entries(content):
    """Extract blog post entries from recent.md"""
    entries = []
    # Match callout boxes like: > [!note]+ [[2026-01-20-viruses-are-people-too|...]]
    pattern = r'> \[!(\w+)\]\+ \[\[(\d{4}-\d{2}-\d{2})-[^\]]+\]\]\n> (.+?)(?=\n\n>|\n\n#|\Z)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    for callout_type, date_str, description in matches:
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            # Reconstruct the full entry by finding it in original content
            full_pattern = rf'(> \[!{callout_type}\]\+ \[\[{date_str}[^\]]+\]\]\n> {re.escape(description[:50])}[^\n]*)'
            full_match = re.search(full_pattern, content, re.DOTALL)
            if full_match:
                full_content = full_match.group(1)
                # Get the complete box (might span multiple lines)
                start = content.find(full_content)
                end = content.find('\n\n>', start + 1)
                if end == -1:
                    end = content.find('\n\n#', start + 1)
                if end == -1:
                    end = len(content)
                full_box = content[start:end].strip()
                
                entries.append({
                    'date': date,
                    'type': 'recent',
                    'content': full_box
                })
        except (ValueError, AttributeError):
            continue
    
    return entries

def main():
    # Read files - use current recent.md since it has all the content
    # We'll just re-read it and add headers
    recent_path = Path('content/recent.md')
    
    with open(recent_path, 'r') as f:
        recent_content = f.read()
    
    # Extract both micro and recent entries from the current merged file
    micro_content = recent_content  # Both types are now in recent.md
    
    # Extract header from recent.md (up to More... box)
    header_end = recent_content.find('<!-- RECENT_POSTS_START -->')
    if header_end == -1:
        header_end = recent_content.find('> [!')
    header = recent_content[:header_end].strip()
    
    # Get entries
    micro_entries = extract_micro_entries(micro_content)
    recent_entries = extract_recent_entries(recent_content)
    
    # Combine and deduplicate by content
    seen_content = set()
    all_entries = []
    for entry in micro_entries + recent_entries:
        # Use first 100 chars as key for deduplication
        content_key = entry['content'][:100]
        if content_key not in seen_content:
            seen_content.add(content_key)
            all_entries.append(entry)
    
    # Sort by date (newest first)
    all_entries.sort(key=lambda x: x['date'], reverse=True)
    
    # Build merged content
    merged = [header, '', '<!-- RECENT_POSTS_START -->', '', '']
    
    current_month = None
    current_year = None
    
    for entry in all_entries:
        entry_date = entry['date']
        entry_month = entry_date.strftime('%Y-%m')
        entry_year = entry_date.strftime('%Y')
        
        # Add year header if year changes
        if current_year != entry_year:
            if current_year is not None:
                merged.append('')
            merged.append(f'## {entry_year}')
            merged.append('')
            current_year = entry_year
            current_month = None  # Reset month when year changes
        
        # Add month header if month changes
        if current_month != entry_month:
            merged.append(f'### {entry_month}')
            merged.append('')
            current_month = entry_month
        
        merged.append(entry['content'])
        merged.append('')
    
    # Write merged file
    output = '\n'.join(merged)
    with open('content/recent_merged.md', 'w') as f:
        f.write(output)
    
    print(f"Merged {len(micro_entries)} micro entries and {len(recent_entries)} recent entries")
    print(f"Total: {len(all_entries)} entries")
    print("Output written to content/recent_merged.md")
    print("Review this file before replacing recent.md")

if __name__ == '__main__':
    main()
