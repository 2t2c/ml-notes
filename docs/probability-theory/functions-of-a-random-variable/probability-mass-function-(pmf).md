# Probability Mass Function (PMF)

## What is PMF?

The PMF is a function that gives the probability of each possible discrete outcome for a random variable.

- **Applies to**: Discrete random variables
- **Notation**: $P(X = x)$
- **Requirements**:
    - $0 \leq P(X = x) \leq 1$
    - $\sum_x P(X = x) = 1$

### Example: Fair Die Roll

A 6-sided die has possible outcomes ${1, 2, 3, 4, 5, 6}$.
Since it is fair:

$P(X = x) = \frac{1}{6} \quad \text{for } x = 1,2,3,4,5,6$

This is a **uniform PMF**.

### Interpretation

- **Each bar** in a PMF plot represents the **exact probability** of that outcome.
- **No area under curve**: Unlike PDFs, we do not interpret PMFs as densities or areas.
- **Sum of bars** must always equal 1: This is a sanity check for correctness.

## Properties

| Property | Description |
| --- | --- |
| Discreteness | Only defined for countable outcomes (e.g., integers) |
| Additivity | Total probability over all outcomes is 1 |
| Visual Form | Bar graph showing probability for each outcome |
| Non-zero values | Only defined at discrete points; between values, probability is 0 |

## Modified Example: Rigged Die

Let’s say the die cannot roll 3 or 4. Then a new PMF could be:

- $P(X = 1) = 0.25$
- $P(X = 2) = 0.25$
- $P(X = 3) = 0$
- $P(X = 4) = 0$
- $P(X = 5) = 0.25$
- $P(X = 6) = 0.25$

Sum still equals 1, but the distribution is **non-uniform** and has **zero mass** at 3 and 4.

### Common Examples

- **Bernoulli** (1 trial, 2 outcomes):

$$
P(X = 1) = p,\quad P(X = 0) = 1 - p
$$

- **Binomial** (n trials):
    
    $$
    P(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}
    $$
    
- **Geometric**, **Poisson**, **Hypergeometric**: All have well-defined PMFs.

## Mean and Variance

- **Expectation (Mean)**:
    
    $$
    \mathbb{E}[X] = \sum_x x \cdot P(X = x)
    $$
    
- **Variance**:
    
    $$
    \text{Var}(X) = \mathbb{E}[(X−μ)^2] = \sum_x (x - \mathbb{E}[X])^2 \cdot P(X = x)
    $$
    

## Relationship to CDF

CDF accumulates the PMF up to a given value:

$$
F(x) = P(X \leq x) = \sum_{k \leq x} P(X = k)
$$

Example:

- $F(4) = P(X \leq 4) = P(1) + P(2) + P(3) + P(4)$

If 3 and 4 are rigged (0 probability), the CDF is flat between 2 and 5.