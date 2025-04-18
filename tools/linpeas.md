# linpeas

Once I have a shell running on a capture the flag box, I often need to escalate my privilege to another user up until root. Privilege escalation is a little bit of art and a little bit of science. There are so many things that I need to check and be aware of on a target machine. Here are something linpeas checks:

- Check environment variables
- Get system information
- View currently running processes
- Check executables that have the Suid bit set
- Check folders and directories that have permissions that are too open
- Check what cron jobs are listed
- What groups the current user belong to

There are many other checks and the list keeps growing. I download and follow the instructions found at the [linPEAS repository](https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS). 
