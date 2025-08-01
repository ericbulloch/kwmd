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

- [Lab: Authentication bypass via information disclosure](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-authentication-bypass)
- [Using Burp to Test for Security Misconfiguration Issues](https://portswigger.net/support/using-burp-to-test-for-security-misconfiguration-issues)

### OWASP Juice Shop

The OWASP Juice Shop is an open-source project that is intentionally vulnerable. It has many vulnerabilities and makes finding them a bit of a game using their scoreboard page. It can be accessed with Heroku or using Docker. I ran it using Docker and I seem to recall that one of the vulnerabilities will not work properly if you use Heroku. More information on the project and how to run it can [be found here](https://owasp.org/www-project-juice-shop/).

### TryHackMe

TryHackMe has a couple rooms dedicated to this subject. The rooms are online and require an account. Here are some links to rooms that talk about Security Logging and Monitoring Failures:

- [OWASP Top 10 - 2021](https://tryhackme.com/room/owasptop102021)
- [Evading Logging and Monitoring](https://tryhackme.com/room/monitoringevasion)
- [Security Operations & Monitoring Training Module](https://tryhackme.com/module/security-operations-and-monitoring)
- [Windows Threat Detection 1](https://tryhackme.com/room/windowsthreatdetection1)
- [Windows Threat Detection 2](https://tryhackme.com/room/windowsthreatdetection2)

## Best Practices

| Best Practice | Why It Matters |
| -------------- | -------------- |
| Enable logging for all authentication attempts | Helps detect brute-force attacks |
| Store logs in a centralized, secure log management system | Ensures logs can’t be tampered with or lost during an incident |
| Include timestamps in all logs, usually utc | Enables accurate timeline reconstruction during incident response |
| Record source IP addresses with every log entry | Helps trace the origin of malicious activity |
| Use log integrity controls (e.g., hashing, immutability) | Prevents attackers or insiders from modifying log history |
| Monitor logs in real-time using a SIEM or log analysis tool | Enables immediate detection and response to critical events |
| Generate alerts for high-risk actions (e.g., privilege escalation) | Informs defenders of potential attacks before damage is done |
| Log all access to sensitive data (PII, health records, etc.) | Tracks who accessed what data and when, ensuring compliance and accountability |
| Protect log data at rest and in transit | Prevents unauthorized access or interception of sensitive log content |
| Set appropriate log retention policies | Ensures logs are available when needed for audits or investigations |
| Log all administrative and configuration changes | Tracks changes to the application or infrastructure that could introduce vulnerabilities |
| Regularly review and audit logs manually and automatically | Identifies patterns or anomalies that may indicate compromise |
| Avoid logging sensitive information in plaintext (e.g., passwords) | Protects against data exposure in case of a breach |
| Ensure application errors are logged with context | Helps developers and security teams understand what failed and why |
| Test logging and alerting controls regularly | Confirms that logging mechanisms are working as intended |
| Use unique identifiers (e.g., request IDs or GUIDs) to trace user sessions | Facilitates tracing actions across systems during investigations |
| Integrate log data with incident response platforms | Accelerates investigation and reduces dwell time during attacks |
| Train developers and engineers on proper logging practices | Ensures logging is done securely and effectively throughout the software development lifecycle |

## Summary

Security Logging and Monitoring Failures often leave organizations blind to ongoing attacks or breaches until it’s too late. The goal for logging is that logs are complete, accurate, secure, and actionable. Key practices include enabling detailed logging for authentication attempts, administrative actions, and access to sensitive data, as well as ensuring all logs include context like timestamps and IP addresses. Storing logs centrally, protecting them from tampering, and applying retention policies ensures that historical data is available and trustworthy during investigations or audits.

Equally important is the proactive use of this logging data. Monitoring tools like SIEMs should analyze logs in real time and generate alerts for suspicious or high-risk behavior, such as privilege escalation or failed login patterns. Developers and engineers must be trained not to log sensitive data in plaintext and to regularly test and review their logging setup. Ultimately, strong logging and monitoring practices empower security teams to detect, investigate, and respond to threats quickly—reducing the potential impact of security incidents.
