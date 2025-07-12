# VulnHub Write-Ups

It is important to setup a home lab before attempting any of the machines on VulnHub for your safety. At [the bottom](#home-lab-setup) of this page I have provided a video link and steps to setup a home lab that I used. The steps are straight forward and quick.

Here are the list of write-ups that I have done for VulnHub.

- [Mr. Robot](mr_robot.md)

## Home Lab Setup

VulnHub provides a lot of machines that can be attacked. There are a lot of learning opportunities because there are so many boxes.

Because of the nature of these boxes, when I install them on my machine, I will be making my machine vulnerable to attack. I want to learn but I also want to reduce the risk of my machine being attacked. I found [this video](https://www.youtube.com/watch?v=0XMYtZx1M9g) on youtube that talks about the steps to create a home lab.

The idea is to setup a hacking virtual environment where I have an attack machine that I can hack from and a vulnerable server that I will be hacking. Both machines are in a virtual network that isn't in the same network as my host computer. Here is a summary of the steps from the video:

- Download and Install VirtualBox.
- Download Kali Linux vbox image.
- Download a machine from VulnHub.
- Open up VirtualBox and add the Kali Linux vbox image.
- Open up VirtualBox and add the machine from VulnHub.
- Create an internal network that our machines will use.
  - In VirtualBox go to the Settings of your Kali Linux machine.
  - Click the Network tab on the left.
  - In the Adapter 1 tab change the Attached to field from NAT to Internal Network.
  - In the Name input field below Attached to, give your network any name you like.
- Repeat the 4 steps above for the vulnerable machine.
- Create a DHCP server for the network you just named.
  - Open up a command prompt and and move to the directory that has the vboxmanage command. On Windows, this is at `C:\Program Files\Oracle\VirtualBox`.
  - Run the following command `vboxmanage dhcpserver add --network=the_network_name_you_chose --server-ip=10.22.1.1 --lower-ip=10.22.1.110 --upper-ip=10.22.1.130 --netmask=255.255.255.0 --enable`
- Now you can power up your machines and run a command like `ifconfig` in Kali to make sure it has an ip address between 10.22.1.110 and 10.22.1.130.
