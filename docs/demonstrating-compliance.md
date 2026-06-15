# Demonstrating Compliance — Evidence & Artifacts

Mapping a control to an Azure service is only half the job. To **pass a CMMC assessment**, you must produce **objective evidence** that the control is implemented and operating. This guide shows, for representative controls, exactly what evidence to collect and how to generate it from Azure.

---

## How CMMC Assessors Evaluate Controls

A C3PAO (Certified Third-Party Assessment Organization) assesses each practice using **three methods** (from NIST SP 800-171A):

| Method | What it means | Typical Azure evidence |
|--------|---------------|------------------------|
| **Examine** | Review documents, configurations, records | Policy assignments, exported configs, screenshots, SSP sections |
| **Interview** | Talk to the people who operate the control | Admin explains process; named role owners |
| **Test** | Observe the control working in real time | Live demo: blocked sign-in, denied deployment, alert firing |

Each practice in CMMC also has **assessment objectives** (the lettered sub-items, e.g., `3.1.1[a]`, `3.1.1[b]`). You must show evidence for **every** objective, not just the practice as a whole.

> **Rule of thumb:** For each control, collect (1) a **configuration artifact** proving it's set up, (2) a **log/record** proving it operates over time, and (3) a **documented procedure** in your System Security Plan (SSP).

---

## Evidence Examples by Control

### AC.L1-3.1.1 — Authorized Access Control

**What you must demonstrate:** Only authorized users, processes, and devices can access the system.

| Method | Evidence to produce | How to generate |
|--------|--------------------|-----------------|
| Examine | List of all users with access + their role assignments | CLI export below |
| Examine | Approved-user roster (from your SSP/onboarding records) | Organizational document |
| Test | Show an unauthorized account is denied / does not exist | Live attempt during assessment |

```bash
# Evidence 1: Export all role assignments (who has access to what)
az role assignment list --all --output table > evidence_AC-3.1.1_role-assignments.txt

# Evidence 2: Export all users in the directory
az ad user list --query "[].{Name:displayName, UPN:userPrincipalName, Enabled:accountEnabled}" \
  --output table > evidence_AC-3.1.1_user-list.txt
```

**Assessor verification:** Cross-references your role-assignment export against your approved-user roster. Every account with access must trace to an authorized individual. Disabled/orphaned accounts are findings.

---

### AC.L2-3.1.5 — Least Privilege

**What you must demonstrate:** Users have only the minimum privileges needed; privileged access is restricted and time-bound.

| Method | Evidence to produce | How to generate |
|--------|--------------------|-----------------|
| Examine | Custom roles scoped to minimum permissions | `az role definition list` export |
| Examine | PIM configuration showing JIT activation for admin roles | PIM screenshot / Graph export |
| Examine | Most recent Access Review results | Entra ID Access Reviews report |
| Test | Activate a privileged role via PIM and show it expires | Live PIM activation demo |

```bash
# Evidence: List custom roles and their exact permissions
az role definition list --custom-role-only true \
  --query "[].{Role:roleName, Actions:permissions[0].actions}" -o json \
  > evidence_AC-3.1.5_custom-roles.json

# Evidence: Identify over-privileged Owner/Contributor assignments to review
az role assignment list --all \
  --query "[?roleDefinitionName=='Owner' || roleDefinitionName=='Contributor'].{User:principalName, Role:roleDefinitionName, Scope:scope}" \
  -o table > evidence_AC-3.1.5_privileged-assignments.txt
```

**Assessor verification:** Confirms privileged roles are not broadly assigned, that PIM enforces just-in-time activation with approval/expiry, and that periodic Access Reviews are documented and acted on.

---

### IA.L2-3.5.3 — Multifactor Authentication

**What you must demonstrate:** MFA is enforced for privileged accounts (local + network) and for network access to non-privileged accounts.

| Method | Evidence to produce | How to generate |
|--------|--------------------|-----------------|
| Examine | Conditional Access policy requiring MFA (enabled state) | CA policy export / screenshot |
| Examine | MFA registration report (% of users registered) | Entra ID Authentication Methods report |
| Test | Sign in and show the MFA prompt enforced | Live sign-in demo |
| Test | Show a sign-in **blocked** for failing MFA | Sign-in logs filtered to failure |

