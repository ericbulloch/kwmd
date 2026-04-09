# Target: Redeemer

- IP Address: 10.129.100.173
- Starting Domain Name: target.htb

## Scope & Goal
- Objective: flag key of redis
- Constraints: lab

# Recon
- Quick TCP:

```bash
$ nmap target.htb                    
Starting Nmap 7.98 ( https://nmap.org ) at 2026-04-09 13:15 -0400
Nmap scan report for target.htb (10.129.100.173)
Host is up (0.066s latency).
All 1000 scanned ports on target.htb (10.129.100.173) are in ignored states.
Not shown: 1000 closed tcp ports (reset)

Nmap done: 1 IP address (1 host up) scanned in 1.32 seconds
```

- Full TCP:

```bash
$ nmap target.htb -sV -sC -A -T4 -p- -vv
Starting Nmap 7.98 ( https://nmap.org ) at 2026-04-09 13:16 -0400
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:16
Completed NSE at 13:16, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:16
Completed NSE at 13:16, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:16
Completed NSE at 13:16, 0.00s elapsed
Initiating Ping Scan at 13:16
Scanning target.htb (10.129.100.173) [4 ports]
Completed Ping Scan at 13:16, 0.08s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 13:16
Scanning target.htb (10.129.100.173) [65535 ports]
Discovered open port 6379/tcp on 10.129.100.173
SYN Stealth Scan Timing: About 40.85% done; ETC: 13:17 (0:00:45 remaining)
Increasing send delay for 10.129.100.173 from 0 to 5 due to max_successful_tryno increase to 5
Increasing send delay for 10.129.100.173 from 5 to 10 due to 11 out of 20 dropped probes since last increase.
SYN Stealth Scan Timing: About 44.08% done; ETC: 13:18 (0:01:17 remaining)
Stats: 0:01:31 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 47.90% done; ETC: 13:19 (0:01:38 remaining)
SYN Stealth Scan Timing: About 52.05% done; ETC: 13:20 (0:01:53 remaining)
Warning: 10.129.100.173 giving up on port because retransmission cap hit (6).
SYN Stealth Scan Timing: About 56.28% done; ETC: 13:20 (0:02:08 remaining)
SYN Stealth Scan Timing: About 71.71% done; ETC: 13:22 (0:01:56 remaining)
SYN Stealth Scan Timing: About 78.63% done; ETC: 13:23 (0:01:35 remaining)
SYN Stealth Scan Timing: About 84.53% done; ETC: 13:23 (0:01:12 remaining)
SYN Stealth Scan Timing: About 90.14% done; ETC: 13:24 (0:00:48 remaining)
Completed SYN Stealth Scan at 13:24, 516.88s elapsed (65535 total ports)
Initiating Service scan at 13:24
Scanning 1 service on target.htb (10.129.100.173)
Completed Service scan at 13:24, 6.15s elapsed (1 service on 1 host)
Initiating OS detection (try #1) against target.htb (10.129.100.173)
Initiating Traceroute at 13:24
Completed Traceroute at 13:24, 0.07s elapsed
Initiating Parallel DNS resolution of 1 host. at 13:24
Completed Parallel DNS resolution of 1 host. at 13:24, 0.50s elapsed
NSE: Script scanning 10.129.100.173.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:24
Completed NSE at 13:24, 0.14s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:24
Completed NSE at 13:24, 0.02s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:24
Completed NSE at 13:24, 0.02s elapsed
Nmap scan report for target.htb (10.129.100.173)
Host is up, received echo-reply ttl 63 (0.059s latency).
Scanned at 2026-04-09 13:16:05 EDT for 525s
Not shown: 65494 closed tcp ports (reset)
PORT      STATE    SERVICE REASON         VERSION
4399/tcp  filtered unknown no-response
6379/tcp  open     redis   syn-ack ttl 63 Redis key-value store 5.0.7
9151/tcp  filtered unknown no-response
9834/tcp  filtered unknown no-response
9937/tcp  filtered unknown no-response
11363/tcp filtered unknown no-response
12434/tcp filtered unknown no-response
14660/tcp filtered unknown no-response
14797/tcp filtered unknown no-response
16164/tcp filtered unknown no-response
16210/tcp filtered unknown no-response
18628/tcp filtered unknown no-response
22178/tcp filtered unknown no-response
22990/tcp filtered unknown no-response
24937/tcp filtered unknown no-response
25296/tcp filtered unknown no-response
27871/tcp filtered unknown no-response
28930/tcp filtered unknown no-response
29078/tcp filtered unknown no-response
35889/tcp filtered unknown no-response
36202/tcp filtered unknown no-response
37672/tcp filtered unknown no-response
37954/tcp filtered unknown no-response
38591/tcp filtered unknown no-response
39727/tcp filtered unknown no-response
43861/tcp filtered unknown no-response
44472/tcp filtered unknown no-response
44859/tcp filtered unknown no-response
46893/tcp filtered unknown no-response
48577/tcp filtered unknown no-response
49024/tcp filtered unknown no-response
49486/tcp filtered unknown no-response
49599/tcp filtered unknown no-response
51922/tcp filtered unknown no-response
53202/tcp filtered unknown no-response
53304/tcp filtered unknown no-response
57132/tcp filtered unknown no-response
60096/tcp filtered unknown no-response
60606/tcp filtered unknown no-response
60701/tcp filtered unknown no-response
63145/tcp filtered unknown no-response
Device type: general purpose|router
Running: Linux 4.X|5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 4.15 - 5.19, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
TCP/IP fingerprint:
OS:SCAN(V=7.98%E=4%D=4/9%OT=6379%CT=1%CU=43606%PV=Y%DS=2%DC=T%G=Y%TM=69D7E0
OS:E2%P=x86_64-pc-linux-gnu)SEQ(SP=102%GCD=1%ISR=106%TI=Z%CI=Z%II=I%TS=A)OP
OS:S(O1=M552ST11NW7%O2=M552ST11NW7%O3=M552NNT11NW7%O4=M552ST11NW7%O5=M552ST
OS:11NW7%O6=M552ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)EC
OS:N(R=Y%DF=Y%T=40%W=FAF0%O=M552NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=
OS:AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(
OS:R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%
OS:F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N
OS:%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%C
OS:D=S)

Uptime guess: 47.231 days (since Sat Feb 21 06:52:43 2026)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=258 (Good luck!)
IP ID Sequence Generation: All zeros

TRACEROUTE (using port 993/tcp)
HOP RTT      ADDRESS
1   57.95 ms 10.10.14.1
2   56.95 ms target.htb (10.129.100.173)

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:24
Completed NSE at 13:24, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:24
Completed NSE at 13:24, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:24
Completed NSE at 13:24, 0.00s elapsed
Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 527.15 seconds
           Raw packets sent: 70592 (3.108MB) | Rcvd: 68511 (2.742MB)
```

## Open Services
- 6379/redis

## Web Enum
- Tech: Redis key-value store 5.0.7
- Findings:

```bash
$ redis-cli -h target.htb
target.htb:6379> scan 0
1) "0"
2) 1) "flag"
   2) "temp"
   3) "numb"
   4) "stor"
target.htb:6379> get "flag"
"03e1d2b376c37ab3f5319922053953eb"
```

The `scan 0` command is used to show all the keys in Redis.

## Flags
- flag: `03e1d2b376c37ab3f5319922053953eb` (Thu Apr  9 05:32:40 PM UTC 2026)

## Lessons
- What Worked: Full TCP scan
- Dead Ends: The quick scan didn't find anything and so a full TCP scan was needed
- Reusable Commands:

```bash
redis-cli -h target.htb

# in redis terminal:
scan 0
get key
```
