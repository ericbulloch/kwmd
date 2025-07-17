# THM: Chocolate Factory

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/chocolate_factory/chocolate_factory.jpeg" alt="Chocolate Factory" width="90"/> |
| Room | Chocolate Factory |
| URL | https://tryhackme.com/room/chocolatefactory |
| Difficulty | Easy |

## Concepts/Tools Used



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
