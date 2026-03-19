# Enumeration - Port Scanning

- A port scan should take place for each machine to determine what services are available.
- Once a foothold has been obtained, a port scan can find services that were hidden.
- Generally a port scan has multiple stages. Generally here are the ones used:
  - Quick scan
  - Filtered scan
  - Full TCP scan
  - UDP scan

## Quick Scan

The goal here is just to look at the 1000 most common ports. If the results are low or ports are marked as filtered, run a Filtered scan. Otherwise run a Full TCP scan.

```bash
nmap <target> -oA quick
```

## Filtered Scan

Some ports have been marked as filtered or perhaps no results came back. A Filtered scan can be used to see if an IPS or firewall is blocking the port.

### Base Filtered Scan

```bash
nmap <target> -sA -p1-1000 -oA filtered --reason
```

### Source Port Filtered Scan

```bash
nmap <target> -sA -p1-1000 -oA filtered --reason --source-port 53
```

### Decoy Port Filtered Scan

This uses 5 random decoys:

```bash
nmap <target> -sA -p1-1000 -oA filtered --reason -D RND:5
```
