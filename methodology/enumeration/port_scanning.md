# Enumeration - Port Scanning

[Back to methodology](/methodology/README.md)

- A port scan should take place for each machine to determine what services are available.
- Once a foothold has been obtained, a port scan can find services that were hidden.
- Generally a port scan has multiple stages. Generally here are the ones used:
  - Quick scan
  - Filtered scan
  - Full TCP scan
  - UDP scan

## TCP Connect Scan

The examples below use a full TCP connect scan (the `-sT` flag). Here is how this scan works:

- Send packet with SYN flag to the target port.
- If the target responds with a SYN-ACK flag packet, that port is marked as open and a packet with the ACK flag is sent to complete the handshake. After the connection has been made nmap closes the connection with a RST-ACK flag packet.
- If the target response with a RST flagged packet, that port is marked as closed.
- If nmap does not receive a packet back or an error code, that port is marked as filtered.

## TCP-SYN Scan

Both the Quick scan and Full TCP scan can use the TCP-SYN scan of nmap (use the `-sS` flag). This scan starts the TCP three-way handshake but doesn't finish it. This scan is called a stealth scan because many systems only log when a connection completes not when it is started. Here is how this scan works:

- Send packet with SYN flag to the target port.
- If the target responds with a SYN-ACK flag packet, that port is marked as open.
- If the target response with a RST flagged packet, that port is marked as closed.
- If nmap does not receive a packet back or an error code, that port is marked as filtered.

## Quick Scan

The goal here is just to look at the 1000 most common ports. If the results are low or ports are marked as filtered, run a Filtered scan. Otherwise run a Full TCP scan.

```bash
nmap <target> -oA nmap/quick
```

## Filtered Scan

Some ports have been marked as filtered or perhaps no results came back. A Filtered scan can be used to see if an IPS or firewall is blocking the port.

### Base Filtered Scan

```bash
nmap <target> -sA -p1-1000 -oA nmap/filtered --reason
```

### Source Port Filtered Scan

```bash
nmap <target> -sA -p1-1000 -oA nmap/filteredFrom53 --reason --source-port 53
```

### Decoy Port Filtered Scan

This uses 5 random decoys:

```bash
nmap <target> -sA -p1-1000 -oA nmap/filteredDecoys --reason -D RND:5
```

## Output of Port Scanning

For each service, try to get the following:

- Port number:
- Service running:
- Version of service:
- Exploit research:

Ports and services should be grouped by priority, for example:

High Priority:

- 80 (Web app -> likely entry point)
- 445 (SMB -> common misconfigurations)

Medium Priority:

- 22 (SSH -> depends on credentials)

Low Priority:

- 631 (CUPS)
