# msfconsole

- [Introduction](#introduction)
- [Usage](#usage)
- [Searching](#searching)
- [Module](#module)

## Introduction

One of my favorite tools is msfconsole. It is the console part of Metasploit. To say this tool is powerful is a massive understatement. It can do so many things. It can allow you to take notes, lookup vulnerabilites and execute payloads. The library of vulnerabilities is massive. The configuration that it provides to create a payload is unreal. Spending time with this tool has been an eye opening experience for me.

## Usage

```bash
$ msfconsole -h
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

Here is what that will look like:

```bash
msf6 > search ftp anonymous
Matching Modules
================

   #   Name                                                     Disclosure Date  Rank    Check  Description
   -   ----                                                     ---------------  ----    -----  -----------
   0   auxiliary/scanner/ftp/anonymous                          .                normal  No     Anonymous FTP Access Detection
   ...
msf6 > use 0
msf6 auxiliary(scanner/ftp/anonymous) > 
```

To use that module, all I have to do is run `use 0`. That will change my console's appearance to let me know the module loaded as seen in the output above.

Searches can be refined and even include version numbers. The msfconsole is very robust when it comes to searching for modules.

## Module

Once I have selected a module like in the example above, I need to provide the parameters necessary for the module to run. Here is an example:

```bash
msf6 auxiliary(scanner/ftp/anonymous) > show options

Module options (auxiliary/scanner/ftp/anonymous):

   Name     Current Setting      Required  Description
   ----     ---------------      --------  -----------
   FTPPASS  mozilla@example.com  no        The password for the specified username
   FTPUSER  anonymous            no        The username to authenticate as
   RHOSTS                        yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT    21                   yes       The target port (TCP)
   THREADS  1                    yes       The number of concurrent threads (max one per host)


View the full module info with the info, or info -d command.
```

The output shows that 3 options are required. I only have 2 of them set. I need to set the RHOSTS option or else I can't run this module. I am going to run this module on a machine with the ip address of 10.10.1.112. Here is an example of setting an option and making sure it was set properly:

```bash
msf6 auxiliary(scanner/ftp/anonymous) > set rhosts 10.10.1.112
msf6 auxiliary(scanner/ftp/anonymous) > show options

Module options (auxiliary/scanner/ftp/anonymous):

   Name     Current Setting      Required  Description
   ----     ---------------      --------  -----------
   FTPPASS  mozilla@example.com  no        The password for the specified username
   FTPUSER  anonymous            no        The username to authenticate as
   RHOSTS   10.10.1.112          yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT    21                   yes       The target port (TCP)
   THREADS  1                    yes       The number of concurrent threads (max one per host)


View the full module info with the info, or info -d command.
```

Now I can execute the module with the following command:

```bash
msf6 auxiliary(scanner/ftp/anonymous) > run
```

The output will be dependent on the success of the module and what module was ran.

When I want to run another module I type `back` and that unselects the module. Here is an example:

```bash
msf6 auxiliary(scanner/ftp/anonymous) > back
msf6 >
```

