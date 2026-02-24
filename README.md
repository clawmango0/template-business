# Template Business Manager

**Professional document templates for small businesses.**

---

## Overview

A comprehensive collection of business templates covering SOPs, HR, Project Management, Finance, Legal, Marketing, and more. Includes a web application for creating, storing, and managing filled templates.

---

## Features

### 50+ Templates

| Category | Templates |
|----------|----------|
| **SOPs** | Onboarding, Incident Response, Change Management, Vendor Mgmt, Data Backup, SaaS Selection, Access Mgmt, Physical Security, SaaS Onboarding |
| **Project** | Charter, Status Report, Meeting Notes, RACI, Risk Register, Decision Log, Retrospective |
| **HR** | Handbook, Job Description, Performance Review, IT Onboarding |
| **Finance** | Invoice, Expense Report, Budget Tracker, Equipment Inventory |
| **Executive** | Board Update, QBR, OKR Tracker |
| **Legal** | NDA, Contractor Agreement, Employment Offer, Privacy Policy, Terms of Service |
| **Marketing** | Campaign Brief |
| **Customer Success** | Success Plan |
| **Operations** | Maintenance Log, Shift Handover, Client Onboarding |
| **Healthcare** | HIPAA Policy |
| **Construction** | Project Checklist |
| **Retail** | Store Opening Checklist |

### Web Application

- ✅ Create forms from 50+ templates
- ✅ Save to SQLite database
- ✅ Search previous forms
- ✅ Export to Markdown, Word (DOCX), PDF
- ✅ Edit existing forms
- ✅ Delete forms
- ✅ Status tracking (draft/complete)
- ✅ REST API

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/clawmango0/template-business.git
cd template-business

# Set up web app
cd webapp
pip install -r requirements.txt

# Run the app
python app.py
```

Then open http://localhost:5000

---

## Templates

### Using Templates

Each template uses {{PLACEHOLDERS}} for customization:

```
{{COMPANY_NAME}} → Your Company
{{DATE}} → 2024-01-15
{{AUTHOR}} → Document Owner
```

### Converting Formats

```bash
# Convert markdown to Word
pandoc template.md -o template.docx

# Convert markdown to PDF
pandoc template.md -o template.pdf
```

---

## Web App Features

### Create Forms
1. Select template from home page
2. Fill in fields
3. Save to database

### Manage Forms
- View all forms
- Search by title, company, content
- Edit existing forms
- Delete forms

### Export
- Markdown (.md)
- Word (.docx)
- PDF (via Pandoc)

### API

```bash
# List all forms
GET /api/forms

# List all templates
GET /api/templates
```

---

## Directory Structure

```
template-business/
├── README.md
├── guides/              # User guides
│   ├── sop-user-guide.md
│   ├── project-user-guide.md
│   ├── hr-user-guide.md
│   ├── finance-user-guide.md
│   └── executive-user-guide.md
├── webapp/             # Flask web app
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
├── sops/               # Tier 1 SOPs
├── project/
├── hr/
├── finance/
├── executive/
├── legal/
├── marketing/
├── customer-success/
├── operations/
├── healthcare/
├── construction/
└── retail/
```

---

## Categories by Tier

### Tier 1 ($5-10)
Basic templates with essential fields.

### Tier 2 ($25-50)
More comprehensive templates with additional sections.

---

## Customization

### Adding Templates

1. Create markdown file in appropriate category folder
2. Use {{PLACEHOLDER}} syntax for customizable fields
3. Add template definition to `app.py` TEMPLATES dict

### Extending Web App

- Modify `app.py` to add features
- Edit templates in `templates/` folder
- Update database schema in `init_db()`

---

## Tech Stack

- **Templates:** Markdown with placeholders
- **Conversion:** Pandoc, LibreOffice
- **Web App:** Flask, SQLite
- **Styling:** Custom CSS

---

## License

MIT License - Use freely for your business.

---

## Contributing

1. Fork the repo
2. Add templates
3. Submit pull request

---

**GitHub:** https://github.com/clawmango0/template-business
