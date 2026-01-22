#!/usr/bin/env python3
"""
Standardize YAML property values by removing unnecessary quotes.
Follows YAML best practices:
- Booleans (true/false) should be unquoted
- Numbers should be unquoted
- Dates can be unquoted
"""

import os
import re

def standardize_yaml_values(content):
    """Standardize YAML property values by removing unnecessary quotes."""
    lines = content.split('\n')
    result_lines = []
    in_frontmatter = False
    
    for line in lines:
        # Track if we're in YAML frontmatter
        if line.strip() == '---':
            in_frontmatter = not in_frontmatter
            result_lines.append(line)
            continue
        
        # Only process lines inside frontmatter
        if in_frontmatter:
            # Remove quotes from boolean values
            # Match patterns like: publish: "true" or publish: "false"
            line = re.sub(r'^(\s*\w+:\s*)"(true|false)"(\s*)$', r'\1\2\3', line)
            
            # Remove quotes from simple ISO dates (YYYY-MM-DD)
            # Match patterns like: date: "2025-01-01"
            line = re.sub(r'^(\s*date:\s*)"(\d{4}-\d{2}-\d{2})"(\s*)$', r'\1\2\3', line)
        
        result_lines.append(line)
    
    return '\n'.join(result_lines)

def process_file(filepath):
    """Process a single markdown file to standardize YAML values."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Check if file has YAML frontmatter
        if not original_content.startswith('---'):
            return False
        
        new_content = standardize_yaml_values(original_content)
        
        # Only write if something changed
        if new_content != original_content:
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
                
                if process_file(filepath):
                    files_modified += 1
                    print(f"Modified: {filepath}")
    
    print(f"\nSummary:")
    print(f"Files processed: {files_processed}")
    print(f"Files modified: {files_modified}")

if __name__ == '__main__':
    main()
