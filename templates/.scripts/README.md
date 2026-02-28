# Template Converter

Convert markdown templates to PDF, Word, HTML — **no activation needed**.

---

## Quick Usage

```bash
# Just run directly - handles everything automatically!

# Fillable PDF (with form fields!)
.scripts/pdf pressure-washing/01-service-agreement.md

# Word document
pandoc pressure-washing/01-service-agreement.md -o output.docx

# HTML
pandoc pressure-washing/01-service-agreement.md -o output.html

# Or use the wrapper
.scripts/convert.sh pdf pressure-washing/*.md
```

---

## All-in-One Command

```bash
# Convert to ALL formats at once
.scripts/convert.sh all pressure-washing/01-service-agreement.md
```

Output:
- `01-service-agreement.pdf` (fillable!)
- `01-service-agreement.docx`
- `01-service-agreement.html`

---

## Format Options

| Command | Output | Fillable |
|---------|--------|----------|
| `.scripts/pdf file.md` | Fillable PDF | ✅ Yes |
| `pandoc file.md -o file.docx` | Word | ⚠ Basic |
| `pandoc file.md -o file.html` | HTML | ❌ No |

---

## Batch Convert

```bash
# All templates in a category
.scripts/convert.sh pdf pressure-washing/*.md

# All templates
.scripts/convert.sh pdf */01-*.md

# Everything
find . -name "*.md" ! -name "*SAMPLE*" -exec .scripts/pdf {} \;
```

---

## How It Works

- **PDF**: Uses reportlab (auto-installs to venv)
- **Word/HTML**: Uses pandoc (system installed)

The scripts automatically handle venv setup — just run them!

---

## Google Docs

Upload the **.html** or **.docx** to Google Drive → Open with Google Docs

---

*Last updated: February 2026*