```bash
# Evidence: Export sign-in logs showing MFA was applied
az monitor activity-log list --query "[?contains(operationName.value, 'SignIn')]" -o table

# In Entra ID portal, export:
#  - Conditional Access > Policies > [MFA policy] > showing State = "On"
#  - Reports > Authentication methods > Registration (CSV export)
#  - Sign-in logs > filter "Authentication requirement = Multifactor authentication"
```

**KQL evidence query (run in Log Analytics, export results):**
```kql
SigninLogs
| where TimeGenerated > ago(30d)
| summarize SignIns = count() by AuthenticationRequirement, ResultType
| order by SignIns desc
```

**Assessor verification:** Confirms the CA policy is enabled (not report-only), covers all required users, and that sign-in logs show MFA actually being satisfied. SMS-only MFA for privileged accounts may be flagged.

---

### AC.L2-3.1.8 — Unsuccessful Logon Attempts

**What you must demonstrate:** The system limits repeated failed logon attempts.

| Method | Evidence to produce | How to generate |
|--------|--------------------|-----------------|
| Examine | Smart Lockout threshold setting | Entra ID > Password protection screenshot |
| Test | Trigger lockout with repeated bad passwords | Live demo (test account) |
| Examine | Sign-in logs showing lockout events (error 50053) | KQL export |

```kql
// Evidence: Account lockout / repeated failure events
SigninLogs
| where ResultType in ("50053", "50126")   // 50053 = locked, 50126 = invalid credential
| project TimeGenerated, UserPrincipalName, IPAddress, ResultType, ResultDescription
| order by TimeGenerated desc
```

**Assessor verification:** Confirms a lockout threshold is configured (not unlimited attempts) and that logs evidence the mechanism triggering.

---

### SC.L2-3.13.16 — Protect CUI at Rest

**What you must demonstrate:** CUI is encrypted at rest.

| Method | Evidence to produce | How to generate |
|--------|--------------------|-----------------|
| Examine | Disk encryption status = Enabled on all VMs | CLI export below |
| Examine | Storage account encryption settings (SSE / CMK) | CLI export below |
| Examine | SQL TDE status = Enabled | CLI export below |

```bash
# Evidence 1: VM disk encryption status
az vm encryption show --name <vm-name> --resource-group <rg> \
  --query "{OS:disks[0].statuses[0].displayStatus}" -o table

# Evidence 2: Storage account encryption (key source + services)
az storage account show --name <sa-name> --resource-group <rg> \
  --query "{KeySource:encryption.keySource, Blob:encryption.services.blob.enabled, RequireTLS:minimumTlsVersion}" -o table

# Evidence 3: Azure SQL Transparent Data Encryption
az sql db tde show --resource-group <rg> --server <sql-server> --database <db> -o table
```

**Assessor verification:** Confirms encryption is enabled on every resource that stores CUI. A single unencrypted disk/storage account in scope is a finding.

---

### AU.L2-3.3.1 — Create and Retain Audit Logs

**What you must demonstrate:** Audit logs are created, centralized, and retained.

| Method | Evidence to produce | How to generate |
|--------|--------------------|-----------------|
| Examine | Log Analytics workspace with defined retention | CLI export below |
| Examine | Diagnostic settings routing logs to the workspace | CLI export below |
| Examine | Sample log records covering the audit window | KQL export |

```bash
# Evidence 1: Workspace retention setting (must meet your documented period)
az monitor log-analytics workspace show --resource-group <rg> --workspace-name <ws> \
  --query "{Workspace:name, RetentionDays:retentionInDays}" -o table

# Evidence 2: Confirm diagnostic settings are sending logs
az monitor diagnostic-settings list --resource <resource-id> -o table
```

```kql
// Evidence 3: Prove logs exist and are queryable for the period
AzureActivity
| where TimeGenerated > ago(90d)
| summarize Events = count() by bin(TimeGenerated, 1d)
| order by TimeGenerated asc
```

**Assessor verification:** Confirms retention meets your stated policy (commonly ≥1 year), that critical resources route logs centrally, and that records actually exist for the assessment window.

