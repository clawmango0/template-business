# SOP: Identity & Access Management

**Company:** {{COMPANY_NAME}}
**Department:** IT Operations / Security
**Document ID:** IAM-001

---

## 1. Purpose

Establish a secure, standardized process for managing user identities, access credentials, and authentication across all company systems to protect data while enabling productivity.

## 2. Scope

Applies to all:
- Employee accounts
- Contractor accounts
- Service accounts
- Third-party integrations
- Physical access credentials

---

## 3. Core Principles

| Principle | Description |
|-----------|-------------|
| Least Privilege | Minimum access needed for job function |
| Need-to-Know | Access granted for specific purposes |
| Separation of Duties | No single person controls entire process |
| Audit Trail | All access logged and reviewable |

---

## 4. Tools & Systems

### 4.1 Password Manager (LastPass)

| Feature | Configuration |
|---------|---------------|
| Master Password | Minimum 16 characters, passphrase |
| MFA | Required for all users |
| Sharing | Allow but no plain-text |
| Offline | Disabled for sensitive accounts |

### 4.2 Identity Provider (IdP)

| System | Purpose |
|--------|---------|
| Google Workspace | SSO for cloud apps |
| Azure AD / Okta | Enterprise identity |
| JumpCloud | SMB IdP |

### 4.3 MFA Methods (Preferred Order)

1. Hardware Key (YubiKey) - **BEST**
2. Authenticator App (1Password, Authy)
3. SMS (Last resort - not recommended)

---

## 5. Account Lifecycle

### 5.1 New Employee Onboarding

```
Day -3  → Create accounts in IdP
Day -2  → Assign to department groups
Day -1  → Provision laptop
Day 0   → Provide credentials (in person or secure)
Day 1   → MFA enrollment
Day 7   → Security training completion
Day 30  → Access review
```

### 5.2 Access Request Process

```
1. Employee submits request (via IT ticket)
2. Manager approves
3. IT provisions access
4. User acknowledges receipt
5. Access logged
```

### 5.3 Access Request Form

| Field | Value |
|-------|-------|
| Requestor | |
| System/Application | |
| Access Level | [Read/Write/Admin] |
| Business Justification | |
| Duration | [Permanent/Temporary] |
| Manager Approval | |

### 5.4 Termination Process

```
Same Day:
- [ ] Disable IdP account
- [ ] Revoke SaaS access
- [ ] Remove from Slack/Teams
- [ ] Forward email
- [ ] Collect hardware

Within 24h:
- [ ] Remove from all groups
- [ ] Archive email
- [ ] Transfer files
- [ ] Revoke API keys
- [ ] Update shared passwords
```

---

## 6. Password Standards

### 6.1 Password Requirements

| Account Type | Min Length | Complexity | MFA Required |
|--------------|------------|------------|--------------|
| Master (LastPass) | 16 chars | No | Yes |
| Work Email | 12 chars | Yes | Yes |
| SaaS Apps | 12 chars | Yes | If available |
| Service Accounts | 20 chars | Yes | N/A |

### 6.2 Prohibited Practices

- ❌ Reusing passwords across systems
- ❌ Sharing passwords via email/chat
- ❌ Writing passwords on paper
- ❌ Using personal info in passwords
- ❌ Password in URL or query string

---

## 7. LastPass Configuration

### 7.1 Admin Console Settings

| Setting | Value |
|---------|-------|
| Minimum master password score | Strong |
| MFA required | Yes |
| Re-prompt for master password | 30 minutes |
| Disable master password hint | Yes |
| Exporting vault | Disabled |

### 7.2 Shared Folders

| Folder | Who Has Access | Can Share |
|--------|----------------|-----------|
| Company Shared | All employees | Admins only |
| Department | Department members | Dept lead |
| Admin Only | IT admins | No |

### 7.3 Emergency Access

| Role | Person | Contact |
|------|--------|---------|
| Primary | | |
| Secondary | | |
| Audit | | |

---

## 8. API Key Management

### 8.1 API Key Lifecycle

```
Request → Approval → Generation → Distribution → Usage → Rotation → Revocation
```

### 8.2 API Key Standards

| Requirement | Standard |
|-------------|----------|
| Storage | Environment variables, never in code |
| Access | Limited to needed services |
| Rotation | Every 90 days |
| Scoping | Per-environment (dev/staging/prod) |
| Monitoring | Log all API calls |

### 8.3 API Key Request Form

| Field | Value |
|-------|-------|
| Developer | |
| Service | |
| Purpose | |
| Permissions needed | |
| Environment | |
| Expiration | |

### 8.4 Revocation Checklist

- [ ] Identify all keys for user/service
- [ ] Revoke in each system
- [ ] Update any docs
- [ ] Confirm in logs

---

## 9. Physical Access

### 9.1 Badge Access Levels

| Level | Access | Approval |
|-------|--------|----------|
| 1 | Building entry | HR |
| 2 | General office | HR |
| 3 | Server room | IT Manager |
| 4 | Executive areas | CEO |

### 9.2 Physical Key Management

- [ ] Keys numbered and logged
- [ ] Sign-out log maintained
- [ ] Annual audit
- [ ] Lost key = rekey immediately

---

## 10. Access Reviews

### 10.1 Quarterly Reviews

| Review | Owner | Frequency |
|--------|-------|-----------|
| SaaS access | Dept head | Quarterly |
| Admin accounts | IT | Monthly |
| Physical access | Security | Quarterly |

### 10.2 Access Review Form

| User | System | Current Access | Still Needed | Action |
|------|--------|----------------|--------------|--------|
| | | | Yes/No | Keep/Revoke |

---

## 11. Incident Response

### Compromised Credential Procedure

```
1. IMMEDIATE: Disable account
2. Within 1hr: Change all passwords
3. Within 4hr: Review access logs
4. Within 24hr: Complete incident report
5. Within 72hr: Post-mortem & remediation
```

---

## Appendix: Quick Reference

| Task | Tool | Where |
|------|------|-------|
| Reset password | LastPass | Vault |
| Request access | Jira/ServiceNow | IT portal |
| Report incident | Slack/Email | IT team |
| MFA setup | LastPass/Authy | Account settings |

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{DATE}} | {{AUTHOR}} | Initial release |

---

*Identity & Access Management - {{COMPANY_NAME}}*
