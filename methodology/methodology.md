# Penetration Testing Methodology

## 1. Pre-Engagement

### Scope Definition
1. **Identify in-scope targets** — obtain the full list of IP addresses, CIDR ranges, domains, subdomains, and web applications that are authorized for testing
2. **Identify out-of-scope systems** — explicitly list systems that must not be touched; document shared infrastructure, third-party services, and production-critical systems
3. **Clarify cloud scope** — confirm whether cloud accounts (AWS, Azure, GCP) are in scope and what actions are permitted; cloud providers have their own penetration testing policies
4. **Confirm third-party restrictions** — identify any CDNs, ISPs, SaaS providers, or shared hosting in the environment; these typically require separate authorization
5. **Define authorized attack paths** — confirm which attack vectors are permitted: external network, internal network, web application, social engineering, physical, wireless
6. **Confirm credentials provided** — document any credentials, VPN access, or accounts provided by the client for grey/white box testing

### Rules of Engagement (RoE)
1. **Testing windows** — confirm authorized testing hours (24/7 vs. business hours only) and any blackout periods (maintenance windows, business-critical dates)
2. **Prohibited techniques** — document explicitly banned actions: denial-of-service attacks, destructive exploits, data exfiltration beyond PoC, production database modification
3. **Evasion testing** — confirm whether security controls (AV, EDR, SIEM, IDS) should be evaded or if testing should be conducted without evasion to focus on vulnerabilities
4. **Social engineering authorization** — confirm whether phishing, vishing, or physical intrusion is authorized and to what extent
5. **Pivoting authorization** — confirm whether lateral movement and pivoting are authorized once a foothold is obtained; some engagements limit testing to the initial foothold
6. **Emergency stop conditions** — define conditions that require immediate cessation of testing (critical system instability, accidental data destruction, discovery of active threat actor)

### Legal Authorization
1. **Signed Statement of Work (SoW)** — ensure a signed contract is in place before any testing begins; defines services, timeline, and deliverables
2. **Signed Rules of Engagement document** — formal document specifying scope, permitted techniques, and restrictions; signed by authorized client representative
3. **Get-out-of-jail letter** — obtain a signed authorization letter on company letterhead that can be presented to law enforcement if testing activities are detected and reported
4. **NDA / confidentiality agreement** — ensure NDA is signed to protect client's sensitive information and findings
5. **Verify client ownership** — confirm the client actually owns or has authorization to test all in-scope systems; unauthorized testing of third-party systems is illegal regardless of client instruction
6. **CPTS exam note** — the exam letter of authorization (LoA) and scope sheet serve as your legal authorization; read them carefully before starting

### Goals & Objectives
1. **Define assessment type** — black box (no prior knowledge), grey box (partial knowledge/credentials), or white box (full knowledge/source code access)
2. **Define success criteria** — what constitutes a successful engagement: Domain Admin, specific flag capture, data exfiltration PoC, specific system compromise
3. **Identify key targets** — are there crown jewels (specific servers, databases, AD domain) that should be prioritized
4. **CPTS exam objectives** — the exam requires capturing specific flags throughout the network; read the exam letter thoroughly and note all flag locations and submission criteria
5. **Deliverables** — confirm what the client expects: executive summary, technical report, remediation guidance, retesting

### Communication Plan
1. **Identify primary contact** — the main point of contact at the client who can answer questions and receive urgent notifications during testing
2. **Identify emergency contact** — a 24/7 emergency contact for critical findings or incidents that require immediate client awareness
3. **Define escalation thresholds** — what findings require immediate notification vs. inclusion in the final report (typically: active threat actor, critical RCE on production, PII exposure)
4. **Reporting cadence** — agree on check-in frequency (daily status emails, weekly calls) and interim deliverable expectations
5. **Secure communication channel** — establish an encrypted channel (Signal, encrypted email with PGP) for sharing sensitive findings during the engagement
6. **Incident notification procedure** — agree on the process if testing causes unintended system instability or outage

### Attack Infrastructure Setup
1. **Provision attack machine** — ensure attack box is clean, updated, and has all required tools installed (Kali Linux, Parrot OS, or equivalent)
2. **VPN connectivity** — establish and verify VPN access to the client network; confirm routing and DNS resolution for in-scope targets
3. **C2 infrastructure** — if using a C2 framework (Metasploit, Cobalt Strike), set up listeners, redirectors, and confirm callbacks are received
4. **DNS and domain setup** — if phishing or external infrastructure is needed, provision domains and configure DNS records
5. **Tool staging** — stage common tools, wordlists (SecLists), and exploit frameworks; verify tooling works against test targets before the engagement
6. **Logging setup** — enable terminal logging (`script`, tmux logging) to capture all commands and output; critical for reporting accuracy and dispute resolution
7. **Timestamping** — ensure system clock is accurate and synchronized; all activities should be timestamped for the activity log

### Engagement Kickoff Checklist
1. **Confirm IP ranges and targets with client** — validate the final scope list immediately before testing begins; scope can change between contract and kickoff
2. **Verify network connectivity** — confirm you can reach in-scope targets; run a simple ping/port scan to verify connectivity before beginning enumeration
3. **Document start time** — record the exact date and time testing began; maintain a running activity log throughout the engagement
4. **Screenshot and document initial state** — capture the initial state of key targets where possible; useful for demonstrating changes made during testing
5. **Review provided credentials and access** — test any provided credentials/VPN access before starting; flag issues to the client immediately if access doesn't work
6. **Review prior reports** — if a prior pentest report was provided, review it to understand previously identified vulnerabilities and remediation status


## 2. Information Gathering & Reconnaissance

### Passive Recon

#### OSINT / Target Profiling
1. **Identify the organization's web presence** — main website, subdomains, related domains, and acquired companies
2. **Enumerate employees** — use LinkedIn to find employee names, roles, and departments; derive email format and username conventions
3. **Review job postings** — job listings often reveal tech stack, internal tools, software versions, and infrastructure details
4. **Check company social media** — Twitter/X, GitHub org pages, and blog posts can leak infrastructure and technology info
5. **Search for data breach exposure** — check if org credentials have appeared in known breaches (HaveIBeenPwned, DeHashed)
6. **Review public documents** — PDFs and Office docs indexed by search engines often contain metadata with internal usernames, software versions, and network paths

