# nmap

- [Introduction](#introduction)
- [Usage](#usage)
- [Port Scans](#port-scans)
  - [Known Machine IP Address](#known-machine-ip-address)
    - [Initial TCP Scan](#initial-tcp-scan)
    - [UDP Scan](#udp-scan)
- [Firewall Evasion](#firewall-evasion)
  - [Use Decoy IP Addresses](#use-decoy-ip-addresses)
  - [Proxy URL](#proxy-url)
  - [Spoof MAC Address](#spoof-mac-address)
  - [Spoof IP Address](#spoof-ip-address)

## Introduction

Capture the flag events often provide a vulnerable machine's ip address. I need to know what is running on that machine so I can figure out what the next step is when attacking that machine. This is where nmap comes into play. The nmap tool is a very useful tool to find what ports are running on a machine. It can also try to detect the operating system that is running on the machine. I commonly use it to get the name and version of software that is listening on a given port.

## Usage

```bash
$ nmap -h
Nmap 7.80 ( https://nmap.org )
Usage: nmap [Scan Type(s)] [Options] {target specification}
TARGET SPECIFICATION:
  Can pass hostnames, IP addresses, networks, etc.
  Ex: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254
  -iL <inputfilename>: Input from list of hosts/networks
  -iR <num hosts>: Choose random targets
  --exclude <host1[,host2][,host3],...>: Exclude hosts/networks
  --excludefile <exclude_file>: Exclude list from file
HOST DISCOVERY:
  -sL: List Scan - simply list targets to scan
  -sn: Ping Scan - disable port scan
  -Pn: Treat all hosts as online -- skip host discovery
  -PS/PA/PU/PY[portlist]: TCP SYN/ACK, UDP or SCTP discovery to given ports
  -PE/PP/PM: ICMP echo, timestamp, and netmask request discovery probes
  -PO[protocol list]: IP Protocol Ping
  -n/-R: Never do DNS resolution/Always resolve [default: sometimes]
  --dns-servers <serv1[,serv2],...>: Specify custom DNS servers
  --system-dns: Use OS's DNS resolver
  --traceroute: Trace hop path to each host
SCAN TECHNIQUES:
  -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans
  -sU: UDP Scan
  -sN/sF/sX: TCP Null, FIN, and Xmas scans
  --scanflags <flags>: Customize TCP scan flags
  -sI <zombie host[:probeport]>: Idle scan
  -sY/sZ: SCTP INIT/COOKIE-ECHO scans
  -sO: IP protocol scan
  -b <FTP relay host>: FTP bounce scan
PORT SPECIFICATION AND SCAN ORDER:
  -p <port ranges>: Only scan specified ports
    Ex: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9
  --exclude-ports <port ranges>: Exclude the specified ports from scanning
  -F: Fast mode - Scan fewer ports than the default scan
  -r: Scan ports consecutively - don't randomize
  --top-ports <number>: Scan <number> most common ports
  --port-ratio <ratio>: Scan ports more common than <ratio>
SERVICE/VERSION DETECTION:
  -sV: Probe open ports to determine service/version info
  --version-intensity <level>: Set from 0 (light) to 9 (try all probes)
  --version-light: Limit to most likely probes (intensity 2)
  --version-all: Try every single probe (intensity 9)
  --version-trace: Show detailed version scan activity (for debugging)
SCRIPT SCAN:
  -sC: equivalent to --script=default
  --script=<Lua scripts>: <Lua scripts> is a comma separated list of
           directories, script-files or script-categories
  --script-args=<n1=v1,[n2=v2,...]>: provide arguments to scripts
  --script-args-file=filename: provide NSE script args in a file
  --script-trace: Show all data sent and received
  --script-updatedb: Update the script database.
  --script-help=<Lua scripts>: Show help about scripts.
           <Lua scripts> is a comma-separated list of script-files or
           script-categories.
OS DETECTION:
  -O: Enable OS detection
  --osscan-limit: Limit OS detection to promising targets
  --osscan-guess: Guess OS more aggressively
TIMING AND PERFORMANCE:
  Options which take <time> are in seconds, or append 'ms' (milliseconds),
  's' (seconds), 'm' (minutes), or 'h' (hours) to the value (e.g. 30m).
  -T<0-5>: Set timing template (higher is faster)
  --min-hostgroup/max-hostgroup <size>: Parallel host scan group sizes
  --min-parallelism/max-parallelism <numprobes>: Probe parallelization
  --min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>: Specifies
      probe round trip time.
  --max-retries <tries>: Caps number of port scan probe retransmissions.
  --host-timeout <time>: Give up on target after this long
  --scan-delay/--max-scan-delay <time>: Adjust delay between probes
  --min-rate <number>: Send packets no slower than <number> per second
  --max-rate <number>: Send packets no faster than <number> per second
FIREWALL/IDS EVASION AND SPOOFING:
  -f; --mtu <val>: fragment packets (optionally w/given MTU)
  -D <decoy1,decoy2[,ME],...>: Cloak a scan with decoys
  -S <IP_Address>: Spoof source address
  -e <iface>: Use specified interface
  -g/--source-port <portnum>: Use given port number
  --proxies <url1,[url2],...>: Relay connections through HTTP/SOCKS4 proxies
  --data <hex string>: Append a custom payload to sent packets
  --data-string <string>: Append a custom ASCII string to sent packets
  --data-length <num>: Append random data to sent packets
  --ip-options <options>: Send packets with specified ip options
  --ttl <val>: Set IP time-to-live field
  --spoof-mac <mac address/prefix/vendor name>: Spoof your MAC address
  --badsum: Send packets with a bogus TCP/UDP/SCTP checksum
OUTPUT:
  -oN/-oX/-oS/-oG <file>: Output scan in normal, XML, s|<rIpt kIddi3,
     and Grepable format, respectively, to the given filename.
  -oA <basename>: Output in the three major formats at once
  -v: Increase verbosity level (use -vv or more for greater effect)
  -d: Increase debugging level (use -dd or more for greater effect)
  --reason: Display the reason a port is in a particular state
  --open: Only show open (or possibly open) ports
  --packet-trace: Show all packets sent and received
  --iflist: Print host interfaces and routes (for debugging)
  --append-output: Append to rather than clobber specified output files
  --resume <filename>: Resume an aborted scan
  --stylesheet <path/URL>: XSL stylesheet to transform XML output to HTML
  --webxml: Reference stylesheet from Nmap.Org for more portable XML
  --no-stylesheet: Prevent associating of XSL stylesheet w/XML output
MISC:
  -6: Enable IPv6 scanning
  -A: Enable OS detection, version detection, script scanning, and traceroute
  --datadir <dirname>: Specify custom Nmap data file location
  --send-eth/--send-ip: Send using raw ethernet frames or IP packets
  --privileged: Assume that the user is fully privileged
  --unprivileged: Assume the user lacks raw socket privileges
  -V: Print version number
  -h: Print this help summary page.
EXAMPLES:
  nmap -v -A scanme.nmap.org
  nmap -v -sn 192.168.0.0/16 10.0.0.0/8
  nmap -v -iR 10000 -Pn -p 80
SEE THE MAN PAGE (https://nmap.org/book/man.html) FOR MORE OPTIONS AND EXAMPLES
```

## Port Scans

### Unknown Machine IP Address

When doing a capture the flag event with a VulnHub machine, I will need to discover the ip address of the machine. In my home lab I restrict the ip addresses of the machines to a range (for example 10.22.1.110-130). When I start up the VulnHub machine I need to find out what the ip address it is using. I already know that my attack machine is using 10.22.1.110. I run the following command to see the other machines with ip addresses:

```bash
$ nmap -sS 10.22.1.111-130
```

Whatever ip address shows up in the results is the machine that I just imported from VulnHub.

### Known Machine IP Address

#### Initial TCP Scan

In a capture the flag event I usually run the following scan. I am using the hostname target.thm for this and future examples. Here is the command I run:

```bash
$ nmap -T4 -n -sC -sV -Pn -v -p- target.thm
```

This command does the following things:

- The `-T4` option will cause nmap to run the scan at one of the fastest levels.
- The `-n` option tells nmap to never resolve the DNS.
- The `-sC` option is used to do a default script scan.
- The `-sV` option probes any open ports to determine the service and version info.
- The `-Pn` option tells nmap to skip host discovery.
- The `-v` option tells nmap that I want verbose output from this scan.
- The `-p-` option tells nmap to scan all ports.

Here is some sample output from the above command when port 22 and 80 were found open on the target machine:

```bash
$ nmap -T4 -n -sC -sV -Pn -v -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-06-23 19:38 BST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 19:38
Completed NSE at 19:38, 0.00s elapsed
Initiating NSE at 19:38
Completed NSE at 19:38, 0.00s elapsed
Initiating NSE at 19:38
Completed NSE at 19:38, 0.00s elapsed
Initiating ARP Ping Scan at 19:38
Scanning target.thm (10.10.232.89) [1 port]
Completed ARP Ping Scan at 19:38, 0.04s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 19:38
Scanning target.thm (10.10.232.89) [65535 ports]
Discovered open port 80/tcp on 10.10.232.89
Discovered open port 25/tcp on 10.10.232.89
Discovered open port 55006/tcp on 10.10.232.89
Discovered open port 55007/tcp on 10.10.232.89
Completed SYN Stealth Scan at 19:38, 2.19s elapsed (65535 total ports)
Initiating Service scan at 19:38
Scanning 4 services on target.thm (10.10.232.89)
Completed Service scan at 19:39, 26.54s elapsed (4 services on 1 host)
NSE: Script scanning 10.10.232.89.
Initiating NSE at 19:39
Completed NSE at 19:39, 7.21s elapsed
Initiating NSE at 19:39
Completed NSE at 19:40, 74.02s elapsed
Initiating NSE at 19:40
Completed NSE at 19:40, 0.00s elapsed
Nmap scan report for target.thm (10.10.232.89)
Host is up (0.00031s latency).
Not shown: 65531 closed ports
PORT      STATE SERVICE     VERSION
25/tcp    open  smtp        Postfix smtpd
|_smtp-commands: ubuntu, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, 
|_ssl-date: TLS randomness does not represent time
80/tcp    open  http        Apache httpd 2.4.7 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: GoldenEye Primary Admin Server
55006/tcp open  ssl/unknown
|_ssl-date: TLS randomness does not represent time
55007/tcp open  pop3        Dovecot pop3d
|_pop3-capabilities: UIDL RESP-CODES PIPELINING CAPA AUTH-RESP-CODE USER STLS SASL(PLAIN) TOP
|_ssl-date: TLS randomness does not represent time
MAC Address: 02:6E:1B:13:75:85 (Unknown)

NSE: Script Post-scanning.
Initiating NSE at 19:40
Completed NSE at 19:40, 0.00s elapsed
Initiating NSE at 19:40
Completed NSE at 19:40, 0.00s elapsed
Initiating NSE at 19:40
Completed NSE at 19:40, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 110.86 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 65536 (2.621MB)
```

If there are no ports open from the previous scan I will try a UDP scan. I have included that scan below.

I cut out some of the output to show some of the important parts of this scan. There are a lot of good things happening with this scan. Nmap is guessing the operating system, doing a traceroute and discovering the service and version number for ports 25, 80, 55006 and  55007. Based on the services that are running from the results, I start looking up vulnerabilities and manually check the services.

#### UDP Scan

If there are no ports open from the original TCP scan that I mentioned above, I'll try a UDP scan. A full UDP scan is significantly slower than a TCP scan. Here is the command I use for a UDP scan:

```bash
$ nmap -p- -sU -Pn -T5 -v target.thm
```

This command is the same as the [original known machine ip address scan](#original-tcp-scan) command above except the `-sU` option has been added to let nmap know I want a UDP scan instead.

## Firewall Evasion

An nmap scan can be frustrated by a firewall. Firewalls can filter traffic based on a large range of criteria. Fortunately nmap has options that can be used to get information about open ports on machines. Some of the criteria that a firewall filters on include:

- Protocol
- Source Address
- MAC Address

I will provide examples below that use the following information:

- The target is located at `10.10.10.10`.
- Nmap is running a SYN scan (`-sS`).
- I want to skip host discovery checks (`-Pn`).
- I want to check the first 100 ports (`-F`).

Here are some of the nmap options that help evade a firewall so that a target machine can get scanned:

### Use Decoy IP Addresses

As mentioned above a firewall might block traffic to a machine if it is coming from the wrong source ip address. The nmap tool has the `-D` option that can be used to source ip addresses that act as a decoy. I can specify the decoy addresses that I would like to use and what order I want them sent. I can also have nmap generate a decoy ip address for me. Here are some examples:

| Command | Explaination |
| --- | --- |
| `nmap -sS -Pn -F -D 10.10.1.1,192.168.1.1,ME 10.10.10.10` | The command is including two decoy ip addresses (`10.10.1.1` and `192.168.1.1`). The `ME` part of the decoy addresses is my machine's ip address. The scans will start with the `10.10.1.1` ip address and then use `192.168.1.1` and then finish with my ip address. |
| `nmap -sS -Pn -F -D 10.10.1.1,192.168.1.1 10.10.10.10` | This is the same command as the one before except I didn't specify where in the decoy ordering my ip address should go. Nmap will pick when it gets ran for me. |
| `nmap -sS -Pn -F -D RND,10.10.1.1,ME 10.10.10.10` | This command will generate a random ip address and then run `10.10.1.1` before finishing with my ip address. |
| `nmap -sS -Pn -F -D RND,10.10.1.1 10.10.10.10` | This command is the same as the previous command except my ip address will be ran randomly between the three decoy addresses. |
| `nmap -sS -Pn -F -D RND,RND,ME,RND 10.10.10.10` | This command runs two random ip addresses before running my ip address and then finishing with another random ip address. |

### Proxy URL

I can also run my scan from behind a proxy. I just need to specify the proxy address with the `--proxies` flag. Multiple proxies can be specified. Here is an example that uses `10.200.20.3` as the proxy address:

```bash
$ nmap -sS -Pn -F --proxies 10.200.20.3 10.10.10.10
```

### Spoof MAC Address

I can spoof the MAC address of my source machine with the `--spoof-mac` flag. Here is an example that specifies a MAC address for a network interface card that was developed by Dell:

```bash
$ nmap -sS -Pn -F --spoof-mac Dell 10.10.10.10
```

#### Common Spoof MAC Address Values

| Value | Description |
| --- | --- |
| 0 | Random MAC address (fully random). |
| apple | Apple, Inc. |
| cisco | Cisco Systems. |
| juniper | Juniper Networks. |
| intel | Intel Corporation. |
| microsoft | Microsoft. |
| vmware | VMware, Inc. |
| xerox | Xerox Corporation. |
| oracle | Oracle Corporation. |
| ibm | IBM. |
| hp | Hewlett-Packard. |
| netgear | NETGEAR. |
| belkin | Belkin International. |
| nintendo | Nintendo. |
| sony | Sony. |
| samsung | Samsung Electronics. |
| huawei | Huawei Technologies. |
| xiaomi | Xiaomi. |
| alcatel | Alcatel. |
| dell | Dell Inc. |

### Spoof IP Address

I can also spoof the ip address of my source machine with the `-S` flag. Here is an example that uses `192.168.1.17` as the spoofed ip address:

```bash
$ nmap -sS -Pn -F -S 192.168.1.17 10.10.10.10
```


