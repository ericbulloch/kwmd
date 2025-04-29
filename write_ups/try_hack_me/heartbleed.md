# THM: HeartBleed

| Stat       | Value                                        |
| ---------- | -------------------------------------------- |
| Room       | HeartBleed                                   |
| URL        | https://tryhackme.com/room/heartbleed        |
| Difficulty | Easy                                         |

## Concepts/Tools Used

- Python
- SearchSploit

## Description

SSL issues are still lurking in the wild! Can you exploit this web servers OpenSSL?

## Process

This room has 2 parts. The first is information about the HeartBleed bug and what is causing it. The room provides a high level summary of how the bug can exploit memory on the server. There are a few external links that give more information and explain how this is a massive vulnerablity. The 2nd task wants you to exploit heartbleed on a server to get the flag.

## Task 1 Background Information

I spent a lot of time reading the material and trying to understand the bug. I had to look up more information and I thought I would just provide some additional insights into what is needed to exploit this vulnerability.

It is obvious that this exploit needs SSL or TLS. Since TLS is the successor of SSL and SSLv3 is totally broken I will just talk about using TLS for an https connection in this room.

In order to perform the heartbeat request (the request that causes the heartbleed attack), you need to have a connection with the server. Below are the minimum requests and responses for a heartbleed attack.

| Step | Description | Who sends it |
| ---- | ----------- | ------------ |
| 1. | **ClientHello** handshake connection request | **Attacker -> Server** |
| 2. | **ServerHello** (plus cert, etc.) handshake connection response | **Server -> Attacker** |
| 3. | **(TLS Handshake completes)** - now both sides can send encrypted data |  |
| 4. | **Heartbeat** request with **fake large payload length** | **Attacker -> Server** |
| 5. | **Heartbeat** response leaking memory past intended payload | **Server -> Attacker** |

Steps 4 and 5 are at the heart (no pun intended) of this room.
