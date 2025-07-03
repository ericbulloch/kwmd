# Linux

I wanted to list some concepts, terms and flows that are specific to Linux. Learning more about Linux has made me a better and more effcient pentration tester.

## LXD (pronounced lex-dee)

LXD is used to manage virtual machines and system containers. It has very minimal overhead. I have used both Docker and Podman in the past and it works very similar to both.

I can create or download an image, start multiple containers from that single image and have them interact with each other.

The lxc command is used to start and stop containers. To use the lxd and lxc binaries my user was in the lxd group.

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

Step 4 - Map the host hard drive to the container hard drive.

```bash
$ lxc config device add kwmd mydrive disk source=/ path=/mnt/root recursive=true
```

This mounts the / directory on the host to the /mnt/root directory in the container. This combined with the security.privileged=true in step 3 is very dangerous.
