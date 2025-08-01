# nikto

The nikto tool is used as a vulnerability scanner for web servers. It tries to identify outdated software, dangerous files and misconfigurations. It can be very useful for finding ways that a server can be exploited.

## TryHackMe Attack Box

The version of nikto on the TryHackMe attack box is older. I have found that I get better results when I use a newer version of the tool. I have been cloning the [repository from GitHub](https://github.com/sullo/nikto) and following there instructions on the main README to run the latest version. The latest version gives better hints and tips out of the box. I strongly recommend using it over the one that comes preinstalled with the attack box.

## Usage

```bash
$ nikto -Help
   Options:
       -ask+               Whether to ask about submitting updates
                               yes   Ask about each (default)
                               no    Don't ask, don't send
                               auto  Don't ask, just send
       -Cgidirs+           Scan these CGI dirs: "none", "all", or values like "/cgi/ /cgi-a/"
       -config+            Use this config file
       -Display+           Turn on/off display outputs:
                               1     Show redirects
                               2     Show cookies received
                               3     Show all 200/OK responses
                               4     Show URLs which require authentication
                               D     Debug output
                               E     Display all HTTP errors
                               P     Print progress to STDOUT
                               S     Scrub output of IPs and hostnames
                               V     Verbose output
       -dbcheck           Check database and other key files for syntax errors
       -evasion+          Encoding technique:
                               1     Random URI encoding (non-UTF8)
                               2     Directory self-reference (/./)
                               3     Premature URL ending
                               4     Prepend long random string
                               5     Fake parameter
                               6     TAB as request spacer
                               7     Change the case of the URL
                               8     Use Windows directory separator (\)
                               A     Use a carriage return (0x0d) as a request spacer
                               B     Use binary value 0x0b as a request spacer
        -Format+           Save file (-o) format:
                               csv   Comma-separated-value
                               htm   HTML Format
                               msf+  Log to Metasploit
                               nbe   Nessus NBE format
                               txt   Plain text
                               xml   XML Format
                               (if not specified the format will be taken from the file extension passed to -output)
       -Help              Extended help information
       -host+             Target host
       -IgnoreCode        Ignore Codes--treat as negative responses
       -id+               Host authentication to use, format is id:pass or id:pass:realm
       -key+              Client certificate key file
       -list-plugins      List all available plugins, perform no testing
       -maxtime+          Maximum testing time per host
       -mutate+           Guess additional file names:
                               1     Test all files with all root directories
                               2     Guess for password file names
                               3     Enumerate user names via Apache (/~user type requests)
                               4     Enumerate user names via cgiwrap (/cgi-bin/cgiwrap/~user type requests)
                               5     Attempt to brute force sub-domain names, assume that the host name is the parent domain
                               6     Attempt to guess directory names from the supplied dictionary file
       -mutate-options    Provide information for mutates
       -nointeractive     Disables interactive features
       -nolookup          Disables DNS lookups
       -nossl             Disables the use of SSL
       -no404             Disables nikto attempting to guess a 404 page
       -output+           Write output to this file ('.' for auto-name)
       -Pause+            Pause between tests (seconds, integer or float)
       -Plugins+          List of plugins to run (default: ALL)
       -port+             Port to use (default 80)
       -RSAcert+          Client certificate file
       -root+             Prepend root value to all requests, format is /directory
       -Save              Save positive responses to this directory ('.' for auto-name)
       -ssl               Force ssl mode on port
       -Tuning+           Scan tuning:
                               1     Interesting File / Seen in logs
                               2     Misconfiguration / Default File
                               3     Information Disclosure
                               4     Injection (XSS/Script/HTML)
                               5     Remote File Retrieval - Inside Web Root
                               6     Denial of Service
                               7     Remote File Retrieval - Server Wide
                               8     Command Execution / Remote Shell
                               9     SQL Injection
                               0     File Upload
                               a     Authentication Bypass
                               b     Software Identification
                               c     Remote Source Inclusion
                               x     Reverse Tuning Options (i.e., include all except specified)
       -timeout+          Timeout for requests (default 10 seconds)
       -Userdbs           Load only user databases, not the standard databases
                               all   Disable standard dbs and load only user dbs
                               tests Disable only db_tests and load udb_tests
       -until             Run until the specified time or duration
       -update            Update databases and plugins from CIRT.net
       -useproxy          Use the proxy defined in nikto.conf
       -Version           Print plugin and database versions
       -vhost+            Virtual host (for Host header)
   		+ requires a value
```

## Examples

### Standard examples

Nikto can be used to run against a web server all it needs is a host name. I run the following command to check for vulnerabilities:

```bash
$ nikto -h http://target.thm
```

The `-h` option lets nikto know what host I want it to check on. This will always default to port 80 since I specified http in the protocol. I wanted to check a different port, I just add it in the host name. So if I wanted to check port 1234, I would modify the command to the following:

```bash
$ nikto -h http://target.thm:1234
```

Checking https traffic on the standard port 443 just needs a protocol change:

```bash
$ nikto -h https://target.thm
```

### Using Basic Authentication

Sometimes the web server will use Basic Authentication to block my scans. If I know what the username and password are I can provide them to nikto so that it can continue to scan. The credentials are provided using the `-id` option. I would provide the username mike and the password letmein1 in the original example like so:

```bash
$ nikto -h http://target.thm -id mike:letmein1
```

Now nikto can log in to the site and continue to run scans on protected pages. A lot of software information and configuration files are hidden behind pages that need credentials. This will help getting past pages that are using Basic Authentication.
