# THM: GLITCH

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/glitch/glitch.jpeg" alt="GLITCH" width="90"/> |
| Room | GLITCH |
| URL | https://tryhackme.com/room/glitch |
| Difficulty | Easy |

## Concepts/Tools Used



## Room Description

Challenge showcasing a web app and simple privilege escalation. Can you find the glitch?

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -p- target.thm

```
