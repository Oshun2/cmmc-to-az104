# CA – Security Assessment (CMMC Level 2)

**Domain:** Security Assessment (CA)  
**CMMC Level:** 2 (Advanced)  
**Number of Practices:** 4  
**Source Standard:** NIST SP 800-171

---

## Practice Summary Table

| Practice ID | Practice Name | AZ-104 Domain | Azure Service(s) |
|------------|---------------|---------------|-----------------|
| CA.L2-3.12.1 | Security Assessment | Monitor & Maintain | Defender for Cloud, Azure Policy |
| CA.L2-3.12.2 | Plan of Action | Monitor & Maintain | Defender for Cloud (recommendations) |
| CA.L2-3.12.3 | Security Control Monitoring | Monitor & Maintain | Defender for Cloud, Azure Monitor, Sentinel |
| CA.L2-3.12.4 | System Security Plan | Monitor & Maintain | Purview Compliance Manager |

---

## Key Practice Details

### CA.L2-3.12.1 — Security Assessment

**Control Description:** Periodically assess the security controls in organizational systems to determine if the controls are effective in their application.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Monitor security posture with Microsoft Defender for Cloud

**Azure Implementation:**
- Use the **Defender for Cloud Regulatory Compliance dashboard** with the **NIST SP 800-171 R2** standard enabled to continuously assess control effectiveness.
- Align resources to the **Microsoft Cloud Security Benchmark (MCSB)**.
- Conduct periodic manual assessments and document results.

```bash
# Enable the NIST 800-171 regulatory standard, then list assessment results
az security regulatory-compliance-standards list -o table
az security regulatory-compliance-controls list --standard-name "NIST-SP-800-171-R2" -o table
```

**Evidence:** Exported compliance report (PDF/CSV) from Defender for Cloud; documented assessment schedule.

---

### CA.L2-3.12.2 — Plan of Action

**Control Description:** Develop and implement plans of action designed to correct deficiencies and reduce or eliminate vulnerabilities in organizational systems.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Monitor and manage Defender for Cloud recommendations

**Azure Implementation:**
- Treat each open **Defender for Cloud recommendation** as a candidate **POA&M** item.
- Export recommendations and track remediation in a Plan of Action & Milestones (see [`audit/poam-template.csv`](../../audit/poam-template.csv)).
- Integrate with Azure DevOps Boards or a ticketing system for accountability.

```bash
# Export current security recommendations as POA&M source data
az security assessment list --query "[?status.code=='Unhealthy'].{Name:displayName, Resource:resourceDetails.id}" -o table
```

**Evidence:** Completed POA&M with owners, milestones, and target dates linked to specific recommendations.

---

### CA.L2-3.12.3 — Security Control Monitoring

**Control Description:** Monitor security controls on an ongoing basis to ensure the continued effectiveness of the controls.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Configure Azure Monitor; Configure Defender for Cloud

**Azure Implementation:**
- Enable **Defender for Cloud continuous assessment** across all subscriptions.
- Use **Azure Policy compliance state** to continuously verify baselines remain enforced.
- Use **Microsoft Sentinel** for ongoing monitoring of security events tied to control operation.

```bash
# Continuous Azure Policy compliance summary
az policy state summarize --query "value[0].results" -o json
```

**Evidence:** Continuous compliance dashboards; policy compliance trend over time; Secure Score history.

---

### CA.L2-3.12.4 — System Security Plan

**Control Description:** Develop, document, and periodically update system security plans that describe system boundaries, system environments of operation, how security requirements are implemented, and the relationships with or connections to other systems.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Monitor and manage Azure resources

**Azure Implementation:**
- **[Partial]** The System Security Plan (SSP) is a required organizational document.
- Use **Microsoft Purview Compliance Manager's CMMC Level 2 template** as a framework to structure and track SSP content.
- Document the Azure architecture (subscriptions, VNets, boundaries) using exported **Azure Resource Graph** inventory and network diagrams.

```bash
# Generate inventory and boundary data to support the SSP
az graph query -q "Resources | project name, type, resourceGroup, location" -o table
az network vnet list --query "[].{VNet:name, AddressSpace:addressSpace.addressPrefixes, RG:resourceGroup}" -o table
```

**Evidence:** Current SSP document; network/architecture diagrams; Purview Compliance Manager assessment.

---

*Back to [README](../../README.md)*
