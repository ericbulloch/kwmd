# Hacking Flow

I wanted to document what I normally do when hacking in a capture the flag event. Some of the points will be for situation and times when services are enabled. There is a general flow that I follow in the beginning. I use this document as a reference while I work on a capture the flag event.

## Starting

Unless the instructions tell me that I have a specific hostname that I must use, I will often change the ip address of the machine to a hostname that is more favorable. For example, if I am working on a capture the flag on TryHackMe and they provide a machine with an ip address of something like 10.10.160.54, I will add an entry to my /etc/hosts file. In this example I will run the following:

`echo "10.10.160.54  target.thm" >> /etc/hosts`

I do this so that I don't have to remember the ip address of the machine that I am attacking in the capture the flag event. I have less to remember and so I can focus more on what I am trying to do.

## Port Scan

### Unknown Machine IP Address

When doing a capture the flag event with a VulnHub machine, I will need to discover the ip address of the machine. In my home lab I restrict the ip addresses of the machines to a range (for example 10.22.1.110-130). When I start up the VulnHub machine I need to find out what the ip address it is using. I already know that my attack machine is using 10.22.1.110. I run the following command to see the other machines with ip addresses:

`nmap -sS 10.22.1.111-130`

Whatever ip address shows up in the results is the machine that I just imported from VulnHub.
