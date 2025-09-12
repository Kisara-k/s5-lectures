## 6. Green’s Theorem and Surface Integrals

## Key Points

#### 1. 🟢 Green’s Theorem  
- Green’s Theorem relates a line integral around a positively oriented, piecewise smooth, simple closed curve $C$ to a double integral over the simply connected region $D$ bounded by $C$.  
- Formula: $\displaystyle \oint_C (M\,dx + N\,dy) = \iint_D \left(\frac{\partial N}{\partial x} - \frac{\partial M}{\partial y}\right) dA$.  
- Applies when $M$ and $N$ have continuous partial derivatives on an open set containing $D$ and $C$.  
- For doubly connected regions (regions with holes), the theorem involves integrals over the outer boundary (counterclockwise) and inner boundaries (clockwise).  
- For multiply connected regions with $n$ holes, the integral is a sum of $n+1$ integrals with appropriate orientations.

#### 2. 🌐 Surface Integrals  
- A surface integral of a scalar function $f$ over a piecewise smooth surface $\sigma$ is defined as $\iint_\sigma f(x,y,z) \, dS = \lim \sum f(x_k^*, y_k^*, z_k^*) \Delta S_k$, where $\Delta S_k$ are small surface areas.  
- For a parametric surface $\mathbf{r}(u,v)$, the surface integral is $\iint_R f(\mathbf{r}(u,v)) \left| \frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v} \right| du\, dv$.  
- For surfaces defined as $z = g(x,y)$, the surface integral is $\iint_R f(x,y,g(x,y)) \sqrt{1 + g_x^2 + g_y^2} \, dx\, dy$.  
- A surface is **smooth** if it has a non-zero normal vector at every point; **piecewise smooth** if composed of finitely many smooth pieces.

#### 3. 🔄 Orientation of Surfaces  
- A surface is **orientable** if it has two distinct sides and a continuous choice of unit normal vector $\mathbf{n}$ over the surface.  
- The **positive orientation** of a parametric surface is given by the direction of $\mathbf{n} = \frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v}$.  
- The **negative orientation** is the opposite direction, $-\mathbf{n}$.  
- Non-orientable surfaces (e.g., Möbius strip) have only one side and no consistent normal vector.

#### 4. 💨 Flux of a Vector Field  
- Flux measures the volume of fluid passing through a surface per unit time, depending on fluid speed, surface orientation, and surface area.  
- The flux of a vector field $\mathbf{F}$ across an oriented surface $\sigma$ with unit normal $\mathbf{n}$ is $\iint_\sigma \mathbf{F} \cdot \mathbf{n} \, dS$.  
- Positive flux means net flow in the direction of $\mathbf{n}$; negative flux means net flow opposite to $\mathbf{n}$; zero flux means equal flow in both directions.  
- For parametric surfaces, flux is computed as $\iint_R \mathbf{F}(\mathbf{r}(u,v)) \cdot \left( \frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v} \right) du\, dv$.

#### 5. 📐 Flux for Non-Parametric Surfaces  
- Surfaces defined implicitly by $G(x,y,z) = 0$ have normal vectors given by $\nabla G$.  
- Surfaces of the form $z = g(x,y)$, $y = g(z,x)$, or $x = g(y,z)$ can be rewritten as $G(x,y,z) = 0$ for flux calculations.  
- The flux integral over such surfaces can be expressed as a double integral over the projection $R$ of the surface onto the coordinate plane of the independent variables, involving components of $\mathbf{F}$ and partial derivatives of $g$.  
- Positive orientation corresponds to the direction of $\nabla G$ pointing outward or upward, depending on context.



<br>

## Study Notes

### 1. 🟢 Green’s Theorem: Connecting Line Integrals and Area Integrals

#### Introduction to Green’s Theorem  
Green’s Theorem is a fundamental result in vector calculus that creates a powerful link between a line integral around a closed curve and a double integral over the region enclosed by that curve. It essentially allows us to convert a complicated line integral into a potentially simpler double integral, or vice versa. This theorem applies to planar regions and is especially useful in physics and engineering for calculating work done by a force field, circulation, and area.

#### Statement of Green’s Theorem  
Let $D$ be a simply connected region in the plane bounded by a positively oriented, piecewise smooth Jordan curve $C$. Suppose $M(x,y)$ and $N(x,y)$ are functions with continuous partial derivatives on an open set containing $D$ and its boundary $C$. Then Green’s Theorem states:


