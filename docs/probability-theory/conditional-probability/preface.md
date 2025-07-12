# Conditional Probability

## **What**

**Conditional Probability** is the probability of an event **A** occurring given that another event **B** has already occurred.

It is denoted as: $P(A \mid B)$

This expresses how the likelihood of **A** changes when we know **B** has happened.

## **How**

The conditional probability is calculated using the formula: 

If $P(B) > 0$, then

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
$$

Where:

- $P(A \cap B)$ is the probability that **both A and B** occur.
- $P(B)$ is the probability that **B** occurs (must be > 0).

### Example:

If flipping two coins:

- Let A = first flip is heads
- Let B = both flips are heads
    
    Then,
    

$$
P(A \mid B) = \frac{P(\text{first = H and both = HH})}{P(\text{both = HH})} = \frac{P(HH)}{P(HH)} = 1
$$

## **Why**

Conditional probability is essential because:

- It allows **updating beliefs** when new information is known (Bayesian reasoning).
- It helps model **dependent events** (where the outcome of one event affects another).
- It is foundational for concepts like **Bayes’ Theorem**, **Markov Chains**, and **Machine Learning models**.

It moves probability from static, one-time events to dynamic, **context-aware inference**.

## **Sections**

[Introduction](Conditional%20Probability%2022d81ba4f78a80d0b53ff357e4a94f69/Introduction%2022d81ba4f78a8060b2bcc6f98a4dcf20.md)

[Law of Total Probability](Conditional%20Probability%2022d81ba4f78a80d0b53ff357e4a94f69/Law%20of%20Total%20Probability%2022d81ba4f78a808f9e5cf92807e8aa20.md)

[Bayes Theorem](Conditional%20Probability%2022d81ba4f78a80d0b53ff357e4a94f69/Bayes%20Theorem%2022d81ba4f78a8051a00ddf0d108ffea3.md)

[Independence](Conditional%20Probability%2022d81ba4f78a80d0b53ff357e4a94f69/Independence%2022d81ba4f78a8036b396f752f6cfdd98.md)