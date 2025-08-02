# Discrete Random Variables

## **Definition**

A random variable $X$ is **discrete** if it can take on at most a countable number of possible values.

## **Probability Mass Function (PMF)**

For a discrete random variable $X$, the PMF $p(x)$ of $X$ is defined as:

$$
p(x) = P(X = x)
$$

where $p(a) \geq 0$ for countably many values $x$.

- **Properties of PMF:**
    
    If $X$ can take values $x_1, x_2, \ldots$, then:
    
    $$
    p(x_i) \geq 0, \quad i = 1, 2, 3,\ldots
    $$
    
    and $p(x)=0$ for all other $x$ 
    
    Also, the total probability sums to 1: $\sum_{i} p(x_i) = 1$
    
- **Graphical Representation:** The PMF can be graphed by plotting $p(x_i)$ on the y-axis against $x_i$ on the x-axis. In short, a histogram.

### Examples of PMFs

1. Example PMF values:
    
    $$
    p(0) = \frac{1}{4}, \quad p(1) = \frac{1}{2}, \quad p(2) = \frac{1}{4}
    $$
    
2. PMF for sum of two dice rolls (values 2 to 12) follows a known distribution with probabilities such as:
    
    $$
    p(7) = \frac{6}{36}, \quad p(2) = \frac{1}{36}, \ldots
    $$
    

### Example Problem

Given:

$$
p(i) = c \frac{\lambda^i}{i!}, \quad i=0,1,2,\ldots, \quad \lambda > 0
$$

- Find:
    1. $P(X=0)$
    2. $P(X > 2)$

**Solution:**

- Since probabilities sum to 1:
    
    $$
    \sum_{i=0}^\infty p(i) = 1 \implies \sum_{i=0}^\infty c \frac{\lambda^i}{i!} = 1
    $$
    
- Recognize the series for $e^\lambda$:
    
    $$
    c e^\lambda = 1 \implies c = e^{-\lambda}
    $$
    
- So the PMF is:
    
    $$
    p(i) = e^{-\lambda} \frac{\lambda^i}{i!}
    $$
    
1. $P(X=0) = e^{-\lambda} \frac{\lambda^0}{0!} = e^{-\lambda}$
2. $P(X > 2) = 1 - P(X \leq 2) = 1 - \sum_{i=0}^2 e^{-\lambda} \frac{\lambda^i}{i!} = 1 - e^{-\lambda}\left(1 + \lambda + \frac{\lambda^2}{2}\right)$

## Cumulative Distribution Function (CDF) for Discrete Variables

- The CDF $F(a)$ is given by:
    
    $$
    F(a) = P(X \leq a) = \sum_{x_i \leq a} p(x_i)
    $$
    
- If $X$ takes values $x_1 < x_2 < x_3 < \ldots$, then $F$ is a **step function**:
    - FF is constant between points $x_{i-1}$ and $x_i$.
    - At each $x_i$, $F$ jumps by $p(x_i)$.

### Example CDF

Given PMF:

$$
p(1) = \frac{1}{4}, \quad p(2) = \frac{1}{2}, \quad p(3) = \frac{1}{8}, \quad p(4) = \frac{1}{8}
$$

The CDF $F(a)$ is:

$$
F(a) = \begin{cases}
0 & a < 1 \\
\frac{1}{4} & 1 \leq a < 2 \\
\frac{3}{4} & 2 \leq a < 3 \\
\frac{7}{8} & 3 \leq a < 4 \\
1 & a \geq 4
\end{cases}
$$

Each jump size equals the probability at that point.