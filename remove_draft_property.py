#!/usr/bin/env python3
"""
Remove 'draft:' property lines from YAML headers in markdown files.
"""

import os
import re

def remove_draft_from_file(filepath):
    """Remove draft property line from a markdown file's YAML header."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has YAML frontmatter
        if not content.startswith('---'):
            return False
        
        # Split into frontmatter and body
        parts = content.split('---', 2)
        if len(parts) < 3:
            return False
        
        frontmatter = parts[1]
        body = parts[2]
        
        # Remove draft line (matches "draft:" followed by any value or nothing)
        # This will match:
        # - draft: false
        # - draft: "false"
        # - draft: "true"
        # - draft:
        # - draft: true
        original_frontmatter = frontmatter
        frontmatter = re.sub(r'^draft:.*$', '', frontmatter, flags=re.MULTILINE)
        
        # Only write if something changed
        if frontmatter != original_frontmatter:
            new_content = '---' + frontmatter + '---' + body
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Process all markdown files in the content directory."""
    content_dir = 'content'
    files_modified = 0
    files_processed = 0
    
    # Walk through all directories
    for root, dirs, files in os.walk(content_dir):
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)
                files_processed += 1
                
                if remove_draft_from_file(filepath):
                    files_modified += 1
                    print(f"Modified: {filepath}")
    
    print(f"\nSummary:")
    print(f"Files processed: {files_processed}")
    print(f"Files modified: {files_modified}")

if __name__ == '__main__':
    main()
