## 13. Residue Theory (ctd.)

## Key Points

#### 1. 🧮 Residue Theory and Real Integrals  
- Residue theory can be used to evaluate real integrals by extending them into the complex plane and applying the residue theorem.  
- Real integrals that are difficult to solve by usual methods can be evaluated using residues of poles inside a chosen contour.

#### 2. 🎯 Trigonometric Integrals via Residues  
- Trigonometric integrals over $[0, 2\pi]$ can be transformed into contour integrals on the unit circle using $z = e^{i\theta}$.  
- Cosine terms can be expressed as $\cos \theta = \frac{z + z^{-1}}{2}$ to convert the integral into a rational function in $z$.  
- Residue theorem applied to this contour integral gives the value of the original trigonometric integral.

#### 3. ♾️ Improper Integrals of Rational Functions  
- Improper integral over $[0, \infty)$ is defined as $\lim_{R \to \infty} \int_0^R f(x) dx$, if the limit exists.  
- Improper integral over $(-\infty, \infty)$ is defined as $\lim_{R \to \infty} \int_{-R}^R f(x) dx$, if both limits exist.  
- The Cauchy Principal Value (P.V.) is defined as $\lim_{R \to \infty} \int_{-R}^R f(x) dx$ when the integral itself does not converge but the symmetric limit exists.

#### 4. 📐 Theorem 13.3.1: Rational Functions and Residues  
- For $f(z) = \frac{P(z)}{Q(z)}$ with polynomials $P, Q$ of degrees $m, n$ respectively, if $Q(x) \neq 0$ for all real $x$ and $n \geq m + 2$, then  

$$
\int_{-\infty}^\infty f(x) dx = 2\pi i \sum \text{Residues of } f \text{ at poles in the upper half-plane}
$$


#### 5. 🎵 Theorem 13.3.2: Convergence of Integrals with Cosine and Sine  
- If $P, Q$ are polynomials with degrees $m, n$ and $n \geq m + 1$, and $Q(x) \neq 0$ for all real $x$, then  

$$
\int_{-\infty}^\infty \frac{P(x)}{Q(x)} \cos x \, dx \quad \text{and} \quad \int_{-\infty}^\infty \frac{P(x)}{Q(x)} \sin x \, dx
$$
  
are convergent improper integrals.

#### 6. ⚡ Theorem 13.3.3: Integrals with Exponential Factors  
- For $P, Q$ polynomials with degrees $m, n$, $n \geq m + 1$, $Q(x) \neq 0$ for all real $x$, and $\alpha > 0$, define  

$$
f(z) = \frac{P(z)}{Q(z)} e^{i \alpha z}
$$
  
Then  

$$
\int_{-\infty}^\infty \frac{P(x)}{Q(x)} \cos(\alpha x) \, dx \quad \text{and} \quad \int_{-\infty}^\infty \frac{P(x)}{Q(x)} \sin(\alpha x) \, dx
$$
  
can be evaluated by summing residues of $f$ at poles in the upper half-plane.

#### 7. 🧩 Example Application  
- Poles of $f(z) = \frac{z e^{i z}}{z^2 + 1}$ are at $z = \pm i$.  
- Residue theorem applied to poles in the upper half-plane (here $z = i$) gives the value of integrals like  

$$
\int_{-\infty}^\infty \frac{x \sin x}{x^2 + 1} dx = \pi (\cos 1 + \sin 1)
$$



<br>

## Study Notes

### 1. 🧮 Introduction to Residue Theory and Real Integrals

Residue Theory is a powerful tool in complex analysis that allows us to evaluate complex integrals, especially contour integrals around singularities (poles) of complex functions. One of the most remarkable applications of residue theory is its ability to evaluate certain **real integrals** that are difficult or impossible to solve using standard calculus techniques.

Throughout the course, you have learned that integrals over curves in three-dimensional space or contours in the complex plane can often be transformed into integrals over real intervals by suitable parametrizations. Residue theory works in the reverse direction as well: it lets us evaluate real integrals by extending them into the complex plane and applying the residue theorem.

This approach is particularly useful for integrals involving rational functions, trigonometric functions, and improper integrals over infinite intervals.


### 2. 🎯 Evaluating Real Integrals Using Residues

The key idea is to consider a real integral as part of a complex contour integral. By choosing an appropriate contour in the complex plane that includes the real axis and closes in the upper or lower half-plane, we can apply the **Residue Theorem** to evaluate the integral.

- The **Residue Theorem** states that the integral of a function around a closed contour is $2\pi i$ times the sum of the residues of the function's singularities inside the contour.
- For real integrals, the contour is often chosen so that the integral over the curved part of the contour vanishes or is easy to evaluate.
- The residues at the poles inside the contour then give the value of the original real integral.

This method is especially effective for integrals involving rational functions and trigonometric functions multiplied by rational functions.


### 3. 🎲 Trigonometric Integrals and Residues

Trigonometric integrals often appear in the form:


$$
\int_0^{2\pi} \frac{1 + 3 \cos^2 \theta}{5 - 4 \cos \theta} \, d\theta
$$


These integrals can be tricky to evaluate directly. However, by using the substitution $z = e^{i\theta}$, which maps the interval $[0, 2\pi]$ on the real line to the unit circle in the complex plane, the integral can be transformed into a contour integral around the unit circle.

