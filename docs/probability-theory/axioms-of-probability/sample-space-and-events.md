# Sample Space and Events

### **Sample Space**

- The **sample space $(Ω)$** is the set of **all possible outcomes** of a random experiment.
- An **element** $(ω ∈ Ω)$ represents a single **outcome or realization**.
- Examples of sample spaces:
    - All outcomes of flipping 5 coins
    - Number of heads in 5 coin flips
    - Daily high temperature
    - Number of emails received in an hour

### **Events and Subsets**

- An **event (A)** is a **subset** of the sample space Ω.
- Example: For 3 coin flips:
    - $Ω$ = {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}
    - Event A: First flip is heads = {HHH, HHT, HTH, HTT}
    - Event B: Second flip is tails = {HTH, HTT, TTH, TTT}

### **Set Operations in Probability**

- **Union $(A ∪ B)$**: Outcomes in A **or** B.
    - More inclusive.
- **Intersection $(A ∩ B)$**: Outcomes in **both** A and B.
    - More restrictive.
- **Complement $(Aᶜ)$**: Outcomes **not in A**.

### **Venn Diagram Intuition**

- Sample space $Ω$ can be visualized as a rectangle.
- Events are subsets (circles) inside $Ω$.
- Area of A / Area of $Ω = P(A)$ when outcomes are equally likely.

### **Additional Derived Rules**

- **Complement Rule**: $P(Aᶜ) = 1 − P(A)$
- **Empty Set**: $P(∅) = 0$
- **Subset Rule**: If $A ⊆ B$, then $P(A) ≤ P(B)$
- **Inclusion-Exclusion Principle**: $P(A ∪ B) = P(A) + P(B) − P(A ∩ B)$
    - We subtract the intersection to avoid counting the overlapping area twice.
    - If the events are mutually exclusive this will be $P(A ∩ B) = 0$.

## Event Types

### **Certain Event**

- $P(S) = 1$
- An event that **always occurs**.
- Denoted by the **sample space SS**.

### **Independent Events**

- Occurrence of one event **does not affect** the other.
- Probability rule: $P(A \cap B) = P(A) \cdot P(B)$

### **Dependent Events**

- Occurrence of one event **does affect** the probability of the other.
- Probability rule: $P(A \cap B) \ne P(A) \cdot P(B)$

### **Mutually Exclusive Events**

- $A \cap B = \emptyset$
- Two or more events **cannot occur at the same time**.
- Example: Drawing a card that is **either a heart or a club** (not both).
- Probability rule: $P(A \cup B) = P(A) + P(B)$
- **Mutually exclusive events are never independent** (unless one has probability zero), because if $A \cap B = 0$, then $P(A \cap B) \ne P(A) \cdot P(B)$ (unless one of them is 0).
- Because mutually exclusive events cannot occur together, knowing that one event has happened means you know the other event definitely did not happen.

### **Mutually Inclusive Events**

- $A \cap B \ne \emptyset$
- Two or more events **can occur together** (they may overlap).
- Example: Drawing a card that is a **king or a heart** (King of Hearts counts in both).

### **Impossible Event**

- $P(\emptyset) = 0$
- An event that **can never occur**.
- Represented by the **empty set $\emptyset$**.

### **Complementary Events**

- $A \cup A^c = S, A \cap A^c = \emptyset$
- Two events $A$ and $A^c$, such that **exactly one must occur**.
- Probability rule: $P(A^c) = 1 - P(A)$