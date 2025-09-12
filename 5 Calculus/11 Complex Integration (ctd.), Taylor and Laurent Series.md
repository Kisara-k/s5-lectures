## 11. Complex Integration (ctd.), Taylor and Laurent Series

## Key Points

#### 1. 🧮 Fundamental Theorems of Complex Integration  
- If $f$ is analytic in a simply connected domain $D$, then the integral $F(z) = \int_{z_0}^z f(w) \, dw$ defines an analytic function with $F'(z) = f(z)$.  
- For any two points $z_0, z_1 \in D$, $\int_{z_0}^{z_1} f(z) \, dz = F(z_1) - F(z_0)$, where $F$ is any antiderivative of $f$.  
- The integral of an analytic function in a simply connected domain depends only on the endpoints, not the path.

#### 2. 🔄 Cauchy's Integral Formula and Derivatives  
- For $f$ analytic in $D$ and $C$ a simple closed contour in $D$, if $z_0$ lies inside $C$, then  

$$
  f(z_0) = \frac{1}{2\pi i} \int_C \frac{f(z)}{z - z_0} \, dz.
$$
  
- The $n$-th derivative of $f$ at $z_0$ is given by  

$$
  f^{(n)}(z_0) = \frac{n!}{2\pi i} \int_C \frac{f(z)}{(z - z_0)^{n+1}} \, dz.
$$
  
- These formulas allow evaluation of function values and derivatives via contour integrals.

#### 3. 📈 Power Series and Convergence  
- A power series $\sum_{n=0}^\infty c_n (z - \alpha)^n$ converges either:  
  a) only at $z = \alpha$,  
  b) inside a disk $D_\rho(\alpha) = \{ z : |z - \alpha| < \rho \}$, or  
  c) everywhere in $\mathbb{C}$.  
- The number $\rho$ is the **radius of convergence**.  
- The series converges uniformly on any closed disk $D_r(\alpha)$ with $r < \rho$.

#### 4. ✍️ Taylor and Maclaurin Series  
- If $f$ is analytic at $\alpha$, its Taylor series is  

$$
  f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(\alpha)}{n!} (z - \alpha)^n.
$$
  
- The Maclaurin series is the Taylor series centered at $\alpha = 0$.  
- Taylor series converges to $f(z)$ inside the largest disk contained in the domain of analyticity.  
- The power series representation of an analytic function is unique.

#### 5. 🔢 Operations on Power Series  
- Sum, scalar multiplication, and product of power series converge to the corresponding operations on functions within the minimum radius of convergence.  
- The product of two power series is given by the **Cauchy product**:  

$$
  c_n = \sum_{k=0}^n a_k b_{n-k}.
$$


#### 6. 🌀 Laurent Series and Annulus Regions  
- A Laurent series centered at $\alpha$ is  

$$
  f(z) = \sum_{n=-\infty}^\infty c_n (z - \alpha)^n,
$$
  
  converging in an annulus $A(r, R, \alpha) = \{ z : r < |z - \alpha| < R \}$.  
- Laurent series converge uniformly on any closed sub-annulus $A(s, t, \alpha)$ with $r < s < t < R$.  
- The coefficients $c_n$ are given by  

$$
  c_n = \frac{1}{2\pi i} \int_{C_\rho(\alpha)} \frac{f(z)}{(z - \alpha)^{n+1}} \, dz,
$$
  
  where $C_\rho(\alpha)$ is a positively oriented circle inside the annulus.

#### 7. ✅ Properties of Laurent Series  
- The Laurent series representation of an analytic function in an annulus is unique.  
- Derivatives of $f$ can be obtained by term-wise differentiation of its Laurent series.



<br>

## Study Notes

### 1. 🧮 Fundamental Theorems of Complex Integration

When studying complex functions, integration plays a crucial role, especially when the functions are analytic (complex differentiable) in a domain. The fundamental theorems of complex integration provide the foundation for evaluating integrals of analytic functions and understanding their properties.

#### Analytic Functions and Simply Connected Domains

- A function $f(z)$ is **analytic** in a domain $D$ if it is complex differentiable at every point in $D$.
- A domain $D$ is **simply connected** if it has no holes; intuitively, any closed loop in $D$ can be continuously shrunk to a point without leaving $D$.

#### Theorem 11.1.1: Indefinite Integrals (Antiderivatives)

If $f$ is analytic in a simply connected domain $D$, and $z_0$ is a fixed point in $D$, then the function


$$
F(z) = \int_{C_z} f(w) \, dw
$$


where $C_z$ is any contour in $D$ from $z_0$ to $z$, is itself analytic in $D$, and its derivative satisfies


$$
F'(z) = f(z).
$$


**Interpretation:** This means that analytic functions have antiderivatives, and the integral from a fixed point to $z$ defines such an antiderivative.

#### Theorem 11.1.2: Definite Integrals

If $f$ is analytic in a simply connected domain $D$, and $z_0, z_1 \in D$, then


$$
\int_{z_0}^{z_1} f(z) \, dz = F(z_1) - F(z_0),
$$


where $F$ is any antiderivative of $f$.

**Interpretation:** The integral of an analytic function between two points depends only on the endpoints, not on the path taken, as long as the path lies entirely in $D$.

#### Examples

- Evaluate integrals like $\int \cos z \, dz$ or $\int e^z \, dz$ using antiderivatives.
- These theorems simplify complex integration by reducing contour integrals to evaluations of antiderivatives.


### 2. 🔄 Integral Representation for Analytic Functions (Cauchy's Integral Formula)

One of the most powerful results in complex analysis is **Cauchy's Integral Formula**, which expresses the value of an analytic function inside a contour in terms of an integral over the contour.

#### Theorem 11.2.1: Cauchy's Integral Formula

