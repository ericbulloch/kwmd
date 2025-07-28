# THM: VulnNet: Internal

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/vuln_net_internal/vuln_net_internal.png" alt="VulnNet: Internal" width="90"/> |
| Room | VulnNet: Internal |
| URL | https://tryhackme.com/room/vulnnetinternal |
| Difficulty | Easy |

## Concepts/Tools Used



## Room Description

VulnNet Entertainment learns from its mistakes, and now they have something new for you...

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -p- target.thm

```
