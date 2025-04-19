| Stat      | Value                                        |
| --------- | -------------------------------------------- |
| Room      | MR-ROBOT: 1                                  |
| URL       | https://www.vulnhub.com/entry/mr-robot-1,151 |
| Difficult | Easy                                         |

## Concepts/Tools Used

- nmap
- Burp Suite
- dirb
- hydra
- netcat
- SUID/GTFOBins
- CrackStation

## Description

This was the first capture the flag challenge that I tried. I have never watched the show Mr. Robot before so most of the references are lost on me. The challenge follows the standard flow of scanning, looking for vulnerabilites and then exploiting them. I was learning what needs to be done while I was doing this capture the flag challenge. I would come up with ideas and run them, once I got stuck I started to watch videos to get ideas on what other people did.

### Process

#### Setup

I imported the virtual machine image into virtual box and booted it up.

#### Port and Service Scan

There is a login screen but I don't have a username or password. I tried admin/admin and root/root but that didn't work.

From here I knew that I needed to get the ip address of the machine so that I could scan it and find out what services were on the machine. When I setup my home lab I limited the ip addresses to the range of 10.22.1.110-130. So I ran the following command to find the machine:

`nmap -sS 10.22.1.110-130`

It provided output for 2 machines. One of the machines was mine (10.22.1.110) so I ignored the output from that machine. The other machine was the target machine. The machine has 3 ports open:

- 22/tcp
- 80/tcp
- 443/tcp

I can use a password to ssh onto the machine since a password prompt showed up when I ran the following command:

`ssh 10.22.1.112`

This lets me know that I can try to brute force login with hydra if I find a username.

#### Website Enumeration

Since I don't have much other information, I opened up Firefox and checked out the website that was running on the target machine.

I viewed the various pages on the website and viewed the page source. I didn't see anything that stood out. None of the links looked particularly promising either.

From here I needed to run some directory enumeration to get more information. I ran the following:

`dirb http://10.22.1.112`

#### First Key

The output mentioned a few things. I started out with the robots.txt file to see what directories are available that they don't want indexed. The output was the following:

```txt
User-agent: *
fsociety.dic
key-1-of-3.txt
```

Nice! I found the first key! I opened that file in Firefox using the following url:

`http://10.22.1.112/key-1-of-3.txt`

#### Provided Word List

Finding the first key file means that the fsociety.dic file is important. I grabbed that file in Firefox using the following url:

`http://10.22.1.112/fsociety.dic`

This file is a giant word list. I downloaded the file and ran the following command on it to see how big it was:

`wc -l fsociety.dic`

The file is over 800k lines. I wanted to see if there were duplicates. I ran the following command:

`uniq fsociety.dic | wc -l`

There are only about 11k unique lines in this file. With that in mind, I saved a copy of the file with just the unique lines using the following command:

`uniq fsociety.dic > test.txt`

#### Admin Login Form

At this point, I have a shorted dictionary list and more things that dirb had in the output. I see that one of the things dirb wanted me to check was the `admin/` path. I'll go there next. The url is:

`http://10.22.1.112/admin`

I went to the page and I am not sure what is happening. It feels like the page is redirecting over and over. I am going to leave this page and check out another directory that dirb wanted me to check. The url is:

`http://10.22.1.112/wp-login.php`

I see a login page and I started to try a few different combinations:

- admin/admin
- admin/password
- admin/123
- admin/1234
- admin/123456

None of these worked. I did notice that the error message doesn't give a generic "your username and password are incorrect" error message. It tells me "Invalid username. Lost your password?". I got the same error message when I tried a few different usernames. If I provide a correct username do I get a different message? So far the only information that I have is the dictionary file that I shortened earlier. I watch the login attempt in the Firefox developer toolbar so I can see the request. Since we have 11k lines in the dictionary file, I don't want to use Burp Suite since it throttles my brute force attempts. I want to use hydra. The command that I used is the following:

`hydra -L test.txt -p admin 10.22.1.112 http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=Invalid username'

Here is a summary of what is happening:
- The `-L` option lets hydra know that I want to use a word list of usernames.
- The `-p` option lets hydra know that I want to use admin as the password.
- 10.22.1.112 is the ip address where hydra is making the request.
- Hydra is making a http-post-form request. This is the request that is made when we type a username and password at the admin login page in Firefox.
- The http-post-form uses a string as input. It has 3 parts that are separated by the colon (:) character.
- The path of the request: `/wp-login.php`.
- The form data. In our case we have 3 items. The ^USER^ variable will be populated by the word list mentioned above. The ^PASS^ variable will be admin. The wp-submit variable will be Log+In.
- Finally, the `F=Invalid username` part tells hydra that a failed request will have the string "Invalid username" in the response.

After running the command I got a valid username:

`Elliot`
