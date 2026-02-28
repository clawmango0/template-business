#!/usr/bin/env python3
"""
Fillable PDF Generator - Convert templates to fillable PDF forms
Automatically handles venv activation
"""

import os
import sys
import re
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
VENV_DIR = SCRIPT_DIR / "venv"

def ensure_venv():
    """Ensure venv exists and packages are installed"""
    if not VENV_DIR.exists():
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", str(VENV_DIR)], check=True)
        
        pip = VENV_DIR / "bin" / "pip"
        subprocess.run([str(pip), "install", "reportlab"], check=True)
        print("✓ Environment ready")
    
    return str(VENV_DIR / "bin" / "python")

# Patch subprocess to use venv python if needed
def run_with_venv():
    venv_python = ensure_venv()
    if venv_python != sys.executable:
        # Re-run with venv python
        os.execv(venv_python, [venv_python] + sys.argv)

# Run with venv on first import - this is simpler
if __name__ == '__main__':
    if not (SCRIPT_DIR / "venv" / "lib").exists():
        print("Setting up environment...")
        subprocess.run([sys.executable, "-m", "venv", str(VENV_DIR)], check=True)
        subprocess.run([str(VENV_DIR / "bin" / "pip"), "install", "reportlab"], check=True)
    
    # Now import and run
    import importlib.util
    
    # The actual PDF generator code is below, so just continue
    pass

# Now import reportlab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class FillablePDFGenerator:
    def __init__(self):
        self.y_position = 10.5 * 72
        self.left_margin = 0.75 * 72
        self.right_margin = 7.25 * 72
        self.line_height = 0.25 * 72
        
    def wrap_text(self, text, max_width):
        words = text.split()
        lines = []
        current_line = []
        for word in words:
            test_line = ' '.join(current_line + [word])
            if len(test_line) * 7 < max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
        if current_line:
            lines.append(' '.join(current_line))
        return lines
    
    def parse_template(self, md_file):
        with open(md_file, 'r') as f:
            content = f.read()
        fields = []
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if '[ ]' in line or '[X]' in line:
                checkbox_text = line.replace('[X]', '').replace('[ ]', '').strip()
                fields.append({'type': 'checkbox', 'text': checkbox_text, 'line_num': i})
                continue
            if '[' in line and ']' in line:
                matches = re.findall(r'\[([^\]]+)\]', line)
                for match in matches:
                    if match.strip() and not match.startswith('_'):
                        fields.append({'type': 'text', 'placeholder': match.strip(), 'text': line, 'line_num': i})
        return fields, content
    
    def generate_pdf(self, md_file, output_file=None):
        fields, content = self.parse_template(md_file)
        if output_file is None:
            output_file = str(Path(md_file).with_suffix('.pdf'))
        
        c = canvas.Canvas(output_file, pagesize=letter)
        width, height = letter
        title = Path(md_file).stem.replace('-', ' ').replace('_', ' ').title()
        
        self.y_position = height - 1*72
        c.setFont("Helvetica-Bold", 16)
        c.drawString(self.left_margin, self.y_position, title)
        self.y_position -= 0.5 * 72
        
        content_lines = content.split('\n')
        
        for line in content_lines:
            if self.y_position < 1 * 72:
                c.showPage()
                self.y_position = height - 1 * 72
            
            if not line.strip():
                self.y_position -= 0.15 * 72
                continue
            
            if line.startswith('# '):
                c.setFont("Helvetica-Bold", 14)
                c.drawString(self.left_margin, self.y_position, line[2:])
                self.y_position -= 0.3 * 72
                continue
            elif line.startswith('## '):
                c.setFont("Helvetica-Bold", 12)
                c.drawString(self.left_margin, self.y_position, line[3:])
                self.y_position -= 0.25 * 72
                continue
            elif line.startswith('### '):
                c.setFont("Helvetica-Bold", 11)
                c.drawString(self.left_margin, self.y_position, line[4:])
                self.y_position -= 0.2 * 72
                continue
            
            if '[ ]' in line or '[X]' in line:
                is_checked = '[X]' in line
                label = line.replace('[X]', '').replace('[ ]', '').strip()
                c.setFont("Helvetica", 10)
                c.rect(self.left_margin, self.y_position - 2, 12, 12)
                if is_checked:
                    c.setFont("ZapfDingbats", 10)
                    c.drawString(self.left_margin + 1, self.y_position, "4")
                c.setFont("Helvetica", 10)
                c.drawString(self.left_margin + 20, self.y_position, label)
                self.y_position -= 0.25 * 72
                continue
            
            if line.startswith('|') and '---' not in line:
                continue
            
            if '[' in line and ']' in line:
                matches = list(re.finditer(r'\[([^\]]+)\]', line))
                if matches:
                    c.setFont("Helvetica", 10)
                    last_end = 0
                    for match in matches:
                        before_text = line[last_end:match.start()]
                        if before_text:
                            c.drawString(self.left_margin + last_end * 5, self.y_position, before_text)
                        placeholder = match.group(1)
                        field_width = min(len(placeholder) * 10 + 40, 200)
                        field_x = self.left_margin + len(before_text) * 5 + len(before_text) * 5
                        c.setLineWidth(0.5)
                        c.rect(field_x, self.y_position - 3, field_width, 14)
                        c.setFont("Helvetica-Oblique", 7)
                        c.drawString(field_x + 2, self.y_position - 2, f"[{placeholder}]")
                        last_end = match.end()
                    self.y_position -= 0.25 * 72
                    continue
            
            c.setFont("Helvetica", 10)
            wrapped = self.wrap_text(line, 6 * 72)
            for wline in wrapped:
                if self.y_position < 1 * 72:
                    c.showPage()
                    self.y_position = height - 1 * 72
                c.drawString(self.left_margin, self.y_position, wline)
                self.y_position -= 0.2 * 72
            self.y_position -= 0.05 * 72
        
        c.save()
        return output_file

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python make_fillable.py <markdown-file> [output-pdf]")
        sys.exit(1)
    
    md_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    gen = FillablePDFGenerator()
    result = gen.generate_pdf(md_file, output_file)
    print(f"✓ Created fillable PDF: {result}")
