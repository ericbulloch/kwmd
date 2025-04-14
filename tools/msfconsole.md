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
