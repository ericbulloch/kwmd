# Netstat

- [Introduction](#introduction)
- [Usage](#usage)
- [Examples](#examples)

## Introduction

The netstat command is used to show connection a computer has made with a remote machine and connections that a remote machine has made with the computer. This can be used to find services that were not found during an initial nmap scan.

## Usage

```bash
netstat -h
usage: netstat [-vWeenNcCF] [<Af>] -r         netstat {-V|--version|-h|--help}
       netstat [-vWnNcaeol] [<Socket> ...]
       netstat { [-vWeenNac] -i | [-cnNe] -M | -s [-6tuw] }

        -r, --route              display routing table
        -i, --interfaces         display interface table
        -g, --groups             display multicast group memberships
        -s, --statistics         display networking statistics (like SNMP)
        -M, --masquerade         display masqueraded connections

        -v, --verbose            be verbose
        -W, --wide               don't truncate IP addresses
        -n, --numeric            don't resolve names
        --numeric-hosts          don't resolve host names
        --numeric-ports          don't resolve port names
        --numeric-users          don't resolve user names
        -N, --symbolic           resolve hardware names
        -e, --extend             display other/more information
        -p, --programs           display PID/Program name for sockets
        -o, --timers             display timers
        -c, --continuous         continuous listing

        -l, --listening          display listening server sockets
        -a, --all                display all sockets (default: connected)
        -F, --fib                display Forwarding Information Base (default)
        -C, --cache              display routing cache instead of FIB
        -Z, --context            display SELinux security context for sockets

  <Socket>={-t|--tcp} {-u|--udp} {-U|--udplite} {-S|--sctp} {-w|--raw}
           {-x|--unix} --ax25 --ipx --netrom
  <AF>=Use '-6|-4' or '-A <af>' or '--<af>'; default: inet
  List of possible address families (which support routing):
    inet (DARPA Internet) inet6 (IPv6) ax25 (AMPR AX.25) 
    netrom (AMPR NET/ROM) ipx (Novell IPX) ddp (Appletalk DDP) 
    x25 (CCITT X.25)
```

## Examples

| What I want to see. | Example |
| --- | --- |
| Show all active connections. | `netstat -a` |
| Show all active tcp connections. | `netstat -at` |
| Show all active udp connections. | `netstat -au` |
| Show listening ports. | `netstat -l` |
| Show listening tcp ports. | `netstat -lt` |
| Show listening udp ports. | `netstat -lu` |
| Show process ids and programs using sockets. | `netstat -p` |
| Show numeric addresses instead of resolving hostnames. | `netstat -n` |
| Show the routing table. | `netstat -r` |
| Show kernel routing information. | `netstat -rn` |
| Show established connections only. | `netstat -ant` |
| Find which process is using a specific port. | `netstat -tulpn` |
| Show summary statistics for each protocol. | `netstat -s` |
| Show summary statistics for tcp only. | `netstat -st` |
| Show summary statistics for udp only. | `netstat -su` |