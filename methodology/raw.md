Working Artifacts during the penetration test
- Target List: IP/hostnames, OS guess, network role guess, discovered open ports, current status (not started, in progress, foothold, and owned), priority, and notes.
- Service Inventory (per host): Port, protocol, service name, version, auth required, anonymous/guest access possible (yes/no/unknown), enumeration status (not started, in progress, and complete), exploitation status, and notes/log references.
- Credentials and Tokens: Credential type (plaintext / hash / token / key), value,  where found, service/host it is valid on, privilege level (user / admin / domain admin / unknown), tested against (list of services tried), and cracked (yes/no/attempted).
- Hypothesis List: "I think X because Y; next test is Z; outcome was W".
- Rabbit Hole Log: What I have tried, why it failed, and a stop reason.
- Timeline/Command Log: Timestamp, host, command run, and one-line result summary.


Anti-Rabbit-Hole System
When you feel stuck, use this checklist:
What is my best current hypothesis?
What evidence supports it?
What evidence contradicts it?
What is the fastest test that changes my decision?
Have I updated my artifacts (especially failed paths and creds)?

Reassess Triggers
30 minutes with no new evidence → go broader (Phases 1a and 1b)
2 failed hypotheses → re-triage services
You are collecting output “just because” → stop and define a question first


Phases:
- Phase 0: Scope Review
- Phase 1a: Passive Reconnaissance
- Phase 1b: Active Reconnaissance
- Phase 2: Service Enumeration


Phase 0 - Scope Review
Goal
Know what "win" means and what constraints exist.

Questions
- What is the objective? (foothold, user flag, root flag, multiple flags, etc.)
- Is this single host or network environment?
- Any rules/constraints? (scan limits, forbidden actions, time limit, pivot allowed)
- What is the starting point? (an IP address, any provided credentials, any provided footholds)
- What is the target IP range / subnet? (helps to confirm the scope boundaries)
- Are there any known credentials or entry points provided? (was a starting user provided?)
- What does "complete" look like? (what proof is required? flags, screenshots, hashes, etc.)

Outputs
- A one-line mission statement. (e.g.: Gain root on a single host)
- Confirmed target IP range / host list (even if just one IP address)
- Confirmed constraints (what you cannot do)
- Confirmed proof requirements (what you need to capture)
- Starting point noted (your attack IP address, any given credentials)

Phase 0 is complete when:
[ ] Objective is clearly stated.
[ ] Target scope (IP addresses / ranges) is confirmed and written down.
[ ] Constraints are documented.
[ ] Proof / flag requirements are known.
[ ] Starting point and any provided assets are noted.


Phase 1 - Reconnaissance / Information Gathering
Goal
Build a complete picture of the attack surface without necessarily touching the target directly.

Phase 1a - Passive Reconnaissance
Goal
Gather information without directly touching the target.

Questions
- What information can be found with a WHOIS lookup of the target?
  - > whois target.htb | tee recon/passive/whois.txt
  - > grep -iE "registrant|admin|tech|name server|email|creation|expir" recon/passive/whois.txt
  - Registrant email and organization
  - Registrant email address (credentials / users artifact)
  - Registration and expiration dates (older domains have more exposed history)
  - Registrar name (credentials / users artifact)
  - Nameservers (needed for DNS enumeration)
  - Admin and tech contact information (credentials / users artifact)
- What information can be found with DNS enumeration?
  - Record types include A, AAAA, MX, NS, TXT, CNAME, SOA, PTR, SRV, ANY
  - Dig examples include:
    - > dig A target.htb | tee recon/passive/dig_a.txt
    - > dig NS target.htb | tee recon/passive/dig_ns.txt
    - > dig TXT target.htb | tee recon/passive/dig_txt.txt
    - > dig ANY target.htb | tee recon/passive/dig_any.txt
    - > dig @nameserver.target.htb target.htb ANY | tee recon/passive/dig_any_nameserver.txt
  - Nslookup examples include:
    - > nslookup target.htb | tee recon/passive/nslookup.txt
    - > nslookup -type=A target.htb | tee recon/passive/nslookup_a.txt
    - > nslookup -type=AAAA target.htb | tee recon/passive/nslookup_aaaa.txt
    - > nslookup -type=CNAME target.htb | tee recon/passive/nslookup_cname.txt
    - > nslookup target.htb nameserver.target.htb | tee recon/passive/nslookup_nameserver.txt
- Did a reverse DSN lookup with any discovered IP addresses yield any other results?
  - > dig -x 10.10.10.10 | tee recon/passive/dig_x_10_10_10_10.txt
  - > nslookup 10.10.10.10 | tee recon/passive/nslookup_reverse_lookup.txt
