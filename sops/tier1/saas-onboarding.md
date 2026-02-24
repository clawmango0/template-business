# SOP: SaaS Onboarding & Offboarding

**Company:** {{COMPANY_NAME}}
**Department:** IT Operations
**Document ID:** SaaS-002

---

## 1. Purpose

Standardize the process for provisioning and deprovisioning user access to SaaS applications to maintain security and compliance during employee lifecycle changes.

## 2. Scope

Applies to all SaaS/cloud applications including:
- Productivity (Google Workspace, Microsoft 365)
- Communication (Slack, Teams, Zoom)
- Development (GitHub, Jira, Vercel)
- Business (Salesforce, HubSpot, QuickBooks)
- Security (LastPass, 1Password, Cloudflare)

---

## 3. Tool Integration Matrix

### 3.1 Primary Integration Stack

| Category | Primary Tool | SSO | SCIM | Admin Portal |
|----------|-------------|-----|------|--------------|
| Identity | Google Workspace | - | - | admin.google.com |
| Password | LastPass | SAML | ✓ | admin.lastpass.com |
| Communication | Slack | SAML | ✓ | my.slack.com |
| Development | GitHub | SAML | ✓ | github.com/settings |
| Project | Jira | SAML | ✓ | [company].atlassian.net |
| Storage | Google Drive | - | ✓ | drive.google.com |

### 3.2 SCIM Capability

| App | SCIM Supported | Auto-provision |
|-----|----------------|----------------|
| Google Workspace | Yes | Groups + Users |
| Slack | Yes | Members + Channels |
| GitHub | Yes | Team membership |
| Atlassian | Yes | Users + Projects |
| Azure AD | Yes | Full sync |
| Okta | Yes | Full integration |

---

## 4. New Employee Onboarding

### 4.1 Pre-Day 1 (IT Preparation)

| Task | Owner | Tool | Completion |
|------|-------|------|------------|
| Create Google account | IT | Admin console | -3 days |
| Add to required groups | IT | Admin console | -3 days |
| Create LastPass vault | IT | LastPass | -2 days |
| Provision laptop | IT | - | -2 days |
| Add to Slack workspace | IT | Slack admin | -1 day |
| Add to GitHub org | IT | GitHub | -1 day |
| Create billing access | Finance | Vendor portal | -1 day |

### 4.2 Day 1 (Employee Setup)

| Task | Owner | Tool | Notes |
|------|-------|------|-------|
| Hand off laptop | IT/HR | In-person | Review policy |
| Set master password | Employee | LastPass | 16+ chars |
| Enable MFA | Employee | Auth app | Required |
| Complete security training | Employee | KnowBe4/LMS | Within 24h |
| Join Slack channels | Employee | Slack | #general, #team |
| Review handbook | Employee | Notion/Google | Within 24h |

### 4.3 Day 1-7 (Configuration)

| Task | Owner | Tool | Due |
|------|-------|------|-----|
| Set up email signature | Employee | Gmail | Day 1 |
| Configure calendar sharing | Employee | Google Calendar | Day 2 |
| Install required software | Employee | Company portal | Day 2 |
| Request necessary access | Employee | IT ticket | Day 3 |
| Complete onboarding checklist | Employee | HR system | Day 5 |
| Meet with manager | Manager | - | Day 5 |

### 4.4 First Month

| Task | Owner | Frequency |
|------|-------|-----------|
| Access review check | Manager | Day 30 |
| Training completion | Employee | Day 30 |
| Feedback session | Manager | Day 30 |

---

## 5. Offboarding Process

### 5.1 Departure Notice

| Timeline | Action |
|----------|--------|
| 2 weeks notice | Initiate offboarding ticket |
| 1 week notice | Schedule knowledge transfer |
| 3 days notice | Begin access revocation |
| Last day | Complete all revocations |

### 5.2 Same-Day Actions (Critical)

```
┌─────────────────────────────────────────────────────────┐
│ IMMEDIATE - Before Employee Leaves                      │
├─────────────────────────────────────────────────────────┤
│ [ ] Disable Google account (suspend, don't delete)     │
│ [ ] Revoke LastPass access                             │
│ [ ] Remove from Slack (don't post publicly)            │
│ [ ] Remove from GitHub organizations                    │
│ [ ] Remove from Jira/Confluence                        │
│ [ ] Remove from cloud infrastructure (AWS, GCP, Azure)│
│ [ ] Remove from VPN                                     │
│ [ ] Revoke building access                             │
│ [ ] Forward email to manager                            │
│ [ ] Collect laptop and badges                          │
└─────────────────────────────────────────────────────────┘
```

### 5.3 Post-Departure (Within 24-48h)

| Task | Owner | Tool |
|------|-------|------|
| Transfer file ownership | IT | Google Drive |
| Transfer calendar ownership | IT | Google Calendar |
| Update shared passwords | IT | LastPass |
| Remove from all groups | IT | All platforms |
| Archive email | IT | Google Admin |
| Convert to shared mailbox | IT | Google Workspace |
| Revoke API keys | IT | Various |
| Review audit logs | Security | SIEM |
| Update documentation | IT | Wiki |

### 5.4 Equipment Return Checklist

| Item | Serial # | Returned | Condition |
|------|----------|----------|-----------|
| Laptop | | ✓/✗ | |
| Badge | | ✓/✗ | |
| Phone | | ✓/✗ | |
| Headphones | | ✓/✗ | |
| Charger | | ✓/✗ | |
| Other | | ✓/✗ | |

---

## 6. Role Changes (Internal Moves)

When employee changes teams:

```
1. Current manager approves transfer
2. IT receives ticket with new role
3. Remove access from old team resources
4. Add access to new team resources
5. Update groups and permissions
6. Document in HR system
7. Confirm with new manager
```

---

## 7. Automated Provisioning (SCIM)

### 7.1 Google Workspace → LastPass

```
Employee created in Google → Auto-created in LastPass
Employee moved to group → Auto-added to shared folder
Employee suspended → Auto-revoked access
```

### 7.2 Okta Workflow (If Using Okta)

```
New Hire → Okta profile → All apps provisioned
Role change → Okta groups update → App access updates  
Terminate → Okta deactivate → All apps revoked
```

---

## 8. Emergency Offboarding

If immediate termination required:

| Time | Action |
|------|--------|
| 0 minutes | Disable Okta/IdP account |
| 5 minutes | Change all shared passwords |
| 15 minutes | Remove from Slack |
| 30 minutes | Revoke cloud access |
| 1 hour | Physical security sweep |

---

## 9. Audit & Compliance

### 9.1 Monthly Checks

- [ ] Review newly provisioned accounts
- [ ] Verify terminated accounts disabled
- [ ] Check for orphan accounts
- [ ] Audit admin access

### 9.2 Quarterly Reviews

- [ ] Access certification by managers
- [ ] Privileged access review
- [ ] Review service accounts
- [ ] Compliance reporting

---

## Appendix: Quick Command Reference

| Action | Tool | Command/API |
|--------|------|-------------|
| Disable user | Google | gam update user |
| Remove from group | Google | gam delete group |
| Revoke tokens | Google | gam revoke |
| Disable vault | LastPass | LP admin console |
| Remove from org | GitHub | API call |
| Disable device | Jamf/MDM | MDM command |

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{DATE}} | {{AUTHOR}} | Initial release |

---

*SaaS Onboarding & Offboarding - {{COMPANY_NAME}}*
