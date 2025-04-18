| Stat      | Value                                        |
| --------- | -------------------------------------------- |
| Room      | MR-ROBOT: 1                                  |
| URL       | https://www.vulnhub.com/entry/mr-robot-1,151 |
| Difficult | Easy                                         |

## Concepts/Tools Used

- nmap
- Burp Suite
- dirb
- hydra
- netcat
- SUID/GTFOBins
- CrackStation

## Description

This was the first capture the flag challenge that I tried. I have never watched the show Mr. Robot before so most of the references are lost on me. The challenge follows the standard flow of scanning, looking for vulnerabilites and then exploiting them. I was learning what needs to be done while I was doing this capture the flag challenge. I would come up with ideas and run them, once I got stuck I started to watch videos to get ideas on what other people did.

### Process

I imported the virtual machine image into virtual box and booted it up. There is a login screen but I don't have a username or password. I tried admin/admin and root/root but that didn't work.

From here I knew that I needed to get the ip address of the machine so that I could scan it and find out what services were on the machine. When I setup my home lab I limited the ip addresses to the range of 10.22.1.110-130. So I ran the following command to find the machine:

`nmap -sS 10.22.1.110-130`

It provided output for 2 machines. One of the machines was mine (10.22.1.110) so I ignored the output from that machine. The other machine was the target machine. The machine has 3 ports open:

- 22/tcp
- 80/tcp
- 443/tcp

I can use a password to ssh onto the machine since a password prompt showed up when I ran the following command:

`ssh 10.22.1.112`

This lets me know that I can try to brute force login with hydra if I find a username.

Since I don't have much other information, I opened up Firefox and checked out the website that was running on the target machine.
