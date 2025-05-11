# kwmd

Welcome! This is my personal repository for all things cyber security. I keep notes for commands that I regularly use and write ups for machines I have hacked on platforms like TryHackMe and VulnHub.

Here is my profile on TryHackMe. I am ranked in the top 2%:

<img src="https://tryhackme-badges.s3.amazonaws.com/kwmd.png" alt="Your Image Badge" />

## Tools

The [tools folder](tools/) contains a list of tools that I regularly use and most importantly examples of how they are used. Most of the tools come by default with Kali Linux. I reference these pages often when I work on a capture the flag event.

## Write Ups

I want to help out others that are learning about cyber security. There are so many capture the flag machines and events available to learn from. Below is a list of platforms that have capture the flag machines. I have grouped them by the provider (TryHackMe, VulnHub, etc...). I then list the write ups that I have for that platform.

In the write ups I provide the steps to get the answers but I usually will not give the actual answer. I also try to include what I am thinking and what commands I ran even if they didn't provide something that helped move forward.

A lot of people who do write ups only include the answers and not all the steps they took to get those answers. I want to include what was checked and eliminated before I found the solution. The thought process is more important than the answers.

- [TryHackMe Write-Ups](write_ups/try_hack_me/)
- [VulnHub Write-Ups](write_ups/vuln_hub/)

# Hacking Flow

I have been documenting the steps and scenarios that I often see in capture the flag events. I call this my hacking flow. I use it as a reference and guide while I work on capture the flag events. My goal is for this to continue to evolve and become my one stop shop for bug bounties and capture the flag events.

## Starting

Unless the instructions tell me that I have a specific hostname that I must use, I will often change the ip address of the machine to a hostname that is more favorable. For example, if I am working on a capture the flag on TryHackMe and they provide a machine with an ip address of something like 10.10.160.54, I will add an entry to my /etc/hosts file. In this example I will run the following:

`echo "10.10.160.54  target.thm" >> /etc/hosts`

I do this so that I don't have to remember the ip address of the machine that I am attacking in the capture the flag event. I have less to remember and so I can focus more on what I am trying to do.

Sometimes, as a sanity check, I will run `ping target.thm` or open a browsers and type `http://target.thm` to make sure that everything is working

# Port Scanning

