# Target: Fawn

- IP Address: 10.129.1.1
- Starting Domain Name: target.htb

## Scope & Goal
- Objective: root.txt
- Constraints: lab

# Recon
- Quick TCP:

```bash
nmap target.htb
Starting Nmap 7.98 ( https://nmap.org ) at 2026-04-08 22:40 -0500
Nmap scan report for target.htb (10.129.99.49)
Host is up (0.060s latency).
Not shown: 999 closed tcp ports (reset)
PORT   STATE SERVICE
21/tcp open  ftp

Nmap done: 1 IP address (1 host up) scanned in 2.93 seconds
```

- Targeted Scan:

```bash
nmap target.htb -sC -sV -A -vv -p21
Starting Nmap 7.98 ( https://nmap.org ) at 2026-04-08 22:42 -0500
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 22:42
Completed NSE at 22:42, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 22:42
Completed NSE at 22:42, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 22:42
Completed NSE at 22:42, 0.00s elapsed
Initiating Ping Scan at 22:42
Scanning target.htb (10.129.99.49) [4 ports]
Completed Ping Scan at 22:42, 0.10s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 22:42
Scanning target.htb (10.129.99.49) [1 port]
Discovered open port 21/tcp on 10.129.99.49
Completed SYN Stealth Scan at 22:42, 0.15s elapsed (1 total ports)
Initiating Service scan at 22:42
Scanning 1 service on target.htb (10.129.99.49)
Completed Service scan at 22:42, 0.18s elapsed (1 service on 1 host)
Initiating OS detection (try #1) against target.htb (10.129.99.49)
Initiating Traceroute at 22:42
Completed Traceroute at 22:42, 0.13s elapsed
Initiating Parallel DNS resolution of 1 host. at 22:42
Completed Parallel DNS resolution of 1 host. at 22:42, 0.50s elapsed
NSE: Script scanning 10.129.99.49.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 22:42
NSE: [ftp-bounce 10.129.99.49:21] PORT response: 500 Illegal PORT command.
Completed NSE at 22:42, 0.77s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 22:42
Completed NSE at 22:42, 0.84s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 22:42
Completed NSE at 22:42, 0.00s elapsed
Nmap scan report for target.htb (10.129.99.49)
Host is up, received echo-reply ttl 63 (0.079s latency).
Scanned at 2026-04-08 22:42:32 CDT for 5s

PORT   STATE SERVICE REASON         VERSION
21/tcp open  ftp     syn-ack ttl 63 vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.15.41
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0              32 Jun 04  2021 flag.txt
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running: Linux 4.X|5.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
OS details: Linux 4.15 - 5.19
TCP/IP fingerprint:
OS:SCAN(V=7.98%E=4%D=4/8%OT=21%CT=%CU=44534%PV=Y%DS=2%DC=T%G=N%TM=69D7202D%
OS:P=x86_64-pc-linux-gnu)SEQ(SP=FC%GCD=1%ISR=102%TI=Z%CI=Z%II=I%TS=A)OPS(O1
OS:=M552ST11NW7%O2=M552ST11NW7%O3=M552NNT11NW7%O4=M552ST11NW7%O5=M552ST11NW
OS:7%O6=M552ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)ECN(R=
OS:Y%DF=Y%T=40%W=FAF0%O=M552NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%R
OS:D=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%
OS:DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%
OS:O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=4
OS:0%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 20.912 days (since Thu Mar 19 00:49:46 2026)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=252 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Unix

TRACEROUTE (using port 21/tcp)
HOP RTT       ADDRESS
1   114.15 ms 10.10.14.1
2   114.21 ms target.htb (10.129.99.49)

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 22:42
Completed NSE at 22:42, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 22:42
Completed NSE at 22:42, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 22:42
Completed NSE at 22:42, 0.00s elapsed
Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 5.35 seconds
           Raw packets sent: 37 (2.414KB) | Rcvd: 27 (1.842KB)
```

- Full TCP:

```bash
nmap target.htb -sC -sV -A -T4 -vv -p-
...
Same as Targeted Scan above
```

## Open Services
- 21/ftp

## FTP Enum
- Tech: vsftpd 3.0.3
- Findings: Nmap has pointed out that it allows anonymous login and that it has the flag.txt file.

## Foothold
- Vector: ftp
- Steps/Commands:

```bash
ftp target.htb                                                                                                                            
Connected to target.htb.
220 (vsFTPd 3.0.3)
Name (target.htb:kwmd): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||15532|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0              32 Jun 04  2021 flag.txt
226 Directory send OK.
ftp> get flag.txt -
remote: flag.txt
229 Entering Extended Passive Mode (|||13046|)
150 Opening BINARY mode data connection for flag.txt (32 bytes).
035db21c881520061c53e0536e44f815226 Transfer complete.
32 bytes received in 00:00 (0.51 KiB/s)
```

- Evidence:

The output above shows the contents of the flag.txt file.

## Flags
- root.txt 035db21c881520061c53e0536e44f815226 (Thu Apr  9 03:46:42 AM UTC 2026)

## Lessons
- What Worked:
- Dead Ends:
- Reusable Commands:
