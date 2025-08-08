# THM: VulnNet: Internal

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/vuln_net_internal/vuln_net_internal.png" alt="VulnNet: Internal" width="90"/> |
| Room | VulnNet: Internal |
| URL | https://tryhackme.com/room/vulnnetinternal |
| Difficulty | Easy |

## Concepts/Tools Used



## Room Description

VulnNet Entertainment learns from its mistakes, and now they have something new for you...

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -v -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-26 00:10 BST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 00:10
Completed NSE at 00:10, 0.00s elapsed
Initiating NSE at 00:10
Completed NSE at 00:10, 0.00s elapsed
Initiating NSE at 00:10
Completed NSE at 00:10, 0.00s elapsed
Initiating ARP Ping Scan at 00:10
Scanning target.thm (10.10.98.81) [1 port]
Completed ARP Ping Scan at 00:10, 0.04s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 00:10
Scanning target.thm (10.10.98.81) [65535 ports]
Discovered open port 139/tcp on 10.10.98.81
Discovered open port 22/tcp on 10.10.98.81
Discovered open port 445/tcp on 10.10.98.81
Discovered open port 111/tcp on 10.10.98.81
Discovered open port 36069/tcp on 10.10.98.81
Discovered open port 6379/tcp on 10.10.98.81
Discovered open port 50353/tcp on 10.10.98.81
Discovered open port 60877/tcp on 10.10.98.81
Discovered open port 873/tcp on 10.10.98.81
Discovered open port 2049/tcp on 10.10.98.81
Discovered open port 55525/tcp on 10.10.98.81
Discovered open port 44401/tcp on 10.10.98.81
Completed SYN Stealth Scan at 00:10, 3.26s elapsed (65535 total ports)
Initiating Service scan at 00:10
Scanning 12 services on target.thm (10.10.98.81)
Completed Service scan at 00:11, 16.02s elapsed (12 services on 1 host)
NSE: Script scanning 10.10.98.81.
Initiating NSE at 00:11
Completed NSE at 00:11, 0.44s elapsed
Initiating NSE at 00:11
Completed NSE at 00:11, 0.03s elapsed
Initiating NSE at 00:11
Completed NSE at 00:11, 0.00s elapsed
Nmap scan report for target.thm (10.10.98.81)
Host is up (0.00015s latency).
Not shown: 65522 closed ports
PORT      STATE    SERVICE     VERSION
22/tcp    open     ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
111/tcp   open     rpcbind     2-4 (RPC #100000)
| rpcinfo:
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      34514/udp   mountd
|   100005  1,2,3      47793/udp6  mountd
|   100005  1,2,3      57653/tcp6  mountd
|   100005  1,2,3      60877/tcp   mountd
|   100021  1,3,4      36069/tcp   nlockmgr
|   100021  1,3,4      44047/tcp6  nlockmgr
|   100021  1,3,4      49357/udp6  nlockmgr
|   100021  1,3,4      53730/udp   nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
139/tcp   open     netbios-ssn Samba smbd 4.6.2
445/tcp   open     netbios-ssn Samba smbd 4.6.2
873/tcp   open     rsync       (protocol version 31)
2049/tcp  open     nfs_acl     3 (RPC #100227)
6379/tcp  open     redis       Redis key-value store
9090/tcp  filtered zeus-admin
36069/tcp open     nlockmgr    1-4 (RPC #100021)
44401/tcp open     java-rmi    Java RMI
50353/tcp open     mountd      1-3 (RPC #100005)
55525/tcp open     mountd      1-3 (RPC #100005)
60877/tcp open     mountd      1-3 (RPC #100005)
MAC Address: 02:5C:19:6C:30:3B (Unknown)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: -1s
| nbstat: NetBIOS name: IP-10-10-98-81, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   IP-10-10-98-81<00>   Flags: <unique><active>
|   IP-10-10-98-81<03>   Flags: <unique><active>
|   IP-10-10-98-81<20>   Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|_  WORKGROUP<1e>        Flags: <group><active>
| smb2-security-mode:
|   2.02:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2025-07-25T23:11:09
|_  start_date: N/A

NSE: Script Post-scanning.
Initiating NSE at 00:11
Completed NSE at 00:11, 0.00s elapsed
Initiating NSE at 00:11
Completed NSE at 00:11, 0.00s elapsed
Initiating NSE at 00:11
Completed NSE at 00:11, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 21.10 seconds
           Raw packets sent: 65537 (2.884MB) | Rcvd: 65535 (2.621MB)
```
