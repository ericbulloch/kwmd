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
| Use signed software packages | Ensures authenticity and integrity of software before installation. |
| Implement Subresource Integrity (SRI) for web assets | Protects against tampering of third-party JavaScript and CSS resources. |
| Verify digital signatures of third-party libraries | Prevents malicious modifications in dependencies. |
| Use trusted sources for updates and dependencies | Reduces risk of downloading backdoored or fake packages. |
| Regularly scan dependencies for known vulnerabilities | Detects and mitigates threats introduced through third-party code. |
| Use immutable infrastructure where possible | Prevents unauthorized changes to systems and applications. |
| Implement strict dependency pinning | Prevents accidental or malicious upgrades to vulnerable versions. |
| Use secure package managers (e.g., pip, npm) with lock files | Maintains integrity and consistency across builds. |
| Perform integrity checks on runtime data and configurations | Helps detect tampering or corruption during operation. |
| Use Content Security Policy (CSP) to limit external resource loading | Reduces risk of loading compromised assets from unknown domains. |
| Validate and verify build pipelines | Prevents CI/CD system compromise and introduction of malicious code. |
| Sign container images and verify signatures during deployment | Ensures container authenticity and immutability. |
| Audit and review code dependencies and license compliance | Identifies untrusted or high-risk libraries. |
| Monitor and alert on unauthorized file or config changes | Detects real-time integrity violations in critical systems. |
| Implement access controls on CI/CD infrastructure | Reduces attack surface for manipulating build artifacts. |
| Avoid using outdated or unsupported libraries | Minimizes exposure to known but unpatched vulnerabilities. |
| Maintain a software bill of materials (SBOM) | Increases transparency and traceability of all software components. |
| Ensure source control integrity (e.g., signed Git commits) | Prevents unauthorized or hidden changes to source code. |
| Use reproducible builds | Ensures that builds can be verified independently to match source. |
| Regularly conduct supply chain security assessments | Identifies weak points in the software development lifecycle. |

## Summary

Software and Data Integrity Failures occur when systems fail to verify the integrity or authenticity of software and data, leaving the door open for attackers to insert malicious content during updates, installations, or runtime. Using preventive measures such as using signed packages, verifying digital signatures, and sourcing dependencies from trusted repositories help reduce your attack surface. Strategies like Subresource Integrity (SRI) and Content Security Policies (CSP) add further protection to web applications by restricting or validating third-party content. Immutable infrastructure and dependency pinning also help maintain consistency and reduce the risk of accidental or malicious changes.

Software and Data Integrity Failures emphasizes securing the development and deployment pipeline. Measures like auditing CI/CD pipelines, using access controls, and verifying container image signatures ensure that only intended code is built and deployed. Maintaining a software bill of materials (SBOM) and monitoring for unauthorized changes enable traceability and detection of supply chain compromises. Ultimately, these practices reinforce the principle that integrity checks must be present throughout the software lifecycle—from development to deployment—to effectively defend against tampering and compromise.
