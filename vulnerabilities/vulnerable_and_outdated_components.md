# Vulnerable and Outdated Components

## What are Vulnerable and Outdated Components

Vulnerable and Outdated Components risks occur when an application uses components like libraries, frameworks, or other software modules that are outdated, unsupported, or have known vulnerabilities. Failing to keep these components up to date increases the attack surface because hackers already know how to break into these systems. The vulnerability isn't limited to one component, it's a systemic risk amplified by automation tools, CI/CD pipelines, and modern development practices.

The bottom line is that by not updating your software, hackers are able to leverage know CVEs against your system.

## Common Examples

- Using Internet Explorer instead of updating to a secure browser like Chrome or Firefox.
- Playing a game with mods that haven’t been updated and could be used to hack your account.
- Still using Android 6 where known viruses can break in easily.
- Keeping an outdated app that hasn’t fixed known bugs.
- The school site runs on a 10-year-old system with known CVEs that hackers can exploit.
- Many apps used outdated Log4j libraries that allowed attackers to execute arbitrary code remotely (Log4Shell vulnerability).
- Using a version of jQuery UI with XSS vulnerabilities in DOM manipulation functions.
- Known SQL injection flaw in old versions of Django (< 2.2.24) not yet patched.
- Using a base docker image like ubuntu:16.04 with unpatched system libraries.
- A site using outdated WordPress plugins that allow file upload or XSS.
- Exploiting RCE in Spring Framework in misconfigured Apache Tomcat deployments (Spring4Shell vulnerability).
- Publishing malicious packages to override internal packages in CI/CD environments.
- Installing npm or PyPI modules without checking signatures, leading to code execution at install time.
- IoT devices running legacy OpenSSL versions with Heartbleed vulnerability.

## Practice Exploiting Vulnerable and Outdated Components

### PortSwigger

PortSwigger has multiple labs to see this vulnerability in action. The labs are online and require an account. Here are some labs:

- [Using Burp to Test for Components with Known Vulnerabilities](https://portswigger.net/support/using-burp-to-test-for-components-with-known-vulnerabilities)

### OWASP Juice Shop

The OWASP Juice Shop is an open-source project that is intentionally vulnerable. It has many vulnerabilities and makes finding them a bit of a game using their scoreboard page. It can be accessed with Heroku or using Docker. I ran it using Docker and I seem to recall that one of the vulnerabilities will not work properly if you use Heroku. More information on the project and how to run it can [be found here](https://owasp.org/www-project-juice-shop/).

### TryHackMe

TryHackMe has a couple rooms dedicated to this subject. The rooms are online and require an account. Here are some links to rooms that talk about Vulnerable and Outdated Components:

- [OWASP Top 10 - 2021](https://tryhackme.com/room/owasptop102021)

## Best Practices

| Best Practice | Why It Matters |
| ------------- | -------------- |
| Maintain an inventory of all components | Helps track what libraries, plugins, and tools are in use so they can be evaluated for security risks. |
| Use software composition analysis (SCA) tools | Automates detection of outdated libraries and known CVEs in your codebase. |
| Monitor official sources for component vulnerabilities | Ensures you stay informed of new security issues affecting dependencies.|
| Apply security patches promptly | Reduces the window of exposure to known exploits. |
| Remove unused dependencies | Minimizes attack surface and maintenance overhead. |
| Use trusted sources for dependencies | Prevents supply chain attacks by avoiding compromised or malicious packages. |
| Pin dependency versions | Helps prevent unintended updates to vulnerable or incompatible versions. |
| Set up automated dependency updates | Keeps your software current while reducing manual workload. |
| Use vulnerability databases like NVD or CVE feeds | Provides a reliable reference for assessing the risk of components. |
| Verify integrity of downloaded components (e.g., checksum, signature) | Detects tampering and ensures the authenticity of third-party software. |
| Use minimal base images for containers | Reduces the number of built-in outdated packages in container deployments. |
| Implement runtime protection (e.g., web application firewall) | Adds a layer of defense even if a vulnerable component is exploited. |
| Use long-term support (LTS) versions | Ensures more reliable patching and vendor support. |
| Periodically audit internal and external dependencies | Provides assurance that older or abandoned components are still secure. |
| Avoid relying on deprecated components | Deprecated libraries often stop receiving updates, making them risky. |
| Enforce dependency approval process | Introduces governance and reduces risk of insecure components being added. |
| Separate vulnerable components from critical data paths | Limits the blast radius if a vulnerable component is compromised. |
| Implement static and dynamic application testing | Identifies potential vulnerable usages of components at build and runtime. |
| Regularly test backup systems for compatibility and updates | Ensures that disaster recovery solutions are free of outdated tools. |
| Include third-party components in threat modeling | Helps consider potential threats introduced by external code early in development. |


## Summary

Vulnerable and outdated components pose a serious risk in software systems because attackers often exploit known flaws in third-party libraries, frameworks, and tools. The best way to defend against this threat is to maintain awareness and control over every component in your environment. Practices like maintaining an up-to-date inventory, removing unused dependencies, and relying only on trusted sources help organizations reduce their exposure. Tools such as Software Composition Analysis (SCA), vulnerability databases, and automated update mechanisms make it easier to detect and fix issues early, before attackers can take advantage.

Security is also strengthened by incorporating thoughtful design and governance processes. Pinning dependency versions, enforcing approval workflows, and using LTS (Long-Term Support) versions ensure greater stability and fewer surprises. Furthermore, verifying the integrity of downloads and isolating risky components from critical data flows adds defense in depth. Periodic auditing, both static and dynamic testing, and incorporating third-party software into your threat models round out a mature and proactive security strategy for managing third-party risks effectively.
