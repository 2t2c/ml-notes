# Introduction

## **Conditional Probability: Core Concept**

- Conditional probability allows you to update the probability of an event **A** given that another event **B** has occurred.
- It answers: *How does knowing that B happened affect the likelihood of A?*

### **Notation and Definition**

- Written as: $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$
- This is the probability that both A and B happen, divided by the probability that B happens.
- Conceptually: zoom into the space where B is true and ask how likely A is inside that space.

### **Visual Interpretation**

- Imagine the total probability space as a big set Ω.
- Event A is a subset of Ω; event B is another subset.
- When B happens, we restrict our view to only the region B.
- Then P(A∣B)P(A \mid B) is the ratio of the overlapping part of A and B to the total area of B.

### **Key Insight**

- **Learning B changes your belief about A.**
- In some cases, it does not change (events are independent), but often it **does**.
- Conditional probability is a way to **refine or update** your expectations based on partial information.

## **Examples**

1. **Dice Rolls (Independent Events)**
    - A: first die is 3
    - B: second die is 5
    - $P(A \mid B) = P(A) = \frac{1}{6}$ → B tells you nothing about A.
2. **Dice and Sum (Dependent Events)**
    - A: first die is 3 → $P(A) = 6/36 = 1/6$
    - C: sum of both dice is 6 → $P(C) = 5/36$
    - Knowing the total is 6 **does** affect the chance the first die is 3. You have fewer valid (die1, die2) pairs to consider.
    - Possible outcomes where sum is 6:
        - (1,5), (2,4), (3,3), (4,2), (5,1) → 5 outcomes
        - Only (3,3) has first die = 3 → 1 outcome
        - $P(A \mid C) = \frac{1}{5}$
3. **Cards (Partial Information Impact)**
    - A: card is a spade (4 suits): $P(A) = \frac{1}{4}$
    - B: card is black (2 reds, 2 blacks): $P(B) = \frac{2}{4}= \frac{1}{2}$
    - Since spades are black, $A \subseteq B$, so knowing the card is black narrows it to spade or club.
        
        $P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{\frac{1}{4}}{\frac{1}{2}} = \frac{1}{2}$
        
    - If card is red → $P(\text{spade} \mid \text{red}) = 0$

## **Real-World Application: Medical Testing (Inverse Problems)**

- A: test result is positive
- B: person has cancer
- $P(A \mid B) = 90\%$ – test catches 90% of real cases
- But what we really want: $P(B \mid A)$: the chance someone has cancer given a positive test → this is *not* 90% due to false positives.
- This is an **inverse problem**: estimating a hidden cause (B) from an observed effect (A).
- Solving these inverse problems requires **Bayes Theorem**.

## **Why Conditional Probability Matters**

- It enables **inference**: making judgments from partial information.
- Crucial for **machine learning**, **diagnostic tests**, **recommendation systems**, and **risk analysis**.
- Foundation for **Bayesian reasoning**, which we use to update beliefs under uncertainty.