# nmap

- [Introduction](#introduction)
- [Flags](#flags)
- [Update The Script Database](#update-the-script-database)
- [Port Scans](#port-scans)
  - [Known Machine IP Address](#known-machine-ip-address)
    - [Initial TCP Scan](#initial-tcp-scan)
    - [UDP Scan](#udp-scan)
- [Firewall Evasion](#firewall-evasion)
  - [Use Decoy IP Addresses](#use-decoy-ip-addresses)
  - [Proxy URL](#proxy-url)
  - [Spoof MAC Address](#spoof-mac-address)
    - [Common Spoof MAC Address Values](#common-spoof-mac-address-values)
  - [Spoof IP Address](#spoof-ip-address)
  - [Specify Source Port Number](#specify-source-port-number)
  - [Fragment Packets](#fragment-packets)
  - [Specify TCP Segment](#specify-tcp-segment)
  - [Specify Time-To-Live](#specify-time-to-live)
  - [Bad Checksum](#bad-checksum)

## Introduction

Capture the flag events often provide a vulnerable machine's ip address. I need to know what is running on that machine so I can figure out what the next step is when attacking that machine. This is where nmap comes into play. The nmap tool is a very useful tool to find what ports are running on a machine. It can also try to detect the operating system that is running on the machine. I commonly use it to get the name and version of software that is listening on a given port.

Things nmap does well:

- Live host discovery
- Open port identification
- Service/version detection
- Basic OS fingerprinting
- Response analysis
- Network mapping
- Types of possible connections
- Check firewall and IDS settings and configuration
- Simulate penetration tests
- Audit security aspects of a network

## Flags

- `-A` Perform OS detection, service detection, and traceroute scan
- `-D` Specifies decoys. Examples include:
  - `-D RND:5` Use five random IP address decoys
  - `-D <decoy,decoy2,ME,decoy3>` Use three decoys, two before me and then one after
- `--disable-arp-ping` Disable ARP ping requests
- `--dns-server <name_server>` DNS resolution is performed by the specified name server
- `-e <interface>` Specifies which interface to use when probing 
- `-f` Fragment packets
- `-F` Fast mode, scan fewer ports than the default scan (top 100 ports)
- `-iL <input_file>` Use an input file with a list of hosts/networks to scan
- `--initial-rtt-timeout <time_with_unit>` Specifies time value of initial Round-Trip-Time (RTT) timeout. For example, 100ms or 2s
- `-g <port_number>` or `--source-port <port_number>` Specifies a port number the probe is coming from
- `--max-retries <number>` Specifies the maximum number of retries for a scan of specified ports
- `--max-rtt-timeout <time_with_unit>` Specifies time value of maximum Round-Trip-Time (RTT) timeout. For example, 100ms or 2s
- `--min-rate <number>` Specifies the number of packets that will be sent simultaneously. For example 500
- `-n` Disables DNS resolution
- `-O` Enable OS detection
- `-oN filename` Store results of the scan in normal format in the filename specified (filename.nmap)
- `-oG filename` Store results of the scan in grepable format in the filename specified (filename.gnmap)
- `-oX filename` Store results of the scan in xml format in the filename specified (filename.xml)
- `-oA filename` Store results of the scan in three files with each in a format specified above (filename.gnmap, filename.nmap, filename.xml)
- `-p` Specifies what ports to scan. Some examples include:
  - `-p80` A single port
  - `-p1-1000` A range of ports
  - `-p22,80,443,5000` Multiple ports
  - `-p21-25,80,443` Range of ports and multiple ports
- `--packet-trace` Show all packets sent and received
- `-PE` Use ICMP echo request scans
- `-Pn` Treat the host as online. Skip host discovery. Disables ICMP echo requests
- `--reason` Display the reason for a result
- `-S <source_address>` Specifies the source address the probe is coming from
- `-sA` ACK scan
- `-sC` Run default nmap scripts
- `-sn` Disable port scanning. Used for [host discovery](/methodology/enumeration/host_discovery.md)
- `-sS` TCP SYN scan
- `-sT` Connect scan
- `-sU` UDP scan (very slow, specify a low number of ports)
- `-sV` Probe open ports to determine service/version information
- `-T<0-5>` Specifies how fast you want to scan. Here are some times:
  - `T0` Wait five minutes between each probe
  - `T1` Wait 15 seconds between each probe
  - `T2` Wait 0.4 seconds between each probe
  - `T3` Is the default probe speed and includes parallelization
  - `T4` Wait 0.1 seconds between each probe and includes parallelization
  - `T5` Wait 0.05 seconds between each probe and includes parallelization
- `--top-ports <number>` Scan the <number> most common ports
- `-v/-vv` Verbose output. It will output while scanning instead of waiting until the end

## Update The Script Database

```bash
nmap --script-updatedb
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

### Specify Source Port Number

Another rule that firewalls often check if the source and destination ports of traffic. It is a common rule for a firewall to block traffic based on the source port. Nmap uses the `-g` or `--source-port` option to specify a source port number. Here is a scan that uses source port 8080:

```bash
$ nmap -sS -Pn -F -g 8080 10.10.10.10
```

Or the other switch:

```bash
$ nmap -sS -Pn -F --source-port 8080 10.10.10.10
```

## Fragment Packets

Some firewalls, intrusion detection systems (IDS) and intrusion prevention systems (IPS) can be bypassed using fragment packets. This is when the packets are smaller and the firewall or IDS/IPS doesn't reassemble the fragment packets before passing them on to the target. The target will reassemble the fragment packets in order to process the request.

Nmap has the `-f` and `-ff` options to fragment packets. The `-f` option will fragment the packet to carry only 8 bytes of data. The `-ff` option will double it to 16. For a SYN packet the headers are 20 bytes and so each packet will be 28 or 36 bytes when using the `-f` or `-ff` options respectively. Here is an example to limit the packets to 8 bytes of data:

```bash
$ nmap -sS -Pn -F -f 10.10.10.10
```

Or the following to limit the packets to 16 bytes of data:

```bash
$ nmap -sS -Pn -F -ff 10.10.10.10
```

Packet lengths can also be set by setting the `--mtu` option. I provide it a value that must be a multiple of 8. So I would run the following commands to do the same thing as the previous commands.

```bash
$ nmap -sS -Pn -F --mtu 8 10.10.10.10
```

and

```bash
$ nmap -sS -Pn -F --mtu 16 10.10.10.10
```

## Specify TCP Segment

Some firewalls will block small packet request because they appear as scans. Nmap provides a way to specify the size of a packet. The `--data-length` option sets how large the TCP segment will be. This must be a multiple of 8. If I specify 128 bytes for the data length, then my packet will be 148 bytes. Here is an example using 128 bytes:

```bash
$ nmap -sS -Pn -F --data-length 128 10.10.10.10
```

## Specify Time-To-Live

Some firewalls reject packets that have the default time-to-live (ttl) of nmap. If this is the case, it is easy to change the value. Here is an example that alters that ttl:

```bash
$ nmap -sS -Pn -F --ttl 123 10.10.10.10
```

## Bad Checksum

Some firewalls will allow packets that have a bad checksum. This can be an indicator of the kind of firewall and technology that they are using. Here is how you send a packet with a bad checksum:

```bash
$ nmap -sS -Pn -F --badsum 10.10.10.10
```
