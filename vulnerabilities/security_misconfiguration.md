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

### OWASP Juice Shop

The OWASP Juice Shop is an open-source project that is intentionally vulnerable. It has many vulnerabilities and makes finding them a bit of a game using their scoreboard page. It can be accessed with Heroku or using Docker. I ran it using Docker and I seem to recall that one of the vulnerabilities will not work properly if you use Heroku. More information on the project and how to run it can [be found here](https://owasp.org/www-project-juice-shop/).

### TryHackMe

TryHackMe has a couple rooms dedicated to this subject. The rooms are online and require an account. Here are some links to rooms that talk about Security Misconfiguration:

- [OWASP Top 10 - 2021](https://tryhackme.com/room/owasptop102021)

## Best Practices

| Best Practice | Why It Matters |
| ------------- | -------------- |
| Example | Because |

## Summary
