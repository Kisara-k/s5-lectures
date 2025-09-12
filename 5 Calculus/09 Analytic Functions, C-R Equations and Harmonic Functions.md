## 9. Analytic Functions, C-R Equations and Harmonic Functions

## Key Points

#### 1. 🧮 Analytic Functions  
- A function $f(z)$ is **analytic** at a point if it has a complex derivative in some neighborhood around that point.  
- An **entire function** is analytic at every finite point in the complex plane.  
- Polynomials are entire functions because their derivatives exist everywhere.  
- A **singular point** is where $f$ fails to be analytic but is analytic arbitrarily close to it.  
- **Isolated singularity:** $f$ is analytic in a punctured neighborhood around the point but not at the point itself.  
- The sum, product, and quotient (denominator non-zero) of analytic functions are analytic.  
- The composition of analytic functions is analytic.  
- If $f'(z) = 0$ everywhere in a domain, then $f$ is constant in that domain.  


#### 2. 📐 Cauchy-Riemann Equations and Harmonic Functions  
- For $f(z) = u(x,y) + iv(x,y)$ to be analytic, $u$ and $v$ must satisfy the **Cauchy-Riemann equations**:  

$$
  u_x = v_y, \quad u_y = -v_x
$$
  
- A real-valued function $H(x,y)$ is **harmonic** if it satisfies Laplace’s equation:  

$$
  H_{xx} + H_{yy} = 0
$$
  
- If $f = u + iv$ is analytic, then both $u$ and $v$ are harmonic functions.  
- $v$ is a **harmonic conjugate** of $u$ if $f = u + iv$ is analytic.  


#### 3. 🔢 Exponential and Logarithm Functions  
- The exponential function $e^z$ is entire and defined by the power series:  

$$
  e^z = \sum_{n=0}^\infty \frac{z^n}{n!}
$$
  
- Euler’s formula:  

$$
  e^{i\theta} = \cos \theta + i \sin \theta
$$
  
- $e^z$ is periodic in the imaginary direction:  

$$
  e^{z + 2n\pi i} = e^z, \quad n \in \mathbb{Z}
$$
  
- The complex logarithm is the inverse of $e^z$ and multi-valued:  

$$
  \log z = \ln |z| + i(\text{Arg}(z) + 2n\pi), \quad n \in \mathbb{Z}
$$
  
- The **principal value** of the logarithm restricts the argument to $-\pi < \text{Arg}(z) \leq \pi$:  

$$
  \text{Log}(z) = \ln |z| + i \text{Arg}(z)
$$
  
- Properties of logarithm:  

$$
  \log(z_1 z_2) = \log z_1 + \log z_2, \quad \log\left(\frac{z_1}{z_2}\right) = \log z_1 - \log z_2
$$
  
- Complex powers defined by:  

$$
  z^c = e^{c \log z}
$$
  
  are multi-valued unless principal branches are chosen.  


#### 4. 🔄 Complex Trigonometric and Hyperbolic Functions  
- Complex sine and cosine are defined by power series:  

$$
  \sin z = \sum_{n=0}^\infty (-1)^n \frac{z^{2n+1}}{(2n+1)!}, \quad \cos z = \sum_{n=0}^\infty (-1)^n \frac{z^{2n}}{(2n)!}
$$
  
- Euler’s formula relates them:  

$$
  e^{iz} = \cos z + i \sin z
$$
  
- Expressions for complex sine and cosine in terms of real and imaginary parts:  

$$
  \sin z = \sin x \cosh y + i \cos x \sinh y
$$
  

$$
  \cos z = \cos x \cosh y - i \sin x \sinh y
$$
  
- Hyperbolic sine and cosine defined by:  

$$
  \sinh z = \frac{e^z - e^{-z}}{2}, \quad \cosh z = \frac{e^z + e^{-z}}{2}
$$
  


