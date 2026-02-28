#!/usr/bin/env python3
"""
Template Converter - Convert markdown templates to PDF, Word, HTML
Usage: python convert.py <format> <input.md> [output]
Formats: pdf, docx, html, all
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent.parent

def convert_markdown(input_file, output_file, format_type):
    """Convert markdown to specified format using pandoc."""
    
    cmd = ['pandoc', input_file, '-o', output_file]
    
    if format_type == 'pdf':
        cmd.extend([
            '--pdf-engine=wkhtmltopdf',
            '--css', str(TEMPLATE_DIR / '.scripts' / 'style.css'),
            '--standalone',
            '--toc',
            '-V', 'mainfont=Helvetica',
            '-V', 'fontsize=11pt',
            '-V', 'geometry=margin=1in'
        ])
    elif format_type == 'docx':
        cmd.extend(['--standalone', '--toc'])
    elif format_type == 'html':
        cmd.extend(['--standalone', '--self-contained', '--toc'])
    
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error converting: {e}")
        return False

def convert_libreoffice(input_file, output_file):
    """Convert using LibreOffice (fallback)."""
    cmd = ['libreoffice', '--headless', '--convert-to', 'docx', input_file, '--outdir', os.path.dirname(output_file)]
    try:
        subprocess.run(cmd, check=True)
        return True
    except:
        return False

def main():
    parser = argparse.ArgumentParser(description='Convert template markdown files')
    parser.add_argument('format', choices=['pdf', 'docx', 'html', 'all'], help='Output format')
    parser.add_argument('input', help='Input markdown file')
    parser.add_argument('-o', '--output', help='Output file (optional)')
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: File not found: {input_path}")
        sys.exit(1)
    
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = input_path.with_suffix(f'.{args.format}')
    
    formats = [args.format] if args.format != 'all' else ['pdf', 'docx', 'html']
    
    for fmt in formats:
        out_file = input_path.with_suffix(f'.{fmt}')
        print(f"Converting: {input_path} → {out_file}")
        
        if convert_markdown(str(input_path), str(out_file), fmt):
            print(f"✓ Created: {out_file}")
        else:
            print(f"✗ Failed: {out_file}")

if __name__ == '__main__':
    main()
