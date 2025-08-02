# Random Variables

## What

A **random variable** is a variable used in probability and statistics that can take on a set of possible values. Each possible value of the random variable is associated with a probability. For example, if you flip a fair coin four times, the random variable $X$ could be the number of heads obtained, which can be 0, 1, 2, 3, or 4.

Random variables can be:

- **Discrete**: They take on distinct, separate values (e.g., number of heads in coin flips).
    - $X$ ~ $Binomial \quad (P_x)$
- **Continuous**: They can take on any value within a range (e.g., height of people, temperature).
    - $X$ ~ $Gaussian\quad(\mathcal{N})$
- $P(X)$ is called a distribution
    - define values of $X$ (i.e. range and domain).
    - Probability $P$ of each possible value of $X$.

## How

1. Define the **sample space** $\Omega$, which is the set of all possible outcomes (e.g., all sequences of heads and tails for four coin flips).
2. Define the random variable $X$ as a function from the sample space to the set of possible values (e.g., number of heads in the sequence).
3. Assign probabilities to each possible value of $X$. For the coin flips, this follows a **binomial distribution**:
    
    $$
    P(X = k) = \binom{4}{k} \left(\frac{1}{2}\right)^k \left(\frac{1}{2}\right)^{n-k}
    $$
    
    where $k = 0, 1, 2, 3, 4$.
    
4. Represent this distribution visually, such as with a histogram showing probabilities for each value of $X$.
5. For continuous random variables, use a **probability density function (PDF)**, which can be integrated over intervals to find probabilities.

## Why

- Random variables provide a **concise way to summarize complex probability spaces**. Instead of listing every possible outcome (which can be huge, e.g., flipping 100 coins), you describe the distribution of the variable (like number of heads).
- Using random variables allows you to **compute probabilities easily** using known distributions (binomial, normal, etc.) without enumerating all outcomes.
- Random variables enable **hypothesis testing and parameter estimation** with data, such as testing if data follows a binomial or normal distribution and estimating distribution parameters from samples.
- You can **visualize and compute** with random variables, including expected values, variances, and probabilities within intervals.
- They support advanced calculations like **integrals or sums over probability distributions** for continuous or discrete variables.
- You can build and apply **functions on random variables**, propagating uncertainty through systems and performing statistical or engineering analyses.

### Example

- Flip a fair coin 4 times:
    - Sample space $\Omega$ has 16 outcomes (e.g., HHHH, HHHT, ... TTTT).
    - Random variable $X = \text{number of heads}$, $x = \text{values can be 0 to 4}$.
- Probability distribution of $X$:
    
    $$
    P(X=0) = \frac{1}{16},\quad P(X=1) = \frac{4}{16},\quad P(X=2) = \frac{6}{16},\quad P(X=3) = \frac{4}{16},\quad P(X=4) = \frac{1}{16}
    $$
    
- Plotting these probabilities creates a binomial distribution histogram.

This abstraction helps summarize and compute probabilities efficiently without listing all outcomes.

## Sections

[Discrete Random Variables](https://www.notion.so/Discrete-Random-Variables-22f81ba4f78a801d8ac6f22d79bf2ae7?pvs=21)

[Expectation of a Function of a Random Variable](https://www.notion.so/Expectation-of-a-Function-of-a-Random-Variable-22f81ba4f78a801f93ecf832bb71b25f?pvs=21)

[Bernoulli and Binomial Variables](https://www.notion.so/Bernoulli-and-Binomial-Variables-23181ba4f78a801b9938f8db23a0e3c5?pvs=21)

[Poisson Distribution](https://www.notion.so/Poisson-Distribution-23381ba4f78a8042a1fed4b2ce63e9b6?pvs=21)

[Geometric Distribution](https://www.notion.so/Geometric-Distribution-23481ba4f78a80979575d90a2aed1e30?pvs=21)