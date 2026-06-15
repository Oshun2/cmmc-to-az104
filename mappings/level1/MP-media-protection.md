# MP – Media Protection (CMMC Level 1)

**Domain:** Media Protection (MP)  
**CMMC Level:** 1 (Foundational)  
**Number of Practices:** 1  
**Source Standard:** FAR 52.204-21

---

## MP.L1-3.8.3 — Media Disposal

**Control Description:**  
Sanitize or destroy information system media containing Federal Contract Information (FCI) before disposal or reuse.

**NIST SP 800-171 Reference:** 3.8.3

### AZ-104 Mapping

| Field | Value |
|-------|-------|
| **AZ-104 Exam Domain** | Implement and Manage Storage |
| **AZ-104 Skill** | Configure Azure Storage security; Configure Azure Disk encryption |
| **Azure Service(s)** | Azure Disk Encryption, Azure Storage (Secure Transfer), Microsoft Purview, Azure Managed Disks |

### Azure Implementation

**Step 1 — Enable Azure Disk Encryption (ADE) on all VMs:**
- Encrypts OS and data disks using BitLocker (Windows) or DM-Crypt (Linux).
- Keys are stored in Azure Key Vault.
- When a disk is deleted, encrypted data cannot be recovered without the key.

```bash
# Enable disk encryption on a VM
az vm encryption enable \
  --resource-group <rg-name> \
  --name <vm-name> \
  --disk-encryption-keyvault <keyvault-name>
```

**Step 2 — Use Azure-managed encryption at rest:**
- Azure Storage automatically encrypts all data at rest using 256-bit AES (SSE).
- No additional configuration required — enabled by default.
- When storage is deleted, data is cryptographically erased.

**Step 3 — Use secure delete for Blob Storage:**
- Enable **Blob Soft Delete** with a retention period, then permanently delete after the retention window.
- Use **Blob versioning** and **immutability policies** where required.

```bash
# Enable soft delete for blob storage
az storage blob service-properties delete-policy update \
  --account-name <storage-account-name> \
  --enable true \
  --days-retained 7
```

**Step 4 — Physical media (Shared Responsibility):**
- Azure data centers handle physical media destruction per NIST 800-88 standards.
- This is covered under Microsoft's Shared Responsibility Model.
- Document this coverage in your System Security Plan (SSP).

### Important Notes

> **[Partial]** For on-premises or removable media (USB drives, external HDDs), organizations must implement their own sanitization procedures per NIST SP 800-88 (Guidelines for Media Sanitization). Azure does not manage physical media held by the customer.

### Assessment Objective

Determine if system media containing FCI is sanitized or destroyed before disposal or reuse.

---

*Back to [Level 1 Index](../../README.md) | Next: [PE – Physical Protection](PE-physical-protection.md)*
