---
id: 4tehy9r57fx8g58o7skhw5x
title: Lecture5
desc: ''
updated: 1736979525823
created: 1736976726958
---
# Topic: Probability examples, Conditioning

## Todo:
- no new tasks

## Notes:
### Probability Space
- Examples
  - Roll 2 fair dice, probability of both dice being even
    - Sample Space: $\{1,2,3,4,5,6\} \times \{1,2,3,4,5,6\}$ 
    - Probability Measure: P(ω) = 1/36 for all $ω \in Ω$
    - Event: $\{2,4,6\} \times \{2,4,6\}$
    - Probability: $\cfrac{3^2}{6^2}$
  - Roll 2 fair dice, probability of both dice being even, always put dice in increasing order
    - Sample Space$\{ 1,1 , 1,2 , 1,3 , 1,4 , 1,5 , 1,6 , 2,2 , 2,3 , 2,4 , 2,5 , 2,6 , 3,3 , 3,4 , 3,5 , 3,6 , 4,4 , 4,5 , 4,6 , 5,5 , 5,6 , 6,6 \}$
  - Shuffle deck of cards so any arrangement is equally likely. What is the probability the the top two cards have the same value?
    - Sample Space: $\{1_a,2_a, ... 52_a \} \times \{1_b,2_b, ... 51_b \}$  
    better way: $\{(x,y): x \text{ and } y \text{ are different cards} \}, 52 \cdot 51$
    - Probability Measure: $P(ω) = \cfrac{1}{52 \cdot 51}$ for all $ω \in Ω$
    - Event: 
    - Probability: $\cfrac{4 \cdot 3 \cdot 13}{52 \cdot 51}$

### Probability Axioms and Consequences
- Axioms
  - $P(x) > 0$ (non-negativity)
  - $\sum_{x \in Ω} P(x) = 1$ (normalization)
  - If E and F are mutually exclusive then $P(E \cup F) = P(E) + P(F)$ (countable additivity)
- Consequences/Corollaries
  - $P(\bar E) = 1 - P(E)$ (complementation)
  - If $E \subseteq F$, then $P(E) \leq P(F)$ (monotonicity) 
  - $P(E \cup F) = P(E) + P(F) - P(E \cap F)$
### Conditional Probability
- For an event B, with P(B) > 0, "Probability of A conditioned on B" is $P(A|B) = \cfrac{P(A \cap B)}{P(B)}$
  - If P(B) = 0, we can't condition on it.
- Example
  - You roll a fair red die and fair blue die, can't see results
    - odds of red = 5? conditioned on sum = 4
      - 0, because that would mean blue = -1 which is impossible
      - Only remaining outcomes after knowing sum = 4 is $\{(1,3), (2,2), (3,1)\}$
  - 