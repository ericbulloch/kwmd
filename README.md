# kwmd

- [Introduction](#introduction)
- [TryHackMe](#tryhackme)
- [Concepts](#concepts)
- [Tools](#tools)
- [Vulnerabilities](#vulnerabilities)
- [Write-Ups](#write-ups)
- [Methodology](#methodology)

## Introduction

Welcome! This is my personal repository for all things cybersecurity. I keep notes for commands that I regularly use and write-ups for machines I have hacked on platforms like TryHackMe and VulnHub.

**Everything in here is for educational purposes.**

## TryHackMe

Here is [my profile on TryHackMe](https://tryhackme.com/p/kwmd). As of August 27, 2035 here are my stats:

- I am ranked in the top 1%.
- I am ranked 865 in the United States of America
- I am ranked 6,749 in the world.

Here is my badge for TryHackMe (generated June 6, 2025):

<a href="https://tryhackme.com/p/kwmd">
  <img src="images/kwmd.png" alt="kwmd TryHackMe Badge" />
</a>

## Concepts

The [concepts folder](concepts/) contains a list of concepts that are more than just a process, tool or idea. These are the things in cyber security that are very deep and wide.

## Tools

The [tools folder](tools/) contains a list of tools that I regularly use and, most importantly, examples of how they are used. Most of the tools come by default with Kali Linux. I reference these pages often when I work on a capture the flag event.

## Vulnerabilities

The [vulnerabilities folder](vulnerabilities/) has information about the OWASP 2021 Top Ten vulnerabilities. Each vulnerability is explained and examples of how it is found in the wild are provided.

Each vulnerability has a list of best practices and links to exercises that use that vulnerability.

## Write-Ups

I want to help others who are learning about cybersecurity. There are many capture the flag machines and events available to learn from. Below is a list of platforms that have capture the flag machines, grouped by provider (TryHackMe, VulnHub, etc.). I then list the write-ups that I have for each platform.

In the write-ups, I provide the steps to get the answers, but I usually do not give the actual answer. I also try to include my thought process and the commands I ran, even if they did not help me move forward.

A lot of people who do write-ups only include the answers and not all the steps they took to get those answers. I want to include what was checked and eliminated before I found the solution. The thought process is more important than the answers.

- [TryHackMe Write-Ups](write_ups/try_hack_me/)
- [VulnHub Write-Ups](write_ups/vuln_hub/)

## Methodology

I have been documenting the steps and scenarios that I often see in capture the flag events. I use it as a reference and guide while I work on capture the flag events. My goal is for this to continue to evolve and become my one-stop shop for bug bounties and capture the flag events.

### Starting

Unless the instructions tell me to use a specific hostname, I will often change the IP address of the machine to a more memorable hostname. For example, if I am working on a capture the flag on TryHackMe and they provide a machine with an IP address like 10.10.160.54, I will add an entry to my /etc/hosts file. In this example, I will run the following:

```bash
$ echo "10.10.160.54  target.thm" >> /etc/hosts
```

I do this so that I do not have to remember the IP address of the machine I am attacking. I have less to remember and can focus more on what I am trying to do.

Sometimes, as a sanity check, I will run `ping target.thm` or open a browser and type `http://target.thm` to make sure that everything is working.

This does not solve all my problems. There are two scenarios where I couldn't just use target.thm for the rest of a capture the flag event:

- A box will require a specific hostname to access their site and any subdomains. In this case, I added their specific domain name to my host file using the command above.
- A box has a vulnerability that calls out to the url that I provide. Since the target machine does not have target.thm in their host file it will fail to resolve an ip address. In this case, I will just provide the ip address of the target machine.

### Port Scanning and Fingerprinting

I have added information about this on my [nmap tool](tools/nmap.md#port-scans) page in the Port Scans section.

I ususally just run the following command:

```bash
$ nmap -T4 -n -sC -sV -Pn -v -p- target.thm
```

An explaination about this command can be found in the link above.

### FTP (File Transfer Protocol)

I have included a tool write up for the [ftp tool](tools/ftp.md) in my [tools](tools/README.md) section. It covers the some of the more common scenarios that I have found during capture the flag events.

### POP3 (Post Office Protocol version 3)

I have included a write up that details interacting with [pop3](services/pop3.md) in my services section. It covers the some of the more common scenarios that I have found during capture the flag events.

### NFS (Network File System)

NFS allows users to access and manage files on a remote server as if those files were on their local computer. The server drives need to be mounted on my machine so that I can see them and use them. Here is the command to see what drives are available on the remote machine:

```bash
$ showmount -e 10.10.1.1
```

This will output something like the following:

```bash
Export list for 10.10.1.1:
/mnt/share *
```

The output tells me I can mount the folder /mnt/share that is on the server with the ip address 10.10.1.1. I usually create a folder with the same name as the drive and then mount that nfs drive to that folder. In this case, here is the commands I run:

```bash
$ mkdir share
$ sudo mount -t nfs 10.10.1.1:/mnt/share share
```

Now I can access the folder and the files. There was a capture the flag event where I couldn't cd into the share directory. I was root on my machine and when I ran `cd share` I got the following error:

`bash: cd: share/: Permission denied`

I ran the following command to see what the permissions were for the share folder:

```bash
$ ls -lh
...
drwx------ 2 1018 1018 4.0K Apr  2  2025 share
...
```

The 1018 user and group didn't exist on my machine. Since I was root I added a user and set their user and group id to 1018. Here are the commands I ran:

```bash
$ sudo useradd kwmd
$ sudo usermod -u 1018 kwmd
$ sudo groupmod -g 1018 kwmd
```

After that I changed to the user by running `su kwmd`. From there, I was able to view the files in the nfs share.

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

```bash
$ pip3 install dirsearch
```

My favorite thing about this tool is how little I have to remember when I run it. I run it with the following command:

`dirsearch -u http://target.thm`

The `-u` option tells dirsearch what URL I want to start searching in. If it finds that the site has a path like `/admin` and I want to search that folder, then I run another search with:

```bash
$ dirsearch -u http://target.thm/admin
```

##### Directory Enumeration with ffuf

Sometimes I run a few different tools just to see if I get different results. The ffuf tool is my go-to when I want a second opinion. I have provided information on how to run it on [its tools page](tools/ffuf.md#directory-enumeration).

##### Directory Enumeration with gobuster

The gobuster tool is also a great tool to get a second opinion. I generally go with ffuf instead of gobuster when I want a second opinion, but I have not been disappointed using either tool. I have provided information on how to run gobuster for directory enumeration on [its tool page](tools/gobuster.md#directoryfile-dir-enumeration-mode).

##### Subdomain Enumeration

Sometimes I will run subdomain enumeration to see if there are any other sites hosted by this machine.

##### Subdomain Enumeration with ffuf

The ffuf tool is my go-to when I run subdomain enumeration. I have provided information on how to run it on [its tools page](tools/ffuf.md#subdomain-enumeration). I have included the command here for a quick reference:

```bash
$ ffuf -H "Host: FUZZ.10.10.1.1" -H "User-Agent: PENTEST" -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-large-directories-lowercase.txt -u http://10.10.1.1 -fs 100
```

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

```bash
$ sqlmap -r request.txt
```

I have more details about this on the [sqlmap tools page](tools/sqlmap.md).

#### File Upload

An image uploading form can be an entry point into a website. This is because the code that uploads files does not check file extensions or if the file is actually a PNG or JPEG file. The [PHP Reverse Shell](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php) makes it easy to get a reverse shell for systems that are vulnerable.

I first grab the file from the repository above or the one on the TryHackMe attack box located at `/usr/share/webshells/php/php-reverse-shell.php`. There are only 2 lines that need to be altered in this file. They are the lines that define the `$ip` and `$port` variables.

I set those to the values that my attack box is using. I'll run a netcat listener with the following `nc -lnvp 4444`. The port 4444 value also got set as the `$port` variable in the script.

From here I'll see if I can upload the shell directly. If that fails I'll try different file extensions hoping that they have not accounted for it. Here is the list of file extensions that I try:

- .php
- .php3
- .php4
- .php5
- .php7
- .phtml
- .phps
- .pht
- .phar

In the event that they want a specific file extension like .jpg, I will try the following extensions:

- .php.jpg
- .php.jpeg
- .php%00.jpg
- .jpg.php (or some variant of the php extension list above).

The `%00` is a null character for a url and marks the end of the string. I am at the mercy of however the server side was implemented. They might only be checking for .jpg in the file name or they might want it to end with that. The server side might also try to validate that the file starts with the correct file signature. The list of file signatures can be [found here](https://en.wikipedia.org/wiki/List_of_file_signatures).

### Decoding Text

I have included a write up for the [text encoding](concepts/cryptography.md#text-encoding) in my Cryptography [concepts](concepts/README.md) section. It covers some of the more common scenarios that I have found during capture the flag events.

### SSH (Secure Shell Protocol)

I have included a tool write up for the [ssh tool](tools/ssh.md) in my tools section. It covers the some of the more common scenarios that I have found during capture the flag events.

### SMB (Server Message Block)

I have included a write up that details interacting with [smb](services/smb.md) in my services section. It covers the some of the more common scenarios that I have found during capture the flag events.

### Stable Shell

Once I have connected to the target machine with netcat, getting a stable shell is my main priority. There are a few different ways to do this; here are the ones that I use.

#### Python PTY

If Python is on the machine, this is my preferred method. There are four steps, and then I will have a stable shell. The steps are:

- Run the command: `python3 -c 'import pty;pty.spawn("/bin/bash")'`. This creates a new process that runs bash in a pseudo-terminal (pty).
- Run the command: `export TERM=xterm`. This sets the terminal emulator to xterm. This is the default setting for Ubuntu.
- Move my shell session to the background by hitting `^Z` (Ctrl+Z). I need to run one more command, and this process needs to be in the background for the command to work.
- Run the command: `stty raw -echo; fg`. This disables the raw input and output and just sends it straight through to standard in and out. The `fg` command moves the previous process from the background to the foreground.

So the commands are as follows:

```bash
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
$ export TERM=xterm
$ ]^z
$ stty raw -echo; fg
```

### Linux Privilege Escalation

I have included a write up for [Linux privilege escalation](concepts/privilege_escalation.md#linux-privilege-escalation) in my Privilege Escalation [concepts](concepts/README.md) section. It covers the more common commands and ideas that I have found and used during capture the flag events.






