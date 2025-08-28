# Website Hacking

- [Introduction](#introduction)
- [Forms](#forms)

## Introduction

So many capture the flag events involve looking at a website and trying to find a vulnerability in the site. There are so many moving parts in a website and with how websites are developed, a single page can be composed of components from different teams. A site could also be populated with API calls or a request that gives a new or updated page as the response. No matter how it gets its data, I'll just refer to it as the website.

Since this is a really big topic, I wanted to break it out and talk about the different things that are done when working on a capture the flag event with a website. I'll try to give a general approach and then talk about specifics for things that need it.

## Forms

Forms are a natural source of issues for security. Users are able to send data and input to the website and get a response. Sometimes forms can give too much information that can then be used to perform a more informed attack on the website. Many times, developers lack the imagination or understanding of what attackers will throw at a form.

Since forms are accepting user input, some of the attacks they need to be aware of are the following:

- SQL Injection
- Cross-Site Scripting (XSS)
- Command Injection
- Authentication Bypass

### Security Measures

Many input issues can be solved by sanitizing user input and making sure what they type is in an approved range of values. For example, if a person needs to enter their name, don't allow them to use numbers and most of the special characters that are on the keyboard. I also want to point out that security measures need to be on both the frontend of the website and the backend. If only the frontend is preventing certain characters but the backend allows them, it is only a matter of time before an attacker will find this out.
