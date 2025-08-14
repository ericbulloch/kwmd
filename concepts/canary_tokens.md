# Canary Tokens

- [Introduction](#introduction)
- [Types of Canary Tokens](#types-of-canary-tokens)
- [When To Use](#when-to-use)

## Introduction

Canary tokens are a digital booby trap that when sprang let's an attacker know that a system is vulnerable to an attack. These are very valuable to help determine if a system is vulnerable to a blind attack (XSS, SSRF, RCE, RFI, etc...). The name comes from the canary birds that miners would take into mines to detect if the air had a high concentration of poison.

## Types of Canary Tokens

Canary tokens are digital objects that can phone home and notify me when they get used. Below is a table of sample canary tokens.

| Type | Explaination |
| --- | --- |
| Fake AWS Access Token | This token can be place in a repository; if someone tries to use the access token, I will get notified. |
| Document Canary | A word or pdf file that contains a script that calls out to my api to let me know it was opened. |
| DNS Canary | A unique subdomain that when queried lets me know that someone tried to access it. Sites like canarytokens.org are used for this. |
| Web Bug Image | An invisible (1x1 pixel) image in a file or webpage that when loaded, calls out to my server. |

## When To Use

There are many parts of a website that do not provide much feedback. Canaries can help detect vulnerabilities in these parts of the system. Below is a list of scenarios where they might help.

- Feedback or contact forms that accept user input. An image could contain an url to my server or a document attachment that phones home when opened.
- CSV upload forms can accept a document with a formula that phones home when opened.
- A page with a file path parameter could reach out to my server to pull a file.
- Any part of a site that takes a url as input, at the very least this can be used as a DNS canary.
- Planting a document in a sensitive share to see if defenders are snooping.
