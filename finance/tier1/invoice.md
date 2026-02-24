# Invoice Template

**Category:** Finance
**Tier:** Tier 1 (Basic)
**Last Updated:** {{DATE}}
**Version:** 1.0

---

## Quick Info

| Field | Value |
|-------|-------|
| Company | {{COMPANY_NAME}} |
| Author | {{AUTHOR}} |
| Department | Finance |
| Invoice ID | INV-{{YYYY}}-#### |

---

## Header Information

### From (Sender)
{{COMPANY_NAME}}
{{ADDRESS}}
{{CITY, STATE ZIP}}
{{EMAIL}} | {{PHONE}}

### To (Bill To)
{{CLIENT_NAME}}
{{CLIENT_COMPANY}}
{{ADDRESS}}
{{CITY, STATE ZIP}}

---

## Invoice Details

| Field | Value |
|-------|-------|
| Invoice Number | INV-{{YYYY}}-#### |
| Invoice Date | {{DATE}} |
| Due Date | {{DUE_DATE}} |
| Payment Terms | {{NET_30 | NET_15 | DUE_ON_RECEIPT}} |

---

## Line Items

| # | Description | Quantity | Unit Price | Total |
|---|-------------|----------|------------|-------|
| 1 | {{SERVICE_OR_PRODUCT}} | {{QTY}} | ${{PRICE}} | ${{LINE_TOTAL}} |
| 2 | | | $ | $ |
| 3 | | | $ | $ |
| 4 | | | $ | $ |
| 5 | | | $ | $ |
|   | | **Subtotal** | | **${{SUBTOTAL}}** |
|   | | Tax ({{TAX_RATE}}%) | | **${{TAX_AMOUNT}}** |
|   | | **TOTAL DUE** | | **${{TOTAL}}** |

---

## Payment Information

### Payment Methods
- **Bank Transfer:** {{BANK_ACCOUNT}}
- **Check:** Mail to address above
- **Card:** {{PAYMENT_LINK}}

### Notes
- Please include invoice number on payment
- Late payments subject to {{LATE_FEE_%}}% fee
- Questions? Contact {{CONTACT_EMAIL}}

---

## Terms & Conditions

1. Payment is due by {{DUE_DATE}}
2. Late payments may incur a {{LATE_FEE_%}}% monthly fee
3. All services are billed as described
4. Disputes must be submitted within {{DISPUTE_DAYS}} days

---

*Template: Invoice-Template | Use {{PLACEHOLDER}} syntax to customize*
