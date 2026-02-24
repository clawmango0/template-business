#!/usr/bin/env python3
"""
Template Generator
Replaces placeholders in templates with custom values
"""

import os
import sys
import re
from datetime import datetime

# Default placeholders
DEFAULTS = {
    'COMPANY_NAME': 'Your Company',
    'PROJECT_NAME': 'Project Name',
    'DATE': datetime.now().strftime('%Y-%m-%d'),
    'AUTHOR': 'Document Owner',
    'PROJECT_MANAGER': 'Project Manager',
}

def replace_placeholders(content, values=None):
    """Replace {{PLACEHOLDER}} with values"""
    if values is None:
        values = {}
    
    # Merge with defaults
    replacements = {**DEFAULTS, **values}
    
    for key, value in replacements.items():
        content = content.replace(f'{{{{{key}}}}}', value)
    
    return content

def process_file(filepath, values=None, output_dir='output'):
    """Process a single template file"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace placeholders
    content = replace_placeholders(content, values)
    
    # Generate filename
    basename = os.path.basename(filepath)
    name_without_ext = os.path.splitext(basename)[0]
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Write customized version
    output_file = os.path.join(output_dir, basename)
    with open(output_file, 'w') as f:
        f.write(content)
    
    print(f"✓ Created: {output_file}")
    return output_file

def batch_process(template_dir, values=None, output_dir='output'):
    """Process all templates in a directory"""
    processed = []
    
    for root, dirs, files in os.walk(template_dir):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                # Calculate relative output path
                rel_dir = os.path.relpath(root, template_dir)
                rel_output = os.path.join(output_dir, rel_dir)
                
                result = process_file(filepath, values, rel_output)
                processed.append(result)
    
    return processed

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 generator.py <template.md> [company_name]")
        print("  python3 generator.py --batch <template_dir>")
        sys.exit(1)
    
    if sys.argv[1] == '--batch':
        template_dir = sys.argv[2] if len(sys.argv) > 2 else '.'
        batch_process(template_dir)
    else:
        template_file = sys.argv[1]
        company_name = sys.argv[2] if len(sys.argv) > 2 else 'Your Company'
        
        values = {'COMPANY_NAME': company_name}
        process_file(template_file, values)

if __name__ == '__main__':
    main()
