# Networking

- [Introduction](#introduction)
- [TCP](#tcp)
  - [TCP Three-Way Handshake](#tcp-three-way-handshake)
- [UDP](#udp)
- [Common Ports](#common-ports)
- [DNS](#dns)
  - [Phonebook Example](#phonebook-example)
  - [How It Works With Computers](#how-it-works-with-computers)
  - [DNS Records](#dns-records)
- [VPN](#vpn)
- [Proxy](#proxy)
- [OSI Model](#osi-model)
  - [Mnemonics To Remember OSI Model Layers](#mnemonics-to-remember-osi-model-layers)

## Introduction

How computer and systems connect is at the heart of cyber security. The scope of networking is massive and so I including items that I have found useful.

## TCP

TCP (Transmission Control Protocol) is one of the most common internet protocols. It used heavily with web browser applications like Chrome. It used for reliable transmission of data. It requires two computers to complete a three-way handshake before data begins to transfer.

TCP guarantees that all data packets are sent in the right order and without errors. If any packets are lost or corrupted, TCP will retransmit them. Some common protocols that care about data integrity are:

- HTTP
- FTP
- SMTP

Applications that use TCP include:

- Web Browsing
- Email
- File Transfers
- Streaming Media

### TCP Three-Way Handshake

The three-way handshake is used by TCP to create a connection between two machines to let them know that data is about to be transmitted. Here is the ordering of the handshake:

- The sender sends a SYN (Synchronize) packet. The SYN packet lets the receiver know that the sender would like to synchronize a connection and the sender includes an initial sequence number.
- The receiver responds with a a SYN/ACK (Synchronize-Acknowledge) packet. The SYN/ACK packet lets the sender know that the receiver is ready for the communication.
- The sender sends a ACK (Acknowledge) packet. This is to let the receiver know that the sender got their SYN/ACK packet. This completes the handshake and a reliable connection is established.

This ladder diagram makes it easy to visualize what is going on with the handshake:

```yaml
Client                                Server
  |                                     |
  | ----------- SYN ------------------> |  (Step 1: Client sends SYN to initiate connection)
  |                                     |
  | <-------- SYN-ACK ----------------- |  (Step 2: Server acknowledges SYN and sends its own SYN)
  |                                     |
  | ----------- ACK ------------------> |  (Step 3: Client acknowledges server's SYN)
  |                                     |
Connection Established            Connection Established
```

## UDP

UDP (User Datagram Protocol) is a connectionless protocol that prioritizes speed over reliability. Unlike TCP, it doesn't establish a connection before sending data. There is no guarantee that packets will be delivered from the sender to the receiver. This makes UDP faster and more efficient for applications where some data loss is acceptable.

Applications that use UDP include:

- Live Streaming
- Online Gaming
- DNS Queries
- Network Monitoring

## Common Ports

A computer can run multiple multiple applications at the same time. Any application that uses a network to send or receive data doesn't want to get another application's traffic. How does a computer do this? They use ports.

Each computer has 65,535 ports they can listen on. One application can listen on port 4444 and the traffic from another application listening on a different port doesn't interfer with the first application.

Some ports are so well known for the protocol that runs on them that they are associated with that protocol. A machine can run any protocol on any port number but some protocols have a tendency to run on specific ports. Some of the more well-known ports include:

| Port | Description |
| --- | --- |
| 20 | FTP (File Transfer Protocol) data transfer. |
| 21 | FTP (File Transfer Protocol) command connection. |
| 22 | Secure Shell (ssh) for secure logins, file transfers (scp, sftp) and port forwarding. |
| 23 | Telnet protocol for unencrypted text communication. |
| 25 | SMTP (Simple Mail Transfer Protocol) for email routing. |
| 53 | DNS (Domain Name System) service. |
| 80 | HTTP (Hypertext Transfer Protocol) for web traffic. |
| 110 | POP3 (Post Office Protocol version 3) for email retrieval. |
| 143 | IMAP (Internet Message Access Protocol) for email management. |
| 443 | HTTPS (Hypertext Transfer Protocol Secure) for secure web traffic. |
| 3000 | Ruby on Rails default development server. |
| 3000 | Grafana default port. |
| 3306 | MySQL database system. |
| 4444 | Metasploit's default listening port. |
| 4444 | My default reverse shell listening port. |
| 5000 | Flask's default development server. |
| 5432 | PostgreSQL database system. |
| 5601 | Kibana default port. |
| 6379 | Redis default port. |
| 8000 | Alternative port for HTTP, often used for web servers. |
| 8000 | Django default port. |
| 8080 | Alternative port for HTTP, often used for web servers. |

## DNS

DNS (Domain Name System) is way for a computer to know where to communicate with another computer. It informs a computer of the ip address of the computer.

### Phonebook Example
DNS acts the same way that phonebooks were used in the real world.

A person could find a person's phone number by looking up a person's name (or the name of the parent of that person) in the phonebook. Once they found the person, they would see their phone number. If this person was important or you thought you would call them often, you would write down their name and number on a sheet of paper and place it by the phone. This made it easy and quick to look them up again without opening the phonebook. Each year, a new phone book would arrive and it became the new authority for phone numbers. The old phonebook would be discarded but it was kept around in case a person's phone number got left out of the new phonebook or if the information was incorrect.

So if I wanted to call someone I had a list of steps that I would follow to get a person's phone number. At each step I could find the number so I wouldn't continue with the steps after that one. Here are the steps:

- Check if I had memorized the phone number.
- Check the sheets of papers taped to the wall by the phonebook.
- Check the sheets of papers in the drawer next to the phone.
- Check the latest phonebook.
- Check an older phonebook.
- Call a mutual friend and ask them.
- Call the operator.

Each step is a type of cache and it is more efficient than the next step. At any step, a person could find the number and write it down at one of the higher steps. I got the following step-by-step diagram from AI to help clarify this:

```txt
(0) You want "Alice's" phone number
    │
    ▼
┌───────────────────────────────┐
│  Personal memory              │
│  (instant local answer)       │ 
└───────────────────────────────┘
    │  hit? return ✅
    └──no
        ▼
┌───────────────────────────────┐
│  Sheets taped to the wall     │
│  (handy, manually kept)       │ 
└───────────────────────────────┘
    │  hit? return ✅
    └──no
        ▼
┌───────────────────────────────┐
│  Papers in the drawer         │
│  (kept nearby, semi-official) │
└───────────────────────────────┘
    │  hit? return ✅
    └──no
        ▼
┌───────────────────────────────┐
│  Latest phonebook             │  
│  (authoritative-ish directory)│
└───────────────────────────────┘
    │  found? return ✅ (and maybe copy it to your notes)
    └──no
        ▼
┌──────────────────────────────┐
│  Older phonebook             │
│  (fallback copy)             │
└──────────────────────────────┘
    │  hit? return (but check if outdated)
    └──no
        ▼
┌──────────────────────────────┐
│  Call a mutual friend        │
│  (someone who might know)    │
└──────────────────────────────┘
    │  they give you the number? ✅
    └──no
        ▼
┌──────────────────────────────┐
│  Call the operator           │
│  (authoritative lookup)      │
└──────────────────────────────┘
    │
    ▼
   ✅ You get Alice’s number (and can write it down / cache it)
```

### How It Works With Computers

Much like the real world phonebook example above, computers have very similar steps. Computers need to change a domain name to an ip address. Humans are good at remembering things like `github.com` but they are terrible at remembering what the ip address of that domain is. Here are the steps computers use to convert a domain name to an ip address (each step can have the answer and so the latter steps will not get used):

- Check local cache to see if it already knows the ip address of the remote machine.
- Ask the resolver - usually your internet service provider or a service like Google DNS. This will also check another resolver that has more authority regarding ip address lookups.
- Check the root servers. There are 13 root server ip addresses in the world.
- Check the top level domain (TLD) servers. This can be the resolver of `.com` domains.
- Check the authoritative server for a domain. Meaning it will ask GitHub's authoritative server: "What is the ip address for `github.com`?

A response at each step can be cached for the higher steps to make lookups even faster.

Cloud flare has provided the following image which makes this very easy to visualize:

![DNS Root Server](/images/concepts/networking/dns_root_server.png)

In the image above a DNS query starts at the top and works its way down. The the root node in the picture is the 3rd step in the list above when it reached out to the root node. Again, there are 13 root server ip addresses in the world. There are many root servers but only 13 ip addresses used to query the different root server networks.

This whole process is long and so I had AI generate a workflow that includes local caches when looking up DNS. This is what it provided:

```sql
(0) You type "www.example.com"
    │
    ▼
┌───────────────────────┐
│  Browser/App Cache    │  — per-site DNS cache (some apps have it)
└───────────────────────┘
    │  hit? return ✅
    └──no
        ▼
┌───────────────────────┐
│  OS Stub Resolver     │  — your device’s DNS client
│  (hosts file checked) │
└───────────────────────┘
    │
    ├───► Check OS DNS Cache ── hit? return ✅
    │
    └──no cache hit → ask configured **recursive resolver**
                      (e.g., router/ISP/1.1.1.1/8.8.8.8)

        (1)
        ▼
┌──────────────────────────┐
│  Recursive Resolver      │  — does the hard work
│  (big shared cache)      │
└──────────────────────────┘
    │  cache hit? return to OS ✅
    └──no
        ▼  iterative resolution (referrals)
        (2) ask ROOT
        ▼
┌──────────────────────────┐
│  Root Name Servers       │
│  (.)                     │  — don’t know the IP
└──────────────────────────┘
        │  return referral: “ask the TLD”
        ▼
(3) ask TLD (e.g., .com)
        ▼
┌──────────────────────────┐
│  TLD Name Servers        │
│  (.com, .org, etc.)      │ — don’t know the IP
└──────────────────────────┘
        │  return referral: “ask the authoritative NS for example.com”
        ▼
(4) ask Authoritative NS for example.com
        ▼
┌──────────────────────────┐
│  Authoritative Servers   │
│  (example.com)           │ — have the A/AAAA/CNAME, etc.
└──────────────────────────┘
        │  return final answer + TTL
        ▼
┌──────────────────────────┐
│  Recursive Resolver      │  — caches per TTL
└──────────────────────────┘
        │
        ▼
┌──────────────────────────┐
│  OS Stub Resolver        │  — caches per TTL
└──────────────────────────┘
        │
        ▼
┌──────────────────────────┐
│  Browser/App Cache       │  — may cache per TTL/policy
└──────────────────────────┘
        │
        ▼
      ✅ You get the IP
```

### DNS Records

Here is a list of the different DNS record types:

| Type | Explaination | Example |
| --- | --- | --- |
| A | Maps a domain to an IPv4 address. |  `github.com` to `140.82.114.3`. |
| AAAA | Maps a domain to an IPv6 address. | `google.com` to `2607:f8b0:4023:100d::65:`. |
| CNAME | Short for canonical name. It maps an alias to a canonical name. | Mapping `mail.google.com` and `www.google.com` to `google.com`. |
| MX | Short for mail exchange. This is used for mail delivery. | `mail.google.com`. |
| TXT | Human readable DNS record. Limited to 255 characters. It is used for infiltration and exfiltration attacks because this field is freeform | "This is a sample text DNS record." |

## VPN

Virtual Private Networks (VPN) are used to connect computers and devices with the intent of making them feel as if they were plugged into the same local area network (LAN). Some VPNs include the following:

- Remote Access VPN: These are networks where the client creates a virtual interface that makes them feel like they are on the network. Sites like TryHackMe and Hack The Box use OpenVPN so that my attack machine can connect to their network.
- SSL VPN: This is a VPN over the browser. Sites like TryHackMe and Hack The Box have attack boxes that can be ran from the browser. Those attack boxes are streaming a desktop session from the browser.

## Proxy

Proxies are servers or devices that sit between two devices that are communicating. Normally one side doesn't want to communicate directly with another and so a proxy acts as a mediator. Proxies can be used for inbound and outbound traffic. Some proxy types include:

- Forward Proxy: When another device or computer makes a request on behalf of you. Burp Suite is an HTTP forward proxy as it intercepts requests from my machine so that I can alter them before sending them to the server. Many of the VPN services that get advertised on sites like YouTube are Forward Proxies.
- Reverse Proxy: A reverse proxy is when another server or device receives a request and then forwards it to your machine. This is a common technique used for web applications where a server receives the request and then forwards that request to one of the application servers that handle the request. This is useful to protect against denial of service attacks. It also adds a layer of protection so that traffic can be filtered.

## OSI Model

- Layer 1: Physical Layer
- Layer 2: Data Link Layer
- Layer 3: Network Layer
- Layer 4: Transport Layer
- Layer 5: Session Layer
- Layer 6: Presentation Layer
- Layer 7: Application Layer

### Mnemonics To Remember OSI Model Layers

- Please Do Not Throw Sausage Pizza Away
- Piper Doesn't Need To Sell Pepper Anymore
- Pete Doesn't Need To Sell Pickles Anymore
