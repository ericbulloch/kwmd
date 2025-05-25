# kwmd

Welcome! This is my personal repository for all things cybersecurity. I keep notes for commands that I regularly use and write-ups for machines I have hacked on platforms like TryHackMe and VulnHub.

## TryHackMe

Here is [my profile on TryHackMe](https://tryhackme.com/p/kwmd). I am ranked in the top 2%. Here is my badge for TryHackMe (generated May 10, 2025):

<img src="https://tryhackme-badges.s3.amazonaws.com/kwmd.png" alt="Your Image Badge" />

## Tools

The [tools folder](tools/) contains a list of tools that I regularly use and, most importantly, examples of how they are used. Most of the tools come by default with Kali Linux. I reference these pages often when I work on a capture the flag event.

## Write-Ups

I want to help others who are learning about cybersecurity. There are many capture the flag machines and events available to learn from. Below is a list of platforms that have capture the flag machines, grouped by provider (TryHackMe, VulnHub, etc.). I then list the write-ups that I have for each platform.

In the write-ups, I provide the steps to get the answers, but I usually do not give the actual answer. I also try to include my thought process and the commands I ran, even if they did not help me move forward.

A lot of people who do write-ups only include the answers and not all the steps they took to get those answers. I want to include what was checked and eliminated before I found the solution. The thought process is more important than the answers.

- [TryHackMe Write-Ups](write_ups/try_hack_me/)
- [VulnHub Write-Ups](write_ups/vuln_hub/)

## Hacking Flow

I have been documenting the steps and scenarios that I often see in capture the flag events. I call this my hacking flow. I use it as a reference and guide while I work on capture the flag events. My goal is for this to continue to evolve and become my one-stop shop for bug bounties and capture the flag events.

### Starting

Unless the instructions tell me to use a specific hostname, I will often change the IP address of the machine to a more memorable hostname. For example, if I am working on a capture the flag on TryHackMe and they provide a machine with an IP address like 10.10.160.54, I will add an entry to my /etc/hosts file. In this example, I will run the following:

`echo "10.10.160.54  target.thm" >> /etc/hosts`

I do this so that I do not have to remember the IP address of the machine I am attacking. I have less to remember and can focus more on what I am trying to do.

Sometimes, as a sanity check, I will run `ping target.thm` or open a browser and type `http://target.thm` to make sure that everything is working.

### Port Scanning

I have added information about this on my [nmap tool](../tools/nmap.md#port-scans) page in the Port Scans section. There are two commands that I generally run, and the provided link explains in detail what they are doing. Here are the commands:

```bash
nmap -p- -Pn -T5 -v target.thm
nmap -A -Pn -v target.thm -p 22,80
```

### Website

This section will most likely become its own file instead of just a section. For now, I am just starting with the process.

#### Enumeration

There are a few different types of enumeration on websites that can be really useful.

##### Directory Enumeration

I almost always run a directory enumeration to see if there are any folders or files that are not directly linked by the website. This is how I usually find the admin login form. Also, I double-check the robots.txt file because this file is notorious in capture the flag events for giving away information.

If the tool finds a directory like `/app`, I will often run the tool again on that directory to see if there are additional results.

There are a lot of automated tools I can use for directory enumeration. Generally, the word list is the most important part. If I get stuck, I use a combination of tools and word lists to see if they find anything different. Here are some tools I like to use and some sample usage:

##### Directory Enumeration with dirsearch

I usually use dirsearch as my directory enumeration tool. The syntax is very terse, so I do not have to remember much to run it. It does not come by default on Kali, so I have to install it before use.

This tool can be installed with pip. I use it because the syntax is easy to remember and it does a good job with its default word list. I install it with the following command:

`pip3 install dirsearch`

My favorite thing about this tool is how little I have to remember when I run it. I run it with the following command:

`dirsearch -u http://target.thm`

The `-u` option tells dirsearch what URL I want to start searching in. If it finds that the site has a path like `/admin` and I want to search that folder, then I run another search with:

`dirsearch -u http://target.thm/admin`

##### Directory Enumeration with ffuf

Sometimes I run a few different tools just to see if I get different results. The ffuf tool is my go-to when I want a second opinion. I have provided information on how to run it on [its tools page](tools/ffuf.md#directory-enumeration).

##### Directory Enumeration with gobuster

The gobuster tool is also a great tool to get a second opinion. I generally go with ffuf instead of gobuster when I want a second opinion, but I have not been disappointed using either tool. I have provided information on how to run gobuster for directory enumeration on [its tool page](tools/gobuster.md#directoryfile-dir-enumeration-mode).

##### Subdomain Enumeration

Sometimes I will run subdomain enumeration to see if there are any other sites hosted by this machine.

##### Subdomain Enumeration with ffuf

The ffuf tool is my go-to when I run subdomain enumeration. I have provided information on how to run it on [its tools page](tools/ffuf.md#subdomain-enumeration). I have included the command here for a quick reference:

`ffuf -H "Host: FUZZ.10.10.1.1" -H "User-Agent: PENTEST" -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-large-directories-lowercase.txt -u http://10.10.1.1 -fs 100`

##### Parameter Enumeration

When I get stuck, I sometimes try to run parameter enumeration on a form to see if there are any other named variables that I can submit that might change the behavior of a form. Sometimes developers do not want the public to know about these hidden parameters because they use them for testing; other times, the developers just did not document them.

#### Browsing

In a capture the flag event, I look at the different pages and try to find forms and input fields. Each one of these is an attack vector that can be used for things like SQL injection or XSS attacks. Mapping the site is one of the first things I do while running directory enumeration.

#### Inspecting HTML

Capture the flag events often have flags in the comments of the HTML. I have found flags, usernames, passwords, directories, and links that my automated runs did not find. This is a very overlooked way to find useful things when I get stuck. Here is an altered sample of some comments that I have found in HTML:

```html
<!--

  Note from me, to me, remember my login name.

  Username: Sk3l3t0r

-->
```

#### SQL Injection

SQL injection is still a vulerability to be aware of in capture the flag events. Many exercises have forms that are vulnerable to this attack. The main forms that I routinely check are the login, feedback and address forms. I'll run a regular request and capture it in Burp. I'll save the request to a file named `request.txt` and then run the following command:

`sqlmap -r request.txt`

I have more details about this on the [sqlmap tools page](tools/sqlmap.md).

### SSH

#### Initial Information

If nmap shows that SSH is running on a machine, I will manually connect to it. I am trying to see if it asks for a password. If that is the case, this is another attack vector I can use if I can find a username on the server.

If the password prompt does not show up and I get an error that says "Permission denied (publickey)", my attack vector is reduced.

Also, sometimes I need to connect to SSH on a different port. This involves using the `-p` option. If I need to connect on port 2222, I would run:

`ssh -p 2222 user@target.thm`

#### SSH Brute Force

SSH does have some CVEs (Common Vulnerabilites and Exposures) but I rarely have to use them in a capture the flag event. Usually I will need to brute force SSH because I have found a username (for example, bob) but do not know the password, I will run Hydra using the rockyou.txt wordlist to see if I can find the password and log into the server. Using [the example found here](tools/hydra.md#ssh), I run:

`hydra -l bob -P /usr/share/wordlists/rockyou.txt 10.10.1.1 ssh`

There are other tools that can do this as well but I prefer Hydra.

### SMB

Server Message Block is commonly used in capture the flag events. It allows users to share files and printers across the network. Enumerating SMB and Samba folders is a gold mine, but I forget the syntax and tools all the time.

#### Enumeration

It is important to find out what disks are available and if any of them do not require me to log in. I use the smbmap tool to solve this. The following command will discover what shares are available and what the permissions for them are:

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

The above example tells me that the `anonymous` disk does not require authentication. Therefore, I can view the contents of that disk.

#### Connecting to Disk

To connect to an anonymous disk, I use the smbclient tool. It makes it easy to browse and download files after enumeration is complete. I connect to the anonymous disk above with:

`smbclient //target.thm/anonymous/ -N`

This will change the command prompt to:

`smb: \>`

Now I can use the `ls` and `cd` commands to look around the disk.

#### Downloading Individual Files

I often need to download the contents of a disk onto my machine for analysis. If the file on the disk is called important.txt, I would run the following command (I included the smb prompt in the beginning of the command):

`smb: \> get important.txt`

This will download the important.txt file to the directory I was in on my machine when I connected to the disk.

#### Downloading Folders

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

### Stable Shell

Once I have connected to the target machine with netcat, getting a stable shell is my main priority. There are a few different ways to do this; here are the ones that I use.

#### Python PTY

If Python is on the machine, this is my preferred method. There are four steps, and then I will have a stable shell. The steps are:

- Run the command: `python3 -c 'import pty;pty.spawn("/bin/bash")'`. This creates a new process that runs bash in a pseudo-terminal (pty).
- Run the command: `export TERM=xterm`. This sets the terminal emulator to xterm. This is the default setting for Ubuntu.
- Move my shell session to the background by hitting `^Z` (Ctrl+Z). I need to run one more command, and this process needs to be in the background for the command to work.
- Run the command: `stty raw -echo; fg`. This disables the raw input and output and just sends it straight through to standard in and out. The `fg` command moves the previous process from the background to the foreground.

### Linux Privilege Escalation

If I have a shell on a Linux machine, the goal is to become root. The process is part art and part science. Learning how Linux works and practicing can go a long way. Being creative is also very important. In my experience, enumeration is the most important skill with privilege escalation. For each user that I escalate to (whether vertically or horizontally), I run nearly identical steps. The things that each user has access to can be very unique.

This section will eventually become a whole page because of how much information it covers. New techniques are constantly being found, and researchers are finding new ways to exploit old systems and vulnerabilities. That is why this art and science intersect wonderfully here.

I eventually find a way to run the [LinPEAS](tools/linpeas.sh) script somewhere on the machine. The insights that it provides are amazing! But I do not usually go straight to LinPEAS. I have a few commands that I run manually and check if they provide some quick wins. Here are the commands that I run and validate before I run LinPEAS:

#### ls /home

I want to know what users are on the machine. If possible, I will go into each user's directory and see what files and folders are available. These include things like the following:

- The public and private keys in the .ssh folder.
- The .bash_history file.
- Documents and Desktop folders.
- Out-of-place folders like .git.

So if the user mike has a folder in /home, I would run the following command to explore what is available to me:

`ls -lha /home/mike`

#### cat /etc/passwd | grep '/bin/bash'

If I can read the /etc/passwd file, it also has information about users of the system and where their home directory is located. Once in a while, the home directory of a user will not be in the /home folder. I am generally just looking for users that have a shell. The `grep '/bin/bash'` part of the command will filter out the users that do not have a shell.

#### SUID Binaries

The SUID (Set User ID) bit is a special permission that allows a user to run a binary with the privileges of the binary's owner, rather than their own user privileges. In other words, I can use a binary that root owns and run that binary as root instead of my regular user. An example of a binary that has the SUID bit set looks like the following:

`-rwsr-xr-x 1 root root 163K Apr   4  2025 /usr/bin/sudo`

The SUID bit in this example is the `s` at the beginning of the user's privileges. Normally I would see `rwx`, but the `s` means that the file is executed with root's privileges.

I search for these files with the following command:

`find / -perm -u=s -type f 2>/dev/null`

Here is an explanation of this command:

- The `-type f` option tells find to look for files.
- The `-perm -u=s` option tells find to look for files with the user SUID bit set.
- The `2>/dev/null` tells the command to redirect all errors to /dev/null (do not show errors).

I pair the output of this command with the [GTFOBins website](https://gtfobins.github.io/) to find out if any of the binaries with the SUID bit set can be used to escalate privileges.

##### SUID Example with GTFOBins

One capture the flag exercise had the SUID bit set for nmap. GTFOBins [has two examples with nmap](https://gtfobins.github.io/gtfobins/nmap/#suid) where you can get root. I like the second one if the version of nmap is between 2.02 and 5.21. All you have to type to get a root shell is the following:

```bash
sudo nmap --interactive
nmap> !sh
```

That will give you new shell as root. There are many examples of how you can exploit a binary with the SUID bit set. GTFOBins has a lot of good documentation around it.

#### crontab -e

Capture the flag events often have a script that runs every minute that I can exploit to do privilege escalation. If my user has access, this will tell me what crons are running and how often. These jobs are for the current user. Here is a sample of a cron that runs each minute and runs a backup script in the user mike's home directory:

`* * * * * /usr/bin/python /home/mike/backup.py`

#### id

The `id` command is one of the very first things I run when I log in with a new user on a Linux machine. The group information that it provides lets me know what my attack surface is with this user. For example, sometimes in a capture the flag event, I will run the `id` command and see that a user is in the adm group. This means that this user can read a lot of log files in the /var/log directory. Log files are full of useful information.

I usually run the `id` command and then check what each group has access to. I note them and continue with other commands. The direction of this and other commands dictates where I should start attacking.

Here is some sample output for the `id` command:

`uid=1000(ubuntu) gid=1000(ubuntu) groups=1000(ubuntu),132(postgres)`

In this case, I would note that the ubuntu user is also in the postgres group. I would make sure I understood what that means and then check the output from the next few sections of commands.

#### sudo -l

If this command does not fail, it will tell me what scripts and binaries I can run as root. From here, I note what commands and binaries can be run. I also look at the binaries, scripts, and their containing directories. I am specifically looking at the permissions. Here are some examples of what I am looking for:

- Can I delete this binary and replace it with another one that does what I need it to do?
- Are there flags that I can run with this binary to do a wildcard attack?
- Can the binary run shell commands?
- Can I edit the script that is being run?
- What input does the script allow?

The answers to all these questions get noted.

#### uname -a

This command is very simple. There are kernel attacks that can be run to get root access. I will take the output of this command and check if there are any CVEs related to this kernel. Here is some sample output when I run the `uname -a` command:

`Linux my_machine 5.15.0-124-generic #134~20.04.1-Ubuntu SMP Tue Oct 1 15:27:33 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux`

I will type "Linux 5.15.0-124 CVE" into Google to see if there are any vulnerabilities.
