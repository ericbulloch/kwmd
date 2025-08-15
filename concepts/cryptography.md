# Cryptography

- [Introduction](#introduction)
- [Text Encoding](#text-encoding)

## Introduction

Cryptography is taking information (generally text) and securing it from unwanted users. Several different forms implementations of cryptography are discussed.

Part of cryptography is encryption, which is the actual process of converting information into an unreadable format (ciphertext) to protect it from unauthorized access. Encryption is one of the key backbone concepts of computing not just cyber security. When done incorrectly or poorly, it can be cause data breaches, financial losses, identity theft and reputation damage.

## Text Encoding

Encoding is similar and related to encryption, with encryption focusing on data security and confidentiality, while encoding focuses on data usability and representation.

Most capture the flag events have text that has been encoded in different formats. The servers in the capture the flag events will have passwords and other credentials encoded in different formats that I need to decode to move on to the next part of the event. I usually decode them on the [CyberChef website](https://cyberchef.com). Some of the formats can be decoded from the Linux terminal using some binaries that are available on Kali.

### Sample Text

I am encoding the text "Anyone can learn about cyber security!" into different formats that I have seen in capture the flag events:

| Type | Text |
| --- | --- |
| Base 32 | `IFXHS33OMUQGGYLOEBWGKYLSNYQGCYTPOV2CAY3ZMJSXEIDTMVRXK4TJOR4SC===` |
| Base 45 | `AC8$FF1/DB44CECK44X C:KE944:JC8%EB44OFF5$CR44Z C6%E-ED4EF` |
| Base 62 | `K0964MlTDohPr4N5YafBjpSbo0l9algtO199y73ed1yOXwW2CfJ` |
| Base 64 | `QW55b25lIGNhbiBsZWFybiBhYm91dCBjeWJlciBzZWN1cml0eSE=` |
| Base 85 | ```6#LsdDIjr#@;[3(ARTUs+CS_tF`\a9H"(?*+EM+(F`M2<Gp*``` |
| Base 92 | `9!kped3j$2gQQqDrD:=AOSa>y{t_*fjGE_9wk<aO@\m1,]$` |
| Binary | `01000001 01101110 01111001 01101111 01101110 01100101 00100000 01100011 01100001 01101110 00100000 01101100 01100101 01100001 01110010 01101110 00100000 01100001 01100010 01101111 01110101 01110100 00100000 01100011 01111001 01100010 01100101 01110010 00100000 01110011 01100101 01100011 01110101 01110010 01101001 01110100 01111001 00100001` |

### Octal

101 156 171 157 156 145 40 143 141 156 40 154 145 141 162 156 40 141 142 157 165 164 40 143 171 142 145 162 40 163 145 143 165 162 151 164 171 41

### Hex

41 6e 79 6f 6e 65 20 63 61 6e 20 6c 65 61 72 6e 20 61 62 6f 75 74 20 63 79 62 65 72 20 73 65 63 75 72 69 74 79 21

### ROT13

Nalbar pna yrnea nobhg plore frphevgl!

### ROT47

p?J@?6 42? =62C? 23@FE 4J36C D64FC:EJP

### URL Encode

`Anyone%20can%20learn%20about%20cyber%20security!`

### HTML Entity

`&#65;&#110;&#121;&#111;&#110;&#101;&#32;&#99;&#97;&#110;&#32;&#108;&#101;&#97;&#114;&#110;&#32;&#97;&#98;&#111;&#117;&#116;&#32;&#99;&#121;&#98;&#101;&#114;&#32;&#115;&#101;&#99;&#117;&#114;&#105;&#116;&#121;&excl;`

The list of formats is long. This is only a fraction of the ones that are available. These are the ones that I have seen multiple times.

**Please note**: It is not uncommon to see text that has been encoded with multiple formats. Two or more encoding can be used. CyberChef has a Magic recipe to help solve these.
