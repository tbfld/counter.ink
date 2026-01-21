#!/usr/bin/env python3
"""
Add month/year headers to recent.md for TOC
"""

import re
from datetime import datetime
from pathlib import Path

def main():
    # Check if the old file exists, otherwise use the current recent.md
    old_file = Path('content/recent_old.md')
    if old_file.exists():
        with open(old_file, 'r') as f:
            content = f.read()
    else:
        # File doesn't exist - recent.md already has headers, so just exit
        print("Note: recent_old.md not found. Recent.md already has headers.")
        return
    
    # Extract header
    header_end = content.find('<!-- RECENT_POSTS_START -->')
    header = content[:header_end].strip()
    body = content[header_end:].strip()
    
    # Find all dates in the content
    micro_dates = re.findall(r'\*\*\*(\d{4}-\d{2}-\d{2}):\*\*\*', body)
    callout_dates = re.findall(r'> \[![^\]]+\]\+ \[\[(\d{4}-\d{2}-\d{2})-', body)
    all_dates = sorted(set(micro_dates + callout_dates), reverse=True)
    
    # Build output with headers
    lines = body.split('\n')
    output = [header, '']
    
    current_month = None
    current_year = None
    
    for line in lines:
        # Check if line contains a date
        date_match = re.search(r'(\d{4}-\d{2}-\d{2})', line)
        if date_match:
            date_str = date_match.group(1)
            try:
                date = datetime.strptime(date_str, '%Y-%m-%d')
                entry_month = date.strftime('%Y-%m')
                entry_year = date.strftime('%Y')
                
                # Add year header
                if current_year != entry_year:
                    if current_year is not None:
                        output.append('')
                    output.append(f'## {entry_year}')
                    output.append('')
                    current_year = entry_year
                    current_month = None
                
                # Add month header
                if current_month != entry_month:
                    output.append(f'### {entry_month}')
                    output.append('')
                    current_month = entry_month
            except:
                pass
        
        output.append(line)
    
    # Write output
    result = '\n'.join(output)
    with open('content/recent.md', 'w') as f:
        f.write(result)
    
    print("Added month/year headers to recent.md")
    print(f"Found {len(all_dates)} unique dates")

if __name__ == '__main__':
    main()
