# Connection Between the Exponential Distribution and the Poisson Process

## Concepts

- **Exponential distribution** models the **waiting time** until a rare event occurs (e.g. a light bulb fails).
    
    $$
    f(x; \lambda) = 
    \begin{cases}
    \lambda e^{-\lambda t} & \text{for } t \geq 0 \\
    0 & \text{for } t < 0
    \end{cases}
    $$
    
- **Poisson process** models the **number of rare events** occurring in a given time interval.
    
    $$
    P\{X = k\} = \frac{\lambda^k}{k!} e^{-\lambda}
    $$
    

These two are closely connected.

### How They Are Related

- Imagine a stream of random events happening at a rate (e.g. receiving emails).
- Even if events are frequent over time, the **probability of one in a very small instant** is still small.
- Therefore, Poisson processes are valid even for frequent events like emails.

### Timeline and Waiting Times

- Events arrive at times: $T₁, T₂, T₃, ..., Tₙ$
- Define waiting times between events: $W₁ = T₂ - T₁, W₂ = T₃ - T₂$, etc.
- Each waiting time $W_j$:
    - Is **independent**
    - Follows an **Exponential(λ)** distribution
    - Where **λ** is the event rate (e.g. 5 emails per minute)
- The **waiting time** (continuous) and the **event count** (discrete) are two sides of the same process.
- A **Poisson process** unites these:
    - Exponential gaps between events
    - Poisson counts in intervals

### Summary

- **Waiting time between events** → Exponential(λ)
- **Number of events in time T** → Poisson(λT)

### Continuous vs Discrete

- Waiting times are **continuous** (e.g. 1.2 minutes)
- Number of events is **discrete** (e.g. 3 emails)

## Example: Emails Arriving

Let emails arrive at a **rate λ = 5 per minute**

### Question 1: Probability of waiting more than t minutes for the next email

$$
P(T > t) = e^{-5t}
$$

This comes from the **exponential distribution**.

The longer you wait, the smaller the probability.

### Question 2: Probability of getting **zero emails** in the next t minutes

$$
P(K = 0) = \frac{(5t)^0 e^{-5t}}{0!} = e^{-5t}
$$

This is from the **Poisson distribution**.

Same numerical result as Question 1.

### Question 3: Probability of getting **exactly one email** in the next t minutes

$$
P(K = 1) = \frac{(5t)^1 e^{-5t}}{1!} = 5t \cdot e^{-5t}
$$

This is 5t times more likely than zero emails, for small t.