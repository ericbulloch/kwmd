# Linux

I wanted to list some concepts, terms and flows that are specific to Linux. Learning more about Linux has made me a better and more effcient pentration tester. There is a lot of information to cover. I use this page as a reference.

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

The lines that start with a `d` are directories.

The lines that start with a `-` are files.

The line that start with a `l` is a symbolic link.



## Privilege Escalation

I have noted the process I use for [Linux privilege escalation](/concepts/privilege_escalation.md#linux-privilege-escalation) in the [concepts](/concepts/README.md) directory.

## Systemctl

## Crons
