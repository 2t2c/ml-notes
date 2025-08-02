# Cumulative Distribution Function (CDF)

## What is CDF?

A **Cumulative Distribution Function (CDF)** of a continuous random variable $X$ gives the **total probability accumulated** up to and including a specific value $x$. It answers:

> “What is the probability that $X \leq x$?”
> 

### Interpretation

- $F_X(x)$ is the **area under the PDF curve** from $-\infty$ to $x$.
- It shows how much probability has **accumulated** up to that point.
- The CDF is **non-decreasing** and always lies in the range $[0, 1]$.
- For small values $x$, $F_X(x) \approx 0$; for large values, $F_X(x) \approx 1$.

## Properties

| **Property** | **Description** |
| --- | --- |
| **Monotonicity** | $F_X(x_1) \leq F_X(x_2)$ for $x_1 < x_2$ |
| **Limits** | $\lim_{x \to -\infty} F_X(x) = 0$, $\lim_{x \to \infty} F_X(x) = 1$ |
| **Range** | $0 \leq F_X(x) \leq 1$ |
| **Continuity** | $F_X(x)$ is continuous from the right |

## Relationship to PMF/PDF

The CDF and PMF/PDF are tightly connected:

- To get the **PMF**:

$$
p_X(x) = F_X(x) - F_X(x^{-}) = \mathbb{P}(X = x)
$$

- To get the **PDF**, differentiate the CDF:

$$
f_X(x) = \frac{d}{dx} F_X(x)
$$

## Example

Let $X \sim \mathcal{N}(165, 10^2)$ be a normal distribution modeling women’s heights with:

- Mean $\mu = 165$
- Standard deviation $\sigma = 10$

Then:

- $F_X(160) \approx 0.31$: 31% of women are shorter than 160 cm.
- $F_X(175) \approx 0.84$: 84% are shorter than 175 cm.

The CDF increases smoothly from 0 to 1, reflecting accumulated probability.