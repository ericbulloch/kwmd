# Home Lab

## Regular Lab

My home lab setup is very simple. Here are the details:

- I use Vagrant and VirtualBox for tooling.
- My host machine is Ubuntu.
- I have created a network called targets. This network does not have access to the internet.
- All the target machine are on the target network so that they can be hacked without having a connection to the internet.
- I have a Kali Linux box as an attack machine that has a NAT connection to my host machine so that it has access to the internet but not my host machine or the host's network. It also has a nic that is on the targets network so that it can connect to the different target machines.

## Bug Bounty Hunting

I also have a Kali Linux virtual machine that I use for bug bounty hunting. It also uses the NAT connection but does not connect to any other network.
