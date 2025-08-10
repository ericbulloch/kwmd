# Networking

- [Introduction](#introduction)
- [TCP](#tcp)
- [UDP](#udp)
- [Ports](#ports)
- [OSI Model](#osi-model)

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

## UDP

UDP (User Datagram Protocol) is a connectionless protocol that prioritizes speed over reliability. Unlike TCP, it doesn't establish a connection before sending data. There is no guarantee that packets will be delivered from the sender to the receiver. This makes UDP faster and more efficient for applications where some data loss is acceptable.

Applications that use UDP include:

- Live Streaming
- Online Gaming
- DNS Queries
- Network Monitoring

## Ports

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
- Play Dough Nunchucks To Smash Antiques
- Piper Doesn't Need To Sell Pepper Anymore
- Pete Doesn't Need To Sell Pickles Anymore
