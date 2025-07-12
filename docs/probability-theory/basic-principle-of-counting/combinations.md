# Combinations

## Definition

We are often interested in determining how many **different groups of $r$ objects** can be formed from a total of $n$ distinct objects, **when the order of selection does not matter**.

## Derivation

To count the number of such groups:

- If **order mattered**, we would have: $n(n - 1)(n - 2)\cdots(n - r + 1) = \frac{n!}{(n - r)!}$
- But each group is **counted $r!$ times** (all permutations of $r$ items), so we divide:
    
    $$
    \text{Number of combinations} = \frac{n!}{r!(n - r)!}
    $$
    

### Notation and Terminology

The number of combinations is denoted as:

$$
^nC_r = \binom{n}{r} = \frac{n!}{r!(n - r)!}
$$

- Where,
    - $n$ = No. of total items
    - $r$ = No. of items chosen at once
    - $0 \leq r \leq n$

<aside>
💡

$^nC_r$ read as “**n choose r**” and represents the number of ways to choose $r$ items from $n$ **without regard to order**.

</aside>

**Special cases:**

- $\binom{n}{n} = \binom{n}{0} = 1$
- $\binom{n}{r} = 0$ if $r > n$ or $r < 0$

### Example: Basic Selection

**How many committees of 3 can be chosen from 20 people?**

$$
^{20}C_3 = \binom{20}{3} = \frac{20 \cdot 19 \cdot 18}{3 \cdot 2 \cdot 1} = 1140
$$

### Example: Grouped Selection

**How many committees of 2 women and 3 men from 5 women and 7 men?**

$$
\binom{5}{2} \cdot \binom{7}{3} = 10 \cdot 35 = 350
$$

**With constraint:**

If 2 men are feuding and cannot serve together, subtract combinations that include both:

We select 1 men from remaining 5 men (because 2 men have already used the restricted space)  and 2 women from all the women.

$$
\text{Total Ways} - \binom{5}{1} \cdot \binom{5}{2}\Rightarrow 350 - 50 = 300
$$

---

### Example: No Consecutive Defectives

**Given $n$ antennas, $m$ defective, and $n - m$ functional, how many arrangements with no two defectives adjacent?**

- Place $n - m$ functional antennas: creates $n - m + 1$ “slots”
- Choose $m$ of those slots: $\binom{n - m + 1}{m}$

## Pascal’s Identity

Pascal's Identity, also known as Pascal's Rule, is **a fundamental combinatorial identity that relates binomial coefficients**. It states that for any positive integers n and k, with k between 1 and n-1, the binomial coefficient (n choose k) is equal to the sum of (n-1 choose k-1) and (n-1 choose k). In simpler terms, each number in Pascal's Triangle is the sum of the two numbers directly above it. 

$$
\binom{n}{r} = \binom{n - 1}{r - 1} + \binom{n - 1}{r}
$$

**Interpretation:** Count of size-r groups that **include** a specific item + those that **exclude** it.

Ts a fundamental identity in combinatorics that expresses a recursive relationship between binomial coefficients:

## Binomial Theorem

The binomial theorem is primarily used **to expand expressions of the form $(x + y)ⁿ$, where $n$ is a non-negative integer**. It provides a formula to find the coefficients and terms in the expanded form of such expressions without direct multiplication. Beyond basic algebra, it has applications in various fields like probability, statistics, and even disaster prediction. 

$$
(x + y)^n = \sum_{k = 0}^{n} \binom{n}{k} x^k y^{n - k}
$$

Each term in the expansion corresponds to choosing $k$ of the $n$ terms to be $x$, and the rest $y$.

### Example: Expand $(x + y)^3$

$$
\begin{gathered}
(x + y)^3 = \binom{3}{0}x^0y^3 + \binom{3}{1}x^1y^2 + \binom{3}{2}x^2y^1 + \binom{3}{3}x^3y^0  \\[10pt]
= y^3 + 3xy^2 + 3x^2y + x^3
\end{gathered}
$$

### Example: Total Number of Subsets

**How many subsets does a set of $n$ elements have?**

Solution: $\sum_{k = 0}^{n} \binom{n}{k} = 2^n$

**Subsets with at least 1 element:** $2^n - 1$

### Example: Counting Heads

What is the probability of getting **exactly 3 heads** in **5 coin tosses**?

Solution: This is a **binomial experiment**

- Each toss has 2 outcomes: head (H) or tail (T).
- Each outcome is independent.
- Probability of head: p = 0.5, tail: 1−p=0.5.

We use the **binomial probability formula**:

$P(k \text{ heads in } n \text{ tosses}) = \binom{n}{k} p^k (1-p)^{n-k}$

Here, $n = 5, k = 3, p = 0.5$

Where,

- $p$ = Probability of Success
- $q$ = Probability of Failure $(1-p)$
- $n$ = No. of trials
- $k$ = No. of times for a specific outcome within $n$ trials

$$
P(3 \text{ heads}) = \binom{5}{3} (0.5)^3 (0.5)^2 = \binom{5}{3} (0.5)^5 = 10 \times \frac{1}{32} = \frac{10}{32} = 0.3125
$$

So, there is a **31.25%** chance of getting exactly 3 heads in 5 fair coin tosses.

<aside>
💡

**Binomial Theorem vs. Binomial Distribution**

- Binomial theorem is a formula for expanding powers of sums algebraically.
- Binomial distribution applies this formula to model probabilities of successes in repeated independent trials.
</aside>

## Multinomial Theorem

For expanding $(x + y + z)^n$ or $(x_1 + x_2 + \cdots + x_m)^n$, the **multinomial theorem** is used.

It generalizes the binomial theorem to more than two terms. The expansion is:

$$
(x + y + z)^n = \sum_{a+b+c = n} \frac{n!}{a! \, b! \, c!} \, x^a y^b z^c
$$

where $a, b, c \geq 0$ and $a + b + c = n$.

The coefficients $\frac{n!}{a! b! c!}$ are called **multinomial coefficients**.

The general form is:

$$
(x_1 + x_2 + \cdots + x_m)^n = \sum_{a_1 + a_2 + \cdots + a_m = n} \frac{n!}{a_1! a_2! \cdots a_m!} \, x_1^{a_1} x_2^{a_2} \cdots x_m^{a_m}
$$

where each $a_i \geq 0$ and the sum of all $a_i$ equals $n$.

## Summary of Binomial Coefficients

$$
\begin{aligned}
&^nC_0 = \binom{n}{0} = 1 \\
&^nC_n = \binom{n}{n} = 1 \\
&^nC_1 = \binom{n}{1} = n \\
&^nC_r = \binom{n}{r} = \binom{n}{n-r} \quad \text{(symmetry)} \\
&^nC_r = \binom{n}{r} = \frac{n!}{r!(n-r)!} \\
&0! = 1 \\
&^nC_r = \binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r} \quad \text{(Pascal's rule)} \\
&^nC_r = \binom{n}{r} = 0 \quad \text{if } r > n \text{ or } r < 0
\end{aligned}
$$