I have added information about this on my [nmap tool](../tools/nmap.md#port-scans) page in the Port Scans section. There are 2 commands that I generally run and the provided link explains in details what they are doing. Here are the commands:

`nmap -p- -Pn -T5 -v target.thm`

and

`nmap -A -Pn -v target.thm -p 22,80`

# Website

This section will most likely be its own file instead of just a section for right now. For now I am just starting with the process.

## Enumeration

There are a few different types of enumeration on websites that can be really useful.

### Directory Enumeration

I almost always run a directory enumeration to see if there are any folders or files that are not linked directly by the website. This is how I usually find the admin login form. Also, I do a double check on the robots.txt file because this file is notorious in capture the flag events for giving away information.

If the tool finds a directory like the `/app` directory, I will often times run the tool again on that directory so I can see if there are additional results.

There are a lot of automated tools that you can use for directory automation. Generally, your word list is the most important part of directory enumeration. If I get stuck I use a combination of tools and word lists to see if they found anything different. Here are some tools I like to use and some sample usage:

#### dirsearch

I usually use dirsearch as my directory enumeration tool. The syntax is very terse and so I don't have to remember much to run it. It doesn't come by default on Kali so I have to install it before I use it.

This tool can be installed with pip. I use this tool because the syntax is easy to remember and it does a pretty good job with its default word list. I install it with the following command:

`pip3 install dirsearch`

My favorite thing about this tool is how little I have to remember when I run it. I run it with the following command:

`dirsearch -u http://target.thm`

The `-u` option tells dirsearch what url I want to start searching in. If it found that the site has a path like `/admin` and I wanted to search that folder, then I would run another search with the following command:

`dirsearch -u http://target.thm/admin`

#### ffuf

Sometimes I run a few different tools just to see if I get different results. The ffuf tool is my go to when I want a second opinion. I have provided information on how to run it on [its tools page](tools/ffuf.md#directory-enumeration).

#### gobuster

The gobuster tool is a wonderful tool to use to get a second opinion as well. I generally go with ffuf instead of gobuster when I want a second opinion. You won't be disappointed using either tool. I have provided information on how to run gobuster for directory enumeration on [its tool page](tools/gobuster.md#directoryfile-dir-enumeration-mode)

### Subdomain Enumeration

Sometimes I will run subdomain enumeration to see if there are any other sites hosted by this machine.

### Parameter Enumeration

When I get stuck I sometimes try to run a parameter enumeration on a form just to see if there are any other named variables that I can submit that might change the behavior of a form. Sometimes developers don't want the public to know about these hidden parameters because they use them for testing, other times the developers just didn't document them.

## Browsing

In a capture the flag event I am looking at the different pages and trying to find forms and input fields. Each one of these is an attack vector that can be used to do things like SQL injection or a XSS attack. Mapping the site is one of the first things I do while running directory enumeration on a website.

## Inpecting HTML

Capture the flag events often have flags in the comments of the HTML. I have found flags, usernames, passwords, directories and links that my automated runs didn't find. This is a very overlooked way to find useful things when I get stuck. Here is an altered sample of some comments that I have found in html:

```html
<!--

  Note from me, to me, remember my login name.

  Username: Sk3l3t0r

-->
```

# SSH

## Initial Information

If nmap shows that ssh is running on a machine, I will manually connect to it. I am trying to see if it asks for a password. If that is the case, this is another attack vector I can use if I can find a username on the server.

If the password prompt did not show up and I got an error that says "Permission denied (publickey)", my attack vector got smaller.

Also, sometimes I need to connect to ssh on a different port. This involves using the `-p` option. If I need to connect on port 2222 I would run the following command:

`ssh -p 2222 user@target.thm`

# SMB

Server Message Block is commonly used in capture the flag events. It allows users to share files and printers across the network. Enumerating SMB and Samba folders are a gold mine but I forget the syntax and tools all the time.

## Enumeration

It is important to find out what diskes are available and if any of them don't require me to login. I use the smbmap tool to solve this. The following command will discover what shares are available and what the permissions for them are:

`smbmap -H target.thm`

The output will look something like the following:

```bash
[+] Finding open SMB ports...
[+] Guest SMB session established on target.thm...
[+] IP: 10.22.112:445           Name: storage
        Disk                                              Permissions
        ----                                              -----------
        print$                                            NO ACCESS
        anonymous                                         READ ONLY
        mrburns                                           NO ACCESS
        IPC$                                              NO ACCESS
```

The above example tells me that the `anonymous` disk doesn't require me to authenticate. Therefore, I can view the contents of that disk.

## Connecting to Disk

To connect to an anonymous disk, I use the smbclient tool. It makes it easy to browse and download files after enumeration is complete. I connect to the anonymous disk above with the following command:

`smbclient //target.thm/anonymous/ -N`

This will change the command prompt to the following:

`smb: \>`

Now I can use the `ls` and `cd` commands to look around the disk.

## Downloading Individual Files

I often times need to download the contents of a disk on to my machine for analysis. If the file on the disk is called important.txt, I would run the following command (I included the smb prompt in the beginning of the command):

`smb: \> get important.txt`

This will download the important.txt file to the directory I was in on my machine when I connected to the disk.

## Downloading Folders

More often then not, I really just want to download a folder rather than running the above command multiple times. This is still easy but I run a few more commands. I go into the folder on the disk that has all the files and folders I want. I then run the following commands (I included the smb prompt in the beginning of the commands):

```bash
smb: \> recurse on
smb: \> prompt off
smb: \> mget *
```

Here is an explanation of these commands:

- `recurse on` will grab all the files and folders inside the folders in this directory.
- `prompt off` will not ask me if I want to download the file.
- `mget *` targets all the files and folders in this directory.

# Stable Shell

Once I have connected to the target machine with netcat, getting a stable shell is my main priority. There are a few different ways to do this, here are the ones that I use.

## Python PTY

If python is on the machine this is my preferred method. There are 4 steps and then I will have a stable shell. The steps are:

- Run the command: `python3 -c 'import pty;pty.spawn("/bin/bash")'`. This creates a new process that runs bash in a pseudo-terminal (pty).
- Run the command: `export TERM=xterm`. This sets the terminal emulator to xterm. This is the default setting for Ubuntu.
- Move your shell session to the background by hitting `^Z` (ctrl+Z). I need to run one more command and this process needs to be in the background for the command to work.
- Run the command: `stty raw -echo; fg`. This disables the raw input and output and just sends it straight through to standard in and out. The `fg` command move the previous process from the background to the foreground.

# Linux Privilege Escalation

If I have a shell on a Linux machine, the goal is to become root. The process is part art and part science. Learning how Linux works and practicing can go a long way. Being creative is also very important. In my experience, enumeration is the most important skill with privilege escalation. For each user that I escalate to (whether vertically or horizontally), I run nearly identical steps with each user. The things that each user has access to can be very unique.

This section will eventually become a whole page because of how much information it covers. New techniques are constantly being found and researchers are finding new ways to exploit old systems and vulnerabilities. That is why this art and science intersect wonderfully here.

I eventually find a way to run the [LinPEAS](tools/linpeas.sh) script somewhere on the machine. The insights that it provides are amazing! But I don't usually go straight to LinPeas. I do have a few commands that I run manually and check if they provide some quick wins. Here are the commands that I run and validate before I run LinPEAS:

## ls /home

I want to know what users are on the machine. If possible, I will go into each users directory and see what files and folders are available. These include things like the the following:

- The public and private keys in the .ssh folder.
- The .bash_history file.
- Documents and Desktop folders.
- Out of place folders like .git.

So if the user mike has a folder in /home I would run the following command explore what is available to me:

`ls -lha /home/mike`

## cat /etc/passwd | grep '/bin/bash'

If I can read the /etc/passwd file it also has information about users of the system and where their home directory is located. Once in a while the home directory of a user will not be in the /home folder. I am generally just looking for users that have a shell. The `grep '/bin/bash'` part the command will filter out the users that do not have  a shell.

## SUID Binaries

The SUID (Set User ID) bit is a special permission that allows a user to run a binary with the privileges of the binary's owner, rather than their own user privileges. In other words, I can use a binary that root owns and run that binary as root instead of my regular user. An example of a binary that has the SUID bit set looks like the following:

`-rwsr-xr-x 1 root root 163K Apr   4  2025 /usr/bin/sudo`

The SUID bit in this example is the `s` at the beginning of the user's privileges. Normally you would see `rwx`, but the `s` means that the file is executed with root's privileges.

I search for these files with the following commands:

`find / -perm -u=s -type f 2>/dev/null`

Here is an explanation of this commands:

- The `-type f` option tell find to look for files.
- The `-perm -u=s` options tell find to look for files with the permissions that match a user SUID bit set.
- The `2>/dev/null` tells the command to redirect all failures to /dev/null (don't show failures).

I pair the output of this command with GTFOBins to find out if any of the binaries have a SUID bit set that can be used to escalate privileges.

## crontab -e

Capture the flag events often have a script that runs every minute that I can exploit to do privilege escalation. If my user has access, this will tell me what crons are running and how often. These jobs are for the current user. Here is a sample of a cron that runs each minute and runs a backup script in the user mike's home directory:

`* * * * * /usr/bin/python /home/mike/backup.py`

## id

The `id` command is one of the very first things I run when I login with a new user on a Linux machine. The group information that it provides lets me know what my attack surface is with this user. For example, sometimes in a capture the flag event, I'll run the `id` command and I'll get output that a user is in the adm group. This means that this user can read a lot of log files in the /var/log directory. Log files are full of useful information.

I usually run the `id` command and then check what each group has access to. I'll note them and and continue with other commands. The direction of this and other commands dictates where I should start attacking.

Here is some sample output for the `id` command:

`uid=1000(ubuntu) gid=1000(ubuntu) groups=1000(ubuntu),132(postgres)`

In this case, I would note that the ubuntu user is also in the postgres group. I would make sure I understood what that means and then check the output from the next few sections of commands.

## sudo -l

If this command doesn't fail, it will tell me what scripts and binaries I can run as root. From here, I note what commands and binaries can be ran. I'll also look at the binaries, scripts and their containing directories. I am specifically looking at the permissions. Here are some examples of what I am looking for:

- Can I delete this binary and replace it with another one that does what I need it to do?
- Are there flags that I can run with this binary to do a wildcard attack?
- Can the binary run shell commands?
- Can I alter edit the script that is being ran?
- What input does the script allow?

The answers to all these questions get noted.

## uname -a

This command is very simple. There are kernal attacks that can be ran to get root access. I will take the output of this command and check if there are any CVEs related to this kernal. Here is some sample output when I run the `uname -a` command:

`Linux my_machine 5.15.0-124-generic #134~20.04.1-Ubuntu SMP Tue Oct 1 15:27:33 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux`

I will type "Linux 5.15.0-124 CVE" into google to see if there are any vulnerabilites.
