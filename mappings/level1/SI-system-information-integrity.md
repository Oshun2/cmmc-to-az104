# SI – System and Information Integrity (CMMC Level 1)

**Domain:** System and Information Integrity (SI)  
**CMMC Level:** 1 (Foundational)  
**Number of Practices:** 3  
**Source Standard:** FAR 52.204-21

---

> [!IMPORTANT]
> **Verify commands before use.** The Azure CLI and KQL examples below are
> illustrative references to show *how* a control is implemented — they are not
> tested deployment scripts. CLI syntax, policy definition IDs, and service
> capabilities change over time. Validate every command in a non-production
> subscription against current
> [Microsoft documentation](https://learn.microsoft.com/cli/azure/) before
> relying on it for compliance work.

## SI.L1-3.14.1 — Flaw Remediation

**Control Description:**  
Identify, report, and correct information and information system flaws in a timely manner.

**NIST SP 800-171 Reference:** 3.14.1

### AZ-104 Mapping

| Field | Value |
|-------|-------|
| **AZ-104 Exam Domain** | Monitor and Maintain Azure Resources |
| **AZ-104 Skill** | Monitor and manage Azure resources; Implement Azure Update Manager |
| **Azure Service(s)** | Microsoft Defender for Cloud, Azure Update Manager, Azure Monitor, Log Analytics |

### Azure Implementation

**Step 1 — Enable Microsoft Defender for Cloud:**
- Provides vulnerability assessments and security recommendations.
- Identifies missing patches, misconfigurations, and exposed ports.
- Free (Foundational CSPM) tier is available at no cost.

```bash
# Enable Defender for Cloud on a subscription
az security auto-provisioning-setting update \
  --name mma \
  --auto-provision On
```

**Step 2 — Use Azure Update Manager for patch management:**
- Assess patch compliance across Azure VMs and Azure Arc-enabled servers.
- Schedule automatic patching maintenance windows.

```bash
# Check update assessment status for a VM
az maintenance configuration create \
  --resource-group <rg-name> \
  --resource-name <vm-name> \
  --resource-type virtualMachines \
  --provider-name Microsoft.Compute \
  --configuration-assignment-name "PatchConfig"
```

**Step 3 — Track remediation with Defender for Cloud recommendations:**
- Review "Secure Score" and prioritize high-severity findings.
- Use the "Fix" button in Defender for Cloud for automated remediation where available.

### Assessment Objective

Determine if information system flaws are identified, reported, and corrected in a timely manner.

---

## SI.L1-3.14.2 — Malicious Code Protection

**Control Description:**  
Provide protection from malicious code at appropriate locations within organizational information systems.

**NIST SP 800-171 Reference:** 3.14.2

### AZ-104 Mapping

| Field | Value |
|-------|-------|
| **AZ-104 Exam Domain** | Monitor and Maintain Azure Resources |
| **AZ-104 Skill** | Configure Microsoft Defender for Cloud; Monitor security posture |
| **Azure Service(s)** | Microsoft Defender for Servers, Microsoft Defender for Storage, Microsoft Antimalware for Azure |

### Azure Implementation

**Step 1 — Enable Microsoft Antimalware on Azure VMs:**
- Deploy the Microsoft Antimalware extension to Windows VMs.
- Provides real-time protection, scheduled scanning, and signature updates.

```bash
# Add antimalware extension to a Windows VM
az vm extension set \
  --publisher Microsoft.Azure.Security \
  --name IaaSAntimalware \
  --resource-group <rg-name> \
  --vm-name <vm-name> \
  --settings '{
    "AntimalwareEnabled": true,
    "RealtimeProtectionEnabled": true,
    "ScheduledScanSettings": {
      "isEnabled": true,
      "scanType": "Quick",
      "day": "7",
      "time": "120"
    }
  }'
```

**Step 2 — Enable Microsoft Defender for Servers:**
- Integrates with Microsoft Defender for Endpoint for advanced threat protection.
- Provides EDR (Endpoint Detection and Response) capabilities.

**Step 3 — Enable Microsoft Defender for Storage:**
- Detects malicious file uploads, anomalous access patterns, and suspicious activity on storage accounts.

```bash
# Enable Defender for Storage
az security pricing create \
  --name StorageAccounts \
  --tier Standard
```

### Assessment Objective

Determine if protection from malicious code is provided at appropriate locations in the system.

---

## SI.L1-3.14.4 — Update Malicious Code Protection

**Control Description:**  
Update malicious code protection mechanisms when new releases are available.

**NIST SP 800-171 Reference:** 3.14.4

### AZ-104 Mapping

| Field | Value |
|-------|-------|
| **AZ-104 Exam Domain** | Monitor and Maintain Azure Resources |
| **AZ-104 Skill** | Implement Azure Update Manager; Monitor security configurations |
| **Azure Service(s)** | Microsoft Antimalware for Azure (auto-update), Microsoft Defender for Endpoint, Azure Update Manager |

### Azure Implementation

**Step 1 — Configure automatic signature updates:**
- Microsoft Antimalware for Azure automatically updates virus definitions without manual intervention.
- Verify the `AutomaticUpdate` setting is enabled in the extension configuration.

**Step 2 — Monitor update compliance in Defender for Cloud:**
- Defender for Cloud flags VMs with outdated antimalware signatures.
- Review "Endpoint protection health failures" recommendation.

**Step 3 — Use Azure Policy to enforce antimalware:**
- Apply the built-in policy **"Deploy default Microsoft IaaSAntimalware extension for Windows Server"** to ensure all VMs have protection deployed and updated.

```bash
# Apply built-in antimalware policy
az policy assignment create \
  --name "enforce-antimalware" \
  --policy "2835b622-407b-4114-9198-6f7064cbe0dc" \
  --scope /subscriptions/<subscription-id>
```

### Assessment Objective

Determine if malicious code protection mechanisms are updated when new releases are available.

---

## SI.L1-3.14.5 — System and File Scanning

**Control Description:**  
Perform periodic scans of the information system and real-time scans of files from external sources as files are downloaded, opened, or executed.

**NIST SP 800-171 Reference:** 3.14.5

### AZ-104 Mapping

| Field | Value |
|-------|-------|
| **AZ-104 Exam Domain** | Monitor and Maintain Azure Resources |
| **AZ-104 Skill** | Monitor security posture with Microsoft Defender for Cloud |
| **Azure Service(s)** | Microsoft Antimalware for Azure, Microsoft Defender for Endpoint, Microsoft Defender for Storage |

### Azure Implementation

**Step 1 — Configure scheduled scans on Azure VMs:**
- Set `ScheduledScanSettings.isEnabled` to `true` in the antimalware extension.
- Configure scan frequency (daily Quick scan or weekly Full scan recommended).

**Step 2 — Enable real-time protection:**
- Set `RealtimeProtectionEnabled` to `true` in the antimalware extension configuration.
- Real-time scans occur automatically as files are created, modified, or executed.

**Step 3 — Scan files uploaded to Azure Storage:**
- Enable **Microsoft Defender for Storage** with on-upload malware scanning.
- This scans blobs when uploaded using hash reputation analysis and deep content scanning.

```bash
# Enable malware scanning in Defender for Storage (per-storage account)
az security defender-for-storage setting update \
  --resource-group <rg-name> \
  --storage-account <storage-account-name> \
  --malware-scanning-enabled true
```

### Assessment Objective

Determine if periodic scans of the system and real-time scans of files from external sources are performed.

---

*Back to [Level 1 Index](../../README.md)*
