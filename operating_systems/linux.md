# Linux

I wanted to list some concepts, terms and flows that are specific to Linux. Learning more about Linux has made me a better and more effcient pentration tester. There is a lot of information to cover. I use this page as a reference.

## Table of Contents

- [Basic Commands](/operating_systems/linux.md#basic-commands)
- [Directories](/operating_systems/linux.md#directories)
- [Groups](/operating_systems/linux.md#groups)
- [Permissions](/operating_systems/linux.md#permissions)
- [Privilege Escalation](/operating_systems/linux.md#privilege-escalation)
- [Systemctl](/operating_systems/linux.md#systemctl)
- [Crons](/operating_systems/linux.md#crons)
- [LXC](/operating_systems/linux.md#lxc)

## Basic Commands

There are some commands that I use all the time. I have put together a list of the most common commands I use while doing a capture the flag event. All the commands have optional flags that can enhance what the commands do. When I need help with a command I run `man <command>` to get a more detailed description of each command. Here are the most common commands that I use:

| Command | Purpose |
| ------------- | -------------- |
| `ls` | Lists files and directories in the current location. |
| `cd` | Changes the current directory. |
| `pwd` | Prints the current working directory. |
| `mkdir` | Creates a new directory. |
| `rm` | Removes files or directories. |
| `cp` | Copies files or directories. |
| `mv` | Moves or renames files and directories. |
| `touch` | Creates an empty file or updates timestamps. |
| [`cat`](/tools/cat.md) | Displays file contents. |
| `head` | Used to look at the first lines of a file. |
| `tail` | Used to look at the last lines of a file. |
| `more` | Used to show a page of text at a time. A kind of interactive cat. |
| `less` | Similar to more but with filtering for terms. |
| `nano` or `vim` | Opens a text editor, nano is more beginner friendly. |
| `chmod` | Changes file permissions. |
| `chown` | Changes file ownership. |
| [`find`](/tools/find.md) | Searches for files and directories. |
| [`grep`](/tools/grep.md) | Searches text using patterns (regular expressions also known as regex). |
| `ps aux` | Lists all running processes. |
| `kill` | Terminates processes by PID or name. |
| `whoami` | What user am I logged in as. |
| `which` | Used to display the location of a binary. |
| `echo` | Used to print text to the terminal but can be redirected to a file. |

## Directories

It helps to have a basic understanding of the directories at the root `/` level of Linux. Directories are case sensitive on Linux. I could have multiple videos directories in a single directory that are only different with their casing. For example, I could have a media directory and inside that directory I could have three folders with the name: videos, VIDEOS and Videos. Here are the directories and a description of what they do:

| Directory | Description |
| ------------- | -------------- |
| `/bin` | Essential user binaries (e.g., `ls`, `cp`, `mv`) needed for basic system operation. Most of the commands in the previous section are here. |
| `/boot` | Files needed for booting the system (e.g., GRUB, Linux kernel). |
| `/dev` | Device files (e.g., `/dev/sda` for disks, `/dev/null`).  |
| `/etc` | System-wide configuration files and settings. These files are critical for the system. |
| `/home` | User home directories (e.g., `/home/kwmd`). The `root` user does not have their home directory here. |
| `/lib` | Essential shared libraries used by binaries in `/bin` and `/sbin`. |
| `/lib64` | 64-bit versions of libraries (on 64-bit systems). |
| `/media` | Mount point for removable media (e.g., USB drives, CDs). |
| `/mnt` | Temporary mount point for filesystems (manually mounted drives). |
| `/opt` | Optional or third-party software packages. |
| `/proc` | Virtual filesystem providing process and kernel information. In Linux everything is a file including processes. |
| `/root` | Home directory of the `root` user (not the same as `/`). |
| `/run` | Runtime variable data (e.g., PID files, sockets). |
| `/sbin` | System binaries (administrative commands, e.g., `reboot`, `iptables`). |
| `/srv` | Data for services like FTP, HTTP (e.g., `/srv/www`). |
| `/sys` | Virtual filesystem exposing system and hardware info. |
| `/tmp` | Temporary files (often cleared on reboot). Usually all users have read and write permissions in this directory. |
| `/usr` | Secondary hierarchy for user programs and data (e.g., `/usr/bin`, `/usr/lib`). |
| `/var` | Variable files (logs, mail, spool files, etc.). |

During a penetration test, knowing which directories on a Linux system contain potentially sensitive or valuable information can help with privilege escalation, lateral movement, or data exfiltration. Here are some of the valuable contents in these directories that I am looking for when I do a penetration test:

| Directory | What to Look For |
| ------------- | -------------- |
| `/bin`, `/sbin`, `/usr/bin`, `/usr/sbin` | SUID/SGID binaries (e.g., `find / -perm -4000 2>/dev/null`). Custom or unusual binaries that may reveal misconfigurations or be exploitable. |
| `/boot` | Kernel version (vmlinuz-*) may help identify known kernel exploits. Grub configs (grub.cfg) may expose passwords or kernel boot options. |
| `/dev` | Access to devices like /dev/mem, /dev/kmem, or disks (if permissions are misconfigured). Sometimes misconfigured device files can lead to privilege escalation. |
| `/etc` | Credentials in config files (e.g., /etc/passwd, /etc/shadow, /etc/fstab). Misconfigured services (e.g., Apache, SSH, cron jobs). Backup files or .old, .bak, .save versions of configs. Misconfigured sudoers file (/etc/sudoers). |
| `/home` | User SSH keys (~/.ssh/id_rsa, authorized_keys). Saved credentials in history or config files (e.g., .bash_history, .gitconfig). Enumerate all users and check for global-readable files. |
| `/lib`, `/lib64`, `/usr/lib` | Look for malicious shared libraries or LD_PRELOAD abuse opportunities. Checking if libraries have known vulnerabilities for privilege escalation. |
| `/media`, `/mnt` | Mounted drives, USBs, or file shares that may contain sensitive data or credentials. Misconfigured mounts that allow unauthorized access. |
| `/opt` | Third-party or custom applications often reside here. Check for hardcoded credentials, scripts, misconfigurations. Exploitable software with escalated permissions. |
| `/proc` | Process info, environment variables (/proc/*/environ), open file descriptors, command-line args. May reveal passwords, tokens, or useful debug info. Inspect /proc/net/tcp, /proc/[pid]/fd/, /proc/[pid]/cmdline. |
| `/root` | Everything in this directory is gold: history files, SSH keys, scripts, notes. Only accessible if you get root—but once you do, enumerate it fully. Usually being the root user and reading a file from this directory is the goal of a capture the flag. |
| `/run` | Runtime data like PID files and sockets. Active sessions or credentials in memory may show up here. |
| `/srv` | Web server data (e.g., /srv/www) or FTP files. Look for exposed sensitive web files, backups, or logs. |
| `/sys` | Hardware and system configuration. Typically less valuable, but may reveal kernel modules, USB devices, or info for kernel exploits. |
| `/tmp` | Global-writable directory that is often used for privilege escalation. Look for temp files with credentials, open sockets, or running binaries. |
| `/var` | Logs are stored in the /var/log/ directory: check the log files of various services (auth.log, secure, apache2/, mysql/, etc...). Mail is stored in /var/mail: users' mail may contain sensitive information like usernames and passwords. Cron jobs are stored in /var/spool/cron: privileged recurring tasks that can sometimes be hijacked. Databases are stored can be stored in /var/lib/mysql: configuration files and backups files might be in here. Website files are stored in /var/www: configuration files can contain sensitive information. |

## Groups

There are a number of groups that are common on Linux system. Knowing what they do has helped during capture the flag events. Here are some common ones that I see often:

| Group Name | Purpose |
| ------------- | -------------- |
| `root` | Superuser group—full system control. |
| `users` | Default group for regular users on many distros. |
| `adm` | Access to system logs (e.g., /var/log/syslog, /var/log/messages). |
| `sudo` or `wheel` | Allows executing commands as root using sudo. The wheel group is used on Red Hat-based systems. |
| `staff` | Administrative group with limited elevated permissions. |
| `nogroup` | Assigned to processes/users with no matching group. |
| `daemon` | Common group for background system services. |
| `tty` | Grants access to terminal devices. |
| `disk` | 	Grants raw disk device access. Can be abused for privilege escalation. |
| `mail` | Access to email services or /var/mail/. |
| `postfix` | Group for the Postfix mail server. |
| `ssh` | Used internally by SSH daemons (varies by distro). |
| `crontab` | Controls access to scheduled cron jobs. |
| `messagebus` | D-Bus messaging system group. |
| `systemd-journal` | Read access to the systemd journal logs. |
| `systemd-network` | Manages network configuration with systemd-networkd. |
| `docker` | Full access to Docker—root-equivalent if misused. |
| `lxd` | LXD container group—can be exploited for privilege escalation. |
| `www-data` | Common web server user group (e.g., Apache, Nginx). |
| `ftp` | Access for FTP services. |
| `nobod` | Very limited privileges—used by unprivileged daemons. |

## Permissions

Directory and file permissions in Linux are very easy to understand. The `ls` is fantastic at showing owners and groups for files and directories as well as determining if a file has read, write or executable permissions.

When I run the `ls -lha` command on my home directory I get the following output:

```bash
$ ls -lha ~
total 912K
drwxr-xr-x 50 kwmd kwmd 4.0K Jul 28 18:57 .
drwxr-xr-x 24 kwmd kwmd 4.0K Jul 28 18:57 ..
drwxr-xr-x  3 kwmd kwmd 4.0K Aug 23  2021 .aspnet
-rw-r--r--  1 kwmd kwmd  416 Nov 15  2024 .bash_aliases
lrwxrwxrwx  1 kwmd kwmd    9 Aug 16  2020 .bash_history -> /dev/null
-rw-r--r--  1 kwmd kwmd 4.2K Jun 22 22:12 .bashrc
...
drwxr-xr-x  3 kwmd kwmd 4.0K May 16 12:28 Pictures
...
```

The output shows a lot of important information. I am going to break it down some of the lines.

The `total 912K` line is stating the size of all the directories and files in my home directory.

All the lines after the total line follow a similar pattern. The pattern is the following:

```text
The file type, in this case a - means a file.
|The owner permissions, in this case rwx means read, write and execute.
||||The group permissions, in this case rw- means read and write.
|||||||The everyone permissions, in this case r-- means read.
||||||||||  The hard link count, defaults to 1.
||||||||||  | The user that owns this file, in this case kwmd.
||||||||||  | |    The group that has access to this file, in this case kwmd.
||||||||||  | |    |    The size of the file, in this case 215K.
||||||||||  | |    |    |    The month the file was created, in this case July.
||||||||||  | |    |    |    |   The day the file was created, in this case the 4th.
||||||||||  | |    |    |    |   |  The time the file was created, in this case 6:16 pm.
||||||||||  | |    |    |    |   |  |     The name of the file, in this case my_file.py.
vvvvvvvvvv  v v    v    v    v   v  v     v
-rwxrw-r--  3 kwmd kwmd 215K Jul 04 18:16 my_file.py
```

That is a lot of information that is compressed very nicely. I want to talk about each item.

### File Type

The file type if the left most piece of information. It give context to the other items in the line. Here are some of the possible values for the file type:

- The lines that start with a `d` are directories.
- The lines that start with a `-` are files. This includes scripts, images, configuration files and spreadsheets.
- The lines that start with a `l` are symbolic links. This are files that point to another file. They are used a lot of time for convenience.

### User, Group and Everyone Permissions

The next 9 characters after the file type are the user, group and everyone permissions. The user permissions are 3 characters, the group permissions are 3 characters and the everyone permissions are 3 characters.

The 3 characters are always go in the same order (read, write and execute). The first character determines read permission, the second character determines write permission and the last character determines execute permission. If permission is not granted, a `-` character will be displayed.

This might be more clear with examples. Here are a few:

- `r--`: Has read permission, does not have write or execute permissions.
- `r-x`: Has read and execute permissions, does not have write permission.
- `rw-`: Has read and write permissions, does not have execute permissions.
- `--x`: Has execute permission, does not have read or write permissions.
- `rwx`: Has read, write and execute permissions.

So if I had a file line that started like this:

`-rwxrw-r--`

I can determine this is a regular file (the `-` at the beginning). The user has read, write and execute permissions (the first 3 characters after the file type `rwx`). The group has read and write permissions but not execute permission (the next 3 characters after the user permissions `rw-`). The everyone group has read permission but not write and execute permissions (the next 3 characters after the group permissions `r--`).

## Privilege Escalation

I have noted the process I use for [Linux privilege escalation](/concepts/privilege_escalation.md#linux-privilege-escalation) in the [concepts](/concepts/README.md) directory.

## Systemctl

## Crons

## LXC

LXC (pronounced lex-cee) is used to manage Linux Containers. It has very minimal overhead. It provides a way to segregate different processes from each other in a Linux environment. I have used both Docker and Podman in the past and it works very similar to both.

With lxc, I can create or download an image, start multiple containers from that single image and have them interact with each other. Images can have databases, web applications, cron jobs, applications or mount parts of the file system.

The lxd command is used in conjunction with ethe lxc command. LXD (pronounced lex-dee) runs on top of lxc and has the goal of providing a better developer experience. One thing it does maintain a repository of images that can be used by lxc. The list of lxd images can be [found here](https://images.lxd.canonical.com/).

There are a few different ways that an image can be imported and ran. I have provided provided some examples below:

### Download the image from GitHub.

```bash
$ git clone https://github.com/saghul/lxd-alpine-builder.git
Cloning into 'lxd-alpine-builder'...
remote: Enumerating objects: 57, done.
remote: Counting objects: 100% (15/15), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 57 (delta 6), reused 8 (delta 4), pack-reused 42 (from 1)
Unpacking objects: 100% (57/57), 3.12 MiB | 17.34 MiB/s, done.
$ cd lxd-alpine-builder/
$ lxc image import alpine-v3.13-x86_64-20210218_0139.tar.gz --alias alpine
If this is your first time running LXD on this machine, you should also run: lxd init
To start your first container, try: lxc launch ubuntu:20.04
Or for a virtual machine: lxc launch ubuntu:20.04 --vm

Image imported with fingerprint: cd73881adaac667ca3529972c7b380af240a9e3b09730f8c8e4e6a23e1a7892b
$ lxc storage create mypool dir
Storage pool mypool created
$ lxc profile device add default root disk path=/ pool=mypool
Device root added to default
$ lxc init alpine kwmd
Creating kwmd
                                           
The instance you are starting doesn't have any network attached to it.
  To create a new network, use: lxc network create
  To attach a network to an instance, use: lxc network attach

$ lxc start kwmd
$ lxc exec kwmd /bin/sh
~ # whoami
root
```

Let me break down the above commands and what they are doing.

- I download the container I want from GitHub using the `git clone https://github.com/saghul/lxd-alpine-builder.git` command. This will create a directory on my machine called `lxd-alpine-builder`.
- I go into the newly downloaded directory with `cd lxd-alpine-builder`.
- The `lxc image import alpine-v3.13-x86_64-20210218_0139.tar.gz --alias alpine` command is telling lxc to import the container found at `alpine-v3.13-x86_64-20210218_0139.tar.gz` and give it the alias of `alpine` instead of calling it `alpine-v3.13-x86_64-20210218_0139`.
- Before the container can be initialized it needs a storage pool and a device. The `lxc storage create mypool dir` command creates a directory pool and names it `mypool`. This tells lxc where to store the container as well. The pool is located at `/var/snap/lxd/common/lxd/storage-pools/mypool`.
- The `lxc profile device add default root disk path=/ pool=mypool` command creates a directory device using the pool that was just created for a container to use. This also makes this device the default.
- The `lxc init alpine kwmd` initializes (creates) the container named `kwmd`.
- `lxc start kwmd` starts the container named `kwmd`.
- Finally, `lxc exec kwmd /bin/sh` runs a shell on the `kwmd` container. Now I am running commands from the container!

### Import the image from LXD Images.

I visit [the site](https://images.lxd.canonical.com/) and find an image that I like. For example, I found the Kali current image that is NOT for cloud. I click the timestamp for that image and it shows a page that has the following command: `lxc launch images:kali/current/default c1`. Here is the command in action:

```bash
$ lxc launch images:kali/current/default c1
Creating c1
                                            
The instance you are starting doesn't have any network attached to it.
  To create a new network, use: lxc network create
  To attach a network to an instance, use: lxc network attach

Starting c1
$ lxc exec c1 /bin/bash
root@c1:~# whoami
root
```

Running that command will download the Kali image and create a new container named `c1`. This is a much faster way to get a container up and running, there are only two commands.

### Privilege Escalation

I have included how LXD/LXC can be used to with privelege escalation in [this write up](/concepts/privilege_escalation.md#lxd).
