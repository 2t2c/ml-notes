# Expectation of a Function of a Random Variable

### Understanding Expectation of a Function g(X)

We often want to calculate the expected value of a function applied to a discrete random variable, written as **$E[g(X)]$**, where:

- **$X$** is a discrete random variable with known probability mass function (pmf) **$p(x)$**
- **g$(X)$** is any real-valued function defined on the values taken by $X$

### Key Principle

The expectation of $g(X)$ is calculated as a weighted average of $g(x)$, weighted by the probability of each corresponding $x$:

$$
E[g(X)]= \sum_{x} g(x) \cdot p(x)
$$

This means:

If $X$ takes values $x_1, x_2, \ldots$ with probabilities $p(x_1), p(x_2), \ldots$, then:

$$
E[g(X)]=\sum_i g(x_i) \cdot p(x_i)
$$

### Example

Let $X$ take values $-1, 0, and 1$ with:

- P$(X = -1) = 0.2$
- $P(X = 0) = 0.5$
- $P(X = 1) = 0.3$

We want to compute **$E[X²]$**.

Let $g(X) = X²$. Then:

- $g(-1) = 1$
- $g(0) = 0$
- $g(1) = 1$

Now use the expectation formula:

$$
E[X^2] = 1 \cdot 0.2 + 0 \cdot 0.5 + 1 \cdot 0.3 = 0.5
$$

### Application: Maximizing Expected Profit

**Scenario**: A store stocks a seasonal product.

- Selling a unit earns **$b$** dollars.
- Unsold units incur a loss of **$ℓ$** dollars per item.

Let **$X$** = number of units ordered by customers (a random variable with pmf $p(i)$)

Let **$s$** = number of units stocked

Then the expected profit **$E[P(s)]$** is computed by breaking it into two cases:

- If demand ≤ stock:

$$
P(s) = bX - (s - X)\ell
$$

- If demand > stock:
    
    $$
    P(s) = sb
    $$
    

Combining these:

$$
E[P(s)] = \sum_{i=0}^s [bi - (s - i)\ell]p(i) + \sum_{i=s+1}^\infty sb \cdot p(i)
$$

To find the optimal stocking level **$s*$**, compute the value of **$s$** that satisfies:

$$
\sum_{i=0}^s p(i) < \frac{b}{b + \ell}
$$

---

### Utility Theory (Decision Under Uncertainty)

Suppose you must choose between two actions. Each leads to one of several consequences $C_1, C_2, \ldots, C_n$, each with associated probabilities $p_i$ (action 1) and $q_i$ (action 2).

We define the **utility** $u(C_i)$ of consequence $C_i$ as the value uu for which the decision-maker is indifferent between:

- receiving $C_i$, or
- taking a gamble with outcome:
    - best consequence CC with probability uu
    - worst consequence cc with probability $1 - u$

Then the expected utility of an action is:

$$
\sum_{i=1}^n p_i \cdot u(C_i)
$$

Choose the action with the **higher expected utility**.

### Linear Property of Expectation (Corollary)

If a and b are constants:

$$
E[aX + b] = aE[X] + b
$$

This linearity property is useful in many calculations.

### Moments

- **Mean (First Moment)**: $E[X]$
- **nth Moment**: $E[X^n] = \sum_x x^n \cdot p(x)$

These moments are used to understand the shape and variability of a distribution.