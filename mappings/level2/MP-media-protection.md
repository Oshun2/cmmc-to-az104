# MP – Media Protection (CMMC Level 2)

**Domain:** Media Protection (MP)  
**CMMC Level:** 2 (Advanced)  
**Number of Practices:** 9  
**Source Standard:** NIST SP 800-171

> Level 1 practice MP.L1-3.8.3 (Media Disposal) is detailed in [Level 1 MP](../level1/MP-media-protection.md) and also applies at Level 2.

---

## Practice Summary Table

| Practice ID | Practice Name | AZ-104 Domain | Azure Service(s) |
|------------|---------------|---------------|-----------------|
| MP.L1-3.8.3 | Media Disposal | Storage | Azure Disk Encryption, SSE |
| MP.L2-3.8.1 | Media Protection | Storage | ADE, SSE, Azure Backup |
| MP.L2-3.8.2 | Media Access | Storage | RBAC (Storage roles), SAS, Entra ID |
| MP.L2-3.8.4 | Media Marking | Storage | Microsoft Purview (sensitivity labels) |
| MP.L2-3.8.5 | Media Accountability | Storage | Azure Monitor, Storage activity logs |
| MP.L2-3.8.6 | Portable Storage Encryption | Storage | Azure Information Protection, Intune (BitLocker) |
| MP.L2-3.8.7 | Removable Media Restrictions | Identities & Governance | Intune (USB restrictions) |
| MP.L2-3.8.8 | Shared Media Use | Identities & Governance | Intune, Azure Policy |
| MP.L2-3.8.9 | Backup CUI Protection | Monitor & Maintain | Azure Backup, Backup Vault (CMK), Immutable Vault |

---

## Key Practice Details

### MP.L2-3.8.1 — Media Protection

**Control Description:** Protect (i.e., physically control and securely store) system media containing CUI, both paper and digital.

**AZ-104 Mapping:**
- **Domain:** Implement and Manage Storage
- **Skill:** Configure Azure Storage security; Configure Azure Disk Encryption

**Azure Implementation:**
- Enable **Azure Disk Encryption** on all VMs and **SSE with CMK** on Storage Accounts.
- Restrict storage account network access; protect backups with **Azure Backup**.

```bash
az storage account update --name <sa> --resource-group <rg> \
  --encryption-key-source Microsoft.Keyvault --min-tls-version TLS1_2
```

**Evidence:** Encryption settings export; storage firewall configuration.

---

### MP.L2-3.8.2 — Media Access

**Control Description:** Limit access to CUI on system media to authorized users.

**AZ-104 Mapping:**
- **Domain:** Implement and Manage Storage
- **Skill:** Configure Azure Storage access controls; Manage RBAC

**Azure Implementation:**
- Assign **Storage Blob Data Reader/Writer** roles via Entra ID (avoid account keys).
- Use **SAS tokens** with least privilege and short expiry where delegated access is needed.
- Disable anonymous/public blob access.

```bash
az storage account update --name <sa> --resource-group <rg> \
  --allow-blob-public-access false
```

**Evidence:** Storage RBAC assignments; public-access-disabled setting.

---

### MP.L2-3.8.4 — Media Marking

**Control Description:** Mark media with necessary CUI markings and distribution limitations.

**AZ-104 Mapping:**
- **Domain:** Implement and Manage Storage
- **Skill:** Configure Microsoft Purview

**Azure Implementation:**
- Apply **Microsoft Purview sensitivity labels** to classify and visibly mark CUI documents.
- Labels propagate to SharePoint, OneDrive, and Office files.

**Evidence:** Purview label policy; sample labeled documents.

---

### MP.L2-3.8.5 — Media Accountability

**Control Description:** Control access to media containing CUI and maintain accountability for media during transport outside of controlled areas.

**AZ-104 Mapping:**
- **Domain:** Implement and Manage Storage
- **Skill:** Configure diagnostic settings

**Azure Implementation:**
- Enable **storage account logging** to track every access to media.
- Restrict network access via storage firewall and Private Endpoints.

**Evidence:** Storage access logs in Log Analytics; network restriction config.

---

### MP.L2-3.8.6 — Portable Storage Encryption

**Control Description:** Implement cryptographic mechanisms to protect the confidentiality of CUI stored on digital media during transport unless otherwise protected by alternative physical safeguards.

**AZ-104 Mapping:**
- **Domain:** Implement and Manage Storage
- **Skill:** Configure Azure Disk Encryption; Configure Intune

**Azure Implementation:**
- Enforce **BitLocker** on portable drives via **Intune** compliance policy.
- Use **Azure Information Protection** to encrypt CUI files before transfer to portable media.

**Evidence:** Intune BitLocker policy; AIP encryption configuration.

---

### MP.L2-3.8.7 — Removable Media Restrictions

**Control Description:** Control the use of removable media on system components.

**AZ-104 Mapping:**
- **Domain:** Manage Azure Identities and Governance
- **Skill:** Configure Intune device restrictions

**Azure Implementation:**
- Use **Intune device configuration profiles** to block or restrict USB/removable storage.
- Allow only approved, encrypted removable media.

**Evidence:** Intune device restriction policy export.

---

### MP.L2-3.8.8 — Shared Media Use

**Control Description:** Prohibit the use of portable storage devices when such devices have no identifiable owner.

**Azure Implementation:**
- Require device enrollment before USB access; block unrecognized/unregistered devices via **Intune**.

**Evidence:** Intune policy blocking unmanaged removable devices.

---

### MP.L2-3.8.9 — Backup CUI Protection

**Control Description:** Protect the confidentiality of backup CUI at storage locations.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Configure Azure Backup; Configure Storage encryption

**Azure Implementation:**
- Encrypt backups with **customer-managed keys (CMK)**.
- Enable **immutable vault** and **soft delete** on the Recovery Services / Backup Vault.
- Restrict vault access via **RBAC**.

```bash
# Enable soft delete on a Recovery Services vault
az backup vault backup-properties set \
  --name <vault-name> --resource-group <rg> --soft-delete-feature-state Enable
```

**Evidence:** Vault encryption (CMK) settings; immutability and soft-delete configuration.

---

*Back to [README](../../README.md) | See also: [Level 1 MP](../level1/MP-media-protection.md)*
