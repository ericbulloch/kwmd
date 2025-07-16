# THM: Chocolate Factory

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/chocolate_factory/chocolate_factory.jpeg" alt="Chocolate Factory" width="90"/> |
| Room | Chocolate Factory |
| URL | https://tryhackme.com/room/chocolatefactory |
| Difficulty | Easy |

## Concepts/Tools Used



## Room Description

A Charlie And The Chocolate Factory themed room, revisit Willy Wonka's chocolate factory!

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -p- target.thm

```