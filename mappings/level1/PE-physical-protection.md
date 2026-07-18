# PE – Physical Protection (CMMC Level 1)

**Domain:** Physical Protection (PE)  
**CMMC Level:** 1 (Foundational)  
**Number of Practices:** 4  
**Source Standard:** FAR 52.204-21

> **Note:** Physical protection controls primarily address the physical security of data centers and equipment. For Azure-hosted workloads, Microsoft manages data center physical security under the **Shared Responsibility Model**. Customer responsibilities apply to on-premises equipment and personnel practices.

---

> [!IMPORTANT]
> **Verify commands before use.** The Azure CLI and KQL examples below are
> illustrative references to show *how* a control is implemented — they are not
> tested deployment scripts. CLI syntax, policy definition IDs, and service
> capabilities change over time. Validate every command in a non-production
> subscription against current
> [Microsoft documentation](https://learn.microsoft.com/cli/azure/) before
> relying on it for compliance work.

## PE.L1-3.10.1 — Limit Physical Access

**Control Description:**  
Limit physical access to organizational information systems, equipment, and the respective operating environments to authorized individuals.

**NIST SP 800-171 Reference:** 3.10.1

### AZ-104 Mapping

| Field | Value |
|-------|-------|
| **AZ-104 Exam Domain** | Implement and Manage Virtual Networking |
| **AZ-104 Skill** | Secure access to virtual networks; Configure Azure Bastion |
| **Azure Service(s)** | Azure Bastion, Microsoft Entra ID (device compliance), Microsoft Intune |

### Azure Implementation (Cloud Workloads)

**Microsoft's Responsibility:**
- Physical access to Azure data centers is controlled via badge readers, biometrics, mantrap entry, and 24/7 security.
- Microsoft holds ISO 27001, SOC 2, and FedRAMP High authorizations covering physical access.

**Customer's Responsibility (on-premises / hybrid):**
- Implement physical access controls for any on-premises servers or equipment in scope.
- Use **Azure Bastion** to eliminate the need for public RDP/SSH access — reducing the attack surface related to remote physical/logical access.

```bash
# Deploy Azure Bastion in a VNet
az network bastion create \
  --name <bastion-name> \
  --public-ip-address <pip-name> \
  --resource-group <rg-name> \
  --vnet-name <vnet-name> \
  --location <region>
```

**Document:** Reference Microsoft's Shared Responsibility documentation in your SSP for this control.

---

## PE.L1-3.10.3 — Escort Visitors

**Control Description:**  
Escort visitors and monitor visitor activity.

**NIST SP 800-171 Reference:** 3.10.3

### AZ-104 Mapping

| Field | Value |
|-------|-------|
| **AZ-104 Exam Domain** | Monitor and Maintain Azure Resources |
| **AZ-104 Skill** | Monitor resources using Azure Monitor; Configure audit logging |
| **Azure Service(s)** | Azure Monitor, Microsoft Entra Audit Logs, Microsoft Sentinel |

### Azure Implementation (Cloud Workloads)

**Microsoft's Responsibility:**
- Azure data centers require all visitors to be registered, badged, and escorted at all times.
- Visitor logs are maintained and available in Microsoft's compliance documentation.

**Customer's Responsibility:**
- For on-premises or co-located environments, organizations must implement visitor escort policies.
- Enable Entra ID audit logs to track guest/B2B user access, which is the logical equivalent.

```bash
# Enable diagnostic settings to send audit logs to Log Analytics
az monitor diagnostic-settings create \
  --name "AuditLogs" \
  --resource /subscriptions/<sub-id>/resourceGroups/<rg>/providers/Microsoft.Insights/... \
  --logs '[{"category":"AuditLogs","enabled":true}]' \
  --workspace <log-analytics-workspace-id>
```

---

## PE.L1-3.10.4 — Physical Access Logs

**Control Description:**  
Maintain audit logs of physical access.

**NIST SP 800-171 Reference:** 3.10.4

### AZ-104 Mapping

| Field | Value |
|-------|-------|
| **AZ-104 Exam Domain** | Monitor and Maintain Azure Resources |
| **AZ-104 Skill** | Configure Azure Monitor Logs; Create and configure Log Analytics workspaces |
| **Azure Service(s)** | Azure Monitor, Log Analytics, Microsoft Entra Sign-in Logs |

### Azure Implementation

**Microsoft's Responsibility:**
- Azure data centers maintain physical access logs including date/time, individual identity, and reason for access.
- Available through Microsoft compliance documentation and FedRAMP audit packages.

**Customer-Side Logical Controls:**
- Enable **Azure Activity Logs** to record all management-plane access.
- Send logs to a **Log Analytics workspace** for retention and querying.
- Set retention to at least 90 days (NIST requirement) — 1 year recommended.

```bash
# Create a Log Analytics workspace
az monitor log-analytics workspace create \
  --resource-group <rg-name> \
  --workspace-name <workspace-name> \
  --retention-time 365

# Link Activity Log to workspace
az monitor diagnostic-settings create \
  --name "ActivityLogs" \
  --resource /subscriptions/<sub-id> \
  --logs '[{"category":"Administrative","enabled":true},{"category":"Security","enabled":true}]' \
  --workspace <workspace-id>
```

---

## PE.L1-3.10.5 — Manage Physical Access Devices

**Control Description:**  
Control and manage physical access devices.

**NIST SP 800-171 Reference:** 3.10.5

### AZ-104 Mapping

| Field | Value |
|-------|-------|
| **AZ-104 Exam Domain** | Manage Azure Identities and Governance |
| **AZ-104 Skill** | Manage Microsoft Entra device settings; Manage device registrations |
| **Azure Service(s)** | Microsoft Entra ID (device management), Microsoft Intune |

### Azure Implementation

**Microsoft's Responsibility:**
- Badge readers, key card systems, and other physical access devices in Azure data centers are managed and audited by Microsoft.

**Customer-Side Device Management:**
- Use **Microsoft Entra ID device registration** and compliance policies (via Intune) to manage devices that access Azure resources.
- Revoke device access immediately upon employee departure.
- Use Conditional Access to block access from non-compliant devices.

```bash
# List Entra ID registered devices
az ad device list --output table

# Delete (revoke) a device
az ad device delete --id <device-object-id>
```

---

*Back to [Level 1 Index](../../README.md) | Next: [SC – System and Communications Protection](SC-system-communications-protection.md)*
