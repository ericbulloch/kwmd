# THM: Crack the hash

| Stat       | Value                                        |
| ---------- | -------------------------------------------- |
| Room       | Crack the hash                               |
| URL        | https://tryhackme.com/room/crackthehash      |
| Difficulty | Easy                                         |

## Concepts/Tools Used

- [CrackStation](https://crackstation.net/)
- [Hashes.com](https://hashes.com/en/tools/hash_identifier)
- [HashCat](https://hashcat.net/wiki/doku.php?id=example_hashes)

## Description

Cracking hashes challenges.

### Process

I am presented with two groups of hashes. The first group is called level 1 and it has 5 hashes. The second group is called level 2 and it has 4 hashes. Since I am trying to break hashes, I load the CrackStation website. I am hoping it can crack a bunch of these. I load all of the hashes into the input field so that I only needed to submit the hashes one time.

#### Level 1

The task text says:

Can you complete the level 1 tasks by cracking the hashes?

##### 48bb6e862e54f2a795ffc4e541caed4d

I load the hash into CrackStation and it breaks this one instantly. This hash is an md5 hash.

##### CBFDAC6008F9CAB4083784CBD1874F76618D2A97

I load the hash into CrackStation and it breaks this one instantly. This hash is an sha1 hash.

##### 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032

I load the hash into CrackStation and it breaks this one instantly. This hash is an sha256 hash.

##### $2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom

CrackStation was unable to instantly break this one. I ran this hash through hashes.com and it thinks the the hash is one of these possible algorithms: bcrypt $2*$, Blowfish (Unix). This hash appears to be mode 3200 on the HashCat example hashes page. I loaded the hash value into a text file that I name hash.txt.

Blowfish is a really slow cipher. It is designed to make it painful to crack a hash by taking a long time with each attempt. The hint for this problem says:

This type of hash can take a very long time to crack, so either filter rockyou for four character words, or use a mask for four lower case alphabetical characters

I have provided a python script that I used to filter the words in rockyou.txt. This sped up the this problem significantly.

```python
import string

with open('trimmed.txt', 'w') as wp:
    with open('/usr/share/wordlists/rockyou.txt', 'r', encoding='latin1') as fp:
        for line in fp.readlines():
            line = line.strip()
            if len(line) != 4:
                continue
            for c in line:
                if c not in string.ascii_lowercase + string.digits:
                    continue
            wp.write(line + '\n')
```

I saved that script as `trim.py` and ran the following command to execute it:

`python3 trim.py`

That generates a file named `trimmed.txt` that I can use for hashcat.

Now there are only 18k words that are being checked instead of millions.

I run the following command on the attack box:

`hashcat -m 3200 hash.txt trimmed.txt`

After a few minutes hashcat output the answer. The answer had the format:

`$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom:####`

The #### at the end was the answer.

##### 279412f945939ba78ce0758d3fd83daa

I load the hash into CrackStation and it breaks this one instantly. This hash is an md4 hash.

#### Level 2

The task text says:

This task increases the difficulty. All of the answers will be in the classic [rock you](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) password list.

You might have to start using hashcat here and not online tools. It might also be handy to look at some example hashes on [hashcats page](https://hashcat.net/wiki/doku.php?id=example_hashes).

##### F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85

I load the hash into CrackStation and it breaks this one instantly. This hash is an sha256 hash.

##### 1DFECA0C002AE40B8619ECF94819CC1B

I load the hash into CrackStation and it breaks this one instantly. This hash is an NTLM hash.

##### Hash: $6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02. Salt: aReallyHardSalt

CrackStation was unable to instantly break this one. I ran this hash through hashes.com and it thinks the the hash is one of these possible algorithms: sha512crypt $6$, SHA512 (Unix).

I loaded the hash value into a text file that I name hash.txt. So my hash.txt file looked like this:

`$6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.`

I found that this type of hash is mode 1800 in hashcat. I ran the following command to crack it:

`hashcat -m 1800 hash.txt /usr/share/wordlists/rockyou.txt`

##### Hash: e5d8870e5bdd26602cab8dbe07a942c8669e56d6 Salt: tryhackme

CrackStation was unable to instantly break this one. I ran this hash through hashes.com and it thinks the the hash is one of these possible algorithms: SHA1.

I loaded the hash value and salt into a text file that I name hash.txt. The 2 values were separated by a colon (:). So my hash.txt file looked like this:

`e5d8870e5bdd26602cab8dbe07a942c8669e56d6:tryhackme`

I found that this type of hash is mode 160 in hashcat. I ran the following command to crack it:

`hashcat -m 160 hash.txt /usr/share/wordlists/rockyou.txt`
