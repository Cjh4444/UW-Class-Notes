---
id: lr2zs38d5g954ylsoij0q5j
title: Lecture2
desc: ''
updated: 1736737189249
created: 1736371992132
---
# Topic: More Counting

## Todo:
- [ ] HW1 - DUE Wednesday, Jan 15

## Notes:
- Factorial definition:
    - $n! = n \cdot (n - 1) \cdot (n - 2) \cdot \cdot \cdot 1$ 
    - n is a natural number
- k-permutation definition
    - Number of k-element sequences of distinct symbols form a universe of n symbols
    - $P(n,k) = n \cdot (n - 1) \cdot (n - 2) \cdot \cdot \cdot (n - k + 1) = \frac{n!}{(n-k)!}$
    - Pronunciations:
        - "P n k"
        - "n permute k"
        - "n pick k"
    - Alt notation: ${}_{n}P_{k}$
    - Edges:
        - P(n, n) = n!
        - P(n, 0) = 1
        - k < 0 or k > n are undefined
- k-combination definition
    - Number of k-element subsets from a set of n symbols
    - $C(n,k) = \frac{P(n,k)}{n!} = \frac{n!}{k!(n-k)!}$
    - Pronunciations:
        - "n choose k"
        - "n combination k"
    - Notations
        - ${}_{n}C_{k}$
        - $\begin{pmatrix} n \\ k \end{pmatrix}$
        - $C(n,k)$
