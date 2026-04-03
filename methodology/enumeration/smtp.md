# Enumeration - SMTP

[Back to methodology](/methodology/README.md)

- SMTP like other protocols was built for convenience with security added later

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
