# ffuf

The ffuf tool is useful for quickly fuzzing things like directories, subdomains and parameters on forms. The ffuf tools has some very intuitive syntax to use. Like all fuzzers, the wordlists are the most important part of fuzzing.

## Usage

```bash
$ ffuf -h
Fuzz Faster U Fool - v1.3.1

HTTP OPTIONS:
  -H                  Header `"Name: Value"`, separated by colon. Multiple -H flags are accepted.
  -X                  HTTP method to use
  -b                  Cookie data `"NAME1=VALUE1; NAME2=VALUE2"` for copy as curl functionality.
  -d                  POST data
  -ignore-body        Do not fetch the response content. (default: false)
  -r                  Follow redirects (default: false)
  -recursion          Scan recursively. Only FUZZ keyword is supported, and URL (-u) has to end in it. (default: false)
  -recursion-depth    Maximum recursion depth. (default: 0)
  -recursion-strategy Recursion strategy: "default" for a redirect based, and "greedy" to recurse on all matches (default: default)
  -replay-proxy       Replay matched requests using this proxy.
  -timeout            HTTP request timeout in seconds. (default: 10)
  -u                  Target URL
  -x                  Proxy URL (SOCKS5 or HTTP). For example: http://127.0.0.1:8080 or socks5://127.0.0.1:8080

GENERAL OPTIONS:
  -V                  Show version information. (default: false)
  -ac                 Automatically calibrate filtering options (default: false)
  -acc                Custom auto-calibration string. Can be used multiple times. Implies -ac
  -c                  Colorize output. (default: false)
  -config             Load configuration from a file
  -maxtime            Maximum running time in seconds for entire process. (default: 0)
  -maxtime-job        Maximum running time in seconds per job. (default: 0)
  -noninteractive     Disable the interactive console functionality (default: false)
  -p                  Seconds of `delay` between requests, or a range of random delay. For example "0.1" or "0.1-2.0"
  -rate               Rate of requests per second (default: 0)
  -s                  Do not print additional information (silent mode) (default: false)
  -sa                 Stop on all error cases. Implies -sf and -se. (default: false)
  -se                 Stop on spurious errors (default: false)
  -sf                 Stop when > 95% of responses return 403 Forbidden (default: false)
  -t                  Number of concurrent threads. (default: 40)
  -v                  Verbose output, printing full URL and redirect location (if any) with the results. (default: false)

MATCHER OPTIONS:
  -mc                 Match HTTP status codes, or "all" for everything. (default: 200,204,301,302,307,401,403,405)
  -ml                 Match amount of lines in response
  -mr                 Match regexp
  -ms                 Match HTTP response size
  -mw                 Match amount of words in response

FILTER OPTIONS:
  -fc                 Filter HTTP status codes from response. Comma separated list of codes and ranges
  -fl                 Filter by amount of lines in response. Comma separated list of line counts and ranges
  -fr                 Filter regexp
  -fs                 Filter HTTP response size. Comma separated list of sizes and ranges
  -fw                 Filter by amount of words in response. Comma separated list of word counts and ranges

INPUT OPTIONS:
  -D                  DirSearch wordlist compatibility mode. Used in conjunction with -e flag. (default: false)
  -e                  Comma separated list of extensions. Extends FUZZ keyword.
  -ic                 Ignore wordlist comments (default: false)
  -input-cmd          Command producing the input. --input-num is required when using this input method. Overrides -w.
  -input-num          Number of inputs to test. Used in conjunction with --input-cmd. (default: 100)
  -input-shell        Shell to be used for running command
  -mode               Multi-wordlist operation mode. Available modes: clusterbomb, pitchfork (default: clusterbomb)
  -request            File containing the raw http request
  -request-proto      Protocol to use along with raw request (default: https)
  -w                  Wordlist file path and (optional) keyword separated by colon. eg. '/path/to/wordlist:KEYWORD'

OUTPUT OPTIONS:
  -debug-log          Write all of the internal logging to the specified file.
  -o                  Write output to file
  -od                 Directory path to store matched results to.
  -of                 Output file format. Available formats: json, ejson, html, md, csv, ecsv (or, 'all' for all formats) (default: json)
  -or                 Don't create the output file if we don't have results (default: false)

EXAMPLE USAGE:
  Fuzz file paths from wordlist.txt, match all responses but filter out those with content-size 42.
  Colored, verbose output.
    ffuf -w wordlist.txt -u https://example.org/FUZZ -mc all -fs 42 -c -v

  Fuzz Host-header, match HTTP 200 responses.
    ffuf -w hosts.txt -u https://example.org/ -H "Host: FUZZ" -mc 200

  Fuzz POST JSON data. Match all responses not containing text "error".
    ffuf -w entries.txt -u https://example.org/ -X POST -H "Content-Type: application/json" \
      -d '{"name": "FUZZ", "anotherkey": "anothervalue"}' -fr "error"

  Fuzz multiple locations. Match only responses reflecting the value of "VAL" keyword. Colored.
    ffuf -w params.txt:PARAM -w values.txt:VAL -u https://example.org/?PARAM=VAL -mr "VAL" -c

  More information and examples: https://github.com/ffuf/ffuf
```

## Examples

The following examples are ones that I have used in capture the flag exercises. The wordlists that are provided are ones that are found on Kali unless otherwise specified.

For each of the examples below, here are the variables that I am using:

- The target machine is found at ip address `10.10.1.1`

### Directory Enumeration

When I find a web server on a target, this is the first scan that I run. I am a big fan of ffuf's syntax for this and other scans. A simple scan looks like the following:

```bash
$ ffuf -u http://10.10.1.1/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-large-directories-lowercase.txt
```

- The `FUZZ` part of the command lets ffuf know where I want to fuzz the words in the wordlist.
- The `-u` lets ffuf know what the target url is.
- The `-w` lets ffuf know what wordlist to use.

### File Enumeration

The above command can be altered slightly to find files with particular extensions. This can be very handy when I am looking for things like zip archives or hidden files. I run this in folders that have suspicious directory names like `test`, `download`, `logs`, `data`, etc...

Here is the command to search for files:

```bash
$ ffuf -u http://10.10.1.1/data/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-large-files-lowercase.txt -e .html,.php,.txt,.zip
```

- The `FUZZ` part of the command lets ffuf know where I want to fuzz the words in the wordlist.
- Notice that I am looking in the data directory. I use whatever directory I find that is suspicious.
- The `-u` lets ffuf know what the target url is.
- The `-w` lets ffuf know what wordlist to use.
- The `-e` lets ffuf know what file extensions we are interested in.

### Subdomain Enumeration

Once in a while, a capture the flag machine has some subdomains that I have to find so that I can continue on in the challenge. The ffuf tool makes this easy to enumerate as well. Here is the syntax:

```bash
$ ffuf -H "Host: FUZZ.10.10.1.1" -H "User-Agent: PENTEST" -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-large-directories-lowercase.txt -u http://10.10.1.1 -fs 100
```

- The `FUZZ` part of the command lets ffuf know where I want to fuzz the words in the wordlist.
- The `-u` lets ffuf know what the target url is.
- The `-w` lets ffuf know what wordlist to use.
- Notice that I am using FUZZ in a header. This will check if the subdomain exists.
- I also included an User-Agent header this was a recommendation that I got from some videos on youtube. I can't remember which ones.
- The `fs` parameter lets me filter responses by size. This needs to be ajusted based on what I get back. Most responses come back as false positives but the actual responses that are subdomains will have a larger size. This parameter is used to filter them out.
