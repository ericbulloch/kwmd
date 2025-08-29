# Website Hacking

- [Introduction](#introduction)
- [Directory Enumeration](#directory-enumeration)
- [Forms](#forms)

## Introduction

So many capture the flag events involve looking at a website and trying to find a vulnerability in the site. There are so many moving parts in a website and with how websites are developed, a single page can be composed of components from different teams. A site could also be populated with API calls or a request that gives a new or updated page as the response. No matter how it gets its data, I'll just refer to it as the website.

Since this is a really big topic, I wanted to break it out and talk about the different things that are done when working on a capture the flag event with a website. I'll try to give a general approach and then talk about specifics for things that need it.

## Inspecting HTML

One of the easiest ways to get information in by inspecting the source HTML for a site. Opening up the website and hitting `ctrl + u` will enable you to view the source html for a site. The source code is loaded with all kinds of information. It can provide links, directories, subdomains and comments.

Developers will work on things and then comment them out thinking that people will not see them. This couldn't be further from the truth. This can lead to finding all kinds of sensitive information or view parts of the site that were meant for employees and not the general public. Many capture the flag events have flags and other sensitive information in the comments of the HTML. During these events I have found flags, usernames, passwords, directories and links that my automated tools missed. This is a very overlooked way to find useful things. Here is a sample comment that I found during a capture the flag event:

```text
<!--

  Note from me, to me, remember my login name.

  Username: Sk3l3t0r

-->
```

## Directory Enumeration

I almost always run a directory enumeration to see if there are any folders or files that are not directly linked by the website. Directory enumeration can provide very important things like the location of the admin login form, hidden folders that have sensitive data or test pages that run commands directly on the server. Files like `robots.txt` and `sitemap.xml` can also provide useful information.

If the tool finds a directory like `/app`, I will often run a directory enumeration again on that directory to see if there are additional results.

There are a lot of automated tools I can use for directory enumeration. Generally, the word list is the **most important** part. If I get stuck, I use a combination of tools and word lists to see if they find anything different. Here are some tools I like to use and some sample usage:

### Directory Enumeration with gobuster

I now almost exclusively run directory enumeration searches with [gobuster](/tools/gobuster.md). It is very easy to use. I have provided information on how to run gobuster for directory enumeration on [its tool page](tools/gobuster.md#directoryfile-dir-enumeration-mode).

### Security Measures

Here are some things that can be done to slow down or even prevent directory enumeration on a website:

- Limiting how many requests an ip address can make per second.
- Disable directory listing on the web server so that it does not list the contents of directories without an index file.
- Monitoring requests for enumeration behavior (common wordlist patterns, repeated 404 status codes, suspicious user agents).
- Using a web applicatin firewall to detect and block enumeration patterns.
- Obfuscate sensitive paths that are found in wordlists like /admin, /backup and /test.
- Remove unused files and directories (beware of things like .git, .env, .bak, .old, debug.php, etc...).
- Use a custom 404 page that avoids revealing information in error messages and provide generic responses that don't confirm the existance of a path.

## Forms

Forms are a natural source of issues for security. Users are able to send data and input to the website and get a response. Sometimes forms can give too much information that can then be used to perform a more informed attack on the website. Many times, developers lack the imagination or understanding of what attackers will throw at a form.

Since forms are accepting user input, some of the attacks they need to be aware of are the following:

- SQL Injection
- Cross-Site Scripting (XSS)
- Command Injection
- Authentication Bypass

### Security Measures

Many input issues can be solved by sanitizing user input and making sure what they type is in an approved range of values. For example, if a person needs to enter their name, don't allow them to use numbers and most of the special characters that are on the keyboard. I also want to point out that security measures need to be on both the frontend of the website and the backend. If only the frontend is preventing certain characters but the backend allows them, it is only a matter of time before an attacker will find this out.
