# Template Data Elements Reference

Common data fields for business templates - use these placeholders consistently.

---

## Company Information

| Element | Placeholder | Example |
|---------|-------------|---------|
| Company Name | `{{COMPANY_NAME}}` | Acme Corp |
| Company Address | `{{COMPANY_ADDRESS}}` | 123 Main St |
| City, State ZIP | `{{CITY_STATE_ZIP}}` | Austin, TX 78701 |
| Company Phone | `{{COMPANY_PHONE}}` | (555) 123-4567 |
| Company Email | `{{COMPANY_EMAIL}}` | info@acme.com |
| Website | `{{COMPANY_WEBSITE}}` | acme.com |
| Tax ID | `{{TAX_ID}}` | XX-XXXXXXX |
| Industry | `{{INDUSTRY}}` | Technology |

---

## People & Roles

| Element | Placeholder | Example |
|---------|-------------|---------|
| Contact Name | `{{CONTACT_NAME}}` | John Smith |
| Job Title | `{{JOB_TITLE}}` | CEO |
| Department | `{{DEPARTMENT}}` | Engineering |
| Manager | `{{MANAGER_NAME}}` | Jane Doe |
| Employee ID | `{{EMPLOYEE_ID}}` | EMP-001 |
| Start Date | `{{START_DATE}}` | 2026-03-01 |

---

## Financial

| Element | Placeholder | Example |
|---------|-------------|---------|
| Invoice Number | `{{INVOICE_NUM}}` | INV-2026-0001 |
| Invoice Date | `{{INVOICE_DATE}}` | 2026-02-24 |
| Due Date | `{{DUE_DATE}}` | 2026-03-24 |
| Amount | `{{AMOUNT}}` | $1,000.00 |
| Subtotal | `{{SUBTOTAL}}` | $900.00 |
| Tax Rate | `{{TAX_RATE}}` | 8.25% |
| Tax Amount | `{{TAX_AMOUNT}}` | $82.50 |
| Total | `{{TOTAL}}` | $982.50 |
| Payment Terms | `{{PAYMENT_TERMS}}` | Net 30 |
| Bank Account | `{{BANK_ACCOUNT}}` | XXXXX1234 |

---

## Dates & Times

| Element | Placeholder | Example |
|---------|-------------|---------|
| Current Date | `{{DATE}}` | 2026-02-24 |
| Year | `{{YEAR}}` | 2026 |
| Month | `{{MONTH}}` | February |
| Deadline | `{{DEADLINE}}` | 2026-03-15 |
| Start Time | `{{START_TIME}}` | 9:00 AM |
| End Time | `{{END_TIME}}` | 5:00 PM |
| Duration | `{{DURATION}}` | 2 hours |

---

## Project Management

| Element | Placeholder | Example |
|---------|-------------|---------|
| Project Name | `{{PROJECT_NAME}}` | Website Redesign |
| Project ID | `{{PROJECT_ID}}` | PRJ-001 |
| Project Manager | `{{PROJECT_MANAGER}}` | Jane Smith |
| Budget | `{{BUDGET}}` | $50,000 |
| Start Date | `{{PROJECT_START}}` | 2026-01-01 |
| End Date | `{{PROJECT_END}}` | 2026-06-30 |
| Milestone | `{{MILESTONE}}` | Beta Launch |
| Task | `{{TASK}}` | Design mockups |

---

## Marketing

| Element | Placeholder | Example |
|---------|-------------|---------|
| Campaign Name | `{{CAMPAIGN_NAME}}` | Spring Sale |
| Target Audience | `{{TARGET_AUDIENCE}}` | SMB Owners |
| Budget | `{{MARKETING_BUDGET}}` | $10,000 |
| Channel | `{{CHANNEL}}` | Email |
| CTA | `{{CTA}}` | Buy Now |
| Hashtags | `{{HASHTAGS}}` | #Sale #Spring |

---

## Sales

| Element | Placeholder | Example |
|---------|-------------|---------|
| Lead Name | `{{LEAD_NAME}}` | ABC Company |
| Deal Value | `{{DEAL_VALUE}}` | $25,000 |
| Probability | `{{PROBABILITY}}` | 75% |
| Close Date | `{{CLOSE_DATE}}` | 2026-03-31 |
| Sales Stage | `{{STAGE}}` | Proposal |

---

## Legal & Compliance

| Element | Placeholder | Example |
|---------|-------------|---------|
| Contract ID | `{{CONTRACT_ID}}` | CNT-2026-001 |
| Effective Date | `{{EFFECTIVE_DATE}}` | 2026-01-01 |
| Expiration Date | `{{EXPIRATION_DATE}}` | 2027-01-01 |
| Jurisdiction | `{{JURISDICTION}}` | Texas |
| Governing Law | `{{GOVERNING_LAW}}` | State of Texas |

---

## Standard Options

| Element | Placeholder | Options |
|---------|-------------|---------|
| Status | `{{STATUS}}` | Draft, Active, Complete, Cancelled |
| Priority | `{{PRIORITY}}` | Low, Medium, High, Critical |
| Type | `{{TYPE}}` | Internal, External |
| Location | `{{LOCATION}}` | Remote, Hybrid, On-site |
| Employment | `{{EMPLOYMENT_TYPE}}` | Full-time, Part-time, Contract |

---

## Placeholder Syntax Variations

| Type | Syntax | Use Case |
|------|--------|----------|
| Simple | `{{FIELD}}` | Any text field |
| With Default | `{{FIELD: default}}` | Pre-fill suggestion |
| Options | `{{FIELD: opt1 \| opt2}}` | Dropdown selection |
| Conditional | `[Optional section]` | Optional content |

---

*Reference: Use these placeholders consistently across all templates*
