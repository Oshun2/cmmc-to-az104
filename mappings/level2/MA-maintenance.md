# MA – Maintenance (CMMC Level 2)

**Domain:** Maintenance (MA)  
**CMMC Level:** 2 (Advanced)  
**Number of Practices:** 6  
**Source Standard:** NIST SP 800-171

---

## Practice Summary Table

| Practice ID | Practice Name | AZ-104 Domain | Azure Service(s) |
|------------|---------------|---------------|-----------------|
| MA.L2-3.7.1 | Perform Maintenance | Compute | Azure Update Manager, Azure Automation |
| MA.L2-3.7.2 | Controlled Maintenance | Identities & Governance | RBAC, PIM, Azure Bastion |
| MA.L2-3.7.3 | Equipment Sanitization | Storage | Azure Disk Encryption, Key Vault |
| MA.L2-3.7.4 | Media Inspection | Monitor & Maintain | Defender for Storage, Antimalware |
| MA.L2-3.7.5 | Remote Maintenance | Identities & Governance | Conditional Access (MFA), Azure Bastion |
| MA.L2-3.7.6 | Maintenance Personnel | Identities & Governance | RBAC, PIM, Azure Monitor |

---

## Key Practice Details

### MA.L2-3.7.1 — Perform Maintenance

**Control Description:** Perform maintenance on organizational systems.

**AZ-104 Mapping:**
- **Domain:** Deploy and Manage Azure Compute Resources
- **Skill:** Implement Azure Update Manager

**Azure Implementation:**
- Schedule maintenance windows with **Azure Update Manager**.
- Automate routine maintenance with **Azure Automation runbooks**.

```bash
az maintenance configuration create \
  --resource-group <rg> --resource-name "MonthlyMaintenance" \
  --maintenance-scope InGuestPatch --location <region>
```

**Evidence:** Maintenance configuration export; patch/maintenance history records.

---

### MA.L2-3.7.2 — Controlled Maintenance

**Control Description:** Provide controls on the tools, techniques, mechanisms, and personnel used to conduct system maintenance.

**AZ-104 Mapping:**
- **Domain:** Manage Azure Identities and Governance
- **Skill:** Manage RBAC; Configure PIM

**Azure Implementation:**
- Restrict who can perform maintenance using **RBAC** scoped roles.
- Require **PIM** just-in-time activation for maintenance roles.
- Route maintenance access through **Azure Bastion** (no direct public access).

**Evidence:** RBAC assignment export for maintenance roles; PIM activation logs.

---

### MA.L2-3.7.3 — Equipment Sanitization

**Control Description:** Ensure equipment removed for off-site maintenance is sanitized of any CUI.

**AZ-104 Mapping:**
- **Domain:** Implement and Manage Storage
- **Skill:** Configure Azure Disk Encryption

**Azure Implementation:**
- Enable **Azure Disk Encryption** on all VMs so disks are cryptographically protected.
- On decommission, delete the encryption key from **Key Vault** — rendering data unrecoverable (cryptographic erase).

```bash
az vm encryption show --name <vm-name> --resource-group <rg> -o table
```

**Evidence:** Disk encryption status; key deletion records in Key Vault audit logs.

---

### MA.L2-3.7.4 — Media Inspection

**Control Description:** Check media containing diagnostic and test programs for malicious code before the media are used in organizational systems.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Configure Defender for Cloud; Configure Defender for Storage

**Azure Implementation:**
- Enable **Defender for Storage** malware scanning to inspect uploaded diagnostic tools.
- Require diagnostic/test programs to come only from approved internal repositories.

```bash
az security defender-for-storage setting update \
  --resource-group <rg> --storage-account <sa> --malware-scanning-enabled true
```

**Evidence:** Defender for Storage scan results; approved-tooling repository policy.

---

### MA.L2-3.7.5 — Remote Maintenance

**Control Description:** Require multifactor authentication to establish nonlocal maintenance sessions via external network connections and terminate such connections when nonlocal maintenance is complete.

**AZ-104 Mapping:**
- **Domain:** Manage Azure Identities and Governance
- **Skill:** Configure Conditional Access; Configure Azure Bastion

**Azure Implementation:**
- Require **MFA** via Conditional Access for all external maintenance access.
- Use **Azure Bastion** — sessions terminate automatically when the browser tab closes.
- Log all maintenance sessions to Azure Monitor.

**Evidence:** Conditional Access policy requiring MFA; Bastion session logs showing connect/disconnect.

---

### MA.L2-3.7.6 — Maintenance Personnel

**Control Description:** Supervise the maintenance activities of maintenance personnel without required access authorization.

**AZ-104 Mapping:**
- **Domain:** Manage Azure Identities and Governance
- **Skill:** Manage RBAC; Configure PIM

**Azure Implementation:**
- Grant time-limited maintenance access via **PIM** with approval workflow.
- Monitor activity in real time using **Azure Monitor** / Bastion session recording.
- Revoke access immediately after the maintenance window.

**Evidence:** PIM activation records with approvers and expiry; activity logs during the session.

---

*Back to [README](../../README.md)*
