# cat

The cat tool is commonly used to view the contents of a file. It is also used to append text, write text and concatenate text to a file.

## Usage

```bash
$ cat --help

```

## Examples

Cat is a foundational command when working with Linux. The output of cat is often piped to other tools perform tasks.

### Display the contents of a file.

```bash
$ cat filename.txt
Hello, world!
This is me outputting a file.
```

### Display multiple files.

```bash
$ cat file1.txt file2.txt
This is output from file1.txt
This is output from file2.txt
```

### Create a new file (basic text entry).

I use this command to type content into a file (newfile.txt in this case). When I am done typing text I press `Ctrl+D` to save and exit.

```bash
$ cat > newfile.txt
This text is all that will be in newfile.txt.
```

### Append to an existing file (basic text entry).

Adds input to the end of a file (existing.txt in this case). When I am done typing text I press Ctrl+D to save and exit.

```bash
$ cat >> existing.txt
This text will start at the end of the last line of the existing.txt file.
```

### Redirect contents of one file into another.

```bash
$ cat source.txt > destination.txt
```

### Concatenate multiple files into a new file.

```bash
$ cat part1.txt part2.txt > full.txt
```

### Number all output lines.

```bash
$ cat -n notes.txt
     1	Hello kwmd!
     2	This is another line.
     3		Third line here.
     4	Final line.
```

### Show tabs and line endings.

The -T option shows tabs as ^I. The -E option shows newlines as $.

```bash
$ cat -T -E notes.txt
Hello kwmd!$
This is another line.$
^IThird line here.$
Final line.$
```

### Suppress blank lines.

Removes repeated blank lines—only one blank line remains between text blocks.

```bash
$ cat -s file.txt
```

### Display all files that match wildcard.

Displays all .log files in the current directory.

```bash
$ cat *.log
```

### Cat a file and then grep it.

```bash
$ cat access.log | grep "404"
```

### Combine wordlist files and sort unique lines.

```bash
$ cat wordlist1.txt other.txt dict.txt | sort | uniq
```

### Read from standard input and as well as a file.

First reads from input (keyboard or pipe), then displays the contents of file.txt.

```bash
$ cat - file.txt
```
