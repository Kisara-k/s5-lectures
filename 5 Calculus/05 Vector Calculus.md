## 5. Vector Calculus

## Key Points

#### 1. 📐 Vector Fields  
- A vector field in ℝ³ is a function $\mathbf{F}(x,y,z) = M \mathbf{i} + N \mathbf{j} + P \mathbf{k}$ assigning a vector to each point.  
- $M, N, P$ are the scalar components of the vector field.  
- A vector field is continuous if $M, N, P$ are continuous; differentiable if all partial derivatives of $M, N, P$ exist.  
- An inverse-square field has the form $\mathbf{F}(\mathbf{r}) = \frac{c \mathbf{r}}{|\mathbf{r}|^3}$.

#### 2. 🌟 Gradient and Conservative Fields  
- The gradient of a scalar function $\phi$ is $\nabla \phi = \frac{\partial \phi}{\partial x} \mathbf{i} + \frac{\partial \phi}{\partial y} \mathbf{j} + \frac{\partial \phi}{\partial z} \mathbf{k}$.  
- A vector field $\mathbf{F}$ is conservative if $\mathbf{F} = \nabla \phi$ for some scalar potential $\phi$.  
- Conservative fields have path-independent line integrals.

#### 3. 🔄 Divergence, Curl, and Laplacian  
- Divergence: $\text{div} \, \mathbf{F} = \frac{\partial f}{\partial x} + \frac{\partial g}{\partial y} + \frac{\partial h}{\partial z}$ for $\mathbf{F} = f \mathbf{i} + g \mathbf{j} + h \mathbf{k}$.  
- Curl: $\text{curl} \, \mathbf{F} = \nabla \times \mathbf{F} = \left( \frac{\partial h}{\partial y} - \frac{\partial g}{\partial z} \right) \mathbf{i} - \left( \frac{\partial h}{\partial x} - \frac{\partial f}{\partial z} \right) \mathbf{j} + \left( \frac{\partial g}{\partial x} - \frac{\partial f}{\partial y} \right) \mathbf{k}$.  
- Laplacian: $\nabla^2 \phi = \frac{\partial^2 \phi}{\partial x^2} + \frac{\partial^2 \phi}{\partial y^2} + \frac{\partial^2 \phi}{\partial z^2} = \text{div}(\nabla \phi)$.  
- Laplace’s equation: $\nabla^2 \phi = 0$.

#### 4. ➰ Line Integrals  
- Scalar line integral over curve $C$: $\int_C f \, ds = \int_a^b f(x(t), y(t), z(t)) \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2} dt$.  
- Vector line integral over curve $C$: $\int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t) dt$.  
- Line integrals of vector fields represent work done by force fields along a path.

#### 5. 🔄 Independence of Path and Conservative Fields  
- Work done by force field $\mathbf{F}$ along curve $C$: $W = \int_C \mathbf{F} \cdot d\mathbf{r}$.  
- Fundamental Theorem of Line Integrals: If $\mathbf{F} = \nabla \phi$, then $\int_C \mathbf{F} \cdot d\mathbf{r} = \phi(B) - \phi(A)$ for curve $C$ from $A$ to $B$.  
- A vector field is conservative if and only if the line integral around every closed curve in the region is zero.  
- In a connected, simply connected region, the following are equivalent:  
  a) $\mathbf{F}$ is conservative.  
  b) Line integral around every closed curve is zero.  
  c) Line integral between two points is path-independent.

#### 6. ✅ Conservative Field Test (2D)  
- For $\mathbf{F} = f(x,y) \mathbf{i} + g(x,y) \mathbf{j}$ with continuous first partial derivatives in a simply connected region, $\mathbf{F}$ is conservative if and only if:  

$$
\frac{\partial f}{\partial y} = \frac{\partial g}{\partial x}
$$



<br>

## Study Notes

### 1. 📐 Introduction to Vector Fields

Vector calculus begins with the concept of **vector fields**, which are fundamental in describing physical phenomena like fluid flow, electromagnetic fields, and forces.

A **vector field** in three-dimensional space (ℝ³) is a function that assigns a vector to every point in a region of space. Formally, if the domain is $D \subseteq \mathbb{R}^3$, a vector field $\mathbf{F}$ can be written as:


$$
\mathbf{F}(x, y, z) = M(x, y, z) \mathbf{i} + N(x, y, z) \mathbf{j} + P(x, y, z) \mathbf{k}
$$


