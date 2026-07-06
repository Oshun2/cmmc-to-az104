# CMMC Controls → Azure Implementation (with AZ-104 mapping)

This repository maps **Cybersecurity Maturity Model Certification (CMMC) 2.0** controls to the **Microsoft Azure resources** that implement them, the **evidence** that proves each control is met, and the **AZ-104 (Azure Administrator)** exam skills involved. It bridges DoD cybersecurity requirements and real Azure configuration.

## Who Is This For?

| Audience | Start here | What you get |
|----------|-----------|--------------|
| 🛡️ **Security auditors & assessors** | [docs/for-auditors.md](docs/for-auditors.md) + [`audit/assessment-tracker.csv`](audit/assessment-tracker.csv) | A complete assessment workflow, a fillable per-practice tracker, a POA&M template, and the evidence required for each control |
| 🏢 **Compliance / GRC teams** | [docs/demonstrating-compliance.md](docs/demonstrating-compliance.md) | How to implement each control in Azure and produce audit-ready evidence |
| 👩‍💻 **Azure administrators** | [mappings/](mappings/) | Step-by-step Azure CLI configuration for each control |
| 🎓 **AZ-104 students** | [csv/](csv/) | Each control tied to the AZ-104 exam domain and skill it reinforces |

> **Note:** The AZ-104 columns are one lens, not the point. Every mapping and CSV works as a standalone CMMC-to-Azure compliance reference — auditors can ignore the exam columns entirely.

---

## Repository Structure

```
.
├── README.md                        # This file
├── docs/
│   ├── overview.md                  # CMMC & AZ-104 background
│   ├── cmmc-program-summary.md      # Official CMMC program summary (levels, rules, dates)
│   ├── nist-800-171.md              # NIST SP 800-171 — the standard behind Level 2
│   ├── how-to-use.md                # How to use this mapping
│   ├── for-auditors.md              # Assessment workflow for auditors/assessors
│   ├── demonstrating-compliance.md  # Evidence & artifacts to prove each control
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
│       ├── CA-security-assessment.md
│       ├── CM-configuration-management.md
│       ├── IA-identification-authentication.md
│       ├── IR-incident-response.md
│       ├── MA-maintenance.md
│       ├── MP-media-protection.md
│       ├── PS-personnel-security.md
│       ├── RA-risk-assessment.md
│       ├── SC-system-communications-protection.md
│       └── SI-system-information-integrity.md
│       # (PE Physical Protection practices: see level1/PE + CSVs)
├── csv/
│   ├── cmmc-level1-az104-mapping.csv
│   └── cmmc-level2-az104-mapping.csv
├── audit/                           # Auditor working artifacts
│   ├── assessment-tracker.csv       # Fillable per-practice assessment worksheet
│   └── poam-template.csv            # Plan of Action & Milestones template
├── scripts/
│   └── build_assessment_tracker.py  # Regenerates the tracker from the mapping CSVs
└── assets/
    └── cmmc-az104-overview-diagram.md
```

---

## Quick Reference: CMMC Levels

| Level | Name | Practices | Aligned Standard | Assessment |
|-------|------|-----------|-----------------|------------|
| Level 1 | Foundational | 17 | FAR 52.204-21 | Annual self-assessment |
| Level 2 | Advanced | 110 | NIST SP 800-171 Rev 2 | Self-assessment or C3PAO (triennial) |
| Level 3 | Expert | 110 + NIST SP 800-172 subset | NIST SP 800-171 + 800-172 | DoD-led (DIBCAC) |

*CMMC Program rule (32 CFR Part 170) effective Dec 16, 2024; DFARS acquisition rule effective Nov 10, 2025. See [docs/cmmc-program-summary.md](docs/cmmc-program-summary.md) for details.*

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

- **New to CMMC?** → Read [docs/cmmc-program-summary.md](docs/cmmc-program-summary.md) (program, levels, rules, dates) and [docs/nist-800-171.md](docs/nist-800-171.md) (the standard behind Level 2).
- **Auditing or assessing an environment?** → Start with [docs/for-auditors.md](docs/for-auditors.md), then work from [`audit/assessment-tracker.csv`](audit/assessment-tracker.csv) and log gaps in [`audit/poam-template.csv`](audit/poam-template.csv).
- **Need to prove a control is met?** → See [docs/demonstrating-compliance.md](docs/demonstrating-compliance.md) for the exact evidence and artifacts per control.
- **Implementing CMMC compliance in Azure?** → Browse `/mappings/` by the relevant CMMC domain and level.
- **Studying for AZ-104?** → Start with [docs/how-to-use.md](docs/how-to-use.md) and use the CSVs in `/csv/` to find which exam topics align with each CMMC control.
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
