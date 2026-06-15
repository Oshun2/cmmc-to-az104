# AT – Awareness and Training (CMMC Level 2)

**Domain:** Awareness and Training (AT)  
**CMMC Level:** 2 (Advanced)  
**Number of Practices:** 3  
**Source Standard:** NIST SP 800-171

> **Note:** Awareness and Training controls are primarily organizational/procedural. Azure provides supporting services for policy acknowledgment and access controls, but does not replace a security awareness training program.

---

## Practice Summary Table

| Practice ID | Practice Name | AZ-104 Domain | Azure Service(s) |
|------------|---------------|---------------|-----------------|
| AT.L2-3.2.1 | Role-Based Risk Awareness | Identities & Governance | Conditional Access (Terms of Use) |
| AT.L2-3.2.2 | Role-Based Training | Identities & Governance | Conditional Access (Terms of Use) |
| AT.L2-3.2.3 | Insider Threat Awareness | Monitor & Maintain | Microsoft Sentinel, Defender for Cloud |

---

## Key Practice Details

### AT.L2-3.2.1 — Role-Based Risk Awareness

**Control Description:** Ensure that managers, systems administrators, and users of organizational systems are made aware of the security risks associated with their activities and of the applicable policies, standards, and procedures related to the security of those systems.

**AZ-104 Mapping:**
- **Domain:** Manage Azure Identities and Governance
- **Skill:** Configure Conditional Access; Configure Terms of Use

**Azure Implementation:**
- Use **Conditional Access — Terms of Use** to require users to acknowledge security policies before accessing Azure resources.
- Requires Entra ID P1.

**Implementation Steps:**
1. Create a Terms of Use document (PDF) with security awareness content.
2. Upload to Entra ID > Security > Conditional Access > Terms of Use.
3. Create a Conditional Access policy requiring Terms of Use acceptance before cloud app access.

> **[Partial]** Azure ToU covers acknowledgment. A full security awareness training program (e.g., KnowBe4, Microsoft Viva Learning) must be implemented separately.

---

### AT.L2-3.2.2 — Role-Based Training

**Control Description:** Ensure that personnel are trained to carry out their assigned information security responsibilities before being granted access.

**Azure Implementation:**
- **[Partial]** This is primarily an organizational HR/training process.
- Use Conditional Access to block access until training completion is confirmed (via integration with an LMS).
- Entra ID Entitlement Management can gate resource access on group membership, where group assignment is contingent on completed training.

---

### AT.L2-3.2.3 — Insider Threat Awareness

**Control Description:** Provide security awareness training on recognizing and reporting potential threats posed by insiders.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Configure Microsoft Sentinel; Monitor user behavior

**Azure Implementation:**
- Enable **User and Entity Behavior Analytics (UEBA)** in Microsoft Sentinel.
- Configure insider threat detection rules in Sentinel.
- Monitor for data exfiltration patterns (large downloads, uploads to external storage).

```kql
// Detect large data downloads from blob storage
StorageBlobLogs
| where OperationName == "GetBlob"
| summarize TotalBytes = sum(ResponseBodySize) by CallerIpAddress, AccountName, bin(TimeGenerated, 1h)
| where TotalBytes > 1073741824  // Alert on > 1 GB per hour
```

> **[Partial]** Training content for insider threat awareness must be provided through an external training platform.

---

*Back to [README](../../README.md)*
