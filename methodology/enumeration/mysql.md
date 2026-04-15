# Enumeration - MySQL

[Back to methodology](/methodology/README.md)

Port(s): 3306

## Nmap Scan

```bash
nmap -sC -sV -A -p336 <target>
```

or

```bash
nmap -sV -A -p336 --script mysql* <target>
```

## Connect To MySQL Database

The following command connections to the database at 10.129.10.100 as the user root:

```bash
mysql -u root -h 10.129.10.100
```

## Connect To MySQL Database With Password

The following command connections to the database at 10.129.10.100 as the user root with the password MyPa55w0rd:

```bash
mysql -u root -pMyPa55w0rd -h 10.129.10.100
```
