# AU – Audit and Accountability (CMMC Level 2)

**Domain:** Audit and Accountability (AU)  
**CMMC Level:** 2 (Advanced)  
**Number of Practices:** 9  
**Source Standard:** NIST SP 800-171

---

## Practice Summary Table

| Practice ID | Practice Name | AZ-104 Domain | Azure Service(s) |
|------------|---------------|---------------|-----------------|
| AU.L2-3.3.1 | Create and Retain Audit Logs | Monitor & Maintain | Azure Monitor, Log Analytics |
| AU.L2-3.3.2 | User Accountability | Monitor & Maintain | Azure Monitor, Entra ID Audit Logs |
| AU.L2-3.3.3 | Event Review | Monitor & Maintain | Log Analytics, Microsoft Sentinel |
| AU.L2-3.3.4 | Alert on Audit Failures | Monitor & Maintain | Azure Monitor Alerts |
| AU.L2-3.3.5 | Audit Correlation | Monitor & Maintain | Microsoft Sentinel, Log Analytics |
| AU.L2-3.3.6 | Audit Reduction | Monitor & Maintain | Log Analytics (KQL queries) |
| AU.L2-3.3.7 | Authoritative Time Source | Monitor & Maintain | Azure NTP (automatic) |
| AU.L2-3.3.8 | Audit Protection | Monitor & Maintain | Log Analytics immutability, Azure Storage WORM |
| AU.L2-3.3.9 | Audit Management | Monitor & Maintain | Azure RBAC on Log Analytics |

---

## Key Practice Details

### AU.L2-3.3.1 — Create and Retain Audit Logs

**Control Description:** Create and retain system audit logs and records to the extent needed to enable the monitoring, analysis, investigation, and reporting of unlawful or unauthorized system activity.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Configure Log Analytics workspaces; Configure diagnostic settings

**Azure Implementation:**

**Step 1 — Create a Log Analytics Workspace:**
```bash
az monitor log-analytics workspace create \
  --resource-group <rg-name> \
  --workspace-name <workspace-name> \
  --retention-time 365
```

**Step 2 — Configure diagnostic settings for all resources:**
```bash
# Enable Activity Logs
az monitor diagnostic-settings create \
  --name "ActivityLogs" \
  --resource /subscriptions/<sub-id> \
  --logs '[
    {"category":"Administrative","enabled":true},
    {"category":"Security","enabled":true},
    {"category":"ServiceHealth","enabled":true},
    {"category":"Alert","enabled":true},
    {"category":"Recommendation","enabled":true},
    {"category":"Policy","enabled":true}
  ]' \
  --workspace <workspace-id>
```

**Step 3 — Enable Entra ID audit and sign-in logs:**
- Entra ID > Diagnostic Settings > Send to Log Analytics workspace.
- Retain for minimum 90 days (1 year recommended).

**Retention Requirements:**
- NIST 800-171 does not specify a minimum, but CMMC assessors expect at least 3 months online + 1 year archived.
- Set Log Analytics retention to 365 days; archive to Storage Account for longer retention.

---

### AU.L2-3.3.2 — User Accountability

**Control Description:** Ensure that the actions of individual system users can be traced to those users, so they can be held accountable for their actions.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Configure Azure Activity Logs; Configure Entra ID Sign-in Logs

**Azure Implementation:**
- Ensure every user has a unique identity (no shared accounts).
- Enable Azure Activity Logs (records WHO did WHAT and WHEN at the management plane).
- Enable Entra ID Sign-in Logs for authentication traceability.
- Enable resource-level diagnostics for data-plane operations (e.g., Storage, SQL).

---

### AU.L2-3.3.4 — Alert on Audit Failures

**Control Description:** Alert in the event of an audit logging process failure.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Configure Azure Monitor alerts; Configure action groups

**Azure Implementation:**
```bash
# Create an alert for Log Analytics workspace health
az monitor metrics alert create \
  --name "LogIngestionFailure" \
  --resource-group <rg-name> \
  --scopes <workspace-resource-id> \
  --condition "count LogManagement/TotalDataIngested < 1" \
  --window-size 1h \
  --evaluation-frequency 30m \
  --action <action-group-id>
```

---

### AU.L2-3.3.5 — Audit Correlation

**Control Description:** Correlate audit record review, analysis, and reporting processes for investigation and response to indications of unlawful, unauthorized, suspicious, or unusual activity.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Configure Microsoft Sentinel; Create KQL queries in Log Analytics

**Azure Implementation:**
- Deploy **Microsoft Sentinel** as a SIEM to correlate events across all Azure resources.
- Create Analytic Rules in Sentinel to detect patterns across multiple log sources.
- Use **KQL (Kusto Query Language)** to write custom correlation queries.

```kql
// Example: Correlate failed sign-ins with subsequent successful sign-in from different IP
SigninLogs
| where ResultType != "0"
| summarize FailCount = count(), LastFail = max(TimeGenerated) by UserPrincipalName, IPAddress
| join kind=inner (
    SigninLogs
    | where ResultType == "0"
    | project UserPrincipalName, SuccessIP = IPAddress, SuccessTime = TimeGenerated
) on UserPrincipalName
| where SuccessTime > LastFail and SuccessIP != IPAddress
```

---

### AU.L2-3.3.8 — Audit Protection

**Control Description:** Protect audit information and audit tools from unauthorized access, modification, and deletion.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Configure Azure Storage (immutability policies); Configure RBAC on Log Analytics

**Azure Implementation:**
- Restrict Log Analytics workspace access using Azure RBAC (read-only for most users).
- Archive logs to an Azure Storage Account with **immutable storage (WORM)** enabled.
- Enable **resource lock** on the Log Analytics workspace to prevent deletion.

```bash
# Enable immutable storage on archive container
az storage container immutability-policy create \
  --account-name <storage-account-name> \
  --container-name <container-name> \
  --period 365

# Apply a resource lock to Log Analytics workspace
az lock create \
  --name "PreventDelete" \
  --resource-group <rg-name> \
  --resource-name <workspace-name> \
  --resource-type Microsoft.OperationalInsights/workspaces \
  --lock-type CanNotDelete
```

---

*Back to [README](../../README.md)*
