# Axioms of Probability

## **What**

The **axioms of probability** are the foundational rules that define valid probability measures in any probability space. There are **three key axioms**:

1. **Axiom 1: Non-negativity**
    
    $0 \leq P(A) \leq 1$ for any event $A$.
    
    Defines: probability that the outcome of the experiment is an outcome in $A$ is some number between 0 and 1.
    
2. **Axiom 2: Normalization (Total Probability)**
    
    $P(S)=1$ where $S$ is the sample space.
    
    Defines: with probability 1, the outcome will be a point in the sample space $S$.
    
3. **Axiom 3: Countable Additivity (Disjoint Events)**
    
    If $A∩B=∅$, then $P(A \cup B) = P(A) + P(B)$
    
    Defines: for any sequence of mutually exclusive events, the probability of at least one of these events occurring is just the sum of their respective probabilities.
    
    For any sequence of **mutually exclusive** events $E1, E2, ...$  (that is, events for
    which $E_iE_j= Ø$ when $i ≠ j$),
    
    $$
    P\left( \bigcup_{i=1}^{\infty} E_i \right) = \sum_{i=1}^{\infty} P(E_i)
    
    $$
    
    We refer to $P(E)$ as the probability of the event $E$.
    

## **How**

These axioms are applied to:

- Ensure probability values are valid (between 0 and 1)
- Build complex probabilities from simple events (e.g., unions, complements)
- Derive further rules like:
    - $P(A^c) = 1 - P(A)$
        - $A^c$ or $A`$ means everything but $A$ inside sample space $S$
        - $^c$ or $`$ is called as a complement in Set Theory.
    - $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
    - Inclusion–exclusion principle

## **Why**

- **Logical consistency:** Forms the basis of probability theory
- **Scalability:** Allows building rules for combinations, sequences, and conditional events
- **Universality:** All valid probability models (discrete or continuous) obey these axioms
- **Practicality:** Used in statistics, machine learning, risk analysis, etc.

## Sections

[Sample Space and Events](Axioms%20of%20Probability%2022b81ba4f78a80d7b990e2b0f0c2926f/Sample%20Space%20and%20Events%2022b81ba4f78a804b86c9cea4973f7d77.md)