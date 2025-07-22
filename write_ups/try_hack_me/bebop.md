# THM: Bebop

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/bebop/bebop.jpeg" alt="Bebop" width="90"/> |
| Room | Bebop |
| URL | https://tryhackme.com/room/bebop |
| Difficulty | Easy |

## Concepts/Tools Used

- telnet

## Room Description

Who thought making a flying shell was a good idea?

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -v -p- target.thm

```
