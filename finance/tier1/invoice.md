# Invoice Template

**From:**
{{COMPANY_NAME}}
[Address]
[City, State ZIP]
[Email] | [Phone]

**Bill To:**
[Client Name]
[Client Company]
[Address]
[City, State ZIP]

---

## Invoice Details

| Field | Value |
|-------|-------|
| Invoice # | INV-{{YYYY}}-#### |
| Date | {{DATE}} |
| Due Date | [Net 30] |
| Terms | Net 30 |

---

## Line Items

| # | Description | Quantity | Unit Price | Total |
|---|-------------|----------|------------|-------|
| 1 | [Service/Product] | 1 | $ | $ |
| 2 | | | $ | $ |
| 3 | | | $ | $ |
| | | **Subtotal** | | **$** |
| | | Tax (0%) | | $ |
| | | **TOTAL** | | **$** |

---

## Payment Information

**Payment Due:** $[AMOUNT]

**Payment Methods:**
- Bank Transfer: [Account Info]
- PayPal: [email]
- Check: Mail to address above

**Please include invoice number with payment.**

---

## Notes

[Additional notes or terms]

---

## Contact

Questions? Contact [Name] at [email] or [phone]

---

*Invoice {{INV-YYYY-####}} - {{COMPANY_NAME}}*
