# SSH

## Initial Information

If nmap shows that SSH is running on a machine, I will manually connect to it. I am trying to see if it asks for a password. If that is the case, this is another attack vector I can use if I can find a username on the server.

If the password prompt does not show up and I get an error that says "Permission denied (publickey)", my attack vector is reduced.

Also, sometimes I need to connect to SSH on a different port. This involves using the `-p` option. If I need to connect on port 2222, I would run:

`ssh -p 2222 user@target.thm`

## SSH Brute Force

SSH does have some CVEs (Common Vulnerabilites and Exposures) but I rarely have to use them in a capture the flag event. Usually I will need to brute force SSH because I have found a username (for example, bob) but do not know the password, I will run Hydra using the rockyou.txt wordlist to see if I can find the password and log into the server. Using [the example found here](hydra.md#ssh), I run:

`hydra -l bob -P /usr/share/wordlists/rockyou.txt 10.10.1.1 ssh`

Other tools like Burp Suite can do this as well but I prefer Hydra because it doesn't rate limit me.
