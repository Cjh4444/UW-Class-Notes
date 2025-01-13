---
id: qafngdhrgvw4747or917vs5
title: Lecture3
desc: ''
updated: 1736800750950
created: 1736541236637
---
# Topic: Lecture 2 Continuation

## Todo:
nothing of note

## Notes:
### Asymptotic Analysis
- $4n + 5 \rightarrow O(n)$
- $0.5nlog(n) + 2n + 7 \rightarrow n log n$
- $n^3 + 2^n + 3n \rightarrow 2^n$
- $n*log(10n^2) \rightarrow n log n$
### Big-Oh Definition
- Big-Oh represents a set of functions
- functions in O(n) describe functions with asymptotic behavior less than or equal f(n)

more notes that i need to rewatch lecture for since i spaced out

- Examples/Practice
    - 4 + 3n is O(n) TRUE
    - n + 2logn is O(logn) FALSE
    - logn + 2 is O(1) FALSE
    - n^50 is O(1.1^n) TRUE

### Asymptotic Notation
- Big Oh
    - Upper bound: O(f(n)) is set of functions less than or equal to f(n)
- Big Omega
    - Lower bound: Ω(f(n)) is set of functions greater than or equal to f(n)
- Big Theta
    - Tight bound: Θ(f(n)) is set of functions equal to f(n)
    - Intersection of Big Oh and Big Omega