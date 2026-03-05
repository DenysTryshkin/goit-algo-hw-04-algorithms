## Introduction

Recursion, as a key aspect of programming, opens the door to limitless possibilities and is used in a wide range of tasks. In this homework assignment, you will gain skills in creating recursive algorithms and applying recursive methods to solve problems.

During this assignment you will:

- perform recursive sorting of files in a directory, which will help expand your file system management skills and understand how recursion can be used to process structured data;
- visualize the **Koch Snowflake** fractal using recursion and explore the potential of recursive algorithms for generating complex structures;
- compare three different sorting algorithms and evaluate their efficiency on different datasets.

To measure execution time of the algorithms, the **timeit** module should be used.

Studying how these algorithms work and comparing them will help understand why programmers most often use built‑in algorithms instead of implementing their own.

---

# Homework Description

## Task 1

Write a Python program that recursively copies files from the source directory, moves them to a new directory, and sorts them into subdirectories whose names are based on file extensions.

### Requirements

1. **Argument parsing**
   The script must accept two command‑line arguments:
   - path to the source directory
   - path to the destination directory

   If the destination directory is not provided, it should be created with the default name **dist**.

2. **Recursive directory traversal**
   You need to implement a function that:
   - accepts a directory path as an argument;
   - iterates through all elements in the directory;
   - if an element is a directory — the function calls itself recursively;
   - if an element is a file — the file should be processed for copying.

3. **File copying**
   For each file type, a new path must be created in the destination directory.

   The name of the subdirectory should be based on the **file extension**.

   The file must be copied into the corresponding subdirectory.

4. **Exception handling**
   The code must properly handle possible exceptions, for example:
   - file access errors;
   - directory access errors;
   - other system errors.

---

## Task 2

Write a Python program that uses recursion to generate the **Koch Snowflake** fractal.

### Requirements

1. The program must run correctly.
2. The user must be able to **specify the recursion level**.
3. The program should display a **visualization of the fractal**.

---

## Task 3

Python has two built‑in sorting functions: **sorted()** and **list.sort()**.

These functions use the **Timsort** algorithm — a hybrid sorting algorithm that combines:

- Merge Sort
- Insertion Sort

### Task

Compare three sorting algorithms by execution time:

- Merge Sort
- Insertion Sort
- Timsort (Python built‑in sorting)

### Requirements

1. Perform a **comparative analysis** of the algorithms based on execution time.
2. Use **different datasets**.
3. Use the **timeit** module to measure execution time.
4. Empirically verify the theoretical complexity estimates of the algorithms.
5. Demonstrate that combining Merge Sort and Insertion Sort makes **Timsort significantly more efficient**.

Based on the analysis results, you must **draw conclusions**.

---

# Homework Acceptance Criteria

The acceptance criteria are a **mandatory condition for evaluation**. If at least one criterion is not met, the homework will be returned for revision.

If you encounter difficulties or need clarification, contact your mentor via **Slack**.

---

## Criteria for Task 1

1. The script accepts two command‑line arguments:
   - path to the source directory;
   - path to the destination directory.

2. **Recursive directory traversal** is implemented.

3. A **separate subdirectory based on file extension** is created for each file type.

4. **Exception handling** is implemented.

5. After the program runs, all files are recursively copied and **sorted by extension**.

---

## Criteria for Task 2

1. The code runs correctly.
2. The program visualizes the **Koch Snowflake fractal**.
3. The user can **specify the recursion level**.

---

## Criteria for Task 3

1. A **comparative analysis of sorting algorithms** is performed.
2. **Empirical testing results** are obtained.
3. The efficiency of **Timsort** is confirmed.
4. **Conclusions** are written and included in the **README.md** file.

---
