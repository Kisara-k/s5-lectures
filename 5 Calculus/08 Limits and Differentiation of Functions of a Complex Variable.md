## 8. Limits and Differentiation of Functions of a Complex Variable

## Key Points

#### 1. 🧮 Functions of a Complex Variable  
- A function $f$ defined on a set $S \subseteq \mathbb{C}$ assigns each $z \in S$ a complex number $\omega = f(z)$.  
- $f(z)$ can be expressed as $u(x,y) + i v(x,y)$, where $u, v$ are real-valued functions of real variables $x, y$.  
- Using polar coordinates, $f(z) = u(r, \theta) + i v(r, \theta)$ where $z = r e^{i \theta}$.  
- A function $f$ is also called a **mapping** or **transformation** from the $z$-plane to the $\omega$-plane.  
- Common geometric transformations:  
  - Translation: $\omega = z + c$ shifts points.  
  - Rotation: $\omega = i z$ rotates points by 90° counterclockwise.  
  - Reflection: $\omega = \bar{z}$ reflects points about the real axis.


#### 2. 🔍 Limits of Complex Functions  
- The limit $\lim_{z \to z_0} f(z) = \omega_0$ means for every $\epsilon > 0$, there exists $\delta > 0$ such that $0 < |z - z_0| < \delta \implies |f(z) - \omega_0| < \epsilon$.  
- Limits in complex functions must be independent of the path of approach.  
- If $f(z) = u(x,y) + i v(x,y)$, then $\lim_{z \to z_0} f(z) = \omega_0 = u_0 + i v_0$ if and only if $\lim_{(x,y) \to (x_0,y_0)} u = u_0$ and $\lim_{(x,y) \to (x_0,y_0)} v = v_0$.  
- Limits, if finite, are unique.  
- Composition of limits: If $\lim_{z \to z_0} f(z) = \omega_0$ and $\lim_{\omega \to \omega_0} g(\omega) = L$, then $\lim_{z \to z_0} g(f(z)) = L$.


#### 3. 🔗 Continuity of Complex Functions  
- $f$ is continuous at $z_0$ if:  
  1. $\lim_{z \to z_0} f(z)$ exists,  
  2. $f(z_0)$ is defined,  
  3. $\lim_{z \to z_0} f(z) = f(z_0)$.  
- The composition of continuous functions is continuous.  
- If $f$ is continuous and non-zero at $z_0$, then $f(z) \neq 0$ in some neighborhood of $z_0$.  
- If $f$ is continuous on a compact region $R$, then $|f(z)|$ is bounded on $R$ and attains its maximum at some point in $R$.


#### 4. ✍️ Differentiation of Complex Functions  
- The derivative of $f$ at $z_0$ is:  

$$
  f'(z_0) = \lim_{z \to z_0} \frac{f(z) - f(z_0)}{z - z_0}
$$
  
  if this limit exists.  
- If $f$ is differentiable at $z_0$, then $f$ is continuous at $z_0$.  
- Differentiation rules hold:  

$$
  \frac{d}{dz} z^n = n z^{n-1} \quad \text{for positive integers } n.
$$
  
- A function is **analytic** at $z_0$ if it is differentiable at every point in some neighborhood of $z_0$.  
- If $f$ is analytic on an open set $G$, then $f'$ is continuous on $G$.


#### 5. 📐 Cauchy-Riemann Equations  
- If $f(z) = u(x,y) + i v(x,y)$ is differentiable at $z_0 = x_0 + i y_0$, then the partial derivatives $u_x, u_y, v_x, v_y$ exist at $(x_0, y_0)$ and satisfy:  

$$
  u_x = v_y, \quad u_y = -v_x
$$
  
- The derivative at $z_0$ can be written as:  

$$
  f'(z_0) = u_x(x_0, y_0) + i v_x(x_0, y_0)
$$
  
- **Sufficient condition:** If $u$ and $v$ have continuous first-order partial derivatives in a neighborhood of $z_0$ and satisfy the Cauchy-Riemann equations there, then $f$ is differentiable at $z_0$.  
- $f$ is analytic on an open set $G$ if and only if $u$ and $v$ satisfy the Cauchy-Riemann equations on $G$ and have continuous partial derivatives.  
- In polar coordinates, the Cauchy-Riemann equations become:  

$$
  r u_r = v_\theta, \quad u_\theta = -r v_r
$$
  
- The derivative in polar form is:  

$$
  f'(z_0) = e^{-i \theta} (u_r + i v_r)
$$



<br>

## Study Notes