Here, $M, N, P$ are scalar functions representing the components of the vector field along the $x, y, z$ directions respectively.

- If $M, N, P$ are continuous functions, then $\mathbf{F}$ is called a **continuous vector field**.
- If all partial derivatives of $M, N, P$ exist and are continuous, then $\mathbf{F}$ is a **differentiable vector field**.

#### Special Types of Vector Fields

- **Inverse-square field:** A vector field of the form


$$
\mathbf{F}(\mathbf{r}) = \frac{c \mathbf{r}}{|\mathbf{r}|^3}
$$


where $\mathbf{r}$ is the position vector and $c$ is a constant, is called an inverse-square field. This type of field appears in physics, for example, in **Coulomb’s Law** describing the electric field around a point charge.


### 2. 🌟 Gradient and Conservative Vector Fields

#### Gradient of a Scalar Function

If $\phi(x, y, z)$ is a scalar function of three variables, its **gradient** is a vector field defined as:


$$
\nabla \phi = \frac{\partial \phi}{\partial x} \mathbf{i} + \frac{\partial \phi}{\partial y} \mathbf{j} + \frac{\partial \phi}{\partial z} \mathbf{k}
$$


- The gradient points in the direction of the greatest rate of increase of $\phi$.
- The magnitude of the gradient gives the rate of increase in that direction.
- The operator $\nabla$ (called the **del operator**) is a vector differential operator.

#### Conservative Vector Fields

A vector field $\mathbf{F}$ is called **conservative** if it can be expressed as the gradient of some scalar function $\phi$:


$$
\mathbf{F} = \nabla \phi
$$


- The function $\phi$ is called the **potential function** of $\mathbf{F}$.
- Conservative fields have important properties, such as path independence of line integrals (work done depends only on start and end points).


### 3. 🔄 Divergence, Curl, and Laplacian

These are key differential operators used to analyze vector fields.

#### Divergence

For a vector field


$$
\mathbf{F}(x, y, z) = f(x, y, z) \mathbf{i} + g(x, y, z) \mathbf{j} + h(x, y, z) \mathbf{k}
$$


the **divergence** is a scalar function defined as:


$$
\text{div} \, \mathbf{F} = \nabla \cdot \mathbf{F} = \frac{\partial f}{\partial x} + \frac{\partial g}{\partial y} + \frac{\partial h}{\partial z}
$$


- Divergence measures the net rate of "flow" out of a point.
- Physically, it represents sources or sinks in a field (e.g., fluid flow expanding or compressing).

#### Curl

The **curl** of $\mathbf{F}$ is a vector field defined as:


$$
\text{curl} \, \mathbf{F} = \nabla \times \mathbf{F} = \left( \frac{\partial h}{\partial y} - \frac{\partial g}{\partial z} \right) \mathbf{i} - \left( \frac{\partial h}{\partial x} - \frac{\partial f}{\partial z} \right) \mathbf{j} + \left( \frac{\partial g}{\partial x} - \frac{\partial f}{\partial y} \right) \mathbf{k}
$$


- Curl measures the tendency of the field to induce rotation or "circulation" around a point.
- A zero curl indicates the field is irrotational.

#### Laplacian

The **Laplacian** operator applied to a scalar function $\phi$ is:


$$
\nabla^2 \phi = \frac{\partial^2 \phi}{\partial x^2} + \frac{\partial^2 \phi}{\partial y^2} + \frac{\partial^2 \phi}{\partial z^2}
$$


- It can also be expressed as the divergence of the gradient: $\nabla^2 \phi = \text{div}(\nabla \phi)$.
- The equation $\nabla^2 \phi = 0$ is called **Laplace’s equation**, fundamental in physics and engineering for steady-state heat flow, electrostatics, and fluid flow.


### 4. ➰ Line Integrals

Line integrals extend the concept of integration to functions defined along curves in space.

#### Scalar Line Integrals

If $f$ is a scalar function defined on a smooth curve $C$ parameterized by


$$
x = x(t), \quad y = y(t), \quad z = z(t), \quad a \leq t \leq b
$$


then the **line integral** of $f$ over $C$ is:


$$
\int_C f \, ds = \int_a^b f(x(t), y(t), z(t)) \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2} \, dt
$$


