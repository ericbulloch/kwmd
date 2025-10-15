#!/bin/bash

VM_NAME="Kali-Lab"
ISO_PATH="/path/to/kali-linux.iso"
HOSTONLY_IF="vboxnet0"  # Replace with your actual host-only interface name

# Create VM
vboxmanage createvm --name "$VM_NAME" --ostype "Debian_64" --register
vboxmanage modifyvm "$VM_NAME" --memory 4096 --cpus 2 --nic1 nat --nic2 hostonly --hostonlyadapter2 "$HOSTONLY_IF"

# Create disk
vboxmanage createhd --filename "$HOME/VirtualBox VMs/$VM_NAME/$VM_NAME.vdi" --size 30000

# Attach storage
vboxmanage storagectl "$VM_NAME" --name "SATA Controller" --add sata --controller IntelAhci
vboxmanage storageattach "$VM_NAME" --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium "$HOME/VirtualBox VMs/$VM_NAME/$VM_NAME.vdi"
vboxmanage storageattach "$VM_NAME" --storagectl "SATA Controller" --port 1 --device 0 --type dvddrive --medium "$ISO_PATH"

# Boot to install
vboxmanage modifyvm "$VM_NAME" --boot1 dvd
