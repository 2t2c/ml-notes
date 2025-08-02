# Continuous Random Variables

## What

A continuous random variable is a variable that can take any value within an interval or range, typically represented by real numbers. Its probabilities are described by a probability density function (PDF), not discrete probabilities.

## How

- The **Probability Density Function (PDF)**, $f(x)$, describes the relative likelihood of the variable near a value $x$.
- The **Cumulative Distribution Function (CDF)**, $F(x) = P(X \leq x)$, gives the probability the variable is less than or equal to xx.
- Probabilities for exact values $P(X = x)$ are zero; only intervals have nonzero probabilities via integrals of the PDF.
- Key properties:
    
    $$
    f(x) dx = 1, \quad F(x) = \int_{-\infty}^x f(t) dt
    $$
    
- Expectation (mean) and variance are computed using integrals of $x f(x)$ and $(x - \mu)^2 f(x)$.

## Why

Continuous random variables model measurements or quantities that vary smoothly, such as time, height, or temperature. Understanding their PDFs and CDFs enables calculation of probabilities, expectations, and predictions in fields like physics, finance, and engineering.

## Sections

[Normal Distribution](Continuous%20Random%20Variables%2022d81ba4f78a8042ad83d2270b380939/Normal%20Distribution%2023381ba4f78a80e5ab5be4e84fb52505.md)

[Exponential Distribution](Continuous%20Random%20Variables%2022d81ba4f78a8042ad83d2270b380939/Exponential%20Distribution%2023981ba4f78a8066b240f2b92a154eb1.md)

[**Connection Between the Exponential Distribution and the Poisson Process**](Continuous%20Random%20Variables%2022d81ba4f78a8042ad83d2270b380939/Connection%20Between%20the%20Exponential%20Distribution%20an%2024081ba4f78a801a9721ec1e660efe5f.md)

[Gamma Distribution](Continuous%20Random%20Variables%2022d81ba4f78a8042ad83d2270b380939/Gamma%20Distribution%2024081ba4f78a80799a49f8f6c2b1179a.md)