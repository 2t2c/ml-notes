# Normal Distribution

## Approximation

Models the number of successes $X$ in $n$ independent Bernoulli trials, each with success probability $p$.

$$
P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}
$$

- Given,
    - $X \sim \text{Binomial}(n, p)$
    - Mean: $\mu = np$
    - Variance: $\sigma^2 = np(1 - p) = npq$

**Normal Approximation**

For large $n$, the binomial distribution approximates a normal distribution:

$$
X \approx \mathcal{N}(np, npq)
$$

- Bell curve shape
- Approximation becomes accurate for $n \gtrsim 30$ and moderate $p$
- **Bernoulli Trials**:
    
    Single trial with two outcomes → success (probability $p$) or failure (probability $1 - p$)
    

## Equation

The probability density function (PDF) of a normal (Gaussian) distribution with mean $\mu$ and standard deviation $\sigma$ is:

$$
P(X = x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right)
$$

Where:

- $\mu = n \cdot p$ is the mean (expected value),
- $\sigma^2 = n \cdot p \cdot q$  is the variance,
- $\sigma = \sqrt{n \cdot p \cdot q}$ is the standard deviation,
- $q = 1 - p$ is the probability of failure.

This formula gives a continuous approximation of the binomial distribution when $n$ is large and $p$ is not too close to 0 or 1.

**Descriptive Statistics**

| Type | Formula |
| --- | --- |
| Support | $x \in (-\infty, \infty)$ |
| Mean | $\mathbb{E}[X] = \mu$ |
| Variance | ${Var}(X) = \sigma^2$ |
| Standard Deviation | $\sigma$ |
| Probability Density Function (PDF) | $f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$ |
| Cumulative Distribution Function (CDF) | $F(x) = \mathbb{P}(X \leq x) = \int_{-\infty}^x f(t) dt$ |

## Intuition and Use

- **Why Approximate Binomial with Normal?**
    - Binomial becomes computationally intensive for large $n$
    - **Normal is continuous and easy to compute probabilities for $(e.g., P(20 ≤ X ≤ 50))$. This would be a monster to compute using Binomial distribution.**
    - Better for analysis and visualization
    - Normal distributions have well-known properties for sums, differences, and linear combinations. This makes complex probability problems much more manageable.
- **When Does Approximation Work Well?**
    - $n$ is large (rule of thumb: $n \geq 30$ or so). The distributions agree well with a lot of overlap.
    - $p$ not too close to 0 or 1 (i.e., $np(1 - p)$ not small)
    - Fails when $p$ or $q$ is too small, may predict impossible values (like negative successes)
- **Central Limit Theorem (CLT)**:
    - Sum of many i.i.d. random variables (of any distribution with finite variance) converges to a normal distribution
    - Binomial is a sum of Bernoulli trials → classic CLT case

## **Probability Density Function (PDF) and Cumulative Distribution Function (CDF)**

- PDF describes the probability density at each point xx; area under the curve between two points gives the probability that $X$ lies within that range.
- CDF is the integral of the PDF from $\int_{-\infty}^x f(x) dx$, representing the probability that $X \leq x$.
- The standard normal distribution ($\mu=0, \sigma=1$) is the canonical form, often denoted $\Phi(x)$ for the CDF.

**Calculating Probabilities**

- Probability $P(a \leq X \leq b) = \int_a^b f(x) dx = \Phi(b) - \Phi(a)$, where $f(x)$ is the PDF.
- CDF values can be found using lookup tables historically, now easily computed with Python libraries like SciPy.

**Applying Normal Approximation to Binomial**

- Example: Flip a fair coin 400 times $(n=400, p=0.5)$:
    - Mean $\mu = np = 200$
    - Variance $\sigma^2 = np(1-p) = 100$
    - Standard deviation $\sigma = 10$
- Calculating let’s say getting # of heads between → $P(190 \leq X \leq 230)$ binomially requires summing 51 probabilities, cumbersome to compute directly.
- Using normal approximation, calculate $\Phi(230) - \Phi(190)$ to get probability efficiently.