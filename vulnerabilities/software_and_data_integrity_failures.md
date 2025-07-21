# Software and Data Integrity Failures

## What are Software and Data Integrity Failures

Software and Data Integrity Failures happen when a computer program doesn’t check if the files, updates, or data it’s using are safe and haven’t been changed by a hacker. If a bad person tricks the software into using fake or changed files, they can make it do bad things.

This category covers failures to verify software code, libraries, dependencies, or data for integrity before use. This often happens when applications use unsigned code, fail to validate digital signatures, or load untrusted components (like plugins) from public sources without verifying their source or integrity.

Attackers exploit trust assumptions in CI/CD pipelines, software supply chains, and external dependencies (such as 3rd-party modules or update mechanisms). Attacks like dependency confusion, typosquatting, or compromised build artifacts fall into this category. This category has gained prominence with attacks like SolarWinds and Codecov.

## Common Examples

- A game downloads a "new update" from the internet, but it doesn't check who sent it. A hacker replaces the update with malware.
- If your school computer runs a program using your homework file and someone changes that file to add a virus, the computer could get infected.
- You install a browser extension from an unofficial site. It looks fine but secretly steals your data.
- A teacher's software auto-runs a file from a USB drive. If that file was replaced by someone with bad intentions, it might harm the system.
- Your antivirus app updates itself without checking if the update is really from the official company. A hacker could push a fake update.
- A pipeline pulls unsigned build scripts from an unverified GitHub repo. A contributor inserts malicious code that gets deployed into production.
- A developer installs an NPM package without checking its source. A malicious update in the package steals environment variables like AWS credentials.
- Pulling a Docker container from Docker Hub without digest verification could result in using a tampered image with backdoors.
- A desktop application downloads updates over HTTP instead of HTTPS and doesn't verify digital signatures.
- A CMS loads third-party plugins directly from a public server. One of the plugins is replaced with a backdoored version.
- An attacker publishes a malicious package with the same name as an internal dependency to a public registry. Internal tooling mistakenly pulls the public one.
- A malicious actor gains access to a developer's credentials and injects a malicious commit into a build branch, which gets signed and deployed.
- An enterprise Java application dynamically loads unsigned JARs, leading to arbitrary code execution.
- A CRM platform uses unverified scripts from a 3rd-party marketing service. The service is compromised, allowing attackers to pivot into customer data.
- Artifacts in a build pipeline are cached and served to downstream systems without checksum validation, leading to compromised artifact reuse.

## Practice Exploiting Software and Data Integrity Failures

### PortSwigger

PortSwigger has multiple labs to see this vulnerability in action. The labs are online and require an account. Here are some labs:

- [Using application functionality to exploit insecure deserialization](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-using-application-functionality-to-exploit-insecure-deserialization)

### OWASP Juice Shop

The OWASP Juice Shop is an open-source project that is intentionally vulnerable. It has many vulnerabilities and makes finding them a bit of a game using their scoreboard page. It can be accessed with Heroku or using Docker. I ran it using Docker and I seem to recall that one of the vulnerabilities will not work properly if you use Heroku. More information on the project and how to run it can [be found here](https://owasp.org/www-project-juice-shop/).

### TryHackMe

TryHackMe has a couple rooms dedicated to this subject. The rooms are online and require an account. Here are some links to rooms that talk about Software and Data Integrity Failures:

- [OWASP Top 10 - 2021](https://tryhackme.com/room/owasptop102021)
- [Hashing Basics](https://tryhackme.com/room/hashingbasics)
- [Cryptography Module](https://tryhackme.com/module/cryptography-101)

## Best Practices

| Best Practice | Why It Matters |
| ------------- | -------------- |
| Example | Because |

## Summary
