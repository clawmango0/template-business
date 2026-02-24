#!/bin/bash
# Template Converter - Generate Multiple Formats
# Usage: ./convert.sh <input.md> [output_name]

INPUT="$1"
OUTPUT="${2:-$(basename $INPUT .md)}"

if [ -z "$INPUT" ]; then
    echo "Usage: $0 <input.md> [output_name]"
    echo "Example: $0 sops/tier1/onboarding.md MyOnboarding"
    exit 1
fi

echo "Converting $INPUT to multiple formats..."

# Create output directory
mkdir -p output

# Convert to Word (.docx)
echo "  → Word (.docx)"
pandoc "$INPUT" -o "output/${OUTPUT}.docx" 2>/dev/null

# Convert to PDF
echo "  → PDF"
pandoc "$INPUT" -o "output/${OUTPUT}.pdf" 2>/dev/null

# Convert to HTML
echo "  → HTML"
pandoc "$INPUT" -o "output/${OUTPUT}.html" 2>/dev/null

# Convert to plain text
echo "  → Plain Text"
pandoc "$INPUT" -t plain -o "output/${OUTPUT}.txt" 2>/dev/null

echo ""
echo "✓ Generated formats in output/ directory:"
ls -la output/

echo ""
echo "To create Fillable PDF with LibreOffice:"
echo "  libreoffice --headless --convert-to pdf --outdir output/ ${OUTPUT}.docx"
