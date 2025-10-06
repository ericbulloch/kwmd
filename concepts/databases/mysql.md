# MySQL

Here are the commands for MySQL that will execute the tasks [found here](/concepts/databases.md#database-commands).

## List database.

```sql
SHOW DATABASES;
```

## Create database.

```sql CREATE DATABASE kwmd;```

## Delete database.

```sql
DROP DATABASE kwmd;
```

## List tables.

```sql
SHOW TABLES;
```

## Create table.

```sql
CREATE TABLE users(
  id INT AUTO_INCREMENT,
  email VARCHAR(250),
  password VARCHAR(250),
  PRIMARY KEY(id)
);
```

## Delete table

```sql
DROP TABLE users;
```

## Add index

```sql
CREATE INDEX users__email ON users(email);
```

## Remove index

```sql
DROP INDEX users__email ON users;
```

## List users

```sql
SELECT user, host FROM mysql.user;
```

## Create users

```sql
CREATE USER 'kwmd'@'localhost' IDENTIFIED BY 'mySuperP@Ss\/\/0r|)';
```

## Delete users

```sql
DROP USER 'kwmd'@'localhost';
```

## List permissions

```sql
SHOW GRANTS FOR 'kwmd'@'localhost';
```

## Add permission

```sql
GRANT ALL PRIVILEGES ON * . * TO 'kwmd'@'localhost';
FLUSH PRIVILEGES;
```

## Delete permission

```sql
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'kwmd'@'localhost';
```

## Select data from table

### All data from record

```sql
SELECT * FROM users;
```

### Some data from record

```sql
SELECT id, email FROM users;
```
