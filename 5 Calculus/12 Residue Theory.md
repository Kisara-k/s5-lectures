## 12. Residue Theory

## Key Points

#### 1. 🧩 Isolated Singularities  
- A point $\alpha$ is an isolated singularity of $f$ if $f$ is not analytic at $\alpha$ but analytic in some punctured neighborhood $0 < |z-\alpha| < R$.  
- Types of isolated singularities are classified by the Laurent series coefficients $a_k$ for $k < 0$.

#### 2. 🔍 Classification of Singularities  
- **Removable singularity:** $a_k = 0$ for all $k < 0$.  
- **Pole of order $n$:** $a_{-n} \neq 0$ and $a_k = 0$ for all $k < -n$.  
- **Essential singularity:** Infinitely many $a_k \neq 0$ for $k < 0$.

#### 3. 🧮 Residue Definition  
- The residue of $f$ at $\alpha$, $\text{Res}[f, \alpha]$, is the coefficient $a_{-1}$ in the Laurent series expansion around $\alpha$.

#### 4. ⚙️ Zeros of Analytic Functions  
- $f$ has a zero of order $k$ at $\alpha$ if $f^{(n)}(\alpha) = 0$ for $n=0,1,\ldots,k-1$ and $f^{(k)}(\alpha) \neq 0$.  
- Equivalently, $f(z) = (z-\alpha)^k g(z)$ where $g$ is analytic and $g(\alpha) \neq 0$.

#### 5. 🕳️ Poles and Their Characterization  
- $f$ has a pole of order $k$ at $\alpha$ if $f(z) = \frac{h(z)}{(z-\alpha)^k}$ with $h$ analytic and $h(\alpha) \neq 0$.  
- If $f$ has a zero of order $k$ at $\alpha$, then $1/f$ has a pole of order $k$ at $\alpha$, and vice versa.

#### 6. 🔗 Behavior of Products and Quotients  
- Product of zeros: zeros of orders $m$ and $n$ multiply to zero of order $m+n$.  
- Product of poles: poles of orders $m$ and $n$ multiply to pole of order $m+n$.  
- Quotient $h = f/g$ with zeros of orders $m$ and $n$ at $\alpha$:  
  - If $m > n$, $h$ has a removable singularity and zero of order $m-n$.  
  - If $m < n$, $h$ has a pole of order $n-m$.  
  - If $m = n$, $h$ has a removable singularity and can be defined analytic at $\alpha$.

#### 7. 🧮 Residue Calculation at Poles  
- For a pole of order $n$ at $\alpha$,  

$$
\text{Res}[f, \alpha] = \frac{1}{(n-1)!} \lim_{z \to \alpha} \frac{d^{n-1}}{dz^{n-1}} \left[ (z-\alpha)^n f(z) \right]
$$


#### 8. 📜 Cauchy's Residue Theorem  
- If $f$ is analytic inside and on a simple closed contour $C$, except for isolated singularities $z_1, z_2, \ldots, z_n$ inside $C$, then  

$$
\int_C f(z) \, dz = 2\pi i \sum_{k=1}^n \text{Res}[f, z_k]
$$


#### 9. 🚫 Residue at Removable Singularities  
- If $\alpha$ is a removable singularity, then  

$$
\text{Res}[f, \alpha] = 0
$$



<br>

## Study Notes

### 1. 🧩 Introduction to Residue Theory and Singularities

Residue theory is a powerful tool in complex analysis, especially useful for evaluating complex integrals and understanding the behavior of complex functions near points where they fail to be analytic. The key idea revolves around studying **singular points** of complex functions and using their **residues** to compute integrals via the famous **Cauchy Residue Theorem**.

#### What is a Singular Point?

A **singular point** (or singularity) of a complex function $f(z)$ is a point $\alpha$ where the function is **not analytic**, but in every neighborhood around $\alpha$, there are points where $f$ *is* analytic. This means the function "breaks down" only at $\alpha$, but behaves nicely nearby.

