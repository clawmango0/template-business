# Template Design Standards

## Unified Template Style Guide v1.0

This document defines the consistent design and formatting for all templates.

---

## 1. Document Header

Every template MUST start with:

```markdown
# [Template Type]: [Template Name]

**Category:** {{CATEGORY}}
**Tier:** {{TIER}}
**Last Updated:** {{DATE}}
**Version:** 1.0

---

## Quick Info

| Field | Value |
|-------|-------|
| Company | {{COMPANY_NAME}} |
| Author | {{AUTHOR}} |
| Department | {{DEPARTMENT}} |
```

---

## 2. Placeholder Syntax

All placeholders MUST use this format:

- **Simple:** `{{PLACEHOLDER_NAME}}`
- **With Options:** `{{OPTION_1 | OPTION_2 | OPTION_3}}`
- **With Default:** `{{FIELD_NAME: default_value}}`
- **Conditional:** `[Optional section content]`

---

## 3. Section Headers

Use consistent hierarchy:

```markdown
## Section Title

### Subsection Title

#### Mini Section
```

---

## 4. Tables

### Standard Table
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Value 1 | Value 2 | Value 3 |

### Checklist Table
| Item | Description | Status |
|------|-------------|--------|
| [ ] | Task 1 | Pending |
| [x] | Task 2 | Complete |

---

## 5. Checkboxes

- Unchecked: `- [ ]`
- Checked: `- [x]`

---

## 6. Required Sections

All templates MUST include:

### Header Section
- Template name
- Category/Tier
- Version/Date
- Quick info table

### Content Sections
- Purpose/Overview
- Details/Instructions
- Examples (when helpful)

### Footer
```markdown
---

*Template: {{TEMPLATE_NAME}} | Use {{PLACEHOLDER}} syntax to customize*
```

---

## 7. Formatting Rules

### Emphasis
- **Bold** for important terms
- *Italic* for notes
- `Code` for technical items

### Lists
- Use bullets for unordered
- Use numbers for sequential steps
- Use tables for parallel data

### Links
- `[Link Text](URL)` for external references

---

## 8. Tier Standards

### Tier 1 (Basic - $5)
- Simple format
- Essential fields only
- 1-2 pages

### Tier 2 (Standard - $25)
- More sections
- Examples included
- 3-5 pages

### Tier 3 (Premium - $75+)
- Comprehensive
- Multiple examples
- 5-10+ pages

---

## 9. Template Structure by Category

### SOPs
1. Purpose
2. Scope
3. Responsible Parties
4. Procedure (step-by-step)
5. Related Documents

### HR
1. Overview
2. Policy Details
3. Procedures
4. Forms/Checklists
5. Legal/Compliance

### Finance
1. Transaction Details
2. Line Items/Tables
3. Calculations
4. Terms/Conditions
5. Signatures

### Marketing
1. Campaign Overview
2. Target Audience
3. Content/Messaging
4. Timeline
5. Metrics

### Project
1. Project Details
2. Tasks/Milestones
3. Resources
4. Timeline
5. Deliverables

---

## 10. Color/Coding (Optional)

When exported to other formats:

| Prefix | Meaning | Style |
|--------|---------|-------|
| {{REQ_}} | Required field | **Bold** |
| {{OPT_}} | Optional field | *Italic* |
| {{DATE_}} | Date field | [Brackets] |
| {{NAME_}} | Name field | Plain |

---

*Last Updated: 2026-02-24*
