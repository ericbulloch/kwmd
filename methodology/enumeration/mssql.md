# Enumeration - MSSQL

[Back to methodology](/methodology/README.md)

Port(s): 1433

- MSSQL will likely be running as `NT SERVICE\MSSQLSERVER` when installed
- Often uses Windows Authentication, and by default, encryption is not enforced when attempting to connect

## Nmap Scan

```bash
nmap -sC -sV -A -p1433 <target>
```

or

```bash
nmap --script ms-sql-info,ms-sql-empty-password,ms-sql-xp-cmdshell,ms-sql-config,ms-sql-ntlm-info,ms-sql-tables,ms-sql-hasdbaccess,ms-sql-dac,ms-sql-dump-hashes --script-args mssql.instance-port=1433,mssql.username=sa,mssql.password=,mssql.instance-name=MSSQLSERVER -sV -p 1433 <target>
```

## Connect With mssqlclient.py

### Locate mssqlclient.py

Running the following command will show where the `mssqlclient.py` file is located

```bash
locate mssqlclient.py
/usr/share/doc/python3-impacket/examples/mssqlclient.py
```

To connect to MSSQL on 10.129.10.100 with username kwmd and password VeryS3cret run the following command:

```bash
python3 /usr/share/doc/python3-impacket/examples/mssqlclient.py kwmd:VeryS3cret@10.129.10.100 -windows-auth
```