- Was a zone transfer attempted against all nameservers found?
  - > dig axfr @nameserver.target.htb target.htb | tee recon/passive/zone_transfer_nameserver.txt
  - Failures have text like "; Transfer failed"
  - Successes will show internal subdomains
- Were any subdomains discovered?
- What IP ranges does this organization own?
- Did Google dorking find any of the following:
  [ ] Usernames or email addresses?
  [ ] Login or admin panels (inurl:admin, inurl:login)
  [ ] Exposed files (filetype:pdf, filetype:xlsx, filetype:env)
  [ ] Error messages revealing software or paths
  [ ] Cached or indexed pages revealing internal content
  1. Start broad — map what is indexed
    > site:targetdomain.com
  2. Find subdomains
    > site:*.targetdomain.com
  3. Find login and admin surfaces
    > inurl:admin OR inurl:login OR inurl:portal site:targetdomain.com
  4. Hunt for exposed files and directories
    > intitle:"index of" site:targetdomain.com
    > filetype:bak OR filetype:sql OR filetype:log site:targetdomain.com
  5. Hunt for credentials and sensitive data
    > filetype:env OR filetype:config OR filetype:yml site:targetdomain.com
  6. Look for technology fingerprints
    > intext:"powered by" site:targetdomain.com
    > intext:"Fatal error" site:targetdomain.com
  7. Find exposed sensitive documents
    > filetype:pdf OR filetype:xlsx OR filetype:docx site:targetdomain.com
  8. Check for misconfigurations
    > inurl:.git OR inurl:phpinfo OR inurl:.env site:targetdomain.com
- Are there any publicly exposed documents (PDF, DOCX, XLSX) that contain metadata revealing usernames, software versions, or internal paths? (Google dork: filetype:pdf site:target.com)
- Were any team members found on LinkedIn? Does the technical team specify what technologies and certifications they have?
- Are there any job postings for this company? Do they mention technologies used?
- Is there an old version of the site on the Wayback Machine?
- Were you able to harvest any emails using Hunter.io or theHarvester?
- Does Shodan or Censys reveal:
  [ ] Open ports or services not found through other means?
  [ ] Software version banners?
  [ ] SSL certificate hostnames revealing subdomains?
  [ ] Default or misconfigured service pages?
  [ ] Historical data showing services that may have been removed?
