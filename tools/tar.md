# tar

- [Introduction](#introduction)
- [Usage](#usage)
- [Examples](#examples)

## Introduction

The tar command is used for creating, maintaining, modifying, and extracting files from archives that are commonly known as "tarballs". They are also sometimes called "tape archives" which is what tar is short for.

## Usage

```bash

```

## Examples

In the following example I have three files called `file1.txt`, `file2.txt`, and `file3.txt`. All the examples below will use these three files as part of a `kwmd.tar` tarball.

### Creating a tarball or archive

```bash
$ tar -cvf kwmd.tar file1.txt file2.txt file3.txt
file1.txt
file2.txt
file3.txt
```

The `-c` option is used to tell the tar command that I am creating an archive. The `-v` option is for verbose output. The `-f` option tells the tar command what the name of archive file is.

### View the files in a tarball

```bash
$ tar -tvf kwmd.tar
-rwx------ 1 root root      513  Oct 22    2025 06:11 file1.txt
-rwx------ 1 root root     8913  Oct 22    2025 06:11 file2.txt
-rwx------ 1 root root      769  Oct 22    2025 06:11 file3.txt
```

The `-t` option is used to tell the tar command that I want a content list of the files in the archive. The `-v` option is for verbose output. The `-f` option tells the tar command what the name of archive file is.

### Extract the files from the tarball

```bash
$ tar -xvf kwmd.tar
file1.txt
file2.txt
file3.txt
```

The `-x` option is used to tell the tar command that I want to extract an archive. The `-v` option is for verbose output. The `-f` option tells the tar command what the name of archive file is.
