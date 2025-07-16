# THM: Poster

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/poster/poster.png" alt="Poster" width="90"/> |
| Room | Poster |
| URL | https://tryhackme.com/room/poster |
| Difficulty | Easy |

## Concepts/Tools Used



## Room Description

The sys admin set up a rdbms in a safe way.

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -p- target.thm

```