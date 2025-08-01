# Networking

How computer and systems connect is at the heart of cyber security. The scope of networking is massive and so I including items that I have found useful.

## TCP

TCP (Transmission Control Protocol) is one of the most common internet protocols. It used heavily with web browser applications like Chrome. It used for reliable transmission of data. It requires two computers to complete a three-way handshake before data begins to transfer.

TCP guarantees that all data packets are sent in the right order and without errors. If any packets are lost or corrupted, TCP will retransmit them. Some common protocols that care about data integrity are:

- HTTP and HTTPS: Browsing the web.
- FTP: Transferring files between machines.
- SMTP: Using email.

## Ports

A computer can run multiple multiple applications at the same time. Any application that uses a network to send or receive data doesn't want to get another application's traffic. How does a computer do this? They use ports.

Each computer has 65,535 ports they can listen on. One application can listen on port 4444 and the traffic from another application listening on a different port doesn't interfer with the first application.

