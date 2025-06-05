# Insecure Design

## What is Insecure Design

Insecure Design is building software without thinking enough about how to keep it safe from hackers. It refers to flaws in architecture and planning phases of software development. It’s not a bug in the code—it’s a flaw in how the system was intended to work from the beginning. It stems from insufficient thread modeling, lack of security-centric user stories, and absence of defense-in-depth.

I want to reiterate, due to poor planning, architecture and design, **these issues exist regardless of how well the code is written**.

## Common Examples

- No login required to use the app – Anyone can access it without proving who they are.
- No limit on password tries – A hacker could keep guessing until they get in.
- Sharing private info in public links – Like showing your diary on a billboard.
- No security questions or recovery options – If you lose access, so can a hacker easily gain it.
- No role-based access control (RBAC) – Users have more access than they should.
- Hardcoded business rules that assume user honesty – Trusting client-side input without server verification.
- Not using HTTPS for sensitive transactions – Leaves user data exposed to man-in-the-middle attacks.
- Lack of security considerations in design documents – Leads to implementation without a secure foundation.
- Business logic flaws – For example, refunding items without verifying the purchase state.
- Missing secure-by-default settings – Allowing insecure configurations in production environments.
- Improper data partitioning in multi-tenant environments – A tenant can access data from another tenant.
- Lack of compensating controls for external integrations – Trusting third-party APIs without validation or isolation.
- Inadequate threat modeling for privileged workflows – E.g., administrative interfaces accessible without sufficient segregation or audit logging.

## Practice Exploiting Insecure Design

### PortSwigger

PortSwigger has multiple labs to see this vulnerability in action. The labs are online and require an account. Here are some labs:

- [Insecure direct object references](https://portswigger.net/web-security/access-control/lab-insecure-direct-object-references)
- [OS command injection, simple case](https://portswigger.net/web-security/os-command-injection/lab-simple)
- [CSRF vulnerability with no defenses](https://portswigger.net/web-security/csrf/lab-no-defenses)

### OWASP Juice Shop

The OWASP Juice Shop is an open-source project that is intentionally vulnerable. It has many vulnerabilities and makes finding them a bit of a game using their scoreboard page. It can be accessed with Heroku or using Docker. I ran it using Docker and I seem to recall that one of the vulnerabilities will not work properly if you use Heroku. More information on the project and how to run it can [be found here](https://owasp.org/www-project-juice-shop/).

### TryHackMe

TryHackMe has a couple rooms dedicated to this subject. The rooms are online and require an account. Here are some links to rooms that talk about Insecure Design:

- [OWASP Top 10 - 2021](https://tryhackme.com/room/owasptop102021)

## Best Practices

| Best Practice | Why It Matters |
| ------------- | -------------- |
| Implement Threat Modeling Early | Identifies potential security issues during the design phase, allowing for proactive mitigation strategies. |
| Adopt Secure Design Principles | Principles like least privilege, defense-in-depth, and fail-safe defaults help in building robust security into the system architecture. |
| Define and Enforce Security Requirements | Clearly stated security requirements ensure that security is considered throughout the development lifecycle. |
| Use Secure Design Patterns and Frameworks | Leveraging established secure design patterns reduces the likelihood of introducing vulnerabilities. |
| Conduct Regular Design Reviews | Periodic reviews of the system design help in identifying and addressing security flaws before implementation. |
| Educate Development Teams on Secure Design | Training developers on secure design principles fosters a security-first mindset, reducing the introduction of design flaws. |
| Integrate Security into SDLC Processes | Incorporating security checkpoints into the Software Development Life Cycle ensures continuous attention to security concerns. |
| Limit Exposure of Sensitive Data | Minimizing the collection and storage of sensitive data reduces the impact in case of a breach. |
| Implement Proper Access Controls | Ensuring that users have access only to the resources they need prevents unauthorized access and potential data breaches. |
| Plan for Secure Failure States | Designing systems to fail securely ensures that, in the event of a failure, the system does not expose sensitive information or become vulnerable to attacks. |

## Summary

Insecure Design can be prevented. The software development process needs to establish and use a secure development lifecycle. The team needs to evaluate and design security and privacy-related controls. Threat modeling needs to occur for critical authentication, access control, business logic and key flows. Bad actor use cases need to be implemented that are based on that threat modeling. Unit and integration tests are needed to try and validate all critical flows that were written for bad actor use cases.
