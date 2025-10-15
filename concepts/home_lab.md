# Home Lab

- [Introduction](#introduction)
- [Regular Lab](#regular-lab)
- [Bug Bountry Hunting](#bug-bounty-hunting)
- [TryHackMe](#tryhackme)
- [Hack The Box](#hack-the-box)

## Introduction

Part of learning cybersecurity is taking steps to learn it safely. A home lab is a great way to try defending like a member of the blue team and also attacking like a member of the red team. A home lab can be very simple like a single machine that acts as a sandbox. I recommend having any target machines in their own segmented network from the host and the host's network that doesn't have internet access.

Home labs are a great way to get hands on experience and try out things that are taught on sites like [TryHackMe](https://tryhackme.com), [Hack The Box](https://hackthebox.com), and [Let's Defend](https://letsdefend.io).

Here are the scripts that I use to setup my home lab:

- [Create Network](home_lab/create_network.sh)
- [Create Attack Box](home_lab/create_attacker.sh)
- [Sample Mr Robot Target Box](home_lab/create_mr_robot_target.sh)

## Regular Lab

My home lab setup is very simple. Here are the details:

- I use VirtualBox for tooling.
- My host machine is Ubuntu.
- I have created a network called targets. This network does not have access to the internet.
- All the target machine are on the target network so that they can be hacked without having a connection to the internet.
- I have a Kali Linux box as an attack machine that has a NAT connection to my host machine so that it has access to the internet but not my host machine or the host's network. It also has a nic that is on the targets network so that it can connect to the different target machines.

## Bug Bounty Hunting

I also have a Kali Linux virtual machine that I use for bug bounty hunting. It also uses the NAT connection but does not connect to any other network.

## TryHackMe

Currently, I connect to the TryHackMe machines from the browser. I plan to make the switch using the same setup as the bug bounty hunting machine above.

## Hack The Box

I plan to start Hack The Box in the next few months. When I do start using it, I will use a machine like the ones described above.