- The cosine terms can be expressed in terms of $z$ and $z^{-1}$ using Euler’s formula:
  

$$
  \cos \theta = \frac{z + z^{-1}}{2}
$$


- The integral then becomes a contour integral of a rational function in $z$.
- Applying the residue theorem to this contour integral allows us to find the value of the original trigonometric integral.

This technique is a standard approach to evaluating integrals involving trigonometric functions.


### 4. ♾️ Improper Integrals of Rational Functions

Improper integrals are integrals where the interval of integration is infinite or the integrand has singularities. Residue theory provides a method to evaluate improper integrals of rational functions, especially those defined on the entire real line.

#### Definition of Improper Integrals

- For a function $f$ continuous on $[0, \infty)$, the improper integral is defined as:


$$
  \int_0^\infty f(x) \, dx := \lim_{R \to \infty} \int_0^R f(x) \, dx
$$


- For functions defined on all real numbers $\mathbb{R}$, the integral over $(-\infty, \infty)$ is:


$$
  \int_{-\infty}^\infty f(x) \, dx := \lim_{R \to \infty} \int_{-R}^R f(x) \, dx
$$


- The **Cauchy Principal Value (P.V.)** is a special limit used when the integral does not converge in the usual sense but the symmetric limit exists:


$$
  \text{P.V.} \int_{-\infty}^\infty f(x) \, dx := \lim_{R \to \infty} \int_{-R}^R f(x) \, dx
$$


#### Example of Principal Value

Sometimes the integral $\int_{-\infty}^\infty f(x) \, dx$ does not exist because the limits diverge, but the principal value exists and can be computed using residues.


### 5. 📐 Theorems on Improper Integrals and Residues

#### Theorem 13.3.1: Rational Functions with Poles in the Upper Half-Plane

Let


$$
f(z) = \frac{P(z)}{Q(z)}
$$


where $P$ and $Q$ are polynomials of degrees $m$ and $n$ respectively, with $Q(x) \neq 0$ for all real $x$, and $n \geq m + 2$.

- This condition ensures the function $f$ decays sufficiently fast at infinity.
- The integral over the real line can be evaluated by summing the residues of $f$ at its poles $z_1, z_2, \ldots, z_k$ in the **upper half-plane**.
- The integral is given by:


$$
  \int_{-\infty}^\infty f(x) \, dx = 2\pi i \sum_{j=1}^k \text{Res}(f, z_j)
$$


This theorem is fundamental because it reduces the evaluation of an improper integral to finding residues at poles in the complex plane.


#### Theorem 13.3.2: Convergence of Integrals Involving Cosine and Sine

If $P$ and $Q$ are polynomials with degrees $m$ and $n$ respectively, and $n \geq m + 1$, and $Q(x) \neq 0$ for all real $x$, then the integrals


$$
\int_{-\infty}^\infty \frac{P(x)}{Q(x)} \cos x \, dx \quad \text{and} \quad \int_{-\infty}^\infty \frac{P(x)}{Q(x)} \sin x \, dx
$$


are convergent improper integrals.

This theorem guarantees that these integrals make sense and can be evaluated, often using residue theory.


#### Theorem 13.3.3: Integrals with Exponential Factors

Let $P$ and $Q$ be polynomials with degrees $m$ and $n$ respectively, $n \geq m + 1$, and $Q(x) \neq 0$ for all real $x$. For $\alpha > 0$, define


$$
f(z) = \frac{P(z)}{Q(z)} e^{i \alpha z}
$$


Then the integrals


$$
\int_{-\infty}^\infty \frac{P(x)}{Q(x)} \cos(\alpha x) \, dx \quad \text{and} \quad \int_{-\infty}^\infty \frac{P(x)}{Q(x)} \sin(\alpha x) \, dx
$$


can be evaluated by summing the residues of $f$ at its poles in the upper half-plane.

This theorem extends the previous results to integrals involving oscillatory exponential terms, which are common in physics and engineering.


### 6. 🧩 Examples and Applications

#### Example: Evaluating an Integral Involving $x \sin x$ and $\cos x$

Consider the integral


$$
\int_{-\infty}^\infty \frac{x \sin x}{x^2 + 1} \, dx
$$


Using residue theory and the theorems above, this integral can be evaluated by:

- Extending the integral to the complex plane.
- Identifying the poles of the function $f(z) = \frac{z e^{i z}}{z^2 + 1}$.
- Calculating the residues at the poles in the upper half-plane (which are at $z = i$ since $z^2 + 1 = 0$ implies $z = \pm i$).
- Applying the residue theorem to find the value of the integral.

The result involves terms like $\pi (\cos 1 + \sin 1)$, showing how residues simplify the evaluation of otherwise complicated integrals.


### Summary

Residue theory is a versatile and powerful method for evaluating complex integrals and, by extension, many real integrals that are difficult to solve by elementary methods. The key steps involve:

- Extending the real integral into the complex plane.
- Choosing an appropriate contour that includes the real axis.
- Identifying poles of the integrand inside the contour.
- Calculating residues at these poles.
- Applying the residue theorem to find the value of the integral.

The theorems presented provide conditions under which improper integrals of rational functions and integrals involving trigonometric or exponential functions converge and can be evaluated using residues.

Understanding these concepts and being able to apply them is essential for advanced calculus, complex analysis, and many applications in physics and engineering.