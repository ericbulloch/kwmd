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

The output mentions a directory that starts with a "g".

## Whose name can you find from this directory?

## What directory has basic authentication?

## What is bob's password to the protected part of the website?

## What other port that serves a webs service is open on the machine?

## What is the name and version of the software running on the port from question 5?

## Use Nikto with the credentials you have found and scan the /manager/html directory on the port found above. How many docume0?

## What is the server version?

## What version of Apache-Coyote is this service using?

## Use Metasploit to exploit the service and get a shell on the system. What user did you get a shell as?

## What flag is found in the root directory?