$$
\oint_C (M\,dx + N\,dy) = \iint_D \left( \frac{\partial N}{\partial x} - \frac{\partial M}{\partial y} \right) dA
$$


- The left side is the line integral of the vector field $\mathbf{F} = M\mathbf{i} + N\mathbf{j}$ around the closed curve $C$.
- The right side is the double integral over the region $D$ enclosed by $C$.

#### Intuition  
Think of the line integral as measuring the circulation of a vector field around the boundary $C$, while the double integral measures the "curl" or rotation inside the region $D$. Green’s Theorem tells us these two quantities are equal.

#### Examples  
- **Example 1:** Verifying Green’s theorem for the line integral $\int (-y\,dx + x\,dy)$ over a semicircular path. This shows how the theorem works on a simple curved boundary.
- **Example 2:** Calculating work done by a force field $\mathbf{F}(x,y) = (x + xy^2)\mathbf{i} + 2(x^2 y - y^2 \sin y)\mathbf{j}$ along a closed path $C$.
- **Example 3:** Using Green’s theorem to find the area of an ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, which results in the well-known formula $\pi a b$.

#### Extension to Multiply Connected Regions  
Green’s Theorem also applies to regions with holes (doubly or multiply connected). For a region $R$ with an outer boundary $C_1$ oriented counterclockwise and inner boundaries $C_2, C_3, \ldots$ oriented clockwise (around holes), the theorem generalizes to:


$$
\oint_{C_1} (M\,dx + N\,dy) - \sum_{i=2}^n \oint_{C_i} (M\,dx + N\,dy) = \iint_R \left( \frac{\partial N}{\partial x} - \frac{\partial M}{\partial y} \right) dA
$$


This means the total circulation around the outer boundary minus the circulation around the holes equals the double integral over the entire multiply connected region.


### 2. 🌐 Surface Integrals: Extending Integration to Surfaces in 3D

#### Introduction to Surface Integrals  
Surface integrals generalize the concept of integration to functions defined on surfaces in three-dimensional space. Instead of integrating over a curve (1D) or a region in the plane (2D), surface integrals allow us to integrate over curved 2D surfaces embedded in 3D space. This is crucial in physics for calculating quantities like flux, mass, and surface area.

#### Normal Vectors to Surfaces  
To define surface integrals, we need to understand the concept of a **normal vector** to a surface, which is a vector perpendicular to the surface at each point.

- **Parametric surfaces:** If a surface $S$ is given parametrically by $\mathbf{r}(u,v) = (x(u,v), y(u,v), z(u,v))$, then a normal vector at a point is given by the cross product of the partial derivatives:


$$
\mathbf{n} = \frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v}
$$


- **Implicit surfaces:** If the surface is defined implicitly by $G(x,y,z) = 0$, then the gradient vector $\nabla G = \left( \frac{\partial G}{\partial x}, \frac{\partial G}{\partial y}, \frac{\partial G}{\partial z} \right)$ is normal to the surface at each point.

- **Graphs of functions:** For surfaces defined as $z = g(x,y)$, an upward-pointing normal vector is:


$$
\mathbf{n} = (-g_x, -g_y, 1)
$$


where $g_x$ and $g_y$ are partial derivatives of $g$.

#### Definition of Surface Integral of a Scalar Function  
Given a continuous scalar function $f(x,y,z)$ defined on a piecewise smooth surface $\sigma$, the surface integral of $f$ over $\sigma$ is defined as the limit of sums:


$$
\iint_\sigma f(x,y,z) \, dS = \lim_{\max \Delta S_k \to 0} \sum_{k=1}^n f(x_k^*, y_k^*, z_k^*) \Delta S_k
$$


where $\Delta S_k$ is the area of the $k$-th small piece of the surface, and $(x_k^*, y_k^*, z_k^*)$ is a sample point in that piece.

#### Calculating Surface Integrals  
- For a parametric surface $\mathbf{r}(u,v)$ over a region $R$ in the $uv$-plane:


$$
\iint_\sigma f(x,y,z) \, dS = \iint_R f(\mathbf{r}(u,v)) \left| \frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v} \right| du\, dv
$$


- For surfaces given by $z = g(x,y)$ over a region $R$ in the $xy$-plane:


$$
\iint_\sigma f(x,y,z) \, dS = \iint_R f(x,y,g(x,y)) \sqrt{1 + g_x^2 + g_y^2} \, dx\, dy
$$


