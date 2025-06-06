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

## Examples

LinPEAS throws a lot of information at me all at once. Generally the first step is to download the file onto the machine. I almost always download the file into the `/tmp` directory since it is writable by all users. To download the file I run the following command:

`wget https://github.com/peass-ng/PEASS-ng/releases/download/20250601-88c7a0f6/linpeas.sh`

This will save the file as linpeas.sh. Now I set the script to executable with the following command:

`chmod +x linpeas.sh`

Again, LinPEAS throws a lot of information at me. When I run it, I use the `-w` option so that it will pause between sections of the script. That way I can look over the report for just that small section and see if it reported anything that will help me escalate. Here is an example of the command:

`./linpeas.sh -w`
