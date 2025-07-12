# Basic Principle of Counting

Probability helps us determine how likely an event is to happen. To put simply, probability is counting the number of ways an event *can* happen divided by the number of *total possible outcomes that can happen*.

$$
\text{Probability of Event A} = \frac{\text{Number of outcomes where A occurs}}{\text{Total number of possible outcomes}}
$$

## The Basic Principle of Counting

If you are doing two things one after the other, and the first thing can happen in **m** ways, and for each of those, the second thing can happen in **n** ways, then the total number of possible outcomes is **m × n**.

**Why this is true:**

You can list out every possible combination. For each of the **m** options from the first thing, there are **n** options from the second thing. So you end up with **m rows**, and each row has **n** items. This means there are **m × n** total combinations.

## Simple Examples

### Example 1: Flipping Two Coins

**Question:** What is the probability of getting *at least one heads*?

- Sample space $(Ω)$: ${\{HH, HT, TH, TT\}}$ → 4 outcomes
- Event A: at least one heads → {HH, HT, TH} → 3 outcomes → $P(A) = \frac{3}{4} = 0.75$

**Question:** What is the probability of *no heads*?

- Event B: no heads → ${TT}$ → 1 outcome → $(B) = \frac{1}{4} = 0.25$

### Example 2: Rolling Two Dice

**Question:** What is the probability that *at least one die is a 5*?

- Total possible outcomes: 6 × 6 = 36
- Favorable outcomes:
    - First die is 5 → (5,1) to (5,6): 6 outcomes
    - Second die is 5 but first is not → (1,5), (2,5), (3,5), (4,5), (6,5): 5 outcomes
    - Total favorable = 6 + 5 = 11
    - Probability: $P(A) = \frac{11}{36}$

### Example 3: Choosing Samples

**Question:** There are 10 women. Each woman has 3 children. You want to pick one woman **and** one of **her** children for best mother-child pair award.

- First, you have 10 choices for the woman (m options).
- Then, for each woman, you have 3 choices (her children) (n options).
- So the total number of different choices is: **10 × 3 = 30** choices.

## Counting as the Foundation

When events become more complex (e.g., flipping 1000 coins, or rolling 15 dice), **brute-force enumeration becomes impractical**. This is where probability theory evolves into using:

- **Combinatorics** (permutations and combinations)
- **Formulas** and **models** (e.g., binomial theorem, distributions)
- **Set theory and logic** (to define events clearly)

**Key Assumptions (in Basic Models)**

1. **Uniform Probability**: All outcomes are equally likely (fair coin, fair die).
2. **Independence**: Events do not affect each other (each flip or roll is independent).

**What Is Random?**

A process is “random” if we cannot predict its outcome with the information available.

- **Deterministic but unknown**: A coin flip is physically deterministic, but too complex to model precisely—so we treat it as random.
- **Truly stochastic**: Radioactive decay is genuinely random (quantum uncertainty).

### Applications of Counting & Probability

- Games (poker, dice, darts)
- Weather forecasts
- Medical diagnostics
- Failure modeling in engineering
- Financial risk assessment
- Machine learning and AI

## Sections

[Permutations](Basic%20Principle%20of%20Counting%2022b81ba4f78a803faaf1ef14487f3b5c/Permutations%2022b81ba4f78a8044b519e9ce1ba5b5bf.md)

[Combinations](Basic%20Principle%20of%20Counting%2022b81ba4f78a803faaf1ef14487f3b5c/Combinations%2022b81ba4f78a802a9aecff975897b517.md)