- Here, $ds$ represents an infinitesimal arc length along the curve.
- Intuitively, this integral sums the values of $f$ weighted by the length of the curve.
- If $f \geq 0$, the integral can be interpreted as the area of a "sheet" formed by moving a vertical segment of height $f$ along the curve.

#### Vector Line Integrals

If $\mathbf{F}$ is a vector field and $C$ is a piecewise smooth oriented curve parameterized by $\mathbf{r}(t)$, then the **line integral of $\mathbf{F}$ along $C$** is:


$$
\int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t) \, dt
$$


- This integral represents the work done by the force field $\mathbf{F}$ on a particle moving along $C$.
- The dot product ensures only the component of $\mathbf{F}$ tangent to the curve contributes.


### 5. 🔄 Independence of Path and Conservative Fields

#### Work Done by a Force Field

When a particle moves under a force field $\mathbf{F}$ along a curve $C$, the **work done** is given by the line integral:


$$
W = \int_C \mathbf{F} \cdot d\mathbf{r}
$$


#### Fundamental Theorem of Line Integrals

If $\mathbf{F} = \nabla \phi$ for some scalar function $\phi$, then for a curve $C$ from point $A$ to point $B$:


$$
\int_C \mathbf{F} \cdot d\mathbf{r} = \phi(B) - \phi(A)
$$


- This means the work done depends only on the endpoints, not on the path taken.
- Such vector fields are called **conservative**.

#### Closed Curves and Simply Connected Regions

- A **closed curve** is one where the start and end points coincide.
- A region $D \subseteq \mathbb{R}^n$ is **connected** if any two points in $D$ can be joined by a curve lying entirely in $D$.
- A connected region is **simply connected** if every closed curve in $D$ encloses only points inside $D$ (no holes).

#### Equivalence of Conditions for Conservative Fields

In a connected, open region $D$, the following are equivalent for a vector field $\mathbf{F}$:

- $\mathbf{F}$ is conservative (i.e., $\mathbf{F} = \nabla \phi$ for some $\phi$).
- The line integral of $\mathbf{F}$ around every closed curve in $D$ is zero.
- The line integral of $\mathbf{F}$ between any two points in $D$ is independent of the path taken.

#### Conservative Field Test (in 2D)

For a vector field $\mathbf{F} = f(x,y) \mathbf{i} + g(x,y) \mathbf{j}$ with continuous first partial derivatives in a simply connected region $D$, $\mathbf{F}$ is conservative if and only if:


$$
\frac{\partial f}{\partial y} = \frac{\partial g}{\partial x}
$$


This condition ensures the curl of $\mathbf{F}$ is zero in 2D, indicating no rotational component.


### 6. 🧮 Examples and Applications

#### Example 1: Line Integral of a Scalar Function

Evaluate


$$
\int_C x^2 z \, ds
$$


where $C$ is the helix parameterized by


$$
x = \cos t, \quad y = 2t, \quad z = \sin t, \quad 0 \leq t \leq \pi
$$


- Compute $ds = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2} dt$.
- Substitute $x(t), z(t)$ into the integrand.
- Integrate over $t$ from 0 to $\pi$.

#### Example 2: Vector Line Integral

Given $\mathbf{F} = y \mathbf{i} + x \mathbf{j}$ and $C$ is the top half of the circle $x^2 + y^2 = 4$ traversed counterclockwise from (2,0) to (-2,0):

- Parameterize $C$ as $x = 2 \cos \theta, y = 2 \sin \theta, 0 \leq \theta \leq \pi$.
- Compute $\mathbf{F}(\mathbf{r}(\theta)) \cdot \mathbf{r}'(\theta)$.
- Integrate over $\theta$.

#### Example 3: Checking if a Vector Field is Conservative

Given


$$
\mathbf{F} = (e^x \sin y - y) \mathbf{i} + (e^x \cos y - x - 2) \mathbf{j}
$$


- Check if $\frac{\partial}{\partial y} (e^x \sin y - y) = \frac{\partial}{\partial x} (e^x \cos y - x - 2)$.
- If equal, $\mathbf{F}$ is conservative.
- Find the potential function $\phi$ by integrating components.


### Summary

Vector calculus provides tools to analyze vector fields through operations like gradient, divergence, curl, and line integrals. Understanding conservative fields and the fundamental theorem of line integrals is crucial, especially in physics and engineering contexts where forces and potentials are involved. The ability to compute line integrals and test for conservativeness is essential for solving real-world problems involving work, energy, and fluid flow.