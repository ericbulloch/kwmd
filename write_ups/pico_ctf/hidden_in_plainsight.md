# Challenge Name: Hidden in plainsight
**Category:** Forensics

**Difficulty:** Easy

**Date Completed:** 2026-03-23

---

## 🧠 Objective
You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag. Download the jpg image here.

---

## 🔍 Initial Analysis
- What information is given?
A link to a jpg image and a hint that the information is hidden in plain site.

- Any files, URLs, or hints?
The url for the image.

- First thoughts / hypotheses
The metadata or some kind of stenography is at play with this one.

---

## 🛠️ Tools Used
- wget
- exiftool
- steghide

---

## 🚶 Approach
Step-by-step process:
1. Downloaded the file.
2. Ran the following command `exiftool img.jpg`.
3. Saw that the comment field had the following: `Comment                         : c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9`.
4. That comment value looks like base64 so I ran the following command: `echo 'c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9' | base64 -d`.
5. That output the following: `steghide:cEF6endvcmQ=`.
6. It looks like they want me to use steghide on this file. The part after the colon is a base64 value. I decoded it with the following command: `echo 'cEF6endvcmQ=' | base64 -d`.
7. This output the value `pAzzword`.
8. Now I ran the following command: `steghide extract -sf img.jpg`.
9. It asked for a password and I entered `pAzzword`.
10. That wrote out a file called flag.txt.
11. I ran the following command to get the value of the file: `cat flag.txt`.

Include commands:
```bash

exiftool img.jpg
...
Comment                         : c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9
...

echo 'c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9' | base64 -d
steghide:cEF6endvcmQ=

echo 'cEF6endvcmQ=' | base64 -d
pAzzword

steghide extract -sf img.jpg
Enter passphrase: 
wrote extracted data to "flag.txt".

cat flag.txt
```
