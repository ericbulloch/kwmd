# Security Logging and Monitoring Failures

## What are Security Logging and Monitoring Failures

Security logging and monitoring failures happen when a system doesn’t properly keep track of what’s going on, such as who logs in, what they do, or if something bad is happening. If the system can’t detect these things, it might not know it’s being attacked.

Systems should have proper event logging, alerting, or log retention. This limits the organization’s ability to detect suspicious activity, trace incidents, or respond quickly to attacks. At an advanced level, this refers to insufficient telemetry, poorly configured audit trails, or lack of automated threat detection. The failure isn’t just not logging, but also not analyzing, alerting, or protecting the logs themselves. These gaps make incident response, threat hunting, and compliance unreliable.

## Common Examples

- No logs when someone logs in or out.
- Alert thresholds are poorly configured (e.g., 1000 failed logins trigger no alert).
- Critical application actions (e.g., password changes, permission updates) are not auditable.
- System crashes, but no error is recorded.
- No way to know if a hacker broke in last week.
- Lack of centralized log aggregation or SIEM integration.
- Logs are overwritten or deleted due to insufficient retention policies.
- Missing end-to-end request tracing in distributed microservices.
- No audit logging of privilege escalation or RBAC changes in cloud environments.
- Logs stored in plaintext without integrity protection or access control.
- Lack of anomaly detection for rare-but-high-impact behaviors (e.g., logins from foreign IPs).
- Failure to alert on lateral movement in internal networks detected by IDS logs.

## Practice Exploiting Security Logging and Monitoring Failures

### PortSwigger

PortSwigger has multiple labs to see this vulnerability in action. The labs are online and require an account. Here are some labs:

### OWASP Juice Shop

The OWASP Juice Shop is an open-source project that is intentionally vulnerable. It has many vulnerabilities and makes finding them a bit of a game using their scoreboard page. It can be accessed with Heroku or using Docker. I ran it using Docker and I seem to recall that one of the vulnerabilities will not work properly if you use Heroku. More information on the project and how to run it can [be found here](https://owasp.org/www-project-juice-shop/).

### TryHackMe

TryHackMe has a couple rooms dedicated to this subject. The rooms are online and require an account. Here are some links to rooms that talk about Security Logging and Monitoring Failures:

- [OWASP Top 10 - 2021](https://tryhackme.com/room/owasptop102021)

## Best Practices

| Best Practice | Why It Matters |
| ------------- | -------------- |
| Example | Because |

## Summary
