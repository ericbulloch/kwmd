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


## Best Practices

## Summary
