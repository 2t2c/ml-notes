# Bernoulli and Binomial Variables

## **Bernoulli Random Variable**

A **Bernoulli random variable** $X$ takes on **two values.** It is a single binary trial.

$$
X \in \{0, 1\}
$$

Where,

- **1**: Event occurs (success)
- **0**: Event does not occur (failure)

Examples:

- Coin flip: heads = 1, tails = 0
- Dice roll: got a 6 = 1, else = 0
- Manufacturing: good part = 1, defective = 0
- Let:
    - $P(X = 1) = p$: probability of success
    - $P(X = 0) = 1 - p = q$: probability of failure
    - Note: $p + q = 1$
- Common in:
    - Simulations (e.g. binary masks for data augmentation)
    - Any binary outcome

### **Bernoulli Distribution**

A probability distribution of a random variable that takes value 1 (success) with probability p, and 0 (failure) with probability 1−p1 - p.

**PMF (Probability Mass Function)**:

$$
P(X = x) = p^x (1 - p)^{1 - x}, \quad x \in \{0, 1\}
$$

**Parameters**: $p \in [0, 1]$ — probability of success.

**Descriptive Statistics**

| **Type** | **Formula** |
| --- | --- |
| **Support** | $x \in \{0, 1\}$ |
| **Mean** | $\mathbb{E}[X] = p$ |
| **Variance** | $\text{Var}(X) = \sigma^2 = p(1 - p) = pq$ |
| **Standard Deviation** | $\sigma = \sqrt{pq}$ |

**Applications**

- Single coin flip
- Binary outcome (pass/fail, defective/good)
- Spam vs. not spam email

<aside>
💡

In statistics, the support of a random variable refers to **the set of all possible values that the random variable can take with a non-zero probability**. Essentially, it's the range of values where the probability distribution or density function is not zero. 

</aside>

## **Binomial Random Variable**

A **Binomial random variable** is the **sum of $n$ independent Bernoulli trials**:

$$
X = B_1 + B_2 + \dots + B_n
$$

Represents the number of successes in $n$ trials.

$$
X \sim \text{Binomial}(n, p)
$$

**Probability Mass Function (PMF):**

$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
$$

- $\binom{n}{k}$: Number of ways to choose kk successes
- $p^k$: Probability of kk successes
- $(1-p)^{n-k}$: Probability of $n-k$ failures
- Useful for:
    - Modeling counts of successes (e.g. number of heads in 10 coin flips)
    - Approximates the normal distribution for large nn

### **Examples**

**Case 1: $n = 2$**

- Outcomes:
    - $X = 0$: both trials fail → $q^2$
    - $X = 1$: one success → $2pq$
    - $X = 2$: both succeed → $p^2$
- Probabilities sum to 1: $q^2 + 2pq + p^2 = (p + q)^2 = 1$

**Case 2: $n = 3$**

- $P(X = 1)$: Exactly one success
    - Three cases: success on trial 1, 2, or 3 → $pq^2$
    - In general:
        
        $$
        P(X = k) = \binom{3}{k} p^k q^{3-k}
        $$
        
- Pascal’s Triangle provides binomial coefficients:
    - $n = 2: 1,2,1$
    - $n = 3: 1,3,3,1$

### **Binomial Distribution**

The distribution of the number of successes in nn independent Bernoulli trials, each with success probability $p$.

**Probability Mass Function (PMF):**

$$
P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}, \quad k = 0, 1, ..., n
$$

**Parameters**:

$n \in \mathbb{N}$ — number of trials

$p \in [0, 1]$ — probability of success per trial

Note: $k$ is not a parameter; it’s a sampling variable

**Descriptive Statistics**

| **Type** | **Formula** |
| --- | --- |
| **Support** | $k \in \{0, 1, ..., n\}$ |
| **Mean** | $\mathbb{E}[X] = np$ |
| **Variance** | $\text{Var}(X) = \sigma^2 = np(1 - p) = npq$ |
| **Standard Deviation** | $\sigma = \sqrt{npq}$ |

**Applications**

- Number of patients improved in a trial.
- Number of ad responses in a campaign.
- Number of items passing quality check.

## **Special Case**

When $n = 1$, **Binomial** becomes **Bernoulli**.

- **Limiting Behavior:** As $n \to \infty \text{(large)}$, $X \sim \text{Binomial}(n, p)$
    - If $npq$ are **not** **small**
        - the Binomial distribution approaches a **Normal Distribution** $X \sim N(np, \sqrt{npq})$ via the Central Limit Theorem.
    - If $np$ or $nq$ are **small**,
        - then it converges to the **Poisson Distribution** $X \sim Poisson(\lambda)$ with parameter $\lambda=np$.