# CMMC Program Summary

An authoritative overview of the **Cybersecurity Maturity Model Certification (CMMC)** program, summarized from the U.S. Department of Defense (DoD) CIO and the published federal rules. Use this as the top-level orientation for the mappings in this repository.

> **Sources:** [About CMMC — DoD CIO](https://dodcio.defense.gov/CMMC/About/), [32 CFR Part 170 Final Rule (Federal Register, Oct 15 2024)](https://www.federalregister.gov/documents/2024/10/15/2024-22905/cybersecurity-maturity-model-certification-cmmc-program), [DFARS Final Rule 2019-D041 (Federal Register, Sep 10 2025)](https://www.federalregister.gov/documents/2025/09/10/defense-federal-acquisition-regulation-supplement-assessing-contractor-implementation-of). Always confirm current requirements against the official rule text before relying on them for a contract.

---

## Purpose

The DoD established the CMMC Program to **verify that defense contractors and subcontractors have implemented the security measures required to protect sensitive unclassified information** — specifically **Federal Contract Information (FCI)** and **Controlled Unclassified Information (CUI)** — across the Defense Industrial Base (DIB).

CMMC moves the DIB from **self-attestation** toward **verified compliance**, adding third-party and government assessments for higher-risk information.

---

## The Two Information Types CMMC Protects

| Type | Definition | Governing reference |
|------|------------|---------------------|
| **FCI** — Federal Contract Information | Information provided by or generated for the Government under a contract to develop or deliver a product/service, not intended for public release. | FAR 52.204-21 |
| **CUI** — Controlled Unclassified Information | Information the Government creates or possesses (or an entity creates/possesses for the Government) that requires safeguarding or dissemination controls under law, regulation, or government-wide policy. | 32 CFR Part 2002 (NARA CUI Program); NIST SP 800-171 |

---

## The Three CMMC Levels

| Level | Name | Requirements | Based On | Assessment |
|-------|------|-------------|----------|------------|
| **Level 1** | Foundational | **15** basic safeguarding requirements | FAR 52.204-21, items (i)–(xv) | **Annual self-assessment** + annual affirmation |
| **Level 2** | Advanced | **110 security requirements** | **NIST SP 800-171 Revision 2** | **Self-assessment** *or* **C3PAO** certification (triennial), depending on the information — plus annual affirmation |
| **Level 3** | Expert | 110 (Level 2) **+ a subset of NIST SP 800-172** | NIST SP 800-171 R2 + NIST SP 800-172 | **DoD-led** (DIBCAC); requires a Level 2 **Final** certification first |

> **Note on "15 vs 17" for Level 1:** Under **CMMC 2.0**, Level 1 is the **15** basic safeguarding requirements of FAR 52.204-21, items (i)–(xv). Older material citing **17 practices** refers to the retired **CMMC 1.0** model, which enumerated the same FAR requirements differently. This repository uses **15**.

### Assessment authorities
- **Level 1 → Self.** The contractor performs an annual self-assessment and affirms compliance in SPRS.
- **Level 2 → Self *or* C3PAO.** Lower-risk CUI may allow self-assessment; most CUI requires an assessment by an accredited **Certified Third-Party Assessment Organization (C3PAO)**. Valid for **3 years** with annual affirmations.
- **Level 3 → Government.** Assessed exclusively by the DoD's **Defense Industrial Base Cybersecurity Assessment Center (DIBCAC)**. Must already hold a Level 2 Final certification.

> **Scale:** DoD estimates roughly **8,350 medium and large entities** will need a Level 2 C3PAO assessment as a condition of award. Level 2 applies to **all contractors that process, store, or transmit CUI**.

---

## Scoring (Level 2 — SPRS)

Level 2 uses the **NIST SP 800-171 DoD Assessment Methodology** to produce a **Supplier Performance Risk System (SPRS)** score:
- Start at **110** (all requirements met).
- Deduct **1, 3, or 5 points** per unmet requirement based on its weight.
- Range: **-203 to 110**.
- Unmet requirements may be tracked on a **Plan of Action & Milestones (POA&M)** where permitted, with a closeout deadline (generally **180 days**). Certain high-value requirements are **not** POA&M-eligible.

See [`audit/poam-template.csv`](../audit/poam-template.csv) and [for-auditors.md](for-auditors.md) for how this repo supports scoring and POA&Ms.

---

## Rulemaking & Effective Dates

CMMC is codified through two rules:

| Rule | What it does | Key dates |
|------|--------------|-----------|
| **32 CFR Part 170** — CMMC Program rule | Establishes the CMMC program, levels, and assessment ecosystem | Proposed **Dec 26, 2023**; Final rule published **Oct 15, 2024**; **effective Dec 16, 2024** |
| **48 CFR / DFARS** (Case 2019-D041) — acquisition rule | Puts CMMC requirements into DoD contracts (clauses 252.204-7021 / -7025) | **Effective Nov 10, 2025** |

---

## Phased Rollout

Per **32 CFR 170.3(e)**, DoD phases CMMC into contracts over a **three-year period in four phases**, beginning **November 10, 2025**. The ramp-up gives industry time to implement controls and lets the assessor ecosystem scale.

| Milestone | What applies |
|-----------|--------------|
| **Nov 10, 2025** (Phase 1 start) | CMMC Level 1 and Level 2 **self-assessment** requirements begin appearing in solicitations/contracts |
| **Nov 10, 2026** (Phase 2 start) | CMMC Level 2 **C3PAO third-party assessments** begin being required for applicable contractors |
| **Phases 3–4** (subsequent years) | Broader application, including Level 3 requirements, per the schedule in 32 CFR 170.3(e) |

> Exact phase content and triggers are set by the contracting activity under 32 CFR 170.3(e); confirm what applies to a specific solicitation.

---

## Why This Matters for Azure Administrators

Because **CMMC Level 2 = the 110 requirements of NIST SP 800-171 Revision 2**, and Azure is a primary platform for DIB workloads (Azure holds **FedRAMP High**; Azure Government supports **IL2/IL4/IL5**), the day-to-day work of meeting CMMC in Azure maps directly to AZ-104-level administration: identity, storage, compute, networking, and monitoring.

This repository turns each CMMC requirement into concrete Azure configuration and evidence. For the underlying standard, see **[nist-800-171.md](nist-800-171.md)**.

---

*Back to [README](../README.md) | See also: [nist-800-171.md](nist-800-171.md) · [overview.md](overview.md) · [for-auditors.md](for-auditors.md)*
