# Enumeration - NFS

[Back to methodology](/methodology/README.md)

- Network File Share (NFS) has the same purpose as SMB - access file systems on a network as if they were local
- NFS is used between Linux and Unix systems, it is not compatible with SMB

## Nmap Scan

```bash
nmap -sC -sV -A -p111,2049 <target>
```

## Nmap Scripts

```bash
sudo nmap 10.10.10.33 -p111,2049 -sV --script nfs*
```

The nfs nmap scripts can enumerate directories and show files along with permissions

## Show Available Shares

```bash
showmount -e 10.10.10.33
```

## Mount Share

```bash
cd /mnt
sudo mkdir target_share
sudo mount -t nfs 10.10.10.33:/ /mnt/target_share -o nolock
```

## List Contents With UIDs And GUIDs

```bash
ls -n target_share
```

## Unmount Share

```bash
sudo umount ./target_share
```
