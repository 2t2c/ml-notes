# Exponential Distribution

## Concept

A random time $T$ is said to be *exponentially distributed* with parameter $\lambda > 0$ if its probability density function (PDF) is:

$$
f(x; \lambda) = 
\begin{cases}
\lambda e^{-\lambda t} & \text{for } t \geq 0 \\
0 & \text{for } t < 0
\end{cases}
$$

where,

- **Parameter $\lambda$**: Called the *rate parameter*
    - Determines how quickly events are expected to happen.
    - Higher $\lambda$ → more frequent events.

It is used to model: Time between rare or random events, e.g.:

- Time until a lightbulb fails
- Time until radioactive decay
- Waiting time at the DMV

**Descriptive Statistics**

| Type | Formula |
| --- | --- |
| Support | $t \in [0, \infty)$ |
| Rate Parameter | $\lambda > 0$ |
| Mean | $\mathbb{E}[T] = \frac{1}{\lambda}$ |
| Variance | $\text{Var}(T) = \frac{1}{\lambda^2}$ |
| Standard Deviation | $\sigma = \frac{1}{\lambda}$ |
| Probability Density Function (PDF) | $f(t) = \lambda e^{-\lambda t} \quad for \quad t\geq 0$ |
| Cumulative Distribution Function (CDF) | $F(t) = \mathbb{P}(T \leq t) = 1 - e^{-\lambda t}$ |

### Probability Calculations

- **Infinitesimal probability** between $t$ and $t + dt$:
    
    $$
    P(t < T \leq t + dt) = \lambda e^{-\lambda t} dt
    $$
    
- **Probability between any two times** aa and bb:
    
    $$
    P(a \leq T \leq b) = \int_a^b \lambda e^{-\lambda t} dt = e^{-\lambda a} - e^{-\lambda b}
    $$
    

## Cumulative Distribution Function (CDF)

Defined as:

$$
F(t) = \int_0^t \lambda e^{-\lambda x} \, dx= \left[ -e^{-\lambda x} \right]_0^t= -e^{-\lambda t} + e^{0}= 1 - e^{-\lambda t}
$$

$$
\text{Total Probability} = \int_0^\infty \lambda e^{-\lambda x} \, dx= \left[ -e^{-\lambda x} \right]_0^\infty= 0 + 1 = 1
$$

## Example Use-Cases

- **Lightbulb lifetime:** Good for modeling how long a lightbulb might last before it fails.
- **Radioactive decay:** Time until a single atom decays.
- **Queueing scenarios:** Time until the next customer is seen.

### Example 1: Lightbulb Lifetime

> Average lifetime: 100 hours
> 
> 
> Find: Probability lightbulb lasts **at least 50 hours**
> 
- Given: $\lambda = \frac{1}{100}$
- Compute $P(T \geq 50)$:

$$
P(T \geq 50) = 1 - P(T < 50) = 1 - F(50) = e^{-\lambda \cdot 50} = e^{-0.5} \approx 0.606
$$

### Example 2: Radioactive Decay (Polonium-210)

> Halflife = 138 days
> 
> 
> Find: Value of $\lambda$
> 
- Half-life definition: $F(t) = 0.5$ when $t = 138$

$$
F(138) = 1 - e^{-138\lambda} = 0.5
\Rightarrow e^{-138\lambda} = 0.5
\Rightarrow -138\lambda = \ln(0.5)
\Rightarrow \lambda = \frac{\ln(2)}{138}
$$

## **Memoryless Property**

One of the most profound properties of the exponential distribution:

$$
P(T > t + s \mid T > s) = P(T > t)
$$

- **Interpretation**:
    - The probability that the event lasts at least an additional $t$ time units given that $s$ time units have already passed is still $P(T > t)$
    - Past time has **no effect** on the future probability.
    - The clock resets back to $t$ if the time $s$ has already passed
    - Only memoryless continuous distribution
- **Example**:
    - Lightbulb lasts 100 hours on average
    - If 100 hours have passed with no failure, the expected lifetime from that point onward is **still** 100 hours

### Intuition Conflict

> “If it was supposed to fail around 100 hours, shouldn't it be close to failure at 100?”
> 
- No. The exponential distribution says **no aging**: surviving longer **does not** increase the risk of near failure.

## The Hazard Rate

The **hazard rate** tells us the chance of something failing *right now*, assuming it has survived up to time $t$.

Think of it like this:

> If a lightbulb has already lasted 100 hours, what is the chance it fails in the next tiny moment?
> 

For the exponential distribution, this hazard rate is constant:

$$
\text{Hazard rate} = \lambda
$$

Suppose a lightbulb’s lifetime follows an exponential distribution with $\lambda = 0.01$ (so average lifetime is 100 hours).

Even if the bulb has lasted:

- 0 hours: chance of failure in next instant = 0.01
- 100 hours: still 0.01
- 500 hours: still 0.01

The risk of failure never changes with age. That is why the exponential distribution is called *memoryless*.

**Proof**

$$
h(t) = \lim_{\Delta t \to 0} \frac{\mathbb{P}(t \leq T < t + \Delta t \mid T > t)}{\Delta t}
$$

For exponential distribution:

$$
\mathbb{P}(t \leq T < t + \Delta t \mid T > t) = 1 - e^{-\lambda \Delta t}
$$

Expand using Taylor series:

$$
e^{-\lambda \Delta t} \approx 1 - \lambda \Delta t + \frac{1}{2} \lambda^2 \Delta t^2 - \cdots
$$

So, **Probability of dying/failure in next $\Delta t$:**

$$
1 - e^{-\lambda \Delta t} \approx \lambda \Delta t
$$

Thus, hazard rate is:

$$
h(t) = \frac{\lambda \Delta t}{\Delta t} = \lambda
$$

Interpretation

- The **hazard rate is constant**: $h(t) = \lambda$
- Meaning: **The risk of failure per unit time is always the same**, no matter how long it has survived.

Derived Formula

$$
\mathbb{P}(T \in [t, t + \Delta t] \mid T > t) \approx \lambda \Delta t
$$

Or equivalently:

$$
\mathbb{P}(T \in [t, t + \Delta t]) = \lambda \cdot \mathbb{P}(T > t) \cdot \Delta t
$$

Connection to the PDF

$$
f(t) = \lambda e^{-\lambda t} = \lambda \cdot \mathbb{P}(T > t)
$$

This confirms:

- The PDF is the hazard rate times survival function where $S(t)=P(T>t)$
- A core identity in survival analysis: $f(t) = h(t) \cdot S(t)$
- The exponential distribution's constant hazard rate is unique real-world systems often do not behave this way (aging, wear, etc.).
- We can write down a differential equation for $f(t)$ using the hazard rate:
    
    $$
    \frac{d}{dt} \mathbb{P}(T > t) = -\lambda \mathbb{P}(T > t) \Rightarrow \mathbb{P}(T > t) = e^{-\lambda t}
    $$