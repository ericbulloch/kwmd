# Buffer Overflow

## Introduction

A buffer overflow occurs when the stack of a program has assigned a section of memory for a variable and the value that gets placed in that section is more than what was allocated and overwrites what is in the next section(s) of memory. It is a tactic that can change the flow of a program, alter behavior of a program or call other code that is already in memory.

## Program Memory

```txt
+----------------------------+  <-- High address
|        Stack               |  <-- Grows downward
+----------------------------+
|        Heap                |  <-- Grows upward
+----------------------------+
|        Data Segment        |  <-- Global/static variables
+----------------------------+
|        Code Segment        |  <-- Executable instructions
+----------------------------+  <-- Low address
```
