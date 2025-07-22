# THM: Bebop

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/bebop/bebop.jpeg" alt="Bebop" width="90"/> |
| Room | Bebop |
| URL | https://tryhackme.com/room/bebop |
| Difficulty | Easy |

## Concepts/Tools Used

- telnet

## Room Description

Who thought making a flying shell was a good idea?

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -v -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-22 11:06 BST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 11:06
Completed NSE at 11:06, 0.00s elapsed
Initiating NSE at 11:06
Completed NSE at 11:06, 0.00s elapsed
Initiating NSE at 11:06
Completed NSE at 11:06, 0.00s elapsed
Initiating ARP Ping Scan at 11:06
Scanning target.thm (10.10.169.138) [1 port]
Completed ARP Ping Scan at 11:06, 0.03s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 11:06
Scanning target.thm (10.10.169.138) [65535 ports]
Discovered open port 23/tcp on 10.10.169.138
Discovered open port 22/tcp on 10.10.169.138
Increasing send delay for 10.10.169.138 from 0 to 5 due to max_successful_tryno increase to 5
SYN Stealth Scan Timing: About 8.82% done; ETC: 11:12 (0:05:21 remaining)
SYN Stealth Scan Timing: About 17.66% done; ETC: 11:12 (0:04:44 remaining)
SYN Stealth Scan Timing: About 26.51% done; ETC: 11:12 (0:04:12 remaining)
SYN Stealth Scan Timing: About 35.34% done; ETC: 11:12 (0:03:41 remaining)
SYN Stealth Scan Timing: About 44.11% done; ETC: 11:12 (0:03:11 remaining)
SYN Stealth Scan Timing: About 52.85% done; ETC: 11:12 (0:02:42 remaining)
SYN Stealth Scan Timing: About 61.40% done; ETC: 11:12 (0:02:13 remaining)
SYN Stealth Scan Timing: About 69.78% done; ETC: 11:12 (0:01:44 remaining)
SYN Stealth Scan Timing: About 78.40% done; ETC: 11:12 (0:01:15 remaining)
SYN Stealth Scan Timing: About 86.77% done; ETC: 11:12 (0:00:46 remaining)
Completed SYN Stealth Scan at 11:12, 346.69s elapsed (65535 total ports)
Initiating Service scan at 11:12
Scanning 2 services on target.thm (10.10.169.138)
Completed Service scan at 11:12, 0.02s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.169.138.
Initiating NSE at 11:12
Completed NSE at 11:12, 7.04s elapsed
Initiating NSE at 11:12
Completed NSE at 11:12, 0.01s elapsed
Initiating NSE at 11:12
Completed NSE at 11:12, 0.00s elapsed
Nmap scan report for target.thm (10.10.169.138)
Host is up (0.00033s latency).
Not shown: 65533 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.5 (FreeBSD 20170903; protocol 2.0)
| ssh-hostkey: 
|   2048 5b:e6:85:66:d8:dd:04:f0:71:7a:81:3c:58:ad:0b:b9 (RSA)
|   256 d5:4e:18:45:ba:d4:75:2d:55:2f:fe:c9:1c:db:ce:cb (ECDSA)
|_  256 96:fc:cc:3e:69:00:79:85:14:2a:e4:5f:0d:35:08:d4 (ED25519)
23/tcp open  telnet  BSD-derived telnetd
MAC Address: 02:45:DA:EE:66:E9 (Unknown)
Service Info: OS: FreeBSD; CPE: cpe:/o:freebsd:freebsd

NSE: Script Post-scanning.
Initiating NSE at 11:12
Completed NSE at 11:12, 0.00s elapsed
Initiating NSE at 11:12
Completed NSE at 11:12, 0.00s elapsed
Initiating NSE at 11:12
Completed NSE at 11:12, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 355.73 seconds
           Raw packets sent: 66080 (2.908MB) | Rcvd: 65537 (2.621MB)
```
