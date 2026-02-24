# SOP: Incident Response

**Company:** {{COMPANY_NAME}}
**Department:** IT Operations
**Document ID:** IR-001

---

## 1. Purpose

This procedure defines the process for detecting, responding to, and recovering from IT security incidents to minimize impact on business operations.

## 2. Scope

Applies to all security incidents affecting:
- Company systems and networks
- Customer data
- Employee credentials
- Business continuity

## 3. Severity Levels

| Level | Description | Response Time |
|-------|-------------|---------------|
| **P1 - Critical** | Data breach, ransomware, complete system outage | Immediate |
| **P2 - High** | Partial outage, suspected breach, malware | 1 hour |
| **P3 - Medium** | Account compromise, phishing attempt | 4 hours |
| **P4 - Low** | Failed login attempts, policy violations | 24 hours |

## 4. Incident Response Team

| Role | Name | Phone | Email |
|------|------|-------|-------|
| IR Lead | | | |
| Security Analyst | | | |
| IT Manager | | | |
| Communications | | | |
| Legal/Compliance | | | |

## 5. Procedure

### 5.1 Detection & Identification

1. Monitor alerts from security tools
2. User reports of suspicious activity
3. Third-party notifications
4. Log analysis and correlation

**Questions to answer:**
- What systems are affected?
- What data is at risk?
- How did the incident occur?
- What's the scope?

### 5.2 Containment

**Immediate (Short-term):**
- Isolate affected systems
- Block malicious IPs/domains
- Disable compromised accounts
- Preserve evidence

**Long-term:**
- Patch vulnerabilities
- Reset credentials
- Implement additional monitoring

### 5.3 Eradication

- Remove malware/threats
- Patch exploited vulnerabilities
- Close attack vectors
- Verify clean state

### 5.4 Recovery

- Restore systems from clean backups
- Verify system functionality
- Monitor for recurrence
- Gradual service restoration

### 5.5 Post-Incident

- Document lessons learned
- Update procedures
- Implement improvements
- Report to stakeholders

## 6. Communication Template

```
INCIDENT ALERT - [SEVERITY]
---
Type: 
Systems Affected: 
Impact: 
Status: 
Action Required: 
Next Update: 
```

## 7. Escalation Matrix

| Severity | Notify | Escalate To |
|----------|--------|-------------|
| P1 | IR Team + CTO | CEO, Board |
| P2 | IR Team + IT Manager | CTO |
| P3 | IR Team | IT Manager |
| P4 | Security Analyst | Team Lead |

---

## Appendix A: Contact List

Update annually or upon personnel changes.

## Appendix B: Tool List

| Tool | Purpose |
|------|---------|
| SIEM | Log monitoring |
| EDR | Endpoint detection |
| Firewall | Network protection |
| Backup | Recovery |

---

*Template for {{COMPANY_NAME}} - Customize sections marked with {{}}*
