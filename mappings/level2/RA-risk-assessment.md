# RA – Risk Assessment (CMMC Level 2)

**Domain:** Risk Assessment (RA)  
**CMMC Level:** 2 (Advanced)  
**Number of Practices:** 3  
**Source Standard:** NIST SP 800-171

---

> [!IMPORTANT]
> **Verify commands before use.** The Azure CLI and KQL examples below are
> illustrative references to show *how* a control is implemented — they are not
> tested deployment scripts. CLI syntax, policy definition IDs, and service
> capabilities change over time. Validate every command in a non-production
> subscription against current
> [Microsoft documentation](https://learn.microsoft.com/cli/azure/) before
> relying on it for compliance work.

## Practice Summary Table

| Practice ID | Practice Name | AZ-104 Domain | Azure Service(s) |
|------------|---------------|---------------|-----------------|
| RA.L2-3.11.1 | Risk Assessments | Monitor & Maintain | Defender for Cloud (Secure Score) |
| RA.L2-3.11.2 | Vulnerability Scan | Monitor & Maintain | Defender for Cloud, Defender for Servers |
| RA.L2-3.11.3 | Vulnerability Remediation | Monitor & Maintain | Defender for Cloud, Update Manager |

---

## Key Practice Details

### RA.L2-3.11.1 — Risk Assessments

**Control Description:** Periodically assess the risk to organizational operations, organizational assets, and individuals resulting from the operation of organizational systems and the associated processing, storage, or transmission of CUI.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Monitor security posture with Microsoft Defender for Cloud

**Azure Implementation:**
- Use **Defender for Cloud Secure Score** as a continuous, quantitative risk indicator.
- Export Secure Score trends over time to track risk posture improvement.
- Use **Microsoft Cloud Security Benchmark (MCSB)** as the risk assessment framework in Defender for Cloud.

```bash
# Get current Secure Score
az security secure-score list --output table
```

---

### RA.L2-3.11.2 — Vulnerability Scan

**Control Description:** Scan for vulnerabilities in organizational systems and applications periodically and when new vulnerabilities affecting those systems are identified.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Configure Defender for Cloud vulnerability assessments

**Azure Implementation:**

**Step 1 — Enable vulnerability assessment on VMs:**
- Defender for Servers includes integrated vulnerability scanning powered by Microsoft Defender Vulnerability Management (MDVM).

```bash
# Enable Defender for Servers (includes vulnerability scanning)
az security pricing create --name VirtualMachines --tier Standard
```

**Step 2 — Enable vulnerability assessment for Container images:**
```bash
az security pricing create --name ContainerRegistry --tier Standard
```

**Step 3 — Review vulnerability findings:**
- In Defender for Cloud > Recommendations > "Vulnerabilities in your virtual machines should be remediated."
- Export findings to CSV or to Log Analytics for tracking.

---

### RA.L2-3.11.3 — Vulnerability Remediation

**Control Description:** Remediate vulnerabilities in accordance with risk assessments.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Configure Azure Update Manager; Monitor and manage Defender for Cloud recommendations

**Azure Implementation:**
- Use **Azure Update Manager** to deploy patches prioritized by CVSS score from Defender vulnerability findings.
- Set up maintenance schedules with automatic patching for critical/important updates.

```bash
# Create a patch schedule (maintenance configuration)
az maintenance configuration create \
  --resource-group <rg-name> \
  --resource-name "CriticalPatchSchedule" \
  --maintenance-scope InGuestPatch \
  --location <region> \
  --install-patches-windows-parameters classifications="Critical,Security"
```

---

*Back to [README](../../README.md)*
