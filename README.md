# Template Business - Multi-Format Document Templates

**Mission:** Help small companies act big with professional templates.

## Product Tiers

| Tier | Price | Customization |
|------|-------|---------------|
| **Starter** | $5-10 | Company name only |
| **Professional** | $25-50 | Name + logo + minor edits |
| **Premium** | $75-100 | Full customization + revisions |
| **Enterprise** | $150+ | White-label + priority support |

## Categories

1. **SOPs** - Standard Operating Procedures
2. **Project Management** - Charters, reports, tracking
3. **HR & People** - Handbooks, forms, policies
4. **Finance & Admin** - Invoices, budgets, inventory
5. **Executive & Strategy** - Board decks, QBRs, one-pagers
6. **Legal & Compliance** - NDAs, agreements (careful!)

## Format Support

| Format | How Generated | Notes |
|--------|--------------|-------|
| **Markdown** | Source | Editable, portable |
| **Word (.docx)** | Pandoc | Most common |
| **PDF** | Pandoc/LibreOffice | Professional |
| **Fillable PDF** | LibreOffice | Interactive forms |
| **Google Doc** | Import instructions | User imports |

## Structure

```
template-business/
├── README.md
├── sops/
│   ├── tier1/  (basic SOPs)
│   ├── tier2/  (expanded SOPs)
│   ├── tier3/  (full SOP bundles)
│   └── tier4/  (custom SOPs)
├── project/
├── hr/
├── finance/
├── executive/
└── legal/
```

## Generation Tools

- **Pandoc** - Convert between formats
- **LibreOffice** - PDF and fillable forms
- **Markdown** - Source format

## Usage

```bash
# Convert markdown to Word
pandoc template.md -o template.docx

# Convert markdown to PDF
pandoc template.md -o template.pdf

# Convert to fillable PDF (LibreOffice)
libreoffice --headless --convert-to pdf template.md
```

---

*Building the template empire one document at a time.*
