# find

- [Introduction](#introduction)
- [Usage](#usage)
- [Examples](#examples)

## Introduction

The find tool does exactly what the name says. It locates files, folders, symlinks, sockets and other types on the files system. There are many flags and options that can be used with this tool to help refine the search space.

## Usage

```bash
$ find -h
Usage: find [-H] [-L] [-P] [-Olevel] [-D debugopts] [path...] [expression]

default path is the current directory; default expression is -print
expression may consist of: operators, options, tests, and actions:
operators (decreasing precedence; -and is implicit where no others are given):
      ( EXPR ) ! EXPR -not EXPR EXPR1 -a EXPR2 EXPR1 -and EXPR2
      EXPR1 -o EXPR2 EXPR1 -or EXPR2 EXPR1 , EXPR2
positional options (always true): -daystart -follow -regextype

normal options (always true, specified before other expressions):
      -depth --help -maxdepth LEVELS -mindepth LEVELS -mount -noleaf
      --version -xdev -ignore_readdir_race -noignore_readdir_race
tests (N can be +N or -N or N): -amin N -anewer FILE -atime N -cmin N
      -cnewer FILE -ctime N -empty -false -fstype TYPE -gid N -group NAME
      -ilname PATTERN -iname PATTERN -inum N -iwholename PATTERN -iregex PATTERN
      -links N -lname PATTERN -mmin N -mtime N -name PATTERN -newer FILE
      -nouser -nogroup -path PATTERN -perm [-/]MODE -regex PATTERN
      -readable -writable -executable
      -wholename PATTERN -size N[bcwkMG] -true -type [bcdpflsD] -uid N
      -used N -user NAME -xtype [bcdpfls]      -context CONTEXT

actions: -delete -print0 -printf FORMAT -fprintf FILE FORMAT -print 
      -fprint0 FILE -fprint FILE -ls -fls FILE -prune -quit
      -exec COMMAND ; -exec COMMAND {} + -ok COMMAND ;
      -execdir COMMAND ; -execdir COMMAND {} + -okdir COMMAND ;

Valid arguments for -D:
exec, opt, rates, search, stat, time, tree, all, help
Use '-D help' for a description of the options, or see find(1)

Please see also the documentation at http://www.gnu.org/software/findutils/.
You can report (and track progress on fixing) bugs in the "find"
program via the GNU findutils bug-reporting page at
https://savannah.gnu.org/bugs/?group=findutils or, if
you have no web access, by sending email to <bug-findutils@gnu.org>.
```

## Examples

Find has a lot of options to help find specific files and folders. Rather than list them out I decided to write a scenario and then write the find command that would handle that. I'll try to use capture the flag examples as I go. Most of the commands will end with `2>/dev/null` because I don't want a bunch of Permission denied output that looks like the following:

```bash
find: /some/random/directory: Permission denied
```

| Command | Description |
| --- | --- |
| `find /home/gimli -type f -user gimli -size 85 2>/dev/null` | Find a file owned by the user gimli with a size of 85 kilobytes in the directory /home/gimli. |
| `find / -type f -name ReadMeIfStuck.txt 2>/dev/null` | There is a file somewhere on the disk drive called ReadMeIfStuck.txt. |
| `find / -type d -name order\ numbers 2>/dev/null` | Look for a directory called "order numbers" (notice the space). |
| `find archived_orders/ -type f -newermt 2009-05-01 ! -newermt 2009-02-03 2>/dev/null` | Find a file with a modified date of 2009-05-02 from the archived_orders directory. |
| `find ~ -type f -name .hidden.txt 2>/dev/null` | Find a file named .hidden.txt inside your home directory. |
| `find ~/Documents -type f -iname 'presentation.pptx' 2>/dev/null` | I created a file called presentation.pptx but I can't remember if I capitalized it or not. It should be in my /home/user/Documents folder. |
| `find /var/log -type f -name "*.log" 2>/dev/null` | Show me all the log files in the /var/log directory. |
| `/ -type d -name "backup*" 2>/dev/null` | Find all the directories that start with the name backup. |
| `find . -maxdepth 1 -type d 2>/dev/null` | List all the directories in the current directory only, without recursing into subdirectories. |
| `find /tmp -type f -empty 2>/dev/null` | Find all empty files in /tmp. |
| `find /var/cache -type d -empty 2>/dev/null` | Find all empty directories in /var/cache. |
| `find /var -not -user root 2>/dev/null` | Find all files that do not belong to the root user in the /var directory. |
| `find /opt -user john 2>/dev/null` | Find all files owned by the user john in the /opt directory. |
| `find /etc -type f -perm 400 2>/dev/null` | Find all files with read-only permissions for the owner (400) in the /etc directory. |
| `find ~ -type f -perm 700 2>/dev/null` | Find all files with read, write, and execute permissions for the owner (700) in your home directory (~). |
| `find . -type f -name "*.tmp" -delete` | Find all .tmp files in the current directory and delete them. |
| `find . -type f -name "*.txt" -exec cat {} \;` | Find all .txt files in the current directory and display their contents using the cat command. |
| `find /var/log -type f -name "*.log" -print -exec chmod 644 {} \;` | Find all .log files in the /var/log directory, print their names, and change their permissions to 644. |
| `find ~ -path "*/Documents/*" -prune -o -name "*.txt" -print` | Find all .txt files in your home directory, but exclude the Documents directory from the search. |
| `find ~ -type l` | Find symbolic links in your home directory. |
| `find ~ -type l -print` | Find symbolic links in your home directory and print the full path. |
| `find / -perm -o+w 2>/dev/null` | Find all world-writable files and directories. |
| `find / -type f -cmin -5 2>/dev/null` | Find all files that have been created or changed in the last five minutes. |

I am also including a list of common file extentions that I look for:

| File Type | Description |
| --- | --- |
| .c | A C source file |
| .conf | A configuration file. System-wide config files reside in /etc while any user-specific configuration will be somewhere in the user's home directory |
| .cpp | A C++ source file |
| .gif | An image file |
| .h | A C or C++ header file |
| .html | An HTML file |
| .jpg | An image file |
| .log | A system or program's log file |
| .pdf | An image of a document |
| .php | A PHP script |
| .png | An image file |
| .py | A Python script |
| .sh | A shell script |
| .so | A shared object or a shared library. This is the equivalent of a Windows .dll file |
| .tar | A compressed file|
| .tar.bz2 | A compressed file |
| .txt | A plain text file |
| .zip | An extension for files in zip format, a popular file compression format |
