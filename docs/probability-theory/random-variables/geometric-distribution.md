# Geometric Distribution

## Core Concept

The **Geometric distribution** models the number of **independent** **Bernoulli trials** until the **first success**.

- A **Bernoulli trial** is an experiment with two outcomes: success (1) or failure (0).
- Trials are **independent** (e.g., coin flips, dice rolls).
- The distribution answers: “***What is the probability that the first success occurs on the $n$-th trial?”***

## Definitions

Let:

- $p$ = probability of success on a single trial
- $q = 1 - p$ = probability of failure
- $X$ = number of trials until the first success

Then:

$$
X \sim \text{Geometric}(p)
$$

The **Probability Mass Function (PMF)** is:

$$
\begin{aligned}
P(\text{first success on the } n\text{th trial}) 
&= P(F_1 \cap F_2 \cap \dots \cap F_{n-1} \cap S_n) \\
&= P(F)^{n - 1} \cdot P(S) \quad \\
&= (1 - p)^{n - 1} \cdot p \\
&= q^{n - 1} \cdot p \\
\text{where } q &= 1 - p, \\
\text{and each } F_i &\sim \text{Bernoulli(0), and } S_n \sim \text{Bernoulli(1)})
\end{aligned}
$$

## Intuition

To succeed for the first time on the $n$-th trial:

- First $n - 1$ trials must be failures ($q^{n - 1}$)
- The $n$-th trial must be a success ($p$)

So:

$$
P(X = n) = q^{n - 1} \cdot p = (1 - p)^{n - 1} \cdot p
$$

| Type | Formula |
| --- | --- |
| Support | $x \in \{1, 2, 3, \dots\}$ |
| Mean | $\mathbb{E}[X] = \frac{1}{p}$ |
| Variance | $\text{Var}(X) = \frac{1 - p}{p^2}$ |
| Standard Deviation | $\sigma = \frac{\sqrt{1 - p}}{p}$ |
| PMF (Probability Mass Function) | $\mathbb{P}(X = k) = (1 - p)^{k - 1} p$ |
| CDF (Cumulative Distribution Function) | $\mathbb{P}(X \leq k) = 1 - (1 - p)^k$ |
| Memoryless Property | $\mathbb{P}(X > m + n \mid X > m) = \mathbb{P}(X > n)$ |

## Example

**Question**: What is the probability that it takes **at least 10** rolls of a fair die to roll a **5**?

- Success = rolling a 5
- $p = \frac{1}{6}, q = \frac{5}{6}$
- $X \sim \text{Geometric}\left(\frac{1}{6}\right)$

We want: $P(X \geq 10)$

### Method 1: Summing Infinite Tail

$$
P(X \geq 10) = \sum_{k=10}^{\infty} P(X = k) = \sum_{k=10}^{\infty} q^{k - 1} \cdot p
$$

Factor out $q^9 \cdot p$:

$$
P(X \geq 10) = q^9 \cdot p \cdot \left(1 + q + q^2 + \dots \right)
$$

This is a geometric series, **sum of an infinite geometric series** where:

- The first term is 1,
- The common ratio is $q$,
- And $∣q∣<1$ (so the series converges)

$$
p\sum_{k=0}^{\infty} q^k = \frac{a}{1 - r} = \frac{1}{1 - q} = \frac{1}{p}
$$

So:

$$
P(X \geq 10) = q^9 \cdot p \cdot \frac{1}{p} = q^9
$$

Final answer:

$$
P(X \geq 10) = \left( \frac{5}{6} \right)^9
$$

### Method 2: No Success in First 9 Trials

$$
P(X \geq 10) = P(\text{no success in first 9 trials}) = q^9 = \left( \frac{5}{6} \right)^9
$$

Same result, simpler reasoning.

### **When to Use the Poisson Distribution**

- Number of independent trials until the first success.
- Each trial has the same success probability $p$.
- Trials are independent Bernoulli (success/failure) events.