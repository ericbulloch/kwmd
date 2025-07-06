# Stegseek

## Installation

Stegseek doesn't come installed with Kali Linux. They have [documentation to install](https://github.com/RickdeJager/stegseek?tab=readme-ov-file#wrench-installation) Stegseek.

## Usage

Running `stegseek --help` provided the following output:

```bash
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek


=== StegSeek Help ===
To crack a stegofile:
stegseek [stegofile.jpg] [wordlist.txt]

Commands:
 --crack                 Crack a stego file using a wordlist. This is the default mode.
 --seed                  Crack a stego file by attempting all embedding patterns.
                         This mode can be used to detect a file encoded by steghide.
                         In case the file was encoded without encryption, this mode will
                         even recover the embedded file.
Positional arguments:
 --crack [stegofile.jpg] [wordlist.txt] [output.txt]
 --seed  [stegofile.jpg] [output.txt]

Keyword arguments:
 -sf, --stegofile        select stego file
 -wl, --wordlist         select the wordlist file
 -xf, --extractfile      select file name for extracted data
 -t, --threads           set the number of threads. Defaults to the number of cores.
 -f, --force             overwrite existing files
 -v, --verbose           display detailed information
 -q, --quiet             hide performance metrics (can improve performance)
 -s, --skipdefault       don't add guesses to the wordlist (empty password, filename, ...)
 -n, --nocolor           disable colors in output
 -c, --continue          continue cracking after a result has been found.
                         (A stego file might contain multiple embedded files)
 -a, --accessible        simplify the output to be more screen reader friendly

Use "stegseek --help -v" to include steghide's help.
```

## Examples

The following examples use a file called shady.jpg. This file has a file embedded into it.

Stegseek uses a dictionary to guess the passphrase of an image file that might have a hidden file. The following command uses the rockyou.txt as the word list to guess the passphrase of the shady.jpg file. Here is the command:

```bash
$ stegseek -sf shady.jpg -wl /usr/share/wordlists/rockyou.txt
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "*baseball#1"
[i] Original filename: "secret.txt".
[i] Extracting to "shady.jpg.out".
```
