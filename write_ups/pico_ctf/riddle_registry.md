# Challenge Name: Riddle Registry
**Category:** Forensics

**Difficulty:** Easy

**Date Completed:** 2026-03-22

---

## 🧠 Objective
Hi, intrepid investigator! 📄🔍 You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as it appears. Amidst the chaos lies a hidden treasure—an elusive flag waiting to be uncovered. Find the PDF file here Hidden Confidential Document and uncover the flag within the metadata.

---

## 🔍 Initial Analysis
- What information is given?
There is a pdf file that is not working correctly. It seems to be filled with nonsense.

- Any files, URLs, or hints?
A link to the PDF is provided

- First thoughts / hypotheses
Opened the pdf and some of the context is blanked out. The flag might be behind the blanked out content.

---

## 🛠️ Tools Used
- wget
- strings
- exiftool
- echo
- base64
- CyberChef

---

## 🚶 Approach
Step-by-step process:
1. Opened up the PDF file.
2. Observed that some of the text is masked.
3. Tried to copy and past the masked text to see what was behind it.
4. None of the masked text had the flag.
5. Opened up the picoCTF Webshell and downloaded the file with the command `wget https://challenge-files.picoctf.net/c_amiable_citadel/570d726d77600d7540c9a8fe7df9e37f4e8b05fafe16f2b316f4a0603dfa7d2f/confidential.pdf`
6. Tried running the following command to get the flag `strings confidential.pdf | grep 'pico'`
7. Still no flag.
8. Experience has taught me to look at the metadata for a file.
9. I ran the following command to get the metadata `exiftool confidential.pdf`
10. I observed the following: `Author                          : cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9mOTQzMDBjNH0=`
11. That value is base64 encoded. I the following command: `echo 'cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9mOTQzMDBjNH0' | base64 -d`. You can also use CyberChef for this.

Include commands:
```bash
wget https://challenge-files.picoctf.net/c_amiable_citadel/570d726d77600d7540c9a8fe7df9e37f4e8b05fafe16f2b316f4a0603dfa7d2f/confidential.pdf

exiftool confidential.pdf
...
Author                          : cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9mOTQzMDBjNH0=
...

echo 'cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9mOTQzMDBjNH0' | base64 -d
picoCTF{puzzl3d_m3tadata_f0und!_f94300c4}
```
