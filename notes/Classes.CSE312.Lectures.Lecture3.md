---
id: ijswo499551xzslgo51z8ff
title: Lecture3
desc: ''
updated: 1736546503670
created: 1736544972373
---
# Topic: Even More Counting

## Todo:
no new tasks

## Notes:
### Overcounting
- For anagrams of words with multiple letters, divide n! where n is the number of letters in the word by $a! \cdot b! ...$ for each group of duplicate letters
- Multinomial coefficient alternate notation:
    - $\begin{pmatrix} 7 \\ 2,3 \end{pmatrix} = \frac{7!}{2!3!}$
### Combinations
- Symmetry of Combinations
    - $\begin{pmatrix} n \\ k \end{pmatrix} = \begin{pmatrix} n \\ n-k \end{pmatrix}$
- Pascal's Rule
    - $\begin{pmatrix} n \\ k \end{pmatrix} = \begin{pmatrix} n - 1 \\ k - 1 \end{pmatrix} + \begin{pmatrix} n - 1 \\ k  \end{pmatrix}$
### Binomial Theorem
- $(x+y)^n = \sum_{i=0}^{n} \begin{pmatrix} n \\ i \end{pmatrix} = x^iy^{n-i}$