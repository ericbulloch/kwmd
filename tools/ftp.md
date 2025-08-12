# FTP

- [Introduction](#introduction)
- [Anonymous Login](#anonymous-login)
- [Login With Credentials](#login-with-credentials)
- [Navigation](#navigation)
- [Downloading File](#downloading-file)
- [Viewing File Contents Without Downloading File](#viewing-file-contents-without-downloading-file)
- [Connecting to Non-Standard Port](#connecting-to-non-standard-port)
- [Upload File](#upload-file)

## Introduction

FTP is a very common way in the real world for businesses to exchange files with each other without having to integrate with an API. It is also a place where a lot of people store a lot of files in capture the flag events that are loaded with juicy bits of information.

## Anonymous Login

It is very easy to log into an FTP server as an anonymous user. Here is a full example:

```bash
$ ftp 10.10.1.1
Connected to 10.10.1.1.
220 (vsFTPd 3.0.3)
Name (target.thm:root): anonymous
331 Please specify the password.
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
```

I run the command ftp and then the host I want to connect to. From here, I enter `anonymous` as the username. **Note that I didn't use blank**, that would have used the username from my machine (in this case, root). After I type `anonymous` it asks for a password. I usually leave it blank, since it is an anonymous login any password will work. If everything went according to plan I will get the 230 status code for a successful login.

## Login with Credentials

For this example, I am going to log in with the username `jenny` and the password `letmein1`.

```bash
$ ftp 10.10.1.1
Connected to 10.10.1.1.
220 (vsFTPd 3.0.3)
USER jenny
331 Please specify the password.
PASS letmein1
230 Login successful.
```

## Navigation

I navigate using the `cd` command to change directories, just like in Linux. The `ls` command is used to view the contents of a directory just like Linux.

## Downloading File

Downloading a file from the ftp server to my machine is very simple. If I wanted to save the `note.txt` file that is in the current directory of the FTP server into the directory on my machine I was in when I ran the ftp command, I would run:

```bash
ftp> get note.txt
local: note.txt remote: note.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for note.txt (418 bytes).
226 Transfer complete.
418 bytes received in 0.06 secs (6.8225 kB/s)
```

If I wanted to specify where the save gets saved on my machine, I can just tell the command where to save the file:

```bash
ftp> get note.txt /root/secret.txt
local: /root/secret.txt remote: note.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for note.txt (418 bytes).
226 Transfer complete.
418 bytes received in 0.06 secs (6.8225 kB/s)
```

This will save the note.txt file on the server as secret.txt on my machine in the /root directory.

### Destination File Path Does Not Exist

If the destination path that was provided does not exist, I will get an error that says `No such file or directory`. In the following example, the `Documents` folder in the /root directory does not exist. This is the input and the error:

```bash
ftp> get note.txt /root/Documents/secret.txt
local: /root/Documents/secret.txt remote: note.txt
local: /root/Documents/secret.txt: No such file or directory
```

## Viewing File Contents Without Downloading File

Viewing files is different in FTP. I have provided some examples of how not to do it:

```bash
ftp> less note.txt
?Invalid command
ftp> head note.txt
?Invalid command
ftp> nano note.txt
?Invalid command
ftp> vim note.txt
?Invalid command
ftp> tail note.txt
?Invalid command
ftp> more note.txt
?Invalid command
```

To view a file's contents without downloading it to my machine, I run the same command that was used to download the file except I add a `-` character at the end. Here is the command to view the file named task.txt:

```bash
ftp> get task.txt -
remote: task.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for task.txt (68 bytes).
1.) Make more $$$$$.
2.) Plan a big party with all the peeps.

kwmd
226 Transfer complete.
68 bytes received in 0.09 secs (0.7435 kB/s)
```

## Connecting to Non-Standard Port

In the example above I connected to port 21 which is the standard ftp port. If I was connecting to a server that was running on a different port like 5555. I would need to use the following to connect:

```bash
$ ftp
ftp> open 10.10.1.1 5555
Connected to 10.10.1.1
```

or

```bash
$ ftp 10.10.1.1 2100
Connected to 10.10.1.1
```

## Upload File

Uploading a file is very simple. In this example, I want to upload a file named shell.php. After I log into the system and navigate to the appropriate directory on the FTP server, I run the following command:

```
ftp> put shell.php
local: shell.php remote: shell.php
200 PORT command successful. Consider using PASV.
```

Another approach is using the EOF (end of file) markers:

```bash
$ ftp -n <<EOF
open 10.10.1.1
user jenny letmein1
put shell.php
EOF
```
