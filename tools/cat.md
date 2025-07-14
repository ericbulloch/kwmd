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
This is text that I am adding to newfile.txt
```

### Append to an existing file (basic text entry).

Adds input to the end of a file (existing.txt in this case). When I am done typing text I press Ctrl+D to save and exit.

```bash
$ cat >> existing.txt
This text will be added to the end of existing.txt
```
