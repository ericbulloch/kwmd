# Windows

- [Introduction](#introduction)
- [Services](#services)
- Permissions
- Windows Defender
- User Account Control (UAC)
- Antivirus
- Active Directory
- Scheduled Tasks
- Startup Applications
- Protocols
- Event Viewer
- Registry
- Privilege Escalation

## Introduction

I wanted to list some concepts, terms and flows that are specific to Windows. There is a lot of information to cover, I use this page as a reference.

## Services

Windows services are background processes that are similar to a Linux daemon. They typically start when the system boots up and run without direct user intervention. They can also start by being manually triggered or when needed. There are many Windows services and they can do a range of functions. Some of those functions include:

- Networking
- Authentication
- Printing
- Monitoring
- Antivirus
- Windows Updates

Each service has a name, display name and description. They are registered in the Windows Service Control Manager, which also starts, stops and manages them. They can run with different levels of privileges. Some of the levels they can run as include:

- Local System (high privilege)
- Network Service
- Local Service
- Specific User Account

They typically run as an executable or a DLL loaded by svchost.exe.

### Privilege escalation vectors

Here are a few ways Windows services can be used for privilege escalation:

- If Windows services are misconfigured, they can allow privilege escalation (e.g. writable binary path).
- If an attacker can write to the executable that is being ran as a service, it can be replaced with malicious code.
- Also, if the service loads a DLL from a directory that is writable, that DLL can be replaced with a malicious one.
- A service running with Local System privileges can be exploited if it executes user-controlled code.

In fact, malware will often install itself as a service to ensure that it is running even after a system reboot.
