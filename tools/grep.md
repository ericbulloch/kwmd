# grep

The grep tool is commonly used to find text patterns in files. It complements the [find](find.md) command very nicely. Closely related to grep is the idea of regular expressions.

## Usage

```bash
$ grep --help
Usage: grep [OPTION]... PATTERNS [FILE]...
Search for PATTERNS in each FILE.
Example: grep -i 'hello world' menu.h main.c
PATTERNS can contain multiple patterns separated by newlines.

Pattern selection and interpretation:
  -E, --extended-regexp     PATTERNS are extended regular expressions
  -F, --fixed-strings       PATTERNS are strings
  -G, --basic-regexp        PATTERNS are basic regular expressions
  -P, --perl-regexp         PATTERNS are Perl regular expressions
  -e, --regexp=PATTERNS     use PATTERNS for matching
  -f, --file=FILE           take PATTERNS from FILE
  -i, --ignore-case         ignore case distinctions in patterns and data
      --no-ignore-case      do not ignore case distinctions (default)
  -w, --word-regexp         match only whole words
  -x, --line-regexp         match only whole lines
  -z, --null-data           a data line ends in 0 byte, not newline

Miscellaneous:
  -s, --no-messages         suppress error messages
  -v, --invert-match        select non-matching lines
  -V, --version             display version information and exit
      --help                display this help text and exit

Output control:
  -m, --max-count=NUM       stop after NUM selected lines
  -b, --byte-offset         print the byte offset with output lines
  -n, --line-number         print line number with output lines
      --line-buffered       flush output on every line
  -H, --with-filename       print file name with output lines
  -h, --no-filename         suppress the file name prefix on output
      --label=LABEL         use LABEL as the standard input file name prefix
  -o, --only-matching       show only nonempty parts of lines that match
  -q, --quiet, --silent     suppress all normal output
      --binary-files=TYPE   assume that binary files are TYPE;
                            TYPE is 'binary', 'text', or 'without-match'
  -a, --text                equivalent to --binary-files=text
  -I                        equivalent to --binary-files=without-match
  -d, --directories=ACTION  how to handle directories;
                            ACTION is 'read', 'recurse', or 'skip'
  -D, --devices=ACTION      how to handle devices, FIFOs and sockets;
                            ACTION is 'read' or 'skip'
  -r, --recursive           like --directories=recurse
  -R, --dereference-recursive  likewise, but follow all symlinks
      --include=GLOB        search only files that match GLOB (a file pattern)
      --exclude=GLOB        skip files that match GLOB
      --exclude-from=FILE   skip files that match any file pattern from FILE
      --exclude-dir=GLOB    skip directories that match GLOB
  -L, --files-without-match  print only names of FILEs with no selected lines
  -l, --files-with-matches  print only names of FILEs with selected lines
  -c, --count               print only a count of selected lines per FILE
  -T, --initial-tab         make tabs line up (if needed)
  -Z, --null                print 0 byte after FILE name

Context control:
  -B, --before-context=NUM  print NUM lines of leading context
  -A, --after-context=NUM   print NUM lines of trailing context
  -C, --context=NUM         print NUM lines of output context
  -NUM                      same as --context=NUM
      --color[=WHEN],
      --colour[=WHEN]       use markers to highlight the matching strings;
                            WHEN is 'always', 'never', or 'auto'
  -U, --binary              do not strip CR characters at EOL (MSDOS/Windows)

When FILE is '-', read standard input.  With no FILE, read '.' if
recursive, '-' otherwise.  With fewer than two FILEs, assume -h.
Exit status is 0 if any line (or file if -L) is selected, 1 otherwise;
if any error occurs and -q is not given, the exit status is 2.

Report bugs to: bug-grep@gnu.org
GNU grep home page: <http://www.gnu.org/software/grep/>
General help using GNU software: <https://www.gnu.org/gethelp/>
```

## Examples

Grep has a lot of options to help find specific text in files. Rather than list them out I decided to write a scenario and then write the grep command that would handle that. I'll try to use capture the flag examples as I go.

### Search for text in a file.

This match is case-sensitive so Error or ERROR will not match.

```bash
$ grep "error" logfile.txt
```

### Search recursively in a directory for the above text.

```bash
$ grep -r "error" /var/log/
```

### Case-insensitive search.

The following will find all lines that have error with any case. That means that Error, ERROR, error and eRrOr will all match.

```bash
$ grep -i "error" logfile.txt
```

### Count matching lines.

Display how many lines match the text.

```bash
$ grep -c "error" logfile.txt
433
```

### Show line numbers.

This command will show the line number with a colon (:) after the line number then the full text of the line. The output below found matches on lines 1 and 35.

```bash
$ grep -n "root" /etc/passwd
1:root:x:0:0:root:/root:/bin/bash
35:nm-openvpn:x:116:123:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/usr/sbin/nologin
```

### Show invert match (the lines that don't contain the pattern).

This command will show all the log lines that don't have 10.10.100.1 (my machine ip address).

```bash
$ grep -v "10.10.100.1" /var/log
```

### Use regular expressions.

This command will match all the lines in the users.txt file that have user1, user2, ..., user9.

```bash
$ grep "user[1-9]" users.txt
```

### Search for multiple patterns.

This will find all lines that match status code 404 or status code 500.

```bash
$ grep -E "404|500" webserver.log
```

### Print only the matching part of the line.

This matches phone numbers with dashes between the numbers and only displays the phone number instead of the whole line of text.

```bash
$ grep -o "[0-9]\{3\}-[0-9]\{3\}-[0-9]\{4\}" phonebook.txt
```

### Print the line and add color to the part that matches.

```bash
$ grep --color=always "password" config.txt
```

### Search for whole words only.

Matches admin, but not administrator or superadmin.

```bash
$ grep -w "admin" users.txt
```

### Search multiple config files in the same directory.

```bash
$ grep "listen" *.conf
```

### Display lines and after the match.

This will display 8 total lines (2 before the matching line, 1 for the matching line and 5 lines after the matching line).

```bash
$ grep -A 5 -B 2 "Error" logfile.log
```

### Quiet mode (checks if the pattern exists).

This command will print Found if the text ubuntu is in the /etc/passwd file.

```bash
$ grep -q "ubuntu" /etc/passwd && echo "Found"
```

### Check if apache is running on the system.

```bash
$ ps aux | grep "apache"
```
