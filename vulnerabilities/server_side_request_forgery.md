# Server-Side Request Forgery

## What is Server-Side Request Forgery

Imagine you ask your friend (a website) to go grab something (data) for you from a store (another website). If your friend isn’t careful, you might trick them into going somewhere dangerous, like a restricted area. SSRF is when a hacker tricks a website into making requests to places it shouldn't.

SSRF occurs when an attacker can make a vulnerable server issue HTTP or other protocol requests on its behalf. It typically results from poorly validated user input used in outbound requests. This is dangerous because internal services (like metadata APIs, admin consoles, or internal APIs) are often not protected from internal access. This can  potentially lead to sensitive data exposure or lateral movement within internal networks.

Modern risks include cloud metadata theft, internal pivoting, service discovery, and chaining with other exploits like RCE or privilege escalation.

## Common Examples

## Practice Exploiting Server-Side Request Forgery

### PortSwigger

PortSwigger has multiple labs to see this vulnerability in action. The labs are online and require an account. Here are some labs:

### OWASP Juice Shop

The OWASP Juice Shop is an open-source project that is intentionally vulnerable. It has many vulnerabilities and makes finding them a bit of a game using their scoreboard page. It can be accessed with Heroku or using Docker. I ran it using Docker and I seem to recall that one of the vulnerabilities will not work properly if you use Heroku. More information on the project and how to run it can [be found here](https://owasp.org/www-project-juice-shop/).

### TryHackMe

TryHackMe has a couple rooms dedicated to this subject. The rooms are online and require an account. Here are some links to rooms that talk about Server-Side Request Forgery:

- [OWASP Top 10 - 2021](https://tryhackme.com/room/owasptop102021)

## Best Practices

| Best Practice | Why It Matters |
| ------------- | -------------- |
| Example | Because |

## Summary
