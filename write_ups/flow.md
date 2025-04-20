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

### Known Machine IP Address

In a capture the flag event I usually run a port scan in 2 parts. I am using the same hostname that I mentioned earlier (target.thm). The first command I run is:

`nmap -p- -Pn -T5 -v target.thm`

This command does the following things:

- The `-p-` option tells nmap to scan all ports.
- The `-Pn` option tells nmap to skip host discovery.
- The `-T5` option will cause nmap to run the scan at one of the fastest levels (insane speed).
- The `-v` option tells nmap that I want verbose output from this scan.

Once this scan is complete and we have some ports that are reported as being up, I will run another command. For this example I will say that port 22 and 80 were up on the target machine. I run the following command to get more information for those ports:

`nmap -p 22,80 -A -Pn -v target.thm`

This command does the following:

- The `-p 22,80` option tells nmap to scan ports 22 and 80.
- The `-A` option tells nmap to try operating system detection, version detection, script scanning and also perform a traceroute.
- The `-Pn` option tells nmap to skip host discovery.
- The `-v` option tells nmap that I want verbose output from this scan.
