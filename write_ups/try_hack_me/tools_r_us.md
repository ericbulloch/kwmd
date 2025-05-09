# THM: ToolsRus

| Stat       | Value                                        |
| ---------- | -------------------------------------------- |
| Room       | ToolsRus                         |
| URL        | https://tryhackme.com/room/toolsrus     |
| Difficulty | Easy                                         |

## Concepts/Tools Used

- [Dirbuster](../../tools/dirbuster.md)
- [Hydra](../../tools/hydra.md)
- [Nmap](../../tools/nmap.md)
- [Nikto](../../tools/nikto.md)
- [Metasploit](../../tools/msfconsole.md)

## Description

Your challenge is to use the tools listed below to enumerate a server, gathering information along the way that will eventually lead to you taking over the machine.

This room will introduce you to the following tools: 

- Dirbuster
- Hydra
- Nmap
- Nikto
- Metasploit

## Process

This room presents a series of questions that needs to be answered using different tools. Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

## What directory can you find, that begins with a "g"?

First of all, I run a couple of nmap commands to find out what ports are open and what software is listening on those ports. I run the following command:

`nmap -p- -Pn -T5 -v target.thm`

Then I run to following based on what ports were discovered in the previous command:

`nmap -A -Pn -v target.thm -p 22,80,1234,8009`

Port 80 has the http service running on it. It has Apache 2.4.18 running. So now I know what port we need to run `dirb` on. I run the following command to answer the question:

`dirb http://target.thm /usr/share/wordlists/dirb/common.txt`

The output mentions a directory that starts with a "g". Here is the output:

```bash
---- Entering directory: http://target.thm/gxxxxxxxx/ ----
+ http://target.thm/gxxxxxxxx/index.html (CODE:200|SIZE:51)
```

## Whose name can you find from this directory?

I opened up the browser and went to the following url:

`http://target.thm/gxxxxxxxx/`

The rendered page has a name on it. The text on the page reads:

`Hey xxx, did you update that TomCat server?`

## What directory has basic authentication?

Since I am looking for a directory that has basic authentication, I went back to my dirbuster output and noticed which directory returned a 401 error. The output from dirbuster was:

```bash
+ http://target.thm/index.html (CODE:200|SIZE:168)
+ http://target.thm/pxxxxxxxx (CODE:401|SIZE:457)
+ http://target.thm/server-status (CODE:403|SIZE:298)
```

I pulled up the middle result in a browser and sure enough it wanted basic authentication.

## What is bob's password to the protected part of the website?

I have a username, and now I need to try and brute force a password for the user bob. I have documentation on how to [break basic authentication using hydra](../../tools/hydra.md#http-get). I copy that guide and run the following command:

`hydra -l bob -P /usr/share/wordlists/rockyou.txt http-get://target.thm/protected/`

I waited a moment and got the following output:

```bash
[DATA] attacking http-get://target.thm:80/protected/
[80][http-get] host: target.thm   login: bob   password: xxxxxxx
1 of 1 target successfully completed, 1 valid password found
```

Logging in with those credentials, I get a message that this page has move to another port.

## What other port that serves a webs service is open on the machine?

I went back to the output of the 2nd nmap command that I ran above. The output from nmap tells me which port is the one:

```bash
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 cd:d9:c0:87:11:dc:40:53:4e:b9:ce:54:bb:cf:26:52 (RSA)
|   256 e1:18:eb:5d:ae:b8:c3:a1:e5:0b:73:6b:21:dd:18:29 (ECDSA)
|_  256 7e:b2:13:a5:ad:05:32:88:1a:22:e6:27:f1:50:16:b4 (ED25519)
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
1234/tcp open  http    Apache Tomcat/Coyote JSP engine 1.1
|_http-favicon: Apache Tomcat
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache-Coyote/1.1
|_http-title: xxxxx xxxxxx/x.x.xx
8009/tcp open  ajp13   Apache Jserv (Protocol v1.3)
|_ajp-methods: Failed to get a valid response for the OPTION request
```

I see that port 1234 is running an http server.

## What is the name and version of the software running on the port from question 5?

The last line of output for port 1234 tells the name and version of the software running on port 1234.

## Use Nikto with the credentials you have found and scan the /manager/html directory on the port found above. How many docume0?

## What is the server version?

## What version of Apache-Coyote is this service using?

## Use Metasploit to exploit the service and get a shell on the system. What user did you get a shell as?

## What flag is found in the root directory?
