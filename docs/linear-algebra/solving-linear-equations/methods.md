# Methods

## **Matrix methods**

For general $m \times n$ systems

1. **Matrix form**: $A\vec{x} = \vec{b}$
    
    Where:
    
    - $A$ is an $m \times n$ matrix of coefficients
    - $\vec{x}$ is an $n \times 1$ vector of variables
    - $\vec{b}$ is an $m \times 1$ output vector
2. **Gaussian elimination / Row reduction**
    
    Convert to row echelon form, solve via back-substitution
    
    1. **Inverse method** (only if $A$ is square and invertible): $\vec{x} = A^{-1} \vec{b}$
3. **Least squares** (for overdetermined):
    
    Solve: $A\vec{x} = A^T\vec{b}$
    

<aside>
💡

Row echelon form (REF) is a matrix format where all zero rows are at the bottom (not always), and the first non-zero entry (leading entry) in each non-zero row is to the right of the leading entry in the row above it. 

</aside>

## **Substitution / Elimination (Small Systems)**

For small systems (like $2 \times 2$ or $3 \times 3$)

- **Example 1:**

$$
\begin{align*}\text{Given:} \quad & \begin{cases}x + y = 5 \quad \text{(1)} \\2x - y = 4 \quad \text{(2)}\end{cases} \\[5pt]
\text{From (1):} \quad & y = 5 - x \\[5pt]
\text{Substitute into (2):} \quad & 2x - (5 - x) = 4 \\& 2x - 5 + x = 4 \\& 3x = 9 \\& x = 3 \\[5pt]
\text{Substitute back:} \quad & y = 5 - 3 = 2 \\[5pt]
\text{Solution:} \quad & x = 3,\quad y = 2\end{align*}
$$

- **Example 2**
    
    $$
    \begin{align*}\text{Given:} \quad & \begin{cases}2x + 3y = 8 \quad \text{(1)} \\4x - 3y = 4 \quad \text{(2)}\end{cases} \\[5pt]
    \text{Add (1) and (2):} \quad & (2x + 3y) + (4x - 3y) = 8 + 4 \\& 6x = 12 \\& x = 2 \\[5pt]
    \text{Substitute into (1):} \quad & 2(2) + 3y = 8 \\& 4 + 3y = 8 \\& 3y = 4 \\& y = \frac{4}{3} \\[5pt]
    \text{Solution:} \quad & x = 2,\quad y = \frac{4}{3}\end{align*}
    $$
    

## Gaussian Elimination (REF)

To solve a system of linear equations by transforming the system into an upper triangular form (all zeros below the main diagonal), and then using **back-substitution** to find the values of variables. Row echelon form is useful because it simplifies solving linear equations using back-substitution.

A matrix is in **row echelon form (REF)** if:

- The first non-zero element in each row (called the leading entry) can be 1.
- Each leading entry is to the right of the leading entry in the row above.
- Any rows with all zeros are at the bottom of the matrix.

A matrix is in **reduced row echelon form (RREF)** if:

- It meets all the conditions of row echelon form.
- Each leading entry must be 1 and is the only non-zero number in its column.
- No back substitution required. However, it is more expensive.

### **Process**

1. **Start with the system of equations** in standard form.
2. **Form the augmented matrix** $[A|b]$, where $A$ is the coefficient matrix and $b$ is the right-hand side.
3. **Forward Elimination**:
    - Use row operations to create zeros below the pivots (leading coefficients) in each column.
    - The goal is to get an upper triangular matrix $U$ such that $Ux = c.$
4. **Back Substitution**:
    - Once in triangular form, solve the last equation for the last variable.
    - Substitute upward into previous equations to find remaining variables.

### **Row Operations Used**

- Swap two rows
- Multiply a row by a nonzero scalar
- Add or subtract a multiple of one row to another
- Column operations are not used.

**Example:**

$$
\begin{align*}
\text{Given:} \quad
& \begin{cases}
2x + 4y - 2z = 2 \\
4x + 9y - 3z = 8 \\
-2x - 3y + 7z = 10
\end{cases} \\[10pt]

\text{Step 1:} \quad
& \text{Row}_2 \leftarrow \text{Row}_2 - 2 \times \text{Row}_1 \\
& \Rightarrow y + z = 4 \\[5pt]

\text{Step 2:} \quad
& \text{Row}_3 \leftarrow \text{Row}_3 + \text{Row}_1 \\
& \Rightarrow y + 5z = 12 \\[5pt]

