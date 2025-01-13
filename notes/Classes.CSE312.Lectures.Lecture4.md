---
id: fgdaalczglbwgzed7hsdel0
title: Lecture4
desc: ''
updated: 1736806879918
created: 1736804096362
---
# Topic: Wrap-up Counting; Probability Definitions

## Todo:
- [ ]

## Notes:
### Pigeonhole Principle
- If you have 5 pigeons and 4 holes, 1 hole must have at least 2 pigeons
- Strong Variation
  - if you have $n$ pigeons and $k$ holes then there is at least one pigeonhole with at least $\lceil \frac{n}{k} \rceil$ pigeons

### Stars and Bars
- To pick $n$ objects from $k$ groups (where order doesn’t matter and every element of each group is indistinguishable), use the formula: $\begin{pmatrix} n+k+-1 \\ k-1 \end{pmatrix}$

### Probability
- Way of quantifying uncertainty when more than one outcome is possible
  - A probability is a number between 1 and 0 describing how likely an outcome is
- Sample Space
  - Set of all possible outcomes (denoted by Ω)
  - Examples
    - Single coin flip: Ω = {H, T}
    - Double coin flip: Ω = {HH,HT,TH,T}
    - Rolling single die: Ω = {1,2,3,4,5,6}
- Event
  - Subset of possible outcomes $E \subseteq Ω$
  - Examples
    - At least 1 head among two coin flips: E = {HH,HT,TH}
    - Even number on die roll: E = {2,4,6}
- Probability Example
  - Toss one fair coin
    - P(H) = P(T) = 0.5
  - Toss one biased/unfair coin
    - P(H) = 0.85, P(T) = 0.15
- Probability Space
  - pair (Ω, P) where Ω is sample space and P is probability
 