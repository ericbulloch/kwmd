#!/bin/bash

OVA_PATH="/path/to/MrRobot.ova"
VM_NAME="MrRobot"
HOSTONLY_IF="vboxnet0"

# Import the VM
vboxmanage import "$OVA_PATH" --vsys 0 --vmname "$VM_NAME"

# Remove internet access
vboxmanage modifyvm "$VM_NAME" --nic1 hostonly --hostonlyadapter1 "$HOSTONLY_IF"
