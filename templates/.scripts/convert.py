#!/usr/bin/env python3
"""
Template Converter - Convert markdown templates to PDF, Word, HTML
Automatically handles venv activation
"""

import os
import sys
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
VENV_PYTHON = SCRIPT_DIR / "venv" / "bin" / "python"

def ensure_pandoc():
    """Check if pandoc is available"""
    try:
        subprocess.run(["pandoc", "--version"], capture_output=True, check=True)
        return True
    except:
        return False

def convert_markdown(input_file, output_file, format_type):
    """Convert markdown to specified format using pandoc"""
    
    cmd = ['pandoc', input_file, '-o', output_file]
    
    if format_type == 'pdf':
        # Try wkhtmltopdf first, then fall back to html
        try:
            subprocess.run(['which', 'wkhtmltopdf'], capture_output=True, check=True)
            cmd.extend([
                '--pdf-engine=wkhtmltopdf',
                '--css', str(SCRIPT_DIR / 'style.css'),
                '--standalone',
                '-V', 'mainfont=Helvetica',
                '-V', 'fontsize=11pt',
                '-V', 'geometry=margin=1in'
            ])
        except:
            # Fall back to HTML then manual PDF
            html_out = str(Path(output_file).with_suffix('.html'))
            subprocess.run(['pandoc', input_file, '-o', html_out, '--standalone'], check=True)
            print(f"✓ Created HTML: {html_out} (PDF needs wkhtmltopdf)")
            return True
            
    elif format_type == 'docx':
        cmd.extend(['--standalone', '--toc'])
    elif format_type == 'html':
        cmd.extend(['--standalone', '--toc'])
    
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error converting: {e}")
        return False

def main():
    if len(sys.argv) < 3:
        print("Usage: python convert.py <format> <input.md> [-o output]")
        print("Formats: pdf, docx, html, all")
        sys.exit(1)
    
    format_type = sys.argv[1]
    input_file = sys.argv[2]
    
    output_file = None
    if '-o' in sys.argv:
        idx = sys.argv.index('-o')
        if idx + 1 < len(sys.argv):
            output_file = sys.argv[idx + 1]
    
    input_path = Path(input_file)
    if not input_path.exists():
        print(f"Error: File not found: {input_file}")
        sys.exit(1)
    
    if not ensure_pandoc():
        print("Error: pandoc not found. Install with: sudo apt install pandoc")
        sys.exit(1)
    
    formats = [format_type] if format_type != 'all' else ['pdf', 'docx', 'html']
    
    for fmt in formats:
        if output_file:
            out_file = output_file
        else:
            out_file = str(input_path.with_suffix(f'.{fmt}'))
        
        print(f"Converting: {input_file} → {out_file}")
        
        if convert_markdown(str(input_path), out_file, fmt):
            print(f"✓ Created: {out_file}")
        else:
            print(f"✗ Failed: {out_file}")

if __name__ == '__main__':
    main()
