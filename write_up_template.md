# Target: Lab

- IP Address: 10.129.1.1
- Starting Domain Name: target.htb

## Scope & Goal
- Objective: user.txt, root.txt
- Constraints: lab

# Recon
- Quick TCP:

```bash
$ nmap target.htb

```

- Targeted Scan:

```bash
$ nmap target.htb -sV -sC -A -p -vv

```

- Full TCP:

```bash
$ nmap target.htb -sC -sV -A -T4 -vv -p-
...
Same as Targeted Scan above
```

## Open Services
- 80/http

## Web Enum
- Tech:
- Dirs/VHosts:
- Params/Endpoints:
- Findings:

## Foothold
- Vector:
- Steps/Commands:
- Evidence:

## Privilege Escalation
- System Information:
- Credentials/Loot:
- Linux Checks:
- Successful Path:

## Flags
- user.txt: `hash` (date -u)
- root.txt: `hash` (date -u)

## Cleanup
- Artifacts Removed

## Lessons
- What Worked:
- Dead Ends:
- Reusable Commands:

```bash

```