### 1. 🧮 Functions of a Complex Variable: Understanding the Basics

When we talk about functions of a complex variable, we are extending the idea of functions from real numbers to complex numbers. A **complex number** is of the form $z = x + iy$, where $x$ and $y$ are real numbers, and $i$ is the imaginary unit with $i^2 = -1$.

#### What is a function of a complex variable?

A function $f$ defined on a set $S$ of complex numbers assigns to each complex number $z \in S$ another complex number $\omega$. We write this as:


$$
\omega = f(z)
$$


Here, $S$ is called the **domain** of the function $f$, and $\omega$ is the **value** of the function at $z$.

#### Expressing complex functions in terms of real variables

Since $z = x + iy$ and $\omega = u + iv$, where $u$ and $v$ are real numbers, the function $f$ can be seen as a pair of real-valued functions:


$$
f(z) = u(x, y) + i v(x, y)
$$


This means the function $f$ depends on two real variables $x$ and $y$, and outputs two real values $u$ and $v$.

#### Using polar coordinates

Instead of Cartesian coordinates $(x, y)$, we can use polar coordinates $(r, \theta)$, where:


$$
z = r e^{i\theta}
$$


In this form, the function can be written as:


$$
f(z) = u(r, \theta) + i v(r, \theta)
$$


This is useful for understanding geometric transformations like rotations and scaling.

#### Examples to illustrate

- **Example 1:** $f(z) = z^3 + z + 1$ can be expanded and expressed in terms of $x$ and $y$.
- **Example 2:** Given $f(z) = x^2 - y^2 - 2y + i(2x - 2xy)$, rewrite $f(z)$ in terms of $z$ using the identities $x = \frac{z + \bar{z}}{2}$ and $y = \frac{z - \bar{z}}{2i}$.
- **Example 3:** Express $f(z) = z + \frac{1}{z}$ (for $z \neq 0$) in polar form $u(r, \theta) + i v(r, \theta)$.

#### Mapping and transformations

A function $f$ can also be viewed as a **mapping** or **transformation** from the complex plane $z$ to the complex plane $\omega$. The image of a point $z$ is $\omega = f(z)$, and the set of all images of points in a subset $T \subseteq S$ is called the **image** of $T$.

- **Translation:** $\omega = z + 1$ shifts every point one unit to the right.
- **Rotation:** $\omega = i z = r e^{i(\theta + \pi/2)}$ rotates every point by 90° counterclockwise.
- **Reflection:** $\omega = \bar{z} = x - iy$ reflects points about the real axis.


### 2. 🔍 Limits of Complex Functions: Approaching Values

Limits in complex analysis extend the idea of limits from real functions to complex functions. The concept is crucial for defining continuity and differentiability.

#### Limit of a real-valued function of two variables

For a function $f(x, y)$ of two real variables, the limit as $(x, y) \to (x_0, y_0)$ is $L$ if for every small positive number $\epsilon$, there exists a $\delta$ such that whenever the distance between $(x, y)$ and $(x_0, y_0)$ is less than $\delta$, the value $f(x, y)$ is within $\epsilon$ of $L$.

#### Limit of a complex-valued function of a complex variable

For a function $f$ defined near $z_0$ (except possibly at $z_0$ itself), the limit of $f(z)$ as $z \to z_0$ is $\omega_0$ if for every $\epsilon > 0$, there exists $\delta > 0$ such that:


$$
0 < |z - z_0| < \delta \implies |f(z) - \omega_0| < \epsilon
$$


This means $f(z)$ can be made arbitrarily close to $\omega_0$ by choosing $z$ sufficiently close to $z_0$, but not equal to $z_0$.

#### Important examples

- **Example 4:** For $f(z) = \frac{i z}{2}$ in the open disk $|z| < 1$, the limit as $z \to 1$ is $\frac{i}{2}$.
- **Example 5:** For $f(z) = \frac{z}{\bar{z}}$, the limit as $z \to 0$ does **not** exist because the value depends on the direction from which $z$ approaches 0.

#### Key theorems about limits

- **Uniqueness:** If a finite limit exists at a point, it is unique.
- **Limit laws:** Limits behave well under addition, multiplication, and division (provided denominators are non-zero).
- **Composition:** If $\lim_{z \to z_0} f(z) = \omega_0$ and $\lim_{\omega \to \omega_0} g(\omega) = L$, then $\lim_{z \to z_0} g(f(z)) = L$.

#### Limits in terms of real and imaginary parts

If $f(z) = u(x, y) + i v(x, y)$, then:


