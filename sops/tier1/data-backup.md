# SOP: Data Backup & Recovery

**Company:** {{COMPANY_NAME}}
**Department:** IT Operations
**Document ID:** BACKUP-001

---

## 1. Purpose

Ensure critical business data is protected, backed up regularly, and can be recovered in case of data loss or disaster.

## 2. Scope

Applies to:
- File servers
- Databases
- Cloud storage
- Email systems
- Application data

---

## 3. Backup Types

| Type | Frequency | Retention | Purpose |
|------|-----------|-----------|---------|
| Full | Weekly | 30 days | Complete restore |
| Incremental | Daily | 30 days | Daily changes |
| Real-time | Continuous | 7 days | Point-in-time |
| Archive | Monthly | 7 years | Compliance |

---

## 4. Responsibilities

| Role | Responsibility |
|------|---------------|
| IT Manager | Oversee backup strategy |
| SysAdmin | Execute backups |
| Department Heads | Identify critical data |

---

## 5. Backup Schedule

### Daily Backups (2:00 AM)

| System | Type | Destination |
|--------|------|-------------|
| File Server | Incremental | Cloud |
| Database | Full | Local + Cloud |
| Email | Incremental | Cloud |

### Weekly Backups (Sunday 1:00 AM)

| System | Type | Destination |
|--------|------|-------------|
| All Systems | Full | Off-site |

---

## 6. Verification

### Daily
- [ ] Verify backup completion
- [ ] Check error logs

### Weekly
- [ ] Test restore to staging
- [ ] Verify file integrity

### Monthly
- [ ] Full restore test
- [ ] Document restore time

---

## 7. Recovery Procedures

### 7.1 File Recovery

1. Identify file(s) needed
2. Determine backup date
3. Retrieve from backup
4. Restore to original location
5. Verify integrity

### 7.2 System Recovery

1. Assess failure scope
2. Notify stakeholders
3. Provision replacement
4. Restore from backup
5. Test functionality
6. Bring online

### 7.3 Disaster Recovery

1. Activate DR plan
2. Contact cloud provider
3. Restore critical systems first
4. Sequence: DB → App → Files → Email

---

## 8. Off-Site Storage

| Backup Type | Location | Encryption |
|-------------|----------|------------|
| Primary | AWS S3 | AES-256 |
| Secondary | Azure Blob | AES-256 |

---

## 9. Testing Log

| Date | Type | Success | Notes |
|------|------|---------|-------|
| | File | Yes/No | |
| | System | Yes/No | |

---

## 10. Contact List

| Role | Name | Phone | Email |
|------|------|-------|-------|
| IT Lead | | | |
| SysAdmin | | | |
| Cloud Provider | | | |

---

## Revision History

| Version | Date | Author |
|---------|------|--------|
| 1.0 | {{DATE}} | {{AUTHOR}} |

---

*Data Backup & Recovery SOP - {{COMPANY_NAME}}*
