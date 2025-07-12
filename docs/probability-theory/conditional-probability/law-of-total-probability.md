# Law of Total Probability

## **Multiplication Law**

An important outcome of conditional probability is the multiplication law. The probability of both A and B happening is equal to the probability of A given B multiplied by the probability of B. Formally:

$$
P(A \cap B) = P(A|B) \times P(B)
$$

This is trivial but very useful, and we will use it all the time.

The multiplication rule expresses the probability of multiple events all occurring together. For events $E1,E2,…,EnE_1, E_2, \ldots, E_n$, the rule states:

$$
P(E_1 E_2 E_3 \cdots E_n) = P(E_1) \times P(E_2 | E_1) \times P(E_3 | E_1 E_2) \times \cdots \times P(E_n | E_1 E_2 \cdots E_{n-1})
$$

In other words, the probability that all events $E_1, E_2, \ldots, E_n$ happen is found by multiplying:

- The probability that $E_1$ occurs,
- The probability that $E_2$ occurs given $E_1$ has occurred,
- The probability that $E_3$ occurs given both $E_1$ and $E_2$ have occurred,
- And so forth, up to the probability that $E_n$ occurs given all previous events $E_1, \ldots, E_{n-1}$.

**Proof Sketch**

To prove this, start with the right-hand side and apply the definition of conditional probability repeatedly:

$$
P(E_1) \times \frac{P(E_1 E_2)}{P(E_1)} \times \frac{P(E_1 E_2 E_3)}{P(E_1 E_2)} \times \cdots \times \frac{P(E_1 E_2 \cdots E_n)}{P(E_1 E_2 \cdots E_{n-1})} = P(E_1 E_2 \cdots E_n)
$$

In this product, all intermediate terms cancel out, leaving: $P(E_1 E_2 \cdots E_n)$ which is the probability that all events occur simultaneously.

## **The Law of Total Probability**

The law of total probability is another key concept. Suppose you break your sample space $\Omega$ into disjoint sets $B_1, B_2, \ldots, B_n$ such that:

$$
\Omega = \bigcup_{i=1}^n B_i
$$

and the sets are disjoint, meaning no overlap between any $B_i$ and $B_j$ if $i \neq j$.

The law of total probability states that for any event A:

$$
P(A) = \sum_{i=1}^n P(A|B_i) \times P(B_i)
$$

This means you can compute the probability of A by summing the conditional probabilities of A given each disjoint set BiB_i, weighted by the probabilities of those sets.

### **Example: Card Suits**

Imagine a deck of 52 cards divided into four disjoint sets: hearts, diamonds, clubs, and spades (each with probability 1/4). Let event A be drawing a red card (hearts or diamonds). Using the law of total probability:

$$
P(A) = P(A|B_1)P(B_1) + P(A|B_2)P(B_2) + P(A|B_3)P(B_3) + P(A|B_4)P(B_4)
$$

where:

- $B_1$ = hearts (red),
- $B_2$ = diamonds (red),
- $B_3$ = clubs (not red),
- $B_4$ = spades (not red).

Calculating,

$$
P(A) = 1 \times \frac{1}{4} + 1 \times \frac{1}{4} + 0 \times \frac{1}{4} + 0 \times \frac{1}{4} = \frac{1}{2}
$$

### **Disjoint Sets and Complements**

A very useful special case is when the sample space is divided into an event B and its complement $B^c$. The law of total probability becomes:

$$
P(A) = P(A|B)P(B) + P(A|B^c)P(B^c)
$$

This expresses the total probability of A happening as a weighted sum over whether B happens or not.