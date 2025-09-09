# Website Hacking

- [Introduction](#introduction)
- [Browsing The Site](#browsing-the-site)
- [Inspecting HTML](#inspecting-html)
- [Directory Enumeration](#directory-enumeration)
  - [Directory Enumeration with Gobuster](#directory-enumeration-with-gobuster)
- [Forms](#forms)
  - [SQL Injection Example](#sql-injection-example)
  - [Command Injection Example](#command-injection-example)
  - [File Upload Forms](#file-upload-forms)

## Introduction

So many capture the flag events involve looking at a website and trying to find a vulnerability in the site. There are so many moving parts in a website and with how websites are developed, a single page can be composed of components from different teams. A site could also be populated with API calls or a request that gives a new or updated page as the response. No matter how it gets its data, I'll just refer to it as the website.

Since this is a really big topic, I wanted to break it out and talk about the different things that are done when working on a capture the flag event with a website. I'll try to give a general approach and then talk about specifics for things that need it.

## Browsing The Site

But seriously, browse the site. It is easier to hack a site if I know how it is suppose to behave. It can help me understand the psycology of what the developers wanted me to experience with the website. I would recommend the following:

- Have a look around.
- Click the links.
- Use the functionality of the site.
- Create a user.
- Capture requests and responses.
- Learn about the processes and flow of the site.

Armed with this information, I can makes better decisions about how to attack the site because I'll understand how it is expected to work. As I document what is on a site and where it is located, I am really documenting all the attack vectors of the site.

## Inspecting HTML

One of the easiest ways to get information in by inspecting the source HTML for a site. Opening up the website and hitting `ctrl + u` will enable me to view the source html for a site. The source code is loaded with all kinds of information. It can provide links, directories, subdomains and comments.

Developers will work on things and then comment them out thinking that people will not see them. This couldn't be further from the truth. This can lead to finding all kinds of sensitive information or view parts of the site that were meant for employees and not the general public. Many capture the flag events have flags and other sensitive information in the comments of the HTML. During these events I have found flags, usernames, passwords, directories and links that my automated tools missed. This is a very overlooked way to find useful things. Here is a sample comment that I found during a capture the flag event:

```text
<!--

  Note from me, to me, remember my login name.

  Username: Sk3l3t0r

-->
```

### Security Measures

Developers need to remove commented out parts of the source code. The risk of what they reveal is not worth it. Also, if a directory or feature is not ready or available for a user it should not allow them to use it. What happens to the user when they try to use one of these items is up to the developer and can be chosen on a case by case basis.

## Directory Enumeration

I almost always run a directory enumeration to see if there are any folders or files that are not directly linked by the website. Directory enumeration can provide very important things like the location of the admin login form, hidden folders that have sensitive data or test pages that run commands directly on the server. Files like `robots.txt` and `sitemap.xml` can also provide useful information.

If the tool finds a directory like `/app`, I will often run a directory enumeration again on that directory to see if there are additional results.

There are a lot of automated tools I can use for directory enumeration. Generally, the word list is the **most important** part. If I get stuck, I use a combination of tools and word lists to see if they find anything different.

The main idea of directory enumeration isn't just to find hidden things. The main point is to find as many things as I can and making notes of them. All of this information is part of the attack surface of the website. The larger the website, the more attack surface it needs to defend.

### Directory Enumeration with gobuster

I now almost exclusively run directory enumeration searches with [gobuster](/tools/gobuster.md). It is very easy to use. I have provided information on how to run gobuster for directory enumeration on [its tool page](/tools/gobuster.md#directoryfile-dir-enumeration-mode).

### Security Measures

Here are some things that can be done to slow down or even prevent directory enumeration on a website:

- Limiting how many requests an ip address can make per second.
- Disable directory listing on the web server so that it does not list the contents of directories without an index file.
- Monitoring requests for enumeration behavior (common wordlist patterns, repeated 404 status codes, suspicious user agents).
- Using a web applicatin firewall to detect and block enumeration patterns.
- Obfuscate sensitive paths that are found in wordlists like /admin, /backup and /test.
- Remove unused files and directories (beware of things like .git, .env, .bak, .old, debug.php, etc...).
- Use a custom 404 page that avoids revealing information in error messages and provide generic responses that don't confirm the existance of a path.

## Forms

Forms are a natural source of issues for security. Users are able to send data and input to the website and get a response. Sometimes forms can give too much information that can then be used to perform a more informed attack on the website. Many times, developers lack the imagination or understanding of what attackers will throw at a form.

Since forms are accepting user input, some of the attacks they need to be aware of are the following:

- [SQL Injection](#sql-injection-example)
- Cross-Site Scripting (XSS)
- [Command Injection](#command-injection-example)
- HTML Injection
- Authentication Bypass
- Broken Authentication
- Privilege Escalation
- Cross-Site Requst Forgery (CSRF)
- Business Logic Flaws
- Sensitive Data Exposure
- Client-Side Only Validation

### SQL Injection Example

Because a form accepts user input, it can be vulnerable to SQL Injection. One of the first things I try on a form during a capture the flag event is to capture the request and save it to a file called `request.txt`. Once I have that file, I run the following command:

```bash
$ sqlmap -r request.txt
```

I have more details about this on the [sqlmap tools page](/tools/sqlmap.md).

The sqlmap tool will check the form to see if it is vulnerable to sql injection. If the form is vulnerable, an attacker can can do the following:

- Read sensitive data in the database.
- Get a dump of the database
- Log into the site with elevated privileges.

Sometimes I just want to test for SQL injection vulnerabilities manually. In this case, I would enter something like the following for the username field or password field of a login form:

```sql
' OR '1'='1
```

This snippet will is a very broad attempt to just login with any user since it will match all users in the system. If the system returns some kind of error or a 503 error that can be an indication that the site is vulnerable and it returned more than 1 result and the code didn't know how to handle it. It might also display an error that talks about the database, if that is the case I have a good feeling that this is vulnerable to SQL injection. At that point, I'll iterate more and try to return a single result by changing the query to the following:

```sql
' OR '1'='1' LIMIT 1; --
```

That way the query will match all results but only return a single record. If the login is successful, I can craft other queries to log in with users that have elevated privileges.

#### Blind SQL Injection

The `sqlmap` tool uses time-based blind injection attacks to get information from the database. This means that it figures out how long a form submit request takes and then adds a buffer of a second or so when it query returns true. This means that it can perform a potential SQL injection attack to get information and if the response is quick, the query is true. If the response is not quick, the query is false. This way, the tool uses boolean (true and false) logic to get information from the the database without getting the actual result set from the database.

This probably sounds really abstract, so lets try an example. If I find that a form is vulnerable to SQL injection, I can ask it yes and no questions to get answers. Since I want this to be as fast as possible and I am more likely to get a no (or a false) answer, I want to have the yes case cause the response to be slow so that I can confirm that I got a yes (or a true) answer. For this example, lets say that I am using a MySQL database. All MySQL databases have a table called `information_schema`.

I could craft a SQL injection query that has the following:

```sql
' OR UNION SELECT IF(EXISTS(SELECT 1 FROM information_schema.tables), SLEEP(5), 0), 2--
```

This query would make the response take 5 extra seconds because the database is MySQL. The query is doing a union select which then checks if selecting 1 from the information_schema.tables happens. In the case that it does return a 1 the query sleeps for 5 seconds. Otherwise it would do nothing.

The `sqlmap` tool is doing something similar to this when it gets data from a vulnerable form. It will ask a question like "Does a table start with a 'u'"? If it does, it will then ask "Does a table start with 'ua'"? If that fails it will try 'ub' until it gets the name of a table like 'users'.

When `sqlmap` dumps a table, it is sending thousands of requests to get column names and values for each record in the table. It is a very slow process but it is much faster than doing it manually. If the page does show the results from a query, `sqlmap` is smart enough to parse the results and hand them over.

#### Manual Step-By-Step SQL Injection Workflow

- Test for SQL injection vulnerability.
- Find the number of columns.
- Confirm injection with time based attack.
- Identify the database version.
- List tables.
- List columns.
- Dump data.

##### Test for SQL Injection vulnerability

To test for SQL injection add the following as a value to a input field on a form:

```sql
' OR '1'='1' --
```

or

```sql
' OR 'a'='a' --
```

These should look familiar as one was used above when talking about manually checking for SQL injection. If the login succeeds or an error message appears this likely means there is a SQL injection vulnerability.

##### Find the number of columns

To test for the number of columns I'll add an order by statement. I'll keep adding one to the column count and once there is an exception I'll know how many columns there are. Here are some samples of what I mean by adding an order by statement in the input field of the login form:

```sql
' ORDER BY 1 --        # test if at least 1 column exists
' ORDER BY 2 --        # test if at least 2 columns exist
' ORDER BY 3 --        # keep going until error
```

or

```sql
' UNION SELECT NULL --  
' UNION SELECT NULL, NULL --  
' UNION SELECT NULL, NULL, NULL --  
```

##### Confirm injection with time based attack

Now that I know the column count, I can add the SLEEP command as part of a union select statement. If there is a delay, then the injection has been confirmed.

```sql
' UNION SELECT SLEEP(5), NULL--  
```

or

```sql
' OR IF(1=1, SLEEP(5), 0)--  
```

**NOTE**: not all database management systems (DBMS) have the same SLEEP function. For example, PostgreSQL uses `pg_sleep`. If SLEEP doesn't work I'll try out other ones. Here is a table of the different ones:

| DBMS | Sleep Function |
| --- | --- |
| MySQL | SLEEP |
| PostgreSQL | pg_sleep |
| SQL Server | WAITFOR DELAY |
| Oracle | DBMS_SESSION.SLEEP |

##### Identify the database version

To find the database version, run one of the following commands (it assumed there were two columns being returned so a null was included in the select):

```sql
' UNION SELECT @@version, NULL --  
```

or

```sql
' UNION SELECT database(), NULL --  
```

The commands provided are for different database vendors. I adapt the command based on the information that I got in the previous step. Once a version is know, I can look up a CVE for the specific database version that I have found.

### SQL Injection Security Measures

Many input issues can be solved by sanitizing user input and making sure what they type is in an approved range of values. For example, if a person needs to enter their name, don't allow them to use numbers and most of the special characters that are on the keyboard. I also want to point out that security measures need to be on both the frontend of the website and the backend. If only the frontend is preventing certain characters but the backend allows them, it is only a matter of time before an attacker will find this out.

SQL injection can be prevented very easily with parameterized queries. Any database abstraction library worth its salt has a way to easily do this. The idea is that all user input is treated as data. Even if they have provided commands, the database doesn't substitute the user input as part of the query.

Below is a simple Python script that asks for a username and password and then runs a query. I have left the unsafe way to do this commented out to show the difference between the wrong way and a parameterized query.

```python
username = input('username ?')
password = input('password ?')
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Example: Ensure the users table exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
""")
conn.commit()

# UNSAFE (example only): vulnerable to SQL injection
# cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")

# SAFE: Use placeholders (?) to parameterize
cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
result = cursor.fetchone()

conn.close()

if result:
    print(f"Welcome, {username}")
else:
    print(f"Invalid username or password")
```

### Command Injection Example

I can't emphasize this enough, allowing users to run abitrary system commands is a **really bad idea**. Even hiding these forms in directories with strange names is bad. Any time a website for a capture the flag event has a form that runs system commands, I know that I am just a few steps and attempts from having a shell on their machine. It is best to treat user input as unsafe and not run commands.

### File Upload Forms

File upload forms can provide a foothold for uploading malicious scripts and files. If the form does not properly validate the uploaded file, an attacker can upload scripts that can provide remote code execution or allow a reverse shell. File upload forms are a common place to get a foothold in a capture the flag event. Here is a file upload form example to help explain this:

Imagine a capture the flag box that has a file upload form. The file upload form code that uploads files does not check file extensions or if the file is actually a .png, .jpeg or .jpg file. This means that I can upload a PHP reverse shell and tell the site that it is an image file. Once the file has been uploaded, I can then ask the server for the file I just uploaded to the `/uploads` directory.

The [PHP Reverse Shell](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php) makes it easy to get a reverse shell for systems that are vulnerable.

I first grab the PHP reverse shell file from the repository above or the one on the TryHackMe attack box located at `/usr/share/webshells/php/php-reverse-shell.php`. There are only 2 lines that need to be altered in this file. They are the lines that define the `$ip` and `$port` variables.

I set those to the `$ip` value to my attack box's ip address and the `$port` value to 4444.

I'll run a netcat listener with the following:

```bash
$ nc -lnvp 4444
```

From here I'll see if I can upload the shell file. I'll start by seeing if I can just upload it with a .php extension. If that fails I'll try different file extensions hoping that they have not accounted for it. Here is the list of file extensions that I try:

- `.php`
- `.php3`
- `.php4`
- `.php5`
- `.php7`
- `.phtml`
- `.phps`
- `.pht`
- `.phar`

In the event that they want a specific file extension like .jpg, I will try the following extensions:

- `.php.jpg`
- `.php.jpeg`
- `.php%00.jpg`
- `.jpg.php` (or some variant of the php extension list above).

The `%00` is a null character for a url and marks the end of the string. Meaning that once it is uploaded the file will not have anything after the `%00`.

I am at the mercy of however the server side was implemented. They might only be checking for .jpg in the file name or they might want it to end with that. The server side might also try to validate that the file starts with the correct file signature. The list of file signatures can be [found here](https://en.wikipedia.org/wiki/List_of_file_signatures). These file signature can be set with a hex editor. I only have to set the first few byes that are mentioned in this link.

### Security Measures

There are checks that can be done to help prevent file upload abuse. As mentioned above, do not rely on just the file extension. Here are some things that can be done:

- Have an allowlist of file types (.jpg, .png, .pdf, etc...)
- Validate on the server side with MIME type checks.
- Verify file headers. A list can be found [here](https://en.wikipedia.org/wiki/List_of_file_signatures)
- Rename uploaded file names (i.e. evilscript.jpg → 2a943bff-9034-40cb-9abc-3a95b20a82df.jpg). An attacker now has to get the file name in order to call it.
- Store files in a directory outside the webroot. This way the web server cannot directly access them and run the malicious script.
- If possible, access the files with a proxy script.
- Make sure that the uploaded file can't be executed as code (e.g., not `+x` file permissions).
- Disable script execution on the uploads folder in Apache/Nginx.
- Limit the size of the file being uploaded to prevent denial of service attacks.
- Scan the files with antivirus/malware detection tools.
- Rate limit uploads from a single IP address to dential of service attacks.
- Strip metadata from image/pdf files since it can contain malicious payloads.
- Disallow special characters in file names like `../` and `%00` or unicode tricks. This prevents path traversal and null byte injection attacks.
- Store files in randomized subdirectories to make guessing where the file is stored harder.
- Serve files from a download endpoint such as `download_file.php?id=123`. This prevents direct browsing in the `uploads/` directory.
- Ensure that only logged in users are able to upload a file. This helps add logging and traceability to the system.
- Track upload attempts, rejections and anomalies. This includes repeated attempts to bypass filters.
- Strip dangerous content from pdfs, Office documents and Excel files as these can contain embedded scripts and macros.
- Prevent double extensions (i.e. `file.php.jpg` or `file.jpg.php`).
- Run image libraries like ImageMagick or PIL inside restricted environment (low privilege user or in a container).
- Ensure the endpoint is covered by a web application firewall.
