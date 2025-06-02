# POP3

POP3 email servers are a great way to gather information for a capture the flag event. Once I learned what to type with netcat it became really easy to login, list emails and read emails. I'll also include a way to brute force a password with hydra.

## Connecting

I use netcat to connect to a POP3 service. There are other clients and ways to do this but in a capture the flag event, I need something that is lightweight. I am not always guaranteed to have a GUI so learning a commandline tool like netcat has been very useful.

For this example, my POP3 service is running on port 110 of my server which is located at 10.10.1.1. Here is how I connect to it:

`nc 10.10.1.1 110`

The banner for the email server will show something once you connect. In my case I got the following:

`+OK KWMD Capture the Flag POP3 Electronic-Mail System`

## Log In

Now that I have connected to the POP3 server, I can log into the server. I'll need to send the user command with my username and then the pass command with my password. Since this is on port 110 and not 995, this traffic is in plain text.

Here is my command prompt:

```bash
nc 10.10.1.1 110
+OK KWMD Capture the Flag POP3 Electronic-Mail System
user Gustavo
+OK
pass letmein1!
+OK Logged in.
```

Just like that, I am now in the POP3 server logged in with the Gustavo user.

## Listing Messages for a User

The purpose of logging into the POP3 server with a user is to get the messages so I can read them and try to move onto the next step of the capture the flag. The list command will list all messages. The first number is the id of the email message and the next number is the size of the message. Below is the continuation of the prompt but with the listed messages:

```bash
nc 10.10.1.1 110
+OK KWMD Capture the Flag POP3 Electronic-Mail System
user Gustavo
+OK
pass letmein1!
+OK Logged in.
list
+OK 2 messages:
1 631
2 1048
.
```

I have found 2 messages for the Gustavo user. Next I'll show how to read them.

## Displaying Messages for a User

The retr command is how I retrieve a message from the server so that I can view it. This command needs the id of the message that I got as output in the previous command. Here is a continuation of the prompt above and the message that it contained:

```bash
nc 10.10.1.1 110
+OK KWMD Capture the Flag POP3 Electronic-Mail System
user Gustavo
+OK
pass letmein1!
+OK Logged in.
list
+OK 2 messages:
1 631
2 1048
.
retr 1
+OK 631 octets
Return-Path: <root@ubuntu>
X-Original-To: Gustavo
Delivered-To: Gustavo@ubuntu
Received: from ok (localhost [127.0.0.1])
	by ubuntu (Postfix) with ESMTP id D5EDA454B1
	for <Gustavo>; Tue, 10 Apr 2025 19:45:33 -0700 (PDT)
Message-Id: <20250425024542.DEADBEEF11@ubuntu>
Date: Tue, 10 Apr 2025 19:45:33 -0700 (PDT)
From: them@ubuntu

Gustavo, please you need to stop breaking Rufus' codes. Also, you are AAA supervisor for training. I will email you once a student is designated to you.

Also, be cautious of possible network breaches. We have intel that DoomBlade is being sought after by a crime syndicate named OASIS.
.
```

To read the second message I just need to type the following:

`retr 2`

## Brute Forcing with Hydra

Brute forcing with Hydra follows the same format as other services. POP3 is very slow for authentication. It will take a long time even for a small word list.

### Brute Forcing a Password

I am going to use the gustavo user above to show the syntax to try different passwords. Here is the syntax:

`hydra -l gustavo -P /usr/share/wordlists/fasttrack.txt 10.10.1.1 pop3`

### Brute Forcing a Username

I am going to use the gustavo user above to show the syntax to try different passwords. Here is the syntax:

`hydra -L /usr/share/wordlists/SecLists/Usernames/top-usernames-shortlist.txt -p letmein1! 10.10.1.1 pop3`

## Conclusion

POP3 is very straight forward and once I learned a few commands it became very easy to do what I needed for capture the flag events.
