#!/usr/bin/env python3
"""
Validate YAML frontmatter in markdown files and identify potential issues.
"""

import os
import re
from collections import defaultdict

class YAMLValidator:
    def __init__(self):
        self.issues = defaultdict(list)
        self.stats = {
            'total_files': 0,
            'files_with_issues': 0,
            'files_without_frontmatter': 0,
        }
        self.property_values = defaultdict(set)
        
    def validate_file(self, filepath):
        """Validate a single markdown file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.stats['total_files'] += 1
            
            # Check if file has frontmatter
            if not content.startswith('---'):
                self.stats['files_without_frontmatter'] += 1
                self.issues['no_frontmatter'].append(filepath)
                return
            
            # Extract frontmatter
            parts = content.split('---', 2)
            if len(parts) < 3:
                self.issues['malformed_frontmatter'].append(filepath)
                return
            
            frontmatter_text = parts[1]
            
            # Check if frontmatter is effectively empty
            if not frontmatter_text.strip():
                self.issues['empty_frontmatter'].append(filepath)
                return
            
            # Parse frontmatter manually
            frontmatter = self._parse_frontmatter_manually(frontmatter_text)
            
            # Check for specific issues
            self._check_property_issues(filepath, frontmatter, frontmatter_text)
            
        except Exception as e:
            self.issues['file_read_error'].append((filepath, str(e)))
    
    def _parse_frontmatter_manually(self, text):
        """Simple manual parser for YAML frontmatter."""
        result = {}
        current_key = None
        
        for line in text.split('\n'):
            line = line.rstrip()
            if not line or line.strip().startswith('#'):
                continue
            
            # Check for key: value lines
            if ':' in line and not line.startswith(' ') and not line.startswith('-'):
                parts = line.split(':', 1)
                key = parts[0].strip()
                value = parts[1].strip() if len(parts) > 1 else None
                
                if value:
                    # Remove quotes if present
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                    elif value.startswith("'") and value.endswith("'"):
                        value = value[1:-1]
                    
                    # Convert boolean strings
                    if value.lower() == 'true':
                        value = True
                    elif value.lower() == 'false':
                        value = False
                    elif value.lower() == 'null' or value == '':
                        value = None
                
                result[key] = value
                current_key = key
        
        return result
    
    def _check_property_issues(self, filepath, frontmatter, frontmatter_text):
        """Check for specific property-related issues."""
        
        # Check for empty required fields
        if isinstance(frontmatter, dict):
            for key, value in frontmatter.items():
                # Track all values for each property
                self.property_values[key].add(str(value) if value is not None else 'None')
                
                # Check for empty string values
                if value == '':
                    self.issues['empty_string_values'].append((filepath, key))
                
                # Check for inconsistent date formats
                if key in ['date', 'created', 'updated']:
                    if value and not self._is_valid_date_format(str(value)):
                        self.issues['invalid_date_format'].append((filepath, key, value))
                
                # Check for boolean-like strings
                if isinstance(value, str) and value.lower() in ['true', 'false']:
                    self.issues['string_boolean'].append((filepath, key, value))
            
            # Check for properties with colons in values (potential YAML issues)
            for line in frontmatter_text.split('\n'):
                if ':' in line:
                    parts = line.split(':', 1)
                    if len(parts) == 2:
                        key = parts[0].strip()
                        value = parts[1].strip()
                        # Check if value has unquoted colons
                        if ':' in value and not (value.startswith('"') or value.startswith("'")):
                            if key not in ['aliases', 'tags']:  # These can have lists
                                self.issues['unquoted_colon_in_value'].append((filepath, key))
    
    def _is_valid_date_format(self, date_str):
        """Check if date string matches common formats."""
        # Common date/datetime formats
        patterns = [
            r'^\d{4}-\d{2}-\d{2}$',  # YYYY-MM-DD
            r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$',  # YYYY-MM-DD HH:MM
            r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$',  # YYYY-MM-DD HH:MM:SS
            r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}',  # ISO format
        ]
        
        return any(re.match(pattern, str(date_str)) for pattern in patterns)
    
    def print_report(self):
        """Print validation report."""
        print("=" * 80)
        print("YAML FRONTMATTER VALIDATION REPORT")
        print("=" * 80)
        print()
        
        print(f"Total files processed: {self.stats['total_files']}")
        print(f"Files without frontmatter: {self.stats['files_without_frontmatter']}")
        print()
        
        if not self.issues or all(len(v) == 0 for v in self.issues.values()):
            print("✓ No issues found!")
            return
        
        # Report issues by category
        if self.issues['malformed_frontmatter']:
            print(f"\n⚠ MALFORMED FRONTMATTER ({len(self.issues['malformed_frontmatter'])} files):")
            for filepath in self.issues['malformed_frontmatter'][:10]:
                print(f"  - {filepath}")
            if len(self.issues['malformed_frontmatter']) > 10:
                print(f"  ... and {len(self.issues['malformed_frontmatter']) - 10} more")
        
        if self.issues['yaml_parse_error']:
            print(f"\n⚠ YAML PARSE ERRORS ({len(self.issues['yaml_parse_error'])} files):")
            for filepath, error in self.issues['yaml_parse_error'][:10]:
                print(f"  - {filepath}")
                print(f"    Error: {error}")
            if len(self.issues['yaml_parse_error']) > 10:
                print(f"  ... and {len(self.issues['yaml_parse_error']) - 10} more")
        
        if self.issues['empty_string_values']:
            print(f"\n⚠ EMPTY STRING VALUES ({len(self.issues['empty_string_values'])} instances):")
            # Group by property name
            by_property = defaultdict(list)
            for filepath, prop in self.issues['empty_string_values']:
                by_property[prop].append(filepath)
            
            for prop, files in sorted(by_property.items()):
                print(f"  Property '{prop}' ({len(files)} files):")
                for filepath in files[:5]:
                    print(f"    - {filepath}")
                if len(files) > 5:
                    print(f"    ... and {len(files) - 5} more")
        
        if self.issues['invalid_date_format']:
            print(f"\n⚠ INVALID DATE FORMATS ({len(self.issues['invalid_date_format'])} instances):")
            for filepath, key, value in self.issues['invalid_date_format'][:10]:
                print(f"  - {filepath}")
                print(f"    Property: {key}, Value: {value}")
            if len(self.issues['invalid_date_format']) > 10:
                print(f"  ... and {len(self.issues['invalid_date_format']) - 10} more")
        
        if self.issues['string_boolean']:
            print(f"\n⚠ STRING BOOLEANS (should be unquoted) ({len(self.issues['string_boolean'])} instances):")
            for filepath, key, value in self.issues['string_boolean'][:10]:
                print(f"  - {filepath}")
                print(f"    Property: {key}, Value: '{value}'")
            if len(self.issues['string_boolean']) > 10:
                print(f"  ... and {len(self.issues['string_boolean']) - 10} more")
        
        if self.issues['unquoted_colon_in_value']:
            print(f"\n⚠ UNQUOTED COLONS IN VALUES ({len(self.issues['unquoted_colon_in_value'])} instances):")
            for filepath, key in self.issues['unquoted_colon_in_value'][:10]:
                print(f"  - {filepath}")
                print(f"    Property: {key}")
            if len(self.issues['unquoted_colon_in_value']) > 10:
                print(f"  ... and {len(self.issues['unquoted_colon_in_value']) - 10} more")
        
        # Property statistics
        print("\n" + "=" * 80)
        print("PROPERTY STATISTICS")
        print("=" * 80)
        print("\nMost common properties:")
        property_counts = [(prop, len(self.property_values[prop])) 
                          for prop in self.property_values.keys()]
        for prop, unique_count in sorted(property_counts, 
                                         key=lambda x: x[0].lower())[:20]:
            print(f"  {prop}: {unique_count} unique value(s)")

def main():
    """Validate all markdown files in the content directory."""
    validator = YAMLValidator()
    content_dir = 'content'
    
    # Walk through all directories
    for root, dirs, files in os.walk(content_dir):
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)
                validator.validate_file(filepath)
    
    validator.print_report()

if __name__ == '__main__':
    main()
