# Enumeration - SMB

[Back to methodology](/methodology/README.md)

- Server Message Block (SMB) is a client-server protocol that regulates files, directories, and network resource (printers, routers, etc...)
- It is generally associated with Windows but Samba can be used with Linux to provide SMB
- Access rights are controlled by Access Control Lists (ACL). These right can be fine grained (read, execute, full access, etc...)
- Rights correspond to rights of the share and not the rights of the user locally on the server
- In a network each host is part of a workgroup. A workgroup is a collection of computers and resources in an SMB network

## Samba

Samba is used by Linux and other Unix systems to be able to use SMB. It uses the Common Internet File System (CIFS) network protocol. CIFS is a dialect of the SMB protocol.

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

## Clients To Interact With SMB

- Nmap
- RPCclient
- Impacket
- SMBmap
- CrackMapExec
- Enum4Linux-ng
