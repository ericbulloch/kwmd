# gobuster

The gobuster tool was the first tool that I learned for fuzzing content and subdirectories. Like all fuzzers, the wordlists are the most important part of fuzzing.

## Usage

Running `gobuster -h` provided the following output:

```bash
Usage:
  gobuster [command]

Available Commands:
  completion  Generate the autocompletion script for the specified shell
  dir         Uses directory/file enumeration mode
  dns         Uses DNS subdomain enumeration mode
  fuzz        Uses fuzzing mode. Replaces the keyword FUZZ in the URL, Headers and the request body
  gcs         Uses gcs bucket enumeration mode
  help        Help about any command
  s3          Uses aws bucket enumeration mode
  tftp        Uses TFTP enumeration mode
  version     shows the current version
  vhost       Uses VHOST enumeration mode (you most probably want to use the IP address as the URL parameter)

Flags:
      --debug                 Enable debug output
      --delay duration        Time each thread waits between requests (e.g. 1500ms)
  -h, --help                  help for gobuster
      --no-color              Disable color output
      --no-error              Don't display errors
  -z, --no-progress           Don't display progress
  -o, --output string         Output file to write results to (defaults to stdout)
  -p, --pattern string        File containing replacement patterns
  -q, --quiet                 Don't print the banner and other noise
  -t, --threads int           Number of concurrent threads (default 10)
  -v, --verbose               Verbose output (errors)
  -w, --wordlist string       Path to the wordlist. Set to - to use STDIN.
      --wordlist-offset int   Resume from a given position in the wordlist (defaults to 0)

Use "gobuster [command] --help" for more information about a command.
```

## Examples

The following examples are ones that I have used in capture the flag exercises. The wordlists that are provided are ones that are found on Kali unless otherwise specified.

For each of the examples below, here are the variables that I am using:

- Password wordlist found in `/usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt`
- The target machine is found at ip address `10.10.1.1`

### directory/file (dir) enumeration mode

The first search I usually do once I have found that a web server is running on the target is to do a directory search on the web site. The gobuster tool makes this very easy to do. It is a specialized command for gobuster and so it has different help output from the vanilla gobuster help. Here is the output from running `gobuster dir -h`:

```bash
Uses directory/file enumeration mode

Usage:
  gobuster dir [flags]

Flags:
  -f, --add-slash                         Append / to each request
      --client-cert-p12 string            a p12 file to use for options TLS client certificates
      --client-cert-p12-password string   the password to the p12 file
      --client-cert-pem string            public key in PEM format for optional TLS client certificates
      --client-cert-pem-key string        private key in PEM format for optional TLS client certificates (this key needs to have no password)
  -c, --cookies string                    Cookies to use for the requests
  -d, --discover-backup                   Also search for backup files by appending multiple backup extensions
      --exclude-length string             exclude the following content lengths (completely ignores the status). You can separate multiple lengths by comma and it also supports ranges like 203-206
  -e, --expanded                          Expanded mode, print full URLs
  -x, --extensions string                 File extension(s) to search for
  -X, --extensions-file string            Read file extension(s) to search from the file
  -r, --follow-redirect                   Follow redirects
  -H, --headers stringArray               Specify HTTP headers, -H 'Header1: val1' -H 'Header2: val2'
  -h, --help                              help for dir
      --hide-length                       Hide the length of the body in the output
  -m, --method string                     Use the following HTTP method (default "GET")
      --no-canonicalize-headers           Do not canonicalize HTTP header names. If set header names are sent as is.
  -n, --no-status                         Don't print status codes
  -k, --no-tls-validation                 Skip TLS certificate verification
  -P, --password string                   Password for Basic Auth
      --proxy string                      Proxy to use for requests [http(s)://host:port] or [socks5://host:port]
      --random-agent                      Use a random User-Agent string
      --retry                             Should retry on request timeout
      --retry-attempts int                Times to retry on request timeout (default 3)
  -s, --status-codes string               Positive status codes (will be overwritten with status-codes-blacklist if set). Can also handle ranges like 200,300-400,404.
  -b, --status-codes-blacklist string     Negative status codes (will override status-codes if set). Can also handle ranges like 200,300-400,404. (default "404")
      --timeout duration                  HTTP Timeout (default 10s)
  -u, --url string                        The target URL
  -a, --useragent string                  Set the User-Agent string (default "gobuster/3.6")
  -U, --username string                   Username for Basic Auth

Global Flags:
      --debug                 Enable debug output
      --delay duration        Time each thread waits between requests (e.g. 1500ms)
      --no-color              Disable color output
      --no-error              Don't display errors
  -z, --no-progress           Don't display progress
  -o, --output string         Output file to write results to (defaults to stdout)
  -p, --pattern string        File containing replacement patterns
  -q, --quiet                 Don't print the banner and other noise
  -t, --threads int           Number of concurrent threads (default 10)
  -v, --verbose               Verbose output (errors)
  -w, --wordlist string       Path to the wordlist. Set to - to use STDIN.
      --wordlist-offset int   Resume from a given position in the wordlist (defaults to 0)
```

A simple directory enumerate looks like the following:

`gobuster dir -u http://10.10.1.1 -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt`

- The `dir` part of the command lets gobuster know that this is a directory search
- The `-u` lets gobuster know what the target url is
- The `-w` lets gobuster know what wordlist to use

#### Useful options for directory/file enumeration mode

| example  | what it means  | when I use it  |
| -------- | -------------- | -------------- |
| `gobuster dir -u http://10.10.1.1 -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt -t 4 --delay 3000`  | The `-t` flag decreases the thread count from 10 to 4 and the `--delay 3000` flag is increasing the delay in each thread between requests.  | If I want to be less noisy on a network or if the machine seems to have less resources because it is slow to handle requests.  |
| `gobuster dir -u http://10.10.1.1 -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt -t 20 --delay 500`  | The `-t` flag increases the thread count from 10 to 20 and the `--delay 500` flag is decreasing the delay in each thread between requests.  | If I don't care noise on a network or if the machine seems to have sufficient resources because it is quick to handle requests.  |
| `gobuster dir -u http://10.10.1.1 -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt -z --no-color -o ~/gobuster.out`  | The `-z` flag removes the progress bar output while the -o flag tells gobuster to save the output to the gobuster.out file in my home directory.  | I have some automated scripts that will run this command and save the file so that it can be parsed and used with other commands and tools.  |
| `gobuster dir -u http://10.10.1.1 -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt --wordlist-offset $(grep -n 'odbc' /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt \| cut -d':' -f1)`  | The `--wordlist-offset` flag tells gobuster to start on the line number provided (in this case grep finds the line number and returns it).  | I have accidentally stopped gobuster when it was most of the way done. This command allowed me to continue from where I was before I accidentally stopped the script.  |
