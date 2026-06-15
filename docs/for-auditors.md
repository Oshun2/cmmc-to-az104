# For Security Auditors & Assessors

This guide explains how to use this repository to **conduct or prepare for a CMMC assessment** of an Azure environment. It is written for C3PAO assessors, internal auditors, GRC analysts, and consultants — no AZ-104 background required.

> **AZ-104 is just one lens.** The exam-domain columns help administrators connect controls to skills they're learning, but every mapping, CSV, and evidence example works as a standalone CMMC-to-Azure compliance reference. Ignore the AZ-104 columns if they aren't useful to you.

---

## What This Repository Gives an Auditor

| Asset | Location | Auditor use |
|-------|----------|-------------|
| Control-to-Azure mappings | `mappings/level1/`, `mappings/level2/` | Understand *how* each control is implemented in Azure |
| Full practice catalog (CSV) | `csv/` | Filter/sort all 108+ practices by domain, level, or Azure service |
| Evidence guide | [demonstrating-compliance.md](demonstrating-compliance.md) | Know exactly what artifact proves each control |
| **Assessment tracker** | [`audit/assessment-tracker.csv`](../audit/assessment-tracker.csv) | **Working worksheet** — record status, evidence, and findings per practice |
| **POA&M template** | [`audit/poam-template.csv`](../audit/poam-template.csv) | Document deficiencies and remediation plans |

---

## The Assessment Workflow

### 1. Scope the environment
Identify which Azure subscriptions, resource groups, and resources store or process **CUI** (Level 2) or **FCI** (Level 1). Only in-scope assets are assessed.

```bash
# Inventory in-scope resources
az graph query -q "Resources | project name, type, resourceGroup, subscriptionId, location" -o table
```

### 2. Select the control set
- **Level 1** → 17 practices (FAR 52.204-21). Annual self-assessment.
- **Level 2** → 110 practices (NIST SP 800-171). Triennial C3PAO or self-assessment.

Open `audit/assessment-tracker.csv` and filter the **Level** column to your scope.

### 3. Assess each practice using NIST 800-171A methods
Every practice is evaluated by one or more methods. Record which you used in the tracker's **Assessment Method** column.

| Method | What the auditor does |
|--------|----------------------|
| **Examine** | Review configurations, policies, exported settings, screenshots, the SSP |
| **Interview** | Ask the responsible administrator to describe the process and ownership |
| **Test** | Observe the control operating — e.g., watch a non-compliant deployment get denied |

For the specific artifact to collect per control, use [demonstrating-compliance.md](demonstrating-compliance.md).

### 4. Score each assessment objective
CMMC practices break into lettered **assessment objectives** (e.g., `3.1.1[a]`, `[b]`, `[c]`). A practice is **MET only if every objective is satisfied**. Record per-practice results in the **Finding** column (`Met` / `Not Met` / `N/A`).

### 5. Document gaps in a POA&M
For any `Not Met` practice, create a row in `audit/poam-template.csv`, assign a `POA&M ID`, and link it back in the tracker's **POA&M ID** column.

### 6. Calculate the SPRS score (Level 2)
For Level 2 self-assessments, DoD requires a **Supplier Performance Risk System (SPRS)** score:
- Start at **110** (all practices met).
- Subtract **1, 3, or 5 points** per unmet practice based on its weighting in NIST SP 800-171 DoD Assessment Methodology.
- Range: **-203 to 110**.

> The point weighting per practice is defined in the *NIST SP 800-171 DoD Assessment Methodology*. This repo maps implementation; consult that document for exact point values.

---

## Using the Assessment Tracker

`audit/assessment-tracker.csv` has one row per practice, pre-filled with context columns and blank columns for you to complete:

| Column | Pre-filled? | What to enter |
|--------|:-----------:|---------------|
| Practice ID, Level, CMMC Domain, Practice Name, NIST Ref, Azure Service(s) | ✅ | (reference only) |
| Implementation Status | — | Implemented / Partially / Planned / Not Implemented |
| Assessment Method | — | Examine / Interview / Test |
| Evidence Artifact / Location | — | Path or system where the evidence lives |
| Assessor Notes | — | Observations, caveats, interview notes |
| Finding | — | Met / Not Met / N/A |
| POA&M ID | — | Link to a row in poam-template.csv if Not Met |

**Regenerate the tracker** any time the mappings change:
```bash
python3 scripts/build_assessment_tracker.py
```

Open the CSV in Excel or Google Sheets, freeze the header row, and add filters on **CMMC Domain**, **Level**, and **Finding** to drive the engagement.

---

## Automated, Continuous Auditing in Azure

Rather than collecting evidence manually, auditors can pull live compliance posture from Azure-native tooling:

| Tool | What it gives an auditor |
|------|--------------------------|
| **Microsoft Defender for Cloud — Regulatory Compliance** | Built-in **NIST SP 800-171 R2** standard; live pass/fail per control; exportable PDF/CSV reports |
| **Microsoft Purview Compliance Manager** | Pre-built **CMMC Level 2** assessment template with per-control evidence repository and improvement actions |
| **Azure Policy compliance state** | Continuous proof that configuration baselines remain enforced |
| **Azure Resource Graph** | On-demand inventory and configuration queries across all subscriptions |

```bash
# Pull current regulatory-compliance posture (after enabling the NIST 800-171 standard)
az security regulatory-compliance-standards list -o table
az security regulatory-compliance-controls list --standard-name "NIST-SP-800-171-R2" -o table
```

These produce **point-in-time, defensible evidence** with Microsoft as the attestation source — far stronger than ad-hoc screenshots.

---

## Independence & Limitations

- This repository is a **reference and working aid**, not an authorized assessment tool or a substitute for the official CMMC Assessment Process (CAP).
- A formal CMMC Level 2 certification must be performed by an **accredited C3PAO**.
- Mappings reflect common Azure implementation patterns; **validate against the customer's actual configuration** — never mark a control Met based on the mapping alone.
- Physical (PE) and infrastructure controls rely on Microsoft's responsibility under the Shared Responsibility Model — obtain Microsoft's attestation packages from the [Service Trust Portal](https://servicetrust.microsoft.com/).

---

*Back to [README](../README.md) | See also: [demonstrating-compliance.md](demonstrating-compliance.md) · [overview.md](overview.md)*
