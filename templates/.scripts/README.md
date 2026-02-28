# Template Converter

Tools to convert markdown templates to PDF, Word, Google Docs, and **fillable forms**.

---

## Quick Start

```bash
# Activate the converter environment
source .scripts/venv/bin/activate

# Convert to Word (.docx)
python3 .scripts/convert.py docx pressure-washing/01-service-agreement.md

# Convert to HTML
python3 .scripts/convert.py html pressure-washing/01-service-agreement.md

# Convert to FILLABLE PDF (with form fields!)
python3 .scripts/make_fillable.py pressure-washing/01-service-agreement.md

# Convert to all formats
python3 .scripts/convert.py all pressure-washing/01-service-agreement.md
```

---

## Requirements

- **pandoc** - For Word/HTML conversion ✓ Installed
- **venv** - Python virtual environment ✓ Created

### Activate environment:
```bash
source .scripts/venv/bin/activate
```

---

## Available Formats

| Format | Command | Fillable | Notes |
|--------|---------|----------|-------|
| Word | `docx` | ⚠ Basic | Use Word forms |
| HTML | `html` | ❌ No | Upload to GDrive |
| **PDF** | `make_fillable.py` | ✅ **YES** | Form fields! |
| Google Docs | Upload | ⚠ Basic | Add forms manually |

---

## Fillable PDFs

The `make_fillable.py` script creates PDFs with interactive form fields:

### Features:
- ✅ Checkboxes (clickable)
- ✅ Text input fields (editable)
- ✅ Placeholder hints
- ✅ Professional formatting

### Usage:
```bash
# Single file
python3 .scripts/make_fillable.py pressure-washing/01-service-agreement.md

# Output to custom location
python3 .scripts/make_fillable.py input.md output.pdf

# Batch convert
for f in pressure-washing/*.md; do
    python3 .scripts/make_fillable.py "$f"
done
```

### Batch Convert All:
```bash
# All templates
for f in pressure-washing/*.md pool-service/*.md hr/*.md operations/*.md sales/*.md financial/*.md; do
    python3 .scripts/make_fillable.py "$f"
done

# All samples
for f in pressure-washing/samples/*.md hr/samples/*.md operations/samples/*.md sales/samples/*.md financial/samples/*.md; do
    python3 .scripts/make_fillable.py "$f"
done
```

---

## Google Docs Options

### Option 1: Upload to Google Drive
1. Go to docs.google.com
2. Click + New → File upload
3. Select your .html or .docx file
4. Right-click → Open with Google Docs
5. Insert → Checkboxes, Text boxes

### Option 2: Google Docs Add-on
1. Open Google Docs
2. Extensions → Add-ons → Get add-ons
3. Search "form" or "checkbox"
4. Install "Google Forms" add-on

### Option 3: Use Our Fillable PDF
- Our PDFs work in any PDF reader
- Fields work in: Adobe Acrobat, Preview, browser PDF viewers

---

## File Formats

Templates include all 4+ formats:

```
pressure-washing/
├── 01-service-agreement.md          ← Edit this
├── 01-service-agreement.docx       ← Word
├── 01-service-agreement.html        ← Web
├── 01-service-agreement.pdf         ← Fillable PDF ⭐
└── samples/
    ├── 01-service-agreement-SAMPLE.md
    ├── 01-service-agreement-SAMPLE.docx
    ├── 01-service-agreement-SAMPLE.html
    └── 01-service-agreement-SAMPLE.pdf
```

---

## Alternative Online Converters

If local conversion fails:
- **adobe.com/pdf-to-word** - PDF to Word
- **convertio.co** - Any to Any
- **pandoc.org/try** - Online pandoc

---

## Troubleshooting

### "venv not found"
```bash
cd .scripts
python3 -m venv venv
source venv/bin/activate
pip install pypdf reportlab fpdf
```

### "Permission denied"
```bash
chmod +x .scripts/*.py
```

---

*Last updated: February 2026*
