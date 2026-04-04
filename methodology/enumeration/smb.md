# Enumeration - SMB

[Back to methodology](/methodology/README.md)

- Server Message Block (SMB) is a client-server protocol that regulates files, directories, and network resource (printers, routers, etc...)
- It is generally associated with Windows but Samba can be used with Linux to provide SMB
- Access rights are controlled by Access Control Lists (ACL). These right can be fine grained (read, execute, full access, etc...)
- Rights correspond to rights of the share and not the rights of the user locally on the server
- In a network each host is part of a workgroup. A workgroup is a collection of computers and resources in an SMB network

## Samba

Samba is used by Linux and other Unix systems to be able to use SMB. It uses the Common Internet File System (CIFS) network protocol. CIFS is a dialect of the SMB protocol.

## Nmap Scan

```bash
nmap -sC -sV -A -p139,445 <target>
```

## View Anonymous Shares

```bash
smbclient -N -L //10.10.1.101

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Print Drivers
        home            Disk      Main Directory
        dev             Disk      Development Notes
        sensitive       Disk      Pillage Me
        IPC$            IPC       IPC Service (DEVSM)
```

The `-N` option tells smbclient to connect as anonymous. The `-L` option tells smbclient to list all the shares.

## Connect To Specific Share

```bash
smbclient //10.10.1.101/sensitive
```

## List Contents Of Share

```bash
smb: \> ls
```

## Download A File

```bash
smb: \> get my_sensitive_file.txt
```

## Rpcclient - Connect

```bash
rpcclient -U "" 10.10.1.101
```


## Rpcclient - List Shares

```bash
rpcclient $> srvinfo
	SomeShare      Wk Sv PrQ Unx NT SNT Some Company Share (Samba, Ubuntu)
	platform_id     :	500
	os version      :	6.1
	server type     :	0x809a03
```

## Rpcclient - Enumerate Domains

```bash
rpcclient $> enumdomains
name:[SomeShare] idx:[0x0]
name:[Builtin] idx:[0x1]
```

## Rpcclient - Query Domain Info

```bash
rpcclient $> querydominfo
Domain:		Operations
Server:		SomeShare
Comment:	Some Company Share (Samba, Ubuntu)
Total Users:	0
Total Groups:	0
Total Aliases:	0
Sequence No:	1775319684
Force Logoff:	-1
Domain Server State:	0x1
Server Role:	ROLE_DOMAIN_PDC
Unknown 3:	0x1
```

## Rpcclient - Enumerate All Netshares

```bash
rpcclient $> netshareenumall
netname: print$
	remark:	Printer Drivers
	path:	C:\var\lib\samba\printers
	password:	
netname: oursmbshare
	remark:	Our Company Share
	path:	C:\home\sambauser\
	password:	
netname: IPC$
	remark:	IPC Service (Our Company Share (Samba, Ubuntu))
	path:	C:\tmp
	password:	
```

## Rpcclient - Get Netshare Information By Name

```bash
rpcclient $> netsharegetinfo oursmbshare
netname: oursmbshare
	remark:	Our Company Share
	path:	C:\home\sambauser\
	password:	
	type:	0x0
	perms:	0
	max_uses:	-1
	num_uses:	1
revision: 1
type: 0x8004: SEC_DESC_DACL_PRESENT SEC_DESC_SELF_RELATIVE 
DACL
	ACL	Num ACEs:	1	revision:	2
	---
	ACE
		type: ACCESS ALLOWED (0) flags: 0x00 
		Specific bits: 0x1ff
		Permissions: 0x1f01ff: SYNCHRONIZE_ACCESS WRITE_OWNER_ACCESS WRITE_DAC_ACCESS READ_CONTROL_ACCESS DELETE_ACCESS 
		SID: S-1-1-0
```

## Rpcclient - Enumerate Users

```bash
rpcclient $> enumdomusers
```

## Clients To Interact With SMB

- Nmap
- RPCclient
- Impacket
- SMBmap
- CrackMapExec
- Enum4Linux-ng