#### DNS Reconnaissance
See [DNS commands](commands.md#dns-port-53) for zone transfer, reverse lookups, and subdomain enumeration.

1. **WHOIS lookup** — identify registrant info, registration dates, nameservers, and related domains
2. **Passive DNS history** — check historical DNS records for previously hosted IPs and infrastructure changes
3. **Enumerate nameservers** — identify all authoritative nameservers for the target domain
4. **MX record enumeration** — mail server records reveal email providers and sometimes internal mail infrastructure
5. **TXT record enumeration** — SPF, DKIM, and DMARC records reveal email providers, cloud services, and sometimes internal hostnames
6. **Subdomain enumeration via passive sources** — use passive sources (VirusTotal, DNSDumpster, Amass passive mode) to find subdomains without touching the target

#### Google Dorking
1. **Find exposed files** — search for sensitive file types (PDF, XLS, DOC, SQL, ENV, CONFIG) hosted on the target domain
2. **Find login portals** — locate admin panels, VPN portals, and other authentication pages
3. **Find subdomains and virtual hosts** — use `site:` operator to enumerate indexed subdomains
4. **Find exposed directories** — look for open directory listings that may expose files and configs
5. **Find error messages** — error pages often leak software versions, stack traces, and internal paths
6. **Find cached/archived content** — Google cache and Wayback Machine can reveal old content, removed pages, and historical credentials

#### Shodan / Censys
1. **Search by organization / ASN** — find all internet-facing assets associated with the target without sending any traffic
2. **Identify open ports and services** — review banners, versions, and service info for all exposed hosts
3. **Review SSL certificates** — cert data reveals subdomains, internal hostnames, and org structure
4. **Look for exposed sensitive services** — flag any RDP, SMB, Telnet, or database ports exposed directly to the internet
5. **Check for known vulnerabilities** — Shodan flags CVEs associated with identified software versions
6. **Review historical data** — past scan data can reveal infrastructure that has since been taken offline

#### Certificate Transparency
1. **Query crt.sh** — search certificate transparency logs for all SSL certs issued for the target domain
2. **Enumerate subdomains from certs** — SANs (Subject Alternative Names) in certs often reveal subdomains not found by other methods
3. **Identify wildcard certs** — wildcard certificates hint at the subdomain naming conventions in use
4. **Check certificate history** — expired and revoked certs can reveal decommissioned infrastructure still worth investigating
5. **Note issuing CAs** — the certificate authority used may hint at cloud providers or hosting infrastructure

#### Social Media & LinkedIn
1. **Build employee list** — enumerate employees by name, title, and department to build a target list for phishing or password spraying
2. **Derive username format** — use known employee names to guess the organization's username convention (firstname.lastname, flastname, etc.)
3. **Identify IT and security staff** — sysadmins and developers often post about the tech they use
4. **Review GitHub profiles** — employee personal GitHub accounts may contain work-related code, credentials, or internal tooling
5. **Check for sensitive posts** — employees sometimes post screenshots, error messages, or network diagrams containing sensitive info

### Active recon

#### Port Scanning

See the following command references for syntax and examples:
- [Nmap commands](commands.md#nmap)
- [RustScan](commands.md#rustscan-faster-initial-port-discovery)
- [Masscan](commands.md#masscan-fastest--use-for-large-ranges)

1. **Fast full TCP scan** — scan all 65535 ports quickly to find open ports
2. **Targeted service/version scan** — run a deeper scan against only the open ports found in step 1
3. **Default script scan** — run default enumeration scripts against open ports to grab banners, versions, and basic vuln info
4. **UDP scan** — scan top common UDP ports (DNS, SNMP, TFTP, NFS, etc.) — often overlooked but critical
5. **Document everything** — note open ports, services, versions, and anything unusual

#### Service Enumeration

##### FTP (Port 21)
1. **Banner grab** — note the FTP software and version for CVE research
2. **Anonymous login check** — attempt to log in with `anonymous` / no password; list and download any accessible files
3. **Check for sensitive files** — look for configs, credentials, backups, or anything useful in accessible directories
4. **Test authenticated access** — if credentials are found elsewhere, try them here
5. **Check FTP software for known exploits** — research the version from the banner for public CVEs
6. **Check for misconfigured write permissions** — test if you can upload files (useful for dropping webshells if FTP root maps to a web directory)
7. **Check for clear-text credential sniffing opportunity** — FTP sends creds in plaintext; worth noting in report

##### SSH (Port 22)
1. **Banner grab** — note the SSH version and software for CVE research
2. **Check for username enumeration** — some older OpenSSH versions are vulnerable to user enumeration
3. **Test default / known credentials** — try common creds and any credentials found elsewhere in the engagement
4. **Check authentication methods** — determine if password auth is enabled or only key-based auth is allowed
5. **Check for weak algorithms** — note supported ciphers, MACs, and key exchange algorithms; older/weak ones may be exploitable
6. **Test with found private keys** — if any private keys are discovered on the target, attempt to use them
7. **Check SSH software for known exploits** — research the version from the banner for public CVEs

##### Telnet (Port 23)
1. **Banner grab** — identify the device type and OS from the banner; Telnet is common on network devices and legacy systems
2. **Test default credentials** — network devices have well-known defaults; always try vendor defaults
3. **Note cleartext transmission** — all Telnet traffic including credentials is sent in plaintext; note for reporting
4. **Test with all found credentials** — credential reuse from other services is common on devices running Telnet

##### SMTP (Port 25)
1. **Banner grab** — note the mail server software and version for CVE research
2. **User enumeration** — use VRFY, EXPN, and RCPT TO commands to enumerate valid users on the system
3. **Check for open relay** — test if the server will relay mail for unauthenticated users (useful for phishing or pivoting)
4. **Enumerate mail domain info** — identify the domain being served, hostnames, and any internal naming conventions revealed
5. **Test authenticated access** — if credentials are found, attempt to authenticate and access mailboxes
6. **Check for known exploits** — research the version from the banner for public CVEs
7. **Check for sensitive info in NDRs** — non-delivery reports can leak internal usernames, hostnames, and infrastructure details

##### DNS (Port 53)
1. **Identify DNS server type and version** — banner grab for software/version info for CVE research
2. **Query basic records** — enumerate A, AAAA, MX, NS, TXT, and SOA records for the target domain
3. **Attempt zone transfer** — try a full zone transfer (AXFR) against each nameserver; misconfigurations often expose all internal hostnames
4. **Subdomain enumeration** — brute-force subdomains to discover hidden or internal hosts
5. **Reverse DNS lookup** — perform reverse lookups on IP ranges to map hostnames to IPs
6. **Check for DNS zone walking** — if DNSSEC is in use, attempt NSEC/NSEC3 zone walking to enumerate records
7. **Look for internal naming conventions** — hostnames often reveal OS, role, or environment (e.g., `dc01`, `web-prod`, `sql-dev`)

##### HTTP/HTTPS (Ports 80,443)
- See dedicated [web enumeration methodology file](web_methodology.md)

##### Kerberos (Port 88)
1. **Confirm it's a Domain Controller** — Kerberos on port 88 almost always means you're dealing with AD; note the domain name
2. **Username enumeration (Kerbrute)** — enumerate valid domain usernames without authentication; valid users get a different response than invalid ones
3. **AS-REP Roasting** — check for accounts with pre-authentication disabled; request their AS-REP hashes and crack offline
4. **Password spraying** — once valid usernames are found, spray common passwords carefully (mind lockout policy)
5. **Kerberoasting** — if you have valid credentials, request service tickets (TGS) for SPNs and crack them offline
6. **Check for delegation issues** — look for unconstrained, constrained, or resource-based constrained delegation misconfigurations
7. **Note the domain and DC info** — domain name, DC hostname, and domain SID are all useful for later AD attacks

##### IMAP/POP3 (Ports 110,143,993,995)
1. **Banner grab** — note the mail server software and version for CVE research
2. **Test default / known credentials** — try common creds and any credentials found elsewhere in the engagement
3. **Enumerate mailboxes** — if authenticated, list all mailboxes and folders for sensitive content
4. **Search for credentials in emails** — look for password reset emails, internal credentials, or sensitive data shared via email
5. **Check for cleartext transmission** — POP3 (110) and IMAP (143) send data in plaintext; note if SSL/TLS (993/995) is not enforced
6. **Check for known exploits** — research the version from the banner for public CVEs
7. **Correlate with SMTP findings** — valid users found via SMTP enumeration are likely valid here too

##### WMI (Port 135)
1. **Confirm RPC endpoint mapper is accessible** — port 135 is the RPC endpoint mapper; WMI uses dynamic high ports after initial contact
2. **Test authenticated access** — WMI requires valid credentials; try any credentials found elsewhere in the engagement
3. **Enumerate system info** — if authenticated, pull OS version, hostname, installed software, running processes, and services
4. **Enumerate local users and groups** — check for local admins and other privileged accounts
5. **Check for command execution** — WMI can be used for remote code execution if you have valid credentials (useful for lateral movement)
6. **Look for credential exposure** — check if WMI is being used in scripts or scheduled tasks that may expose credentials
7. **Note for lateral movement** — WMI is a primary lateral movement technique in AD environments; credentials found elsewhere should always be tested here

##### SMB (Ports 139,445)
1. **Banner grab and version detection** — identify SMB version (SMBv1 vs SMBv2/v3) and OS; SMBv1 may indicate EternalBlue vulnerability
2. **Null session / anonymous access** — test unauthenticated access to list shares, users, and groups
3. **Enumerate shares** — list all accessible shares and check read/write permissions on each
4. **Check share contents** — look for sensitive files, configs, credentials, scripts, and backups in accessible shares
5. **Enumerate users and groups** — pull local users, groups, and domain info via RID cycling or RPC
6. **Test authenticated access** — try any credentials found elsewhere; recheck share access and permissions with each new credential set
7. **Check for known vulnerabilities** — test for EternalBlue (MS17-010), PrintNightmare, and other SMB CVEs based on OS/version
8. **Check for password policy** — enumerate the domain/local password policy to inform password spraying (avoid lockouts)
9. **Note for lateral movement** — SMB is a primary lateral movement technique; always retest with new credentials throughout the engagement

##### SNMP (Ports 161,162 (UDP))
1. **Identify SNMP version** — determine if SNMPv1/v2c (cleartext community strings) or SNMPv3 (authenticated/encrypted) is in use
2. **Brute-force community strings** — test default strings (`public`, `private`, `manager`) and brute-force others; community strings act as passwords
3. **Enumerate with read access (GET)** — if a valid community string is found, pull system info, running processes, installed software, network interfaces, and routing tables
4. **Enumerate user accounts** — SNMP can expose local user accounts and logged-in users on Windows hosts
5. **Check for write access (SET)** — test if the community string allows write access; this can lead to configuration changes or RCE
6. **Look for credentials in SNMP data** — configuration data pulled via SNMP sometimes contains cleartext credentials
7. **Check SNMPv3 for weak credentials** — if SNMPv3 is in use, attempt to brute-force the username/password combination

##### LDAP/LDAPS (Ports 389,636)
1. **Test anonymous / null bind** — check if unauthenticated LDAP queries are allowed; this can expose significant AD information
2. **Enumerate base DN** — identify the base distinguished name (e.g., `DC=domain,DC=local`) to scope all further queries
3. **Enumerate users** — pull all domain user accounts including attributes like description fields (often contain passwords)
4. **Enumerate groups** — identify privileged groups (Domain Admins, Enterprise Admins, etc.) and their members
5. **Enumerate computers** — list all domain-joined computers including OS versions and hostnames
6. **Enumerate GPOs and OUs** — organizational units and group policy objects can reveal security configurations and misconfigurations
7. **Check for sensitive attributes** — look for `userPassword`, `unixUserPassword`, `description`, and `info` fields that may contain credentials
8. **Check LDAPS certificate** — inspect the SSL cert on port 636 for hostnames, domain info, and validity issues
9. **Use credentials to expand access** — rerun all queries with any credentials found; authenticated LDAP reveals significantly more data

##### IPMI (Port 623 (UDP))
1. **Identify IPMI version and BMC type** — determine the vendor and firmware version (HP iLO, Dell iDRAC, Supermicro, etc.) for CVE research
2. **Check for IPMI 2.0 cipher 0 authentication bypass** — cipher suite 0 allows authentication with any password; a critical misconfiguration
3. **Dump password hashes (RAKP attack)** — IPMI 2.0 is vulnerable to an unauthenticated hash disclosure attack; capture and crack hashes offline
4. **Test default credentials** — vendors ship BMCs with well-known defaults (e.g., `ADMIN/ADMIN`, `root/calvin`); always test these
5. **Check for known CVEs** — research the specific BMC firmware version for public exploits
6. **Access the web management interface** — if credentials are found, log into the BMC web UI (typically on port 443/80) for full server control
7. **Note high-value target** — IPMI access is essentially physical access to the server; credentials here often reuse elsewhere in the environment

##### rsync (Port 873)
1. **List available modules** — connect anonymously to enumerate available rsync shares/modules
2. **Check for unauthenticated read access** — download the contents of any accessible module; often exposes sensitive files and configs
3. **Check for unauthenticated write access** — if writable, upload SSH keys or web shells for RCE
4. **Test with discovered credentials** — if credentials are found elsewhere, try them against rsync modules

##### MSSQL (Port 1433)
1. **Banner grab and version detection** — identify the SQL Server version; older versions have more public CVEs
2. **Test default / known credentials** — try `sa` with blank or common passwords; also try Windows credentials found elsewhere (MSSQL often uses Windows auth)
3. **Enumerate databases, tables, and columns** — if authenticated, map out the database structure and look for sensitive data
4. **Check for linked servers** — linked servers can allow pivoting to other SQL instances, sometimes with elevated privileges
5. **Check xp_cmdshell status** — determine if `xp_cmdshell` is enabled; if so, it allows OS command execution directly from SQL
6. **Attempt to enable xp_cmdshell** — if you have sysadmin privileges, attempt to enable it for RCE
7. **Check for credentials in database** — look for stored credentials, connection strings, and application config data in the databases
8. **Test Windows authentication** — MSSQL often integrates with AD; domain credentials found elsewhere may grant SQL access
9. **Check service account privileges** — identify what Windows account MSSQL runs as; sysadmin on SQL may mean SYSTEM on the OS

##### Oracle TNS (Port 1521)
1. **Banner grab and version detection** — identify the Oracle version; older versions (pre-11g) have significant unauthenticated vulnerabilities
2. **Enumerate SIDs / service names** — brute-force valid SIDs (database instance names) as they are required to connect; common ones include `ORCL`, `XE`, `DB`
3. **Test default credentials** — try well-known Oracle defaults (`sys/change_on_install`, `system/manager`, `scott/tiger`, etc.)
4. **Enumerate accounts once authenticated** — list database users, roles, and privileges; look for accounts with DBA role
5. **Check for OS interaction** — Oracle can interact with the OS via Java stored procedures or external procedures; test if this is possible
6. **Attempt privilege escalation within Oracle** — look for users with excessive privileges that can be exploited to gain DBA access
7. **Check for sensitive data in databases** — enumerate schemas, tables, and columns for credentials and sensitive information
8. **Check TNS Poison vulnerability** — older Oracle versions are vulnerable to TNS Poison (CVE-2012-1675) allowing MitM attacks against Oracle traffic

##### NFS (Port 2049)
1. **Enumerate available shares** — list all NFS exports on the target without authentication; misconfigured servers expose shares to everyone
2. **Check share permissions** — identify which shares allow unauthenticated access (`no_root_squash`, world-readable exports)
3. **Mount accessible shares** — mount readable shares and enumerate all files and directories for sensitive content
4. **Look for sensitive files** — search for SSH keys, credentials, config files, scripts, and backups
5. **Check for no_root_squash misconfiguration** — if enabled, a local root user can access the share as root on the remote server; allows privilege escalation
6. **Upload files for privilege escalation** — if write access exists and `no_root_squash` is set, plant a SUID binary or SSH key for privesc
7. **Check NFS version** — NFSv3 and earlier have weaker auth; note the version for CVE research

##### Docker API (Port 2375 / 2376)
1. **Check for unauthenticated Docker API** — port 2375 is the unencrypted API; if accessible, you have full control over the Docker daemon
2. **List running containers and images** — enumerate what's running and what images are available
3. **Mount the host filesystem** — run a privileged container with the host filesystem mounted; read/write any file on the host as root
4. **Escape to host** — use the Docker socket or API to break out of any container context and gain root on the host
5. **Check for Docker socket exposure** — `/var/run/docker.sock` mounted inside a container is equivalent to root on the host

##### MySQL (Port 3306)
1. **Banner grab and version detection** — identify the MySQL/MariaDB version for CVE research
2. **Test default / known credentials** — try `root` with no password or common passwords; also try credentials found elsewhere
3. **Check for remote root login** — determine if root can authenticate remotely (a critical misconfiguration)
4. **Enumerate databases, tables, and columns** — if authenticated, map out the structure and look for sensitive data (users, passwords, PII)
5. **Check for credentials in the mysql system database** — the `mysql.user` table stores hashed credentials that can be cracked offline
6. **Check FILE privilege** — if your user has FILE privilege, you can read local files from the OS (`LOAD_FILE`) or write files (`INTO OUTFILE`)
7. **Attempt to write a webshell** — if FILE privilege exists and the web root path is known, write a PHP webshell directly via SQL
8. **Check for UDF exploitation** — user-defined functions can be abused for OS command execution if conditions are met
9. **Check service account** — identify what OS user MySQL runs as; combined with FILE privilege this may lead to privesc

##### RDP (Port 3389)
1. **Banner grab and version detection** — identify the OS version from the RDP certificate and response for CVE research
2. **Check SSL certificate** — inspect the cert for hostname, domain, and any useful internal naming info
3. **Test default / known credentials** — try any credentials found elsewhere in the engagement; RDP is often the target for credential reuse
4. **Check for BlueKeep and related CVEs** — test for BlueKeep (CVE-2019-0708), DejaBlue, and other RDP RCE vulnerabilities based on OS version
5. **Check NLA requirements** — determine if Network Level Authentication is enforced; without NLA, you can reach the login screen unauthenticated
6. **Password spraying** — carefully spray common passwords against known usernames (mind lockout policy)
7. **Check for restricted admin mode** — if enabled, allows Pass-the-Hash attacks against RDP
8. **Screenshot the login screen** — the login screen may reveal the hostname, domain, and logged-in users
9. **Note for lateral movement** — RDP is a primary lateral movement technique; always test new credentials against RDP throughout the engagement

##### VNC (Port 5900+)
1. **Check for no authentication** — some VNC servers are configured with no password; attempt connection directly
2. **Test default / common passwords** — try blank password, `password`, `admin`, and other common VNC passwords
3. **Brute force the password** — VNC passwords are limited to 8 characters; targeted brute force is feasible
4. **Note screen access value** — VNC gives GUI access; useful for interacting with applications that don't have CLI interfaces

##### WinRM (Ports 5985,5986)
1. **Confirm WinRM is enabled** — port 5985 (HTTP) or 5986 (HTTPS) being open confirms WinRM is active; not all Windows hosts have it enabled by default
2. **Check SSL certificate on 5986** — inspect for hostname, domain, and internal naming info
3. **Test default / known credentials** — try any credentials found elsewhere; WinRM requires the user to be in the Remote Management Users group or be a local admin
4. **Attempt remote shell access** — if valid credentials are found, connect for an interactive PowerShell session
5. **Check for Pass-the-Hash** — WinRM supports NTLM authentication; Pass-the-Hash attacks may work with captured hashes
6. **Enumerate accessible hosts** — once inside, use WinRM to attempt connections to other hosts on the network (lateral movement)
7. **Note for lateral movement** — WinRM is one of the cleanest lateral movement techniques in AD environments; always test new credentials here throughout the engagement

##### Redis (Port 6379)
1. **Check for unauthenticated access** — Redis has no authentication by default; connect and run `INFO` to confirm access
2. **Enumerate stored data** — list all keys and dump values; may contain session tokens, credentials, or application data
3. **Check for write access** — if writable, use Redis to write an SSH key to `/root/.ssh/authorized_keys` or a cron job for RCE
4. **Check Redis version for known CVEs** — older versions have RCE vulnerabilities via RESP protocol abuse
5. **Check for authentication** — if a password is required, check for weak or default passwords

##### Jenkins (Port 8080 / 8443)
1. **Check for default credentials** — `admin/admin`, `admin/password`; first-install Jenkins often has no auth or default creds
2. **Check for anonymous access** — some Jenkins instances allow unauthenticated job viewing or building
3. **Execute Groovy script via Script Console** — if admin access is obtained, use the Script Console (`/script`) for direct OS command execution as the Jenkins service account
4. **Enumerate build job configurations** — job configs often contain credentials, API keys, and deployment scripts
5. **Check for credential stores** — Jenkins stores credentials in its credential manager; accessible via Groovy script if admin

##### Elasticsearch (Port 9200 / 9300)
1. **Check for unauthenticated access** — older Elasticsearch instances have no auth by default; query `/_cat/indices` to list all indexes
2. **Dump sensitive data** — enumerate indexes for credentials, PII, application data, and internal documents
3. **Check for known CVEs** — research the version for RCE vulnerabilities (CVE-2014-3120, CVE-2015-1427, etc.)
4. **Check for write access** — if writable, potentially abuse dynamic scripting for RCE on vulnerable versions

#### Credential Discovery
1. **Check for default credentials** — research default creds for all identified software, appliances, and services; many are never changed
2. **Hunt exposed config files** — look for web.config, .env, database.yml, wp-config.php, and similar files on web servers and accessible shares
3. **Search SMB shares** — spider all readable shares for files containing passwords, connection strings, or API keys
4. **Check publicly exposed repositories** — search GitHub/GitLab for the organization's repos; look for hardcoded credentials and secrets in commit history
5. **Check for credential files on hosts** — look for cleartext passwords in scripts, batch files, PowerShell history, and scheduled tasks
6. **Hunt for browser-saved credentials** — post-foothold; browsers store credentials that can be extracted
7. **Check password managers and credential stores** — look for KeePass databases, Windows Credential Manager, and similar stores
8. **Note credential reuse** — always try every credential found against every service; password reuse is extremely common

#### Password Attacks & Brute Forcing
See the following command references for syntax and examples:
- [Hashcat](commands.md#hashcat)
- [John the Ripper](commands.md#john-the-ripper)
- [Hydra](commands.md#hydra-online-brute-force)

1. **Build a targeted wordlist** — combine common password lists (rockyou, SecLists) with company-specific words, employee names, and discovered naming conventions
2. **Identify the password policy first** — enumerate lockout thresholds before spraying anything; a lockout will alert defenders and block access
3. **Username enumeration before spraying** — confirm valid usernames via Kerbrute, SMTP VRFY, or other methods before attempting any passwords
4. **Password spraying** — try one or two common passwords against all known users; safer than brute-force and avoids lockouts
5. **Credential stuffing** — test breached credential pairs from known data dumps against all discovered services
6. **Targeted brute force** — only brute-force individual accounts when no lockout policy exists or when you have a strong wordlist lead
7. **Hash cracking** — crack captured hashes (NTLM, NetNTLMv2, Kerberos tickets) offline using wordlists and rules
8. **Rule-based cracking** — apply Hashcat rules to mutate wordlists (append numbers/symbols, capitalize, leetspeak) for better coverage
9. **Always retest services with new credentials** — every new credential found should be immediately tested against all known services

### Host Discovery & Infrastructure Mapping
1. **Identify live hosts** — perform ping sweeps and ARP scans across in-scope IP ranges to find active hosts
2. **Map network ranges** — identify subnets, VLANs, and network segments in scope
3. **Identify key hosts** — flag Domain Controllers, web servers, databases, and other high-value targets early
4. **Reverse DNS lookups** — resolve hostnames for discovered IPs to reveal roles and naming conventions
5. **Traceroute / network topology** — map routing paths to understand network segmentation and pivot points
6. **Document everything** — maintain a running list of hosts, IPs, open ports, services, OS versions, and credentials as you go

## 3. Vulnerability Assessment

### CVE / Public Exploit Research
1. **Compile all identified versions** — gather every software name and version found during enumeration into one list
2. **Run automated vulnerability scan** — use Nessus, OpenVAS, or Nmap vuln scripts to baseline known CVEs; supplement with manual research
3. **Search Exploit-DB** — query each service/version for public exploits; note CVE numbers and exploit availability
4. **Search NVD (NIST)** — cross-reference CVEs for CVSS scores and detailed vulnerability descriptions
5. **Search GitHub for PoCs** — public proof-of-concept code is often available before Metasploit modules; search by CVE number
6. **Check Metasploit modules** — identify if reliable Metasploit modules exist for discovered vulnerabilities
7. **Check for unauthenticated vs authenticated exploits** — prioritize unauthenticated RCE; note which exploits require prior access
8. **Verify exploit applicability** — confirm OS, version, and patch level match before attempting; avoid noisy failed attempts
9. **Document findings** — record CVE, CVSS score, affected service, and exploit source for the report

### Misconfiguration Analysis
1. **Review anonymous / null access findings** — flag any service allowing unauthenticated access that shouldn't (SMB, FTP, LDAP, NFS)
2. **Review overly permissive shares** — identify readable/writable shares that expose sensitive data or allow file uploads
3. **Check for default credentials in use** — note any service still using vendor defaults; high-severity finding
4. **Review AD ACL misconfigurations** — flag dangerous permissions found during AD enumeration (GenericAll, WriteDACL, DCSync rights, etc.)
5. **Check for cleartext protocols in use** — FTP, Telnet, HTTP, SNMPv1/v2 transmitting credentials in cleartext
6. **Review GPO misconfigurations** — overly permissive policies, autologon credentials in SYSVOL, passwords in GPP files
7. **Hunt for GPP passwords in SYSVOL** — Group Policy Preferences stored encrypted passwords (MS14-025); the key is public and all domain users can read SYSVOL
8. **Check for delegation misconfigurations** — flag any hosts or accounts with unconstrained delegation, constrained delegation, or RBCD misconfigurations; flag for AD Attacks phase
9. **Check for ADCS misconfigurations** — enumerate Active Directory Certificate Services for ESC1-ESC8 vulnerabilities; misconfigured certificate templates are a major CPTS attack path
10. **Check for weak or self-signed certificates** — flag certificates that are expired, self-signed, or using weak algorithms; note any ADCS roles present
11. **Check for no_root_squash on NFS** — flag if present; high-severity misconfiguration
12. **Check for IPMI cipher 0** — flag if present; allows authentication bypass
13. **Check for SMBv1 in use** — flag if enabled; indicates unpatched systems potentially vulnerable to EternalBlue
14. **Prioritize misconfigs by exploitability** — rank findings by how directly they lead to access or privilege escalation

### Credential Analysis
1. **Catalog all discovered credentials** — compile usernames, passwords, hashes, and keys found throughout enumeration
2. **Test all credentials against all services** — systematically try each credential set against every accessible service
3. **Identify password patterns** — look for patterns (Season+Year, Company+Number) that suggest a password policy; build a targeted wordlist
4. **Check for credential reuse** — flag any credential that works on multiple systems; common and high-impact finding
5. **Attempt hash cracking** — crack all captured NTLM, NetNTLMv2, and Kerberos hashes offline
6. **Check for cleartext passwords in configs** — review all config files and scripts found during enumeration for hardcoded credentials
7. **Assess password complexity** — note if weak or predictable passwords are in use; document for reporting

### Web Application Vulnerability Assessment
- See dedicated [web enumeration methodology file](web_methodology.md)

### Password Policy Review
1. **Enumerate the domain password policy** — minimum length, complexity requirements, history, and lockout threshold/duration
2. **Enumerate fine-grained password policies** — specific groups may have different (weaker or stronger) policies applied
3. **Document lockout threshold** — this is the single most important number for safe password spraying; never exceed it
4. **Check for accounts with no lockout** — service accounts and some admin accounts may be exempt from lockout; safer targets for brute force
5. **Assess policy strength** — short minimum length, no complexity, or no lockout are reportable findings
6. **Note observation window** — some lockout policies reset the counter after a period; factor this into spray timing

### Attack Surface Summary
1. **List all confirmed vulnerabilities** — compile CVEs, misconfigs, and weak credentials into a single prioritized list
2. **Rank by exploitability and impact** — put unauthenticated RCE at the top; credential reuse and misconfigs next
3. **Identify the most likely initial foothold** — pick the highest-confidence path to first access before starting exploitation
4. **Map paths to high-value targets** — outline the steps from initial foothold to Domain Admin or other objectives
5. **Identify quick wins** — flag any finding that immediately yields access or data with minimal effort
6. **Note dependencies** — some exploits require prior access; map the chain (e.g., need SMB creds before MSSQL xp_cmdshell)
7. **Document for reporting** — every finding here needs a corresponding entry in the final report regardless of whether it was exploited

## 4. Exploitation

### Initial Foothold
1. **Review attack surface summary** — start from your prioritized list; don't randomly attempt exploits
2. **Attempt credential-based access first** — if valid credentials were found during recon, try them against SSH, RDP, WinRM, SMB before attempting exploits
3. **Exploit public-facing vulnerabilities** — attempt CVE-based exploits against identified vulnerable services in order of reliability
4. **Try anonymous / unauthenticated access paths** — anonymous FTP, SMB null sessions, NFS mounts, open LDAP; sometimes access is already there
5. **Exploit misconfigurations** — leverage misconfigs identified in VA (writable shares, no_root_squash, xp_cmdshell, etc.)
6. **Try default credentials on all remaining services** — always worth a final pass before moving to more complex techniques
7. **Confirm and stabilize access** — once a foothold is established, stabilize immediately before doing anything else (see Shell Handling)
8. **Document the exact steps taken** — record every command and technique used for the report

### Web Application Exploitation
- See dedicated [web enumeration methodology file](web_methodology.md)

### Service Exploitation
1. **Match exploit to exact version** — confirm the target version matches the exploit requirements before running anything
2. **Test in a safe environment first if possible** — some exploits are destructive; understand what they do before running against a live target
3. **Prefer reliable exploits over unstable ones** — a Metasploit module with a high reliability rating beats an untested GitHub PoC
4. **SMB exploitation** — EternalBlue (MS17-010), PrintNightmare, and other SMB CVEs; confirm SMBv1 is enabled before attempting EternalBlue
5. **RDP exploitation** — BlueKeep (CVE-2019-0708) and DejaBlue for older unpatched systems
6. **Database exploitation** — MSSQL xp_cmdshell for RCE, MySQL UDF/FILE privilege abuse, Oracle external procedures
7. **FTP exploitation** — anonymous write + web root = webshell; version-specific CVEs for RCE
8. **SNMP exploitation** — community string with write access can allow config changes leading to RCE on network devices
9. **IPMI exploitation** — cipher 0 bypass or RAKP hash dump for credential access; often leads to full server control
10. **Chain exploits when needed** — some paths require multiple steps (e.g., SNMP read → get creds → SSH → privesc)

### Password Attacks
1. **NTLM relay attacks** — use Responder to capture NTLMv2 hashes and relay them for authentication without cracking
2. **Pass-the-Hash** — use captured NTLM hashes directly for authentication against SMB, WMI, RDP (restricted admin), and WinRM
3. **Password spraying** — spray one or two passwords across all known accounts; respect lockout policy
4. **Credential stuffing** — test breached credential pairs from data dumps against all services
5. **AS-REP Roasting** — request hashes for accounts with pre-auth disabled; crack offline
6. **Kerberoasting** — request TGS tickets for SPN accounts; crack offline; works with any domain user
7. **Targeted brute force** — only against accounts with no lockout or when you have a strong lead on the password
8. **Hash cracking** — use Hashcat with rockyou + rules for NetNTLMv2, NTLM, and Kerberos tickets
9. **Re-test all services with new credentials** — every successful crack or capture should be immediately tested everywhere

### Payload Generation & Delivery
1. **Choose staged vs stageless payload** — stageless payloads are self-contained and more reliable over unstable connections; staged are smaller but require a handler to be reachable
2. **Match payload to target architecture** — confirm x86 vs x64 before generating; wrong architecture will fail silently or crash
3. **Choose the right payload format** — EXE, DLL, PowerShell, Python, PHP, ASP, WAR — match the format to the delivery method and target environment
4. **Generate with msfvenom** — use msfvenom for quick payload generation; specify LHOST, LPORT, format, and encoder as needed
5. **Craft manual payloads when AV blocks msfvenom** — bash one-liners, PowerShell reverse shells, and Python shells often bypass AV better than msfvenom defaults
6. **Set up your listener before delivering** — always have your handler running before executing the payload on target
7. **Test payload locally if possible** — verify the payload executes and connects back before sending to target

### AV / EDR Evasion
1. **Identify what's running first** — check AV/EDR product before attempting evasion; different products require different techniques
2. **Use LOLBins (Living off the Land)** — use built-in Windows binaries (certutil, rundll32, regsvr32, mshta, wscript) to avoid dropping custom executables
3. **AMSI bypass** — PowerShell's AMSI scans scripts before execution; bypass with known AMSI patching techniques before running offensive PowerShell tools
4. **Obfuscate PowerShell** — use encoding, string concatenation, and variable substitution to evade signature-based detection
5. **In-memory execution** — load and execute tools directly in memory using PowerShell or .NET reflection; avoids writing to disk
6. **Use custom compiled tools** — recompile common tools from source with modified strings and signatures to evade static detection
7. **Disable script block logging if possible** — reduces forensic artifacts from PowerShell activity
8. **Test with common AV evasion checkers** — verify payload detection rate before deploying against target

### Metasploit Usage
1. **Plan your one Metasploit use carefully** — the CPTS exam allows Metasploit for one exploitation only; save it for the most complex or reliable use case
2. **Use auxiliary modules freely** — scanners, enumeration, and brute-force auxiliary modules do not count as the one Metasploit exploit use
3. **Set up the handler correctly** — configure LHOST, LPORT, and payload to match your generated payload before executing
4. **Use multi/handler for all reverse shells** — Metasploit's multi/handler works with any reverse shell, not just msfvenom payloads
5. **Upgrade to Meterpreter when possible** — Meterpreter sessions provide superior post-exploitation capabilities (file transfer, pivoting, token manipulation)
6. **Use post-exploitation modules** — Metasploit has extensive post modules for enumeration, credential dumping, and privilege escalation
7. **Set up pivoting via Metasploit** — use `route add` and SOCKS proxy modules to pivot through compromised hosts to new network segments

### File Transfer Techniques

#### General
See the following command references for syntax and examples:
- [File Transfers commands](commands.md#file-transfers)
- [File Transfer payloads](payloads.md#file-transfers)

1. **Always verify file integrity after transfer** — check MD5/SHA256 hash on both ends to confirm the file wasn't corrupted
2. **Use encoded transfers when direct methods are blocked** — base64 encode files and decode on the target when binary transfers fail
3. **Set up a simple HTTP server on your attack box** — Python's built-in HTTP server is the fastest way to serve files to targets
4. **Use HTTPS when possible** — encrypted transfers avoid detection by network monitoring tools
5. **Clean up transferred files after use** — remove tools and payloads from the target when done to reduce forensic artifacts

#### Windows (Downloading to Target)
1. **PowerShell DownloadFile / DownloadString** — use `Invoke-WebRequest` or `(New-Object Net.WebClient).DownloadFile()` to pull files from your HTTP server
2. **PowerShell DownloadString + IEX** — download and execute scripts directly in memory without writing to disk
3. **certutil** — built-in LOLBin that can download files and decode base64; often overlooked by AV
4. **bitsadmin** — built-in Windows tool for background file transfers; less common but reliable
5. **SMB server** — set up an SMB share on your attack box with Impacket's smbserver; copy files using standard `copy` or `xcopy`
6. **Base64 encode and paste** — encode a file as base64, paste the string into a shell, and decode on target; works when no network transfer is possible

#### Windows (Uploading from Target)
1. **PowerShell upload to web server** — use `Invoke-RestMethod` or `Invoke-WebRequest` with POST to upload to a listener on your attack box
2. **SMB copy to attack box share** — copy files directly to your Impacket SMB share
3. **Base64 encode and copy** — encode sensitive files as base64 and paste the output to exfiltrate when no outbound transfer is possible
4. **Meterpreter download** — use `download` command in a Meterpreter session for reliable file retrieval

#### Linux (Downloading to Target)
1. **wget / curl** — primary tools for downloading files; wget for simple downloads, curl for more complex requests
2. **Python HTTP server + wget/curl** — serve files from your attack box with Python, download with wget or curl on target
3. **SCP** — if SSH access exists, use SCP for reliable encrypted file transfers in both directions
4. **Base64 encode and paste** — encode file as base64, echo the string on target, and decode; works in restricted shells
5. **Netcat file transfer** — pipe a file through netcat when other methods aren't available; set up listener on target, send from attack box
6. **/dev/tcp** — use bash's built-in `/dev/tcp` for file transfer when no tools are available

#### Linux (Uploading from Target)
1. **SCP to attack box** — use SCP to push files from target to your attack box over SSH
2. **curl POST** — upload files to a web listener on your attack box using curl's POST functionality
3. **Netcat** — pipe file contents through netcat to a listener on your attack box
4. **Base64 encode and copy** — encode the file, print it to the terminal, and copy the output manually

### Phishing / Social Engineering
- Part of a real-world engagement when explicitly authorized

### Shell Handling & Stabilization
See the following command references for syntax and examples:
- [Reverse Shells](payloads.md#reverse-shells)
- [Bind Shells](payloads.md#bind-shells)
- [Shell Upgrade & Stabilization](payloads.md#shell-upgrade--stabilization)

1. **Upgrade your shell immediately** — raw netcat shells are unstable; upgrade to a fully interactive TTY as soon as you land
2. **Linux shell upgrade** — use Python/Python3 pty spawn, then `stty` to set terminal size and enable job control
3. **Windows shell upgrade** — upgrade to PowerShell if in cmd; consider evil-winrm or a Meterpreter session for a better experience
4. **Note your current user and hostname** — first commands after landing should always be `whoami`, `hostname`, and `id`
5. **Check network interfaces** — identify all interfaces immediately; internal subnets reveal pivot opportunities
6. **Establish a stable C2 channel** — consider a Meterpreter session or other reliable handler for long engagements
7. **Avoid dropping to disk unnecessarily** — in-memory execution reduces forensic artifacts and AV detections
8. **Set up port forwarding if needed** — if the target has access to internal services you can't reach, set up tunneling immediately
9. **Keep notes on every shell** — record user, hostname, IP, and how access was obtained for each session

## 5. Post-Exploitation

### Automated Enumeration Tools
1. **Run LinPEAS on Linux** — comprehensive automated enumeration script; highlights privesc vectors, interesting files, and misconfigs in color-coded output
2. **Run WinPEAS on Windows** — Windows equivalent of LinPEAS; covers privileges, services, credentials, scheduled tasks, and more
3. **Run BloodHound / SharpHound** — collect AD relationship data and visualize attack paths to Domain Admin; essential for any AD environment
4. **Use PowerView for targeted AD queries** — supplement BloodHound with manual PowerView queries for specific enumeration tasks
5. **Use Seatbelt for Windows host checks** — focused Windows security configuration enumeration tool; great for finding quick wins
6. **Transfer tools carefully** — rename tools before transferring to avoid AV signature detection on common tool names
7. **Review tool output thoroughly** — automated tools generate a lot of output; look for highlighted/red items first, then review everything

### Network Enumeration from Foothold
1. **Check ARP cache** — reveals hosts the compromised machine has recently communicated with; faster than scanning
2. **Review routing table** — identifies all reachable subnets directly from the current host
3. **Check DNS resolution** — attempt to resolve internal hostnames; reveals naming conventions and host roles
4. **Enumerate reachable hosts on new subnets** — ping sweep or TCP probe new subnets discovered via routing table
5. **Check hosts file** — `/etc/hosts` or `C:\Windows\System32\drivers\etc\hosts` may contain internal hostnames not in DNS
6. **Identify internal services** — scan reachable hosts on new subnets for open ports to expand attack surface
7. **Note firewall rules** — check local firewall rules (`iptables`, Windows Firewall) to understand what outbound/inbound traffic is allowed
8. **Update your network map** — document all newly discovered hosts, subnets, and services; feed findings into pivot planning

### Situational Awareness
1. **Identify current user and privileges** — run `whoami /all` (Windows) or `id` (Linux); understand exactly what you have before proceeding
2. **Identify the hostname and role** — is this a workstation, server, DC, or database host? Shapes your next steps significantly
3. **Check network interfaces and routing** — identify all IP addresses, subnets, and routes; look for interfaces on internal segments not previously known
4. **Identify AV / EDR in use** — know what defensive tools are running before executing anything noisy; adjust tradecraft accordingly
5. **Check logging and monitoring** — identify if Sysmon, audit policies, or SIEM agents are present; note for operational security
6. **Identify active sessions and logged-in users** — other users logged in may have valuable tokens or sessions to hijack
7. **Note the OS version and patch level** — informs privilege escalation options
8. **Check domain membership** — confirm if the host is domain-joined and identify the domain name and DC

### Local Enumeration (Linux)
1. **Enumerate users and groups** — review `/etc/passwd`, `/etc/group`, and `/etc/shadow` (if readable) for accounts and hashes
2. **Check sudo rights** — `sudo -l` to see what commands the current user can run as root; common privesc vector
3. **Find SUID / SGID binaries** — binaries with SUID set run as their owner (often root); check GTFOBins for exploitation
4. **Enumerate cron jobs** — check system-wide and user cron jobs for writable scripts or paths that can be hijacked
5. **Review running processes** — look for processes running as root, unusual services, or processes with readable command-line arguments containing credentials
6. **Check installed software and versions** — look for outdated software with known local privesc CVEs
7. **Review network connections** — identify listening services only accessible locally; may expose additional attack surface
8. **Check for interesting files** — search home directories, `/tmp`, `/var`, `/opt`, and `/etc` for credentials, keys, configs, and backups
9. **Check capabilities** — Linux capabilities can grant elevated privileges without full SUID; enumerate with `getcap`
10. **Review environment variables and shell history** — `.bash_history`, `.zsh_history`, and env vars sometimes contain credentials

### Local Enumeration (Windows)
1. **Enumerate user privileges** — `whoami /priv`; look for SeImpersonatePrivilege, SeBackupPrivilege, SeDebugPrivilege, and other abusable privileges
2. **Enumerate local users and groups** — identify local admins and other privileged accounts on the host
3. **Check installed software** — look for outdated applications with known local privesc CVEs; check both 32-bit and 64-bit locations
4. **Enumerate running services** — look for services running as SYSTEM with weak permissions or unquoted paths
5. **Check scheduled tasks** — identify tasks running as SYSTEM or admin with writable script/binary paths
6. **Review registry autoruns** — check common autorun keys for writable entries that persist or escalate
7. **Check AppLocker and AV status** — understand what execution restrictions are in place before dropping tools
8. **Review network connections** — identify locally listening services not exposed externally
9. **Check PowerShell history** — `ConsoleHost_history.txt` often contains previously run commands with credentials
10. **Search for interesting files** — check user profiles, `C:\inetpub`, `C:\xampp`, `C:\Users\*\Desktop`, and config files for credentials
11. **Check for DPAPI-protected secrets** — browser credentials, Outlook passwords, and RDP credentials are protected by DPAPI; extract with Mimikatz or SharpDPAPI using the user's master key

### Sensitive Data Hunting
1. **Search for flags** — in CTF/CPTS context, look for `user.txt` and `root.txt` / `local.txt` and `proof.txt` in user home dirs and Desktop
2. **Search for credentials in files** — grep recursively for keywords like `password`, `passwd`, `secret`, `credential`, `api_key`
3. **Check configuration files** — web app configs, database connection strings, and service configs frequently contain plaintext credentials
4. **Review email and messaging data** — local mail spools, Outlook PST files, and chat logs can contain sensitive info and credentials
5. **Check browser data** — saved passwords, cookies, and browsing history in Chrome, Firefox, and Edge profiles
6. **Look for private keys** — SSH keys (`~/.ssh/`), certificate private keys, and PGP keys are high-value finds
7. **Check backup files** — `.bak`, `.old`, `.zip`, and similar files often contain copies of sensitive configs or databases
8. **Search network shares from the host** — the compromised host may have access to shares not reachable from your attack box

### Credential Harvesting
1. **Dump SAM database** — extract local NTLM hashes from the SAM hive (requires SYSTEM or admin); crack or use for PTH
2. **Dump LSASS** — extract cached credentials, NTLM hashes, and Kerberos tickets from memory; use Mimikatz, pypykatz, or similar
3. **Extract cached domain credentials** — domain-joined hosts cache credentials locally; extract from registry
4. **Dump NTDS.dit** — if on a DC, extract the Active Directory database for all domain hashes
5. **Extract Kerberos tickets** — dump TGTs and service tickets from memory for Pass-the-Ticket attacks
6. **Check Windows Credential Manager** — stored credentials for network shares, RDP sessions, and web logins
7. **Extract browser-saved passwords** — Chrome, Firefox, and Edge store credentials locally; extractable with user-level access
8. **Look for KeePass and other password manager databases** — `.kdbx` files are high value; check for weak master passwords
9. **Check for cleartext credentials in memory** — WDigest may be enabled on older systems; Mimikatz can extract plaintext passwords
10. **Extract LSA secrets** — LSA secrets are stored in the registry (`HKLM\SECURITY\Policy\Secrets`) and contain service account passwords, cached domain credentials, and the DPAPI machine key; requires SYSTEM access

### ADCS Enumeration
1. **Confirm ADCS is present** — check if Active Directory Certificate Services is installed; look for a CA server in the domain
2. **Enumerate certificate templates** — use Certify or Certipy to list all certificate templates and their permissions
3. **Check for ESC1** — enrollee can supply a Subject Alternative Name (SAN); request a cert as any user including Domain Admin
4. **Check for ESC2** — template has the Any Purpose EKU or no EKU; can be used for any purpose including authentication
5. **Check for ESC3** — template has Certificate Request Agent EKU; allows enrollment on behalf of other users
6. **Check for ESC4** — template has weak ACLs allowing modification; modify the template to introduce ESC1 vulnerability
7. **Check for ESC5** — Vulnerable PKI Object ACLs** — check for weak ACLs on the CA computer object itself, the `CN=Public Key Services` container, or certificate template objects in AD; write access to these allows escalation equivalent to ESC4
8. **Check for ESC6** — CA has EDITF_ATTRIBUTESUBJECTALTNAME2 flag set; allows SAN in any request regardless of template
9. **Check for ESC7** — CA has weak ACLs; manage CA or issue certificates permissions granted to low-privileged users
10. **Check for ESC8** — CA web enrollment endpoint is enabled; NTLM relay to ADCS HTTP endpoint for certificate on behalf of relayed user
11. **Request and use certificates for authentication** — use obtained certificates with PKINIT for Kerberos authentication or LDAP over TLS

### Pillaging
1. **Identify data of value** — look for intellectual property, financial data, PII, and anything the client would consider sensitive
2. **Check mapped network drives** — the compromised host likely has access to file shares containing valuable data
3. **Review database contents** — if a database is accessible from the host, enumerate tables for sensitive records
4. **Check email archives** — PST files, local mail, and cached Exchange data can contain highly sensitive communications
5. **Look for documentation** — network diagrams, password spreadsheets, runbooks, and IT docs are often stored on internal shares
6. **Document all sensitive findings** — record what was found and where for inclusion in the report; do not exfiltrate data beyond what is authorized

### Persistence
- In a real engagement, document all persistence mechanisms and remove them at engagement close
- Common techniques include scheduled tasks, registry autoruns, web shells, and SSH key injection

### Active Directory Enumeration
1. **Identify AD presence** — confirm you're in an AD environment via DNS, Kerberos on port 88, LDAP on 389, or SMB domain info
2. **Enumerate domain users** — build a full user list; description fields often contain passwords
3. **Enumerate domain groups** — identify privileged groups (Domain Admins, Enterprise Admins, Account Operators, Backup Operators, etc.) and their members
4. **Enumerate domain computers** — list all domain-joined hosts including OS versions; identify DCs, servers, and workstations
5. **Enumerate GPOs** — group policy objects can reveal security settings, deployed software, and potential misconfigurations
6. **Enumerate ACLs** — look for misconfigured access control entries that grant unprivileged users dangerous rights (GenericAll, WriteDACL, ForceChangePassword, etc.)
7. **Enumerate trusts** — identify domain and forest trusts; trust relationships can enable cross-domain/forest attacks
8. **Enumerate SPNs** — service principal names identify accounts running services; SPN-set accounts are Kerberoasting targets
9. **Enumerate shares across the domain** — spider accessible SMB shares across all domain hosts for sensitive files and credentials
10. **Map attack paths** — use findings to plan the shortest path to Domain Admin

## 6. Lateral Movement

### Credential Reuse
1. **Test every credential against every host** — always the first thing to try; password reuse is the most common lateral movement path
2. **Build a credential matrix** — maintain a table of username/password/hash combinations and which hosts/services they work on
3. **Test against all remote services** — SSH, RDP, WinRM, SMB, WMI, MSSQL, and any other service found during enumeration
4. **Test local admin credentials across all hosts** — organizations often use the same local admin password everywhere; one compromise can mean all hosts
5. **Test domain credentials against all domain-joined hosts** — valid domain creds may grant local admin or remote access on other machines
6. **Re-test after every new credential find** — add new credentials to the matrix and retest immediately

### CrackMapExec (CME)
1. **Spray credentials across all hosts** — CME can test a credential pair against an entire subnet in one command across SMB, WinRM, MSSQL, SSH, and RDP
2. **Spray hashes (PTH)** — CME natively supports Pass-the-Hash; spray captured NTLM hashes across all hosts as efficiently as plaintext creds
3. **Enumerate logged-in users** — identify which users are currently or recently logged into each host; reveals high-value targets for token theft
4. **Enumerate shares** — spider SMB shares across all domain hosts in one pass; flag readable/writable shares
5. **Execute commands on accessible hosts** — once access is confirmed, run commands directly via CME for quick post-exploitation without a full shell
6. **Run built-in modules** — CME has modules for SAM dumping, LSASS dumping, BloodHound collection, and more without transferring additional tools
7. **Use `--continue-on-success`** — prevent CME from stopping after first valid login; map all hosts where credentials work

### Responder / NTLM Relay (Mid-Engagement)
See the following command references for syntax and examples:
- [Responder & NTLM Relay commands](commands.md#responder--ntlm-relay)

1. **Run Responder in analyze mode first** — identify traffic on the network before poisoning anything; avoid unnecessary noise
2. **Poison LLMNR / NBT-NS / mDNS** — capture NTLMv2 hashes from hosts making failed name resolution requests
3. **Identify SMB signing disabled hosts** — these are relay targets; enumerate with CME or Nmap before relaying
4. **Relay to SMB** — relay captured authentication to hosts with SMB signing disabled for direct access
5. **Relay to LDAP** — relay to LDAP for creating accounts, modifying ACLs, or setting up RBCD; more powerful than SMB relay in many scenarios
6. **Relay to MSSQL** — relay authentication to SQL Server for command execution
7. **Use mitm6 alongside Responder** — IPv6 DNS poisoning captures authentications that LLMNR/NBT-NS poisoning misses
8. **Crack captured hashes offline** — NetNTLMv2 hashes that can't be relayed should be cracked with Hashcat

### SSH Agent Hijacking
1. **Check for running SSH agents** — look for `SSH_AUTH_SOCK` environment variables in running processes on compromised Linux hosts
2. **Identify agent socket files** — find socket files in `/tmp` owned by other users; accessible if you have root or the right permissions
3. **Hijack the agent socket** — set `SSH_AUTH_SOCK` to point to another user's agent socket; authenticate as them to any host their key is trusted on
4. **Enumerate trusted hosts** — check `~/.ssh/known_hosts` and `~/.ssh/config` for hosts the user connects to
5. **Note: requires elevated access to hijack other users' agents** — typically needs root or same-user access to the socket file

### RDP Hijacking
1. **Requires SYSTEM access** — RDP session hijacking uses `tscon` to connect to another user's session without their password
2. **Enumerate disconnected sessions** — use `query session` or `qwinsta` to list all active and disconnected RDP sessions
3. **Hijack disconnected sessions** — use `tscon <session_id> /dest:<your_session>` to take over a disconnected session as SYSTEM
4. **High value when domain admins have disconnected sessions** — a disconnected DA session on any host is an immediate Domain Admin takeover
5. **Note for reporting** — disconnected sessions that can be hijacked without credentials is a significant security finding

### Pass-the-Hash (PTH)
1. **Collect NTLM hashes** — gather hashes from SAM, LSASS, NTDS.dit, or Responder captures
2. **Identify PTH-compatible services** — SMB, WMI, RDP (restricted admin mode), and WinRM all support NTLM authentication
3. **Test hash against all hosts** — spray the hash across all known hosts; local admin hash reuse is common
4. **Use hash for SMB access** — access shares and execute commands via SMB using the hash directly
5. **Use hash with WMI / WinRM** — execute commands remotely using captured hashes without cracking
6. **Check for restricted admin mode on RDP** — if enabled, PTH works against RDP; gives GUI access with just a hash
7. **Note: PTH does not work with NTLMv2 challenge/response** — PTH uses the NT hash directly; don't confuse with NetNTLMv2 relay

### Pass-the-Ticket (PTT)
1. **Collect Kerberos tickets** — dump TGTs and TGS tickets from LSASS memory using Mimikatz or Rubeus
2. **Inject TGT into current session** — use Mimikatz `kerberos::ptt` or Rubeus `ptt` to load a stolen TGT
3. **Request service tickets using injected TGT** — once a TGT is injected, request TGS tickets for any service the account has access to
4. **Use TGS for direct service access** — inject a specific service ticket to access a service as the ticket's owner
5. **Golden Ticket attack** — if KRBTGT hash is obtained, forge TGTs for any account with any privileges; unlimited domain access
6. **Silver Ticket attack** — forge a TGS for a specific service using the service account hash; more stealthy than Golden Ticket
7. **Overpass-the-Hash** — convert an NTLM hash into a Kerberos TGT; useful when Kerberos is required and PTH won't work

### Remote Service Exploitation
1. **PsExec** — authenticate via SMB and execute commands as SYSTEM; noisy but reliable; requires admin share access
2. **WMI execution** — run commands remotely via WMI; slightly less noisy than PsExec; requires admin credentials
3. **WinRM / Evil-WinRM** — clean interactive PowerShell session over WinRM; preferred method for interactive access
4. **DCOM execution** — use COM objects (MMC20, ShellWindows, etc.) for remote execution; more stealthy than PsExec
5. **SMB exec** — execute commands via SMB using tools like Impacket's smbexec; leaves fewer artifacts than PsExec
6. **RDP** — GUI-based lateral movement; use when you need interactive desktop access or when other methods fail
7. **SSH** — if SSH keys or credentials are found, use them to move to Linux hosts in the environment
8. **Choose method based on stealth requirements** — PsExec is noisiest; DCOM and WMI are quieter; match technique to engagement rules

### Token Impersonation
1. **Identify impersonatable tokens** — list available tokens on the compromised host; look for tokens belonging to higher-privileged users
2. **Check for SeImpersonatePrivilege** — if present, use Potato attacks (JuicyPotato, PrintSpoofer, GodPotato) to impersonate SYSTEM
3. **Check for SeAssignPrimaryTokenPrivilege** — similar to SeImpersonate; also allows privilege escalation to SYSTEM
4. **Impersonate logged-in domain users** — if a domain admin is logged into the host, their token may be available for impersonation
5. **Use Incognito / token manipulation tools** — list and impersonate available tokens to move laterally as other users
6. **Create processes under impersonated token** — spawn a shell or payload running as the impersonated user

### Pivoting & Tunneling
See the following command references for syntax and examples:
- [Chisel](commands.md#chisel)
- [SSH Tunnels](commands.md#ssh-tunnels)
- [Ligolo-ng](commands.md#ligolo-ng)
- [Proxychains](commands.md#proxychains)

1. **Identify pivot opportunities** — check network interfaces and routing tables on each compromised host for access to new subnets
2. **Port forwarding (local)** — forward a remote port to your local machine to access services on unreachable segments
3. **Port forwarding (remote/reverse)** — forward a local port through a compromised host to reach internal services
4. **SOCKS proxy** — set up a dynamic SOCKS proxy through a compromised host to route all tool traffic through it
5. **SSH tunneling** — use SSH's built-in forwarding capabilities for reliable, encrypted tunnels
6. **Chisel / ligolo-ng** — dedicated tunneling tools for complex multi-hop pivot scenarios; preferred for CPTS multi-subnet labs
7. **Metasploit routing and SOCKS** — use `route add` and the `auxiliary/server/socks_proxy` module to pivot through Meterpreter sessions without additional tools
8. **Double pivoting** — chain tunnels through multiple hosts to reach deeply segmented networks
9. **Update proxychains config** — ensure your tools route through the correct proxy for each network segment
10. **Keep a network map** — document each pivot point, the subnets accessible from it, and the tunnels in use; essential for complex environments

## 7. Privilege Escalation

### Linux Privilege Escalation

#### Sudo Abuse
1. **Check sudo rights** — `sudo -l`; look for commands that can be run as root with or without a password
2. **Check GTFOBins** — nearly every binary that can be run via sudo has a GTFOBins entry showing how to escape to a shell
3. **Look for NOPASSWD entries** — any command runnable as root without a password is an immediate privesc path
4. **Check for sudo version vulnerabilities** — Baron Samedit (CVE-2021-3156) and other sudo CVEs affect specific versions

#### SUID / SGID Binaries
1. **Find all SUID binaries** — search the filesystem for binaries with the SUID bit set
2. **Check against GTFOBins** — cross-reference every non-standard SUID binary with GTFOBins for exploitation techniques
3. **Look for custom SUID binaries** — non-standard binaries with SUID are almost always intentional misconfigs or CTF paths
4. **Check SGID binaries** — group-owned binaries with SGID can grant access to privileged groups

#### Cron Job Abuse
1. **Enumerate all cron jobs** — check `/etc/crontab`, `/etc/cron.d/`, `/var/spool/cron/`, and `cron.hourly/daily/weekly/monthly`
2. **Check for writable scripts** — if a cron job runs a script you can write to, replace or modify it for code execution as the cron user
3. **Check for writable paths** — if the script path or a directory in the PATH used by cron is writable, plant a malicious binary
4. **Check for wildcard injection** — cron jobs using wildcards with tools like tar, chown, or chmod can be exploited via filename manipulation
5. **Check timing** — note how frequently jobs run; use `pspy` to monitor process execution without root to catch jobs not in crontab

#### Writable Files & Path Abuse
1. **Find world-writable files and directories** — look for writable files owned by root or other privileged users
2. **Check PATH hijacking opportunities** — if a script or SUID binary calls commands without full paths, plant a malicious binary earlier in PATH
3. **Check for writable service configs** — writable systemd unit files or init scripts that run as root
4. **Check `/etc/passwd` writability** — if writable, add a root user directly

#### Shared Library Hijacking
1. **Find binaries with missing shared libraries** — use `strace` or `ltrace` on privileged binaries to find library calls that fail to load
2. **Check LD_LIBRARY_PATH** — if set in a root-executed script or service, a writable directory in the path allows planting a malicious `.so`
3. **Check for writable library directories** — if a directory in the binary's library search path is writable, plant a malicious shared library
4. **Craft a malicious `.so` file** — compile a shared library that executes a payload when loaded; export the expected function to avoid crashes
5. **Check `/etc/ld.so.conf`** — writable config files that define library search paths can be modified to include attacker-controlled directories

#### Logrotate Abuse
1. **Check logrotate configuration** — look for logrotate configs that reference log files you can write to
2. **Check for writable log files rotated as root** — if logrotate runs as root and rotates a file you own or can write to, exploit the race condition
3. **Use logrotten exploit** — automates the race condition between logrotate creating a new file and your payload being in place

#### Credential Reuse (Local)
1. **Try found passwords with `su`** — always attempt found credentials with `su` to switch to root or other users before trying technical privesc
2. **Check `/etc/passwd` and shadow for password reuse** — if you can crack any hashes, try them for root and other accounts
3. **Test credentials found in files against all local users** — credentials found in configs, history, or scripts often reuse across accounts

#### Linux Capabilities
1. **Enumerate capabilities** — use `getcap -r /` to find binaries with elevated capabilities
2. **Check GTFOBins for capability abuse** — `cap_setuid`, `cap_net_raw`, `cap_dac_override` are commonly abusable
3. **Python/Perl/Ruby with cap_setuid** — immediately escalates to root if the interpreter has this capability

#### NFS no_root_squash
1. **Check `/etc/exports`** — look for shares with `no_root_squash` enabled
2. **Mount the share from your attack box as root** — create a SUID binary on the share; execute it on the target for root

#### Docker / LXC Escape
1. **Check group membership** — being in the `docker` group is equivalent to root; use `docker run` to mount the host filesystem
2. **Check for container escape** — if running inside a container, look for mounted docker sockets, privileged flags, or host path mounts
3. **LXC group abuse** — similar to docker group; can mount host disk and read/write the entire filesystem

#### Kernel Exploits
1. **Note the kernel version** — `uname -a`; research the version for local privilege escalation CVEs
2. **Check for DirtyCow, DirtyPipe, and other kernel CVEs** — match kernel version to known exploits
3. **Use as a last resort** — kernel exploits can crash the system; try all other vectors first
4. **Compile carefully** — ensure the exploit is compiled for the correct architecture and kernel version

#### PwnKit / Polkit (CVE-2021-4034)
See the following command references for syntax and examples:
- [Linux Privilege Escalation commands](commands.md#linux-post-exploitation)

1. **Check if pkexec is present** — `which pkexec`; present on virtually all Linux distributions with Polkit installed
2. **Check Polkit version** — versions prior to 0.120 (most systems before early 2022 patches) are vulnerable
3. **Exploit CVE-2021-4034** — a local privilege escalation in `pkexec` that gives immediate root regardless of sudo rights or SUID bits
4. **Use as an early check** — PwnKit is reliable and fast; worth checking before spending time on manual privesc enumeration
5. **Note: widely patched** — more recent lab environments may be patched; confirm version before attempting

### Windows Privilege Escalation

#### Token Impersonation & Potato Attacks
1. **Check SeImpersonatePrivilege** — most common privesc on Windows; present on service accounts by default
2. **Use PrintSpoofer** — works on Windows 10 and Server 2019+; most reliable modern Potato attack
3. **Use GodPotato** — works across a wide range of Windows versions; good fallback
4. **Use JuicyPotato** — older technique; works on Windows Server 2016 and earlier; requires a valid CLSID
5. **Check SeAssignPrimaryTokenPrivilege** — similar impact to SeImpersonate; use same Potato techniques

#### Weak Service Permissions
1. **Enumerate service permissions** — check if you can modify the binary path or configuration of any service running as SYSTEM
2. **Replace service binary** — if the service binary is in a writable location, replace it with a malicious one
3. **Modify service config** — if you have SERVICE_CHANGE_CONFIG rights, change the binary path to execute your payload
4. **Restart the service** — trigger execution by restarting the service or waiting for system reboot

#### Unquoted Service Paths
1. **Find unquoted service paths with spaces** — a service path like `C:\Program Files\My App\service.exe` without quotes is vulnerable
2. **Identify writable directories in the path** — if you can write to `C:\Program Files\My.exe`, it runs before the real binary
3. **Plant a malicious binary** — place your payload at the exploitable path; it runs as SYSTEM when the service starts

#### DLL Hijacking
1. **Identify services / applications with missing DLLs** — use Process Monitor to find DLL not found errors
2. **Check DLL search order** — Windows searches predictable locations; a writable directory early in the path is exploitable
3. **Plant a malicious DLL** — write your payload DLL to the exploitable path; it loads when the application starts
4. **Check for writable DLL locations** — even if the DLL exists, a writable directory earlier in the search order is exploitable

#### AlwaysInstallElevated
1. **Check registry keys** — query `HKLM` and `HKCU` for `AlwaysInstallElevated` set to 1 in both hives
2. **Create a malicious MSI** — if both keys are set to 1, any MSI package installs with SYSTEM privileges
3. **Execute the MSI** — run the malicious installer to get a SYSTEM shell

#### Scheduled Task Abuse
1. **Enumerate scheduled tasks** — look for tasks running as SYSTEM or Administrator with writable script/binary paths
2. **Replace the task binary or script** — if the executable or script path is writable, replace it with your payload
3. **Check task triggers** — note when the task runs; trigger it manually if possible or wait for the scheduled time

#### Stored Credentials & Registry
1. **Check Windows Credential Manager** — stored credentials for network resources may include domain admin accounts
2. **Search registry for credentials** — query common registry paths for stored passwords (Autologon, VNC, PuTTY)
3. **Check PowerShell history** — `ConsoleHost_history.txt` frequently contains previously used credentials
4. **Search for unattended install files** — `unattend.xml`, `sysprep.xml`, and similar files often contain base64-encoded passwords
5. **Check web.config and application configs** — IIS and application config files often contain database credentials

#### SeBackupPrivilege Abuse
1. **Check for SeBackupPrivilege** — grants the ability to read any file on the system regardless of ACLs; often assigned to backup service accounts
2. **Copy SAM and SYSTEM hives** — use the privilege to copy `C:\Windows\System32\config\SAM` and `SYSTEM` to extract local NTLM hashes
3. **Copy NTDS.dit from a DC** — on a Domain Controller, use SeBackupPrivilege to copy the AD database for full domain hash extraction
4. **Use robocopy or built-in backup tools** — `robocopy /B` and `wbadmin` respect SeBackupPrivilege and can copy protected files
5. **Extract and crack or PTH** — dump hashes from copied hives offline; use for Pass-the-Hash or crack for plaintext passwords

#### SeDebugPrivilege Abuse
1. **Check for SeDebugPrivilege** — grants the ability to open any process with full access, including SYSTEM processes; rare but extremely powerful
2. **Dump LSASS directly** — use SeDebugPrivilege to open and read LSASS memory without triggering standard AV alerts on admin tool usage
3. **Inject into privileged processes** — inject a payload into a SYSTEM process to execute as SYSTEM
4. **Migrate Meterpreter session** — if in Meterpreter, use `migrate` to move into a SYSTEM process using this privilege

#### PrintNightmare (Spooler Privesc)
1. **Check if Print Spooler service is running** — `sc query spooler`; if running, the host may be vulnerable
2. **Test for CVE-2021-1675 / CVE-2021-34527** — local privilege escalation variant allows low-privileged users to load a malicious DLL as SYSTEM
3. **Use the local privesc variant** — distinct from the remote code execution variant; abuses the spooler's DLL loading to escalate locally
4. **Drop a malicious DLL** — the DLL is loaded by the Spooler service running as SYSTEM; executes your payload with SYSTEM privileges

#### SeTakeOwnershipPrivilege / SeRestorePrivilege
1. **Check for SeTakeOwnershipPrivilege** — grants ability to take ownership of any file, registry key, or object regardless of ACLs
2. **Take ownership of sensitive files** — take ownership of SAM, SYSTEM, or other protected files and read them for credential extraction
3. **Take ownership of privileged executables** — take ownership of a SYSTEM-run binary, replace it with a payload, and trigger execution
4. **Check for SeRestorePrivilege** — grants write access to any file regardless of ACLs; functionally similar impact to SeTakeOwnershipPrivilege
5. **Modify registry with SeRestorePrivilege** — use the privilege to write to protected registry keys for persistence or privesc

#### UAC Bypass
1. **Check UAC level** — determine the UAC configuration; some levels are bypassable without user interaction
2. **Use known UAC bypass techniques** — fodhelper, eventvwr, and other auto-elevating binaries can bypass UAC
3. **Note: UAC bypass gives high integrity, not SYSTEM** — you still need another technique to reach SYSTEM after UAC bypass

#### Windows Kernel Exploits
1. **Note the OS and patch level** — `systeminfo`; check for missing patches that correspond to local privesc CVEs
2. **Check for PrintNightmare** — if Print Spooler is running, test for CVE-2021-1675 / CVE-2021-34527
3. **Check for HiveNightmare / SeriousSAM** — allows reading SAM/SYSTEM as a low-privileged user on unpatched Windows 10/11
4. **Use as a last resort** — kernel exploits can cause BSODs; exhaust all other options first

## 8. Active Directory Attacks

### Kerberoasting
See the following command references for syntax and examples:
- [Impacket Kerberos commands](commands.md#---kerberos--)
- [BloodHound Cypher queries](commands.md#key-cypher-queries-run-in-bloodhound-query-box)

1. **Identify accounts with SPNs** — any domain user account with a Service Principal Name set is a Kerberoasting target
2. **Request TGS tickets for SPN accounts** — any authenticated domain user can request these; no special privileges needed
3. **Extract tickets for offline cracking** — export the TGS tickets in crackable format
4. **Crack tickets offline with Hashcat** — use wordlists and rules; service accounts often have weak or old passwords
5. **Test cracked credentials everywhere** — service accounts often have elevated privileges and their passwords reuse elsewhere
6. **Prioritize high-value SPN accounts** — focus on accounts that are members of privileged groups first

### AS-REP Roasting
See the following command references for syntax and examples:
- [GetNPUsers command examples](commands.md#---kerberos--)

1. **Identify accounts with pre-authentication disabled** — enumerate the `DONT_REQ_PREAUTH` UAC flag on user accounts
2. **Request AS-REP hashes without authentication** — no credentials needed; the KDC returns an encrypted blob that can be cracked
3. **Crack hashes offline** — use Hashcat with wordlists and rules
4. **Test cracked credentials** — immediately test against all services and check group memberships

### ACL / ACE Abuse
1. **Enumerate dangerous ACEs** — look for GenericAll, GenericWrite, WriteOwner, WriteDACL, ForceChangePassword, and AllExtendedRights on user/group/computer objects
2. **GenericAll on a user** — change their password or perform targeted Kerberoasting without needing their current password
3. **GenericAll on a group** — add yourself or a controlled account to the group (e.g., Domain Admins)
4. **GenericAll on a computer** — perform Resource-Based Constrained Delegation (RBCD) attack for SYSTEM on that host
5. **WriteDACL** — grant yourself GenericAll on the object, then proceed with full control
6. **WriteOwner** — take ownership of the object, then grant yourself additional rights
7. **ForceChangePassword** — reset the target user's password without knowing the current one
8. **GenericWrite on a user** — set an SPN for targeted Kerberoasting or modify logon scripts
9. **Chain ACL abuse** — map the full path; a series of weak ACEs can lead from a low-privilege user to Domain Admin

### Delegation Attacks
1. **Unconstrained Delegation** — any host with unconstrained delegation stores TGTs of users who authenticate to it; compromise the host and extract TGTs from LSASS
2. **Printer Bug / SpoolSample** — force a DC to authenticate to a host with unconstrained delegation; capture the DC's TGT for DCSync
3. **Constrained Delegation** — if an account has constrained delegation, use S4U2Self/S4U2Proxy to impersonate any user to the allowed service
4. **Resource-Based Constrained Delegation (RBCD)** — if you have WriteProperty/GenericWrite over a computer object, configure RBCD to impersonate any user to that host
5. **Identify delegation settings** — enumerate `TrustedForDelegation` and `msDS-AllowedToDelegateTo` attributes during AD enumeration

### NTLM Relay Attacks
1. **Set up Responder in analyze mode first** — identify what's on the network before poisoning anything
2. **Poison LLMNR / NBT-NS / mDNS** — use Responder to capture NTLMv2 hashes from hosts making name resolution requests
3. **Relay instead of capturing** — when SMB signing is disabled, relay captured authentication directly to other hosts for access
4. **Check SMB signing status** — enumerate which hosts have SMB signing disabled; these are relay targets
5. **NTLM relay to LDAP** — relay to LDAP for account creation, ACL modification, or RBCD setup
6. **NTLM relay to MSSQL** — relay authentication to SQL Server for command execution
7. **Use mitm6 for IPv6 poisoning** — supplement Responder with mitm6 to capture authentications via IPv6 DNS poisoning

### DCSync Attack
1. **Confirm required privileges** — DCSync requires Domain Admin, Enterprise Admin, or an account with Replicating Directory Changes / Replicating Directory Changes All rights
2. **Execute DCSync** — impersonate a DC and request password data for any account including KRBTGT and all domain users
3. **Extract KRBTGT hash** — the KRBTGT hash enables Golden Ticket attacks; highest-value credential in the domain
4. **Extract all domain hashes** — dump the entire domain's NTLM hashes for offline cracking and PTH attacks
5. **Check for non-admin DCSync rights** — ACL misconfigurations sometimes grant DCSync rights to non-admin accounts; always check

### Domain Trust Attacks
1. **Enumerate all trusts** — identify parent/child domain trusts, forest trusts, and external trusts with their directions and transitivity
2. **Child-to-parent domain escalation** — compromise a child domain and use the SID history or KRBTGT hash to escalate to the parent/root domain
3. **SID history injection** — add the Enterprise Admins SID to a forged ticket's SID history to gain Enterprise Admin rights across the forest
4. **ExtraSids attack** — when child domain KRBTGT hash is known, forge an inter-realm TGT with the Enterprise Admins SID in ExtraSids
5. **Forest trust abuse** — if a bidirectional forest trust exists, enumerate the trusted forest for attack paths and escalation opportunities
6. **Foreign group membership** — enumerate users from one domain with group membership in another; may reveal cross-domain privilege paths

### Golden & Silver Ticket Attacks
1. **Golden Ticket prerequisites** — requires the KRBTGT account NTLM hash, domain SID, and any username (even non-existent)
2. **Forge a Golden Ticket** — create a TGT valid for any account with any group memberships; provides persistent domain access
3. **Golden Ticket persistence** — KRBTGT password must be reset twice to invalidate Golden Tickets; often survives remediation attempts
4. **Silver Ticket prerequisites** — requires the service account NTLM hash and the SPN of the target service
5. **Forge a Silver Ticket** — create a TGS for a specific service without touching the DC; more stealthy than Golden Ticket
6. **Common Silver Ticket targets** — CIFS for file access, HOST for command execution, HTTP for web services, MSSQL for database access

### Password Spraying & Domain Account Attacks
1. **Enumerate the password policy first** — always check lockout threshold before spraying anything
2. **Spray with Kerbrute** — use Kerberos pre-authentication for spraying; faster and generates fewer logs than LDAP spraying
3. **Target high-value accounts** — prioritize spraying against service accounts and accounts in privileged groups
4. **Use seasonal / common passwords** — `Season+Year`, `Company+Year`, and `Welcome1` patterns are consistently effective
5. **Time sprays around the lockout observation window** — wait for the counter to reset between spray rounds

### Privileged Group Abuse
1. **Account Operators** — can create and modify most domain accounts and add them to non-protected groups; use to create a new account and add to a privileged group
2. **Backup Operators** — can log on locally to DCs and back up/restore files; use SeBackupPrivilege to copy NTDS.dit from a DC
3. **DNS Admins** — can load a DLL as SYSTEM on the DNS server (usually the DC); plant a malicious DLL via `dnscmd` for SYSTEM execution
4. **Server Operators** — can modify and start/stop services on DCs; change a DC service binary path to execute a payload as SYSTEM
5. **Print Operators** — can load printer drivers (DLLs) on DCs; abuse to load a malicious driver for SYSTEM execution
6. **DnsAdmins to DA** — the DNS Admins DLL injection path is one of the most reliable group-to-DA escalations; always check DNS Admins membership
7. **Event Log Readers** — can read security event logs; useful for intelligence gathering rather than direct escalation
8. **Remote Management Users / Remote Desktop Users** — grants WinRM or RDP access to specific hosts; useful for lateral movement

### LAPS (Local Administrator Password Solution) Attacks
1. **Confirm LAPS is deployed** — check for the `ms-Mcs-AdmPwd` attribute on computer objects; if present, LAPS is in use
2. **Enumerate who can read LAPS passwords** — identify which users, groups, or OUs have read access to the `ms-Mcs-AdmPwd` attribute
3. **Read LAPS passwords if permitted** — if your account has read access, retrieve the local admin password for target computers directly from AD
4. **Use LAPS passwords for lateral movement** — the local admin password retrieved is valid for that specific host; use for PTH or direct authentication
5. **Check for LAPS misconfiguration** — overly broad read permissions (e.g., Domain Users can read LAPS passwords) is a critical finding

### GPO Abuse
1. **Enumerate GPO permissions** — identify GPOs where your account or a controlled group has write access (`CreateChild`, `WriteProperty`, `GenericWrite`, `GenericAll`)
2. **Identify linked OUs** — check which OUs the vulnerable GPO is linked to; computers and users in those OUs will apply your malicious policy
3. **Add a malicious scheduled task via GPO** — create a scheduled task in the GPO that executes a payload as SYSTEM on all computers in the linked OU
4. **Add a local admin account via GPO** — use Restricted Groups or Local Users and Groups policy to add a controlled account to the local Administrators group
5. **Force GPO update** — use `gpupdate /force` or wait for the standard 90-minute refresh cycle; domain computers will pull and apply the modified policy
6. **Target GPOs linked to high-value OUs** — a GPO linked to the Domain Controllers OU gives code execution as SYSTEM on every DC

### ADCS Attacks
1. **ESC1 — Misconfigured Certificate Templates** — if a template allows the enrollee to specify a SAN and enables client authentication, request a certificate as any user including Domain Admin; use with Certipy or Certify
2. **ESC2 — Any Purpose / No EKU Templates** — templates with Any Purpose EKU or no EKU can be used for authentication; request and use for domain escalation
3. **ESC3 — Enrollment Agent Abuse** — obtain a Certificate Request Agent cert, then use it to enroll on behalf of any user including Domain Admin
4. **ESC4 — Vulnerable Template ACLs** — if you have write access to a template, modify it to introduce ESC1 conditions, then exploit as ESC1
5. **ESC5 — Vulnerable PKI Object ACLs** — if you have write access to the CA computer object, `CN=Public Key Services` container, or any certificate template object in AD, modify them to introduce exploitable conditions; escalation path is equivalent to ESC4 once write access is established
6. **ESC6 — EDITF_ATTRIBUTESUBJECTALTNAME2** — if this flag is set on the CA, any template with client authentication enabled allows SAN specification; request cert as Domain Admin
7. **ESC7 — Vulnerable CA ACLs** — if you have Manage CA rights, grant yourself the Issue and Manage Certificates right, then approve pending requests for any user
8. **ESC8 — NTLM Relay to ADCS HTTP** — relay NTLM authentication to the ADCS web enrollment endpoint to obtain a certificate on behalf of the relayed user
9. **Use certificate for authentication** — convert obtained certificate to a TGT using PKINIT (Rubeus `asktgt` or Certipy `auth`); gives full Kerberos access as the target user
10. **Retrieve NTLM hash from certificate** — use the PKINIT TGT to retrieve the target account's NTLM hash via U2U Kerberos for Pass-the-Hash

### Shadow Credentials (msDS-KeyCredentialLink)
1. **Prerequisites** — requires GenericWrite or WriteProperty over a user or computer object's `msDS-KeyCredentialLink` attribute
2. **Add a key credential to the target object** — use Whisker or Certipy to add a controlled key credential to the target's `msDS-KeyCredentialLink` attribute
3. **Request a TGT using PKINIT** — authenticate using the key credential to obtain a TGT for the target account without knowing their password
4. **Retrieve the target's NTLM hash** — use the TGT via U2U Kerberos to obtain the account's NTLM hash for Pass-the-Hash
5. **Works against both user and computer accounts** — compromising a computer account's key credential enables LSASS dumping and full host control
6. **Clean up after exploitation** — remove the added key credential from `msDS-KeyCredentialLink` after use to avoid detection

### AdminSDHolder / SDProp Abuse
1. **Understand AdminSDHolder** — a special AD object whose ACL is automatically propagated to all members of protected groups every 60 minutes by the SDProp process
2. **Identify the attack** — if you have WriteDACL or GenericAll on the AdminSDHolder object, add a controlled account's ACE; SDProp will propagate this to all protected group members
3. **Add a malicious ACE to AdminSDHolder** — grant your controlled account GenericAll or DCSync rights on the AdminSDHolder object
4. **Wait for SDProp to run** — within ~60 minutes the ACE propagates to Domain Admins, Enterprise Admins, and all other protected groups
5. **Exploit propagated rights** — use the propagated GenericAll to reset DA passwords, perform DCSync, or add accounts to protected groups
6. **High persistence value** — the ACE re-propagates every 60 minutes; survives removal from the protected group members until AdminSDHolder itself is cleaned

### BloodHound Attack Path Analysis
1. **Collect data with SharpHound or BloodHound.py** — run the collector from a domain-joined host or with valid credentials; collect All data if possible
2. **Import data into BloodHound** — load the collected JSON files into the BloodHound GUI for analysis
3. **Mark owned principals** — right-click and mark every user, computer, and group you have control over as Owned; enables path finding from your current position
4. **Find shortest path to Domain Admin** — use the built-in query to find the shortest attack path from your owned principals to Domain Admin
5. **Use pre-built queries** — run built-in queries for Kerberoastable users, AS-REP Roastable users, unconstrained delegation, and other attack vectors
6. **Analyze outbound control** — for each owned principal, check what objects they have rights over; reveals ACL abuse paths
7. **Look for path through unexpected groups** — BloodHound often reveals non-obvious paths through nested group memberships and cross-object permissions
8. **Identify high-value targets** — use BloodHound to find all paths to DA, EA, and other Tier 0 assets; prioritize the shortest and most reliable path

### Coercion Attacks (PetitPotam / DFSCoerce / PrinterBug)
1. **What coercion is** — forcing a machine account to authenticate to an attacker-controlled host via various MS-RPC protocols; the resulting Net-NTLMv2 hash or Kerberos ticket can then be relayed or cracked
2. **PrinterBug (MS-RPRN)** — use `printerbug.py` or Rubeus to trigger spooler service authentication: `python printerbug.py domain/user:pass@DC attacker-IP`; requires Print Spooler service running on target
3. **PetitPotam (MS-EFSRPC)** — use `PetitPotam.py` to coerce LSASS authentication via EFS RPC: `python PetitPotam.py attacker-IP DC-IP`; works unauthenticated on older systems, requires auth on patched systems
4. **DFSCoerce (MS-DFSNM)** — use `dfscoerce.py` to trigger authentication via the Distributed File System Namespace protocol; useful when Print Spooler and EFS are patched/disabled
5. **Relay coerced auth to LDAP for RBCD** — start `ntlmrelayx.py --delegate-access` before triggering coercion; the relayed authentication creates a computer account with delegation rights over the target
6. **Relay coerced auth to ADCS (ESC8)** — relay the coerced DC authentication to the AD CS HTTP enrollment endpoint to obtain a certificate for the DC account; use the certificate for DCSync via PKINIT
7. **Coerce then crack** — if relay is not possible, capture the Net-NTLMv2 hash with Responder and attempt offline cracking with hashcat
8. **Check for mitigations** — EPA (Extended Protection for Authentication) on LDAP/LDAPS and disabling Print Spooler on DCs are the primary mitigations; test for their presence before attempting coercion

### MachineAccountQuota (MAQ) Abuse
1. **Check MachineAccountQuota** — query the `ms-DS-MachineAccountQuota` attribute: `Get-ADObject -Identity ((Get-ADDomain).distinguishedname) -Properties ms-DS-MachineAccountQuota`; default is 10
2. **Create a computer account** — if MAQ > 0, any domain user can add computer accounts: `addcomputer.py -computer-name 'ATTACKER$' -computer-pass 'Password123!' domain/user:pass`
3. **Use the computer account for RBCD** — once a computer account is created, configure Resource-Based Constrained Delegation from a target machine to the attacker computer account (requires WriteMSDS-AllowedToActOnBehalfOfOtherIdentity on the target)
4. **Impersonate any user via S4U2Proxy** — use the RBCD setup to request a service ticket on behalf of a privileged user (e.g., Administrator): `getST.py -spn cifs/target.domain.com -impersonate Administrator -dc-ip DC domain/ATTACKER$:Password123!`
5. **Use ticket for access** — import the obtained TGS into the session and access the target service as the impersonated administrator
6. **Check if MAQ is 0** — if MachineAccountQuota is 0, this attack path requires an existing computer account you control or the ability to create accounts via other means (e.g., ADCS, ACL abuse)

## 9. Reporting

### Activity Log & Evidence Collection
1. **Maintain a running activity log** — record every significant action with timestamps: commands run, hosts accessed, credentials found, vulnerabilities confirmed
2. **Screenshot everything** — capture screenshots of every finding at the moment of discovery; include the URL/IP, proof of exploitation, and impact demonstration
3. **Save raw tool output** — keep nmap scans, BloodHound data, sqlmap output, and other raw tool results; they support findings and may be requested by the client
4. **Record exact commands** — note the exact syntax used to exploit each vulnerability; the report's reproduction steps must be accurate enough for the client to verify
5. **Document lateral movement chain** — record every hop: how access was obtained, what credentials were used, and what system was reached at each step
6. **Capture flag proof** — for CPTS and CTF-style engagements, screenshot each flag in context (showing the hostname and the flag value together)

### Report Structure
1. **Cover page** — engagement title, client name, tester name/company, report date, classification (Confidential)
2. **Table of contents** — link to all major sections for navigation
3. **Executive Summary** — non-technical overview written for management; key findings, overall risk posture, and top recommendations in plain language (1-2 pages)
4. **Scope & Methodology** — define what was tested, what was excluded, the testing approach (black/grey/white box), and the testing timeline
5. **Attack Chain Narrative** — a walkthrough of the full attack path from initial access to highest impact; tells the story of the engagement in a linear, readable format
6. **Technical Findings** — detailed write-up of each vulnerability; see Finding Structure below
7. **Remediation Summary** — consolidated table of all findings with risk rating, affected system, and recommended fix; useful for tracking remediation
8. **Appendices** — raw tool output, additional screenshots, credential lists (hashed/redacted), and supporting evidence

### Finding Structure (per vulnerability)
Each individual finding should contain:
1. **Finding title** — clear, descriptive name (e.g., "SQL Injection in Login Form — Authentication Bypass")
2. **Risk rating** — Critical / High / Medium / Low / Informational with justification
3. **Affected system(s)** — IP address, hostname, URL, or component
4. **Description** — what the vulnerability is and why it exists
5. **Evidence** — screenshots, request/response captures, tool output proving the vulnerability
6. **Reproduction steps** — numbered, step-by-step instructions to reproduce the finding from scratch
7. **Impact** — what an attacker can do if this is exploited; be specific (data accessed, systems compromised, business impact)
8. **Remediation recommendation** — specific, actionable guidance; reference CVEs, vendor advisories, or CIS benchmarks where applicable
9. **References** — CVE numbers, OWASP links, vendor advisories, CWE identifiers

### Risk Rating Guidelines
- **Critical** — direct path to full system/domain compromise, unauthenticated RCE, plaintext credentials for privileged accounts, Active Directory domain compromise
- **High** — authenticated RCE, SQLi with data exfiltration, privilege escalation to root/SYSTEM, significant sensitive data exposure
- **Medium** — stored XSS, IDOR exposing sensitive data, insecure direct object reference, missing authentication on sensitive functionality
- **Low** — reflected XSS, information disclosure, weak TLS configuration, missing security headers with limited exploitability
- **Informational** — best practice deviations, missing headers with no direct impact, verbose error messages without sensitive data

### Executive Summary Guidelines
1. **Write for a non-technical audience** — avoid jargon; a CFO or CEO should be able to understand the key message
2. **Lead with overall risk posture** — one clear statement about the security posture observed (e.g., "critical vulnerabilities were identified that would allow an attacker to fully compromise the network")
3. **Summarize key findings by count and severity** — "X critical, Y high, Z medium findings were identified"
4. **Highlight the most impactful finding** — describe the worst-case scenario in business terms (data breach, operational disruption, regulatory exposure)
5. **End with top 3-5 remediation priorities** — what the client should fix first; frame in terms of risk reduction
6. **Avoid blame** — keep the tone constructive; the goal is to help the client improve

### Remediation Recommendations
1. **Be specific** — "disable SMBv1" is better than "harden SMB"; "apply KB5004945" is better than "patch Windows"
2. **Prioritize by risk** — lead with Critical and High findings; clients have limited resources and need to know what to fix first
3. **Include quick wins** — some fixes (disabling a service, changing a password, applying a patch) can be done immediately; highlight these
4. **Reference vendor guidance** — link to official vendor advisories, Microsoft security baselines, CIS Benchmarks, and OWASP remediation guides
5. **Avoid prescribing architecture** — recommend what to fix, not a full redesign; scope creep in recommendations reduces report usability
6. **Offer retesting** — note that remediation can be verified through retesting; builds client confidence and relationship

### Post-Engagement Cleanup
1. **Remove all tools and payloads** — delete uploaded webshells, binaries, scripts, and any files transferred to target systems
2. **Remove all persistence mechanisms** — disable and delete any backdoors, cron jobs, scheduled tasks, registry keys, or SSH keys added during testing
3. **Restore modified configurations** — revert any configuration changes made during testing (enabled services, modified ACLs, changed passwords)
4. **Document what was cleaned** — include a cleanup confirmation section in the report; note every artifact removed and from which system
5. **Revoke temporary access** — remove any accounts created during testing; confirm with the client that all temporary access has been revoked
6. **Secure report delivery** — deliver the report via encrypted channel (encrypted PDF, secure portal, PGP email); do not send findings over unencrypted email
7. **Retain engagement data securely** — store notes, evidence, and tool output per your data retention policy; destroy sensitive client data after the agreed retention period

