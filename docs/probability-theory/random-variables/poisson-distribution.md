# Poisson Distribution

## **Poisson Approximation to the Binomial Distribution**

### **When Normal Approximation Fails**

- **Binomial Distribution**: Models the number of successes in $n$ independent Bernoulli trials with success probability $p$.
- For large $n$ and **moderate** $p$, the binomial converges to a **normal distribution**.
- However, if $p$ is **very small or very large**, the **normal approximation becomes inaccurate**:
    - Example: If $n = 1000, p = \frac{1}{1000}$, then mean $\mu = 1$ and std. dev. $\sigma = 1$, but normal approximation will assign ~16% probability to $X < 0$, which is **non-physical**. Meaning you can’t have negative number of coin flips or dice rolls or probability in general.

### **Poisson Distribution as the Fix**

- The **Poisson distribution** provides a better approximation for rare events (small $p$, large $n$, with $\lambda = np$ fixed).
- **Key condition**: $n \to \infty$, $p \to 0$, such that $\lambda = np$ remains constant.

## **Deriving the Poisson Distribution**

Given  $X \sim \text{Binomial}(n, p)$, with $\lambda = np$, and as $n \to \infty, p \to 0$:

$$
\mathbb{P}(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}
$$

Substitute $p = \lambda/n$, then in the limit:

$$
\begin{align*}
P\{X = k\} 
&= \frac{n!}{(n - k)! \, k!} \, p^k \, (1 - p)^{n - k} \\
&= \frac{n!}{(n - k)! \, k!} \cdot \left( \frac{\lambda}{n} \right)^k \cdot \left(1 - \frac{\lambda}{n} \right)^{n - k} \\
&= \frac{n(n - 1) \cdots (n - k + 1)}{k!} \cdot \left( \frac{\lambda}{n} \right)^k \cdot \left(1 - \frac{\lambda}{n} \right)^n \cdot \left(1 - \frac{\lambda}{n} \right)^{-k} \\
&=\frac{\lambda^k}{k!} \cdot \frac{ n(n− 1) \dots (n− k + 1)}{n^k} \cdot\left(1 - \frac{\lambda}{n} \right)^n \cdot \left(1 - \frac{\lambda}{n} \right)^{-k}
\end{align*}
$$

$$
\text{Now, for large } n \to \infty \text{ and moderate } \lambda:  
$$

$$
\begin{align*}
\left(1 - \frac{\lambda}{n} \right)^n &\approx e^{-\lambda} \quad \frac{ n(n− 1) \dots (n− k + 1)}{n^k} &\approx 1 \quad
\left(1 - \frac{\lambda}{n} \right)^k \approx 1
\end{align*}
$$

$$
\text{Hence, for large } n \text{ and moderate } \lambda:
$$

$$
\begin{align*}
P\{X = k\} &\approx \frac{\lambda^k}{k!} e^{-\lambda}
\end{align*}
$$


Where,

- $k$ is the **number of events** (e.g. emails, calls, arrivals) that occur in a **fixed time interval**.
    - It must be a **non-negative integer**: $k = 0, 1, 2, 3, …$
- $\lambda$ (lambda) is the **expected number of events** in the time interval.
    - It is both the **mean** and the **variance** of the Poisson distribution.

This is the **Poisson distribution**. If you perform $n$ independent trials where each trial has a success probability $p$, then when $n$ is large and $p$ is small so that the product $np$ remains moderate, the number of successes can be well approximated by a Poisson random variable with parameter $\lambda = np$. This parameter $\lambda$, which corresponds to the expected number of successes, is often determined from data.

Examples of random variables that typically follow the Poisson distribution include:

1. The number of misprints on a page (or a set of pages) in a book.
2. The number of people in a population who live to age 100 **(rare)**.
3. The number of incorrect phone numbers dialed in one day.
4. The number of dog biscuit packages sold in a store daily.
5. The number of customers visiting a post office in a day.
6. The number of job vacancies in the federal judiciary in a year.

**Derivative Statistics**

| Type | Formula |
| --- | --- |
| Support | $x \in \{0, 1, 2, \dots\}$ |
| Mean | $\mathbb{E}[X] = \lambda$ |
| Variance | $\text{Var}(X) = \lambda$ |
| Standard Deviation | $\sigma = \sqrt{\lambda}$ |
| PMF (Probability Mass Function) | $\mathbb{P}(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$ |

### **When to Use the Poisson Distribution**

- Use when events are:
    - Rare (small $p$)
    - Numerous opportunities (large $n$)
    - Independent occurrences
    - or Failure probability is low and you need to be reliable
- Examples:
    - Number of defective products in a factory
    - Number of emails received per minute
    - Number of light failures in a large building per day

### **Example**

- Suppose:
    - $p = 0.002$ (failure rate)
    - $n = 10,000$ lights
    - Then $\lambda = np = 20$
- The number of failures per day (super rate):
    
    $$
    X \sim \text{Poisson}(\lambda = 20)
    $$
    
- You can now compute $\mathbb{P}(X = k)$ using the Poisson formula.