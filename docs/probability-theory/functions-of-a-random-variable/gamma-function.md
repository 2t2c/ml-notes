# Gamma Function

## What is the Gamma Function?

The **Gamma function** $\Gamma(z)$ generalizes the factorial function for real and complex numbers (except negative integers). It is widely used in probability, especially for defining distributions like the Gamma and Beta distributions. The Gamma function answers the question: “What is the factorial of a non-integer?” For example, $\Gamma(3.5)$ gives the value of $(2.5)!$.

### Interpretation

- For a positive integer $n$, $\Gamma(n) = (n-1)!$.
    - so $\Gamma(4) = 3! = 6$.
- For non-integers, $\Gamma(z)$ extends factorial smoothly and continuously.
- It arises from extending the factorial rule/constraint $n! = n \cdot (n-1)!$ to a function $f(x)$ that satisfies:
    
    $$
    f(x) = x \cdot f(x-1)
    $$
    
    for all $x > 0$, not just integers.
    
- The Gamma function **scales** functions and appears in the normalization constants of many continuous probability distributions.

## Definition

For any complex number $z$ with positive real part:

$$
\Gamma(z) = \int_0^\infty t^{z-1} e^{-t} \, dt
$$

- $\Gamma(n) = (n-1)!$ if $n$ is a positive integer.
- Recursive relation:
    
    $$
    \Gamma(z+1) = z \cdot \Gamma(z)
    $$
    
- It is undefined for zero and negative integers but defined elsewhere.

## Properties

| **Property** | **Description** |
| --- | --- |
| **Integral form** | $\displaystyle \Gamma(z) = \int_0^\infty t^{z-1} e^{-t} dt$, valid for $\text{Re}(z) > 0$ |
| **Relation to factorial** | $\Gamma(n) = (n-1)!$ for positive integers $n$ |
| **Recursion** | $\Gamma(z+1) = z \Gamma(z)$ |
| **Analytic continuation** | Extends to all complex $z$ except non-positive integers |
| **Positivity** | $\Gamma(z) > 0$ for $z > 0$ |

## Why is the Gamma function important in probability?

- It appears in the **Gamma distribution's PDF**, used to model waiting times and other continuous phenomena.
- The Gamma function helps normalize PDFs involving powers and exponentials, ensuring total probability integrates to 1.
- Many distributions (Beta, Chi-square, t-distribution) use the Gamma function in their formulas.

## Gamma distribution PDF

Let $X$ be a Gamma-distributed variable with shape parameter $\alpha > 0$ and rate parameter $\beta > 0$. Its PDF is:

$$
f_X(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\beta x}, \quad x > 0
$$

- Here, $\Gamma(\alpha)$ normalizes the function so the total area is 1.
- The Gamma function allows $\alpha$ to be any positive real number, not just integers.

## Relationship to factorial

For integers:

$$
\Gamma(n) = (n-1)!
\\
\Gamma(n+1) = n!
$$

Example:

- $\Gamma(5) = 4! = 24$
- $\Gamma(1/2) = \sqrt{\pi}$, an important special value used in probability theory.

## Example

To compute $\left(\frac{3}{2}\right)!$, use:

We know:

$$
n! = \Gamma(n + 1)\Rightarrow \left(\frac{3}{2}\right)! = \Gamma\left(\frac{3}{2} + 1\right) = \Gamma\left(\frac{5}{2}\right)
$$

Using recursion property:  

$$
\Gamma(z+1) = z \cdot \Gamma(z) \Rightarrow \Gamma\left(\frac{3}{2} + 1\right) = \frac{3}{2} \cdot \Gamma\left(\frac{3}{2}\right) = \frac{3}{2} \cdot \frac{1}{2} \cdot \Gamma\left(\frac{1}{2}\right) \\=\frac{3}{2} \cdot \frac{1}{2} \cdot \sqrt{\pi} \approx 1.329
$$