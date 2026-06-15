# SI – System and Information Integrity (CMMC Level 2)

**Domain:** System and Information Integrity (SI)  
**CMMC Level:** 2 (Advanced)  
**Number of Practices:** 7  
**Source Standard:** NIST SP 800-171

---

## Practice Summary Table

| Practice ID | Practice Name | AZ-104 Domain | Azure Service(s) |
|------------|---------------|---------------|-----------------|
| SI.L1-3.14.1 | Flaw Remediation | Monitor & Maintain | Defender for Cloud, Update Manager |
| SI.L1-3.14.2 | Malicious Code Protection | Monitor & Maintain | Defender for Servers, Antimalware |
| SI.L1-3.14.4 | Update Malicious Code Protection | Monitor & Maintain | Antimalware (auto-update), Azure Policy |
| SI.L1-3.14.5 | System and File Scanning | Monitor & Maintain | Antimalware, Defender for Storage |
| SI.L2-3.14.3 | Security Alerts | Monitor & Maintain | Defender for Cloud, Azure Monitor |
| SI.L2-3.14.6 | Monitor System Security | Monitor & Maintain | Microsoft Sentinel, Defender for Cloud |
| SI.L2-3.14.7 | Identify Unauthorized Use | Monitor & Maintain | Microsoft Sentinel, Defender for Cloud |

---

## Key Practice Details

### SI.L2-3.14.3 — Security Alerts

**Control Description:** Monitor system security alerts and advisories and take action in response.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Configure Azure Monitor alerts; Configure Defender for Cloud

**Azure Implementation:**

**Step 1 — Enable Defender for Cloud alerts:**
```bash
# Enable Defender for Cloud enhanced protections
az security pricing create --name VirtualMachines --tier Standard
az security pricing create --name SqlServers --tier Standard
az security pricing create --name AppServices --tier Standard
az security pricing create --name StorageAccounts --tier Standard
az security pricing create --name KeyVaults --tier Standard
```

**Step 2 — Configure email notifications for security alerts:**
```bash
az security contact create \
  --name "security-contact" \
  --email "security@yourdomain.com" \
  --alert-notifications On \
  --alerts-to-admins On
```

**Step 3 — Subscribe to Microsoft Security Advisories:**
- Enable **Azure Service Health** alerts for security advisories.
- Subscribe to Microsoft Security Response Center (MSRC) notifications.

```bash
# Create Service Health alert for security advisories
az monitor activity-log alert create \
  --name "SecurityAdvisory" \
  --resource-group <rg-name> \
  --condition category=Security \
  --action-group <action-group-id>
```

---

### SI.L2-3.14.6 — Monitor System Security

**Control Description:** Monitor the organizational system to detect attacks and indicators of potential attacks in accordance with organizational monitoring objectives.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Configure Microsoft Sentinel; Configure Defender for Cloud

**Azure Implementation:**

**Step 1 — Deploy Microsoft Sentinel:**
- Sentinel provides SIEM + SOAR capabilities for continuous monitoring.
- Connect all data sources: Azure Activity, Entra ID, Defender for Cloud, NSG flow logs.

**Step 2 — Enable NSG Flow Logs:**
```bash
# Enable NSG flow logs
az network watcher flow-log create \
  --location <region> \
  --name <flow-log-name> \
  --nsg <nsg-name> \
  --storage-account <storage-account-id> \
  --workspace <log-analytics-workspace-id> \
  --enabled true \
  --format JSON \
  --log-version 2
```

**Step 3 — Enable Microsoft Defender for Cloud continuous monitoring:**
- Enable "Continuous Export" to Log Analytics for all Defender alerts.
- Set up automated workflows in Defender for Cloud for response actions.

**Step 4 — Use Kusto queries for security monitoring:**
```kql
// Detect unusual number of resource deletions
AzureActivity
| where OperationNameValue endswith "/delete"
| where ActivityStatusValue == "Success"
| summarize DeleteCount = count() by Caller, bin(TimeGenerated, 1h)
| where DeleteCount > 10
| order by DeleteCount desc
```

---

### SI.L2-3.14.7 — Identify Unauthorized Use

**Control Description:** Identify unauthorized use of organizational systems.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Configure Microsoft Sentinel; Configure Defender for Cloud Identity Protection

**Azure Implementation:**

**Step 1 — Enable Microsoft Entra ID Protection:**
- Detects risky users and sign-ins using Microsoft's threat intelligence.
- Requires Entra ID P2.

**Step 2 — Enable Defender for Cloud user behavior analytics:**
- Detects anomalous behavior patterns (unusual data access, off-hours activity).

**Step 3 — Create Sentinel Analytic Rules for unauthorized access:**
```kql
// Detect access to storage from unexpected countries
StorageBlobLogs
| where StatusCode == 200
| where CallerIpAddress !startswith "10." and CallerIpAddress !startswith "192.168."
| summarize AccessCount = count() by CallerIpAddress, AccountName
| join kind=leftouter (
    _GetWatchlist('AuthorizedIPs')
) on $left.CallerIpAddress == $right.IPAddress
| where isempty(IPAddress)
```

**Step 4 — Review Access Reviews in Entra ID:**
- Periodically review who has access to what resources.
- Automated access reviews via Entra ID Identity Governance (P2).

---

*Back to [README](../../README.md) | See also: [Level 1 SI](../level1/SI-system-information-integrity.md)*
