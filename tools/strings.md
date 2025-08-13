# Strings

- [Introduction](#introduction)
- [Usage](#usage)
- [Examples](#examples)

## Introduction

Some files, like binaries, are loaded with useful plain text information but it is hard to read because the file also has a lot of characters that are not readable. The strings command looks for all the text in a file that is printable and sends it to standard output. This command is a staple in capture the flag challenges.

## Usage

```bash
Usage: strings [option(s)] [file(s)]
 Display printable strings in [file(s)] (stdin by default)
 The options are:
  -a - --all                Scan the entire file, not just the data section [default]
  -d --data                 Only scan the data sections in the file
  -f --print-file-name      Print the name of the file before each string
  -n --bytes=[number]       Locate & print any NUL-terminated sequence of at
  -<number>                   least [number] characters (default 4).
  -t --radix={o,d,x}        Print the location of the string in base 8, 10 or 16
  -w --include-all-whitespace Include all whitespace as valid string characters
  -o                        An alias for --radix=o
  -T --target=<BFDNAME>     Specify the binary file format
  -e --encoding={s,S,b,l,B,L} Select character size and endianness:
                            s = 7-bit, S = 8-bit, {b,l} = 16-bit, {B,L} = 32-bit
  -s --output-separator=<string> String used to separate strings in output.
  @<file>                   Read options from <file>
  -h --help                 Display this information
  -v -V --version           Print the program's version number
strings: supported targets: elf64-x86-64 elf32-i386 elf32-iamcu elf32-x86-64 pei-i386 pei-x86-64 elf64-l1om elf64-k1om elf64-little elf64-big elf32-little elf32-big pe-x86-64 pe-bigobj-x86-64 pe-i386 srec symbolsrec verilog tekhex binary ihex plugin
Report bugs to <http://www.sourceware.org/bugzilla/>
```

## Examples

| What I want to do. | Example |
| --- | --- |
| Read the binary file called `exploit`. | `strings exploit` |
| Find hidden messagse in an image file. | `strings image.jpg` |
| Use with find to scan multiple binaries for keywords. | `find . -type f -exec strings {};` |
