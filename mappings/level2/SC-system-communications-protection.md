# SC – System and Communications Protection (CMMC Level 2)

**Domain:** System and Communications Protection (SC)  
**CMMC Level:** 2 (Advanced)  
**Number of Practices:** 16  
**Source Standard:** NIST SP 800-171

---

## Practice Summary Table

| Practice ID | Practice Name | AZ-104 Domain | Azure Service(s) |
|------------|---------------|---------------|-----------------|
| SC.L1-3.13.1 | Boundary Protection | Virtual Networking | NSG, Azure Firewall |
| SC.L1-3.13.5 | Public System Separation | Virtual Networking | VNet (DMZ), Private Endpoints |
| SC.L2-3.13.2 | Security Engineering Principles | Compute / Networking | Defender for Cloud, Azure Architecture |
| SC.L2-3.13.3 | Role Separation | Identities & Governance | RBAC, PIM |
| SC.L2-3.13.4 | Shared Resource Control | Compute | VM isolation, Dedicated Hosts |
| SC.L2-3.13.6 | Network Communication by Exception | Virtual Networking | NSG, Azure Firewall (deny by default) |
| SC.L2-3.13.7 | Split Tunneling | Virtual Networking | VPN Gateway (force tunneling) |
| SC.L2-3.13.8 | Data in Transit Encryption | Storage / Networking | TLS 1.2+, VPN/ExpressRoute |
| SC.L2-3.13.9 | Network Disconnect | Virtual Networking | Conditional Access (session timeout) |
| SC.L2-3.13.10 | Key Management | Storage / Identities | Azure Key Vault |
| SC.L2-3.13.11 | FIPS-Validated Cryptography | Storage / Networking | Azure FIPS 140-2 compliance |
| SC.L2-3.13.12 | Collaborative Computing | Compute | Azure Policy, Intune |
| SC.L2-3.13.13 | Mobile Code | Compute | Defender for Cloud, App Service |
| SC.L2-3.13.14 | VoIP | Networking | (organizational policy) |
| SC.L2-3.13.15 | Communications Authenticity | Virtual Networking | Azure VPN, ExpressRoute |
| SC.L2-3.13.16 | Data at Rest | Storage | Azure Disk Encryption, SSE, CMK |

---

## Key Practice Details

### SC.L2-3.13.8 — Data in Transit Encryption

**Control Description:** Implement cryptographic mechanisms to prevent unauthorized disclosure of CUI during transmission unless otherwise protected by alternative physical safeguards.

**AZ-104 Mapping:**
- **Domain:** Implement and Manage Storage / Virtual Networking
- **Skill:** Configure Azure Storage security; Configure VPN Gateway; Configure App Service TLS

**Azure Implementation:**

**Step 1 — Enforce TLS 1.2 or higher on all Azure services:**
```bash
# Enforce minimum TLS 1.2 on Storage Account
az storage account update \
  --name <storage-account-name> \
  --resource-group <rg-name> \
  --min-tls-version TLS1_2

# Enforce HTTPS on App Service
az webapp update \
  --name <app-name> \
  --resource-group <rg-name> \
  --https-only true

# Enforce minimum TLS on Azure SQL
az sql server update \
  --name <sql-server-name> \
  --resource-group <rg-name> \
  --minimal-tls-version 1.2
```

**Step 2 — Use Azure VPN Gateway (IPsec/IKEv2) for site-to-site traffic:**
```bash
# Create VPN Gateway
az network vnet-gateway create \
  --name <vpn-gw-name> \
  --resource-group <rg-name> \
  --vnet <vnet-name> \
  --gateway-type Vpn \
  --vpn-type RouteBased \
  --sku VpnGw2 \
  --public-ip-address <pip-name>
```

**Step 3 — Use ExpressRoute for dedicated encrypted private connectivity:**
- ExpressRoute provides private Layer 3 connectivity without traversing the public internet.
- Enable **MACsec** on ExpressRoute Direct for Layer 2 encryption.

---

### SC.L2-3.13.10 — Key Management

**Control Description:** Establish and manage cryptographic keys for cryptography employed in organizational systems.

**AZ-104 Mapping:**
- **Domain:** Implement and Manage Storage
- **Skill:** Configure Azure Key Vault; Manage encryption keys

**Azure Implementation:**

**Step 1 — Use Azure Key Vault for all key management:**
```bash
# Create Key Vault with HSM-backed keys
az keyvault key create \
  --vault-name <vault-name> \
  --name <key-name> \
  --kty RSA \
  --size 4096 \
  --protection hsm
```

**Step 2 — Rotate keys regularly:**
```bash
# Configure automatic key rotation
az keyvault key rotation-policy update \
  --vault-name <vault-name> \
  --name <key-name> \
  --value @rotation-policy.json
```

**Step 3 — Use Customer-Managed Keys (CMK) for Storage:**
```bash
# Configure Storage Account to use CMK from Key Vault
az storage account update \
  --name <storage-account-name> \
  --resource-group <rg-name> \
  --encryption-key-source Microsoft.Keyvault \
  --encryption-key-vault <vault-uri> \
  --encryption-key-name <key-name> \
  --encryption-key-version <key-version>
```

---

### SC.L2-3.13.11 — FIPS-Validated Cryptography

**Control Description:** Employ FIPS-validated cryptography when used to protect the confidentiality of CUI.

**AZ-104 Mapping:**
- **Domain:** Implement and Manage Storage
- **Skill:** Configure Azure Storage encryption; Configure Azure Key Vault HSM

**Azure Implementation:**
- Azure services use FIPS 140-2 validated cryptographic modules by default.
- Azure Key Vault Premium tier uses HSMs validated at FIPS 140-2 Level 2.
- Azure Key Vault Managed HSM uses FIPS 140-2 Level 3 validated HSMs.
- Document Azure's FIPS compliance using the [Microsoft Service Trust Portal](https://servicetrust.microsoft.com/) in your SSP.

```bash
# Create a Managed HSM (FIPS 140-2 Level 3)
az keyvault create \
  --hsm-name <hsm-name> \
  --resource-group <rg-name> \
  --location <region> \
  --sku Standard_B1
```

---

### SC.L2-3.13.16 — Data at Rest Protection

**Control Description:** Protect the confidentiality of CUI at rest.

**AZ-104 Mapping:**
- **Domain:** Implement and Manage Storage
- **Skill:** Configure Azure Disk Encryption; Configure Storage encryption

**Azure Implementation:**

**Step 1 — Enable Azure Disk Encryption on all VMs:**
```bash
az vm encryption enable \
  --resource-group <rg-name> \
  --name <vm-name> \
  --disk-encryption-keyvault <keyvault-name>
```

**Step 2 — Enable Server-Side Encryption (SSE) on Storage (default):**
- Azure Storage is encrypted at rest by default using 256-bit AES.
- Optionally use Customer-Managed Keys (CMK) for additional control.

**Step 3 — Encrypt Azure SQL databases:**
- Transparent Data Encryption (TDE) is enabled by default on all Azure SQL databases.

```bash
# Verify TDE is enabled on Azure SQL
az sql db tde show \
  --resource-group <rg-name> \
  --server <sql-server-name> \
  --database <db-name>
```

---

*Back to [README](../../README.md) | See also: [Level 1 SC](../level1/SC-system-communications-protection.md)*
