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

## What other port that serves a webs service is open on the machine?

## What is the name and version of the software running on the port from question 5?

## Use Nikto with the credentials you have found and scan the /manager/html directory on the port found above. How many docume0?

## What is the server version?

## What version of Apache-Coyote is this service using?

## Use Metasploit to exploit the service and get a shell on the system. What user did you get a shell as?

## What flag is found in the root directory?
