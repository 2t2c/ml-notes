# Expectation

## **Definition**

### Discrete Case

For a **discrete** random variable $X$ with probability mass function $p(x)$, the expected value (or mean) is:

$$
E[X] = \sum_{x} x \cdot P(X = x) = \sum_{x} x \cdot p(x)
$$

It represents a **weighted average** of all possible values of $X$, where the weights are the probabilities. A **normal (arithmetic) average** is a special case when all values are equally likely.

### Continuous Case

For a **continuous** random variable $X$ with probability density function $f_X(x)$, the expected value is:

$$
E[X] = \int_{-\infty}^{\infty} x \cdot f_X(x) \, dx
$$

It is the **probability-weighted average** over a continuous range of outcomes.

### **Equal Probabilities (Avg.)**

If PMF is given by $p(0) = p(1) = \frac{1}{2}$:

$$
E[X] = 0 \cdot \frac{1}{2} + 1 \cdot \frac{1}{2} = \frac{1}{2}
$$

### **Unequal Probabilities (Weighted Avg.)**

If $p(0) = \frac{1}{3},\ p(1) = \frac{2}{3}$:

$$
E[X] = 0 \cdot \frac{1}{3} + 1 \cdot \frac{2}{3} = \frac{2}{3}
$$

### **Frequency Interpretation**

- In repeated trials, the long-run average value of $X$ converges to $E[X]$.
- Example: If $X$ represents winnings in a game, $E[X]$ is the **average winnings per game** over time.

## Difference to Arithmetic Mean

Expectation is a theoretical, probability-weighted average defined for a random variable based on its distribution. Whereas, mean is a sample-based average of observed values. In expectation, the values are not samples but possible outcomes of a random variable.

$$
  \bar{x} = \frac{1}{n} \sum_{i=1}^n x_i
$$

Expectation does **not** require a sample, it is defined over the probability model.

- **True mean** = **Expectation** of the random variable (exact, theoretical average).
- **Sample mean** = average from observed data (an **estimate** of the true mean).
- If the **expectation of the sample mean** (over all possible samples) equals the **true mean**, so the sample mean is an **unbiased estimator**.

## Examples

### **Fair Die**

Let $X$ be the result of rolling a fair 6-sided die:

$$
E[X] = \sum_{i=1}^{6} i \cdot \frac{1}{6} = \frac{1+2+3+4+5+6}{6} = \frac{21}{6} = 3.5
$$

### **Indicator Variables**

Let $I$ be an indicator variable for event $A$:

$$
\begin{cases}
1, & \text{if } A \text{ occurs} \\
0, & \text{otherwise} (A^c)
\end{cases}
$$

Then: $E[I] = P(A)$

### **Bus Paradox**

A student is selected at random from a group on 3 buses:

- 36, 40, and 44 students on each bus respectively
- Let $X$ be the size of the bus that the student is on

$$
P(X = 36) = \frac{36}{120},\quad P(X = 40) = \frac{40}{120},\quad P(X = 44) = \frac{44}{120}
$$

$$
E[X] = 36 \cdot \frac{3}{10} + 40 \cdot \frac{1}{3} + 44 \cdot \frac{11}{30} = 40.27
$$

- Average bus size: $\frac{120}{3} = 40$
- **Expected size is higher** than average due to higher chance of picking a student from a larger bus (sampling bias)