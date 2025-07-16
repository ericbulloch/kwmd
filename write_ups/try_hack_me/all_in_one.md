# THM: All in One

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/all_in_one/all_in_one.png" alt="All in One" width="90"/> |
| Room | All in One |
| URL | https://tryhackme.com/room/allinonemj |
| Difficulty | Easy |

## Concepts/Tools Used



## Room Description

This is a fun box where you will get to exploit the system in several ways. Few intended and unintended paths to getting user and root access.

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -p- target.thm

```