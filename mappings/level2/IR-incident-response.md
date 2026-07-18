# IR – Incident Response (CMMC Level 2)

**Domain:** Incident Response (IR)  
**CMMC Level:** 2 (Advanced)  
**Number of Practices:** 3  
**Source Standard:** NIST SP 800-171

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
| IR.L2-3.6.1 | Incident Handling | Monitor & Maintain | Microsoft Sentinel (SOAR), Defender for Cloud |
| IR.L2-3.6.2 | Incident Reporting | Monitor & Maintain | Defender for Cloud, Azure Monitor Alerts |
| IR.L2-3.6.3 | Incident Response Testing | Monitor & Maintain | Microsoft Sentinel (Playbooks) |

---

## Key Practice Details

### IR.L2-3.6.1 — Incident Handling

**Control Description:** Establish an operational incident-handling capability for organizational systems that includes preparation, detection, analysis, containment, recovery, and user response activities.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Configure Microsoft Sentinel; Configure Defender for Cloud automated responses

**Azure Implementation:**

**Step 1 — Deploy Microsoft Sentinel for SIEM/SOAR:**
- Sentinel provides detection (Analytic Rules), investigation (Incidents), and response (Playbooks/Logic Apps).

**Step 2 — Create Playbooks for automated containment:**
```json
// Example Logic App action: Block user on alert
{
  "trigger": "When a Microsoft Sentinel incident is created",
  "condition": "Severity == High",
  "action": "Disable Entra ID user account"
}
```

**Step 3 — Use Defender for Cloud's automated response:**
- Configure workflow automation in Defender for Cloud to trigger Logic Apps on specific alerts.
- Example: Automatically restrict NSG inbound rules when a VM is flagged for suspicious activity.

---

### IR.L2-3.6.2 — Incident Reporting

**Control Description:** Track, document, and report incidents to designated officials and/or authorities both internal and external to the organization.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Configure Azure Monitor alerts and action groups

**Azure Implementation:**
- Configure **Action Groups** in Azure Monitor to notify security teams via email, SMS, or webhook on incidents.
- Use Sentinel Incidents for tracking — assign, comment, and close incidents with audit trail.
- Configure Sentinel to export incidents to external ticketing systems (ServiceNow, Jira) via Logic Apps.

```bash
# Create an action group for security incident notification
az monitor action-group create \
  --name "SecurityIncidentTeam" \
  --resource-group <rg-name> \
  --short-name "SecIncident" \
  --email-receivers name=CISO email=ciso@yourdomain.com
```

> **[Partial]** Reporting to US-CERT / DIBCAC for DoD contractors is an organizational process that Azure supports through logging and notification but does not automate.

---

### IR.L2-3.6.3 — Incident Response Testing

**Control Description:** Test the organizational incident response capability.

**AZ-104 Mapping:**
- **Domain:** Monitor and Maintain Azure Resources
- **Skill:** Configure Microsoft Sentinel playbooks; Test automation runbooks

**Azure Implementation:**
- Test Sentinel Playbooks in the Logic Apps designer before live deployment.
- Use Sentinel's **"Run Playbook"** feature on test incidents to validate response.
- Schedule tabletop exercises and use Azure Monitor to validate alerting pipelines.

---

*Back to [README](../../README.md)*
