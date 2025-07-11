# find

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
find: /mine/var/log/mysql_stuff: Permission denied
```

### Find a file owned by the user gimli with a size of 85 kilobytes in the directory /home/gimli.

```bash
$ find /home/gimli -type f -use gimli -size 85 2>/dev/null
```

### If you get stuck, there is a file somewhere on the disk drive called ReadMeIfStuck.txt

```bash
$ find / -type f -name ReadMeIfStuck.txt 2>/dev/null
```

### Look for a directory called "order numbers" (notice the space).

```bash
$ find / -type d -name order\ numbers 2>/dev/null
```

### Find a file with a modified date of 2009-05-02 from the archived_orders directory

```bash
$ find archived_orders/ -type f -newermt 2009-05-01 ! -newermt 2009-02-03 2>/dev/null
```

### Find a file named .hidden.txt inside your home directory

```bash
$ find ~/ -type f -name .hidden.txt 2>/dev/null
```
