# Buffer Overflow

## Introduction

A buffer overflow occurs when the stack of a program has assigned a section of memory for a variable and the value that gets placed in that section is more than what was allocated and overwrites what is in the next section(s) of memory. It is a tactic that can change the flow of a program, alter behavior of a program or call other code that is already in memory.

## Program Memory

Modern operating systems will allocate a section of memory for each process. The section of memory will have a high address and a low address. All the memory for the process will fit within the high and low addresses. The section will contain four segments; the stack, the heap, data segment and code segment. It can be visualized like the following:

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
