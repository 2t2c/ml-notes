# Beta Function

## What is the Beta Function?

The **Beta function** $B(x, y)$ is a continuous function that tells you **how to weight values between 0 and 1** when combining two quantities with different “pulls” or “strengths” $x$ and $y$. The Beta function takes two inputs because it measures interactions between two quantities, it’s about how two competing forces shape a distribution over the interval $[0,1]$. It is also closely related to the Gamma function.

For example:

- $x$ controls how strongly we **pull toward 1**
- $y$ controls how strongly we **pull toward 0**

It acts like a **balancing tool**:

- When you want to measure how much a value leans toward one side (e.g., near 0 or near 1),
- And you want both sides to influence the outcome smoothly.

### Interpretation

- The Beta function acts like a **normalization constant** for the Beta distribution.
- It provides a way to **combine two inputs** $x$ and $y$ in a symmetric and continuous fashion.
- It's useful in modeling probabilities over intervals (e.g., proportions, rates, percentages between 0 and 1).

## Definition

For real numbers $x > 0$ and $y > 0$, the **Beta function** $B(x, y)$ is defined as:

$$
B(x, y) = \int_0^1 t^{x - 1} (1 - t)^{y - 1} \, dt
$$

This integral converges for all positive $x$ and $y$.

## Properties

| **Property** | **Description** |
| --- | --- |
| **Symmetry** | $B(x, y) = B(y, x)$ |
| **Relation to Gamma** | $B(x, y) = \dfrac{\Gamma(x)\Gamma(y)}{\Gamma(x + y)}$ |
| **Positive** | $B(x, y) > 0$ for $x, y > 0$ |
| **Used in distributions** | Normalizes the PDF of the Beta distribution |
| **Special values** | $B(1, y) = \frac{1}{y}$, $B(x, 1) = \frac{1}{x}$ |

## Why is the Beta Function important in probability?

- It **normalizes the Beta distribution**, making the area under the PDF equal to 1.
- It models **random variables bounded between 0 and 1** (e.g., proportions).
- Its relationship with the Gamma function helps simplify many statistical formulas.

## Connection to Gamma Function

The Beta function can be expressed using the Gamma function:

$$
B(x, y) = \frac{\Gamma(x) \cdot \Gamma(y)}{\Gamma(x + y)}
$$

This identity is extremely useful when computing Beta-related expressions in probability or simplifying integrals.

## Example

Let’s compute $B(2, 3)$:

Using the definition:

$$
\begin{align*}B(2, 3) = \int_0^1 t^{1} (1 - t)^{2} \, dt = \int_0^1 t (1 - t)^2 \, dt\\= \int_0^1 t (1 - 2t + t^2) \, dt = \int_0^1 (t - 2t^2 + t^3) \, dt\\= \left[ \frac{t^2}{2} - \frac{2t^3}{3} + \frac{t^4}{4} \right]_0^1 = \frac{1}{2} - \frac{2}{3} + \frac{1}{4}\\= \frac{6}{12} - \frac{8}{12} + \frac{3}{12} = \frac{6 - 8 + 3}{12} = \frac{1}{12}\end{align*}
$$

Using the Gamma relation:

$$
B(2, 3) = \frac{\Gamma(2)\Gamma(3)}{\Gamma(5)} = \frac{1! \cdot 2!}{4!} = \frac{1 \cdot 2}{24} = \frac{1}{12}
$$

## Use in Beta Distribution

The **Beta distribution** with parameters $\alpha > 0$, $\beta > 0$ has PDF:

$$
f(x; \alpha, \beta) = \frac{1}{B(\alpha, \beta)} x^{\alpha - 1} (1 - x)^{\beta - 1}, \quad \text{for } x \in (0, 1)
$$

Here, the **Beta function** in the denominator ensures that the area under the PDF is 1.