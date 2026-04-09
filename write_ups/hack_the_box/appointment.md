# Target: Appointment

- IP Address: 10.129.1.1
- Starting Domain Name: target.htb

## Scope & Goal
- Objective: user.txt, root.txt
- Constraints: lab

# Recon
- Quick TCP:

```bash
$ nmap target.htb                       
Starting Nmap 7.98 ( https://nmap.org ) at 2026-04-09 13:38 -0400
Nmap scan report for target.htb (10.129.100.194)
Host is up (0.068s latency).
Not shown: 999 closed tcp ports (reset)
PORT   STATE SERVICE
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 1.32 seconds
```

- Targeted Scan:

```bash
$ nmap target.htb -sV -sC -A -p80 -vv   
Starting Nmap 7.98 ( https://nmap.org ) at 2026-04-09 13:38 -0400
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:38
Completed NSE at 13:38, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:38
Completed NSE at 13:38, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:38
Completed NSE at 13:38, 0.00s elapsed
Initiating Ping Scan at 13:38
Scanning target.htb (10.129.100.194) [4 ports]
Completed Ping Scan at 13:38, 0.09s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 13:38
Scanning target.htb (10.129.100.194) [1 port]
Discovered open port 80/tcp on 10.129.100.194
Completed SYN Stealth Scan at 13:38, 0.08s elapsed (1 total ports)
Initiating Service scan at 13:38
Scanning 1 service on target.htb (10.129.100.194)
Completed Service scan at 13:38, 6.20s elapsed (1 service on 1 host)
Initiating OS detection (try #1) against target.htb (10.129.100.194)
Initiating Traceroute at 13:38
Completed Traceroute at 13:38, 0.06s elapsed
Initiating Parallel DNS resolution of 1 host. at 13:38
Completed Parallel DNS resolution of 1 host. at 13:38, 0.50s elapsed
NSE: Script scanning 10.129.100.194.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:38
Completed NSE at 13:38, 2.13s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:38
Completed NSE at 13:38, 0.27s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:38
Completed NSE at 13:38, 0.01s elapsed
Nmap scan report for target.htb (10.129.100.194)
Host is up, received echo-reply ttl 63 (0.069s latency).
Scanned at 2026-04-09 13:38:41 EDT for 11s

PORT   STATE SERVICE REASON         VERSION
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.38 ((Debian))
|_http-title: Login
|_http-server-header: Apache/2.4.38 (Debian)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-favicon: Unknown favicon MD5: 7D4140C76BF7648531683BFA4F7F8C22
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|router
Running: Linux 4.X|5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 4.15 - 5.19, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
TCP/IP fingerprint:
OS:SCAN(V=7.98%E=4%D=4/9%OT=80%CT=%CU=36814%PV=Y%DS=2%DC=T%G=N%TM=69D7E42C%
OS:P=x86_64-pc-linux-gnu)SEQ(SP=109%GCD=1%ISR=10D%TI=Z%CI=Z%II=I%TS=A)OPS(O
OS:1=M552ST11NW7%O2=M552ST11NW7%O3=M552NNT11NW7%O4=M552ST11NW7%O5=M552ST11N
OS:W7%O6=M552ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)ECN(R
OS:=Y%DF=Y%T=40%W=FAF0%O=M552NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%
OS:RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y
OS:%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R
OS:%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=
OS:40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S
OS:)

Uptime guess: 22.056 days (since Wed Mar 18 12:17:38 2026)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=265 (Good luck!)
IP ID Sequence Generation: All zeros

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   60.58 ms 10.10.14.1
2   61.13 ms target.htb (10.129.100.194)

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:38
Completed NSE at 13:38, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:38
Completed NSE at 13:38, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:38
Completed NSE at 13:38, 0.00s elapsed
Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.69 seconds
           Raw packets sent: 37 (2.414KB) | Rcvd: 26 (1.790KB)
```

- Full TCP:

```bash
$ nmap target.htb -sC -sV -A -T4 -vv -p-
...
Same as Targeted Scan above
```

## Open Services
- 80/http

## Web Enum
- Tech: Apache httpd 2.4.38
- Dirs/VHosts:

```bash
$ gobuster dir -u http://target.htb -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt 
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://target.htb
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
images               (Status: 301) [Size: 309] [--> http://target.htb/images/]
css                  (Status: 301) [Size: 306] [--> http://target.htb/css/]
js                   (Status: 301) [Size: 305] [--> http://target.htb/js/]
vendor               (Status: 301) [Size: 309] [--> http://target.htb/vendor/]
fonts                (Status: 301) [Size: 308] [--> http://target.htb/fonts/]
server-status        (Status: 403) [Size: 275]
Progress: 207641 / 207641 (100.00%)
===============================================================
Finished
===============================================================
```

- Params/Endpoints:
- Findings:

## Foothold
- Vector:
- Steps/Commands:
- Evidence:

## Privilege Escalation
- System Information:
- Credentials/Loot:
- Linux Checks:
- Successful Path:

## Flags
- user.txt: `hash` (date -u)
- root.txt: `hash` (date -u)

## Cleanup
- Artifacts Removed

## Lessons
- What Worked:
- Dead Ends:
- Reusable Commands:

```bash

```