More specifically, if there exists a radius $R > 0$ such that $f$ is analytic everywhere in the punctured disk $D_R^*(\alpha) = \{ z : 0 < |z - \alpha| < R \}$, then $\alpha$ is called an **isolated singularity**. This isolation is important because it allows us to study the function's behavior near $\alpha$ without interference from other singularities.

**Example:**  
Consider $f(z) = \frac{1}{1-z}$. This function is not analytic at $z=1$ (division by zero), but analytic everywhere else. Hence, $z=1$ is an isolated singularity.


### 2. 🔍 Classification of Isolated Singularities

Isolated singularities come in three main types, classified by the behavior of the function's **Laurent series** expansion around the singularity.

#### Laurent Series Recap

For $f$ with an isolated singularity at $\alpha$, we can write:


$$
f(z) = \sum_{k=-\infty}^{\infty} a_k (z - \alpha)^k
$$


valid for $0 < |z - \alpha| < R$.

#### Types of Singularities

1. **Removable Singularity**  
   If all coefficients $a_k = 0$ for $k < 0$, the singularity is removable. This means the function behaves like an analytic function except possibly at $\alpha$, and we can redefine $f(\alpha)$ to make it analytic there.

2. **Pole of Order $n$**  
   If there exists a finite negative power $-n$ such that $a_{-n} \neq 0$ but $a_k = 0$ for all $k < -n$, then $\alpha$ is a pole of order $n$. The function "blows up" like $\frac{1}{(z-\alpha)^n}$ near $\alpha$.

3. **Essential Singularity**  
   If infinitely many negative powers $a_k \neq 0$ for $k < 0$, the singularity is essential. The function behaves very wildly near $\alpha$, with no simple pole-like behavior.

#### Residue Definition

The **residue** of $f$ at $\alpha$, denoted $\text{Res}[f, \alpha]$, is the coefficient $a_{-1}$ in the Laurent series. This coefficient plays a crucial role in evaluating integrals around $\alpha$.


### 3. ⚙️ Zeros of Analytic Functions and Their Orders

Understanding zeros of analytic functions is essential because zeros and poles are closely related.

#### Zero of Order $k$

A function $f$ analytic at $\alpha$ has a **zero of order $k$** at $\alpha$ if:

- $f(\alpha) = f'(\alpha) = \cdots = f^{(k-1)}(\alpha) = 0$, but
- $f^{(k)}(\alpha) \neq 0$.

This means the function "touches zero" at $\alpha$ with multiplicity $k$.

**Example:**  
$f(z) = z \sin(z^2)$ has a zero of order 3 at $z=0$.

#### Taylor Series Characterization

The Taylor series of $f$ around $\alpha$ will have the first $k$ coefficients zero:


$$
f(z) = c_k (z-\alpha)^k + c_{k+1} (z-\alpha)^{k+1} + \cdots
$$


with $c_k \neq 0$.

#### Factorization Form

A function with a zero of order $k$ at $\alpha$ can be written as:


$$
f(z) = (z - \alpha)^k g(z)
$$


where $g$ is analytic at $\alpha$ and $g(\alpha) \neq 0$.


### 4. 🕳️ Poles and Their Orders

Poles are the "opposite" of zeros in a sense. A pole of order $k$ at $\alpha$ means the function behaves like $\frac{1}{(z-\alpha)^k}$ near $\alpha$.

#### Characterization of Poles

If $f$ has a pole of order $k$ at $\alpha$, then:


$$
f(z) = \frac{h(z)}{(z-\alpha)^k}
$$


where $h$ is analytic at $\alpha$ and $h(\alpha) \neq 0$.

#### Relationship Between Zeros and Poles

