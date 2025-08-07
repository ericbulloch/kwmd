# THM: VulnNet: Node

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/vuln_net_node/vuln_net_node.png" alt="VulnNet: Node" width="90"/> |
| Room | VulnNet: Node |
| URL | https://tryhackme.com/room/vulnnetnode |
| Difficulty | Easy |

## Concepts/Tools Used

- base64

## Room Description

After the previous breach, VulnNet Entertainment states it won't happen again. Can you prove they're wrong?

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -v -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-25 19:45 BST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 19:45
Completed NSE at 19:45, 0.00s elapsed
Initiating NSE at 19:45
Completed NSE at 19:45, 0.00s elapsed
Initiating NSE at 19:45
Completed NSE at 19:45, 0.00s elapsed
Initiating ARP Ping Scan at 19:45
Scanning target.thm (10.10.173.80) [1 port]
Completed ARP Ping Scan at 19:45, 0.03s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 19:45
Scanning target.thm (10.10.173.80) [65535 ports]
Discovered open port 8080/tcp on 10.10.173.80
Discovered open port 22/tcp on 10.10.173.80
Completed SYN Stealth Scan at 19:45, 2.45s elapsed (65535 total ports)
Initiating Service scan at 19:45
Scanning 2 services on target.thm (10.10.173.80)
Completed Service scan at 19:45, 6.89s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.173.80.
Initiating NSE at 19:45
Completed NSE at 19:45, 1.32s elapsed
Initiating NSE at 19:45
Completed NSE at 19:45, 0.17s elapsed
Initiating NSE at 19:45
Completed NSE at 19:45, 0.00s elapsed
Nmap scan report for target.thm (10.10.173.80)
Host is up (0.00011s latency).
Not shown: 65533 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
8080/tcp open  http    Node.js Express framework
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-open-proxy: Proxy might be redirecting requests
|_http-title: VulnNet &ndash; Your reliable news source &ndash; Try Now!
MAC Address: 02:30:92:F5:EA:A5 (Unknown)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 19:45
Completed NSE at 19:45, 0.00s elapsed
Initiating NSE at 19:45
Completed NSE at 19:45, 0.00s elapsed
Initiating NSE at 19:45
Completed NSE at 19:45, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.63 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 65536 (2.621MB)
```

I explored the website on port 8080. I checked a few things and I couldn't find anything. I examined the requests and responses and I noticed that I had a session value. Here is what my header looked like:

```text
Cookie: session=eyJ1c2VybmFtZSI6Ikd1ZXN0IiwiaXNHdWVzdCI6dHJ1ZSwiZW5jb2RpbmciOiAidXRmLTgifQ%3D%3D
```
The %3D is the `=` character with html encoding. That means the session is:

```text
eyJ1c2VybmFtZSI6Ikd1ZXN0IiwiaXNHdWVzdCI6dHJ1ZSwiZW5jb2RpbmciOiAidXRmLTgifQ==
```

That looks like it is base64 encoded. I ran the following in the command line:

```bash
$ echo 'eyJ1c2VybmFtZSI6Ikd1ZXN0IiwiaXNHdWVzdCI6dHJ1ZSwiZW5jb2RpbmciOiAidXRmLTgifQ==' | base64 -d
{"username":"Guest","isGuest":true,"encoding": "utf-8"}
```

I couldn't change these values to anything that would allow a login. It turns out this was a red herring.

Looking back at the nmap output I see that the site is running on Node.js Express framework. I ran some google searches and found a repository that can get a reverse shell on Node.js servers. The repository can be [found here](https://github.com/ajinabraham/Node.Js-Security-Course/blob/master/nodejsshell.py).


