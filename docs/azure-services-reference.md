# Azure Services Quick Reference for CMMC Compliance

This page provides a quick reference of Azure services and which CMMC domains and AZ-104 exam domains they map to.

---

## Identity and Access Management

| Azure Service | CMMC Domain(s) | AZ-104 Domain | Key CMMC Practices |
|--------------|----------------|---------------|--------------------|
| Microsoft Entra ID | AC, IA | Identities & Governance | AC.L1-3.1.1, IA.L1-3.5.1, IA.L1-3.5.2 |
| Azure RBAC | AC | Identities & Governance | AC.L1-3.1.1, AC.L1-3.1.2, AC.L2-3.1.5 |
| Microsoft Entra PIM | AC, IA | Identities & Governance | AC.L2-3.1.5, AC.L2-3.1.6, AC.L2-3.1.15 |
| Conditional Access | AC, IA | Identities & Governance | AC.L2-3.1.8, AC.L2-3.1.9, IA.L2-3.5.3 |
| Entra ID Password Protection | IA | Identities & Governance | IA.L2-3.5.7, IA.L2-3.5.8 |
| Microsoft Entra ID Protection | IA, SI | Identities & Governance / Monitor | IA.L2-3.5.3, SI.L2-3.14.7 |
| Entra ID Access Reviews | AC, IA | Identities & Governance | AC.L2-3.1.5, IA.L2-3.5.6 |
| Microsoft Intune | AC, IA, MP | Identities & Governance | AC.L2-3.1.16, AC.L2-3.1.18, MP.L2-3.8.7 |

---

## Networking

| Azure Service | CMMC Domain(s) | AZ-104 Domain | Key CMMC Practices |
|--------------|----------------|---------------|--------------------|
| Network Security Groups (NSG) | AC, SC | Virtual Networking | AC.L2-3.1.3, SC.L1-3.13.1, SC.L2-3.13.6 |
| Azure Firewall | AC, SC | Virtual Networking | AC.L2-3.1.3, SC.L1-3.13.1, SC.L2-3.13.6 |
| Azure Bastion | AC, PE | Virtual Networking | AC.L2-3.1.12, PE.L1-3.10.1 |
| Azure VPN Gateway | AC, SC | Virtual Networking | AC.L2-3.1.12, AC.L2-3.1.14, SC.L2-3.13.7, SC.L2-3.13.8 |
| ExpressRoute | SC | Virtual Networking | SC.L2-3.13.8, SC.L2-3.13.15 |
| Azure Private Endpoints | AC, SC | Virtual Networking | AC.L2-3.1.3, SC.L1-3.13.5 |
| Azure DDoS Protection | SC | Virtual Networking | SC.L1-3.13.1 |
| Application Gateway (WAF) | SC | Virtual Networking | SC.L1-3.13.1, SC.L1-3.13.5 |
| Azure Virtual Network | AC, SC | Virtual Networking | AC.L2-3.1.3, SC.L1-3.13.1, SC.L1-3.13.5 |
| User-Defined Routes (UDRs) | AC, SC | Virtual Networking | AC.L2-3.1.14, SC.L2-3.13.7 |

---

## Storage and Data Protection

| Azure Service | CMMC Domain(s) | AZ-104 Domain | Key CMMC Practices |
|--------------|----------------|---------------|--------------------|
| Azure Disk Encryption (ADE) | MP, SC | Storage | MP.L1-3.8.3, SC.L2-3.13.16 |
| Azure Storage SSE | MP, SC | Storage | MP.L1-3.8.3, SC.L2-3.13.16 |
| Customer-Managed Keys (CMK) | MP, SC | Storage | SC.L2-3.13.10, SC.L2-3.13.16 |
| Azure Key Vault | IA, SC | Identities & Governance / Storage | IA.L2-3.5.10, SC.L2-3.13.10 |
| Azure Key Vault Managed HSM | SC | Storage | SC.L2-3.13.10, SC.L2-3.13.11 |
| Azure Backup | SI, MA | Monitor & Maintain / Compute | SI.L1-3.14.1, MA.L2-3.7.1 |
| Azure Site Recovery | SI | Monitor & Maintain | SI.L1-3.14.1 |
| Azure Storage (immutable) | AU | Monitor & Maintain | AU.L2-3.3.8 |
| Microsoft Purview | MP, AU | Storage | MP.L2-3.8.4, AU.L2-3.3.1 |
| Azure Information Protection | AC, MP | Storage | AC.L2-3.1.19, MP.L2-3.8.4 |

