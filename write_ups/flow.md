# Hacking Flow

I wanted to document what I normally do when hacking in a capture the flag event. Some of the points will be for situation and times when services are enabled. There is a general flow that I follow in the beginning. I use this document as a reference while I work on a capture the flag event.

## Starting

Unless the instructions tell me that I have a specific hostname that I must use, I will often change the ip address of the machine to a hostname that is more favorable. For example, if I am working on a capture the flag on TryHackMe and they provide a machine with an ip address of something like 10.10.160.54, I will add an entry to my /etc/hosts file. In this example I will run the following:

`echo "10.10.160.54  target.thm" >> /etc/hosts`

I do this so that I don't have to remember the ip address of the machine that I am attacking in the capture the flag event. I have less to remember and so I can focus more on what I am trying to do.

# Port Scanning

## Unknown Machine IP Address

When doing a capture the flag event with a VulnHub machine, I will need to discover the ip address of the machine. In my home lab I restrict the ip addresses of the machines to a range (for example 10.22.1.110-130). When I start up the VulnHub machine I need to find out what the ip address it is using. I already know that my attack machine is using 10.22.1.110. I run the following command to see the other machines with ip addresses:

`nmap -sS 10.22.1.111-130`

Whatever ip address shows up in the results is the machine that I just imported from VulnHub.

## Known Machine IP Address

### Original TCP Scan

In a capture the flag event I usually run a port scan in 2 parts. I am using the same hostname that I mentioned earlier (target.thm). The first command I run is:

`nmap -p- -Pn -T5 -v target.thm`

This command does the following things:

- The `-p-` option tells nmap to scan all ports.
- The `-Pn` option tells nmap to skip host discovery.
- The `-T5` option will cause nmap to run the scan at one of the fastest levels (insane speed).
- The `-v` option tells nmap that I want verbose output from this scan.

Here is some sample output from the above command when port 22 and 80 were found open on the target machine:

```bash
Starting Nmap 7.80 ( https://nmap.org ) at 2025-04-21 15:30 BST
Initiating ARP Ping Scan at 15:30
Scanning target.thm (10.10.7.168) [1 port]
Completed ARP Ping Scan at 15:30, 0.03s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 15:30
Scanning target.thm (10.10.7.168) [65535 ports]
Discovered open port 22/tcp on 10.10.7.168
Discovered open port 80/tcp on 10.10.7.168
Completed SYN Stealth Scan at 15:30, 1.81s elapsed (65535 total ports)
Nmap scan report for target.thm (10.10.7.168)
Host is up (0.00012s latency).
Not shown: 65533 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
MAC Address: 02:42:CD:52:D4:57 (Unknown)

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 2.02 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 65536 (2.621MB)
```

Notice how fast this scan is with the `-T5` option (1.81 seconds to scan 65535 ports). If there are no ports open from the previous scan I will try a UDP scan. I have included that scan below.

### Second TCP Scan

Once this scan is complete and I have some ports that are reported as being up, I will run another command. I scan ports 22 and 80 from the previous output and get more information about the services running on thos ports. I run the following command to get more information for those ports:

`nmap -p 22,80 -A -Pn -v target.thm`

This command does the following:

- The `-p 22,80` option tells nmap to scan ports 22 and 80.
- The `-A` option tells nmap to try operating system detection, version detection, script scanning and also perform a traceroute.
- The `-Pn` option tells nmap to skip host discovery.
- The `-v` option tells nmap that I want verbose output from this scan.

Here is some sample output from this command:

```bash
Starting Nmap 7.80 ( https://nmap.org ) at 2025-04-21 15:37 BST
...
Host is up (0.00034s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: My Super Amazing Website!
MAC Address: 02:42:CD:52:D4:57 (Unknown)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), Linux 3.10 - 3.13 (94%), Linux 3.8 (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 2.6.32 (92%), Linux 2.6.39 - 3.2 (92%), Linux 3.1 - 3.2 (92%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 6.032 days (since Tue Apr 15 14:51:39 2025)
Network Distance: 1 hop
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.34 ms target.thm (10.10.7.168)

NSE: Script Post-scanning.
Initiating NSE at 15:37
Completed NSE at 15:37, 0.00s elapsed
Initiating NSE at 15:37
Completed NSE at 15:37, 0.00s elapsed
Initiating NSE at 15:37
Completed NSE at 15:37, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.12 seconds
           Raw packets sent: 47 (3.672KB) | Rcvd: 31 (2.616KB)
```

I cut out some of the output to show some of the important parts of this scan. There are a lot of good things happening with this scan. Nmap is guessing the operating system, doing a traceroute and discovering the service and version number for ports 22 and 80. Based on the services that are running from the results I now move on to the next segment.

### UDP Scan

If there are no ports open from the original TCP scan that I mentioned above, I'll try a UDP scan. A full UDP scan is significantly slower than a TCP scan. Here is the command I use for a UDP scan:

`nmap -p- -sU -Pn -T5 -v target.thm`

This command is the same as the original known machine ip address scan command above except the `-sU` option has been added to let nmap know I want a UDP scan instead.

# Website

This section will most likely be its own file instead of just a section for right now. For now I am just starting with the process.

## Browsing

In a capture the flag event I am looking at the different pages and trying to find forms and input fields. Each one of these is an attack vector that can be used to do things like SQL injection or a XSS attack. Mapping the site is one of the first things I do while running directory enumeration on a website.

## Inpecting HTML

Capture the flag events often have flags in the comments of the HTML. I have found flags, usernames, passwords, directories and links that my automated runs didn't find. This is a very overlooked way to find useful things when I get stuck.

# SSH

## Initial Information

If nmap shows that ssh is running on a machine, I will manually connect to it. I am trying to see if it asks for a password. If that is the case, this is another attack vector I can use if I can find a username on the server.

If the password prompt did not show up and I got an error that says "Permission denied (publickey)", my attack vector got smaller.

Also, sometimes I need to connect to ssh on a different port. This involves using the `-p` option. If I need to connect on port 2222 I would run the following command:

`ssh -p 2222 user@target.thm`

# Stable Shell

Once I have connected to the target machine with netcat, getting a stable shell is my main priority. There are a few different ways to do this, here are the ones that I use.

## Python PTY

If python is on the machine this is my preferred method. There are 4 steps and then I will have a stable shell. The steps are:

- Run the command: `python3 -c 'import pty;pty.spawn("/bin/bash")'`. This creates a new process that runs bash in a pseudo-terminal (pty).
- Run the command: `export TERM=xterm`. This sets the terminal emulator to xterm. This is the default setting for Ubuntu.
- Move your shell session to the background by hitting `^Z` (ctrl+Z). I need to run one more command and this process needs to be in the background.
- Run the command: `stty raw -echo; fg`. This disables the raw input and output and just sends it straight through.
