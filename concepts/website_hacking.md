# Website Hacking

- [Introduction](#introduction)
- [Forms](#forms)

## Introduction

So many capture the flag events involve looking at a website and trying to find a vulnerability in the site. There are so many moving parts in a website and with how websites are developed, a single page can be composed of components from different teams. A site could also be populated with API calls or a request that gives a new or updated page as the response. No matter how it gets its data, I'll just refer to it as the website.

Since this is a really big topic, I wanted to break it out and talk about the different things that are done when working on a websites.

## Forms

Forms are a natural source of issues for security. Users are able to send data and input to the website and get a response. Sometimes forms can give too much information that can then be used to perform a more informed attack on the website.

Since forms are accepting user input, they need to be aware of the following attacks:

- SQL Injection
- Cross-Site Scripting (XSS)
- Command Injection
- Authentication Bypass
