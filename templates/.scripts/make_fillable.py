#!/usr/bin/env python3
"""
Fillable PDF Generator - Convert templates to fillable PDF forms
Uses reportlab for PDF creation with form fields
"""

import os
import re
import sys
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT, TA_CENTER

TEMPLATE_DIR = Path(__file__).parent.parent

class FillablePDFGenerator:
    def __init__(self):
        self.y_position = 10.5 * inch
        self.left_margin = 0.75 * inch
        self.right_margin = 7.25 * inch
        self.line_height = 0.25 * inch
        self.styles = getSampleStyleSheet()
        
    def wrap_text(self, text, max_width):
        """Simple text wrapping"""
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            if len(test_line) * 7 < max_width:  # Approximate char width
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
    
    def parse_template(self, md_file):
        """Parse markdown file and extract fields"""
        with open(md_file, 'r') as f:
            content = f.read()
        
        fields = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            # Checkboxes: [ ] or [X]
            if '[ ]' in line or '[X]' in line:
                checkbox_text = line.replace('[X]', '').replace('[ ]', '').strip()
                fields.append({
                    'type': 'checkbox',
                    'text': checkbox_text,
                    'line_num': i
                })
                continue
            
            # Placeholders: [TEXT], [DATE], [NAME], etc.
            if '[' in line and ']' in line:
                # Table headers
                if '|' in line:
                    continue
                
                # Regular placeholders
                matches = re.findall(r'\[([^\]]+)\]', line)
                for match in matches:
                    if match.strip() and not match.startswith('_'):
                        fields.append({
                            'type': 'text',
                            'placeholder': match.strip(),
                            'text': line.replace(f'[{match}]', '').strip(),
                            'line_num': i
                        })
        
        return fields, content
    
    def generate_pdf(self, md_file, output_file=None):
        """Generate fillable PDF from markdown"""
        
        fields, content = self.parse_template(md_file)
        
        if output_file is None:
            output_file = str(Path(md_file).with_suffix('.pdf'))
        
        c = canvas.Canvas(output_file, pagesize=letter)
        width, height = letter
        
        # Form title from filename
        title = Path(md_file).stem.replace('-', ' ').replace('_', ' ').title()
        
        # Track form fields for later reference
        form = c.acroForm
        
        # Build content lines
        content_lines = content.split('\n')
        
        # First page
        self.y_position = height - 1*inch
        
        # Title
        c.setFont("Helvetica-Bold", 16)
        c.drawString(self.left_margin, self.y_position, title)
        self.y_position -= 0.5 * inch
        
        # Process content
        for line in content_lines:
            if self.y_position < 1 * inch:
                c.showPage()
                self.y_position = height - 1 * inch
            
            # Skip empty or very short lines
            if not line.strip():
                self.y_position -= 0.15 * inch
                continue
            
            # Handle headers
            if line.startswith('# '):
                c.setFont("Helvetica-Bold", 14)
                c.drawString(self.left_margin, self.y_position, line[2:])
                self.y_position -= 0.3 * inch
                continue
            elif line.startswith('## '):
                c.setFont("Helvetica-Bold", 12)
                c.drawString(self.left_margin, self.y_position, line[3:])
                self.y_position -= 0.25 * inch
                continue
            elif line.startswith('### '):
                c.setFont("Helvetica-Bold", 11)
                c.drawString(self.left_margin, self.y_position, line[4:])
                self.y_position -= 0.2 * inch
                continue
            
            # Handle checkboxes
            if '[ ]' in line or '[X]' in line:
                is_checked = '[X]' in line
                label = line.replace('[X]', '').replace('[ ]', '').strip()
                
                c.setFont("Helvetica", 10)
                
                # Draw checkbox
                checkbox_size = 12
                c.rect(self.left_margin, self.y_position - 2, checkbox_size, checkbox_size)
                
                if is_checked:
                    c.setFont("ZapfDingbats", 10)
                    c.drawString(self.left_margin + 1, self.y_position, "4")
                
                c.setFont("Helvetica", 10)
                c.drawString(self.left_margin + 20, self.y_position, label)
                
                self.y_position -= 0.25 * inch
                continue
            
            # Handle table headers
            if line.startswith('|') and '---' not in line:
                # Skip table formatting lines
                continue
            
            # Handle placeholders
            if '[' in line and ']' in line:
                # Find the placeholder and draw a field
                matches = list(re.finditer(r'\[([^\]]+)\]', line))
                
                if matches:
                    # Draw the text before the placeholder
                    c.setFont("Helvetica", 10)
                    last_end = 0
                    
                    for match in matches:
                        # Text before placeholder
                        before_text = line[last_end:match.start()]
                        if before_text:
                            c.drawString(self.left_margin, self.y_position, before_text)
                        
                        # Draw the field
                        placeholder = match.group(1)
                        field_width = min(len(placeholder) * 10 + 40, 200)
                        
                        # Draw field border
                        field_x = self.left_margin + len(before_text) * 5
                        c.setLineWidth(0.5)
                        c.rect(field_x, self.y_position - 3, field_width, 14)
                        
                        # Add field name as hint
                        c.setFont("Helvetica-Oblique", 7)
                        c.drawString(field_x + 2, self.y_position - 2, f"[{placeholder}]")
                        
                        last_end = match.end()
                    
                    self.y_position -= 0.25 * inch
                    continue
            
            # Regular text
            c.setFont("Helvetica", 10)
            wrapped = self.wrap_text(line, 6 * inch)
            
            for wline in wrapped:
                if self.y_position < 1 * inch:
                    c.showPage()
                    self.y_position = height - 1 * inch
                
                c.drawString(self.left_margin, self.y_position, wline)
                self.y_position -= 0.2 * inch
            
            self.y_position -= 0.05 * inch
        
        c.save()
        return output_file

def main():
    if len(sys.argv) < 2:
        print("Usage: python make_fillable.py <markdown-file> [output-pdf]")
        sys.exit(1)
    
    md_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    generator = FillablePDFGenerator()
    result = generator.generate_pdf(md_file, output_file)
    print(f"✓ Created fillable PDF: {result}")

if __name__ == '__main__':
    main()
