---
id: 5xy7dh8osgyad4s9ch3gw23
title: Lecture2
desc: ''
updated: 1736368457661
created: 1736368457661
---
# Topic: Algorithm Analysis 1

## Todo:
- no new tasks

## Notes:
### What do we care about?
- Correctness
- Performance:
    - Speed (time complexity)
    - Memory (space complexity)
### How to compare two algorithms
- Evaluate the algorithm itself rather than the implementation/performance of the code
- Consider large inputs, small inputs cause anything to work fine.
### Analyzing Code
- Different Measures
    - Constant time operations (sorta)
        - arithmetic
        - assignment
        - access single java field or array index
    - Consecutive statements: count time of each statement ($t_1 + t_2 + ... + t_n$)
    - Loops: count num iters * time for loop body ($i \cdot t$ )
    - Conditionals: time of condition + slowest branch ($c \cdot s$)
    - Function calls: time of function body
    - Recursion: solve recurrence equation
- Complexity Cases
    - Best Case: min num of steps
    - Worst Case: max num of steps
    - Average Case: DATASET DEPENDENT, avg num of steps on random inputs
    - Amortized Case: total num of steps on sequential inputs / num inputs
### Asymptotic Analysis
### Big-Oh Definition