---

## Monitoring and Security

| Azure Service | CMMC Domain(s) | AZ-104 Domain | Key CMMC Practices |
|--------------|----------------|---------------|--------------------|
| Azure Monitor | AU, CM, SI | Monitor & Maintain | AU.L2-3.3.1, CM.L2-3.4.4, SI.L2-3.14.3 |
| Log Analytics Workspace | AU, CM, SI | Monitor & Maintain | AU.L2-3.3.1, AU.L2-3.3.5, AU.L2-3.3.8 |
| Microsoft Sentinel | AU, IR, SI | Monitor & Maintain | AU.L2-3.3.5, IR.L2-3.6.1, SI.L2-3.14.6 |
| Defender for Cloud | CA, CM, RA, SI | Monitor & Maintain | CA.L2-3.12.1, CM.L2-3.4.3, RA.L2-3.11.1 |
| Defender for Servers | SI, RA | Monitor & Maintain | SI.L1-3.14.2, RA.L2-3.11.2 |
| Defender for Storage | MP, SI | Monitor & Maintain / Storage | MP.L2-3.8.2, SI.L1-3.14.5 |
| Microsoft Antimalware | SI | Monitor & Maintain | SI.L1-3.14.2, SI.L1-3.14.4, SI.L1-3.14.5 |
| Azure Update Manager | CM, RA, SI | Monitor & Maintain | CM.L2-3.4.2, RA.L2-3.11.3, SI.L1-3.14.1 |
| Azure Change Tracking | CM | Monitor & Maintain | CM.L2-3.4.4 |
| Azure Service Health | SI | Monitor & Maintain | SI.L2-3.14.3 |
| NSG Flow Logs | AU, SC, SI | Monitor & Maintain | AU.L2-3.3.1, SI.L2-3.14.6 |

---

## Compute and Application

| Azure Service | CMMC Domain(s) | AZ-104 Domain | Key CMMC Practices |
|--------------|----------------|---------------|--------------------|
| Azure Virtual Machines | CM, SC, SI | Compute | CM.L2-3.4.1, SC.L2-3.13.4, SI.L1-3.14.2 |
| Azure Dedicated Hosts | SC | Compute | SC.L2-3.13.4 |
| Azure App Service | CM, SC | Compute | CM.L2-3.4.6, SC.L2-3.13.8 |
| Azure Compute Gallery | CM | Compute | CM.L2-3.4.1 |
| ARM Templates / Bicep | CM | Compute | CM.L2-3.4.1, CM.L2-3.4.2 |
| Azure Policy | AC, CM, SC | Identities & Governance | AC.L1-3.1.2, CM.L2-3.4.2, SC.L2-3.13.12 |
| Azure Automation | MA, SI | Monitor & Maintain | MA.L2-3.7.1, SI.L1-3.14.1 |
| Logic Apps | IR | Monitor & Maintain | IR.L2-3.6.1, IR.L2-3.6.2 |

---

## Shared Responsibility Summary

| Control Area | Microsoft's Responsibility | Customer's Responsibility |
|-------------|--------------------------|--------------------------|
| Physical data center security | Full (PE controls) | Document in SSP |
| Hypervisor and host OS | Full | N/A |
| Guest OS security | Customer | Patch, configure, monitor |
| Application security | Customer | Secure coding, WAF, AppSec |
| Identity and access | Shared | Configure, enforce, monitor |
| Data encryption at rest | Shared (default SSE) | Enable CMK for stricter control |
| Data encryption in transit | Shared (TLS defaults) | Enforce TLS 1.2+, configure VPN |
| Network boundary controls | Shared | Configure NSG, Firewall, VPN |
| Logging and monitoring | Shared | Enable, route, retain, alert |
| Incident response | Shared (platform alerts) | Implement SIEM, playbooks |
