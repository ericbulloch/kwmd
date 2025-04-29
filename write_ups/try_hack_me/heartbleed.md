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

### How the request and response should work

It turns out that a heartbeat request is very simple. The 2 properties that matter are the content and the length of the content. So I send a heartbeat request with these 2 properties to a server:

Content: 'Hello'
Content-Length: 5

The server is suppose to look at the Content-Length property and create a buffer of that length in memory. Then it copies the text in the Content property into that buffer that it just created. Then it copys that buffer into a response and sends the response back to me so that our TLS connection stays alive.

### How heartbleed works

This vulnerability exists because it trusted user input. In my example above I said that my Content-Length was 5 bytes. But what if I had the same Content and I said that my Content-Length was 65,535 bytes?

This is where the vulnerability. It doesn't check the length of my Content it just blindly trusts that I am sending the correct Content-Length for my Content.

In this case, the server will allocate a 65,535 byte buffer in memory. Keep in mind that deallocated memory still has the values that were in those addresses when the memory was allocated. Then it will copy over the 5 bytes in my Content property. Then it will read all the bytes from the buffer (all 65,535 of them) and copy them to the response that goes back to me.

So now I have all kinds of things that were in memory when I made my request. It turns out that this can be usernames, passwords, sensitive chat logs and emails, environment variables, secret keys for X.509 certificates, critical business documents and more.
