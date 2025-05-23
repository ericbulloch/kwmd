# Broken Access Control

## What is Broken Access Control

Broken Access Control is when a website or app lets people do things they shouldn't be allowed to do. It refers to flaws in how a system enforces what users are allowed to do. This includes missing or improperly implemented authorization checks. It allows unauthorized users to access data or perform actions outside of their intended permissions.

In the OWASP Top Ten list for 2021 it is the number one most common vulnerability. The OWASP Top Ten site says the following:

> 94% of applications were tested for some form of broken access control. The 34 Common Weakness Enumerations (CWEs) mapped to Broken Access Control had more occurrences in applications than any other category.

Most applications implement some form of authentication but forget to implement or enforce proper authorization logic — especially on sensitive endpoints, API routes, and across microservices.

## Common Examples

- You're only supposed to see your own grades in a school portal. But there's a bug that lets you type in a different student's ID and see their grades too.
- Editing another student’s homework even though you’re not the teacher.
- Deleting files that aren’t yours.
- Accessing admin pages without logging in as an admin.
- Unlocking premium features without paying, just by changing part of the app’s request.
- Changing /api/order/1001 to /api/order/1002 and accessing another user’s order. This is called an IDOR (Insecure Direct Object References)
- A regular user manually accesses /admin/dashboard and gains admin access due to missing role checks.
- A user can view or edit other users' data because the app only checks authentication, not ownership.
- A user performs admin functions like user deletion because role-based access is not enforced.
- APIs return sensitive data even though the user has no permission to access it (especially in SPAs or mobile apps).
- A user of one organization accesses data from another org (e.g., SaaS apps leaking tenant data due to poorly scoped resource access).
- An attacker sends extra fields (like isAdmin=true) during a profile update to elevate privileges.
- Front-end hides the delete route in an API (i.e. DELETE /user/123), but it’s still available and executable via tools like Burp Suite or curl.
- Navigating to unlinked admin or restricted resources that are not protected by access controls (/internal/reports/export.csv).
- Especially in REST/GraphQL APIs, users can manipulate identifiers (user IDs, object IDs) and access or modify resources they don’t own.

## Practice Exploiting the Vulnerability

### PortSwigger

PortSwigger has multiple labs to see this vulnerability in action. The labs are online and require an account. A list of the labs can [be found here](https://portswigger.net/web-security/all-labs#access-control-vulnerabilities).

### OWASP Juice Shop

The OWASP Juice Shop is an open-source project that is intentionally vulnerable. It has many vulnerabilities and makes finding them a bit of a game using their scoreboard page. It can be accessed with Heroku or using Docker. I ran it using Docker and I seem to recall that one of the vulnerabilities will not work properly if you use Heroku. More information on the project and how to run it can [be found here](https://owasp.org/www-project-juice-shop/).

### TryHackMe

TryHackMe has a couple rooms dedicated to this subject. The rooms are online and require an account. Here are some links to rooms that talk about Broken Access Control:

- [OWASP Broken Access Control](https://tryhackme.com/room/owaspbrokenaccesscontrol)
- [OWASP Top 10 - 2021](https://tryhackme.com/room/owasptop102021)

## Best Practices

| Best Practice | Why It Matters |
| ------------- | -------------- |
| Always do access checks on the server | Client-side checks can be bypassed |
| Implement role-based access control (RBAC) | Users should only see/do what their role allows |
| Use indirect object references (e.g., UUIDs or tokens) | Hides internal resource structure |
| Test access at every entry point (API, UI, CLI) | Hackers don't only go through the UI |
| Log and alert on access control violations | Helps detect malicious probing |

## Summary

In short, Broken Access Control vulnerabilities exist because a system doesn't check if a user has permission to perform an action. The server should always check if the user has permission to perform the action. Whether a user is trying to access a resource or perform an action, the system should check if a user is authenticated and authorized to continue. Broken Access Control vulnerabilities are so prevelent because authentication and authorization checks, while not hard to implement, are easy to forget or miss. They rely on humans to initially set for resources and endpoints and humans are the weakest part of security.
