# CM – Configuration Management (CMMC Level 2)

**Domain:** Configuration Management (CM)  
**CMMC Level:** 2 (Advanced)  
**Number of Practices:** 9  
**Source Standard:** NIST SP 800-171

---

## Practice Summary Table

| Practice ID | Practice Name | AZ-104 Domain | Azure Service(s) |
|------------|---------------|---------------|-----------------|
| CM.L2-3.4.1 | System Baseline | Compute / Governance | Azure Policy, VM Image Gallery |
| CM.L2-3.4.2 | Baseline Change Control | Compute / Governance | Azure Policy, ARM Templates, Bicep |
| CM.L2-3.4.3 | Security Configuration Analysis | Monitor & Maintain | Defender for Cloud, Azure Policy |
| CM.L2-3.4.4 | Unauthorized Change Detection | Monitor & Maintain | Azure Change Tracking, Azure Monitor |
| CM.L2-3.4.5 | Access Restrictions for Change | Identities & Governance | RBAC, PIM, Azure Blueprints |
| CM.L2-3.4.6 | Least Functionality | Compute / Governance | Azure Policy, VM extensions |
| CM.L2-3.4.7 | Nonessential Feature Removal | Compute | VM customization, App Service settings |
| CM.L2-3.4.8 | Application Execution Policy | Compute | Defender for Cloud (adaptive controls) |
| CM.L2-3.4.9 | User-Installed Software Control | Compute / Governance | Azure Policy, Intune |

---

## Key Practice Details

### CM.L2-3.4.1 — System Baseline

**Control Description:** Establish and maintain baseline configurations and inventories of organizational systems (including hardware, software, firmware, and documentation).

**AZ-104 Mapping:**
- **Domain:** Deploy and Manage Azure Compute Resources
- **Skill:** Configure VMs; Automate deployment with ARM templates/Bicep

**Azure Implementation:**

**Step 1 — Define baseline via ARM Templates or Bicep:**
- Store infrastructure-as-code (IaC) templates in source control.
- Baselines are version-controlled and auditable.

```bicep
// Example baseline VM definition (Bicep)
resource vm 'Microsoft.Compute/virtualMachines@2023-03-01' = {
  name: 'baseline-vm'
  location: resourceGroup().location
  properties: {
    hardwareProfile: { vmSize: 'Standard_D2s_v3' }
    osProfile: {
      adminUsername: 'azureadmin'
      windowsConfiguration: {
        enableAutomaticUpdates: true
        patchSettings: { patchMode: 'AutomaticByPlatform' }
      }
    }
  }
}
```

**Step 2 — Use Azure Compute Gallery for baseline images:**
- Create a Shared Image Gallery with hardened, approved OS images.
- Enforce use of approved images via Azure Policy.

**Step 3 — Maintain resource inventory:**
- Use **Azure Resource Graph** to query and export full resource inventory.

```bash
# Query all resources in a subscription
az graph query -q "Resources | project name, type, resourceGroup, location" \
  --subscriptions <sub-id> --output table
```

---

### CM.L2-3.4.2 — Baseline Change Control

**Control Description:** Establish and enforce security configuration settings for information technology products employed in organizational systems.

**AZ-104 Mapping:**
- **Domain:** Manage Azure Identities and Governance
- **Skill:** Configure Azure Policy; Configure Management Groups

**Azure Implementation:**
- Apply Azure Policy initiatives to enforce baseline settings (e.g., require disk encryption, enforce TLS 1.2, require specific VM SKUs).
- Use **Defender for Cloud's Azure Security Benchmark** as a baseline policy initiative.

```bash
# Apply the Azure Security Benchmark initiative
az policy assignment create \
  --name "azure-security-benchmark" \
  --policy-set-definition "1f3afdf9-d0c9-4c3d-847f-89da613e70a8" \
  --scope /subscriptions/<subscription-id>
```

---

### CM.L2-3.4.4 — Unauthorized Change Detection

**Control Description:** Detect and document changes to baseline configurations of systems.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Configure Change Tracking and Inventory; Configure Azure Monitor alerts

**Azure Implementation:**
- Enable **Azure Change Tracking and Inventory** (via Azure Monitor) on VMs.
- Tracks changes to software, services, registry keys, daemons, and files.
- Send change alerts to a Log Analytics workspace.

```bash
# Enable Change Tracking on a VM
az vm extension set \
  --resource-group <rg-name> \
  --vm-name <vm-name> \
  --name ChangeTracking-Windows \
  --publisher Microsoft.Azure.ChangeTrackingAndInventory
```

---

### CM.L2-3.4.6 — Least Functionality

**Control Description:** Configure the system to provide only essential capabilities.

**AZ-104 Mapping:**
- **Domain:** Deploy and Manage Azure Compute Resources
- **Skill:** Configure Azure VMs; Configure App Service settings

**Azure Implementation:**
- Disable unused VM extensions and features.
- Use **Azure Policy** to deny deployment of unauthorized resource types.
- For App Services, disable FTP, disable remote debugging, enforce HTTPS only.

```bash
# Enforce HTTPS only on App Service
az webapp update \
  --name <app-name> \
  --resource-group <rg-name> \
  --https-only true

# Disable FTP on App Service
az webapp config set \
  --name <app-name> \
  --resource-group <rg-name> \
  --ftps-state Disabled
```

---

*Back to [README](../../README.md)*
