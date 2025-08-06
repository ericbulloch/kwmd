# THM: GLITCH

| Stat | Value |
| ---------- | -------------------------------------------- |
| Image | <img src="/images/write_ups/try_hack_me/glitch/glitch.jpeg" alt="GLITCH" width="90"/> |
| Room | GLITCH |
| URL | https://tryhackme.com/room/glitch |
| Difficulty | Easy |

## Concepts/Tools Used



## Room Description

Challenge showcasing a web app and simple privilege escalation. Can you find the glitch?

## Process

Once the machine starts up I save the machine's ip address to my host file so that I can type `target.thm` instead of an ip address.

I run nmap to see what ports are open:

```bash
$ nmap -T4 -n -sC -sV -Pn -v -p- target.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-23 04:47 BST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 04:47
Completed NSE at 04:47, 0.00s elapsed
Initiating NSE at 04:47
Completed NSE at 04:47, 0.00s elapsed
Initiating NSE at 04:47
Completed NSE at 04:47, 0.00s elapsed
Initiating SYN Stealth Scan at 04:47
Scanning target.thm (10.10.231.210) [65535 ports]
Discovered open port 80/tcp on 10.10.231.210
SYN Stealth Scan Timing: About 21.92% done; ETC: 04:50 (0:01:50 remaining)
SYN Stealth Scan Timing: About 57.78% done; ETC: 04:49 (0:00:45 remaining)
Completed SYN Stealth Scan at 04:49, 88.52s elapsed (65535 total ports)
Initiating Service scan at 04:49
Scanning 1 service on target.thm (10.10.231.210)
Completed Service scan at 04:49, 6.03s elapsed (1 service on 1 host)
NSE: Script scanning 10.10.231.210.
Initiating NSE at 04:49
Completed NSE at 04:49, 0.05s elapsed
Initiating NSE at 04:49
Completed NSE at 04:49, 0.01s elapsed
Initiating NSE at 04:49
Completed NSE at 04:49, 0.00s elapsed
Nmap scan report for target.thm (10.10.231.210)
Host is up (0.00054s latency).
Not shown: 65534 filtered ports
PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.14.0 (Ubuntu)
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: not allowed
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 04:49
Completed NSE at 04:49, 0.00s elapsed
Initiating NSE at 04:49
Completed NSE at 04:49, 0.00s elapsed
Initiating NSE at 04:49
Completed NSE at 04:49, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 96.25 seconds
           Raw packets sent: 131137 (5.770MB) | Rcvd: 70 (3.076KB)
```

## What is your access token?

I check the html for http://target.thm and I see an interesting script tag near the bottom:

```html
<script>
  function getAccess() {
    fetch('/api/access')
      .then((response) => response.json())
      .then((response) => {
        console.log(response);
      });
  }
</script>
```

Within the browser console I run getAccess() and get the following logged to the console:

```json
{
  "token": "dGhpc19pc19ub3RfcmVhbA=="
}
```

That token value looks like it is base64 encoded so I ran it on the console:

```bash
$ echo 'dGhpc19pc19ub3RfcmVhbA==' | base64 -d
REDACTED
```
