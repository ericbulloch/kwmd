# Enumeration - FTP

[Back to methodology](/methodology/README.md)

File Transfer Protocol (FTP)
- The client and server establish a control channel on port 21 TCP
- The data channel is on port 20 TCP, it is exclusively data transmission and can continue if the connection is broken and re-established

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
