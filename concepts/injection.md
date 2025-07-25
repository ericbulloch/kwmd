# Injection

Injection is when input either from a user or an external system is processed by a program as an executable command. Attackers are able to use the natural processing of the program to run commands that it normally wouldn't. The execution of commands can be things like queries to a database, reading files, creating archives, downloading files, uploading files and escalating privileges.

For many years, this was the number one item on OWASP Top Ten lists. The main cause of this vulnerability is that programs and systems take input from users or systems and fail to sanitize or validate it. Many injection vulnerabilities can be prevented by limiting what users and systems are able to provide as input.

Some of the more common injection types include:

- SQL Injection
- Cross-Site Scripting
- Server Side Template Injection
- Remote File Injection
- Shell Injection
