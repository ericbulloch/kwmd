# Enumeration - DNS

[Back to methodology](/methodology/README.md)

- Domain Name System (DNS) is the phonebook of the internet

## Entities

There are three main entities in the world of DNS, they are the following:

- Zones
- Hosts
- DNS Servers

DNS servers are discussed in more detail below. Hosts are domains like wwww.example.com or mail.example.com. These domains map to an ip address. Zones are a grouping of hosts that might use another DNS server. For example, the domain www.example.com could be in a zone like example.com but the domain mail.example.com could be in a different zone called mail.example.com where it might have its own DNS server.

## DNS Servers

The different DNS servers include:

- DNS root server
- Authoritative name server
- Non-authoritative name server
- Caching server
- Forwarding server
- Resolver

### DNS Root Server

Root servers are responsible for the top-level domains (TLD). Top-level domains are things like .com, .net, .org, and .edu. There are 13 DNS root servers around the world. It is only called if the authoritative name server doesn't respond.

### Authoritative Name Server

They only answer queries for areas of their responsibility, and their information is binding. If they can't answer then the root name server takes the request.

### Non-Authoritative Name Server

Not responsible for a particular DNS zone. They collect information on specific DNS zones themselves, which is done using recursive or iterative DNS querying.

### Caching DNS Server

They cache information about domains and keep it stored based on the time period that Authoritative name servers give them.

### Forwarding Server

They only forward DNS queries to another DNS server.

### Resolver

When your router or computer performs name resolution instead of sending the request to DNS servers.

## DNS Record Types

DNS record types include:
- A
- AAAA
- MX
- NS
- TXT
- CNAME
- PTR
- SOA

### DNS Record Type A

The IPv4 address of the requested domain.

### DNS Record Type AAAA

The IPv6 address of the requested domain.

### DNS Record Type MX

The mail server of the requested domain.

### DNS Record Type NS

The DNS nameservers of the domain.

### DNS Record Type TXT

This field is a free hand form field. Anything can be placed in this field. It is a great source of loot when pillaging.

### DNS Record Type CNAME

The alias of the domain. This could include prefixes like www., portal., app., etc...

### DNS Record Type PTR

This record is the opposite of DNS and converts IP addresses into valid domain names.

### DNS Record Type SOA

This record provides corresponding DNS zone and email address of the administrative contact.

## Parsing Dig Output

The next few commands make heavy use of `dig`. It is important to understand the output so that domain names can be classified as DNS servers, hosts, or zones. Here are some tips:

1) If the name appears on the left side, it is either a zone or a host.
2) If the name appears on the right side, it is either a server, alias, or an ip address
3) Something is a zone if it meets the following criteria:
   - Has a SOA record
   - Has a NS record
   - Is a left side name in a zone transfer (axfr) attempt
4) Something is a nameserver if it meets the following criteria:
   - It appears on the right side of an NS record
   - It answers authoritative DNS queries
   - It can be queried directly using @
   - It responds to a chaos text query
5) Something is a host if it meets the following criteria:
   - It has an A or AAAA record
   - It resolves to an ip address
   - It is not referenced by an NS record.
6) CNAME is not a host, it is an alias. Its role depends on the target (right side name):
   - If target has A/AAAA record, it is the underlying host
   - If target is external, this is a pivot opportunity

## Getting The SOA DNS Record

```bash
dig soa www.example.com
```

## Getting The NS DNS Recorrd

```bash
dig ns <zone> @dns_server
```

This is only for zone targets. Nameserver records live at the zone level, not hostnames. Run against root domains and any subdomain you think will be a separate zone.

## Getting Any DNS Record

```bash
dig any <zone> @dns_server
```

This command is only for zone targets. Modern DNS servers will suppress and sanitize this information. I am checking if this zone leaks TXT, SPF, MX, and other DNS records. This is a low effort query.

## Running Chaos Text Query

```bash
dig CH TXT version.bind @dns_server
```

Chaos queries interrogate the server, not the domain. Run this command after discovering the nameserver. This command is meant to be ran directly against the nameserver.

## Performing A Zone Transfer

```bash
dig axfr <zone> @dns_server
```

In this example, dig is trying to do a zone transfer for the zone named domain.htb using the dns nameserver dns_server. This command is only ran against zones and must be requested against the authoritative servers. It is a low effort, high reward query. This command should be ran against every discovered zone and authoritative server.

## Performing An Internal Zone Transfer

```bash
dig axfr <internal_zone> @dns_server
```

I am inside the network and have indentified the internal nameservers. Internal DNS often trusts internal ip addresses, is Active Directory integrated, and contains internal only hostnames. Attempt this command post-compromise and against internal DNS servers.

## Subdomain Enumeration

```bash
dnsenum --dnsserver <dns_server> --enum -p 0 -s 0 -o subdomains.txt -f /path/to/wordlist.txt <zone>
```

I am discovering child hosts of a zone, not grandchildren of the host. I am finding new A/CNAME records, dev/stage/admin services, and forgotten infrastructure. Brute force every valid zone discovered, especially zones that fail the zone transfer command above. Wordlists are everything with this command.

## Command Mapping To DNS Entity

| DNS Entity | Examples | Commands To Run |
| --- | --- | --- |
| Zone | example.com | `dig NS`, `dig ANY`, zone transfer, subdomain enumeration |
| Host | www.example.com | `dig A`, `dig AAAA`, `dig CNAME` queries only |
| DNS Server | ns1.example.com | chaos text, zone transfer |

## Example

1. Start with example.com
2. `dig ns example.com`
3. For each nameserver:
   - `dig ch txt version.bind @dns_server`
   - `dig axfr example.com @dns_server`
4. If zone transfer (axfr) fails:
   - Subdomain enumeration
5. Check if each host is it's own zone
   - `dig ns new.example.com`
6. If yes, repeat steps for the new zone