\text{Step 3:} \quad
& \text{Row}_3 \leftarrow \text{Row}_3 - \text{Row}_2 \\
& \Rightarrow 4z = 8 \Rightarrow z = 2 \\[10pt]

\text{Echelon Matrix:} \quad
& \left[
\begin{array}{ccc|c}
\mathbf{x} & \mathbf{y} & \mathbf{z} & \mathbf{b} \\
2 & 4 & -2 & 2 \\
0 & 1 & 1  & 4 \\
0 & 0 & 4  & 8
\end{array}
\right] \\[10pt]

\text{Back Substitution:} \quad
& y + z = 4 \Rightarrow y = 2 \\
& 2x + 4y - 2z = 2 \Rightarrow 2x + 8 - 4 = 2 \Rightarrow x = -1 \\[10pt]

\text{Solution:} \quad
& (x, y, z) = (-1, 2, 2)
\end{align*}
$$

## Gauss-Jordan Elimination (Matrix Inversion, RREF)

This method goes further to reduce the matrix to **reduced row echelon form (RREF)** where leading entries are 1 and the only nonzero entries in their columns, which directly gives the solution or the inverse matrix without back substitution.

- Write the matrix $A$ alongside the identity matrix $I$ as an augmented matrix $[A | I]$.
- Use row operations (swap, multiply row by scalar, add/subtract multiples of rows) to transform the left part $A$ into the identity matrix.
- When the left side becomes $I$, the right side of the augmented matrix will be $A^{-1}$, the inverse of $A$.
- If the left side cannot be reduced to $I$, then $A$ is not invertible which can be checked beforehand by calculating $det(A)≠0.$

$$
\begin{align*}
& \text{Start with augmented matrix } [A | I]: \\
& \quad
\left[
\begin{array}{ccc|ccc}
2 & 4 & -2 & 1 & 0 & 0 \\
4 & 9 & -3 & 0 & 1 & 0 \\
-2 & -3 & 7 & 0 & 0 & 1
\end{array}
\right]
\\[12pt]
& \text{Step 1: } R_1 \leftarrow \frac{1}{2} R_1 \\
& \quad
\Rightarrow
\quad
\left[
\begin{array}{ccc|ccc}
1 & 2 & -1 & \frac{1}{2} & 0 & 0 \\
4 & 9 & -3 & 0 & 1 & 0 \\
-2 & -3 & 7 & 0 & 0 & 1
\end{array}
\right]
\\[12pt]
& \text{Step 2: Eliminate below } R_1: \quad
R_2 \leftarrow R_2 - 4R_1, \quad R_3 \leftarrow R_3 + 2R_1 \\
& \quad
\Rightarrow
\quad
\left[
\begin{array}{ccc|ccc}
1 & 2 & -1 & \frac{1}{2} & 0 & 0 \\
0 & 1 & 1 & -2 & 1 & 0 \\
0 & 1 & 5 & 1 & 0 & 1
\end{array}
\right]
\\[12pt]
& \text{Step 3: } R_3 \leftarrow R_3 - R_2 \\
& \quad
\Rightarrow
\quad
\left[
\begin{array}{ccc|ccc}
1 & 2 & -1 & \frac{1}{2} & 0 & 0 \\
0 & 1 & 1 & -2 & 1 & 0 \\
0 & 0 & 4 & 3 & -1 & 1
\end{array}
\right]
\\[12pt]
& \text{Step 4: } R_3 \leftarrow \frac{1}{4} R_3 \\
& \quad
\Rightarrow
\quad
\left[
\begin{array}{ccc|ccc}
1 & 2 & -1 & \frac{1}{2} & 0 & 0 \\
0 & 1 & 1 & -2 & 1 & 0 \\
0 & 0 & 1 & \frac{3}{4} & -\frac{1}{4} & \frac{1}{4}
\end{array}
\right]
\\[12pt]
& \text{Step 5: Eliminate above } R_3: \quad
R_2 \leftarrow R_2 - R_3, \quad R_1 \leftarrow R_1 + R_3 \\
& \quad
\Rightarrow
\quad
\left[
\begin{array}{ccc|ccc}
1 & 2 & 0 & \frac{5}{4} & -\frac{1}{4} & \frac{1}{4} \\
0 & 1 & 0 & -\frac{11}{4} & \frac{5}{4} & -\frac{1}{4} \\
0 & 0 & 1 & \frac{3}{4} & -\frac{1}{4} & \frac{1}{4}
\end{array}
\right]
\\[12pt]
& \text{Step 6: Eliminate } 2 \text{ in } R_1, \text{ column } 2: \quad
R_1 \leftarrow R_1 - 2 R_2 \\
& \quad
\Rightarrow
\quad
\left[
\begin{array}{ccc|ccc}
1 & 0 & 0 & \frac{27}{4} & -\frac{11}{4} & \frac{3}{4} \\
0 & 1 & 0 & -\frac{11}{4} & \frac{5}{4} & -\frac{1}{4} \\
0 & 0 & 1 & \frac{3}{4} & -\frac{1}{4} & \frac{1}{4}
\end{array}
\right]
\\[12pt]
& \text{So, inverse matrix } A^{-1} =
\begin{bmatrix}
\frac{27}{4} & -\frac{11}{4} & \frac{3}{4} \\
-\frac{11}{4} & \frac{5}{4} & -\frac{1}{4} \\
\frac{3}{4} & -\frac{1}{4} & \frac{1}{4}
\end{bmatrix}
\\[12pt]
& \text{Multiply } A^{-1} \text{ by } b =
\begin{bmatrix}
2 \\
8 \\
10
\end{bmatrix}:
\quad
x = A^{-1} b = 
\begin{bmatrix}
-1 \\
2 \\
2
\end{bmatrix}
\end{align*}
$$

