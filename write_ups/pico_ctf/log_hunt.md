# Challenge Name: Log Hunt
**Category:** General Skills

**Difficulty:** Easy

**Date Completed:** 2026-03-23

---

## 🧠 Objective
Our server seems to be leaking pieces of a secret flag in its logs. The parts are scattered and sometimes repeated. Can you reconstruct the original flag? Download the logs and figure out the full flag from the fragments.

---

## 🔍 Initial Analysis

### What information is given?
There is a log file and part of the flag will be repeated.

### Any files, URLs, or hints?
The file url is provided. I'll need to look for repeated patterns in the file.

### First thoughts / hypotheses
I should look for any lines that have pico in them. That will help me see where the flag might be repeating.

---

## 🛠️ Tools Used
- wget
- grep
---

## 🚶 Approach
Step-by-step process:
1. I downloaded the server.log file.
2. I used grep to see what lines had pico in the server file with the following command: `grep -in 'pico' server.log`. The `-in` makes the search case insensitive and shows what line number matches the pattern.
3. I noticed that lines 1, 728-730, and 1544-1546 match that pattern.
4. The lines all say `INFO FLAGPART` in the log file. I wondered if the other lines would say the same.
5. I ran the following command `grep -in 'flag' server.log`.
6. That got me all the lines that are part of the flag. I copied and pasted them into the answer box.

Include commands:
```bash

grep -in 'pico' server.log
1:[1990-08-09 10:00:10] INFO FLAGPART: picoCTF{us3_
728:[1990-08-09 11:04:27] INFO FLAGPART: picoCTF{us3_
729:[1990-08-09 11:04:29] INFO FLAGPART: picoCTF{us3_
730:[1990-08-09 11:04:37] INFO FLAGPART: picoCTF{us3_
1544:[1990-08-09 12:19:23] INFO FLAGPART: picoCTF{us3_
1545:[1990-08-09 12:19:29] INFO FLAGPART: picoCTF{us3_
1546:[1990-08-09 12:19:32] INFO FLAGPART: picoCTF{us3_

grep -in 'flag' server.log
```
