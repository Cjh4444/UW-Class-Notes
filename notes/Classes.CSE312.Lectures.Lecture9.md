---
id: g9290iuygou4gsugaswbqk9
title: Lecture9
desc: ''
updated: 1738016297880
created: 1738013714275
---
# Topic: Random Variables

## Todo:
- none

## Notes:
### Random Variable
- Definition
  - $X: \Omega \rightarrow \Reals$ is a random variable
  - $X(\omega)$ is the summary of the outcome $\omega$
  - Informally: a random variable summarizes the important (numerical) information of your outcome
- Example
  - Events
    - $E_2$ = Sum of dice is 2
    - $E_3$ = Sum of dice is 3
    - ...
    - $E_12$ = Sum of dice is 12
  - Random Variable
    - $X: \Omega \rightarrow \Reals$
    - X is the sum of the 2 dice
- From one sample space, many random variables can be defined
  - Example
    - D is the difference between the dice rolls
    - S is the sum
    - M is the maximum
- Capital letters for random variables, lowercase letters for values they could take on
  - Formally random variables are functions, so X = 2 technically means X(H, H, T) = 2, but the former is used for simplicity
### Support ($\Omega_X$) 
- Definition
  - The support is the range of the values a random variable can take
  - Examples
    - D has support {-5,-4,-3...,4,5} 
    - S has support {2,3,...,11,12} 
    - M has support {1,2,...,5,6}
### Probability Mass Function
- Often interested in the even $\{\omega: X(\omega) = x\}$
  - which means the event that X = x
- Use $\mathbb{P}(X=x)$ to describe probability of event
  - Example
    - $\mathbb{P}(S=2) = \frac{1}{36}$
    - $\mathbb{P}(S=7) = \frac{1}{6}$
- $\mathbb{P}(X=x)$ is known as the probability mass function
  - often written as $P_X(x)$
- A random variable partitions $\Omega$
- Example
  - 20 balls, 3 picked without replacement, X is largest value among three balls
### Cumulative Distribution Function
- Definition
  - Gives probability X ≤ x
    - Formally: $\mathbb{P}(\{\omega: X(\omega) \leq x\})$
    - Often written: $F_X(x) = \mathbb{P}(X \leq x)$
### Expectation
- Definition
  - the expectation (expected value) of random variable X is $\mathbb{E}[X] = \sum_k k \cdot \mathbb{P}(X=k)$
    - Intuition: weighted average of values X could take on
      - weighted by probability you actually see them
- Examples 
  - flip fair coin twice, X is number of heads
    - $\Omega = \{TT, TH, HT, HH\}$, $\mathbb{P}()$ is uniform measure
    - $\mathbb{E}[X] = \frac{1}{4} \cdot 0 + \frac{1}{2} \cdot 1 + \frac{1}{4} \cdot 2 = 1$
  - biased die, 6 prob of 1/3, 1-5 with prob of 2/15
    - $\mathbb{E}[X] = \frac{1}{3} \cdot 6 + \frac{2}{15} \cdot 5 + \frac{2}{15} \cdot 4 + \frac{2}{15} \cdot 3 + \frac{2}{15} \cdot 2 + \frac{2}{15} \cdot 1 = 2 + \frac{2(5+4+3+2+1)}{15} = 2 + \frac{30}{15} = 4$
