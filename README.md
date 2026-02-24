# Template Business Manager

**Professional document templates + web app for small businesses.**

---

## 🚀 Quick Start

### Run the Web App

```bash
# Navigate to webapp folder
cd template-business/webapp

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then open **http://localhost:5000**

---

## What's Included

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

### Web App Features

- ✅ User accounts & login
- ✅ Company management
- ✅ Create/Edit/Delete templates
- ✅ Fill forms from templates
- ✅ Save forms to database
- ✅ Search & filter forms
- ✅ Duplicate forms
- ✅ Version history
- ✅ Export: Markdown, Word, PDF, JSON
- ✅ Status tracking (draft/complete)

---

## Directory Structure

```
template-business/
├── README.md                    # This file
├── guides/                       # User guides
│   ├── sop-user-guide.md
│   ├── project-user-guide.md
│   ├── hr-user-guide.md
│   ├── finance-user-guide.md
│   └── executive-user-guide.md
├── webapp/                      # Flask web application
│   ├── app.py                  # Main application
│   ├── requirements.txt        # Python dependencies
│   ├── config.json             # Configuration
│   └── templates/              # HTML templates
├── sops/                       # Tier 1 SOPs
├── project/                    # Project templates
├── hr/                        # HR templates
├── finance/                   # Finance templates
├── executive/                 # Executive templates
├── legal/                     # Legal templates
├── marketing/                 # Marketing templates
├── customer-success/          # CS templates
├── operations/               # Operations templates
├── healthcare/               # Healthcare templates
├── construction/             # Construction templates
└── retail/                   # Retail templates
```

---

## Web App Usage

### First Time Setup

1. Run `python app.py`
2. Open http://localhost:5000
3. Click **Register** to create an account
4. Your company is automatically created

### Creating Forms

1. Go to Dashboard
2. Click on any template
3. Fill in the fields
4. Click Save

### Managing Templates

1. Click **Templates** in the nav
2. Click **New Template** to add your own
3. Or click **Edit** on existing templates to customize

### Managing Forms

1. Click **All Forms** to see all your forms
2. Use filters to search by status or template
3. Click **View** to see a form
4. Click **Edit** to modify
5. Click **Copy** to duplicate

### Exporting

- **Single form:** On form page, click Download Markdown/Word/PDF
- **All forms:** Click "Export All" for JSON backup

---

## Template Format

Templates use Markdown with `{{PLACEHOLDERS}}`:

```markdown
# Invoice

**Company:** {{COMPANY_NAME}}
**Date:** {{DATE}}

## Bill To
{{CLIENT_NAME}}
```

### Supported Placeholders

| Placeholder | Example |
|-------------|---------|
| `{{COMPANY_NAME}}` | Acme Corp |
| `{{DATE}}` | 2024-01-15 |
| `{{EMPLOYEE_NAME}}` | John Smith |
| `{{AMOUNT}}` | 1000 |
| Any field name | Custom field |

---

## Converting Templates

### Using Pandoc (Command Line)

```bash
# Markdown to Word
pandoc template.md -o template.docx

# Markdown to PDF
pandoc template.md -o template.pdf

# Markdown to HTML
pandoc template.md -o template.html
```

### Using the Web App

The web app automatically converts to:
- Markdown (.md)
- Word (.docx)
- PDF (via Pandoc)

---

## Adding Custom Templates

### Option 1: Via Web App

1. Go to `/template/new`
2. Fill in name, category, fields
3. Save

### Option 2: Add Manually

1. Create markdown file in appropriate folder
2. Use `{{FIELD_NAME}}` for placeholders
3. Add to `app.py` TEMPLATES dictionary

---

## Tech Stack

- **Backend:** Python Flask
- **Database:** SQLite
- **Frontend:** HTML/CSS/JavaScript
- **Conversion:** Pandoc, LibreOffice

---

## API Endpoints

```bash
# List all forms
GET /api/forms

# List all templates
GET /api/templates
```

---

## Troubleshooting

### "Module not found" errors

```bash
pip install -r requirements.txt
```

### Port already in use

```bash
python app.py --port 5001
```

### PDF export not working

Install Pandoc:
```bash
# Ubuntu/Debian
sudo apt install pandoc

# macOS
brew install pandoc

# Windows
# Download from https://pandoc.org/
```

---

## Contributing

1. Fork the repo
2. Add templates to appropriate folder
3. Submit pull request

---

## License

MIT License - Use freely for your business.

---

**GitHub:** https://github.com/clawmango0/template-business
**Web App:** http://localhost:5000 (when running)
