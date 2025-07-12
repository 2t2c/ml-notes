# Bayes Theorem

## **Introduction and Intuition**

Bayes' Theorem is one of the most powerful and widely-used tools in probability and statistics. It allows us to **update our beliefs** about an event based on new evidence, and is essential in:

- **Statistics**
- **Machine Learning (especially Bayesian models)**
- **Medical diagnosis**
- **Inverse problems in engineering and science**

## **Conditional Probability Refresher**

We define the probability of event A given that event B has occurred as:

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

This represents an **update** to the probability of A when we know that B has happened.

## **Multiplication Rule**

From the definition above, we also get: $P(A \cap B) = P(A|B) \cdot P(B)$

This is known as the **multiplication rule**, and it can also be written as: $P(B \cap A) = P(B|A) \cdot P(A)$

This symmetry is important and is used to derive Bayes' Theorem.

## **Why Do We Want to Reverse the Conditioning?**

Often, we know:

- $P(\text{symptom} \mid \text{disease})$: how likely the symptom is *if* someone has the disease.

But what we want is:

- $P(\text{disease} \mid \text{symptom})$: how likely someone has the disease *given* the symptom (this is the **inverse problem**).

This reversal is essential in **diagnostics, prediction, and decision making**.

## **Bayes’ Theorem (Basic Form)**

$$
P(B|A) = \frac{P(A|B) \cdot P(B)}{P(A)}
$$

This is derived by noting:

- $P(A \cap B) = P(A|B) \cdot P(B) = P(B|A) \cdot P(A)$

### **Bayesian Terminology**

- **Posterior** $P(B|A)$: updated belief after seeing evidence A.
- **Likelihood (Update)** $P(A|B)$: probability of seeing evidence A if B is true.
- **Prior** $P(B)$: belief about B before seeing evidence.
- **Evidence** **(Marginal)** $P(A)$: total probability of observing A (normalizing constant).

Bayes’ Theorem expresses: $\text{Posterior} = \frac{\text{Likelihood} \times \text{Prior}}{\text{Evidence}}$

## **Bayes’ Theorem (Extended Form: Law of Total Probability)**

Often, $P(A)$ is hard to compute directly. But we can break it into components using the **law of total probability**:

$$
P(A) = P(A|B) \cdot P(B) + P(A|B^c) \cdot P(B^c)
$$

So the full expression becomes:

$$
P(B|A) = \frac{P(A|B) \cdot P(B)}{P(A|B) \cdot P(B) + P(A|B^c) \cdot P(B^c)}
$$

This is extremely useful when we only know conditional probabilities and priors.

## **Bayes’ Theorem (General Form for Partitioned Sample Space)**

If events $B_1, B_2, ..., B_n$ form a **partition** of the sample space (disjoint and exhaustive), then:

$$
P(B_j|A) = \frac{P(A|B_j) \cdot P(B_j)}{\sum_{i=1}^n P(A|B_i) \cdot P(B_i)}
$$

This is useful in multiclass classification and hypothesis testing with multiple possible causes.

## **Example: Cancer Screening Paradox**

### **Setup:**

- Test is **99% accurate**.
    - $P(\text{+}|\text{disease}) = 0.99$
    - $P(\text{+}|\text{no disease}) = 0.01$
- Disease is **rare**:
    - $P(\text{disease}) = 0.001$
        - i.e. only 1 in 1000 people have the disease
    - $P(\text{no disease}) = 0.999$

We want: $P(\text{disease}|\text{+})$

### **Apply Bayes’ Theorem:**

$$
P(\text{disease}|\text{+}) = \frac{P(\text{+}|\text{disease}) \cdot P(\text{disease})}{P(\text{+}|\text{disease}) \cdot P(\text{disease}) + P(\text{+}|\text{no disease}) \cdot P(\text{no disease})}
$$

$$
=\frac{0.99 \cdot 0.001}{0.99 \cdot 0.001 + 0.01 \cdot 0.999} \approx \frac{0.00099}{0.00099 + 0.00999} = \frac{0.00099}{0.01098} \approx 0.09
$$

### **Interpretation:**

Even with a 99% accurate test, the chance you **actually have cancer** given a positive result is only **9%**.

Why? Because the **disease is so rare**, the **false positives dominate**.

This is why positive results in screening often lead to **secondary confirmatory tests**.

### **Sequential Updates and Priors**

Bayesian reasoning supports **sequential data updates**:

1. Start with a **prior** (e.g., the coin is fair).
2. Gather data (e.g., coin shows tails 10 times).
3. Compute the **posterior** (updated belief).
4. Use that posterior as the **new prior** for the next observation.
5. Repeat.

This principle is at the heart of **Bayesian machine learning**, e.g., in:

- Bayesian optimization
- Bayesian networks
- Bayesian deep learning

Bayesian thinking is about **updating beliefs** with new evidence. In practice, prior knowledge and base rates **dramatically affect interpretation**, especially for **rare events**. Think carefully about what you can measure (e.g., test results) vs. what you really want to know (e.g., actual condition).