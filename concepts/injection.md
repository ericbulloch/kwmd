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

Because databases are so widely used SQL Injection (sometimes styled SQLi) attacks remain as one of the most prevelent and dangerous cybersecurity threats. The idea is very simple. A program takes untrusted input from a user or another system and inserts that input into a sql command. That input will alter the meaning of the original sql command. It will run a sql command that was not intended to be ran by the program.

### SQL Injection Examples

Consider the following SQL table:

| id | username | password | role |
| --- | --- | --- | --- |
| 1 | admin | f702df58bd23c8a4dc7162c9d1b1d333 | administrator |
| 2 | bob | 96293e35600c05f1e19f0964c4232b07 | user |
| 3 | alice | c57b2cf12ff14d748ea68b41c8093bf1 | user |

Please ignore the MD5 hashed passwords, the point of this table is to provide a table an data to demonstrate SQL injection.

Consider the following PHP script snippet:

```php
$config = parse_ini_file('config.ini', true);
$connection = new mysqli($config['database']['host'], $config['database']['user'], $config['database']['password'], $config['database']['database']);

$username = $_GET['user_id'];

$sql = "SELECT * FROM users WHERE id = $username";

$result = $connection->query($sql);

$data = array();

if ($result->num_rows > 0) {
  while ($row = $result->fetch_assoc()) {
    $data[] = $row
  }
}

$json_data = json_encode($data);
header('Content-Type: application/json');
echo $json_data;

$connection->close();
```

Here is a summary of what this script is doing:

- Creating a database connection.
- Grabbing the user_id that the user supplied.
- Putting that user_id into a SQL command.
- Running that SQL command on the database.
- Converting the result from the database to json.
- Printing the json result to the user.

The SQL command will get passed to the database and it will execute with whatever user_id was passed from the user. Notice that there is no validation. The input from a user is blindly trusted. This doesn't even check to make sure that the user_id provided is an integer like the database is expecting.

There are are few scenarios to consider regarding the user_id input. First, if the user passes in an integer value, one of two things can happen. It will either find a record that matches the id or it will not. If a user passes in the value of 3, the database will return the record for alice. If they pass in the value of 4, the database will return nothing.

What if they don't pass in an integer? What if they pass in a string? Better yet, what if they pass in another SQL command? This is the idea of sql injection. Here are some different ways this script could be used for a SQL injection attack:

#### Get all records

If the user_id that was supplied to the script was "'a' or 1 = 1", the script would return all records. The SQL statment would become the following:

```sql
SELECT * FROM users WHERE id = 'a' or 1 = 1
```

The database would look up a user with the id 'a' and not find anything, then it would see the condition of 1 = 1 and return all records in the users table because 1 = 1 is the same as saying true. Since each record will now match to true, that record will be included in the results.

The user would see a result on the web page that looked like this:

```json
[
  {
    "id": "1",
    "username": "admin",
    "password": "f702df58bd23c8a4dc7162c9d1b1d333",
    "role": "administrator"
  },
  {
    "id": "2",
    "username": "bob",
    "password": "96293e35600c05f1e19f0964c4232b07",
    "role": "user"
  },
  {
    "id": "3",
    "username": "alice",
    "password": "c57b2cf12ff14d748ea68b41c8093bf1",
    "role": "user"
  }
]
```

#### Getting admin users

If the user_id that was supplied to the script was "'a' or role = 'admin'", the script would return all records that have an admin role value. The SQL statment would become the following:

```sql
SELECT * FROM users WHERE id = 'a' or role = 'admin'
```

The database would look up a user with the id 'a' and not find anything, then it would see the condition of role = 'admin' and return all records in the users table that have an admin role (in this case one record).

The user would see a result on the web page that looked like this:

```json
[
  {
    "id": "1",
    "username": "admin",
    "password": "f702df58bd23c8a4dc7162c9d1b1d333",
    "role": "administrator"
  }
]
```

#### Dropping a table

If the user_id that was supplied to the script was "'a'; DROP TABLE users", the script would return drop the users table. Yikes! The SQL statment would become the following:

```sql
SELECT * FROM users WHERE id = 'a'; DROP TABLE users
```

As you can see the single statement now became two statements. The database would run the first statement and look up a user with the id 'a' and not find anything. Then it would run the second statement and drop the users table.

If I recall, MySQL doesn't return anything when a table is dropped. I would expect the user to see a result on the web page that looked like this:

```json
[]
```

The next time someone tried to look up a user, an execption would get thrown because the table does not exist. Since this is a critical table for the application, I would expect most parts of the application to break.

### SQL Injection Prevention

SQL injection attacks mitigations are very well documented. The problem is when untrusted data is used as input for a query to the database.

#### Validate input

The examples above could have been easily prevented by checking if the user_id provided was an integer. None of the attacks would have even hit the database. The script could have been changed to the following:

```php
$config = parse_ini_file('config.ini', true);
$connection = new mysqli($config['database']['host'], $config['database']['user'], $config['database']['password'], $config['database']['database']);

if (filter_var($_GET['user_id'], FILTER_VALIDATE_INT) === false) {
  throw new InvalidArgumentException("Invalid user_id provided: " . $_GET['user_id']);
}

$username = (int)$_GET['user_id'];

$sql = "SELECT * FROM users WHERE id = $username";
...
```

The user_id can now be trusted because we can be assured it is an integer.

#### Parameterized query

Scripts can also used parameterized queries. A parameterized query uses placeholders in the SQL command which are then replaced with actual values at runtime. This ensures that user input is treated as data rather than executable code, thus mitigating the risk of SQL injection.

To use a parameterized query (PHP calls it a prepared statement) the script could be changed to:

```php
$config = parse_ini_file('config.ini', true);
$connection = new mysqli($config['database']['host'], $config['database']['user'], $config['database']['password'], $config['database']['database']);

$username = $_GET['user_id'];

$sql = "SELECT * FROM users WHERE id = ?";
$statement = $conn->prepare($sql);

if ($statement === false) {
  die("Error preparing statement")
}

// Bind parameters to the placeholders
// The 'i' string specifies the types of the bound variables:
// 's' for string, 'i' for integer, 'd' for double, 'b' for blob
$statement->bind_param('i', $_GET['user_id']);

$statement->execute();
$result = $statement->get_result();

$data = array();

if ($result->num_rows > 0) {
  while ($row = $result->fetch_assoc()) {
    $data[] = $row
  }
}

$json_data = json_encode($data);
header('Content-Type: application/json');
echo $json_data;

$statement->close();
$connection->close();
```
