# CMMC & AZ-104 Overview

## What is CMMC?

The **Cybersecurity Maturity Model Certification (CMMC) 2.0** is a framework developed by the U.S. Department of Defense (DoD) to verify that defense contractors and subcontractors adequately protect **Federal Contract Information (FCI)** and **Controlled Unclassified Information (CUI)**.

### CMMC 2.0 Levels

| Level | Name | Target | Practices | Assessment |
|-------|------|--------|-----------|------------|
| 1 | Foundational | All DoD contractors handling FCI | 15 | Annual self-assessment |
| 2 | Advanced | Contractors handling CUI | 110 (NIST SP 800-171) | Triennial third-party (C3PAO) or self-assessment |
| 3 | Expert | Critical programs / highest CUI | 110+ (NIST SP 800-172) | Triennial government-led |

### CMMC Domains

CMMC 2.0 organizes practices into **14 domains**:

| Abbreviation | Domain |
|-------------|--------|
| AC | Access Control |
| AT | Awareness and Training |
| AU | Audit and Accountability |
| CA | Security Assessment |
| CM | Configuration Management |
| IA | Identification and Authentication |
| IR | Incident Response |
| MA | Maintenance |
| MP | Media Protection |
| PE | Physical Protection |
| PS | Personnel Security |
| RA | Risk Assessment |
| SC | System and Communications Protection |
| SI | System and Information Integrity |

---

## What is AZ-104?

**AZ-104: Microsoft Azure Administrator** is a Microsoft certification exam that validates skills in implementing, managing, and monitoring Azure environments. It is commonly held by cloud administrators and engineers supporting Azure infrastructure.

### AZ-104 Exam Domains

| Domain | Approximate Weight |
|--------|--------------------|
| Manage Azure Identities and Governance | 20–25% |
| Implement and Manage Storage | 15–20% |
| Deploy and Manage Azure Compute Resources | 20–25% |
| Implement and Manage Virtual Networking | 15–20% |
| Monitor and Maintain Azure Resources | 10–15% |

---

## Why Map CMMC to AZ-104?

Azure is one of the leading cloud platforms used by DoD contractors. Microsoft Azure holds a **FedRAMP High** authorization and supports **IL2, IL4, IL5, and IL6** impact levels in Azure Government. Azure administrators who hold or are studying for AZ-104 are often responsible for implementing and managing the controls that fulfill CMMC requirements.

This mapping helps:
- **Administrators** understand which Azure features and configurations satisfy specific CMMC controls.
- **Compliance teams** identify which AZ-104 skills are relevant to their CMMC assessment scope.
- **Students** preparing for AZ-104 who also need to demonstrate CMMC knowledge.

---

## Key Azure Services for CMMC Compliance

| Azure Service | Relevant CMMC Domains |
|--------------|----------------------|
| Microsoft Entra ID (Azure AD) | AC, IA |
| Azure Role-Based Access Control (RBAC) | AC |
| Azure Policy | CM, CA |
| Microsoft Defender for Cloud | SI, CA, RA |
| Azure Monitor / Log Analytics | AU |
| Microsoft Sentinel | AU, IR |
| Azure Key Vault | SC, IA |
| Azure Virtual Network (VNet) / NSG | SC, AC |
| Azure Private Endpoints | SC |
| Azure Backup / Site Recovery | SI |
| Azure Disk Encryption | MP, SC |
| Azure Bastion | AC, PE |
| Azure Firewall / DDoS Protection | SC |
| Microsoft Purview | MP, AU |
