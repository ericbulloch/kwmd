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
- [Registry](#registry)
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

## Registry

The Windows Registry can be very useful for pentration tests. There are many sensitive details that can be gleaned from the Registry. It contains configurations for the following:

- System hardware
- Installed software
- User preferences
- Startup programs
- Services and drivers

Some of the important registry hives to know are:

| Hive | Description |
| --- | --- |
| HKEY_LOCAL_MACHINE (HKLM) | System-wide settings. |
| HKEY_CURRENT_USER (HKCU) | Settings for the current user. |
| HKEY_CLASSES_ROOT (HKCR) | File associations. |
| HKEY_USERS (HKU) | All user profiles. |
| HKEY_CURRENT_CONFIG (HKCC) | Hardware profile info. |

Some targeted or monitored registry paths include:

| Path | Reason |
| --- | --- |
| HKCU\Software\Microsoft\Windows\CurrentVersion\Run | This is used by startup programs. Malware often adds entries here to persist after reboot. |
| HKLM\Software\Microsoft\Windows\CurrentVersion\Run | This is used by startup programs. Malware often adds entries here to persist after reboot. |
| HKLM\SYSTEM\CurrentControlSet\Services | This is used by services and drivers. Used to install malicious services. |
| HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon | This is used for shell modifications. Attackers may hijack shell or userinit values. |
| HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache | This is used by scheduled tasks. Registry entries for scheduled tasks can be abused for persistence. |
