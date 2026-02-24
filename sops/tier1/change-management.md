# SOP: Change Management

**Company:** {{COMPANY_NAME}}
**Department:** IT Operations
**Document ID:** CM-001

---

## 1. Purpose

Ensure all changes to production systems are reviewed, approved, tested, and documented to minimize risk and maintain stability.

## 2. Scope

All changes to:
- Production servers and infrastructure
- Production applications
- Security configurations
- Network settings
- User access permissions

## 3. Change Types

| Type | Description | Examples | Approval |
|------|-------------|----------|----------|
| Standard | Low risk, routine | Patches, backups | Auto-approved |
| Normal | Standard changes | App updates, config | Manager |
| Emergency | Urgent fixes | Security patches | expedite |

## 4. Roles

| Role | Responsibility |
|------|----------------|
| Requestor | Submit change request |
| Reviewer | Technical assessment |
| Approver | Final authorization |
| Implementor | Execute the change |
| Validator | Verify success |

## 5. Procedure

### 5.1 Request

1. Complete Change Request Form
2. Include:
   - Description and purpose
   - Risk assessment
   - Rollback plan
   - Test plan
   - Implementation timeline

### 5.2 Review

1. Technical review (1-2 days)
2. Impact assessment
3. Risk evaluation
4. Resource allocation

### 5.3 Approval

| Change Type | Approver |
|-------------|----------|
| Standard | Auto |
| Normal | IT Manager |
| Emergency | CTO + Documentation |

### 5.4 Implementation

1. Schedule change (maintenance window)
2. Pre-change backup
3. Execute change
4. Document start time

### 5.5 Validation

1. Verify functionality
2. Check monitoring
3. Confirm no alerts
4. Document completion

### 5.6 Post-Implementation

1. Update documentation
2. Close change record
3. Schedule follow-up review

## 6. Emergency Change

For emergency changes:

1. Notify IT Manager immediately
2. Document as you go
3. Complete formal request within 24 hours
4. Post-mortem within 5 business days

## 7. Change Request Template

```
CHANGE REQUEST #[NUMBER]
---
Title: 
Requestor: 
Date Requested: 
Target Date: 

Description:
[What and why]

Risk Assessment:
[Low/Medium/High]

Rollback Plan:
[How to undo]

Test Plan:
[How to verify]

Impact:
[What's affected]
```

---

## Revision History

| Version | Date | Author |
|---------|------|--------|
| 1.0 | {{DATE}} | {{AUTHOR}} |

---

*Template customized for {{COMPANY_NAME}}*
