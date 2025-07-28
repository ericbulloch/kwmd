# THM: VulnNet: Node

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/vuln_net_node/vuln_net_node.png" alt="VulnNet: Node" width="90"/> |
| Room | VulnNet: Node |
| URL | https://tryhackme.com/room/vulnnetnode |
| Difficulty | Easy |

## Concepts/Tools Used



## Room Description

After the previous breach, VulnNet Entertainment states it won't happen again. Can you prove they're wrong?

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -p- target.thm

```
