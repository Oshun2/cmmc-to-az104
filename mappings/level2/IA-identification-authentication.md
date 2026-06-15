# IA – Identification and Authentication (CMMC Level 2)

**Domain:** Identification and Authentication (IA)  
**CMMC Level:** 2 (Advanced)  
**Number of Practices:** 11  
**Source Standard:** NIST SP 800-171

---

## Practice Summary Table

| Practice ID | Practice Name | AZ-104 Domain | Azure Service(s) |
|------------|---------------|---------------|-----------------|
| IA.L1-3.5.1 | Identification | Identities & Governance | Entra ID, Managed Identities |
| IA.L1-3.5.2 | Authentication | Identities & Governance | Entra ID MFA, Conditional Access |
| IA.L2-3.5.3 | Multifactor Authentication | Identities & Governance | Entra ID MFA, Conditional Access |
| IA.L2-3.5.4 | Replay-Resistant Authentication | Identities & Governance | Entra ID (FIDO2, Certificate-based) |
| IA.L2-3.5.5 | Identifier Reuse | Identities & Governance | Entra ID (account lifecycle) |
| IA.L2-3.5.6 | Identifier Handling | Identities & Governance | Entra ID (disable/delete accounts) |
| IA.L2-3.5.7 | Password Complexity | Identities & Governance | Entra ID Password Protection |
| IA.L2-3.5.8 | Password Reuse | Identities & Governance | Entra ID Password Protection |
| IA.L2-3.5.9 | Temporary Passwords | Identities & Governance | Entra ID (SSPR, temp access pass) |
| IA.L2-3.5.10 | Cryptographically Protected Passwords | Identities & Governance | Entra ID (hashed passwords) |
| IA.L2-3.5.11 | Obscure Feedback | Identities & Governance | Entra ID (default behavior) |

---

## Key Practice Details

### IA.L2-3.5.3 — Multifactor Authentication

**Control Description:** Use multifactor authentication for local and network access to privileged accounts and for network access to non-privileged accounts.

**AZ-104 Mapping:**
- **Domain:** Manage Azure Identities and Governance
- **Skill:** Configure MFA; Configure Conditional Access policies

**Azure Implementation:**

**Option 1 — Enable Security Defaults (Free tier):**
- Requires MFA for all users including admins.
- Enable via Entra ID > Properties > Manage Security Defaults.

**Option 2 — Conditional Access Policies (Recommended):**
- Require MFA for all users accessing cloud apps.
- Require phishing-resistant MFA (FIDO2 or certificate) for privileged roles.

```bash
# Conditional Access is managed via the Entra ID portal or MS Graph API
# Verify MFA registration for a user via Azure CLI
az ad user show --id <user-principal-name> --query "strongAuthenticationDetail"
```

**Supported MFA Methods (ranked by strength):**
1. FIDO2 security keys (strongest — phishing resistant)
2. Windows Hello for Business (phishing resistant)
3. Certificate-based authentication
4. Microsoft Authenticator (Passwordless)
5. Microsoft Authenticator (Push notification)
6. TOTP (Time-based One-Time Password)
7. SMS (weakest — not recommended for CUI)

---

### IA.L2-3.5.4 — Replay-Resistant Authentication

**Control Description:** Employ replay-resistant authentication mechanisms for network access to privileged and non-privileged accounts.

**AZ-104 Mapping:**
- **Domain:** Manage Azure Identities and Governance
- **Skill:** Configure authentication methods in Entra ID

**Azure Implementation:**
- Enable **FIDO2 security keys** or **certificate-based authentication** in Entra ID.
- Entra ID tokens use short-lived JWTs and nonces — inherently replay-resistant.
- Avoid SMS OTP for privileged accounts (vulnerable to SS7 replay attacks).

---

### IA.L2-3.5.7 — Password Complexity

**Control Description:** Enforce a minimum password complexity and change when passwords are created or changed.

**AZ-104 Mapping:**
- **Domain:** Manage Azure Identities and Governance
- **Skill:** Configure Entra ID Password Protection

**Azure Implementation:**
- Entra ID enforces minimum 8 characters by default (Microsoft recommends 14+).
- Enable **Entra ID Password Protection** to block banned passwords.
- For hybrid environments, deploy the Password Protection proxy agent to on-premises AD.

```bash
# Verify password protection is enabled
# Check via: Entra ID > Security > Authentication methods > Password protection
```

---

### IA.L2-3.5.10 — Cryptographically Protected Passwords

**Control Description:** Store and transmit only cryptographically protected passwords.

**AZ-104 Mapping:**
- **Domain:** Manage Azure Identities and Governance
- **Skill:** Manage Entra ID; Configure Azure Key Vault

**Azure Implementation:**
- Entra ID stores passwords as salted hashes (bcrypt-based) — never in plaintext.
- Use **Azure Key Vault** to store application secrets and connection strings instead of embedding in config.
- Enable **Key Vault soft delete** and **purge protection**.

```bash
# Create Key Vault with soft delete and purge protection
az keyvault create \
  --name <vault-name> \
  --resource-group <rg-name> \
  --enable-soft-delete true \
  --enable-purge-protection true

# Store a secret
az keyvault secret set \
  --vault-name <vault-name> \
  --name "app-db-password" \
  --value "<password>"
```

---

*Back to [README](../../README.md) | See also: [Level 1 IA](../level1/IA-identification-authentication.md)*
