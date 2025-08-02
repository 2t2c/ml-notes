# Gamma Distribution

## Recap

- Exponential distribution models **waiting time until the next event** in a Poisson process.
- The number of events in time $T$ follows a **Poisson(λT)** distribution.
- Events occur at times $T₁, T₂, T₃, ...$
    
    The **waiting times** between them are exponential.
    

Beyond the First Event

- What if we want the **waiting time until the r-th event**, not just the next one?
- This leads to the **Gamma distribution**.

## Definition: Gamma Distribution (Generalizing Exponential Waiting Times)

Let:

- $Tᵣ = W₁ + W₂ + ... + Wᵣ$ be the waiting time for the r-th event.
- Each $Wⱼ$ is independent and follows **Exponential(λ)**.

Then:

$$
Tᵣ \sim \text{Gamma}(r, \lambda)
$$

- $r$: number of events we are waiting for
- $\lambda$: event rate

Gamma has **two parameters**: $r$ and $\lambda$

Exponential is a special case when $r = 1$.

## Derivation Sketch (without messy math)

To compute: 

Continuous waiting time for $r^{th}$ arrival

$$
P(Tᵣ > t)
$$

This is the same as:

$$
P(\text{fewer than r events occur in time } t)
$$

Which is:

# of Poisson events that occur in time $t$

$$
P(N(t) \leq r - 1)
$$

Where $N(t)$ is the number of Poisson events in time $t$.

$$
P(Tᵣ > t) = \sum_{k=0}^{r-1} \frac{(λt)^k e^{-λt}}{k!}
$$

This is the **CDF** (complement) of the Gamma distribution.

Take the derivative to get the **PDF**:

$$
f(t) = \frac{λ^r t^{r-1} e^{-λt}}{(r-1)!}
$$

This is the **Gamma probability density function**.

**Descriptive Statistics**

| Type | Formula |
| --- | --- |
| Support | $t \in [0, \infty)$ |
| Shape Parameter | $r > 0$ (number of events) |
| Rate Parameter | $\lambda > 0$ |
| Mean | $\mathbb{E}[T] = \frac{r}{\lambda}$ |
| Variance | $\text{Var}(T) = \frac{r}{\lambda^2}$ |
| Standard Deviation | $\sigma = \sqrt{\frac{r}{\lambda^2}}$ |
| Probability Density Function (PDF) | $f(t) = \frac{\lambda^r t^{r-1} e^{-\lambda t}}{(r-1)!} \quad \text{for } t \geq 0$ |
| Cumulative Distribution Function (CDF) | $F(t) = \mathbb{P}(T \leq t) = \int_0^t f(s)\, ds \quad or \quad \frac{\gamma(r, \lambda t)}{\Gamma(r)}$ |

## Use Case Example

### DMV Analogy (Series Case)

- You must speak to **three agents**, one after another.
- (Mean of Exp. Distribution) Each has a **15-minute exponential wait** ⇒ $λ = \frac{1}{15}$

Total wait time is the **sum of 3 exponential variables**:

$$
T \sim \text{Gamma}(3, 1/15)
$$

## Clarification: Series vs Parallel

### **Series (Gamma)**: You wait for 3 stages one after another

e.g. DMV → agent A → agent B → agent C

→ Waiting time follows Gamma

$$
T \sim \text{Gamma}(3, 1/15)
$$

**Mean and Variance**

For $T \sim \text{Gamma}(r, \lambda)$, where:

- $r=3$
- $\lambda = \frac{1}{15}$

Then:

- **Mean**: $\mathbb{E}[T] = \frac{r}{\lambda} = \frac{3}{1/15} = 45 \text{ minutes}$
- **Variance**: $\text{Var}(T) = \frac{r}{\lambda^2} = \frac{3}{(1/15)^2} = 3 \cdot 225 = 675$
    
    

**Probability Density Function (PDF)**

The PDF of the Gamma distribution is:

$$
f(t) = \frac{\lambda^r t^{r-1} e^{-\lambda t}}{(r-1)!}
$$

Substitute values:

$$
f(t) = \frac{(1/15)^3 \cdot t^2 \cdot e^{-t/15}}{2!} = \frac{1}{2} \cdot \left(\frac{1}{3375}\right) \cdot t^2 \cdot e^{-t/15}
$$

So:

$$
f(t) = \frac{t^2}{6750} \cdot e^{-t/15}
$$

This gives the **probability density** at time $t$, in minutes.

### **Parallel (Not Gamma, Exponential)**:

3 open lanes, choose the shortest

→ Minimum of exponential variables

→ Not Gamma, uses Exponential Distribution

For the **parallel case**, you are taking the **minimum** of 3 independent exponential wait times, each with: $\lambda = \frac{1}{15}$

This gives:

$$
T_{\min} \sim \text{Exponential}(3 \cdot \lambda) = \text{Exponential}\left(\frac{1}{5}\right)
$$

**Mean and Variance**

For $T \sim \text{Exponential}(\lambda)$, we have:

- **Mean**: $\mathbb{E}[T] = \frac{1}{\lambda} = 5 \text{ minutes}$
- **Variance**: $\text{Var}(T) = \frac{1}{\lambda^2} = 25$

**Probability Density Function (PDF)**

The PDF is: $f(t) = \lambda e^{-\lambda t}$

Substitute $\lambda = \frac{1}{5}$: $f(t) = \frac{1}{5} e^{-t/5}$

This gives the **probability density** for being helped at time $t$, when choosing the fastest of 3 lanes.