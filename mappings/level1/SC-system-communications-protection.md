# SC – System and Communications Protection (CMMC Level 1)

**Domain:** System and Communications Protection (SC)  
**CMMC Level:** 1 (Foundational)  
**Number of Practices:** 2  
**Source Standard:** FAR 52.204-21

---

## SC.L1-3.13.1 — Boundary Protection

**Control Description:**  
Monitor, control, and protect organizational communications (i.e., information transmitted or received by organizational information systems) at the external boundaries and key internal boundaries of the information systems.

**NIST SP 800-171 Reference:** 3.13.1

### AZ-104 Mapping

| Field | Value |
|-------|-------|
| **AZ-104 Exam Domain** | Implement and Manage Virtual Networking |
| **AZ-104 Skill** | Configure Network Security Groups (NSGs); Configure Azure Firewall; Configure virtual network peering |
| **Azure Service(s)** | Azure Firewall, Network Security Groups (NSG), Azure DDoS Protection, Azure Front Door, Azure Application Gateway (WAF) |

### Azure Implementation

**Step 1 — Define network boundaries with VNets and Subnets:**
- Create a Virtual Network (VNet) with subnets to logically separate workloads.
- Use separate subnets for web tier, app tier, and database tier.

```bash
# Create a VNet with two subnets
az network vnet create \
  --resource-group <rg-name> \
  --name <vnet-name> \
  --address-prefix 10.0.0.0/16

az network vnet subnet create \
  --resource-group <rg-name> \
  --vnet-name <vnet-name> \
  --name frontend-subnet \
  --address-prefix 10.0.1.0/24

az network vnet subnet create \
  --resource-group <rg-name> \
  --vnet-name <vnet-name> \
  --name backend-subnet \
  --address-prefix 10.0.2.0/24
```

**Step 2 — Apply Network Security Groups (NSGs):**
- Attach NSGs to subnets and/or NICs to control inbound/outbound traffic.
- Use deny-all default rules and explicitly allow only required traffic.

```bash
# Create an NSG and deny all inbound by default (Azure default behavior)
az network nsg create \
  --resource-group <rg-name> \
  --name <nsg-name>

# Allow only HTTPS inbound
az network nsg rule create \
  --resource-group <rg-name> \
  --nsg-name <nsg-name> \
  --name allow-https \
  --priority 100 \
  --destination-port-ranges 443 \
  --protocol Tcp \
  --access Allow \
  --direction Inbound

# Associate NSG with subnet
az network vnet subnet update \
  --resource-group <rg-name> \
  --vnet-name <vnet-name> \
  --name frontend-subnet \
  --network-security-group <nsg-name>
```

**Step 3 — Deploy Azure Firewall for centralized boundary control:**
- Route all outbound traffic through Azure Firewall.
- Use Application and Network rules to filter traffic.
- Enable threat intelligence-based filtering.

**Step 4 — Enable DDoS Protection:**
- Enable Azure DDoS Protection (Standard tier) on VNets handling external traffic.

### Assessment Objective

Determine if organizational communications are monitored, controlled, and protected at external and key internal boundaries.

---

## SC.L1-3.13.5 — Public-Access System Separation

**Control Description:**  
Implement subnetworks for publicly accessible system components that are physically or logically separated from internal networks.

**NIST SP 800-171 Reference:** 3.13.5

### AZ-104 Mapping

| Field | Value |
|-------|-------|
| **AZ-104 Exam Domain** | Implement and Manage Virtual Networking |
| **AZ-104 Skill** | Configure virtual networks; Configure private access to Azure services; Configure service endpoints and private endpoints |
| **Azure Service(s)** | Azure VNet (DMZ pattern), Application Gateway, Azure Private Endpoints, Service Endpoints |

### Azure Implementation

**Step 1 — Create a DMZ architecture in Azure:**
- Use a dedicated "public" subnet for internet-facing resources (e.g., Application Gateway, Azure Firewall).
- Keep backend resources (databases, app servers) in private subnets with no public IPs.

**Step 2 — Disable public endpoints for backend services:**
- Remove public IP addresses from VMs handling internal workloads.
- Disable public network access on Storage Accounts, SQL Databases, and Key Vaults.

```bash
# Disable public access to a Storage Account
az storage account update \
  --name <storage-account-name> \
  --resource-group <rg-name> \
  --public-network-access Disabled

# Disable public access to Azure SQL
az sql server update \
  --name <sql-server-name> \
  --resource-group <rg-name> \
  --public-network-access Disabled
```

**Step 3 — Use Private Endpoints for PaaS services:**
- Create private endpoints so PaaS services (Storage, SQL, Key Vault) resolve to private IPs within your VNet.

```bash
# Create a private endpoint for a Storage Account
az network private-endpoint create \
  --name <pe-name> \
  --resource-group <rg-name> \
  --vnet-name <vnet-name> \
  --subnet backend-subnet \
  --private-connection-resource-id <storage-account-id> \
  --group-id blob \
  --connection-name <connection-name>
```

**Step 4 — Route public traffic through Application Gateway (WAF):**
- Place the Application Gateway in the public subnet.
- Configure WAF policies to inspect inbound web traffic.
- Backend pool targets should use private IPs only.

### Assessment Objective

Determine if subnetworks for publicly accessible system components are physically or logically separated from internal networks.

---

*Back to [Level 1 Index](../../README.md) | Next: [SI – System and Information Integrity](SI-system-information-integrity.md)*
