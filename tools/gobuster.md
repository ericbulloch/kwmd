# THM: All in One

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/all_in_one/all_in_one.png" alt="All in One" width="90"/> |
| Room | All in One |
| URL | https://tryhackme.com/room/allinonemj |
| Difficulty | Easy |

## Concepts/Tools Used

- [ftp](/tools/ftp.md)
- [gobuster](/tools/gobuster.md)
- [wpscan](/tools/wpscan.md)
- [find](/tools/find.md)
- base64

## Room Description

This is a fun box where you will get to exploit the system in several ways. Few intended and unintended paths to getting user and root access.

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -v -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-14 18:12 BST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 18:12
Completed NSE at 18:12, 0.00s elapsed
Initiating NSE at 18:12
Completed NSE at 18:12, 0.00s elapsed
Initiating NSE at 18:12
Completed NSE at 18:12, 0.00s elapsed
Initiating ARP Ping Scan at 18:12
Scanning target.thm (10.10.242.126) [1 port]
Completed ARP Ping Scan at 18:12, 0.04s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 18:12
Scanning target.thm (10.10.242.126) [65535 ports]
Discovered open port 22/tcp on 10.10.242.126
Discovered open port 21/tcp on 10.10.242.126
Discovered open port 80/tcp on 10.10.242.126
Completed SYN Stealth Scan at 18:12, 2.30s elapsed (65535 total ports)
Initiating Service scan at 18:12
Scanning 3 services on target.thm (10.10.242.126)
Completed Service scan at 18:12, 6.04s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.242.126.
Initiating NSE at 18:12
NSE: [ftp-bounce] PORT response: 500 Illegal PORT command.
Completed NSE at 18:12, 0.84s elapsed
Initiating NSE at 18:12
Completed NSE at 18:12, 0.05s elapsed
Initiating NSE at 18:12
Completed NSE at 18:12, 0.00s elapsed
Nmap scan report for target.thm (10.10.242.126)
Host is up (0.00013s latency).
Not shown: 65532 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.5
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.10.137.140
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.5 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
MAC Address: 02:77:89:7F:E5:71 (Unknown)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 18:12
Completed NSE at 18:12, 0.00s elapsed
Initiating NSE at 18:12
Completed NSE at 18:12, 0.00s elapsed
Initiating NSE at 18:12
Completed NSE at 18:12, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.93 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 65536 (2.621MB)
```