## **Solution Types (2D)**

- **Unique solution**: consistent and independent i.e. the lines intersect
    - Example: $y = 5 - x$,  $y = x - 1$ cross at $(3, 2)$
- **Infinite solutions**: consistent but dependent i.e. if the two equations are actually the same.
    - Example: $2y = 6x + 8$ and $y = 3x + 4$
- **No solution**: inconsistent system i.e. if the lines are parallel
    - Example $y = x + 3$ and $y = x - 1$

## **Solution Types (3D)**

1**. Unique solution**

- **Algebraic:** System is **consistent** and **all equations are independent**.
- **Geometric (3 variables):** Three planes intersect at **exactly one point**.
- **Example:**
    
    $$
    \begin{cases}
    x + y + z = 6 \\
    2x - y + z = 3 \\
    x + 2y - z = 4
    \end{cases}
    $$
    
- **Interpretation:**
    
    The three planes meet at a single point, giving exactly one solution $(x, y, z)$.
    

2. **Infinite solutions**

- **Algebraic:** System is **consistent but dependent** (some equations are multiples or linear combinations of others).
- **Geometric (3 variables):**
    - The planes intersect along a **line** (all points on the line satisfy the system), or
    - All three planes coincide (overlap completely).
- **Example:**
    
    $$
    \begin{cases}
    x + y + z = 3 \\
    2x + 2y + 2z = 6 \\
    x - y = 1
    \end{cases}
    $$
    
- **Interpretation:**
    
    The first two equations represent the **same plane** (second is just twice the first).
    
    The third plane intersects this plane in a **line**, so infinitely many points satisfy all three.
    

3. **No solution**

- **Algebraic:** System is **inconsistent** (contradictory equations).
- **Geometric (3 variables):**
    - The planes do **not all intersect in a common point or line**.
    - For example, two planes might be parallel but distinct, so no common intersection.
- **Example:**
    
    $$
    \begin{cases}
    x + y + z = 4 \\
    2x + 2y + 2z = 10 \\
    x - y = 1
    \end{cases}
    $$
    
- **Interpretation:**
    
    The second equation contradicts the first (if multiplied by 2, the right side should be 8, not 10). 
    
    So no point exists that satisfies all three equations simultaneously.
    

## Summary of Methods  (Others)

1. **Gaussian Elimination** – Row reduction to row echelon form.
2. **Gauss-Jordan Elimination** – Row reduction to reduced row echelon form.
3. **Matrix Inversion** – If $A\mathbf{x} = \mathbf{b}$, then $\mathbf{x} = A^{-1}\mathbf{b}$ (if $A$ is invertible).
4. **Cramer's Rule** – Uses determinants, applicable only when $A$ is square and $\det(A) \neq 0$.
5. **LU Decomposition** – Factor $A = LU$, then solve via forward and backward substitution.
6. **Cholesky Decomposition** – For symmetric positive-definite $A$, factor as $A = LL^T$.
7. **QR Decomposition** – Factor $A = QR$, then solve  $Rx = Q^Tb$.
8. **Singular Value Decomposition (SVD)** – For general or ill-conditioned systems.
9. **Iterative Methods** – e.g., Jacobi, Gauss-Seidel, Conjugate Gradient (for large sparse systems).

## References

1. https://www.youtube.com/watch?v=eDb6iugi6Uk
2. https://www.youtube.com/watch?v=hu6B1d3vvqU