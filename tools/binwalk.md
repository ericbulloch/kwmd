# binwalk

Is a tool that looks at the binary of an image and detects embedded files and executable code. Its primary focus is firmware analysis but it works really well in capture the flag events for different image types.

## TryHackMe Attack Box

On the TryHackMe attack box, I have noticed that the binwalk command will generate the following error:

`AttributeError: module 'capstone' has no attribute 'CS_ARCH_ARM64'`

When this happens, I run the following command:

`sed -i 's/CS_ARCH_ARM64/CS_ARCH_AARCH64/g' /usr/lib/python3/dist-packages/binwalk/modules/disasm.py`

[This fix](https://www.reddit.com/r/tryhackme/comments/1i8jj5f/comment/mcqjsir/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) solves the issue.

## Usage

Running `binwalk -h` provided the following output:
