## 10. Complex Integration

## Key Points

#### 1. 🧮 Complex Integral Definition  
- If $f(t) = u(t) + i v(t)$ with $u, v$ continuous on $[a,b]$, then  

$$
  \int_a^b f(t) dt = \int_a^b u(t) dt + i \int_a^b v(t) dt
$$

- Complex integrals inherit linearity and additivity properties from real integrals.

#### 2. 📐 Contours and Contour Integrals  
- A **contour** is a finite chain of smooth curves joined end-to-end in the complex plane.  
- The contour integral of $f(z)$ over contour $C$ is defined as the limit of Riemann sums:  

$$
  \int_C f(z) dz = \lim_{n \to \infty} \sum_{k=1}^n f(c_k) \Delta z_k
$$

- If $z(t)$ parametrizes $C$ for $t \in [a,b]$, then:  

$$
  \int_C f(z) dz = \int_a^b f(z(t)) z'(t) dt
$$


#### 3. 📏 Integral Inequalities  
- **Integral Triangle Inequality:**  

$$
  \left| \int_a^b f(t) dt \right| \leq \int_a^b |f(t)| dt
$$

- **ML Inequality:** If $|f(z)| \leq M$ on contour $C$ of length $L$, then:  

$$
  \left| \int_C f(z) dz \right| \leq M L
$$


#### 4. 🔄 Cauchy-Goursat Theorem  
- If $f$ is analytic in a simply connected domain $D$, then for any simple closed contour $C \subset D$:  

$$
  \int_C f(z) dz = 0
$$

- This implies contour integrals of analytic functions depend only on endpoints, not the path.

#### 5. 🔄 Deformation of Contour Lemma  
- If $C_1$ lies inside $C_2$, both simple closed contours, and $f$ is analytic in the region between them, then:  

$$
  \int_{C_1} f(z) dz = \int_{C_2} f(z) dz
$$


#### 6. 🧩 Extended Cauchy-Goursat Theorem  
- For a domain with multiple holes bounded by contours $C, C_1, C_2, ..., C_n$, with $f$ analytic in the region between:  

$$
  \int_C f(z) dz = \int_{C_1} f(z) dz + \int_{C_2} f(z) dz + \cdots + \int_{C_n} f(z) dz
$$


#### 7. ⚠️ Path Dependence and Singularities  
- For functions analytic everywhere on and inside contours, integrals are path-independent.  
- For functions with singularities (e.g., $f(z) = \frac{1}{z}$), integrals depend on the path taken around singularities.

#### 8. 🔢 Integral Values for Specific Contours  
- If $C$ is a simple closed contour positively oriented enclosing $z_0$, then:  

$$
  \int_C \frac{1}{z - z_0} dz = 2 \pi i
$$

- For integer $n \neq 1$:  

$$
  \int_C (z - z_0)^n dz = 0
$$



<br>

## Study Notes

### Complex Integration Study Notes


### 1. 🧮 Introduction to Complex Integrals

When we extend the idea of integration from real-valued functions to complex-valued functions, we enter the realm of **complex integration**. Here, the function we integrate, $f(t)$, takes complex values and is defined over a real interval $[a, b]$. 

#### What is a Complex Integral?

Suppose $f(t) = u(t) + i v(t)$, where $u(t)$ and $v(t)$ are real-valued functions of a real variable $t$, and $i = \sqrt{-1}$. If both $u(t)$ and $v(t)$ are continuous on $[a, b]$, then they are integrable in the usual real sense. This allows us to define the integral of $f(t)$ over $[a, b]$ as:


$$
\int_a^b f(t) \, dt = \int_a^b u(t) \, dt + i \int_a^b v(t) \, dt
$$


This means the integral of a complex function is just the integral of its real part plus $i$ times the integral of its imaginary part.

#### Key Properties of Complex Integrals

If $f(t) = u(t) + i v(t)$ and $g(t) = p(t) + i q(t)$ are continuous on $[a, b]$, then:

- **Linearity:** The integral of a sum is the sum of the integrals.
- **Scalar multiplication:** Multiplying a function by a complex constant scales the integral accordingly.
- **Additivity over intervals:** Integrals over adjacent intervals add up.

These properties mirror those of real integrals and are fundamental for working with complex integrals.


### 2. 📐 Contours and Contour Integrals

#### What is a Contour?

In complex integration, instead of integrating over a real interval, we often integrate over a path or curve in the complex plane. Such a path, made by joining a finite number of smooth curves end-to-end, is called a **contour**.

For example, a polygonal path connecting points $A$ to $B$ in the complex plane is a contour.

#### Parametrization of a Contour

To integrate over a contour $C$, we describe it using a parameter $t$ that runs from $a$ to $b$. The contour is represented as a function $z(t) = x(t) + i y(t)$, where $x(t)$ and $y(t)$ are real-valued functions describing the coordinates of points on the contour.

#### Defining the Contour Integral

Given a complex-valued function $f(z)$ and a contour $C$ parametrized by $z(t)$, the contour integral is defined as:


$$
\int_C f(z) \, dz := \lim_{n \to \infty} \sum_{k=1}^n f(c_k) \Delta z_k
$$


where:

- $\{z_0, z_1, ..., z_n\}$ is a partition of the contour $C$ from $z_0 = A$ to $z_n = B$,
- $\Delta z_k = z_k - z_{k-1}$,
- $c_k$ is some point on the segment between $z_{k-1}$ and $z_k$,
- The limit is taken as the partition gets finer.

This is the complex analogue of the Riemann integral, but now the increments $\Delta z_k$ are complex numbers representing small steps along the contour.

