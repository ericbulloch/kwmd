# john

The john tool (aka John the Ripper) is an extremely effective password cracking tool. I have used it in multiple capture the flag events to crack hashes, ciphers and passwords. I have used it to get ssh, Keepass, Linux user and ftp passwords.

It is a very versatile tool. It can generate wordlists and it can also use one that you provide.

## Usage

Running `john -h` provided the following output:

```bash
John the Ripper 1.9.0-jumbo-1+bleeding-51f7f3dcd 2020-09-01 13:29:43 +0200 OMP [linux-gnu 64-bit x86_64 AVX2 AC]
Copyright (c) 1996-2019 by Solar Designer and others
Homepage: https://www.openwall.com/john/

Usage: john [OPTIONS] [PASSWORD-FILES]
--single[=SECTION[,..]]    "single crack" mode, using default or named rules
--single=:rule[,..]        same, using "immediate" rule(s)
--wordlist[=FILE] --stdin  wordlist mode, read words from FILE or stdin
                  --pipe   like --stdin, but bulk reads, and allows rules
--loopback[=FILE]          like --wordlist, but extract words from a .pot file
--dupe-suppression         suppress all dupes in wordlist (and force preload)
--prince[=FILE]            PRINCE mode, read words from FILE
--encoding=NAME            input encoding (eg. UTF-8, ISO-8859-1). See also
                           doc/ENCODINGS and --list=hidden-options.
--rules[=SECTION[,..]]     enable word mangling rules (for wordlist or PRINCE
                           modes), using default or named rules
--rules=:rule[;..]]        same, using "immediate" rule(s)
--rules-stack=SECTION[,..] stacked rules, applied after regular rules or to
                           modes that otherwise don't support rules
--rules-stack=:rule[;..]   same, using "immediate" rule(s)
--incremental[=MODE]       "incremental" mode [using section MODE]
--mask[=MASK]              mask mode using MASK (or default from john.conf)
--markov[=OPTIONS]         "Markov" mode (see doc/MARKOV)
--external=MODE            external mode or word filter
--subsets[=CHARSET]        "subsets" mode (see doc/SUBSETS)
--stdout[=LENGTH]          just output candidate passwords [cut at LENGTH]
--restore[=NAME]           restore an interrupted session [called NAME]
--session=NAME             give a new session the NAME
--status[=NAME]            print status of a session [called NAME]
--make-charset=FILE        make a charset file. It will be overwritten
--show[=left]              show cracked passwords [if =left, then uncracked]
--test[=TIME]              run tests and benchmarks for TIME seconds each
                           (if TIME is explicitly 0, test w/o benchmark)
--users=[-]LOGIN|UID[,..]  [do not] load this (these) user(s) only
--groups=[-]GID[,..]       load users [not] of this (these) group(s) only
--shells=[-]SHELL[,..]     load users with[out] this (these) shell(s) only
--salts=[-]COUNT[:MAX]     load salts with[out] COUNT [to MAX] hashes
--costs=[-]C[:M][,...]     load salts with[out] cost value Cn [to Mn]. For
                           tunable cost parameters, see doc/OPTIONS
--save-memory=LEVEL        enable memory saving, at LEVEL 1..3
--node=MIN[-MAX]/TOTAL     this node's number range out of TOTAL count
--fork=N                   fork N processes
--pot=NAME                 pot file to use
--list=WHAT                list capabilities, see --list=help or doc/OPTIONS
--devices=N[,..]           set OpenCL device(s) (see --list=opencl-devices)
--format=NAME              force hash of type NAME. The supported formats can
                           be seen with --list=formats and --list=subformats
```

## Examples

The following examples are ones that I have used in capture the flag exercises. I rarely include a wordlist in capture the flag events. I will mention the type of file that john is trying to crack.

### Keepass

Once during a capture the flag event I found a keepass file. The keepass file is not in a format that john knows how to use. Fortunately, there are tools online that I was able to use that converted the file to a format that john could understand. In this example I am going to use a keepass file called database.kdbx that is in the directory I am currently in. The steps are the following:

- Run the keepass2john script on my keepass database. `keepass2john database.kdbx > john.txt`
- Run john. `john --format=keepass john.txt`

### Linux shadow file

I have had to crack some user's linux password in a capture the flag event. For this example, I am on the linux machine and I can read both the /etc/passwd and /etc/shadow files. Here are the steps to run:

- Create an unshadow file that john can use. Run `unshadow /etc/passwd /etc/shadow > mypasswd`
- Run john on the new file. `john mypasswd`

#### Useful switches with Linux shadow file

If I have a custom wordlist that I would like to use, here is the command to use:

`john --wordlist=wordlist.txt mypasswd`

Once some passwords have been cracked, john stores the results in the $JOHN/john.pot file. They do not intend for me to view that file directly. The have provided to following command to see the results:

`john --show mypasswd`

I can also see if any root (UID 0) accounts got cracked with the following command:

`john --show --users=0 mypasswd`

### RAR archive file

I have found .rar files that were password protected in a capture the flag event. Similar to Keepass, there are tools that can convert the rar file to a format that john can use. In this example I have the secrets.rar file in my current directory. Here are the steps:

- Run rar2john on the rar file. `rar2john secrets.rar > john.txt
- Run john. `john john.txt`

### ZIP archive file

I have found .zip files that were password protected in a capture the flag event. Similar to Keepass, there are tools that can convert the zip file to a format that john can use. In this example I have the secrets.zip file in my current directory. Here are the steps:

- Run zip2john on the rar file. `zip2john secrets.rar > john.txt
- Run john. `john john.txt`

### PGP and ASC file

I have been a part of a few capture the flag events that use the combination of a .gpg and .asc file to get credentials. The process has a few steps, they are:

- Convert the the .asc file to a hash that john can understand.
- Run john on the new hash to get a password.
- Use the password when importing the .asc file.
- Decrypt the .pgp file to get the credentials.

As an example, I have 2 files named mine.asc and credentials.pgp. Here are the commands to get the credentials:

For the first step, I would run:

`g2g2john mine.asc > hash.txt`

The hash.txt file has a hash that john can now understand. I run the following command so john can crack the password:

`john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt`

When john cracks the password it will look like the following:

```bash
Press 'q' or Ctrl-C to abort, almost any other key for status
my_password      (mine)
```

Now that I have the decrypted password, I decrypt the credentials.pgp file with the following commands:

```bash
gpg --import mine.asc
gpg -d credentials.pgp
```

I was asked for a password after running each of those commands, the password would be my_password that john just cracked.

### MD5

Every now and then I will find a hash that [CrackStation](https://crackstation.net/) doesn't have a solution for. I can use john to try to crack the hash. John has a built in word list but I can also supply my own. In the following example I have an md5 hash that is stored in a file called hash.txt in the current directory. I also know for sure that this is an md5 hash. This is the command to have john try to crack the hash:

`john --format=raw-md5 hello.txt`

The `--format` option is important because if it is not supplied john will try to crack the hash with multiple different hashing algorithms that it detects.

I was abled to see the cracked hash, once john finished, with the following command:

`john --format=raw-md5 hello.txt --show`

I often times want to use my own word list when I am doing this. For this example, my wordlist is found in list.txt. To use a custom word list change the command to the following:

`john --format=raw-md5 --wordlist=list.txt hello.txt`

I still had to run the following command to see the cracked hash once john finished:

`john --format=raw-md5 hello.txt --show`
