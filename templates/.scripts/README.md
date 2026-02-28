# Template Converter

Tools to convert markdown templates to PDF, Word, and other formats.

---

## Quick Start

```bash
# Convert to Word (.docx)
python3 .scripts/convert.py docx pressure-washing/01-service-agreement.md

# Convert to HTML
python3 .scripts/convert.py html pressure-washing/01-service-agreement.md

# Convert to all formats
python3 .scripts/convert.py all pressure-washing/01-service-agreement.md
```

---

## Requirements

- **pandoc** - Installed ✓
- **wkhtmltopdf** - For PDF (optional)

### Install wkhtmltopdf (if needed):
```bash
sudo apt install wkhtmltopdf
```

---

## Available Formats

| Format | Command | Notes |
|--------|---------|-------|
| Word | `docx` | ✓ Works |
| HTML | `html` | ✓ Works |
| PDF | `pdf` | Needs wkhtmltopdf |
| Google Docs | See below | Upload HTML |

---

## Google Docs Options

### Option 1: Upload to Google Drive
1. Go to docs.google.com
2. Click + New → File upload
3. Select your .html or .docx file
4. Right-click → Open with Google Docs

### Option 2: Google Docs Add-on
1. Open Google Docs
2. Extensions → Add-ons → Get add-ons
3. Search "Markdown"
4. Install "Markdown & highlight"

### Option 3: Drive Sync
1. Upload .docx to Google Drive
2. Right-click → Open with Google Docs

---

## Batch Conversion

Convert all templates in a folder:

```bash
# Convert all pressure-washing templates
for f in pressure-washing/*.md; do
    python3 .scripts/convert.py docx "$f";
done
```

---

## Alternative Online Converters

If local conversion fails:
- **cloudconvert.com** - Free tier
- **convertio.co** - Free tier  
- **pandoc.org/try** - Online pandoc

---

## Troubleshooting

### "wkhtmltopdf not found"
```bash
# Install via apt
sudo apt install wkhtmltopdf

# Or use alternative
python3 .scripts/convert.py html your-file.md
# Then upload HTML to Google Docs
```

### "Permission denied"
- Make scripts executable: `chmod +x .scripts/*.py`

---

## Using with Templates

Templates are in: `templates/[category]/`

| Category | Templates |
|----------|-----------|
| pressure-washing/ | Service Agreement, Checklist, etc. |
| pool-service/ | Service Agreement, Chemical Log, etc. |
| hr/ | Job Application, Handbook, etc. |
| operations/ | Vehicle Inspection, etc. |
| sales/ | Quotes, Intake Forms, etc. |
| financial/ | Invoices, Receipts, etc. |

Each has a `samples/` subfolder with filled examples.

---

*Last updated: February 2026*
