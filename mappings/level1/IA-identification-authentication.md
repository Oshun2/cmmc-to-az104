# IA – Identification and Authentication (CMMC Level 1)

**Domain:** Identification and Authentication (IA)  
**CMMC Level:** 1 (Foundational)  
**Number of Practices:** 2  
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

## IA.L1-3.5.1 — Identification

**Control Description:**  
Identify information system users, processes acting on behalf of users, and devices.

**NIST SP 800-171 Reference:** 3.5.1

### AZ-104 Mapping

| Field | Value |
|-------|-------|
| **AZ-104 Exam Domain** | Manage Azure Identities and Governance |
| **AZ-104 Skill** | Manage Microsoft Entra users and groups; Manage service principals and managed identities |
| **Azure Service(s)** | Microsoft Entra ID, Managed Identities, Azure Active Directory B2B |

### Azure Implementation

**Step 1 — Ensure all users have unique identities:**
- Create individual Entra ID accounts; do not share credentials.
- Disable guest access that does not require identity verification.
- Enable Entra ID audit logs to track user identity events.

**Step 2 — Use Managed Identities for service-to-service:**
- Assign system-assigned or user-assigned managed identities to Azure resources (VMs, App Services, Functions).
- Avoid embedding service account credentials in code or config files.

**Step 3 — Identify devices:**
- Register or join devices to Entra ID (Entra ID Join or Hybrid Entra ID Join).
- Use Microsoft Intune for device inventory and compliance enforcement.

### Key Azure CLI Commands

```bash
# List all users in Entra ID
az ad user list --output table

# Create a managed identity
az identity create --name <identity-name> --resource-group <rg-name>

# Assign managed identity to a VM
az vm identity assign --name <vm-name> --resource-group <rg-name>
```

### Assessment Objective

Determine if system users, processes acting on behalf of users, and devices are identified.

---

## IA.L1-3.5.2 — Authentication

**Control Description:**  
Authenticate (or verify) the identities of those users, processes, or devices, as a prerequisite to allowing access to organizational information systems.

**NIST SP 800-171 Reference:** 3.5.2

### AZ-104 Mapping

| Field | Value |
|-------|-------|
| **AZ-104 Exam Domain** | Manage Azure Identities and Governance |
| **AZ-104 Skill** | Manage authentication and authorization; Configure multi-factor authentication (MFA) |
| **Azure Service(s)** | Microsoft Entra ID, Microsoft Entra MFA, Conditional Access, Azure Key Vault |

### Azure Implementation

**Step 1 — Require Multi-Factor Authentication (MFA):**
- Enable Microsoft Entra MFA for all users via Security Defaults or Conditional Access policies.
- Require MFA for all administrative roles at minimum.

**Step 2 — Set strong password policies:**
- Use Entra ID Password Protection to block weak/common passwords.
- Configure password expiration and complexity policies.

**Step 3 — Authenticate service accounts and devices:**
- Use managed identities (no passwords) for Azure resources.
- Use certificate-based authentication for devices where supported.
- Store secrets in Azure Key Vault, never hardcoded.

**Step 4 — Monitor authentication failures:**
- Enable Entra ID Sign-in logs.
- Create alerts in Microsoft Sentinel or Azure Monitor for repeated failed sign-ins.

### Key Azure CLI Commands

```bash
# Enable security defaults (includes MFA)
# Done via Azure Portal: Entra ID > Properties > Manage Security Defaults

# List sign-in logs (requires Log Analytics workspace)
az monitor activity-log list --resource-group <rg-name> --output table

# Create a Key Vault secret (instead of hardcoding credentials)
az keyvault secret set --vault-name <vault-name> --name "db-password" --value "MySecretValue"
```

### Assessment Objective

Determine if the identities of users, processes, or devices are authenticated before access to the system is granted.

---

*Back to [Level 1 Index](../../README.md) | Next: [MP – Media Protection](MP-media-protection.md)*
