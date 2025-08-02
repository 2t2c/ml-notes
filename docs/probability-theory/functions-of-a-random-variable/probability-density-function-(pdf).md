# Probability Density Function (PDF)

## What is PDF?

A **Probability Density Function** (PDF) describes the **relative likelihood** that a continuous random variable takes on a value **within a small interval**. Unlike discrete distributions where probabilities are assigned to exact values, the PDF defines a **density**, not an exact probability at a single point.

### Interpretation

- The **height** of the PDF at a point does **not** represent the probability of that exact value. This means $P(X=x)=0$ because the set containing just one point has no width, so the "area" under the PDF at exactly $𝑥$ is zero.
- Instead, it represents the **density** of the distribution or likelihood. Density is how concentrated/densely packed the probability is at a point.
- The **probability** of landing within a small range $[x, x+\delta]$ is approximately:
    
    $$
    P(x \leq X \leq x+\delta) \approx f_X(x)\cdot \delta
    $$
    
- A PDF value, let’s say $f(x) = 2$ means the probability density at point $x$ is 2 per unit length of $x$. For a small interval of width 0.1 around $x$, the approximate probability is $2 \times 0.1 = 0.2$ (or 20%).

## Definition

Let $X$ be a continuous random variable with PDF $f_X(x)$. Then:

- **Probability over an interval**:
    
    $$
    P(a \leq X \leq b) = \int_a^b f_X(x)\, dx
    $$
    
- **Properties**:
    - $f_X(x) \geq 0$ for all $x$
    - Total area under the curve is 1:
        
        $$
        \int_{-\infty}^{\infty} f_X(x)\, dx = 1
        $$
        

 **Why PDF is non-negative?**

- PDF is non-negative because probability densities cannot represent negative probabilities.

**Why PDF can be greater than 1?**

- PDF can be greater than 1 when probability is concentrated in a very small range, keeping the total area under the curve equal to 1.

## Properties

| **Property** | **Description** |
| --- | --- |
| **Non-negativity** | $f_X(x) \geq 0$ for all $x \in \mathbb{R}$ |
| **Total Area = 1** | $\int_{-\infty}^{\infty} f_X(x)\,dx = 1$ |
| **Probability in Interval** | $\mathbb{P}(a \leq X \leq b) = \int_{a}^{b} f_X(x)\,dx$ |
| **Point Probability** | $\mathbb{P}(X = x) = 0$ – for continuous variables, the probability at a single point is zero |
| **Support** | The set of $x$ for which $f_X(x) > 0$ |

## Mean and Variance

- Mean

$$
\mathbb{E}[X] = \mu = \int_{-\infty}^{\infty} x \cdot f_X(x)\,dx
$$

- Variance

$$
\text{Var}(X) = \mathbb{E}[(X - \mu)^2] = \int_{-\infty}^{\infty} (x - \mu)^2 \cdot f_X(x)\,dx
$$

## Relationship to CDF

The **Cumulative Distribution Function** (CDF), $F_X(x)$, is defined as:

$$
F_X(x) = P(X \leq x) = \int_{-\infty}^x f_X(t)\, dt
$$

i.e. for a given point in PDF the area to the left.

The **PDF is the derivative** of the CDF i.e. the gradient.

$$
f_X(x) = \frac{d}{dx}F_X(x)
$$

## Example

PDFs allow us to model **continuous real-world measurements** (e.g., height, weight, time) where individual values have **zero probability**, but intervals have meaningful probabilities.

Let $X$ represent the height of women, modeled by a **normal distribution** with:

- Mean $\mu = 165$
- Standard deviation $\sigma = 10$

Then $X \sim \mathcal{N}(165, 10^2)$, and its PDF is:

$$
f_X(x) = \frac{1}{\sqrt{2\pi}\cdot 10} \exp\left(-\frac{(x - 165)^2}{2 \cdot 10^2}\right)
$$