# nmap

Capture the flag events often provide a vulnerable machine's ip address. I need to know what is running on that machine so I can figure out what the next step is when attacking that machine. This is where nmap comes into play. The nmap tool is a very useful tool to find what ports are running on a machine. It can also try to detect the operating system that is running on the machine. I commonly use it to get the name and version of software that is listening on a given port.

## Usage

Running `nmap -h` provided the following output:

```bash
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

## Unknown Machine IP Address

When doing a capture the flag event with a VulnHub machine, I will need to discover the ip address of the machine. In my home lab I restrict the ip addresses of the machines to a range (for example 10.22.1.110-130). When I start up the VulnHub machine I need to find out what the ip address it is using. I already know that my attack machine is using 10.22.1.110. I run the following command to see the other machines with ip addresses:

`nmap -sS 10.22.1.111-130`

Whatever ip address shows up in the results is the machine that I just imported from VulnHub.

## Known Machine IP Address

### Original TCP Scan

In a capture the flag event I usually run a port scan in 2 parts. I am using the hostname target.thm for this an future examples. The first command I run is:

`nmap -p- -Pn -T5 -v target.thm`

This command does the following things:

- The `-p-` option tells nmap to scan all ports.
- The `-Pn` option tells nmap to skip host discovery.
- The `-T5` option will cause nmap to run the scan at one of the fastest levels (insane speed).
- The `-v` option tells nmap that I want verbose output from this scan.

Here is some sample output from the above command when port 22 and 80 were found open on the target machine:

```bash
Starting Nmap 7.80 ( https://nmap.org ) at 2025-04-21 15:30 BST
Initiating ARP Ping Scan at 15:30
Scanning target.thm (10.10.7.168) [1 port]
Completed ARP Ping Scan at 15:30, 0.03s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 15:30
Scanning target.thm (10.10.7.168) [65535 ports]
Discovered open port 22/tcp on 10.10.7.168
Discovered open port 80/tcp on 10.10.7.168
Completed SYN Stealth Scan at 15:30, 1.81s elapsed (65535 total ports)
Nmap scan report for target.thm (10.10.7.168)
Host is up (0.00012s latency).
Not shown: 65533 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
MAC Address: 02:42:CD:52:D4:57 (Unknown)

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 2.02 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 65536 (2.621MB)
```

Notice how fast this scan is with the `-T5` option (1.81 seconds to scan 65535 ports). If there are no ports open from the previous scan I will try a UDP scan. I have included that scan below.

### Second TCP Scan

Once this scan is complete and I have some ports that are reported as being up, I will run another command. I scan ports 22 and 80 from the previous output and get more information about the services running on thos ports. I run the following command to get more information for those ports:

`nmap -p 22,80 -A -Pn -v target.thm`

This command does the following:

- The `-p 22,80` option tells nmap to scan ports 22 and 80.
- The `-A` option tells nmap to try operating system detection, version detection, script scanning and also perform a traceroute.
- The `-Pn` option tells nmap to skip host discovery.
- The `-v` option tells nmap that I want verbose output from this scan.

Here is some sample output from this command:

```bash
Starting Nmap 7.80 ( https://nmap.org ) at 2025-04-21 15:37 BST
...
Host is up (0.00034s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: My Super Amazing Website!
MAC Address: 02:42:CD:52:D4:57 (Unknown)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), Linux 3.10 - 3.13 (94%), Linux 3.8 (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 2.6.32 (92%), Linux 2.6.39 - 3.2 (92%), Linux 3.1 - 3.2 (92%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 6.032 days (since Tue Apr 15 14:51:39 2025)
Network Distance: 1 hop
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.34 ms target.thm (10.10.7.168)

NSE: Script Post-scanning.
Initiating NSE at 15:37
Completed NSE at 15:37, 0.00s elapsed
Initiating NSE at 15:37
Completed NSE at 15:37, 0.00s elapsed
Initiating NSE at 15:37
Completed NSE at 15:37, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.12 seconds
           Raw packets sent: 47 (3.672KB) | Rcvd: 31 (2.616KB)
```

I cut out some of the output to show some of the important parts of this scan. There are a lot of good things happening with this scan. Nmap is guessing the operating system, doing a traceroute and discovering the service and version number for ports 22 and 80. Based on the services that are running from the results I now move on to the next segment.

### UDP Scan

If there are no ports open from the original TCP scan that I mentioned above, I'll try a UDP scan. A full UDP scan is significantly slower than a TCP scan. Here is the command I use for a UDP scan:

`nmap -p- -sU -Pn -T5 -v target.thm`

This command is the same as the original known machine ip address scan command above except the `-sU` option has been added to let nmap know I want a UDP scan instead.
