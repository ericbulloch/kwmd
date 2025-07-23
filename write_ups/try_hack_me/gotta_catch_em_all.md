# THM: Gotta Catch'em All!

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/gotta_catch_em_all/gotta_catch_em_all.jpeg" alt="Gotta Catch'em All!" width="90"/> |
| Room | Gotta Catch'em All! |
| URL | [https://tryhackme.com/room/pokemon](https://tryhackme.com/room/pokemon) |
| Difficulty | Easy |

## Concepts/Tools Used

- [find](/tools/find.md)

## Room Description

This room is based on the original Pokemon series. Can you obtain all the Pokemon in this room?

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:
```bash
$ nmap -T4 -n -sC -sV -Pn -v -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-06-25 18:11 BST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 18:11
Completed NSE at 18:11, 0.00s elapsed
Initiating NSE at 18:11
Completed NSE at 18:11, 0.00s elapsed
Initiating NSE at 18:11
Completed NSE at 18:11, 0.00s elapsed
Initiating ARP Ping Scan at 18:11
Scanning target.thm (10.10.109.207) [1 port]
Completed ARP Ping Scan at 18:11, 0.03s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 18:11
Scanning target.thm (10.10.109.207) [65535 ports]
Discovered open port 22/tcp on 10.10.109.207
Discovered open port 80/tcp on 10.10.109.207
Completed SYN Stealth Scan at 18:11, 1.47s elapsed (65535 total ports)
Initiating Service scan at 18:11
Scanning 2 services on target.thm (10.10.109.207)
Completed Service scan at 18:11, 6.04s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.109.207.
Initiating NSE at 18:11
Completed NSE at 18:11, 0.09s elapsed
Initiating NSE at 18:11
Completed NSE at 18:11, 0.01s elapsed
Initiating NSE at 18:11
Completed NSE at 18:11, 0.00s elapsed
Nmap scan report for target.thm (10.10.109.207)
Host is up (0.00014s latency).
Not shown: 65533 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 58:14:75:69:1e:a9:59:5f:b2:3a:69:1c:6c:78:5c:27 (RSA)
|   256 23:f5:fb:e7:57:c2:a5:3e:c2:26:29:0e:74:db:37:c2 (ECDSA)
|_  256 f1:9b:b5:8a:b9:29:aa:b6:aa:a2:52:4a:6e:65:95:c5 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-methods:
|_  Supported Methods: POST OPTIONS GET HEAD
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Can You Find Them All?
MAC Address: 02:2B:68:F5:74:69 (Unknown)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 18:11
Completed NSE at 18:11, 0.00s elapsed
Initiating NSE at 18:11
Completed NSE at 18:11, 0.00s elapsed
Initiating NSE at 18:11
Completed NSE at 18:11, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.36 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 65536 (2.621MB)
```

I check the ssh service on port 22, it allows password authentication. I checked it by running:

```bash
$ ssh target.thm
```

## Getting a Foothold

I decided to check the website by going to http://target.thm in Chrome. I inspect the html and I see the following comment:

```bash
<!--(Check console for extra surprise!)-->
```

I checked the console which didn't show me much beside the names of some pokemon. Right above this comment there are 2 tags separated by a colon. This stumped me for a long time. I see usernames and passwords in the format `username:password` all the time. The tags above that comment had the format `<username>:<password>`. The tags threw me off. When I removed the tag brackets text text had the username and password format that I just mentioned. I used that username and password to ssh into the machine.

I ran the following command:

```bash
$ ssh pokemon@target.thm
```

I have a shell. I'm in!

## Find the Grass-Type Pokemon

I ran the following to see what files are in the home directory:

```bash
$ ls -lha
```

In most capture the flag events there is a flag file in this directory. Since I don't see one here I look through all the directories in in this folder. I noticed that the Desktop directory has a P0kEmOn.zip file.

I unzip the file by running:

```bash
$ unzip P0kEmOn.zip
```

Now I cat the grass-type.txt file that is in the P0kEmOn directory:

```bash
$ cat P0kEmOn/grass-type.txt
50 6f 4b 65 4d 6f 4e 7b 42 75 6c 62 61 73 61 75 72 7d
```

This text is hex encoded. I use From Hex on [CyberChef](https://gchq.github.io/CyberChef/) to get the flag.

## Horizontal Privilege Escalation

I continue to look through the other folders on in pokemon's home directory. I found something interesting in the Videos folder. There is a C++ file that has credentials. I get the credentials by using cat to view them:

```bash
$ cat Videos/Gotta/Catch/Them/ALL!/Could_this_be_what_Im_looking_for?.cplusplus
# include <iostream>

int main() {
std::cout << "ash : REDACTED"
return 0;
}
```

I have a new username and password. I confirm that ash is in the /home directory by running:

```bash
$ ls /home
ash pokemon roots-pokemon.txt
```

I run the following to become ash by running the following command:

```bash
$ su ash
```

Just like that I am now ash.

## Who is Root's Favorite Pokemon?

The /home/roots-pokemon.txt file is owned by ash. Now that I am ash, I cat the file to get the flag:

```bash
$ cat /home/roots-pokemon.txt
REDACTED
```

## Find the Water-Type Pokemon

I finished looking around all the other folders in pokemon's directory. Once I finished that, I looked around in ash's home directory. I didn't find anything interesting.

I started looking around other common folders. I first checked /opt. I didn't find anything. I then moved to /var. In the /var/www/html folder has a file called water-type.txt. I viewd the contents of it with the following command:

```bash
$ cat /var/www/html/water-type.txt
Ecgudfxq_EcGmP{Ecgudfxq}
```

This text is encoded in ROT13 so I used the ROT13 recipe on [CyberChef](https://gchq.github.io/CyberChef/) to break it. This recipe has an amount you can change, I adjust it to 14 and it give the flag.

## Find the Fire-Type Pokemon

At this point all the files have had the same format for the name. I run the following command to locate the fire-type.txt file:

```bash
$ find / -type f -name fire*.txt 2>/dev/null
/etc/why_am_i_here?/fire-type.txt
```

I cat the file:

```bash
$ cat /etc/why_am_i_here?/fire-type.txt
UDBrM20wbntDaGFybWFuZGVyfQ==
```

This text is base64 encoded I can tell from the = characters at the end. I used the From Base64 recipe on [CyberChef](https://gchq.github.io/CyberChef/) to break it.