- Does the certificate reveal any additional subdomains?
- Does GitHub, GitLab, or any public repository contain code, commits, or comments referencing the target domain or organization? (leaked API keys, hardcoded credentials, internal hostnames)
- Are there any data breach records associated with discovered email addresses? (DeHashed, HaveIBeenPwned)
- ASN Lookup
  [ ] ASN identified for target organization
  [ ] All IP ranges registered to that ASN documented
  [ ] IP ranges added to Target List artifact for Phase 1b scanning
  [ ] Ranges cross-referenced with DNS findings
  [ ] Hosts with no DNS record flagged for priority investigation
  > whois 10.10.10.5 | grep -iE "ASN|AS|aut-num|org"
  > whois AS15169  # Look up the ASN directly
  > curl https://ipinfo.io/10.10.10.5/org  # Look up ASN from IP address
  > curl https://ipinfo.io/10.10.10.5/json  # Full JSON response with ASN, organization name, and IP range
  - This provides the following:
    * Without ASN lookup:
    * You know → 10.10.10.5 (one IP from DNS)
    * With ASN lookup:
    * You know → 10.10.10.0/24 (the entire range the org owns)
      * 192.168.50.0/22 (another range you didn't know existed)
      * 172.16.0.0/20 (yet another range)
  1. Find the ASN → confirms the org's registered number
  2. Find all IP ranges tied to that ASN
  3. Add all ranges to your Target List artifact
  4. Feed ranges into nmap for host discovery (Phase 1b)
  5. Cross reference with DNS findings to find hosts with no DNS record (potentially unmonitored infrastructure)

Outputs
- List of domains and subdomains
- List of IP addresses
- List of users
- List of usernames
- List of emails addresses
- Naming conventions, used technologies, and conventions used by the target
- Paths and directories used by the old version of the website
- Interesting files found by Google dorking
- ASN and IP ranges owned by the organization
- Leaked credentials or API keys found
- Data breach hits on discovered emails
- Document metadata findings
- GitHub / repository findings

Phase 1a is complete when:
[ ] Domains, subdomains, and IP addresses are documented
[ ] WHOIS, DNS, zone transfer, email harvesting, cert analysis documented
[ ] Users, usernames, emails, and credentials documented
[ ] Technologies found and used are documented
[ ] ASN and IP ranges documented
[ ] GitHub/public repo search completed and findings noted
[ ] Google dork results documented (all categories run)
[ ] Wayback Machine reviewed and findings noted
[ ] Shodan/Censys results documented
[ ] Breach database check completed on discovered emails
[ ] All raw tool output saved (not just summarized)

Phase 1b - Active Reconnaissance
Goal
Gather information by directly touching the target. Stealthy options first, louder options later.

Questions
- What hosts are up?
- What ports are filtered?
- What service, protocol, and version are running on an open port?
- Are any ports UDP ports running?
- What role is an individual machine based on the running services?
- Which machine and port have the highest priority for enumeration next phase?
- Were scans saved in all formats for reference and reporting?
- Were scans run against all hosts in the confirmed IP range, not just assumed targets?
- Did the scan reveal any unexpected hosts that weren't in the original target list?
- Were results cross-referenced with Phase 1a passive findings to confirm or expand the host list?
- Did any service banners reveal version information worth immediately cross-referencing with CVE databases?

Outputs
- Host discovery results (live hosts confirmed with IPs and hostnames)
  > nmap -sn 10.10.1.0/24 -oA host_discovery
  > sudo arp-scan -localhost | tee recon/active/arp_scan.txt
  > netdiscover -r 10.10.1.0/24 | tee recon/active/netdiscover_scan.txt
- Full TCP port scan results per host (all 65535 ports)
- Targeted service/version scan results on confirmed open ports
- UDP scan results on key ports
- Scan process
  > nmap -p- --min-rate 5000 -T4 target.htb -oA recon/active/tcp_all_ports
  > nmap -p <comma,separated,ports> -sC -sV -T4 target.htb -oA recon/active/tcp_targeted
  > nmap -sU -p 53,67,68,69,111,123,161,162,500,514,623,1194 target.htb -oA recon/active/udp_scan
  - Start with a quick sweep, move to a targeted deep scan, finish with a udp scan (very slow)
  > nmap -O --osscan-guess target.htb -oA os_detection
  - Convert nmap .xml output to html for easy reading
    > xsltproc recon/active/tcp_targeted.xml -o tcp_targeted.html
  - Quick grep for all open ports from nmap gnmap output
    > grep "open" recon/active/tcp_targeted.gnmap
- OS detection results per host (where possible)
- Updated Target List artifact (from Working Artifacts) with:
    [ ] Confirmed live hosts
    [ ] Open ports per host
    [ ] Service and version per port
    [ ] OS guess per host
    [ ] Assigned priority for Phase 2 enumeration
- All scan output saved in nmap format (-oA) for every scan run
- Directory structure for scan output looks similar to the following for each host:
  /recon
    /passive
      whois.txt
      dns_records.txt
      subdomains.txt
      shodan_results.txt
      ...
    /active
      host_discovery.nmap / .gnmap / .xml
      <host_ip>_tcp_allports.nmap / .gnmap / .xml
      <host_ip>_tcp_targeted.nmap / .gnmap / .xml
      <host_ip>_udp_scan.nmap / .gnmap / .xml

Phase 1b is complete when:
[ ] Host discovery completed — all live hosts confirmed and documented
[ ] Full TCP port scan completed on all in-scope hosts
[ ] Targeted service/version scan completed on all open TCP ports
[ ] UDP scan completed on all in-scope hosts
[ ] OS detection attempted on all hosts
[ ] All scans saved with -oA in an organized directory
[ ] Target List artifact updated with confirmed hosts, ports, services
[ ] Service Inventory artifact populated with Phase 1b findings
[ ] Unexpected hosts noted and scope confirmed with rules of engagement
[ ] Phase 1a passive findings cross-referenced with active scan results
[ ] Each host assigned an enumeration priority for Phase 2

Phase 1 is complete when:
[ ] All Phase 1a and Phase 1b checklists are fully signed off
[ ] All Working Artifacts have been updated with Phase 1 findings:
    [ ] Target List updated with confirmed hosts, OS, ports, priority
    [ ] Service Inventory populated for all discovered services
    [ ] Credentials artifact updated with any findings
    [ ] Hypothesis List populated with initial attack ideas
[ ] A prioritized list of targets and services for Phase 2 exists
[ ] All raw output is saved and organized
[ ] You can answer the following in one paragraph: "What hosts exist, what are they running, and where am I going first in Phase 2 and why?"

Phase 2 - Service Enumeration
Goal
Detailed enumeration about "every port, every service, and every version" so that potential attack paths can be planned.

Questions
For every single open port ask these questions in order:
- What service is running here?
- What version is it?
- Does it require authentication?
- Can I access it anonymously or with default credentials?
- What information can I extract from it without credentials?
- What does this service tell me about the machine's role?
- Are there known vulnerabilities for this version?

Phase 2a - Web Services (HTTP/HTTPS)
Ports: 80, 443
- Fingerprinting
  > whatweb http://target.htb | tee enum/target_htb_whatweb.txt
  > curl -IL http://target.htb | tee enum/target_htb_headers.txt
- Directory & File Bruteforce
  > feroxbuster -u http://target.htb -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt -x php,html,txt,bak,old,conf,config,xml,json -o enum/target_htb_feroxbuster.txt
  > gobuster dir -u http://target.htb -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt -x php,html,txt,bak -o enum/target_htb_gobuster.txt
- Virtual Host / Subdomain Enumeration
  > gobuster vhost -u http://target.htb -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain -o enum/target_htb_vhosts.txt
  > ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -H "Host: FUZZ.target.htb" -u http://target.htb -o enum/target_htb_ffuf_vhosts.txt
- CMS Detection & Scanning
  > wpscan --url http://target.htb --enumerate u,vp,vt,cb,dbe -o enum/target_htb_wpscan.txt
- Nikto (noisy, catches misconfigurations)
  > nikto -h http://target.htb -o enum/target_htb_nikto.txt
- SSL Certification Inspection (HTTPS targets)
  > openssl s_client -connect target.htb:443 </dev/null 2>/dev/null | openssl x509 -noout -text | tee enum/web_ssl_cert.txt
  > sslscan target.htb | tee enum/web_sslscan.txt








Reference Sheets
-----
Passive Reconnaissance Steps
# 1. Create your output directory first
mkdir -p recon/passive

# 2. WHOIS - get registrant info and nameservers
whois targetdomain.com | tee recon/passive/whois.txt

# 3. Grab all common DNS records
dig A targetdomain.com +short | tee recon/passive/dns_A.txt
dig AAAA targetdomain.com +short | tee recon/passive/dns_AAAA.txt
dig MX targetdomain.com | tee recon/passive/dns_MX.txt
dig NS targetdomain.com +short | tee recon/passive/dns_NS.txt
dig TXT targetdomain.com | tee recon/passive/dns_TXT.txt
dig SOA targetdomain.com | tee recon/passive/dns_SOA.txt

# 4. Attempt zone transfer against each nameserver found in step 2
dig axfr @<nameserver1> targetdomain.com | tee recon/passive/zone_transfer_ns1.txt
dig axfr @<nameserver2> targetdomain.com | tee recon/passive/zone_transfer_ns2.txt

# 5. Reverse lookups on any IPs discovered
dig -x <discovered_ip> | tee recon/passive/reverse_<ip>.txt



WHOIS
-----
whois domain.com                          → Full registrant info
whois <ip>                                → IP ownership info

DIG
---
dig A domain.com +short                   → IPv4 address
dig AAAA domain.com +short                → IPv6 address
dig MX domain.com                         → Mail servers
dig NS domain.com +short                  → Nameservers
dig TXT domain.com                        → Text records
dig SOA domain.com                        → Zone authority
dig -x <ip>                               → Reverse lookup
dig axfr @<nameserver> domain.com         → Zone transfer attempt

NSLOOKUP
--------
nslookup domain.com                       → Basic lookup
nslookup -type=MX domain.com             → Mail servers
nslookup <ip>                             → Reverse lookup

HOST
----
host domain.com                           → Quick A record
host -t MX domain.com                    → Mail servers
host <ip>                                 → Reverse lookup




Google Dorking (exploit-db.com/google-hacking-database)
-----
Credential & Sensitive Data Discovery
These are the highest value dorks for a penetration test.
# Look for password files
filetype:txt intext:"password" site:targetdomain.com
filetype:log intext:"password"
filetype:env intext:"DB_PASSWORD"

# Configuration files with credentials
filetype:xml intext:"password" site:targetdomain.com
filetype:yml intext:"password" site:targetdomain.com
filetype:config intext:"password" site:targetdomain.com

# Private keys accidentally exposed
filetype:pem intext:"PRIVATE KEY"
filetype:key intext:"PRIVATE KEY"

# Database connection strings
filetype:sql intext:"INSERT INTO" site:targetdomain.com
intext:"DB_CONNECTION" filetype:env

# AWS / API keys
intext:"AKIA" filetype:txt
intext:"aws_access_key_id" filetype:txt


Exposed Files & Directories
# Open directory listings — goldmine for files
intitle:"index of" site:targetdomain.com
intitle:"index of" "parent directory" site:targetdomain.com
intitle:"index of" intext:".sql"
intitle:"index of" intext:".bak"
intitle:"index of" intext:".log"

# Backup files
filetype:bak site:targetdomain.com
filetype:old site:targetdomain.com
filetype:backup site:targetdomain.com
inurl:backup site:targetdomain.com
inurl:".bak" OR inurl:".old" OR inurl:".backup" site:targetdomain.com

# Log files
filetype:log site:targetdomain.com
intitle:"index of" "access.log"
intitle:"index of" "error.log"

# Database files
filetype:sql site:targetdomain.com
filetype:db site:targetdomain.com
filetype:sqlite site:targetdomain.com


Login & Admin Panels
# Generic admin panels
inurl:admin site:targetdomain.com
inurl:login site:targetdomain.com
inurl:administrator site:targetdomain.com
inurl:portal site:targetdomain.com
intitle:"admin login" site:targetdomain.com
intitle:"admin panel" site:targetdomain.com

# Specific CMS login pages
inurl:wp-admin site:targetdomain.com  # WordPress
inurl:wp-login.php site:targetdomain.com  # WordPress
inurl:/administrator/index.php site:targetdomain.com  # Joomla
inurl:/user/login site:targetdomain.com  # Drupal

# Remote access panels
intitle:"phpMyAdmin" inurl:phpmyadmin
intitle:"Webmin" inurl:10000
inurl:"/remote/login" intitle:"FortiGate"
intitle:"Kibana" inurl:5601


Technology & Version Discovery
# Find specific technologies in use
intext:"powered by" site:targetdomain.com
intitle:"Welcome to" intext:"Apache" site:targetdomain.com

# Error messages revealing tech stack
intext:"Fatal error" site:targetdomain.com
intext:"Warning: mysql_" site:targetdomain.com
intext:"ORA-" site:targetdomain.com   # Oracle DB errors
intext:"Microsoft OLE DB Provider" site:targetdomain.com  # MSSQL errors
intext:"syntax error" filetype:php site:targetdomain.com

# Server default pages (often mean misconfigured servers)
intitle:"Apache2 Ubuntu Default Page" site:targetdomain.com
intitle:"Welcome to nginx" site:targetdomain.com
intitle:"IIS Windows Server" site:targetdomain.com
intitle:"Test Page for Apache" site:targetdomain.com


Sensitive Documents
# General sensitive document search
filetype:pdf "confidential" site:targetdomain.com
filetype:pdf "internal use only" site:targetdomain.com
filetype:xlsx site:targetdomain.com
filetype:docx site:targetdomain.com

# Documents that often contain usernames or internal info
filetype:pdf site:targetdomain.com
filetype:doc site:targetdomain.com

# Network diagrams and documentation
filetype:pdf intitle:"network diagram"
filetype:pdf intitle:"infrastructure"


Subdomain & Infrastructure Discovery
# Find subdomains not found through other methods
site:*.targetdomain.com
site:targetdomain.com -www  # Exclude www, find others

# VPN and remote access infrastructure
inurl:vpn site:targetdomain.com
intitle:"SSL VPN" site:targetdomain.com
inurl:remote site:targetdomain.com

# Development and staging environments
inurl:dev site:targetdomain.com
inurl:staging site:targetdomain.com
inurl:test site:targetdomain.com
inurl:beta site:targetdomain.com


User & Employee Information
# Employee names and emails
site:linkedin.com "targetdomain.com"
site:linkedin.com/in "Target Company"

# Email addresses indexed on the site
intext:"@targetdomain.com" site:targetdomain.com
filetype:pdf intext:"@targetdomain.com"

# Resumes that reveal internal tech stack
site:linkedin.com "targetdomain.com" "engineer"
site:linkedin.com "targetdomain.com" "administrator"


Misconfiguration & Vulnerability Discovery
# Exposed Git repositories
inurl:"/.git" site:targetdomain.com
intitle:"index of" ".git" site:targetdomain.com

# Exposed WordPress config files
inurl:wp-config.php site:targetdomain.com

# Exposed .htaccess and .htpasswd
filetype:htpasswd inurl:htpasswd
inurl:.htaccess site:targetdomain.com

# Exposed phpinfo pages (reveals PHP config and server info)
intitle:"phpinfo()" site:targetdomain.com
inurl:phpinfo.php site:targetdomain.com

# Exposed .env files
inurl:.env site:targetdomain.com
filetype:env site:targetdomain.com

# Exposed SSH config
filetype:pub intext:"ssh-rsa"
