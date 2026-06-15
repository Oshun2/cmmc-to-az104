# CMMC Controls to AZ-104 Mapping

This repository maps **Cybersecurity Maturity Model Certification (CMMC) 2.0** controls to **Microsoft AZ-104 (Azure Administrator)** exam skills and Azure services. It serves as a study guide, compliance reference, and bridge between DoD cybersecurity requirements and Azure implementation.

---

## Repository Structure

```
.
├── README.md                        # This file
├── docs/
│   ├── overview.md                  # CMMC & AZ-104 background
│   ├── how-to-use.md                # How to use this mapping
│   └── azure-services-reference.md  # Quick reference of relevant Azure services
├── mappings/
│   ├── level1/                      # CMMC Level 1 (17 practices)
│   │   ├── AC-access-control.md
│   │   ├── IA-identification-authentication.md
│   │   ├── MP-media-protection.md
│   │   ├── PE-physical-protection.md
│   │   ├── SC-system-communications-protection.md
│   │   └── SI-system-information-integrity.md
│   └── level2/                      # CMMC Level 2 (110 practices)
│       ├── AC-access-control.md
│       ├── AT-awareness-training.md
│       ├── AU-audit-accountability.md
│       ├── CA-assessment-authorization.md
│       ├── CM-configuration-management.md
│       ├── IA-identification-authentication.md
│       ├── IR-incident-response.md
│       ├── MA-maintenance.md
│       ├── MP-media-protection.md
│       ├── PE-physical-protection.md
│       ├── PS-personnel-security.md
│       ├── RA-risk-assessment.md
│       ├── CA-security-assessment.md
│       ├── SC-system-communications-protection.md
│       └── SI-system-information-integrity.md
├── csv/
│   ├── cmmc-level1-az104-mapping.csv
│   └── cmmc-level2-az104-mapping.csv
└── assets/
    └── cmmc-az104-overview-diagram.md
```

---

## Quick Reference: CMMC Levels

| Level | Name | Practices | Aligned Standard |
|-------|------|-----------|-----------------|
| Level 1 | Foundational | 17 | FAR 52.204-21 |
| Level 2 | Advanced | 110 | NIST SP 800-171 |

---

## Quick Reference: AZ-104 Exam Domains

| Domain | Weight | Key Topics |
|--------|--------|------------|
| Manage Azure Identities & Governance | 20–25% | Entra ID, RBAC, Subscriptions, Policy |
| Implement & Manage Storage | 15–20% | Storage Accounts, Blob, Files, Security |
| Deploy & Manage Azure Compute | 20–25% | VMs, Containers, App Service, ARM/Bicep |
| Implement & Manage Virtual Networking | 15–20% | VNet, NSG, VPN, Private Endpoints, DNS |
| Monitor & Maintain Azure Resources | 10–15% | Monitor, Alerts, Backup, Site Recovery |

---

## How to Navigate

- **Studying for AZ-104?** → Start with [docs/how-to-use.md](docs/how-to-use.md) and use the CSVs in `/csv/` to find which exam topics align with each CMMC control.
- **Implementing CMMC compliance in Azure?** → Browse `/mappings/` by the relevant CMMC domain and level.
- **Quick lookup?** → Use the CSV files — they are searchable and filterable.

---

## Disclaimer

This mapping is provided for educational and reference purposes. CMMC assessments must be conducted by a C3PAO (Certified Third-Party Assessment Organization). This guide does not constitute official compliance certification or legal advice.

---

## Contributing

Pull requests are welcome. Please open an issue first to discuss proposed changes.

---

## License

MIT License — see [LICENSE](LICENSE)
