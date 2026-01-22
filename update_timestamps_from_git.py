#!/usr/bin/env python3
"""
Update the 'updated' field in YAML frontmatter with the file's last git commit date.
This recovers the modification dates from before the recent YAML cleanup operations.
"""

import os
import re
import subprocess
from datetime import datetime

def get_git_last_modified(filepath):
    """Get the last commit date for a file from git history."""
    try:
        # Get the last commit date for this file
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%ci', filepath],
            capture_output=True,
            text=True,
            check=True
        )
        
        if result.stdout.strip():
            # Parse the git timestamp (format: "2025-01-21 21:33:44 -0500")
            git_date_str = result.stdout.strip()
            # Extract just the date and time part
            datetime_part = git_date_str.split()[0] + ' ' + git_date_str.split()[1]
            # Parse and format as "YYYY-MM-DD HH:MM"
            dt = datetime.strptime(datetime_part, '%Y-%m-%d %H:%M:%S')
            return dt.strftime('%Y-%m-%d %H:%M')
        
        return None
    except subprocess.CalledProcessError:
        return None
    except Exception as e:
        print(f"Error getting git date for {filepath}: {e}")
        return None

def update_yaml_updated_field(content, new_date):
    """Update the 'updated' field in YAML frontmatter."""
    lines = content.split('\n')
    result_lines = []
    in_frontmatter = False
    updated_modified = False
    
    for line in lines:
        # Track if we're in YAML frontmatter
        if line.strip() == '---':
            in_frontmatter = not in_frontmatter
            result_lines.append(line)
            continue
        
        # Only process lines inside frontmatter
        if in_frontmatter and line.startswith('updated:') and new_date:
            # Replace the updated field with the git date
            result_lines.append(f'updated: {new_date}')
            updated_modified = True
        else:
            result_lines.append(line)
    
    return '\n'.join(result_lines), updated_modified

def process_file(filepath):
    """Process a single markdown file to update its 'updated' field."""
    try:
        # Get the last git commit date
        git_date = get_git_last_modified(filepath)
        
        if not git_date:
            # No git history for this file
            return False
        
        # Read the file
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Check if file has YAML frontmatter and an 'updated' field
        if not original_content.startswith('---'):
            return False
        
        if 'updated:' not in original_content:
            return False
        
        # Update the 'updated' field
        new_content, was_modified = update_yaml_updated_field(original_content, git_date)
        
        # Only write if something changed
        if was_modified and new_content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Process all modified markdown files."""
    # Get list of modified files from git
    try:
        result = subprocess.run(
            ['git', 'diff', '--name-only', 'HEAD'],
            capture_output=True,
            text=True,
            check=True
        )
        
        modified_files = [f for f in result.stdout.strip().split('\n') if f.endswith('.md')]
        
        if not modified_files:
            print("No modified markdown files found.")
            return
        
        files_modified = 0
        files_processed = 0
        
        for filepath in modified_files:
            if os.path.exists(filepath):
                files_processed += 1
                
                if process_file(filepath):
                    files_modified += 1
                    print(f"Modified: {filepath}")
        
        print(f"\nSummary:")
        print(f"Files processed: {files_processed}")
        print(f"Files modified: {files_modified}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error running git command: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
