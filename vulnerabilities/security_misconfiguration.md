# Security Misconfiguration

## What is Security Misconfiguration

Security Misconfiguration is when systems, frameworks or servers are deployed with insecure settings. This can also include cases when unnecessary services are enabled, giving attackers room to exploit flaws. It is caused by overlooked defaults, missing hardening steps or improper permissions.

## Common Examples

- Default passwords left on (like "admin:admin")
- Directory listings turned on—anyone can browse your files
- Settings open to everyone instead of just users/admins
- Unpatched systems exposing known CVEs due to lax update policies
- Verbose error messages revealing stack traces or backend tech
- Public S3 buckets or unsecured cloud storage
- Debug mode enabled in production environments
- Over-permissive CORS configurations, allowing arbitrary sites to access sensitive APIs
- Exposed admin panels (e.g., /phpmyadmin, Jenkins, or Grafana) without auth or protected by weak creds
- Kubernetes dashboards exposed with cluster-admin roles and no RBAC
- HTTP methods misconfigured—allowing PUT/DELETE where they shouldn’t be (leads to web shell uploads)
- Misconfigured CSP headers allowing XSS via whitelisted wildcard domains
- CI/CD pipelines exposing secrets in environment variables or build logs

## Practice Exploiting Security Misconfiguration

### PortSwigger

PortSwigger has multiple labs to see this vulnerability in action. The labs are online and require an account. Here are some labs:

- [Using Burp to Test for Security Misconfiguration Issues](https://portswigger.net/support/using-burp-to-test-for-security-misconfiguration-issues)
- [Lab: Authentication bypass via information disclosure](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-authentication-bypass)
- [Lab: CORS vulnerability with trusted insecure protocols](https://portswigger.net/web-security/cors/lab-breaking-https-attack)

### OWASP Juice Shop

The OWASP Juice Shop is an open-source project that is intentionally vulnerable. It has many vulnerabilities and makes finding them a bit of a game using their scoreboard page. It can be accessed with Heroku or using Docker. I ran it using Docker and I seem to recall that one of the vulnerabilities will not work properly if you use Heroku. More information on the project and how to run it can [be found here](https://owasp.org/www-project-juice-shop/).

### TryHackMe

TryHackMe has a couple rooms dedicated to this subject. The rooms are online and require an account. Here are some links to rooms that talk about Security Misconfiguration:

- [OWASP Top 10 - 2021](https://tryhackme.com/room/owasptop102021)

## Best Practices

| Best Practice | Why It Matters |
| ------------- | -------------- |
| Disable default/admin features in production | Prevents attackers from using built-in test tools or debug consoles. |
| Remove directory listings | Avoid exposing file structures that reveal sensitive components. |
| Turn off verbose error/debug modes | Prevents leaking internal paths, stack traces, and config details. |
| Apply vendor hardening guides & patch regularly | Ensures servers and services are secure, reducing attack surface. |
| Set secure HTTP headers (HSTS, CSP, CORS) | Blocks client-side attacks enabled by misconfigured headers . |
| Restrict unnecessary services/ports | Reduces the number of potential entry points for attackers. |
| Enforce principle of least privilege | Limits damage if a component gets compromised. |
| Secure cloud configurations (e.g., AWS S3/VPC) | Misconfigured cloud services are a top cause of breaches. |
| Regularly audit and review configurations | Detects drift, forgotten test environments, or insecure defaults. |
| Ensure sensitive endpoints require authentication | Prevents exposures of admin or debug interfaces. |

## Summary

Systems, frameworks or servers that have been deployed need to have their settings hardened. Default credentials need to be changed. Error messages need to be examined to make sure they don't reveal too much information. Software with known CVEs (common vulnerabilities and exposures) need to be patched to limit the attack surface. The settings for an application need to follow the principle of least privilege. Software in production should not have debug settings since it can reveal too much information.
