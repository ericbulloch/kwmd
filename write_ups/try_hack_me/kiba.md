# THM: Kiba

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="../../images/write_ups/try_hack_me/kiba/kiba.png" alt="Kiba" width="90"/> |
| Room | Kiba |
| URL | https://tryhackme.com/room/kiba |
| Difficulty | Easy |

## Concepts/Tools Used



## Room Description

Identify the critical security flaw in the data visualization dashboard, that allows execute remote code execution.

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -p- target.thm

```
