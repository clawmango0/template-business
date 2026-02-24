# SOP: Physical Security & Asset Management

**Company:** {{COMPANY_NAME}}
**Department:** Operations / Facilities
**Document ID:** PHYS-001

---

## 1. Purpose

Establish procedures for protecting physical assets, controlling facility access, and managing equipment to prevent loss, theft, and unauthorized access.

## 2. Scope

Applies to:
- Company offices and facilities
- Physical equipment (laptops, monitors, servers)
- Mobile devices (phones, tablets)
- Physical access credentials (badges, keys)
- Visitor management

---

## 3. Facility Access Levels

| Level | Access Area | Authorization | Review |
|-------|-------------|---------------|--------|
| 1 | Building exterior/public areas | All employees | Annual |
| 2 | General office workspace | All employees | Annual |
| 3 | Server room/IT closet | IT only | Quarterly |
| 4 | Executive offices | Executives + assistants | Annual |
| 5 | Sensitive areas (vault, data center) | Specific roles | Monthly |

---

## 4. Access Credentials

### 4.1 Badge System

| Badge Type | Color | Access | Validity |
|------------|-------|--------|----------|
| Employee | Blue | Levels 1-2 | Employment |
| Contractor | Yellow | Level 1 | Contract period |
| Visitor | Red | Level 1 + escort | Day pass |
| IT Admin | Green | Levels 1-3 | Employment |
| Executive | Purple | Levels 1-4 | Employment |

### 4.2 Badge Distribution Log

| Date | Name | Badge # | Access Level | Issued By | Returned |
|------|------|---------|--------------|-----------|----------|
| | | | | | |

### 4.3 Lost Badge Procedure

```
1. IMMEDIATELY report to IT/Security
2. IT disables badge in system (within 15 min)
3. New badge issued
4. Incident logged
5. Review access logs for suspicious activity
```

---

## 5. Equipment Inventory

### 5.1 Asset Categories

| Category | Examples | Tracking |
|----------|----------|----------|
| Computing | Laptops, desktops, monitors | Serial number |
| Mobile | Phones, tablets | IMEI/Serial |
| Peripherals | Keyboards, mice, webcams | Asset tag |
| Furniture | Desks, chairs, cabinets | Location |
| Infrastructure | Servers, routers, switches | Serial + location |

### 5.2 Asset Tracking System

| Field | Value |
|-------|-------|
| Asset Tag | {{COMPANY}}-#### |
| Serial Number | |
| Make/Model | |
| Purchase Date | |
| Purchase Cost | |
| Assigned To | |
| Location | |
| Status | Active/Repair/Retired |

### 5.3 Inventory Schedule

| Frequency | Task | Owner |
|-----------|------|-------|
| Weekly | Check-out log review | IT |
| Monthly | Spot check 10% of assets | IT |
| Quarterly | Full inventory audit | Finance/IT |
| Annual | 100% physical audit | All depts |

---

## 6. Laptop & Device Management

### 6.1 Check-Out Procedure

```
1. Employee requests device
2. Manager approves
3. IT logs checkout with:
   - Employee name
   - Asset tag
   - Date/time
   - Expected return
4. Employee signs acknowledgment
5. Device configured and handed over
```

### 6.2 Device Return Procedure

```
1. Employee returns device to IT
2. IT inspects for damage
3. Wipe device (MDM)
4. Update inventory status
5. Return to inventory or recycle
6. Log return in tracker
```

### 6.3 Lost/Stolen Device Procedure

| Time | Action |
|------|--------|
| Immediate | Report to IT |
| 15 min | Remote wipe (if MDM) |
| 30 min | Disable account access |
| 1 hr | File police report |
| 24 hr | Insurance claim (if applicable) |

---

## 7. Visitor Management

### 7.1 Visitor Sign-In

| Step | Action |
|------|--------|
| 1 | Visitor arrives, shows ID |
| 2 | Staff logs in visitor book |
| 3 | Visitor badge issued (day pass) |
| 4 | Employee notified of arrival |
| 5 | Visitor escorted to meeting area |
| 6 | Visitor signs out and returns badge |

### 7.2 Visitor Log

| Date | Time In | Time Out | Name | Company | Host | Badge # | ID Verified |
|------|---------|----------|------|---------|------|---------|-------------|
| | | | | | | | ✓/✗ |

### 7.3 Visitor Restrictions

- Must be escorted in secure areas
- No access to employee systems
- No photos without approval
- Must return badge same day
- Mobile devices may be logged

---

## 8. Server Room / Data Center

### 8.1 Access Requirements

| Role | Access Level | Approval |
|------|--------------|----------|
| IT Admin | Full | IT Manager |
| DevOps | Server access | IT Manager |
| Managed SP | As needed | IT Manager + escort |
| Executive | Tour only | CEO + IT Manager |

### 8.2 Access Log

| Date | Time In | Time Out | Name | Purpose | Badged Out |
|------|---------|----------|------|---------|------------|
| | | | | | |

### 8.3 Security Requirements

- [ ] Access requires badge + PIN
- [ ] CCTV recording 24/7
- [ ] No food/drink allowed
- [ ] Emergency power cutoff documented
- [ ] Fire suppression inspected

---

## 9. Shipping & Receiving

### 9.1 Incoming Packages

```
1. Received by designated staff
2. Logged in package tracker
3. Notified recipient
4. Package held in secure area
5. Recipient signs upon pickup
```

### 9.2 Outgoing Shipments

```
1. Shipping request submitted
2. Manager approval
3. Items logged
4. Packed and labeled
5. Carrier tracking number recorded
6. Recipient confirms delivery
```

---

## 10. Annual Security Audit

| Area | Checklist Item | Frequency | Status |
|------|---------------|-----------|--------|
| Access | Badge audit | Quarterly | |
| Access | Key inventory | Quarterly | |
| Equipment | Physical inventory | Annual | |
| Equipment | Asset tag verification | Annual | |
| Policy | Policy review | Annual | |
| Training | Security training | Annual | |

---

## Appendix: Emergency Contacts

| Role | Name | Phone | Email |
|------|------|-------|-------|
| Security Lead | | | |
| IT Manager | | | |
| Facilities | | | |
| Local Police (non-emergency) | | | |

---

## Appendix: Equipment Request Form

| Field | Value |
|-------|-------|
| Requestor | |
| Department | |
| Equipment Type | |
| Justification | |
| Manager Approval | |
| IT Approval | |

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{DATE}} | {{AUTHOR}} | Initial release |

---

*Physical Security & Asset Management - {{COMPANY_NAME}}*
