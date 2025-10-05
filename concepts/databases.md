# Databases

- [Introduction](#introduction)
- [Database Commands](#database-commands)

## Introduction

Databases are where information is stored. They store information like users, products, shopping carts, shipments, customers, clients and payment information. When people talk about hackers getting people's information they are talking about how hackers took that information from a database.

## Database Commands

All database management systems (DBMS) have similar functionality that users need to use the database. I have compiled a list here and the specific ways to do these things are listed below for the more common DBMS systems. Here is what gets covered:

- List databases
- Create database
- Delete database
- List tables
- Create table
- Delete table
- Add index
- Remove index
- List users
- Create user
- Delete user
- List permissions
- Add permission
- Delete permission
- Assign permission to user
- Revoke permission from user
- Select data from table
  - All data from record
  - Some data from record
- Join multiple tables
  - Inner join
  - Outer join
  - Left join
  - Select records from multiple tables
- Insert record into table
- Update record in table
- Delete record from table
- Limit the number of records
- Group records
- Order records
- Count records
- Max value
- Min value
- Select distinct values
- Filter records
  - Filter exact match
  - Filter fuzzy match
  - Filter records between dates
  - Filter value in list

## MySQL

### List database.

```sql
SHOW DATABASES;
```

### Create database.

```sql CREATE DATABASE kwmd;```

### Delete database.

```sql
DROP DATABASE kwmd;
```

### List tables.

```sql
SHOW TABLES;
```

### Create table.

```sql
CREATE TABLE users(
  id INT AUTO_INCREMENT,
  email VARCHAR(250),
  password VARCHAR(250),
  PRIMARY KEY(id)
);
```

### Delete table

```sql
DROP TABLE users;
```

### Add index

```sql
CREATE INDEX users__email ON users(email);
```

### Remove index

```sql
DROP INDEX users__email ON users;
```

### List users

```sql
SELECT user, host FROM mysql.user;
```

### Create users

```sql
CREATE USER 'kwmd'@'localhost' IDENTIFIED BY 'mySuperP@Ss\/\/0r|)';
```

### Delete users

```sql
DROP USER 'kwmd'@'localhost';
```

### List permissions

```sql
SHOW GRANTS FOR 'kwmd'@'localhost';
```

### Add permission

```sql
GRANT ALL PRIVILEGES ON * . * TO 'kwmd'@'localhost';
FLUSH PRIVILEGES;
```

### Delete permission

```sql
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'kwmd'@'localhost';
```

## PostgreSQL

## SQLite
