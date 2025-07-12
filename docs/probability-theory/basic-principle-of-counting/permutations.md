# Permutations

## Definition

A **permutation** is an ordered arrangement of objects. The number of permutations of $n$ distinct objects is: 

$$
n! = n \times (n - 1) \times (n - 2) \times \ldots \times 3 \times 2 \times 1
$$

By definition, $0! = 1$.

### Example 1: Arranging Letters

**Question:** How many different ordered arrangements of the letters a, b, and c are possible (without repetition)?

**Solution:**
Each position can be filled as follows:

- 3 choices for the first letter
- 2 choices for the second
- 1 choice for the last

$3 \times 2 \times 1 = 6 \text{ permutations: } abc, acb, bac, bca, cab, cba$

### Example 2: Ranking Students

**Question:** A class has 6 men and 4 women. If all 10 students are ranked uniquely, how many different rankings are possible?

**Solution:** $10! = 3,628,800$ total rankings.

If men are ranked among themselves and women among themselves: $6! \times 4! = 720 \times 24 = 17,280$ rankings.

## Ordering and Replacement

Permutations arise when **order matters** in counting outcomes.

### Order Matters

- Example 1 **(order matters)**: Flipping a Coin
    - Flipping a coin 10 times — number of unique sequences = $2^{10}$ because each flip has 2 outcomes and flips are independent. So, if we create a binary tree, total levels would be 10 and at the last level total leaves would be 1024.
    
    ```
    Level 0:       Start
                   /    \
    Level 1:     H       T
                / \     / \
    Level 2:  H   T   H   T
              ...      ...
    ```
    
    - Order matters here because sequence HT is different from TH.
- General formula for permutations (order matters, **with** replacement):

$$
\text{No. of Sequences (\#)} = n^r
$$

- Example 2 **(order matters, without replacement)**: Poker
    - Dealing 5 cards from a 52-card deck where order matters.
    - Number of ordered 5-card sequences = $52 \times 51 \times 50 \times 49 \times 48$.
    - This is called sampling **without replacement** since cards are not put back in the deck.
    - This can be expressed using factorials: $\frac{52!}{(52 - 5)!} = \frac{52!}{47!}$
- General formula for permutations (order matters, **without** replacement):
    
    $$
    P(n, r) = \frac{n!}{(n-r)!}
    $$
    
    where
    
    $n$ = total number of items to choose from (choices)
    
    $r$ = number of items chosen (sampling)
    

### Order Does Not Matters

When order does**n’t** matter, you divide permutations by $r!$ because each combination can be permuted $r!$ ways which count as the same set. 

General formula for permutations (order doesn’t matters, **without** replacement):

$$
\frac{n!}{(n-r)! r!}
$$

Example of Poker from above:

- Dealing 5 cards from a 52-card deck where order doesn’t matters.
- Number of ordered 5-card sequences = $52 \times 51 \times 50 \times 49 \times 48$.
- A,K,Q,J,10 or 10,J,Q,K,A – anything will work.
- There are $r!$ ways of permuting of above 5 cards uniquely. All the orders are equivalent.
- This can be expressed using factorials: $\frac{52!}{(52 - 5)! 5!} = \frac{52!}{47! 5!}$

The permutation formula counts unique ordered sequences, the combination formula counts unique unordered sets.