Let $f$ be analytic in a simply connected domain $D$, and let $C$ be a simple closed positively oriented contour inside $D$. If $z_0$ lies inside $C$, then


$$
f(z_0) = \frac{1}{2\pi i} \int_C \frac{f(z)}{z - z_0} \, dz.
$$


**Interpretation:** The value of an analytic function at any point inside a closed contour can be recovered exactly by integrating the function around the contour. This formula is fundamental because it links function values to contour integrals.

#### Theorem 11.2.2: Cauchy's Integral Formula for Derivatives

Extending the above, the $n$-th derivative of $f$ at $z_0$ can be expressed as


$$
f^{(n)}(z_0) = \frac{n!}{2\pi i} \int_C \frac{f(z)}{(z - z_0)^{n+1}} \, dz.
$$


**Interpretation:** Not only can we find the function value inside the contour, but all derivatives can be computed via contour integrals, which is a remarkable property unique to analytic functions.

#### Examples

- Evaluate integrals like $\int_C e^z / (z - z_0) \, dz$ where $C$ is a circle.
- Use these formulas to find derivatives of functions inside contours.


### 3. 📈 Taylor and Laurent Series: Power Series Representations of Analytic Functions

Analytic functions can be represented locally by power series, which are infinite sums of powers of $(z - \alpha)$. This is a cornerstone of complex analysis, allowing us to approximate and understand functions deeply.

#### 3.1 Convergence of Sequences and Series of Functions

Before discussing series expansions, it's important to understand how sequences of functions converge.

- **Pointwise convergence:** For each fixed $z$, the sequence $f_n(z)$ converges to $f(z)$.
- **Uniform convergence:** The sequence $f_n$ converges to $f$ uniformly if the speed of convergence does not depend on $z$.

Uniform convergence is stronger and ensures properties like continuity and integrability pass to the limit function.

#### 3.2 Power Series and Radius of Convergence

A **power series** centered at $\alpha$ is


$$
f(z) = \sum_{n=0}^\infty c_n (z - \alpha)^n,
$$


where $c_n$ are complex coefficients.

- The series converges in one of three ways:
  - Only at $z = \alpha$,
  - Inside a disk $D_\rho(\alpha) = \{ z : |z - \alpha| < \rho \}$,
  - Or everywhere in the complex plane.

- The number $\rho$ is called the **radius of convergence**.

Within the radius of convergence, the series converges uniformly on any smaller closed disk.

#### 3.3 Taylor and Maclaurin Series

- If $f$ is analytic at $\alpha$, its **Taylor series** is


$$
f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(\alpha)}{n!} (z - \alpha)^n.
$$


- When $\alpha = 0$, this is called the **Maclaurin series**.

Taylor's theorem guarantees that the Taylor series converges to $f(z)$ inside the largest disk contained in the domain of analyticity.

#### 3.4 Uniqueness and Operations on Power Series

- The power series representation of an analytic function is unique.
- Power series can be added, multiplied, and scaled term-by-term within their radius of convergence.
- The **Cauchy product** formula gives the coefficients of the product of two power series.

#### Examples

- Find Maclaurin series for $\sin z$ and $\sin^3 z$.
- Use Cauchy product to find series for products of functions.


### 4. 🌀 Laurent Series: Series Expansions in Annulus Regions

Sometimes, functions are analytic not in a disk but in an **annulus** (a ring-shaped region). Laurent series generalize Taylor series to such regions and include negative powers of $(z - \alpha)$.

#### 4.1 Definition of Laurent Series

A **Laurent series** centered at $\alpha$ is


$$
f(z) = \sum_{n=-\infty}^\infty c_n (z - \alpha)^n,
$$


where the series splits into two parts:

- The **principal part**: terms with negative powers,
- The **regular part**: terms with non-negative powers.

#### 4.2 Annulus and Convergence

An **annulus** is defined as


$$
A(r, R, \alpha) = \{ z : r < |z - \alpha| < R \},
$$


where $0 \leq r < R \leq \infty$.

The Laurent series converges uniformly on any closed sub-annulus inside $A(r, R, \alpha)$.

#### 4.3 Laurent's Theorem

If $f$ is analytic in an annulus $A(r, R, \alpha)$, then $f$ can be represented by a Laurent series converging to $f$ in that annulus. The coefficients $c_n$ are given by contour integrals:


$$
c_n = \frac{1}{2\pi i} \int_{C_\rho(\alpha)} \frac{f(z)}{(z - \alpha)^{n+1}} \, dz,
$$


where $C_\rho(\alpha)$ is a circle inside the annulus.

#### 4.4 Properties of Laurent Series

- The Laurent series representation is unique.
- Derivatives of $f$ can be obtained by term-wise differentiation of the Laurent series.
- Laurent series are essential for studying singularities and residues.

#### Examples

- Find Laurent series for functions like $f(z) = 2 + z - z^2$ in different regions.
- Find Laurent series for $f(z) = \frac{\cos z - 1}{z^4}$.
- Find Laurent series for $e^{-z^2}$ centered at 0.


### Summary and Key Takeaways

- **Analytic functions** have antiderivatives and their integrals depend only on endpoints in simply connected domains.
- **Cauchy's Integral Formula** allows evaluation of function values and derivatives via contour integrals.
- **Taylor series** represent analytic functions inside disks, converging uniformly within the radius of convergence.
- **Laurent series** generalize Taylor series to annulus regions, including negative powers, crucial for handling singularities.
- Understanding **pointwise vs uniform convergence** is important for handling limits and integrals of sequences of functions.
- Power series operations (addition, multiplication) follow algebraic rules within convergence domains.
- These concepts are foundational for complex analysis and have applications in physics, engineering, and applied mathematics.