#### 5. 🔄 Inverse Trigonometric and Hyperbolic Functions  
- Because trigonometric and hyperbolic functions are periodic and many-to-one, their inverses are **multi-valued**.  
- Inverse functions are expressed using logarithms of complex variables.  
- Derivatives of inverse trigonometric and hyperbolic functions can be found using implicit differentiation and standard formulas.



<br>

## Study Notes

### 1. 🧮 Analytic Functions: What They Are and Why They Matter

Analytic functions are central to complex analysis. Intuitively, a function $f(z)$ of a complex variable $z$ is **analytic** at a point if it behaves nicely enough there to have a complex derivative — not just at that point, but in some neighborhood around it. This means the function is smooth and differentiable in a complex sense, which is a stronger condition than differentiability in real variables.

#### What Does Analytic Mean?

- A function $f(z)$ is **analytic at a point $z_0$** if it has a complex derivative at every point in some open neighborhood around $z_0$.
- If a function is analytic at **every finite point** in the complex plane, it is called an **entire function**.

#### Examples to Understand

- $f(z) = \frac{1}{z}$ is analytic everywhere except at $z=0$ because it has a derivative at every other point.
- $f(z) = |z|^2$ is **not analytic anywhere except possibly at $z=0$**, but even there, it fails to be analytic in any neighborhood. This is because the complex derivative does not exist in the complex sense (it depends on direction).

#### Entire Functions

- Polynomials are entire functions because their derivatives exist everywhere in the complex plane.
- The exponential function $e^z$, sine, cosine, and many other standard functions are also entire.

#### Singular Points and Singularities

A **singular point** or **singularity** is a point where a function fails to be analytic but is analytic arbitrarily close to it.

- **Isolated singularity:** There exists a small radius $\delta$ such that the function is analytic everywhere in the punctured disk $0 < |z - a| < \delta$, but not at $z = a$ itself.
- **Non-isolated singularity:** Singular points that cluster or form a continuum, such as branch cuts.

**Branch cuts** are lines or curves in the complex plane where a function is discontinuous or multi-valued, like the argument function $\arg(z)$, logarithm $\log(z)$, or square root $\sqrt{z}$, often taken along the negative real axis.

#### Important Properties of Analytic Functions

- The sum, product, and quotient (where denominator is non-zero) of analytic functions are analytic.
- The composition of analytic functions is analytic.
- If the derivative of an analytic function is zero everywhere in a domain, the function must be constant there.


### 2. 📐 Cauchy-Riemann (C-R) Equations and Harmonic Functions

#### What Are Cauchy-Riemann Equations?

For a complex function $f(z) = u(x,y) + i v(x,y)$, where $u$ and $v$ are real-valued functions of two real variables $x$ and $y$, the function $f$ is analytic if and only if $u$ and $v$ satisfy the **Cauchy-Riemann equations**:


$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}
$$


These equations ensure the complex differentiability of $f$.

#### Harmonic Functions

A **harmonic function** is a twice continuously differentiable real-valued function $H(x,y)$ that satisfies **Laplace’s equation**:


$$
H_{xx} + H_{yy} = 0
$$


where $H_{xx}$ and $H_{yy}$ are the second partial derivatives with respect to $x$ and $y$.

#### Connection Between Analytic and Harmonic Functions

- If $f(z) = u + iv$ is analytic in a domain, then both $u$ and $v$ are harmonic functions in that domain.
- The function $v$ is called a **harmonic conjugate** of $u$ if $f = u + iv$ is analytic.

#### Examples

- $u = x^2 - y^2$ and $v = 2xy$ are harmonic conjugates because they satisfy the C-R equations and Laplace’s equation.
- $u = x^2 - y^2$ and $v = x^2 + y^2$ are both harmonic but **not** harmonic conjugates because they do not satisfy the C-R equations.


### 3. 🔢 Elementary Functions in Complex Analysis

#### The Exponential Function $e^z$

Defined by the power series:


$$
e^z = \sum_{n=0}^\infty \frac{z^n}{n!}
$$


