# dirb

The dirbuster tool is a tool for fuzzing content and subdirectories. Like all fuzzers, the wordlists are the most important part of fuzzing.

## Usage

Running `dirb` provided the following output:

```bash
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

### hotkeys

The dirb tool has a few keys that I can press during a scan. Here are the keys and what they do:

- `q` will stop the scan. It also saves the state of the scan so I can continue if needed.
- `r` will display that show how many words are left to try in this scan.

### directory enumeration

When I find a web server on a target, this is the first scan that I run.

`dirb http://10.10.1.1/`

This will start the directory scan with the basic wordlist. It will output the results as the scan finds any hidden paths or files.
