# SMB (Server Message Block)

- [Introduction](#introduction)
- [Enumeration](#enumeration)
- [Downloading Individual Files](#downloading-individual-files)
- [Downloading Folders](#downloading-folders)

## Introduction

Server Message Block is commonly used in capture the flag events. It allows users to share files and printers across the network. Enumerating SMB and Samba folders is a gold mine, but I forget the syntax and tools all the time.

## Enumeration

It is important to find out what disks are available and if any of them do not require me to log in. I use the smbmap tool to solve this. The following command will discover what shares are available and what the permissions for them are:

```bash
$ smbmap -H target.thm
```

The output will look something like the following:

```bash
[+] Finding open SMB ports...
[+] Guest SMB session established on target.thm...
[+] IP: 10.10.22.112:445           Name: storage
        Disk                                              Permissions
        ----                                              -----------
        print$                                            NO ACCESS
        anonymous                                         READ ONLY
        mrburns                                           NO ACCESS
        IPC$                                              NO ACCESS
```

The above example tells me that the `anonymous` disk does not require authentication. Therefore, I can view the contents of that disk.

## Connecting to Disk

To connect to an anonymous disk, I use the smbclient tool. It makes it easy to browse and download files after enumeration is complete. I connect to the anonymous disk above with:

```bash
$ smbclient //target.thm/anonymous/ -N
```

When it successfully finishes, it will change the command prompt to:

`smb: \>`

Now I can use the `ls` and `cd` commands to look around the disk.

## Downloading Individual Files

I often need to download the contents of a disk onto my machine for analysis. If the file on the disk is called important.txt, I would run the following command (I included the smb prompt in the beginning of the command):

```bash
smb: \> get important.txt
```

This will download the important.txt file to the directory I was in on my machine when I connected to the disk.

## Downloading Folders

More often than not, I really just want to download a folder rather than running the above command multiple times. This is still easy, but I run a few more commands. I go into the folder on the disk that has all the files and folders I want. I then run the following commands (I included the smb prompt in the beginning of the commands):

```bash
smb: \> recurse on
smb: \> prompt off
smb: \> mget *
```

Here is an explanation of these commands:

- `recurse on` will grab all the files and folders inside the folders in this directory.
- `prompt off` will not ask me if I want to download each file.
- `mget *` targets all the files and folders in this directory.
