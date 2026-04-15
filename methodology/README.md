# Hacking Methodology

## 1. Reconnaissance
- [Passive recon](reconnaissance/passive.md)
- Active recon
- Subdomain enumeration

## 2. Enumeration
- [Host discovery](enumeration/host_discovery.md)
- [Port Scanning](enumeration/port_scanning.md)
- Services
  - [FTP](enumeration/ftp.md) (21)
  - [SMTP](enumeration/smtp.md) (25, 465, 587)
  - [DNS](enumeration/dns.md) (53, 53 UDP)
  - [MySQL](enumeration/mysql.md) (3306)
  - [NFS](enumeration/nfs.md) (111, 2049)
  - [SMB](enumeration/smb.md) (139, 445)
  - [SNMP](enumeration/snmp.md) (161 UDP, 162 UDP)
  - [IMAP/POP3](enumeration/imap_pop3.md) (110, 143, 993, 995)
- Users
- Shares

## 3. Exploitation
- Vulnerability identification
- Exploit execution

## 4. Privilege Escalation
- Linux privesc
- Windows privesc

## 5. Post-Exploitation
- Persistence
- Data exfiltration
- Pivoting
