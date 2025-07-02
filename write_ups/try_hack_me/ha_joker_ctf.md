# THM: HA Joker CTF

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="../../images/write_ups/try_hack_me/ha_joker_ctf/ha_joker_ctf.jpeg" alt="HA Joker CTF" width="90"/> |
| Room | HA Joker CTF |
| URL | [https://tryhackme.com/room/jokerctf](https://tryhackme.com/room/jokerctf) |
| Difficulty | Easy |

## Concepts/Tools Used



## Room Description

Batman hits Joker.

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

## Enumerate services on target machine.

I run nmap to see what ports are open:
```bash
$ nmap -T4 -n -sC -sV -Pn -v -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-02 04:58 BST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 04:58
Completed NSE at 04:58, 0.00s elapsed
Initiating NSE at 04:58
Completed NSE at 04:58, 0.00s elapsed
Initiating NSE at 04:58
Completed NSE at 04:58, 0.00s elapsed
Initiating ARP Ping Scan at 04:58
Scanning target.thm (10.10.83.112) [1 port]
Completed ARP Ping Scan at 04:58, 0.04s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 04:58
Scanning target.thm (10.10.83.112) [65535 ports]
Discovered open port 8080/tcp on 10.10.83.112
Discovered open port 22/tcp on 10.10.83.112
Discovered open port 80/tcp on 10.10.83.112
Completed SYN Stealth Scan at 04:58, 2.35s elapsed (65535 total ports)
Initiating Service scan at 04:58
Scanning 3 services on target.thm (10.10.83.112)
Completed Service scan at 04:58, 6.07s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.83.112.
Initiating NSE at 04:58
Completed NSE at 04:58, 0.47s elapsed
Initiating NSE at 04:58
Completed NSE at 04:58, 0.01s elapsed
Initiating NSE at 04:58
Completed NSE at 04:58, 0.01s elapsed
Nmap scan report for target.thm (10.10.83.112)
Host is up (0.000096s latency).
Not shown: 65532 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 ad:20:1f:f4:33:1b:00:70:b3:85:cb:87:00:c4:f4:f7 (RSA)
|   256 1b:f9:a8:ec:fd:35:ec:fb:04:d5:ee:2a:a1:7a:4f:78 (ECDSA)
|_  256 dc:d7:dd:6e:f6:71:1f:8c:2c:2c:a1:34:6d:29:99:20 (ED25519)
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: HA: Joker
8080/tcp open  http    Apache httpd 2.4.29
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Basic realm=Please enter the password.
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: 401 Unauthorized
MAC Address: 02:17:AC:6D:9E:AB (Unknown)
Service Info: Host: localhost; OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 04:58
Completed NSE at 04:58, 0.00s elapsed
Initiating NSE at 04:58
Completed NSE at 04:58, 0.00s elapsed
Initiating NSE at 04:58
Completed NSE at 04:58, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.95 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 65536 (2.621MB)
```

## What version of Apache is it?

Looking at the nmap output above, Apache is running on ports 80 and 8080. The version is 2.4.29.

## What port on this machine not need to be authenticated by user and password?

This question slightly vague. Port 22 is ssh and it requires an ssh key or a username and password combination. But that is not the answer it is looking for. I pull up the site in Chrome by navigating to http://target.thm. This site is using basic authentication. Since this is http and a port wasn't specified it defaults to 80.
