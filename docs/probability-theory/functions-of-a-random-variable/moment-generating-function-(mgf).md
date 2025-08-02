# Moment Generating Function (MGF)

## What is the Moment Generating Function (MGF)?

The **Moment Generating Function (MGF)** is a function that summarizes **all moments** (mean, variance, skewness, etc.) of a random variable in one place, making it easier to find these moments without computing complicated integrals for each.

## Definition

For a random variable $X$, the MGF is defined as:

$$
M_X(t) = \mathbb{E}[e^{tX}] = \int_{-\infty}^\infty e^{t x} f_X(x) \, dx
$$

where $f_X(x)$ is the probability density function (pdf) of $X$, and $t$ is a real number.

The main practical use of the Moment Generating Function (MGF) is to **make calculating moments (mean, variance, higher moments) easier** by using derivatives instead of direct integration over the PDF or PMF.

### Interpretation

MGF summarizes the entire probability distribution of a random variable in a single function. It can be thought of as a “generator” of moments because its derivatives at zero give all moments (mean, variance, skewness, etc.). Basically you give it a number, it gives you a property. 

MGFs make it easier to work with sums of independent random variables since the MGF of a sum is the product of their MGFs. This property simplifies analysis in probability and statistics.

### Why is it called “Moment Generating”?

Expand the exponential as a power series:

$$
e^{tX} = 1 + tX + \frac{t^2 X^2}{2!} + \frac{t^3 X^3}{3!} + \cdots
$$

Taking expectation inside:

$$
M_X(t) = 1 + t \mathbb{E}[X] + \frac{t^2}{2!} \mathbb{E}[X^2] + \frac{t^3}{3!} \mathbb{E}[X^3] + \cdots
$$

Each coefficient contains a moment $\mathbb{E}[X^n]$.

### What are Moments?

Moments are numerical values that describe important characteristics of a random variable’s distribution, like its shape, spread, and central tendency.

- The **1st moment** is the **mean** (average), showing the central location.
- The **2nd moment** relates to the **variance**, measuring how spread out the values are.
- The **3rd moment** measures **skewness**, indicating asymmetry (whether the distribution leans left or right).
- The **4th moment** measures **kurtosis**, which shows how heavy or light the tails of the distribution are compared to a normal distribution.

More formally, the $n$-th moment of a random variable $X$ is:

$$
\mathbb{E}[X^n] = \int_{-\infty}^\infty x^n f_X(x) \, dx
$$

where $f_X(x)$ is the probability density function (PDF) of $X$.

Moments help summarize and understand the overall behavior of the distribution.

### How to extract moments from MGF?

Evaluating at $t=0$ is the natural point where the exponential series starts, so the derivatives there directly extract the raw moments of the distribution.

- **1st moment (mean):**

$$
E[X] = \int_{-\infty}^{\infty} x \cdot f_X(x) \, dx
\\
\mathbb{E}[X] = M_X'(0) = \left.\frac{d}{dt} M_X(t) \right|_{t=0}
$$

- **2nd moment (variance):**

$$
E[X^2] = \int_{-\infty}^{\infty} x^2 \cdot f_X(x) \, dx
\\
\mathbb{E}[X^2] = M_X''(0) = \left.\frac{d^2}{dt^2} M_X(t) \right|_{t=0}
$$

- **nth moment:**

$$
\mathbb{E}[X^n] = M_X^{(n)}(0) = \left.\frac{d^n}{dt^n} M_X(t) \right|_{t=0}
$$

## Properties

| Property | Description |
| --- | --- |
| **Existence** | Exists if $\mathbb{E}[e^{tX}] < \infty$ for $t$ near 0 |
| **Value at zero** | $M_X(0) = 1$ |
| **Sum of independent random variables** | $M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$ for independent $X, Y$ |
| **Uniqueness** | If $M_X(t) = M_Y(t)$  near 0, then $X$ and $Y$ have the same distribution |

## Example: MGF of Gaussian

$$
M_X(t) = \exp \left( \mu t + \frac{\sigma^2 t^2}{2} \right)
$$

- First derivative (Mean):

$$
M_X'(t) = \left(\mu + \sigma^2 t\right) \exp \left( \mu t + \frac{\sigma^2 t^2}{2} \right)
$$

- Evaluate at $t=0$:

$$
M_X'(0) = \mu \cdot 1 = \mu
$$

- Second derivative (variance):

$$
M_X''(t) = \left(\sigma^2 + (\mu + \sigma^2 t)^2\right) \exp \left( \mu t + \frac{\sigma^2 t^2}{2} \right)
$$

- Evaluate at $t=0$:

$$
M_X''(0) = \sigma^2 + \mu^2 = \mathbb{E}[X^2]
$$

To get variance, 

$$
Var(X)=E[X^2]−(E[X])^2 = \sigma^2 + \mu^2 - \mu^2 = \sigma^2
$$