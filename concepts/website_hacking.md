# Website Hacking

- [Introduction](#introduction)
- [Browsing The Site](#browsing-the-site)
- [Inspecting HTML](#inspecting-html)
- [Directory Enumeration](#directory-enumeration)
- [Forms](#forms)

## Introduction

So many capture the flag events involve looking at a website and trying to find a vulnerability in the site. There are so many moving parts in a website and with how websites are developed, a single page can be composed of components from different teams. A site could also be populated with API calls or a request that gives a new or updated page as the response. No matter how it gets its data, I'll just refer to it as the website.

Since this is a really big topic, I wanted to break it out and talk about the different things that are done when working on a capture the flag event with a website. I'll try to give a general approach and then talk about specifics for things that need it.

## Browsing The Site

But seriously, browse the site. It is easier to hack a site if I know how it is suppose to behave. It can help me understand the psycology of what the developers wanted me to experience with the website. I would recommend the following:

- Have a look around.
- Click the links.
- Use the functionality of the site.
- Create a user.
- Capture requests and responses.
- Learn about the processes and flow of the site.

Armed with this information, I can makes better decisions about how to attack the site because I'll understand how it is expected to work. As I document what is on a site and where it is located, I am really documenting all the attack vectors of the site.

## Inspecting HTML

One of the easiest ways to get information in by inspecting the source HTML for a site. Opening up the website and hitting `ctrl + u` will enable me to view the source html for a site. The source code is loaded with all kinds of information. It can provide links, directories, subdomains and comments.

Developers will work on things and then comment them out thinking that people will not see them. This couldn't be further from the truth. This can lead to finding all kinds of sensitive information or view parts of the site that were meant for employees and not the general public. Many capture the flag events have flags and other sensitive information in the comments of the HTML. During these events I have found flags, usernames, passwords, directories and links that my automated tools missed. This is a very overlooked way to find useful things. Here is a sample comment that I found during a capture the flag event:

```text
<!--

  Note from me, to me, remember my login name.

  Username: Sk3l3t0r

-->
```

### Security Measures

Developers need to remove commented out parts of the source code. The risk of what they reveal is not worth it. Also, if a directory or feature is not ready or available for a user it should not allow them to use it. What happens to the user when they try to use one of these items is up to the developer and can be chosen on a case by case basis.

## Directory Enumeration

I almost always run a directory enumeration to see if there are any folders or files that are not directly linked by the website. Directory enumeration can provide very important things like the location of the admin login form, hidden folders that have sensitive data or test pages that run commands directly on the server. Files like `robots.txt` and `sitemap.xml` can also provide useful information.

If the tool finds a directory like `/app`, I will often run a directory enumeration again on that directory to see if there are additional results.

There are a lot of automated tools I can use for directory enumeration. Generally, the word list is the **most important** part. If I get stuck, I use a combination of tools and word lists to see if they find anything different.

The main idea of directory enumeration isn't just to find hidden things. The main point is to find as many things as I can and making notes of them. All of this information is part of the attack surface of the website. The larger the website, the more attack surface it needs to defend.

### Directory Enumeration with gobuster

I now almost exclusively run directory enumeration searches with [gobuster](/tools/gobuster.md). It is very easy to use. I have provided information on how to run gobuster for directory enumeration on [its tool page](/tools/gobuster.md#directoryfile-dir-enumeration-mode).

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

### SQL Injection Example

Because a form accepts user input, it can be vulnerable to SQL Injection. One of the first things I try on a form during a capture the flag event is to capture the request and save it to a file called `request.txt`. Once I have that file, I run the following command:

```bash
$ sqlmap -r request.txt
```

I have more details about this on the [sqlmap tools page](/tools/sqlmap.md).

The sqlmap tool will check the form to see if it is vulnerable to sql injection. If the form is vulnerable, an attacker can can do the following:

- Read sensitive data in the database.
- Get a dump of the database
- Log into the site with elevated privileges.

### Security Measures

Many input issues can be solved by sanitizing user input and making sure what they type is in an approved range of values. For example, if a person needs to enter their name, don't allow them to use numbers and most of the special characters that are on the keyboard. I also want to point out that security measures need to be on both the frontend of the website and the backend. If only the frontend is preventing certain characters but the backend allows them, it is only a matter of time before an attacker will find this out.

### File Upload Forms

File upload forms can provide a foothold for uploading malicious scripts and files. If the form does not properly validate the uploaded file, an attacker can upload scripts that can provide remote code execution or allow a reverse shell. File upload forms are a common place to get a foothold in a capture the flag event.

### Security Measures

There are checks that can be done to help prevent file upload abuse. As mentioned above, do not rely on just the file extension. Here are some things that can be done:

- Have an allowlist of file types (.jpg, .png, .pdf, etc...)
- Validate on the server side with MIME type checks.
- Verify file headers. A list can be found [here](https://en.wikipedia.org/wiki/List_of_file_signatures)
- Rename uploaded file names (i.e. evilscript.jpg → 2a943bff-9034-40cb-9abc-3a95b20a82df.jpg). An attacker now has to get the file name in order to call it.
- Store files in a directory outside the webroot. This way the web server cannot directly access them and run the malicious script.
- If possible, access the files with a proxy script.
- Make sure that the uploaded file can't be executed as code (e.g., not `+x` file permissions).
- Disable script execution on the uploads folder in Apache/Nginx.
- Limit the size of the file being uploaded to prevent denial of service attacks.
