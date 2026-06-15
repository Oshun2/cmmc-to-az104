# PS – Personnel Security (CMMC Level 2)

**Domain:** Personnel Security (PS)  
**CMMC Level:** 2 (Advanced)  
**Number of Practices:** 2  
**Source Standard:** NIST SP 800-171

> **Note:** Personnel Security controls are primarily organizational/HR processes. Azure provides the identity lifecycle and access-revocation mechanisms that enforce the technical side of these controls.

---

## Practice Summary Table

| Practice ID | Practice Name | AZ-104 Domain | Azure Service(s) |
|------------|---------------|---------------|-----------------|
| PS.L2-3.9.1 | Screen Individuals | Identities & Governance | Entra ID (provisioning), Entitlement Management |
| PS.L2-3.9.2 | Terminate and Transfer Actions | Identities & Governance | Entra ID (account lifecycle), RBAC, PIM |

---

## Key Practice Details

### PS.L2-3.9.1 — Screen Individuals

**Control Description:** Screen individuals prior to authorizing access to organizational systems containing CUI.

**AZ-104 Mapping:**
- **Domain:** Manage Azure Identities and Governance
- **Skill:** Manage Microsoft Entra users; Configure Entitlement Management

**Azure Implementation:**
- **[Partial]** Background screening is an organizational/HR process.
- Provision **Entra ID accounts only after** screening clearance is recorded.
- Use **Entra ID Entitlement Management access packages** with an approval workflow so access to CUI resources requires documented sign-off.

```bash
# Verify when an account was created and its enabled state
az ad user show --id <upn> --query "{Created:createdDateTime, Enabled:accountEnabled}" -o table
```

**Evidence:** HR screening records tied to account creation dates; Entitlement Management approval history.

---

### PS.L2-3.9.2 — Terminate and Transfer Actions

**Control Description:** Ensure that organizational systems containing CUI are protected during and after personnel actions such as terminations and transfers.

**AZ-104 Mapping:**
- **Domain:** Manage Azure Identities and Governance
- **Skill:** Manage Microsoft Entra users; Manage RBAC

**Azure Implementation:**
- **On termination/transfer, immediately:**
  - Disable or delete the **Entra ID account**.
  - Revoke all **RBAC role assignments** and **PIM** eligible assignments.
  - Revoke active sessions/refresh tokens.
  - Transfer or remove the user's OneDrive/mailbox content per policy.
- Use **Entra ID Access Reviews** to detect and remove stale access from past transfers.

```bash
# Disable an account on termination
az ad user update --id <upn> --account-enabled false

# Revoke all active sessions (sign-in tokens)
az ad user revoke-sign-in-sessions --id <upn>

# List and remove the user's role assignments
az role assignment list --assignee <upn> --all -o table
az role assignment delete --assignee <upn>
```

**Evidence:** Account disablement timestamp vs. termination date; token revocation record; removed role assignments; Access Review results.

---

*Back to [README](../../README.md)*
