# THM: ColddBox: Easy

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/coldd_box_easy/coldd_box_easy.png" alt="ColddBox: Easy" width="90"/> |
| Room | ColddBox: Easy |
| URL | https://tryhackme.com/room/colddboxeasy |
| Difficulty | Easy |

## Concepts/Tools Used



## Room Description

An easy level machine with multiple ways to escalate privileges. By Hixec.

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -p- target.thm

```