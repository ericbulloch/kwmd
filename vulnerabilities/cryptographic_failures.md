# Cryptographic Failures

## What are Cryptographic Failures

Cryptographic Failures are when a website or app doesn't keep data safe using encryption - or doesn't use it correctly. When this is done incorrectly or not at all, hackers can steal or see private things such as passwords and credit card information.

In the OWASP Top Ten list for 2021 it is the number two most common vulnerability.

## Common Examples

- Passwords stored in plain text.
- Websites not using HTTPS.
- Using weak encryption like MD5 or SHA1 which is easily cracked using modern GPUs.
- Sharing secret data in URLs.
- Sending passwords in an email.
- Hardcoding cryptographic keys or credentials in source code.
- Using ECB (Electronic Cookbook) mode in block ciphers. This reveals patterns in encrypted data.
- Insecure random number generation. This can be predictable and exploitable.
- Misconfigured TLS, making the site vulnerable to downgrade or man in the middle attacks.
- Weak cipher suites.
- Not enforcing HSTS (HTTP Strict Transport Security).
- Misuse of cryptographic libraries.
- Poor key lifecycle management.
- Insecure storage of sensitive data.
- Using deprecated protocols (TLS 1.0, 1.1, or SSLv3).

## Practice Exploiting Cryptographic Failures

### PortSwigger

PortSwigger has multiple labs to see this vulnerability in action. The labs are online and require an account. Here are some labs:

- [JWT authentication bypass via unverified signature](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-unverified-signature).
- [JWT authentication bypass via flawed signature verification](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-flawed-signature-verification).

### OWASP Juice Shop

The OWASP Juice Shop is an open-source project that is intentionally vulnerable. It has many vulnerabilities and makes finding them a bit of a game using their scoreboard page. It can be accessed with Heroku or using Docker. I ran it using Docker and I seem to recall that one of the vulnerabilities will not work properly if you use Heroku. More information on the project and how to run it can [be found here](https://owasp.org/www-project-juice-shop/).

### TryHackMe

TryHackMe has a couple rooms dedicated to this subject. The rooms are online and require an account. Here are some links to rooms that talk about Cryptographic Failures:

- [Crypto Failures](https://tryhackme.com/room/cryptofailures)
- [OWASP Top 10 - 2021](https://tryhackme.com/room/owasptop102021)
- [Introduction to Cryptography](https://tryhackme.com/room/cryptographyintro)
- [Breaking Crypto the Simple Way](https://tryhackme.com/room/breakingcryptothesimpleway)

## Best Practices

## Summary
