# Injection

Injection is when input either from a user or an external system is processed by a program as an executable command. Attackers are able to use the natural processing of the program to run commands that it normally wouldn't. The execution of commands can be things like queries to a database, reading files, creating archives, downloading files, uploading files and escalating privileges.

For many years, this was the number one item on OWASP Top Ten lists. The main cause of this vulnerability is that programs and systems take input from users or systems and fail to sanitize or validate it. Many injection vulnerabilities can be prevented by limiting what users and systems are able to provide as input.

Some of the more common injection types include:

- SQL Injection
- Cross-Site Scripting
- Server Side Template Injection
- Remote File Injection
- Shell Injection

## SQL Injection

Database commands are used to create, read, update and delete information within the database. Theses commands are very well defined. The syntax of the commands varies slightly between different database vendors.

Because databases are so widely used SQL Injection attacks might be the most famous type of injection attack. The idea is very simple. A program takes untrusted input from a user or another system and inserts that input into a sql command. That input will alter the meaning of the original sql command. It will run a sql command that was not intended to be ran by the program.

### SQL Injection Examples

Consider the following SQL table:

```bash
| id | username | password | role |
| --- | --- | --- | --- |
| 1 | admin | f702df58bd23c8a4dc7162c9d1b1d333 | administrator |
| 2 | bob | 96293e35600c05f1e19f0964c4232b07 | user |
| 3 | alice | c57b2cf12ff14d748ea68b41c8093bf1 | user |
```

A PHP program could have the following SQL command that it will run:

```php
$username = $_GET['user_id'];
$sql = "SELECT * FROM users WHERE id = $username";
```

That SQL command will get passed to the database and it will execute with whatever was passed from the user. Notice that there is no validation. The input from a user is blindly trusted. This doesn't even check to make sure that the user_id provided is an integer like the database is expecting.

There are are few scenarios to consider. First, if the user passes in an integer value, one of two things can happen. It will either find a record that matches the id or it will not. The second scenario is where strange things can happen.

So if a user passes in the value of 3, it will return the record for alice. If they pass in the value of 4, it will return nothing. Very straight forward and easy.

What if they don't pass in an integer? What if they pass in a string? Better yet, what if they pass in another SQL command?