- If $f$ has a zero of order $k$ at $\alpha$, then $g(z) = \frac{1}{f(z)}$ has a pole of order $k$ at $\alpha$.
- Conversely, if $f$ has a pole of order $k$ at $\alpha$, then $g(z) = \frac{1}{f(z)}$ has a zero of order $k$ at $\alpha$.

#### Products and Quotients

- The product of two functions with zeros of orders $m$ and $n$ at $\alpha$ has a zero of order $m + n$.
- The product of two functions with poles of orders $m$ and $n$ at $\alpha$ has a pole of order $m + n$.
- For the quotient $h(z) = \frac{f(z)}{g(z)}$, where $f$ and $g$ have zeros of orders $m$ and $n$ at $\alpha$:
  - If $m > n$, $h$ has a removable singularity at $\alpha$ and a zero of order $m-n$.
  - If $m < n$, $h$ has a pole of order $n-m$.
  - If $m = n$, $h$ has a removable singularity and can be defined to be analytic at $\alpha$.


### 5. 🧮 Calculating Residues

Residues are central to evaluating complex integrals via the residue theorem.

#### Residue at a Removable Singularity

If $\alpha$ is a removable singularity, then all negative powers in the Laurent series vanish, so:


$$
\text{Res}[f, \alpha] = 0
$$


#### Residue at a Pole of Order $n$

If $\alpha$ is a pole of order $n$, the residue can be computed by:


$$
\text{Res}[f, \alpha] = \frac{1}{(n-1)!} \lim_{z \to \alpha} \frac{d^{n-1}}{dz^{n-1}} \left[ (z-\alpha)^n f(z) \right]
$$


This formula allows us to extract the coefficient $a_{-1}$ without explicitly finding the full Laurent series.


### 6. 📜 Cauchy's Residue Theorem

This theorem is the cornerstone of residue theory and complex integration.

#### Statement

Let $D$ be a simply connected domain and $C$ a simple closed positively oriented contour inside $D$. Suppose $f$ is analytic on and inside $C$, except for isolated singularities $z_1, z_2, \ldots, z_n$ inside $C$. Then:


$$
\int_C f(z) \, dz = 2\pi i \sum_{k=1}^n \text{Res}[f, z_k]
$$


This means the integral of $f$ around $C$ depends only on the sum of residues at the singularities inside $C$.

#### Importance

This theorem simplifies the evaluation of complex integrals, especially those difficult to compute by direct methods. It is widely used in physics, engineering, and applied mathematics.


### 7. 🧩 Examples and Applications

#### Example 1: Removable Singularities

- $f(z) = \frac{\sin z}{z}$ has a removable singularity at $z=0$ because $\sin z \approx z - \frac{z^3}{6} + \cdots$, so $\frac{\sin z}{z} \to 1$ as $z \to 0$.
- $g(z) = \cos z - 1$ also has a removable singularity at $z=0$ since $\cos z - 1 \approx -\frac{z^2}{2} + \cdots$.

#### Example 2: Poles

- $f(z) = \frac{\sin z}{z^3}$ has a pole of order 2 at $z=0$ because dividing by $z^3$ introduces negative powers.
- $g(z) = \frac{z}{e^z}$ has a simple pole (order 1) at $z=0$.

#### Example 3: Zeros

- $f(z) = z \sin z^2$ has a zero of order 3 at $z=0$.

#### Example 4: Using Residue Theorem

- To evaluate integrals like $\int_C \frac{\pi \cot(\pi z)}{z} dz$ where $C$ is a circle, find residues at singularities inside $C$ and apply the residue theorem.


### Summary

Residue theory provides a structured way to analyze complex functions near their singularities and compute complex integrals efficiently. Key concepts include:

- **Isolated singularities** and their classification (removable, poles, essential).
- **Zeros of analytic functions** and their orders.
- The relationship between zeros and poles.
- **Residues** as coefficients in Laurent expansions.
- The **Cauchy Residue Theorem** for evaluating integrals.

Mastering these concepts is essential for complex analysis and has practical applications in many scientific fields.