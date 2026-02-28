#!/bin/bash
# Template Converter - Convert markdown templates to PDF, Word, Google Docs

TEMPLATE_DIR="$(dirname "$0")/.."

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

usage() {
    echo "Usage: $0 <format> <template-file>"
    echo ""
    echo "Formats:"
    echo "  pdf     - Convert to PDF"
    echo "  docx    - Convert to Word (.docx)"
    echo "  all     - Convert to all formats"
    echo ""
    echo "Examples:"
    echo "  $0 pdf pressure-washing/01-service-agreement.md"
    echo "  $0 docx hr/01-employee-handbook-acknowledgment.md"
    echo "  $0 all financial/01-invoice.md"
    exit 1
}

convert_pdf() {
    local input="$1"
    local output="${input%.md}.pdf"
    
    echo -e "${YELLOW}Converting to PDF: $input → $output${NC}"
    
    pandoc "$input" \
        -o "$output" \
        --pdf-engine=wkhtmltopdf \
        --css="$TEMPLATE_DIR/.scripts/style.css" \
        --standalone \
        --toc \
        --toc-depth=2 \
        -V mainfont="Helvetica" \
        -V fontsize=11pt \
        -V geometry=margin=1in
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ PDF created: $output${NC}"
    else
        echo -e "${RED}✗ PDF conversion failed${NC}"
    fi
}

convert_docx() {
    local input="$1"
    local output="${input%.md}.docx"
    
    echo -e "${YELLOW}Converting to Word: $input → $output${NC}"
    
    pandoc "$input" \
        -o "$output" \
        --standalone \
        --toc \
        --toc-depth=2 \
        --reference-doc="$TEMPLATE_DIR/.scripts/template.docx"
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ Word doc created: $output${NC}"
    else
        # Try without reference doc
        pandoc "$input" -o "$output" --standalone --toc
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✓ Word doc created: $output${NC}"
        else
            echo -e "${RED}✗ Word conversion failed${NC}"
        fi
    fi
}

convert_all() {
    local input="$1"
    convert_pdf "$input"
    convert_docx "$input"
}

# Main
if [ $# -lt 2 ]; then
    usage
fi

FORMAT="$1"
INPUT="$2"

if [ ! -f "$INPUT" ]; then
    echo -e "${RED}Error: File not found: $INPUT${NC}"
    exit 1
fi

case "$FORMAT" in
    pdf)
        convert_pdf "$INPUT"
        ;;
    docx)
        convert_docx "$INPUT"
        ;;
    all)
        convert_all "$INPUT"
        ;;
    *)
        echo -e "${RED}Unknown format: $FORMAT${NC}"
        usage
        ;;
esac