$$
\lim_{z \to z_0} f(z) = \omega_0 = u_0 + i v_0
$$


if and only if


$$
\lim_{(x,y) \to (x_0,y_0)} u(x,y) = u_0 \quad \text{and} \quad \lim_{(x,y) \to (x_0,y_0)} v(x,y) = v_0
$$



### 3. 🔗 Continuity of Complex Functions: Smooth Behavior

Continuity in complex functions is similar to real functions but involves complex limits.

#### Definition of continuity at a point

A function $f$ is **continuous** at $z_0$ if:

1. The limit $\lim_{z \to z_0} f(z)$ exists.
2. The function value $f(z_0)$ is defined.
3. The limit equals the function value: $\lim_{z \to z_0} f(z) = f(z_0)$.

#### Important properties

- The composition of continuous functions is continuous.
- If $f$ is continuous and non-zero at $z_0$, then $f(z) \neq 0$ in some neighborhood around $z_0$.
- If $f$ is continuous on a **compact** region (closed and bounded), then $|f(z)|$ is bounded by some real number $M$, and this bound is attained at some point in the region.


### 4. ✍️ Differentiation of Complex Functions: The Complex Derivative

Differentiation in complex analysis is more restrictive and powerful than in real analysis.

#### Definition of the complex derivative

The derivative of $f$ at $z_0$ is defined as:


$$
f'(z_0) = \lim_{z \to z_0} \frac{f(z) - f(z_0)}{z - z_0}
$$


if this limit exists. The function $f$ is said to be **differentiable** at $z_0$ if $f'(z_0)$ exists.

#### Examples

- For $f(z) = z^2$, the derivative at any point $z$ is $f'(z) = 2z$.
- For $f(z) = \bar{z}$, the derivative does **not** exist anywhere.
- For the real-valued function $f(z) = |z|^2 = x^2 + y^2$, the derivative does not exist as a complex derivative.

#### Important theorems

- If $f$ is differentiable at $z_0$, then $f$ is continuous at $z_0$.
- Differentiation rules for sums, products, and powers hold similarly to real functions. For example:


$$
\frac{d}{dz} z^n = n z^{n-1}
$$


for positive integers $n$.

#### Analytic functions

A function $f$ is **analytic** at $z_0$ if it is differentiable at every point in some neighborhood around $z_0$. If $f$ is analytic on an open set $G$, then $f'$ is continuous on $G$, meaning $f$ is **continuously differentiable** there.


### 5. 📐 Cauchy-Riemann Equations: The Heart of Complex Differentiability

The Cauchy-Riemann equations provide necessary and sufficient conditions for a complex function to be differentiable (and hence analytic).

#### Statement of the Cauchy-Riemann equations

Suppose:


$$
f(z) = u(x, y) + i v(x, y)
$$


and $f'(z)$ exists at $z_0 = x_0 + i y_0$. Then the partial derivatives $u_x, u_y, v_x, v_y$ exist at $(x_0, y_0)$ and satisfy:


$$
u_x = v_y \quad \text{and} \quad u_y = -v_x
$$


Moreover, the derivative can be expressed as:


$$
f'(z_0) = u_x(x_0, y_0) + i v_x(x_0, y_0)
$$


#### Sufficient conditions for differentiability

If $u$ and $v$ have continuous first-order partial derivatives in a neighborhood of $z_0$ and satisfy the Cauchy-Riemann equations there, then $f$ is differentiable at $z_0$.

#### Corollary for analyticity

If $u$ and $v$ are defined on an open region $G$, have continuous partial derivatives, and satisfy the Cauchy-Riemann equations throughout $G$, then $f$ is analytic on $G$.

#### Polar form of Cauchy-Riemann equations

If $f(z) = u(r, \theta) + i v(r, \theta)$, then the Cauchy-Riemann equations become:


$$
r u_r = v_\theta, \quad u_\theta = -r v_r
$$


where subscripts denote partial derivatives. If these hold and the derivatives are continuous, then:


$$
f'(z_0) = e^{-i \theta} (u_r + i v_r)
$$



### Summary

- A **complex function** maps complex numbers to complex numbers and can be expressed in terms of real and imaginary parts.
- **Limits** in complex functions require the function values to approach a specific complex number as the input approaches a point from any direction.
- **Continuity** means the function value matches the limit at a point.
- The **complex derivative** is defined similarly to the real derivative but is more restrictive.
- The **Cauchy-Riemann equations** are the key conditions that characterize complex differentiability and analyticity.
- Functions satisfying these conditions are smooth and have many powerful properties in complex analysis.