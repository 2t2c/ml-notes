# Solving Linear Equations

## **What**

A **linear equation** is an equation where all variables appear to the power 1 (no exponents, products, or functions like sin or log).

A **system of linear equations** is a set of linear equations with the same variables.

General form (for one equation in nn variables): $a_1x_1 + a_2x_2 + \dots + a_nx_n = b$

It looks like this: $ax+b=c$

- $x$ is the unknown (what we want to find).
- $a,b,c$ are numbers (called **constants**).
- The graph of a linear equation is always a **straight line**.

## **How**

**Number of Variables vs Number of Equations**

- Let $n$  = number of variables
- Let $m$ = number of equations

**Cases**

1. **Exactly determined**
    
    If $m = n$:
    
    - The system *might* have a unique solution.
    - Depends on whether equations are independent.
    - A unique solution means the lines **intersect at one point**.
    
2. **Underdetermined**
    
    If $m < n$:
    
    - Fewer equations than unknowns
    - Infinite solutions (if consistent) or none
    - Example: 2 variables, 1 equation → line in 2D

3. **Overdetermined**
    
    If $m > n$:
    
    - More equations than unknowns
    - May have no solution (inconsistent)
    - If consistent, still can have a unique solution (e.g. in least squares problems)

## **Why**

Understanding the structure of linear systems is key to:

- Linear algebra
- Data science (e.g. regression)
- Physics (e.g. forces in equilibrium)
- Engineering (e.g. circuit analysis)
- Optimization

Linear systems are the building blocks for more complex models in applied math and machine learning.

## Sections

[Methods](Solving%20Linear%20Equations%2022681ba4f78a8080b26dc20e4518ce66/Methods%2022781ba4f78a80fe83ccfa6d4d3770ca.md)