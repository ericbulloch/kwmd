# Enumeration - IMAP/POP3

[Back to methodology](/methodology/README.md)

- Internet Message Access Protocol (IMAP) uses ports 110 and 995
- Post Office Protocol (POP3) uses ports 143 and 993

## Nmap Scan

```bash
nmap 10.10.1.100 -sV -p110,143,993,995 -sC
```

## Curl - Connect To IMAP

```bash
curl -k 'imaps://10.10.1.100' --user kwmd:kwmd -v
```

## OpenSSL - Connect To IMAP

```bash
openssl s_client -connect 10.10.1.100:imaps
```

## OpenSSL - Connect To POP3

```bash
openssl s_client -connect 10.10.1.100:pop3s
```

## IMAP Commands

### Login

```bash
A LOGIN username password
```

### List Inboxes

```bash
A LIST "" *
```

### Select Inbox

```bash
SELECT inbox_name
```

### Retrieve Emails

```bash
A UID FETCH 1 (UID RFC822.SIZE BODY.PEEK[])
```