---

### CM.L2-3.4.2 — Enforce Security Configuration Settings

**What you must demonstrate:** Baseline security settings are enforced across the environment.

| Method | Evidence to produce | How to generate |
|--------|--------------------|-----------------|
| Examine | Azure Policy assignment(s) for the security baseline | CLI export below |
| Examine | Compliance state showing % compliant resources | Policy compliance export |
| Test | Attempt a non-compliant deployment and show it denied | Live demo |

```bash
# Evidence 1: Show the baseline policy/initiative is assigned
az policy assignment list --query "[].{Name:displayName, Policy:policyDefinitionId, Scope:scope}" -o table

# Evidence 2: Show compliance state
az policy state summarize --query "value[0].results" -o json \
  > evidence_CM-3.4.2_compliance-summary.json
```

**Assessor verification:** Confirms the baseline is assigned at the correct scope, reviews the compliance percentage, and may ask you to attempt a violating action to see the `deny` effect fire live.

---

### SI.L2-3.14.6 — Monitor for Attacks

**What you must demonstrate:** The system is continuously monitored to detect attacks and indicators of compromise.

| Method | Evidence to produce | How to generate |
|--------|--------------------|-----------------|
| Examine | Microsoft Sentinel deployed with connected data sources | Portal screenshot / CLI |
| Examine | Active analytic (detection) rules | Sentinel rules export |
| Examine | Sample incidents created by detections | Sentinel Incidents export |
| Examine | NSG flow logs enabled | CLI export below |

```bash
# Evidence: NSG flow logs are enabled
az network watcher flow-log list --location <region> \
  --query "[].{Name:name, Enabled:enabled, TargetNSG:targetResourceId}" -o table

# Evidence: Defender for Cloud plans enabled (continuous monitoring)
az security pricing list --query "value[].{Plan:name, Tier:pricingTier}" -o table
```

**Assessor verification:** Confirms monitoring is active (not just deployed), that detection rules exist, and that real incidents/alerts have been generated and triaged.

---

## Building Your Evidence Package

For an assessment, organize evidence per practice. A common structure:

```
evidence/
├── AC/
│   ├── AC-3.1.1_role-assignments.txt
│   ├── AC-3.1.1_user-roster.xlsx        (approved users)
│   └── AC-3.1.1_screenshot-iam.png
├── IA/
│   ├── IA-3.5.3_conditional-access-policy.png
│   └── IA-3.5.3_mfa-registration-report.csv
├── AU/
│   └── ...
└── SSP.docx                              (System Security Plan)
```

### Tips for Strong Evidence
- **Timestamp and label** every artifact (control ID + date generated).
- **Show the setting AND the result** — a policy *plus* a log proving it works.
- **Cover every assessment objective**, not just the headline practice.
- **Keep evidence current** — assessors expect artifacts from within the assessment window (typically last 30–90 days for operational logs).
- **Reference Microsoft's Shared Responsibility** docs for physical/infrastructure controls (PE domain) from the [Microsoft Service Trust Portal](https://servicetrust.microsoft.com/).
- **Use Microsoft Purview Compliance Manager** — it has a built-in **NIST SP 800-171 / CMMC** assessment template that tracks evidence and improvement actions per control.

---

## Continuous Compliance (Beyond the Assessment)

| Tool | Use for ongoing evidence |
|------|--------------------------|
| **Defender for Cloud — Regulatory Compliance dashboard** | Live compliance posture against NIST 800-171; exportable reports |
| **Microsoft Purview Compliance Manager** | Per-control evidence repository + improvement actions |
| **Azure Policy compliance** | Continuous proof that baselines stay enforced |
| **Azure Workbooks** | Scheduled compliance dashboards for auditors |

```bash
# Enable the NIST SP 800-171 compliance standard in Defender for Cloud
# Portal: Defender for Cloud > Regulatory compliance > Manage compliance policies
#         > select subscription > add "NIST SP 800-171 R2"
# Then export the compliance report (PDF/CSV) as point-in-time evidence.
```

---

*Back to [README](../README.md) | See also: [how-to-use.md](how-to-use.md) · [azure-services-reference.md](azure-services-reference.md)*
