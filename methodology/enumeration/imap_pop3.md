# Enumeration - IMAP/POP3

[Back to methodology](/methodology/README.md)

- IMAP uses ports 110 and 995
- POP3 uses ports 143 and 993

## Nmap Scan

```bash
nmap 10.10.1.100 -sV -p110,143,993,995 -sC
```

## Curl - Connect To IMAP

```bash
curl -k 'imaps://10.10.1.100' --user kwmd:kwmd -v
```
