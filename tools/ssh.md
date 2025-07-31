# SSH

## Initial Information

If nmap shows that ssh is running on a machine, I will manually connect to it. I am trying to see if it asks for a password. If that is the case, this is another attack vector I can use if I can find a username on the server.

If the password prompt does not show up and I get an error that says "Permission denied (publickey)", my attack vector is reduced.

## Typical Usage

The syntax for using ssh is very easy. I specify the username I want to connect as and the host that I want to connect to. For example, if I wanted to connect as the user bob to machine at the ip address 10.10.1.1, I would run the following:

```bash
$ ssh bob@10.10.1.1
```

The username is optional. If the username is not provided it will use the username of the machine I am currently logged in as. For example, if I was logged in as the user kwmd on my machine and I ran the following command, it would use kwmd as the username:

```bash
$ ssh 10.10.1.1
kwmd@10.10.1.1's password:
```

### Connecting on a different port.

Also, sometimes I need to connect to ssh on a different port. This involves using the `-p` option. For example, if I need to connect on port 2222, I would run:

```bash
$ ssh -p 2222 bob@10.10.1.1
```

### Using another identity file

Some capture the flag events involve me finding a private key. I can then use that private key to log into the machine using ssh. I can specify an identity file with the `-i` option. For example, if I wanted to connect as the user bob to machine at the ip address 10.10.1.1 with an identity file called secretKey, I would run the following:

```bash
$ ssh -i secretKey bob@10.10.1.1
```

## SSH Port Forwarding

SSH port forwarding, sometimes called ssh tunneling, is a method of creating secure, encrypted connections between a local machine and a remote server. This connection allows traffic from specific ports to be securely transmitted through the ssh connection. There are three types of ssh port forwarding; local port forwarding, remote port forwarding and dynamic port forwarding.

| Type | Command | Explaination |
| --- | --- | --- |
| Local Port Forwarding | `ssh -L 8080:example.com:80 user@remote_server` | This redirects traffic from a port on the local machine to a specified port on the remote server, which then forwards the traffic to a destination host. In the example traffic on local port 8080 is forwarded to a web server running on port 80 on example.com via remote_server |
| Remote Port Forwarding | ` ssh -R 9090:localhost:80 user@remote_server` | Remote Port Forwarding (-R): This redirects traffic from a port on the remote server to a specified port on the local client machine, which then forwards the traffic to a destination host (which can be the local client itself or another host accessible from the local client). |
| Dynamic Port Forwarding | `ssh -D 1080 user@remote_server` | This creates a SOCKS proxy on the local client machine, allowing various applications to forward their traffic through the SSH connection to the remote server. This provides a more flexible way to tunnel multiple connections. |
