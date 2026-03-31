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

## Getting The SOA DNS Record

```bash
dig soa www.example.com
```

## Performing A Zone Transfer

```bash
dig axfr domain.htb @10.10.10.75
```

In this example, dig is trying to do a zone transfer for the domain named domain.htb using the dns name server 10.10.10.75.
