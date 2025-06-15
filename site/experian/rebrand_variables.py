#!/usr/bin/env python3
"""
Rebrand _variables.yml for Experian
"""

import re
import os
import sys
from pathlib import Path

def rebrand_variables():
    # Show current working directory
    current_dir = Path.cwd()
    print(f"Current working directory: {current_dir}")
    
    # Try multiple possible locations for _variables.yml
    possible_paths = [
        Path('_variables.yml'),  # Current directory
        Path('../_variables.yml'),  # Parent directory (if running from experian/)
        current_dir / '_variables.yml',  # Absolute current
        current_dir.parent / '_variables.yml',  # Absolute parent
    ]
    
    variables_file = None
    for path in possible_paths:
        print(f"Checking {path.resolve()}")
        if path.exists():
            variables_file = path
            print(f"Found _variables.yml at {variables_file.resolve()}")
            break
    
    if variables_file is None:
        print(f"Error: _variables.yml not found in any expected location:")
        for path in possible_paths:
            print(f"  - {path.resolve()}")
        return False
    
    # Check if file is readable
    if not os.access(variables_file, os.R_OK):
        print(f"Error: Cannot read {variables_file}. Check file permissions.")
        return False
    
    # Check if file is writable
    if not os.access(variables_file, os.W_OK):
        print(f"Error: Cannot write to {variables_file}. Check file permissions.")
        return False
    
    try:
        # Read the file
        with open(variables_file, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Perform replacements
        content = original_content
        replacements_made = 0
        
        # Show what we're looking for
        print(f"File content length: {len(content)} characters")
        if 'product:' in content:
            print("Found 'product:' in file")
            # Show lines containing 'product:'
            for i, line in enumerate(content.split('\n'), 1):
                if 'product:' in line:
                    print(f"Line {i}: {line.strip()}")
        else:
            print("No 'product:' found in file")
        
        # Required replacements
        pattern = r'product: "ValidMind AI risk platform"'
        replacement = r'product: "Experian Model Governance Manager powered by ValidMind"'
        print(f"Looking for pattern: {pattern}")
        
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            replacements_made += 1
            print("Replacement made!")
        else:
            print("No replacement made - pattern not found")
        content = new_content
        
        # Additional replacement examples (uncomment as needed):
        # new_content = re.sub(r'platform: "ValidMind Platform"', 
        #                      r'platform: "Experian Model Governance Platform"', content)
        # if new_content != content:
        #     replacements_made += 1
        # content = new_content
        
        # new_content = re.sub(r'developer: "ValidMind Library"', 
        #                      r'developer: "Experian Model Development Library"', content)
        # if new_content != content:
        #     replacements_made += 1
        # content = new_content
        
        # new_content = re.sub(r'legal: "ValidMind Inc\."', 
        #                      r'legal: "Experian Information Solutions, Inc."', content)
        # if new_content != content:
        #     replacements_made += 1
        # content = new_content
        
        # new_content = re.sub(r'training: "ValidMind Academy"', 
        #                      r'training: "Experian Model Governance Academy"', content)
        # if new_content != content:
        #     replacements_made += 1
        # content = new_content
        
        # Write the updated content
        with open(variables_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        if replacements_made > 0:
            print(f"✓ Variables rebranded for Experian ({replacements_made} replacement(s) made)")
        else:
            print("⚠ No replacements made - file may already be rebranded or patterns not found")
        
        return True
        
    except IOError as e:
        print(f"Error reading/writing file: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = rebrand_variables()
    sys.exit(0 if success else 1) 