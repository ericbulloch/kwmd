# Enumeration - FTP

[Back to methodology](/methodology/README.md)

Port(s): 21

File Transfer Protocol (FTP)
- The client and server establish a control channel on port 21 TCP
- The data channel is on port 20 TCP, it is exclusively data transmission and can continue if the connection is broken and re-established
- All FTP transmissions are in clear text
- Trivial File Transfer Protocol (TFTP) is similar to FTP but uses UDP for transmission
- OpenSSL can be used to enable using FTP over SSH.

## Active vs Passive mode

In both modes, the client connects to the server on the control port (usually 21). The difference is who connects on the data port.

In the case of Active mode, the server provides a random port number and the client listens on that port number waiting for a connection from the server. The problem with this approach is that the client's firewall will often block a request to a random port. The connection can be visualized like this:

```text
Client → Server (port 21)   [control]
Server → Client (random port) [data]
```

In the case of Passive mode, the server provide the client with an IP address and a port number. The client again connects to the provided IP address and port number for data transmission. The firewall for the server will have to whitelist port range(s). The connection can be visualized like this:

```text
Client → Server (port 21)     [control]
Client → Server (random port) [data]
```

# Trivial File Transfer Protocol (TFTP)

TFTP is similar to FTP but uses UDP for transmission. This means that transmissions are unreliable. Unlike FTP, TFTP does not require the user's authentication. It does not support protected login via passwords and sets limits on access based solely on the read and write permissions of a file in the operating system. This means that all the files and directories are "globally" shared among users. TFTP should only be used in secure local networks.

*TFTP does not have a list directory command.*

## Nmap Scan

The following command with try to get the service, version number, and run default scripts with nmap:

```bash
nmap -sC -sV -A -p21 <target>
```

## Banner Grabbing

Netcat can be used to grab the banner with the following command:

```bash
nc <target> 21
```

Nmap can also be used with the following command:

```bash
nmap --script=banner -p21 <target>
```

## Authentication

FTP does allow anonymous authentication. Typically the username is anonymous and the password is blank or an email address. Some common FTP credentials include:

```text
admin:admin
admin:password
root:root
root:password
ftp:ftp
user:user
guest:guest
admin:1234
```

## Server Status

Once I have logged into an FTP server, I can view stats about the server with the `status` command. Some sample output includes:

```text
No proxy connection.
Connecting using address family: any.
Mode: stream; Type: binary; Form: non-print; Structure: file
Verbose: on; Bell: off; Prompting: on; Globbing: on
Store unique: off; Receive unique: off
Case: off; CR stripping: on
Quote control characters: on
Ntrans: off
Nmap: off
Hash mark printing: off; Use of PORT cmds: on
Tick counter printing: off
```

## Debug And Trace

FTP does have `debug` and `trace` commands that can be ran to get more information about what is running on a server.

## Recursive Listing

It is time to see what the FTP server has on it. To view all directories and files on an FTP server run the following command:

```bash
ls -R
```

This will show files and folders recursively from the current directory.

## View A File Without Downloading

```bash
get fileToDownload.txt -
```

## Check Upload Permissions

Create a file like the following:

```bash
echo 'kwmd FTW!' > test.txt
```

Then try uploading the file in the ftp client with the following command:

```bash
put test.txt
```

Afterwards see if it uploaded with the listing command:

```bash
ls
-rw-------    1 1002     133             9 Oct 122 17:01 test.txt
```

## Connect Over SSH

OpenSSL can be used to connect to an FTP server. Use the following command:

```bash
openssl s_client -connect 10.10.1.222:21 -starttls ftp
```

## Connect With Netcat

```bash
nc -nv 10.10.1.222 21
```

## Connect With Telnet

```bash
telnet 10.10.1.222 21
```
