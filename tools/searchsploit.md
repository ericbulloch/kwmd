# searchsploit

The searchsploit tool is a useful commandline database that allows me to look up a vulnerabilities in the [Exploit Database](https://www.exploit-db.com/searchsploit) based on the name and version of software. This information provides a list of known vulnerabilites and scripts that can be used to run against target machines. Once I install searchsploit on my machine I can look up vulnerabilites without using an internet connection.

## Usage

Running `searchsploit -h` provided the following output:

```bash
  Usage: searchsploit [options] term1 [term2] ... [termN]

==========
 Examples 
==========
  searchsploit afd windows local
  searchsploit -t oracle windows
  searchsploit -p 39446
  searchsploit linux kernel 3.2 --exclude="(PoC)|/dos/"
  searchsploit -s Apache Struts 2.0.0
  searchsploit linux reverse password
  searchsploit -j 55555 | jq
  searchsploit --cve 2021-44228

  For more examples, see the manual: https://www.exploit-db.com/searchsploit

=========
 Options 
=========
## Search Terms
   -c, --case     [term]      Perform a case-sensitive search (Default is inSEnsITiVe)
   -e, --exact    [term]      Perform an EXACT & order match on exploit title (Default is an AND match on each term) [Implies "-t"]
                                e.g. "WordPress 4.1" would not be detect "WordPress Core 4.1")
   -s, --strict               Perform a strict search, so input values must exist, disabling fuzzy search for version range
                                e.g. "1.1" would not be detected in "1.0 < 1.3")
   -t, --title    [term]      Search JUST the exploit title (Default is title AND the file's path)
       --exclude="term"       Remove values from results. By using "|" to separate, you can chain multiple values
                                e.g. --exclude="term1|term2|term3"
       --cve      [CVE]       Search for Common Vulnerabilities and Exposures (CVE) value

## Output
   -j, --json     [term]      Show result in JSON format
   -o, --overflow [term]      Exploit titles are allowed to overflow their columns
   -p, --path     [EDB-ID]    Show the full path to an exploit (and also copies the path to the clipboard if possible)
   -v, --verbose              Display more information in output
   -w, --www      [term]      Show URLs to Exploit-DB.com rather than the local path
       --id                   Display the EDB-ID value rather than local path
       --disable-colour       Disable colour highlighting in search results

## Non-Searching
   -m, --mirror   [EDB-ID]    Mirror (aka copies) an exploit to the current working directory
   -x, --examine  [EDB-ID]    Examine (aka opens) the exploit using $PAGER

## Non-Searching
   -h, --help                 Show this help screen
   -u, --update               Check for and install any exploitdb package updates (brew, deb & git)

## Automation
       --nmap     [file.xml]  Checks all results in Nmap's XML output with service version
                                e.g.: nmap [host] -sV -oX file.xml

=======
 Notes 
=======
 * You can use any number of search terms
 * By default, search terms are not case-sensitive, ordering is irrelevant, and will search between version ranges
   * Use '-c' if you wish to reduce results by case-sensitive searching
   * And/Or '-e' if you wish to filter results by using an exact match
   * And/Or '-s' if you wish to look for an exact version match
 * Use '-t' to exclude the file's path to filter the search results
   * Remove false positives (especially when searching using numbers - i.e. versions)
 * When using '--nmap', adding '-v' (verbose), it will search for even more combinations
 * When updating or displaying help, search terms will be ignored
```

## Examples

The following examples are ones that I have used in capture the flag exercises.

### Searching

I found a web application that was running the "Online Book Store v1.0" software. Using searchsploit I was able to find all kinds of vulnerabilities. Here is the command I ran to find what exploits were available:

`searchsploit Online Book Store`

The following was the output:

```bash
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                                                   |  Path
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
GotoCode Online Bookstore - Multiple Vulnerabilities                                                                                                                             | asp/webapps/17921.txt
Online Book Store 1.0 - 'bookisbn' SQL Injection                                                                                                                                 | php/webapps/47922.txt
Online Book Store 1.0 - 'id' SQL Injection                                                                                                                                       | php/webapps/48775.txt
Online Book Store 1.0 - Arbitrary File Upload                                                                                                                                    | php/webapps/47928.txt
Online Book Store 1.0 - Unauthenticated Remote Code Execution                                                                                                                    | php/webapps/47887.py
Online Event Booking and Reservation System 1.0 - 'reason' Stored Cross-Site Scripting (XSS)                                                                                     | php/webapps/50450.txt
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

The `Online Book Store 1.0 - Unauthenticated Remote Code Execution` line caught my eye. Looking in the Path column of the table, I see that `php/webapps/47887.py` is the file to run this exploit. I was to see more information about this exploit. I'll run the following command to get more information:

`searchsploit 47887 -p`

It output the following:

```bash
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                                                   |  Path
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Online Book Store 1.0 - Unauthenticated Remote Code Execution                                                                                                                    | php/webapps/47887.py
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
root@ip-10-10-92-190:~/Instructions# searchsploit 47887 -p
  Exploit: Online Book Store 1.0 - Unauthenticated Remote Code Execution
      URL: https://www.exploit-db.com/exploits/47887
     Path: /opt/exploitdb/exploits/php/webapps/47887.py
    Codes: N/A
 Verified: True
File Type: ASCII text
```
