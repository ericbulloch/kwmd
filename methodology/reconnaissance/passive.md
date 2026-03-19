# Passive Reconnaissance

[Back to methodology](/methodology/README.md)

## Google Dorking

I have notes on how to do this in my [Google Dorking](/concepts/google_dorking.md) page. I am looking for the following:

- Organization & Domain profiling
  - Primary domain(s)
  - Company name variables and doing business as (dba) names
  - Subsidiaries/acquisitions
  - Associated brands
- Additional Domains
- Email patterns (e.g., first.last@company.com)
- Ownership clues

## DNS & Subdomain Enumeration (Passive Only)

Tools that can be used include:

- crt.sh (certificate transparency logs)
- Subfinder

crt.sh can be used to extract subdomains tied to SSL certs. These subdomains might not be indexes elsewhere. Domains can still work even if DNS no longer resolves the subdomain.

Sample usage for subfinder:

```bash
subfinder -d target.com -passive -o subdomains.txt
```

I am looking for:

- Hidden subdomains
- Dev/staging environments
- Internal naming conventions (dev, test, staging, preprod, vpn, jira, etc.)

## Public Data Leaks & Breaches

Usernames and passwords can be viewed for sites that have been compromised. Some sites include:

- HaveIBeenPwned
- Paste sites

I am looking for the following:

- Credentials
- Email formats
- Password reuse patterns

## Leaked Technologies

I am looking to find out what technologies the company is using. I can find this information on the following sites:

- LinkedIn
- GitHub
- X

Here is what I am looking for:

- Technologies in use (from job postings and proficiencies of employees on LinkedIn)
- Internal tools (Jira, Jenkins, AWS, Azure, etc.)
- Developer mistakes (hardcoded secrets on GitHub)
