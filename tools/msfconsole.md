# msfconsole

One of my favorite tools is msfconsole. It is the console part of Metasploit. To say this tool is powerful is a massive understatement. It can do so many things. It can allow you to take notes, lookup vulnerabilites and execute payloads. The library of vulnerabilities is massive. The configuration that it provides to create a payload is unreal. Spending time with this tool has been an eye opening experience for me.

## Usage

Running `msfconsole -h` provided the following output:

```bash
Usage: msfconsole [options]

Common options:
    -E, --environment ENVIRONMENT    Set Rails environment, defaults to RAIL_ENV environment variable or 'production'

Database options:
    -M, --migration-path DIRECTORY   Specify a directory containing additional DB migrations
    -n, --no-database                Disable database support
    -y, --yaml PATH                  Specify a YAML file containing database settings

Framework options:
    -c FILE                          Load the specified configuration file
    -v, -V, --version                Show version

Module options:
        --[no-]defer-module-loads    Defer module loading unless explicitly asked
    -m, --module-path DIRECTORY      Load an additional module path

Console options:
    -a, --ask                        Ask before exiting Metasploit or accept 'exit -y'
    -H, --history-file FILE          Save command history to the specified file
    -l, --logger STRING              Specify a logger to use (Stdout, StdoutWithoutTimestamps, TimestampColorlessFlatfile, Flatfile, Stderr)
        --[no-]readline
    -L, --real-readline              Use the system Readline library instead of RbReadline
    -o, --output FILE                Output to the specified file
    -p, --plugin PLUGIN              Load a plugin on startup
    -q, --quiet                      Do not print the banner on startup
    -r, --resource FILE              Execute the specified resource file (- for stdin)
    -x, --execute-command COMMAND    Execute the specified console commands (use ; for multiples)
    -h, --help                       Show this message
```

## Searching

The msfconsole's search is really good. I will often times search for something generic like 'ftp anonymous' to get the module that will check if anonymous logins are allowed. The msfconsole is loaded with useful modules to help find and exploit vulnerabilities.

Going with the example that was just mentioned, when I search for 'ftp anonymous' the output will look like:

```bash
Matching Modules
================

   #   Name                                                     Disclosure Date  Rank    Check  Description
   -   ----                                                     ---------------  ----    -----  -----------
   0   auxiliary/scanner/ftp/anonymous                          .                normal  No     Anonymous FTP Access Detection
   ...
```

To use that module, all I have to do is run `use 0`. That will change my console's appearance to let me know the module loaded. In this case, the console will display:

`msf6 auxiliary(scanner/ftp/anonymous) > `

Searches can be refined and even include version numbers. The msfconsole is very robust when it comes to searching for modules.