- $e^z$ is an **entire function** (analytic everywhere).
- Euler’s formula connects exponential and trigonometric functions:


$$
e^{i\theta} = \cos \theta + i \sin \theta
$$


- The exponential function is periodic in the imaginary direction:


$$
e^{z + 2n\pi i} = e^z, \quad n \in \mathbb{Z}
$$


This periodicity means $e^z$ is **many-to-one**, so its inverse, the logarithm, is multi-valued.

#### The Logarithm Function $\log z$

- Defined as the inverse of the exponential function for $z \neq 0$.
- Expressed as:


$$
\log z = \ln |z| + i \arg(z)
$$


- Because $\arg(z)$ is multi-valued (differing by multiples of $2\pi$), the logarithm is multi-valued:


$$
\log z = \ln |z| + i(\text{Arg}(z) + 2n\pi), \quad n \in \mathbb{Z}
$$


- The **principal value** of the logarithm, denoted $\text{Log}(z)$, restricts the argument to $-\pi < \text{Arg}(z) \leq \pi$:


$$
\text{Log}(z) = \ln |z| + i \text{Arg}(z)
$$


#### Properties of $\log z$ and $\text{Log}(z)$

- $e^{\text{Log}(z)} = z$ for all $z \neq 0$.
- $\text{Log}(x) = \ln x$ for positive real $x$.
- Logarithm satisfies:


$$
\log(z_1 z_2) = \log z_1 + \log z_2, \quad \log\left(\frac{z_1}{z_2}\right) = \log z_1 - \log z_2
$$


#### Complex Powers

For $z \neq 0$ and complex $c$, define:


$$
z^c = e^{c \log z}
$$


Because $\log z$ is multi-valued, $z^c$ is also multi-valued unless we restrict to principal values.


### 4. 🔄 Trigonometric and Hyperbolic Functions of Complex Variables

#### Complex Sine and Cosine

Using power series expansions extended to complex arguments:


$$
\sin z = \sum_{n=0}^\infty (-1)^n \frac{z^{2n+1}}{(2n+1)!}, \quad \cos z = \sum_{n=0}^\infty (-1)^n \frac{z^{2n}}{(2n)!}
$$


From Euler’s formula:


$$
e^{iz} = \cos z + i \sin z
$$


We can express sine and cosine in terms of real and imaginary parts:


$$
\sin z = \sin x \cosh y + i \cos x \sinh y
$$


$$
\cos z = \cos x \cosh y - i \sin x \sinh y
$$


where $z = x + iy$.

#### Hyperbolic Sine and Cosine

Defined by:


$$
\sinh z = \frac{e^z - e^{-z}}{2}, \quad \cosh z = \frac{e^z + e^{-z}}{2}
$$


These functions share many properties with their real counterparts but are defined for complex arguments.


### 5. 🔄 Inverse Trigonometric and Hyperbolic Functions

#### Multi-Valued Nature

Because trigonometric and hyperbolic functions are periodic and many-to-one, their inverses are multi-valued.

#### Inverse Trigonometric Functions

- Defined via logarithmic expressions involving complex variables.
- Their derivatives can be found using implicit differentiation and chain rule.

#### Inverse Hyperbolic Functions

- Similarly defined using logarithms.
- Derivatives are also expressible in closed form.


### Summary for Interview Preparation

- **Analytic functions** are complex differentiable in neighborhoods, with entire functions analytic everywhere.
- **Singularities** are points where analyticity fails; isolated singularities are surrounded by analytic points.
- **Cauchy-Riemann equations** characterize analyticity via partial derivatives of real and imaginary parts.
- **Harmonic functions** satisfy Laplace’s equation; real and imaginary parts of analytic functions are harmonic.
- **Exponential and logarithm functions** in complex analysis are multi-valued due to periodicity in the imaginary direction.
- **Complex trigonometric and hyperbolic functions** extend real functions with complex arguments, maintaining many familiar identities.
- **Inverse functions** of these are multi-valued and involve branch cuts and principal values.