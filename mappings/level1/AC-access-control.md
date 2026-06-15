# AC – Access Control (CMMC Level 1)

**Domain:** Access Control (AC)  
**CMMC Level:** 1 (Foundational)  
**Number of Practices:** 2  
**Source Standard:** FAR 52.204-21

---

## AC.L1-3.1.1 — Authorized Access Control

**Control Description:**  
Limit information system access to authorized users, processes acting on behalf of authorized users, and devices (including other information systems).

**NIST SP 800-171 Reference:** 3.1.1

### AZ-104 Mapping

| Field | Value |
|-------|-------|
| **AZ-104 Exam Domain** | Manage Azure Identities and Governance |
| **AZ-104 Skill** | Manage Microsoft Entra users and groups; Manage role-based access control (RBAC) |
| **Azure Service(s)** | Microsoft Entra ID, Azure RBAC, Conditional Access |

### Azure Implementation

**Step 1 — Manage user identities in Microsoft Entra ID:**
- Create user accounts only for authorized personnel.
- Disable or delete accounts when users leave the organization.
- Use groups to manage access at scale.

**Step 2 — Apply least-privilege RBAC:**
- Assign built-in Azure roles (e.g., Reader, Contributor) at the appropriate scope (subscription, resource group, or resource).
- Avoid assigning the Owner role broadly.
- Use `az role assignment create` or the Azure Portal > IAM blade.

**Step 3 — Restrict device access with Conditional Access:**
- Require compliant or Entra ID-joined devices.
- Block access from unknown or unmanaged devices.
- Requires Microsoft Entra ID P1 or P2.

### Key Azure CLI Commands

```bash
# List role assignments at a subscription
az role assignment list --scope /subscriptions/<subscription-id> --output table

# Assign a role to a user
az role assignment create \
  --assignee <user-principal-name> \
  --role "Reader" \
  --scope /subscriptions/<subscription-id>/resourceGroups/<rg-name>
```

### Assessment Objective

Determine if access to the system is limited to authorized users, processes acting on behalf of authorized users, and devices.

---

## AC.L1-3.1.2 — Transaction & Function Control

**Control Description:**  
Limit information system access to the types of transactions and functions that authorized users are permitted to execute.

**NIST SP 800-171 Reference:** 3.1.2

### AZ-104 Mapping

| Field | Value |
|-------|-------|
| **AZ-104 Exam Domain** | Manage Azure Identities and Governance |
| **AZ-104 Skill** | Manage role-based access control (RBAC); Manage Azure Policy |
| **Azure Service(s)** | Azure RBAC, Azure Policy, Microsoft Entra Privileged Identity Management (PIM) |

### Azure Implementation

**Step 1 — Scope RBAC roles to specific functions:**
- Use built-in roles scoped to what the user needs (e.g., `Storage Blob Data Reader` instead of `Contributor`).
- Use custom RBAC roles when built-in roles grant excessive permissions.

**Step 2 — Use Azure Policy to restrict transactions:**
- Apply `deny` policies to block non-compliant resource operations.
- Example: deny creation of public IP addresses, or restrict VM SKUs.

**Step 3 — Use PIM for privileged function access:**
- Require just-in-time (JIT) activation for high-privilege roles.
- Set time-bound access with approval workflows.
- Requires Microsoft Entra ID P2.

### Key Azure CLI Commands

```bash
# List all custom role definitions
az role definition list --custom-role-only true --output table

# Create a policy assignment to restrict a transaction type
az policy assignment create \
  --name "deny-public-ip" \
  --policy "NotAllowedResourceTypes" \
  --params '{"listOfResourceTypesNotAllowed": {"value": ["Microsoft.Network/publicIPAddresses"]}}' \
  --scope /subscriptions/<subscription-id>
```

### Assessment Objective

Determine if access to the system is limited to the types of transactions and functions that authorized users are permitted to execute.

---

*Back to [Level 1 Index](../../README.md) | Next: [IA – Identification and Authentication](IA-identification-authentication.md)*
