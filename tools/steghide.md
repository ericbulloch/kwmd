# steghide

The steghide tool allows me to hide files within images and audio files. Capture the flag events use these all the time. I usually find txt and zip files within image files. Those usually contain usernames, passwords or hints for the next steps of the capture the flag.

## Usage

Running `steghide -h` provided the following output:

```bash

steghide version 0.5.1

the first argument must be one of the following:
 embed, --embed          embed data
 extract, --extract      extract data
 info, --info            display information about a cover- or stego-file
   info <filename>       display information about <filename>
 encinfo, --encinfo      display a list of supported encryption algorithms
 version, --version      display version information
 license, --license      display steghide's license
 help, --help            display this usage information

embedding options:
 -ef, --embedfile        select file to be embedded
   -ef <filename>        embed the file <filename>
 -cf, --coverfile        select cover-file
   -cf <filename>        embed into the file <filename>
 -p, --passphrase        specify passphrase
   -p <passphrase>       use <passphrase> to embed data
 -sf, --stegofile        select stego file
   -sf <filename>        write result to <filename> instead of cover-file
 -e, --encryption        select encryption parameters
   -e <a>[<m>]|<m>[<a>]  specify an encryption algorithm and/or mode
   -e none               do not encrypt data before embedding
 -z, --compress          compress data before embedding (default)
   -z <l>                 using level <l> (1 best speed...9 best compression)
 -Z, --dontcompress      do not compress data before embedding
 -K, --nochecksum        do not embed crc32 checksum of embedded data
 -N, --dontembedname     do not embed the name of the original file
 -f, --force             overwrite existing files
 -q, --quiet             suppress information messages
 -v, --verbose           display detailed information

extracting options:
 -sf, --stegofile        select stego file
   -sf <filename>        extract data from <filename>
 -p, --passphrase        specify passphrase
   -p <passphrase>       use <passphrase> to extract data
 -xf, --extractfile      select file name for extracted data
   -xf <filename>        write the extracted data to <filename>
 -f, --force             overwrite existing files
 -q, --quiet             suppress information messages
 -v, --verbose           display detailed information

options for the info command:
 -p, --passphrase        specify passphrase
   -p <passphrase>       use <passphrase> to get info about embedded data

To embed emb.txt in cvr.jpg: steghide embed -cf cvr.jpg -ef emb.txt
To extract embedded data from stg.jpg: steghide extract -sf stg.jpg
```

## Examples

### Extracting Files

As mentioned before, capture the flag events use image and audio files to hide other files. If I had an image file called hello.jpg and I wanted to try and extract a file from it, I would run the following command:

`steghide extract -sf hello.jpg`

After I run this command steghide askes me for a passphrase. I provide one if I have it, otherwise I just press enter for a blank password. If it was successful, it will extract a file. Here is some sample output when I extracted a file called password.txt from my image file hello.jpg and ran the cat command on the password.txt file:

```bash
$ steghide extract -sf hello.jpg
Enter passphrase:
wrote extracted data to "password.txt".
$ cat password.txt
MyPassword: letmein1!
```

Sometimes I don't want to keep that file name that was hidden in the image or audio file. I use the `-xf` option to change the name of the extracted file. Using the above example I can save the password.txt file as not_password.txt when it gets extracted using the following command:

`steghide extract -sf hello.jpg -xf not_password.txt`

This provides the output of:

`wrote extracted data to "not_password.txt".`

### Information from Files

I can try to get information about hidden files using steghide. If it is passphrase protected then I'll need to provide it. Sometimes the information can be useful. Here is how I check for hidden file information:

`steghide info hello.jpg`

Here is some sample output when no hidden files are in the image or when I enter the wrong passphrase:

```bash
$steghide info hello.jpg
"hello.jpg":
  format: jpeg
  capacity: 144.0 Byte
Try to get information about embedded data ? (y/n) y
Enter passphrase:
steghide: could not extract any data with that passphrase!
```

Here is some sample output when it works:

```bash
$steghide info hello.jpg
"hello.jpg":
  format: jpeg
  capacity: 144.0 Byte
Try to get information about embedded data ? (y/n) y
Enter passphrase:
  embedded file "password.txt":
    size 21.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
```
