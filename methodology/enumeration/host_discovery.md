# Enumeration - Host Discovery

[Back to methodology](/methodology/README.md)

Sometimes I don't know all the machines in a network. Sometimes I need to scan the network to find all the hosts that are alive. Here are some commands to do this:

## Scan All Machines In A Subdomain

```bash
nmap 10.10.10.0/24 -sn -n -oA nmap/subdomain
```

## Scan With Specified Source Port

```bash
nmap 10.10.10.0/24 -sn -n --source-port 53 -oA nmap/subdomainFrom53
```

## Scan IP Range

```bash
nmap 10.10.10.100-130 -sn -n -oA nmap/subdomainRange
```
