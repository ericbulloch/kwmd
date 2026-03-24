# Challenge Name: Flag in Flame
**Category:** Forensics

**Difficulty:** Easy

**Date Completed:** 2026-03-23

[Back to picoCTF challenges](/write_ups/pico_ctf/)

---

## 🧠 Objective
The SOC team discovered a suspiciously large log file after a recent breach. When they opened it, they found an enormous block of encoded text instead of typical logs. Could there be something hidden within? Your mission is to inspect the resulting file and reveal the real purpose of it. The team is relying on your skills to uncover any concealed information within this unusual log. Download the encoded data here: Logs Data. Be prepared—the file is large, and examining it thoroughly is crucial .

---

## 🔍 Initial Analysis
### What information is given?
The log file is large and contains encoded text.

### Any files, URLs, or hints?
A url to the file.

### First thoughts / hypotheses
Without looking at the file my first thought is that the file is base64 encoded. I'll have to decode the text and then work on the decoded text.

---

## 🛠️ Tools Used
- wget
- wc
- tail
- base64
- head
- CyberChef

---

## 🚶 Approach
Step-by-step process:
1. I downloaded the file. The file is 1.6M in size.
2. I wanted to know how many lines are in the file so I ran the following `wc -l logs.txt`.
3. It said 0 lines, meaning this file is all in one line.
4. I ran `tail logs.txt` and noticed that the text ended with `gg==`.
5. That usually means that the text is base64 encoded.
6. I decoded the text and saved it to another file using the command `cat logs.txt | base64 -d > temp.txt`.
7. The resulting file has 4,181 lines when I ran `wc -l temp.txt`.
8. I wanted to know what the first few lines say so I ran `head temp.txt` and say that it starts with PNG.
9. I renamed the file as temp.png using the following command `mv temp.txt temp.png`.
10. I then opened the file.
11. At the bottom of the file there is a string of letters and numbers.
12. I ran that string of letters and numbers (7069636f4354467b666f72656e736963735f616e616c797369735f69735f616d617a696e675f62396163346362397d) through CyberChef's magic recipe and that output the flag.

Include commands:
```bash
wc -l logs.txt 
0 logs.txt

tail logs.txt

cat logs.txt | base64 -d > temp.txt

wc -l temp.txt
4181 temp.txt

head temp.txt
PNG
...

mv temp.txt temp.png
```
