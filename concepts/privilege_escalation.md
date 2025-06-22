# Privilege Escalation

Most capture the flag events involve scenarios where I have a foothold on a machine and now I need to become a user with more privileges so that I can get flags.

There are two main types of escalations, horizontal privilege escalation and vertical privilege escalation.

A typical example of of vertical privilege escalation is where I move from regular user on a Linux machine to root. In most capture the flag events this is the goal so that I can get the root flag.

A horizontal privilege escalation example is moving from one user to another that is not root. The new user will have their own groups, permissions and resources (folders and files) that the original user didn't have. Therefore, I now have more access to the machine but not root access.
