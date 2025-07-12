# Introduction

## What

**Probability** is the mathematical framework used to quantify and model **uncertainty** in complex systems. It provides tools to describe the likelihood of various outcomes when the exact behavior of a system is too complicated or unknown.

- It assumes a **known probability distribution** that models how likely different outcomes are.
- Probability helps us say something quantifiable about **future observations** or events whose exact results are unknown.
- Examples include modeling measurement errors, gas molecules behavior, turbulence, weather, and human behavior.

**Key Concepts with Examples**

**Uncertainty and Complex Systems**

- Example: Cannot track every molecule in a gas, so we model temperature and entropy probabilistically using distributions like the Maxwell-Boltzmann distribution.
- Example: Turbulence in fluid flow is too complex to simulate exactly, so statistical models are used.

**Measurement Error**

- Measurements (e.g., speed of light, gravity acceleration) have inherent errors, often modeled as normally distributed random variables. Repeating an experiment yields slightly different results each time.
- Often times measurement error behave according to Gaussian distribution **(Genesis)**.

**Random Variables**

- A variable (X) whose possible values have associated probabilities.
- Example: X could represent the number of heads in 10 coin flips.
- Distributions have parameters: e.g., Gaussian with mean (average) and standard deviation (spread).

**Counting Events**

- Probability often reduces to counting how many outcomes satisfy certain criteria.
- Example: How many poker hands of a certain type are possible? What is the probability that three dice sum to 13?


!!! note
    **Probability vs. Statistics**  
    - Probability: Assume Known distribution, unknown future data; quantifies chance of events.  
    - Statistics: Known data samples, unknown distribution; infer properties of the system from data. For example, ML for learning the probability distribution (i.e. parameters)

!!! note
    **Probability vs. Likelihood**  
    - Probability is the chance of observing a given outcome based on a known model. Likelihood is the chance of the model being true given a specific outcome.  
    - **Likelihood** is a method/statistical concept **used within** statistics. In other words, **probability** asks "What are the odds of seeing this data, given the model?" while **likelihood** asks "How likely is this model, given the data?"  
    - **Probability** is used when we know the model or process and want to predict how likely a particular outcome is. For example, if we know a coin is fair, the probability of getting heads is 50%.  
    - **Likelihood** is used when we have data (the outcome) and want to figure out which model or parameter is most likely to have produced that data. For example, if we flip a coin and get heads 9 out of 10 times, we might use likelihood to determine how fair the coin is.  

## How

- **Model uncertainty by using probability distributions:** For example, a normal (Gaussian) distribution models measurement errors. This means, to use parameters (e.g., mean and standard deviation) to define distributions.
- Use **random variables** to represent quantities that can take on different values with certain probabilities.
- Count possible outcomes and group events into sets to calculate probabilities.
- Apply probability to **calculate the chance of events** such as flipping 7 heads in 10 coin tosses or rolling dice sums.
- Use probability in dynamic systems by combining it with differential equations, leading to **stochastic differential equations**.
- Techniques like the **Kalman filter** merge control theory with probabilistic models to handle measurement uncertainty in real-time systems.
- Understand that some physical systems (coin flips, turbulence) are fundamentally deterministic but appear random due to complexity and measurement limits.

## Why

The real world is **complex and uncertain**, and it is often impossible to measure or model every detail exactly.  Probability offers an elegant way to **simplify this complexity** into manageable statistical quantities. It provides a framework for **modeling measurement errors** that naturally occur in experiments. Also, enables prediction and understanding of inherently unpredictable phenomena like weather and human behavior. It allows bridging from deterministic physics to practical modeling when full knowledge is unavailable.