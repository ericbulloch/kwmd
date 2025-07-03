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
