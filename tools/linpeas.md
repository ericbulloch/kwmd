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

### Useful Options

#### Pause execution between big blocks of checks

Again, LinPEAS throws a lot of information at me. When I run it, I use the `-w` option so that it will pause between sections of the script. That way I can look over the report for just that small section and see if it reported anything that will help me escalate. Here is an example of the command:

`./linpeas.sh -w`

The output will now show results and then have `Press enter to continue` after a few sections have executed. Now I can review what was found and press enter when I am ready to continue.

#### Only execute selected checks

Sometimes I will get stuck and miss something during a capture the flag event. I'll look at a write up and it will tell me that they found something in LinPEAS that helped them. I don't want to wait for the entire script to run again so I will just run a single check. The `-o` option makes this possible. If I only wanted to run the system_information check, I would run the following:

`./linpeas.sh -o system_information`

I can also specify two or more checks by separating them with a comma. Here is an example:

`./linpeas.sh -o system_information,procs_crons_timers_srvcs_sockets,interesting_files`

#### Perform all checks

There are a few checks that LinPEAS doesn't perform. Some of them are time consuming. If I include the `-a` flag, LinPEAS will run the extra checks. These checks include 1 min of processes, su brute, and extra checks. Here is an example of how to run this:

`./linpeas.sh -a`
