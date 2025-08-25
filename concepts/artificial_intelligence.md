# Artificial Intelligence

## Introduction

I must talk about artificial intelligence as a tool. I will not go into large language models or deep learning. I think that other references can do a much better job with that than I can. I want to discuss what artificial intelligence can be used for with regards to cyber security and how to learn. I currently view it as a tool and nothing more. I don't believe the people out there that think it will remove jobs. I merely see it as something that will make you faster at your job.

## Learning Cyber Security

I have been utilizing AI in a number of ways as I have been learning cyber security. It has helped me learn concepts faster and provided feedback on ways that I can improve. What I like the most about the tool is that it is available when I need it.

I have used it to do the following:

- Explain broad cyber security concepts. This helps with understanding general ideas and then focusing on parts that are unfamiliar, unclear or new. This helps to personalize learning.
- Analyze results from tools to help show me what the output means. Each tool outputs things in different ways and having a tool that can provide feedback about the output has been very valuable for learning.
- Getting a different perspective. I am like any other person and I miss things. AI has been useful when I provide it with output from scans and my own analysis on the output regarding what steps I have done. AI has given me additional considerations that might yield good results. I don't know what I don't know and AI can show me areas that are a blind spot for me.
- A quiz game where the AI will generate a scenario that has an objective and provide me with clues within that scenario. I read the clues and try to pick what moves I should make next. The AI reviews what I decided and then it will let me know what I did right and what other things I should consider. I talk more about this in the quiz game section below.
- Generate scripts with vulnerabilities. I have used an AI to generate blocks of code that are vulnerable to attacks. This has been extremely beneficial to see both the red and blue side of cyber security.
- Explain malicious payloads. Sometimes the payloads can be a lot to take in and AI can break down the different parts very easily. If something is still unclear to me, I can have it further explain concepts so that I can more easily form connections between concepts.

### Quiz Game

As I have learned more and more about cyber security, I have come to realize the parts that I need to improve on. For example, I feel that I could be better at privilege escalation in Linux systems. This is something that I normally practice near the end of a capture the flag box in TryHackMe. So normally I have to compromise a web application and get a foothold on a server with remote code execution or a reverse shell. That can take a fair amount of time. I wanted to practice Linux privilege escalation without having to get to remote code execution or a reverse shell on a machine before I started.

This is where AI came into play. I expained to AI that I wanted to learn about privilege escalation and I wanted it to provide me with clues. I would then look at the clues and say what I think the next step is to obtain privilege escalation. AI would then look at my response and analyze both my answer and the logic I gave for going in that direction. AI would then provide feedback to let me know if I was on the right track, if I had the correct analysis or if I was way off. It provides feedback about what other kinds of things to look for and where I can improve.

Here is the prompt that I use

```text
I want to get better at Linux privilege escalation.
I need you to provide me with a scenario and some clues.
I will review the clues and then tell you what I think the right path is to get escalated privileges.
I'll need you to then take my answer and consider it with other possible solutions to tell me how good the solution is.

I want you to provide the strengths of my solution along with alternate paths and real world considerations.
Bonus tips are always welcome.
```

This caused the AI to out the following:

```text
🧪 Scenario #1: "The Misconfigured Utility"
You're logged in as a low-privilege user kwmd on a Debian-based system.

🔍 Evidence

$ whoami
kwmd

$ sudo -l
Matching Defaults entries for kwmd on vulnbox:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

User kwmd may run the following commands on vulnbox:
    (ALL) NOPASSWD: /usr/bin/vim


$ ls -l /usr/bin/vim
-rwxr-xr-x 1 root root 2.1M Jan 10 2024 /usr/bin/vim


$ id
uid=1001(kwmd) gid=1001(kwmd) groups=1001(kwmd)

🎯 Your Task
Based on this evidence, what would you do to escalate privileges to root?

Once you respond, I’ll evaluate your answer and compare it to known techniques. Ready when you are!
```

From here I mentioned that vim can execute shell commands and I explained how I would start vim and then execute a shell.

The AI said that answer was correct but I could also start a shell with the following command:

```bash
$ vim -c ':!/bin/bash'
```

It also provided some real world considerations like the following:

```text
- Some hardened systems may restrict shell escapes in vim.
- Always verify the actual behavior in a live environment — some distros alias vim to vi, which may behave differently.
```

I run through scenarios like this all the time with AI to keep practicing.

### Generating Scripts

There are a lot of times where AI generating scripts is the right call. In general, it does a good job generating small scripts. I have a high level of confidence with AI when the problem is small and focused.

For a while I used the following prompt:

```text
I will ask you to generate scripts from time to time. I need them to run using python 3. I would prefer (not required) that the script doesn't have any external packages dependencies. If I mention parameters I will tell you the name of the parameter and type. I want those arguments to get parsed by argparse.
```

I know that stating python 3 is strange when python 2 support ended years ago. I have found many scripts and proof of concepts online that still use python 2. I want the AI to not question which version of python is the correct one.

I mention that I don't favor external packages because AI will generally not put a comment in the script regarding what version number the package is using. Down the line this can be frustrating when I try to run my old scripts. Either I have to include a `requirements.txt` file or add a comment in the script. Doing as with vanilla python prevents both of those headaches.

## What I Don't Use It For

What you are not is just as important as what you are! I wanted to note a few things that I have not used AI for. I am not the guy that run all things through AI, I want to ask it specific questions because it currently does not do well understanding an entire process or a complete system. It is amazing at providing insights and analysis about parts of a system, but it struggles to explain the complex relationship between parts.

### Writing This Repository

The notes that I take for this repository are written by me. I do run it through AI from time to time to get feedback on writing style and other things. While I think that AI is very good at writing many things, the goal of this repository is to make my notes and talk about things that I have learned. If AI were to write this repository, I would have failed in what I was trying to do.

### Writing Commands

This might seem crazy to people but I am rarely have AI generate a command for me. I do have a list of commands in this repository that I regularly run that probably could be automated in some fashion. However, my goal is to learn and understand. I write out most of my commands to learn what the various switches and options do. I find that I am getting more comfortable with the tools and that I am able to quickly fix an issue if something goes wrong. I do from time to time, run commands through AI to ask if it is correct. I will also ask it for other considerations that I may have missed.

### Writing All Code

I have been a software developer for 15+ years. I enjoy it a lot and I also enjoy the challenge of solving some of the problems with code. There are some things that I like to write and there are things that I will ask the AI to write for me. My machine has a large collection of scripts that I have accumulated over the years that have worked out really well. For those reasons, I don't have AI write all the code.
