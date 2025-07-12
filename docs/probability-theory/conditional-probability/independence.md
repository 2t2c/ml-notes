# Independence

## Statistical Independence

**Definition**:

Two events $A$ and $B$ are **independent** if knowing that one of them occurred gives **no additional information** about the probability of the other occurring.

- Formally: $P(A \mid B) = P(A) \quad \text{and} \quad P(B \mid A) = P(B)$

This means that the occurrence of one event does not affect the probability of the other.

## Key Consequence of Independence

If $A$ and $B$ are independent: 

$$
P(A \cap B) = P(A) \cdot P(B)
$$

**Proof using conditional probability**:

We know:

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
$$

If $A$ and $B$ are independent, then $P(A \mid B) = P(A)$, so:

$$
P(A) = \frac{P(A \cap B)}{P(B)} \Rightarrow P(A \cap B) = P(A) \cdot P(B)
$$

## Example: Deck of Cards

For a single card draw:

- Let $A$: card is a **Spade** → $P(A) = \frac{13}{52} = \frac{1}{4}$
- Let $B$: card is a **Queen** → $P(B) = \frac{4}{52} = \frac{1}{13}$

Then:

- $A \cap B$: card is the **Queen of Spades** → $P(A \cap B) = \frac{1}{52}$
- Since  $\frac{1}{4} \cdot \frac{1}{13} = \frac{1}{52}$, $A$ and $B$ are independent.

Selecting either of the cards won’t affect the probability of the other one. 

Graphically, you can imagine the full deck as a grid of suits and ranks. The Spades form 1/4 of the set, and the Queens form 1/13. Their intersection, the Queen of Spades is just one card out of 52.

## Example: Non-Independent Event

For a single card draw:

- $A$: selecting a black card → 26 black cards (Spades + Clubs)
    - $P(A) = \frac{26}{52} = \frac{1}{2}$
- $B$: selecting a spade → 13 cards
    - $P(B) = \frac{13}{52} = \frac{1}{4}$
- $P(A \cap B) = P(\text{card is a spade}) = \frac{13}{52} = \frac{1}{4}$

Since $P(A) \cdot P(B) = \frac{1}{8} \neq \frac{1}{4} = P(A \cap B)$, the events are **dependent**. This makes intuitive sense: if you know a card is black, you've increased the probability it's a spade from 1/4 to 1/2 (since spades are half of all black cards).

## Independence in Practice: Reliability

### Series Configuration

- **n components** in **series** (e.g., Christmas lights):
    - If **any** component fails, the system fails.
    - Let failure probability of one component be pp
    - Probability of **success**: $P(\text{success}) = (1 - p)^n$
    - Therefore, $P(\text{failure}) = 1 - (1 - p)^n$

**Example**:

If $p = 0.05$, $n = 10$:

$P(\text{failure}) = 1 - (0.95)^{10} \approx 0.40$

So, even components with 95% reliability fail 40% of the time in series.

### Parallel Configuration

- **n components** in **parallel**:
    - System fails only if **all** components fail.
    - Probability of **failure**: $P(\text{failure}) = p^n$

**Example**:

If $p = 0.05$, $n = 10$:

$P(\text{failure}) = (0.05)^{10} \approx 10^{-13}$

So, parallel configurations are **vastly more reliable** under the assumption of independence.