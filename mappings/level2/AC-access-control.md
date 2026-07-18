# AC – Access Control (CMMC Level 2)

**Domain:** Access Control (AC)  
**CMMC Level:** 2 (Advanced)  
**Number of Practices:** 22  
**Source Standard:** NIST SP 800-171

> This file covers all Level 2 AC practices. Level 1 practices (AC.L1-3.1.1 and AC.L1-3.1.2) are included here with additional Level 2 requirements.

---

> [!IMPORTANT]
> **Verify commands before use.** The Azure CLI and KQL examples below are
> illustrative references to show *how* a control is implemented — they are not
> tested deployment scripts. CLI syntax, policy definition IDs, and service
> capabilities change over time. Validate every command in a non-production
> subscription against current
> [Microsoft documentation](https://learn.microsoft.com/cli/azure/) before
> relying on it for compliance work.

## Practice Summary Table

| Practice ID | Practice Name | AZ-104 Domain | Azure Service(s) |
|------------|---------------|---------------|-----------------|
| AC.L1-3.1.1 | Authorized Access Control | Identities & Governance | Entra ID, RBAC |
| AC.L1-3.1.2 | Transaction & Function Control | Identities & Governance | RBAC, Azure Policy |
| AC.L2-3.1.3 | Control CUI Flow | Virtual Networking | NSG, Azure Firewall, Private Endpoints |
| AC.L2-3.1.4 | Separation of Duties | Identities & Governance | RBAC, PIM |
| AC.L2-3.1.5 | Least Privilege | Identities & Governance | RBAC, PIM |
| AC.L2-3.1.6 | Non-Privileged Account Use | Identities & Governance | PIM, Entra ID |
| AC.L2-3.1.7 | Privileged Function Logging | Monitor & Maintain | Azure Monitor, Log Analytics |
| AC.L2-3.1.8 | Unsuccessful Logon Attempts | Identities & Governance | Entra ID Smart Lockout, Conditional Access |
| AC.L2-3.1.9 | Privacy & Security Notices | Identities & Governance | Conditional Access (Terms of Use) |
| AC.L2-3.1.10 | Session Lock | Identities & Governance | Conditional Access, Intune |
| AC.L2-3.1.11 | Session Termination | Identities & Governance | Conditional Access (Sign-in frequency) |
| AC.L2-3.1.12 | Control Remote Access | Virtual Networking | Azure Bastion, VPN Gateway, Conditional Access |
| AC.L2-3.1.13 | Remote Access Confidentiality | Virtual Networking | VPN Gateway, ExpressRoute |
| AC.L2-3.1.14 | Remote Access Routing | Virtual Networking | VPN Gateway (force tunneling) |
| AC.L2-3.1.15 | Privileged Remote Access | Identities & Governance | PIM, Azure Bastion |
| AC.L2-3.1.16 | Wireless Access Authorization | Identities & Governance | Entra ID, Intune (Wi-Fi profiles) |
| AC.L2-3.1.17 | Wireless Access Protection | Virtual Networking | Intune (WPA2/3 enforcement) |
| AC.L2-3.1.18 | Mobile Device Connection | Identities & Governance | Intune, Conditional Access |
| AC.L2-3.1.19 | Encrypt CUI on Mobile | Storage | Azure Information Protection, Intune |
| AC.L2-3.1.20 | External System Connections | Virtual Networking | Azure Firewall, NSG, Private Link |
| AC.L2-3.1.21 | Portable Storage Restriction | Identities & Governance | Intune (device restrictions) |
| AC.L2-3.1.22 | Public-Access System CUI | Storage | Azure Policy, Azure Storage (access control) |

---

## Key Practice Details

### AC.L2-3.1.3 — Control CUI Flow

**Control Description:** Control the flow of CUI in accordance with approved authorizations.

**AZ-104 Mapping:**
- **Domain:** Implement and Manage Virtual Networking
- **Skill:** Configure NSGs; Configure Azure Firewall; Configure Private Endpoints

**Azure Implementation:**
- Use NSG rules to restrict data flows between subnets containing CUI.
- Use Azure Firewall FQDN filtering to control outbound data flows.
- Use Private Endpoints to keep data flow within the Azure backbone.
- Use Azure Information Protection / Purview to classify and control CUI data movement.

---

### AC.L2-3.1.4 — Separation of Duties

**Control Description:** Separate the duties of individuals to reduce the risk of malevolent activity without collusion.

**AZ-104 Mapping:**
- **Domain:** Manage Azure Identities and Governance
- **Skill:** Manage RBAC; Configure Entra ID PIM

**Azure Implementation:**
- Assign different RBAC roles to different individuals (e.g., network admin vs. storage admin).
- Use PIM to ensure no single user holds both write and approve roles simultaneously.
- Use Azure Policy to enforce separation (e.g., prevent users from assigning their own roles).

```bash
# Example: deny self-role-assignment via Azure Policy
# Use the built-in policy: "Deny role assignment to subscription scope"
az policy assignment create \
  --name "deny-self-role-assignment" \
  --policy "<policy-definition-id>" \
  --scope /subscriptions/<subscription-id>
```

---

### AC.L2-3.1.5 — Least Privilege

**Control Description:** Employ the principle of least privilege, including for specific security functions and privileged accounts.

**AZ-104 Mapping:**
- **Domain:** Manage Azure Identities and Governance
- **Skill:** Manage RBAC; Configure PIM

**Azure Implementation:**
- Audit and remove excessive role assignments regularly.
- Use PIM for just-in-time privileged access.
- Create custom RBAC roles scoped to minimum required permissions.
- Review Azure Advisor and Entra ID Access Reviews periodically.

```bash
# List all role assignments for a user
az role assignment list --assignee <user-principal-name> --all --output table

# Create a custom role with minimal permissions
az role definition create --role-definition @custom-role.json
```

---

### AC.L2-3.1.8 — Unsuccessful Logon Attempts

**Control Description:** Limit unsuccessful logon attempts.

**AZ-104 Mapping:**
- **Domain:** Manage Azure Identities and Governance
- **Skill:** Configure Microsoft Entra Smart Lockout; Configure Conditional Access

**Azure Implementation:**
- Enable **Entra ID Smart Lockout** (enabled by default in Entra ID) — locks accounts after repeated failures.
- Configure the lockout threshold (default: 10 attempts) via Entra ID > Security > Authentication methods > Password protection.
- Use Conditional Access policies to block access from risky sign-in locations.

---

### AC.L2-3.1.12 — Control Remote Access

**Control Description:** Monitor, control, and protect remote access sessions.

**AZ-104 Mapping:**
- **Domain:** Implement and Manage Virtual Networking
- **Skill:** Configure Azure VPN Gateway; Configure Azure Bastion

**Azure Implementation:**
- Use **Azure Bastion** to provide browser-based RDP/SSH without exposing VMs to the internet.
- Use **Azure VPN Gateway** for site-to-site or point-to-site VPN connectivity.
- Require MFA for all remote access via Conditional Access.
- Log all Azure Bastion sessions to Azure Monitor.

```bash
# Enable diagnostic logs for Azure Bastion
az monitor diagnostic-settings create \
  --name "BastionLogs" \
  --resource <bastion-resource-id> \
  --logs '[{"category":"BastionAuditLogs","enabled":true}]' \
  --workspace <log-analytics-workspace-id>
```

---

### AC.L2-3.1.14 — Remote Access Routing

**Control Description:** Route remote access via managed access control points.

**AZ-104 Mapping:**
- **Domain:** Implement and Manage Virtual Networking
- **Skill:** Configure VPN Gateway; Configure forced tunneling

**Azure Implementation:**
- Configure **forced tunneling** on VPN connections to route all traffic through Azure Firewall or a central inspection point.
- Use User-Defined Routes (UDRs) to force traffic through Network Virtual Appliances (NVAs).

```bash
# Create a route table with a forced tunnel default route
az network route-table create \
  --name <route-table-name> \
  --resource-group <rg-name>

az network route-table route create \
  --route-table-name <route-table-name> \
  --resource-group <rg-name> \
  --name default-route \
  --address-prefix 0.0.0.0/0 \
  --next-hop-type VirtualAppliance \
  --next-hop-ip-address <firewall-private-ip>
```

---

*Back to [README](../../README.md) | See also: [Level 1 AC](../level1/AC-access-control.md)*
