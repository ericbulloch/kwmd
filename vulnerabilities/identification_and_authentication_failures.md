# Identification and Authentication Failures

## What are Identification and Authentication Failures

This vulnerability refers to failures in verifying a user's identity and session integrity. If the controls that handle identification and authentication are weak, attackers can impersonate users, escalate privileges, hijack a current session, or takeover an account.

Imagine websites like lockers at school. Only people with the right key or combination (like a password) should be able to opent them. If the lock is weak or someone guesses the combo, they can sneak in.

## Common Examples

- Weak passwords – Using 123456 or password makes it easy for someone to break in.
- Login pages don’t block brute force – No rate-limiting or IP throttling on login attempts allows mass automated attacks. You can try guessing the password over and over without being stopped.
- Passwords stored in plain text – If someone hacks the system, they can read everyone's password easily.
- No two-factor authentication (2FA) – Just a password isn't enough to keep accounts safe anymore.
- Logged-in users not verified – A site might forget to check if you're still who you say you are.
- Insecure password reset workflows – Predictable reset tokens or missing expiration allows unauthorized resets.
- Session fixation – Attacker sets a known session ID before login and hijacks it after authentication.
- Improper session termination – Users remain logged in indefinitely, allowing session hijacking on shared devices.
- JWT tampering or misconfigured validation – Accepting unsigned tokens (alg=none) or using symmetric keys incorrectly.
- Exploitable biometric spoofing – Facial recognition or fingerprint systems bypassed with fake data.
- Authentication bypass via SQL injection – admin' OR '1'='1 bypasses login if not sanitized.
- Subdomain takeover via SSO misconfiguration – Attacker gains access by registering a forgotten subdomain tied to authentication.
- Exposed internal APIs with weak auth – Internal endpoints protected by weak or hardcoded credentials.

## Practice Exploiting Identification and Authentication Failures

### PortSwigger

PortSwigger has multiple labs to see this vulnerability in action. The labs are online and require an account. They provide a lot of [background information here](https://portswigger.net/web-security/authentication). Here are some labs:

- [Vulnerabilities in password-based login](https://portswigger.net/web-security/authentication/password-based)
- [Vulnerabilities in multi-factor authentication](https://portswigger.net/web-security/authentication/multi-factor)
- [Vulnerabilities in other authentication mechanisms](https://portswigger.net/web-security/authentication/other-mechanisms)

### OWASP Juice Shop

The OWASP Juice Shop is an open-source project that is intentionally vulnerable. It has many vulnerabilities and makes finding them a bit of a game using their scoreboard page. It can be accessed with Heroku or using Docker. I ran it using Docker and I seem to recall that one of the vulnerabilities will not work properly if you use Heroku. More information on the project and how to run it can [be found here](https://owasp.org/www-project-juice-shop/).

### TryHackMe

TryHackMe has a couple rooms dedicated to this subject. The rooms are online and require an account. Here are some links to rooms that talk about Identification and Authentication Failures:

- [OWASP Top 10 - 2021](https://tryhackme.com/room/owasptop102021)
- [Enumeration & Brute Force](https://tryhackme.com/room/enumerationbruteforce)
- [Identity and Access Management](https://tryhackme.com/room/iaaaidm)
- [Authentication Bypass](https://tryhackme.com/r/room/authenticationbypass)

## Best Practices

| Best Practice | Why It Matters |
| ------------- | -------------- |
| Enforce Strong Password Policies | Prevents easy-to-guess passwords, reducing the risk of unauthorized access. |
| Implement Multi-Factor Authentication (MFA) | Adds an extra layer of security, making it harder for attackers to compromise accounts. |
| Secure Session Management | Protects against session hijacking by ensuring session IDs are unique, unpredictable, and properly invalidated. |
| Limit Failed Login Attempts | Mitigates brute-force and credential stuffing attacks by restricting repeated login attempts. |
| Use Secure Password Storage Techniques | Protects stored passwords using hashing algorithms like bcrypt, preventing attackers from retrieving plaintext passwords. |
| Avoid Exposing Session IDs in URLs | Prevents session fixation and leakage through browser history or logs. |
| Implement CAPTCHA on Login Forms | Deters automated login attempts by requiring human interaction. |
| Regularly Monitor and Audit Authentication Logs | Helps detect suspicious activities and potential breaches in real-time. |
| Educate Users on Phishing and Social Engineering | Reduces the risk of credential compromise through user awareness and training. |
| Utilize Secure Authentication Protocols | Ensures the use of up-to-date and secure protocols (e.g., OAuth 2.0) to manage authentication processes. |

## Summary
