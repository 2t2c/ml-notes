# Functions of a Random Variable

## **What**

We define a new random variable $Y = g(X)$, where $X$ is a known random variable and $g$ is a deterministic function. This allows us to study the distribution of transformed quantities, like kinetic energy from velocity, Celsius from Fahrenheit, or squared values from a normal distribution.

## **Why**

- Many real-world quantities are **functions** of more basic random variables.
- Enables modeling derived or transformed metrics, like energy, signal power, or log-returns.
- Critical in probability and statistics for creating new distributions (e.g., chi-square from normal).

## **How**

To find the distribution of $Y = g(X)$:

1. **Do not** directly plug $g(X)$ into the PDF of $X$ → this is incorrect.
2. Instead, follow this **valid procedure**:

**Why you cannot directly plug $g(X)$ into the PDF$f_X(x)$:**

- The PDF $f_X(x)$ gives the probability density at a particular Celsius temperature $x$.
- $g(X)$ gives the Fahrenheit temperature corresponding to Celsius temperature $X$.
- To find the PDF of $Y$, you cannot just substitute $g(x)$ inside $f_X$ like $f_X(g(x))$. That won't give you a proper PDF of $Y$.

### 1. Use the CDF:

$$
F_Y(y) = P(Y \leq y) = P(g(X) \leq y)
$$

Transform this into an expression involving $X$ and use $F_X$ (the known CDF of $X$).

### 2. Differentiate the CDF to get the PDF:

**You cannot go PDF → PDF directly.** You must pass through the CDF.

$$
f_Y(y) = \frac{d}{dy} F_Y(y)
$$

This gives a well-defined PDF for $Y$, which reflects the correct transformation.

### **Example 1: Linear Transformation**

Let $X \sim \mathcal{N}(\mu, \sigma^2)$ and define $Y = aX + b$
Then to get the CDF:

$$
\begin{align*}
F_Y(y) = P(Y \lt y) = P(aX + b < y) 
\\
=P(X < \frac{y-b}{a})
\\
=F_X\left(\frac{y - b}{a}\right)
\end{align*} 
$$

Differentiating CDF to get the PDF:

$$
\begin{align*}
f_Y(y) = \frac{d}{dy}F_X\left(\frac{y - b}{a}\right)
\\
=\frac{1}{a} f_X\left(\frac{y - b}{a}\right)
\end{align*}
$$

Result: $Y \sim \mathcal{N}(a\mu + b, a^2\sigma^2)$

## Sections

[Probability Mass Function (PMF)](Functions%20of%20a%20Random%20Variable%2024181ba4f78a801ca928ec66c6ca4aa3/Probability%20Mass%20Function%20(PMF)%2024181ba4f78a80b29aadea06ffebfd92.md)

[Probability Density Function (PDF)](Functions%20of%20a%20Random%20Variable%2024181ba4f78a801ca928ec66c6ca4aa3/Probability%20Density%20Function%20(PDF)%2024181ba4f78a80b3aa03d1ad644e235a.md)

[Cumulative Distribution Function (CDF)](Functions%20of%20a%20Random%20Variable%2024181ba4f78a801ca928ec66c6ca4aa3/Cumulative%20Distribution%20Function%20(CDF)%2024181ba4f78a8023b165e2a1687ab89f.md)

[Gamma Function](Functions%20of%20a%20Random%20Variable%2024181ba4f78a801ca928ec66c6ca4aa3/Gamma%20Function%2024181ba4f78a80bf9f98f5e82d0bd458.md)

[Beta Function](Functions%20of%20a%20Random%20Variable%2024181ba4f78a801ca928ec66c6ca4aa3/Beta%20Function%2024181ba4f78a80278acec4cec7ad3baa.md)

[Moment Generating Function (MGF)](Functions%20of%20a%20Random%20Variable%2024181ba4f78a801ca928ec66c6ca4aa3/Moment%20Generating%20Function%20(MGF)%2024181ba4f78a806493b1fadfa5d13618.md)