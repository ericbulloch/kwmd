#!/bin/bash

# Script to scan a network for machines that have MySQL port 3306 running.
# Adapted from Linux Basics for Hackers.
echo "Starting the MySQL scanner."

defaultRange="target.thm"
echo "Enter IP address range for nmap to scan (default: $defaultRange): "
read ipRange
ipRange="${ipRange:-$defaultRange}"

defaultPort=3306
echo "Enter the port number(s) you want nmap to scan (default: $defaultPort): "
read port
port="${port:-$defaultPort}"

echo "Starting scan of $ipRange on port(s) $port."
nmap -sT $ipRange -p $port >/dev/null -oG mysql_scan.txt

echo "Scan complete, parsing results."
cat mysql_scan.txt | grep open
