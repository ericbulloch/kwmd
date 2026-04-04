# Enumeration - SMTP

[Back to methodology](/methodology/README.md)

- SMTP like other protocols was built for convenience with security added later

## Nmap Scan

```bash
nmap -sC -sV -A -p25 <target>
```

## Nmap Scan - Open Relay

```bash
nmap --script smtp-open-relay -p25 <target>
```

## Nmap Scan - Available Commands

```bash
nmap --script smtp-commands -p25 <target>

PORT   STATE SERVICE
25/tcp open  smtp
|_smtp-commands: mail1, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, CHUNKING
```

## Connecting Example Manual User Enumeration

```bash
telnet 10.10.10.100 25

Trying 10.10.10.100...
Connected to 10.10.10.100.
Escape character is '^]'.
220 My SMTP Server 

EHLO target.thm

250-target.thm
250-PIPELINING
250-SIZE 10240000
250-ETRN
250-ENHANCEDSTATUSCODES
250-8BITMIME
250-DSN
250-SMTPUTF8
250 CHUNKING

VRFY jim
550 5.1.1 <jim>: Recipient address rejected: User unknown in local recipient table
VRFY cindy
252 2.0.0 cindy
```

## VRFY, EXPN, And RCPT

There are three commands that can be used to enumerate users on the smtp service. They are VRFY, EXPN, and RCPT.

### VRFY

Checks an individual user running the command `VRFY <username>`. Here is an explaination of the return codes:

- 250: User exists
- 550: User does not exist
- 252: Server won't confirm, but will accept mail

### EXPN

Checks for all users running the command `EXPN`. If it is successful it will return a list of all users (rarely works). If it fails it will return a 502 or 550 for disabled or not supported.

### RCPT

Check an individual user running the command `RCPT <username>`. Here is an explaination of the return codes:

- 250: User exists
- 550: User does not exist

## Python - Enumerate Users

I have a script to enumerate users [found here](/concepts/python/enumerate_smtp_users.py).
