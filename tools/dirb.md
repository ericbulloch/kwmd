# dirb

- [Introduction](#introduction)
- [Usage](#usage)
- [Examples](#examples)

## Introduction

The dirbuster tool is a tool for fuzzing content and subdirectories. Like all fuzzers, the wordlists are the most important part of fuzzing.

## Usage

```bash
$ dirb
-----------------
DIRB v2.22    
By The Dark Raver
-----------------

dirb <url_base> [<wordlist_file(s)>] [options]

========================= NOTES =========================
 <url_base> : Base URL to scan. (Use -resume for session resuming)
 <wordlist_file(s)> : List of wordfiles. (wordfile1,wordfile2,wordfile3...)

======================== HOTKEYS ========================
 'n' -> Go to next directory.
 'q' -> Stop scan. (Saving state for resume)
 'r' -> Remaining scan stats.

======================== OPTIONS ========================
 -a <agent_string> : Specify your custom USER_AGENT.
 -b : Use path as is.
 -c <cookie_string> : Set a cookie for the HTTP request.
 -E <certificate> : path to the client certificate.
 -f : Fine tunning of NOT_FOUND (404) detection.
 -H <header_string> : Add a custom header to the HTTP request.
 -i : Use case-insensitive search.
 -l : Print "Location" header when found.
 -N <nf_code>: Ignore responses with this HTTP code.
 -o <output_file> : Save output to disk.
 -p <proxy[:port]> : Use this proxy. (Default port is 1080)
 -P <proxy_username:proxy_password> : Proxy Authentication.
 -r : Don't search recursively.
 -R : Interactive recursion. (Asks for each directory)
 -S : Silent Mode. Don't show tested words. (For dumb terminals)
 -t : Don't force an ending '/' on URLs.
 -u <username:password> : HTTP Authentication.
 -v : Show also NOT_FOUND pages.
 -w : Don't stop on WARNING messages.
 -X <extensions> / -x <exts_file> : Append each word with this extensions.
 -z <millisecs> : Add a milliseconds delay to not cause excessive Flood.

======================== EXAMPLES =======================
 dirb http://url/directory/ (Simple Test)
 dirb http://url/ -X .html (Test files with '.html' extension)
 dirb http://url/ /usr/share/dirb/wordlists/vulns/apache.txt (Test with apache.txt wordlist)
 dirb https://secure_url/ (Simple Test with SSL)
```

## Examples

The following examples are ones that I have used in capture the flag exercises. The wordlists that are provided are ones that are found on Kali unless otherwise specified.

For each of the examples below, here are the variables that I am using:

- The target machine is found at ip address `10.10.1.1`

### Hotkeys

The dirb tool has a few keys that I can press during a scan. Here are the keys and what they do:

- `q` will stop the scan. It also saves the state of the scan so I can continue if needed.
- `r` will display that show how many words are left to try in this scan.
- `n` stop searching in the current directory. By default dirb searchings directories recursively and when I want it to move on I press this key.

### Directory Enumeration

When I find a web server on a target, this is the first scan that I run.

```bash
$ dirb http://10.10.1.1/
```

This will start the directory scan with the basic wordlist. It will output the results as the scan finds any hidden paths or files.

### Useful Options

I wanted to provide some examples of different options and an example of how to use them.

#### Output File

The `-o` option tells dirb where to save the output in a file. I am going to save the output to the results.txt file using the following command:

```bash
$ dirb http://10.10.1.1/ -o results.txt
```

#### Don't Search Recursively

Once in a while I only want to search the current directory and not anything below it. In that case I run the following:

```bash
$ dirb http://10.10.1.1/ -r
```

#### Basic Authentication

Some Tomcat managers require basic authentication in order to view it and all sub pages. Dirb provides a way to use basic authentication to continue looking at the manager and all sub pages. I would log in with the username owner and password letmein1 with the following command:

```bash
$ dirb http://10.10.1.1/ -u owner:letmein1
```

#### Slowing Down Requests

Some machines in capture the flag events have firewalls to block me when I flood the machine with too many requests. Dirb has a way to show down requests so the firewall doesn't block me. I use the following command to wait 2 seconds (2000 milliseconds) between each request:

```bash
$ dirb http://10.10.1.1/ -z 2000
```