#### Evaluating Contour Integrals via Parametrization

If $z(t)$ parametrizes $C$ for $t \in [a, b]$, then:


$$
\int_C f(z) \, dz = \int_a^b f(z(t)) z'(t) \, dt
$$


This formula allows us to convert a contour integral into a standard integral over a real interval, which is often easier to evaluate.


### 3. 📏 Important Inequalities in Complex Integration

#### Integral Triangle Inequality

For a continuous complex function $f(t) = u(t) + i v(t)$, the absolute value of the integral satisfies:


$$
\left| \int_a^b f(t) \, dt \right| \leq \int_a^b |f(t)| \, dt
$$


This inequality is intuitive: the magnitude of the integral cannot exceed the integral of the magnitudes.

#### ML Inequality (Estimation Lemma)

If $f(z)$ is continuous on a contour $C$ of length $L$, and $|f(z)| \leq M$ for all $z$ on $C$, then:


$$
\left| \int_C f(z) \, dz \right| \leq M L
$$


This is a very useful tool for estimating the size of contour integrals without computing them exactly. It tells us that the integral's magnitude is bounded by the product of the maximum value of the function on the contour and the length of the contour.


### 4. 🔄 Cauchy-Goursat Theorem and Its Consequences

#### What is the Cauchy-Goursat Theorem?

This theorem is a cornerstone of complex analysis. It states:

> If $f$ is analytic (complex differentiable) in a simply connected domain $D$, and $C$ is any simple closed contour lying entirely in $D$, then:


$$
\int_C f(z) \, dz = 0
$$


This means that the integral of an analytic function around any closed loop in a simply connected domain is zero.

#### Why is this important?

- It implies that contour integrals of analytic functions depend only on the endpoints of the path, not on the path itself.
- It leads to powerful results like the existence of antiderivatives and integral formulas for analytic functions.

#### Deformation of Contour Lemma

If $C_1$ and $C_2$ are two simple closed contours with $C_1$ inside $C_2$, and $f$ is analytic in the region between them, then:


$$
\int_{C_1} f(z) \, dz = \int_{C_2} f(z) \, dz
$$


This means you can continuously deform one contour into another without changing the value of the integral, as long as you don't cross any singularities.


### 5. 🔄 Extended Cauchy-Goursat Theorem

This theorem generalizes the Cauchy-Goursat theorem to domains with holes (multiply connected domains).

Suppose you have a big contour $C$ and smaller contours $C_1, C_2, ..., C_n$ inside it, each enclosing a "hole" in the domain. If $f$ is analytic everywhere in the region between $C$ and the smaller contours, then:


$$
\int_C f(z) \, dz = \int_{C_1} f(z) \, dz + \int_{C_2} f(z) \, dz + \cdots + \int_{C_n} f(z) \, dz
$$


This allows us to analyze integrals in complex domains with multiple boundaries.


### 6. 🔍 Examples and Applications

#### Example 1: Integrating a Polynomial

Show that:


$$
\int (t - i)^3 \, dt = \text{(some explicit expression)}
$$


Since $(t - i)^3$ is a polynomial in $t$, integration is straightforward by expanding and integrating term-by-term.

#### Example 2: Integrating an Exponential Function

Evaluate:


$$
\int e^{t + i t} \, dt
$$


Rewrite the exponent as $t(1 + i)$, then integrate using the standard exponential integral formula.

#### Example 3: Parametrizing a Polygonal Path

Given points $-1 + i$ to $3 - i$, find a parametrization of the polygonal path $C$. This involves expressing the path as a piecewise linear function $z(t)$ over intervals.

#### Example 4: Contour Integral of $e^z$

- Approximate the integral using Riemann sums.
- Evaluate exactly using parametrization.

#### Example 5: Integral over a Semi-Circle

Evaluate:


$$
\int_C \frac{1}{z} \, dz
$$


where $C$ is the upper semi-circle of radius 1 centered at $x=2$, oriented counter-clockwise.

#### Example 6: Comparing Integrals over Different Paths

Show that:


$$
\int_{C_1} z \, dz = \int_{C_2} z \, dz
$$


where $C_1$ is a line segment and $C_2$ is a parabola joining the same points. This illustrates path independence for analytic functions.

#### Example 7: Different Values for Different Paths

Show that:


$$
\int_{C_1} \frac{1}{z} \, dz = \pi i, \quad \text{but} \quad \int_{C_2} \frac{1}{z} \, dz = -4i
$$


where $C_1$ and $C_2$ are different paths between the same points. This shows that the function $1/z$ is not analytic everywhere (has a singularity at 0), so integrals depend on the path.


### 7. 🧩 Summary and Key Takeaways

- **Complex integrals** extend real integrals to complex-valued functions and paths in the complex plane.
- **Contours** are piecewise smooth paths over which complex integrals are defined.
- The **contour integral** can be computed by parametrizing the contour and integrating over a real interval.
- The **Integral Triangle Inequality** and **ML Inequality** provide useful bounds for integrals.
- The **Cauchy-Goursat theorem** is fundamental: integrals of analytic functions over closed contours in simply connected domains are zero.
- The **Deformation of Contour lemma** allows contour deformation without changing integral values, provided no singularities are crossed.
- The **Extended Cauchy-Goursat theorem** handles domains with holes, relating integrals over outer and inner contours.
- Examples illustrate how to compute integrals, understand path dependence, and apply these theorems.


This detailed understanding of complex integration is essential for interviews and further study in complex analysis, as it forms the basis for many advanced topics like residue theory, conformal mappings, and analytic continuation.