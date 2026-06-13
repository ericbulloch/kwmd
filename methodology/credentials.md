# Engagement Credentials
**Engagement:** <!-- Name / IP range / date -->
**Domain:** <!-- domain.local -->
**DC IP:** <!-- x.x.x.x -->

---

## Credential Table

| Username | Password | NTLM Hash | Type | Source | Works On |
|----------|----------|-----------|------|--------|----------|
| administrator | Password123! | aad3b435b51404eeaad3b435b51404ee | local | SAM dump — WEB01 | WEB01 (SMB, RDP) |
| jsmith | Welcome1 | — | domain | /home/jsmith/.bash_history | SSH WEB01, WinRM WEB01 |
| svc_backup | — | 31d6cfe0d16ae931b73c59d7e0c089c0 | domain service | LSASS dump — WEB01 | SMB all hosts |

> **Type options:** `local` / `domain` / `domain service` / `domain admin` / `local admin`
> **Add a ✓ or ✗ next to each Works On entry as you confirm/deny**

---

## Hash Dumps

### WEB01 — SAM (local accounts)
```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
```

### DC01 — NTDS.dit (domain accounts)
```
<!-- paste secretsdump output here -->
```

### LSASS Dumps
```
<!-- paste pypykatz / mimikatz output here, note which host it came from -->
```

---

## Kerberos Tickets

| Ticket Type | Account | Target Service | Captured From | Expires | Status |
|-------------|---------|----------------|---------------|---------|--------|
| TGT | administrator@domain.local | krbtgt | DC01 LSASS | 10h | imported |
| TGS | svc_mssql | MSSQLSvc/SQL01 | Kerberoast | — | cracking |
| Golden | [forged] administrator | krbtgt | — | 10y | active |

> **Status options:** `captured` / `imported` / `cracking` / `cracked` / `expired` / `active`

---

## Keys & Tokens

### SSH Private Keys
```
<!-- Host found on: WEB01 /home/jsmith/.ssh/id_rsa -->
<!-- Works for: jsmith@10.10.10.5 -->
-----BEGIN OPENSSH PRIVATE KEY-----
...
-----END OPENSSH PRIVATE KEY-----
```

### API Keys / Tokens
| Type | Value | Source | Works On |
|------|-------|--------|----------|
| AWS Access Key | AKIA... | .env — WEB01 web root | AWS CLI |
| JWT | eyJ... | Cookie on /admin | app.domain.local |

### Cloud Credentials
```
<!-- AWS / Azure / GCP credentials found via SSRF, metadata, or config files -->
```

---

## Cracking Queue

| Hash | Type | Wordlist / Rules | Status |
|------|------|-----------------|--------|
| 31d6cfe0d16ae931b73c59d7e0c089c0 | NTLM | rockyou + best64 | cracking |
| $krb5tgs$23$*svc_backup*... | Kerberos 5 TGS (RC4) | rockyou + d3ad0ne | pending |
| $NETNTLMv2$jsmith$... | NetNTLMv2 | rockyou | cracked → Welcome1 |

> **Common Hashcat modes:** NTLM = 1000 · NetNTLMv1 = 5500 · NetNTLMv2 = 5600 · Kerberos TGS RC4 = 13100 · Kerberos TGS AES-128 = 19600 · Kerberos TGS AES-256 = 19700 · AS-REP = 18200 · md5crypt (`$1$`) = 500 · sha512crypt (`$6$`) = 1800 · bcrypt (`$2*$`) = 3200

---

## ADCS Certificates

> Certificate files obtained via ESC1, ESC8, Shadow Credentials, or other ADCS attacks.

| Account | Certificate File | Source / Attack | Expires | Used With | Status |
|---------|-----------------|-----------------|---------|-----------|--------|
| administrator@domain.local | admin.pfx | ESC1 — svc_backup enrolled | 1 year | Certipy auth / Rubeus asktgt | active |

> **Status options:** `obtained` / `active` / `used` / `expired`

**Convert certificate to TGT (Certipy):**
```bash
certipy auth -pfx admin.pfx -dc-ip DC_IP
```

**Convert certificate to TGT (Rubeus):**
```bash
Rubeus.exe asktgt /user:administrator /certificate:admin.pfx /password:CERT_PASSWORD /domain:domain.local /dc:DC_IP /ptt
```

**Retrieve NTLM hash from certificate (U2U — Certipy):**
```bash
# Certipy auth outputs the NTLM hash alongside the TGT automatically
certipy auth -pfx admin.pfx -dc-ip DC_IP
```

---

## Notes
<!-- Anything that doesn't fit above: password patterns observed, lockout policy, spray timing, etc. -->

- Password policy: min 8 chars, lockout after 5 attempts, 30 min window
- Pattern observed: `Season+Year!` (e.g. Summer2023!)
- Local admin hash reuse confirmed across: WEB01, DEV01
