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

| Best Practice | Why It Matters |
| ------------- | -------------- |
| Use HTTPS/TLS for all data in transit | Prevents attackers from intercepting sensitive information (e.g., MITM attacks). |
| Store passwords using strong hashing algorithms (e.g., bcrypt, Argon2) | Protects credentials even if the database is compromised (e.g. very slow algorithms, each entry has a unique salt, etc...). |
| Use modern, secure encryption algorithms (e.g., AES-GCM, RSA with OAEP) | Outdated algorithms like MD5 or RC4 are easily breakable and no longer secure. |
| Enforce strong key management practices | Hardcoded or reused keys can be easily stolen or misused across systems. |
| Avoid rolling your own cryptography | Custom implementations often have flaws; use well-reviewed libraries instead. |
| Verify digital certificates and signatures correctly | Prevents spoofing and ensures integrity of the data or identity. |
| Disable outdated protocols (e.g., SSL, TLS 1.0/1.1) | These protocols have known vulnerabilities and can be exploited for decryption. |
| Use authenticated encryption (e.g., AES-GCM, ChaCha20-Poly1305) | Ensures both confidentiality and authenticity — avoids padding oracle attacks. |
| Do not log sensitive data (e.g., secrets, keys, tokens) | Logs can be accessed or leaked — exposing private data. |
| Enforce secure random number generation (e.g., /dev/urandom, secrets module in Python) | Weak randomness can lead to predictable tokens or keys, undermining security. |

## Summary

Evaluate your data and determine the protection level of data in transit and at rest. Avoid sending data in clear text with protocols like HTTP, SMTP and FTP. If the data falls under privacy laws like GDPR or PCI DSS, make sure their rules are followed. 
