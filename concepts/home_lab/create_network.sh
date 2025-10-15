#!/bin/bash

# Create a new host-only network
vboxmanage hostonlyif create

# Get the name of the newly created interface
IFACE=$(vboxmanage list hostonlyifs | grep -B1 "IPAddress: 192.168.56.1" | head -n1 | awk -F: '{print $2}' | xargs)

# Configure the interface with a custom subnet
vboxmanage hostonlyif ipconfig "$IFACE" --ip 192.168.56.1 --netmask 255.255.255.0

# Disable DHCP to prevent host access
vboxmanage dhcpserver remove --ifname "$IFACE"
