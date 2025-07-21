# Server-Side Request Forgery

## What is Server-Side Request Forgery

Imagine you ask your friend (a website) to go grab something (data) for you from a store (another website). If your friend isn’t careful, you might trick them into going somewhere dangerous, like a restricted area. SSRF is when a hacker tricks a website into making requests to places it shouldn't.

Server-Side Request Forgery (SSRF) occurs when an attacker can make a vulnerable server issue HTTP or other protocol requests on its behalf. It typically results from poorly validated user input used in outbound requests. This is dangerous because internal services (like metadata APIs, admin consoles, or internal APIs) are often not protected from internal access. This can  potentially lead to sensitive data exposure or lateral movement within internal networks.

Modern risks include cloud metadata theft, internal pivoting, service discovery, and chaining with other exploits like remote code execution (RCE) or privilege escalation.

## Common Examples

- A file upload page lets you input a URL to fetch an image, and you trick it into opening http://localhost/admin.
- Using a URL field in a form to probe internal IP ranges: http://10.0.0.1/admin.
- A contact form grabs a profile picture from a URL, but you make it connect to a private IP address like http://127.0.0.1.
- A site lets you check weather info via a URL and you enter an internal network URL instead.
- A website allows importing a document by URL and you use it to make the server request a secret service endpoint.
- An online form that fetches profile pictures via URL is tricked into requesting metadata from a cloud provider (like AWS).
- Exploiting a PDF generation tool that loads external stylesheets to fetch a sensitive file.
- Forcing a server to perform a port scan of internal services.
- SSRF to bypass a firewall and access staging systems or dev tools (e.g., Jenkins dashboards).
- An SSRF chain allowing access to internal GCP/GKE metadata endpoints using crafted Host headers.
- SSRF used against a webhook tester endpoint to enumerate internal services through response timing.
- SSRF leading to Redis command injection via HTTP deserialization in a misconfigured microservice.
- Exploiting image fetch features in reverse proxy setups to bypass authentication to services like Kibana.
- A zero-trust network misconfiguration allows SSRF to trigger OAuth token retrieval from an internal auth server.

## Practice Exploiting Server-Side Request Forgery

- [Basic SSRF against the local server](https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-localhost)
- [SSRF with blacklist-based input filter](https://portswigger.net/web-security/ssrf/lab-ssrf-with-blacklist-filter)

### PortSwigger

PortSwigger has multiple labs to see this vulnerability in action. The labs are online and require an account. Here are some labs:

### OWASP Juice Shop

The OWASP Juice Shop is an open-source project that is intentionally vulnerable. It has many vulnerabilities and makes finding them a bit of a game using their scoreboard page. It can be accessed with Heroku or using Docker. I ran it using Docker and I seem to recall that one of the vulnerabilities will not work properly if you use Heroku. More information on the project and how to run it can [be found here](https://owasp.org/www-project-juice-shop/).

### TryHackMe

TryHackMe has a couple rooms dedicated to this subject. The rooms are online and require an account. Here are some links to rooms that talk about Server-Side Request Forgery:

- [OWASP Top 10 - 2021](https://tryhackme.com/room/owasptop102021)
- [Advanced Server-Side Attacks Module](https://tryhackme.com/module/advanced-server-side-attacks)
- [SSRF](https://tryhackme.com/room/ssrfhr)

## Best Practices


| Best Practice | Why It Matters |
| ------------- | -------------- |
| Validate and sanitize all user-supplied URLs| Prevents attackers from manipulating URLs to target internal systems. |
| Use whitelists for external requests| Restricts requests to trusted and verified domains only. |
| Block access to internal IP ranges (e.g., 127.0.0.1, 169.254.169.254) | Prevents access to sensitive metadata services and internal infrastructure. |
| Disable unused URL-fetching functionality | Reduces the attack surface by removing unnecessary entry points. |
| Use DNS resolution controls | Helps detect and prevent redirection to internal resources via DNS rebinding. |
| Enforce timeouts on HTTP requests | Mitigates potential DoS attacks via slow or stalled internal service calls. |
| Reject URL redirections unless explicitly required | Prevents attackers from chaining redirects to internal services. |
| Log all outbound requests made by the server | Enables detection of suspicious or malicious external calls. |
| Implement server-side request filters | Adds an additional layer of request validation independent of user input. |
| Use separate networks for internal vs. external services | Limits the damage if SSRF is exploited. |
| Do not return raw responses from fetch requests to the client | Prevents data leakage that may aid attackers. |
| Monitor and alert on unusual outbound traffic | Early detection of exploitation attempts or scanning. |
| Use minimal permissions for the server to make external requests | Limits what resources can be accessed even if SSRF occurs. |
| Validate URL schemes (e.g., allow only http/https) | Blocks dangerous protocols like `file://`, `gopher://`, or `ftp://`. |
| Avoid using user-controlled URLs directly in backend APIs | Removes the possibility of SSRF vectors in logic. |
| Use WAF (Web Application Firewalls) with SSRF signatures | Provides an additional defensive layer against known patterns. |
| Regularly test for SSRF via security assessments | Proactively finds and remediates SSRF flaws. |
| Treat URL input as untrusted even if passed from internal sources | Prevents lateral movement attacks using SSRF from internal apps. |
| Educate developers and conduct secure code reviews | Builds awareness of SSRF risks and promotes secure development habits. |


## Summary

Server-Side Request Forgery (SSRF) is a critical web vulnerability where attackers can abuse server functionality to send unauthorized requests to internal or external systems. To mitigate SSRF, best practices focus on validating and sanitizing all user-supplied URLs, using whitelists to restrict destinations, and blocking access to sensitive internal resources like cloud metadata endpoints. It is equally important to enforce strict network segmentation, apply request timeouts, and disable unused request-handling features that may inadvertently expose SSRF vectors.
