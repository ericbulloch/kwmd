# Enumeration - FTP

[Back to methodology](/methodology/README.md)

File Transfer Protocol (FTP)
- The client and server establish a control channel on port 21 TCP
- The data channel is on port 20 TCP, it is exclusively data transmission and can continue if the connection is broken and re-established
- All FTP transmissions are in clear text
- Trivial File Transfer Protocol (TFTP) is similar to FTP but uses UDP for transmission

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

** TFTP does not have a list directory command. **