#### Examples  
- **Example 5:** Evaluate $\iint_\sigma x^2 \, dS$ over the unit sphere $x^2 + y^2 + z^2 = 1$.
- **Example 6:** Evaluate $\iint_\sigma y^2 z^2 \, dS$ where $\sigma$ is the part of the cone $z = \sqrt{x^2 + y^2}$ between planes $z=1$ and $z=2$.
- **Example 7:** Find the mass of a lamina shaped like the top hemisphere with density $\rho(x,y,z) = z$.


### 3. 🔄 Orientation of Surfaces: Why Direction Matters

#### What is Orientation?  
Orientation of a surface refers to the consistent choice of a direction for the normal vector at every point on the surface. This is important because many surface integrals, especially flux integrals, depend on the direction of the normal vector.

- A **two-sided surface** (like a sphere or a plane) is **orientable** because you can consistently choose a "positive" side.
- A **one-sided surface** (like a Möbius strip) is **non-orientable** because it has only one side, so you cannot consistently define a normal vector direction.

#### Positive and Negative Orientation  
For a smooth parametric surface $\mathbf{r}(u,v)$, the normal vector $\mathbf{n} = \frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v}$ defines the **positive orientation**. Reversing the sign of $\mathbf{n}$ gives the **negative orientation**.

Choosing the orientation is crucial when calculating flux because the sign of the flux depends on the direction of the normal vector.


### 4. 💨 Flux: Measuring Flow Through a Surface

#### What is Flux?  
Flux measures the quantity of a vector field (like fluid velocity) passing through a surface per unit time. Imagine a fluid flowing through a net: the flux tells you how much fluid passes through the net.

#### Factors Affecting Flux  
1. **Speed of the fluid:** Faster flow means more volume passes through.
2. **Orientation of the surface:** The flux is greatest when the flow is perpendicular to the surface.
3. **Area of the surface:** Larger area means more fluid can pass through.

#### Mathematical Definition of Flux  
Given a vector field $\mathbf{F}$ with continuous partial derivatives on a surface $\sigma$ oriented by a unit normal vector $\mathbf{n}$, the flux of $\mathbf{F}$ across $\sigma$ is:


$$
\iint_\sigma \mathbf{F} \cdot \mathbf{n} \, dS
$$


- A **positive flux** means more fluid passes through in the direction of $\mathbf{n}$.
- A **negative flux** means more fluid passes in the opposite direction.
- Zero flux means equal flow in both directions.

#### Calculating Flux for Parametric Surfaces  
If $\sigma$ is given by $\mathbf{r}(u,v)$, then:


$$
\iint_\sigma \mathbf{F} \cdot \mathbf{n} \, dS = \iint_R \mathbf{F}(\mathbf{r}(u,v)) \cdot \left( \frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v} \right) du\, dv
$$


#### Examples  
- **Example 8:** Find the flux of $\mathbf{F}(x,y,z) = z \mathbf{k}$ across the outward-oriented sphere $x^2 + y^2 + z^2 = a^2$.


### 5. 📐 Orientation and Flux for Non-Parametric Surfaces

#### Surfaces Defined Implicitly or as Graphs  
Surfaces given by equations like $z = g(x,y)$, $y = g(z,x)$, or $x = g(y,z)$ can be treated as level surfaces of a function $G(x,y,z) = 0$, where:


$$
G(x,y,z) = z - g(x,y), \quad \text{or} \quad y - g(z,x), \quad \text{or} \quad x - g(y,z)
$$


The gradient $\nabla G$ is normal to the surface.

#### Flux Integral for Such Surfaces  
If $\sigma$ is oriented positively, and $R$ is the projection of $\sigma$ onto the coordinate plane of the independent variables, then the flux integral can be expressed as a double integral over $R$ involving the components of $\mathbf{F}$ and the partial derivatives of $g$.

This approach simplifies flux calculations for surfaces defined as graphs.


### Summary  
- **Green’s Theorem** connects line integrals around closed curves to double integrals over the enclosed region, simplifying many calculations.
- **Surface integrals** extend integration to curved surfaces in 3D, requiring understanding of normal vectors.
- **Orientation** of surfaces is essential for defining consistent normal vectors and calculating flux.
- **Flux** measures how much of a vector field passes through a surface, depending on speed, orientation, and area.
- Surfaces defined implicitly or as graphs can be handled using gradients and projections for flux calculations.