## 7. Stokes Theorem and Divergence Theorem

## Key Points

#### 1. 🌀 Stokes' Theorem  
- Stokes' Theorem relates the line integral of a vector field **F** around a closed curve **C** to the surface integral of the curl of **F** over the surface **σ** bounded by **C**.  
- Formula: $\displaystyle \oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_\sigma (\nabla \times \mathbf{F}) \cdot \mathbf{n} \, dS$  
- The vector field **F** must have continuous components with continuous first partial derivatives on an open set containing **σ**.  
- The curve **C** must be simple, closed, piecewise smooth, and positively oriented with respect to the surface **σ**.  
- The unit normal vector **n** defines the orientation of the surface **σ**.

#### 2. 🔗 Relationship Between Green's Theorem and Stokes' Theorem  
- Green's Theorem is a special case of Stokes' Theorem applied to a flat surface in the xy-plane.  
- For a vector field $\mathbf{F}(x,y) = f(x,y)\mathbf{i} + g(x,y)\mathbf{j} + 0\mathbf{k}$, and region $R$ enclosed by curve $C$,  

$$
\oint_C (f dx + g dy) = \iint_R \left( \frac{\partial g}{\partial x} - \frac{\partial f}{\partial y} \right) dA
$$
  
- The orientation of $R$ is upward, and $C$ is oriented counterclockwise when viewed from above.

#### 3. 🌊 Divergence Theorem  
- The Divergence Theorem relates the flux of a vector field **F** through a closed surface **σ** to the triple integral of the divergence of **F** over the volume **R** enclosed by **σ**.  
- Formula: $\displaystyle \iint_\sigma \mathbf{F} \cdot \mathbf{n} \, dS = \iiint_R \nabla \cdot \mathbf{F} \, dV$  
- The vector field **F** must have continuous components with continuous partial derivatives on an open set containing **R**.  
- The surface **σ** must be smooth, orientable, and closed, with **n** as the outward unit normal vector.

#### 4. 🌬️ Divergence as Flux Density  
- Divergence at a point $P_0$ is defined as the limit of the outward flux per unit volume as the volume shrinks to zero around $P_0$:  

$$
\text{div} \mathbf{F}(P_0) = \lim_{\text{vol}(G) \to 0} \frac{\phi(G)}{\text{vol}(G)}
$$
  
where $\phi(G)$ is the flux of **F** across the surface of a small region $G$ around $P_0$.  
- Physically, if **F** is a fluid velocity field, divergence measures the net rate of fluid flowing out of (positive divergence) or into (negative divergence) a point.  
- Zero divergence implies incompressible flow (no net volume change).

#### 5. ✅ Conditions for Applying Theorems  
- For **Stokes' Theorem**:  
  - Surface **σ** must be piecewise smooth and oriented.  
  - Boundary curve **C** must be simple, closed, piecewise smooth, and positively oriented.  
  - Vector field **F** must have continuous components and continuous first partial derivatives on an open set containing **σ**.  
- For **Divergence Theorem**:  
  - Surface **σ** must be smooth, closed, and orientable with outward normal.  
  - Vector field **F** must have continuous components and continuous partial derivatives on an open set containing the enclosed volume **R**.



<br>

## Study Notes

### 1. 🌀 Introduction to Stokes' Theorem

Stokes' Theorem is a fundamental result in vector calculus that connects the circulation of a vector field around a closed curve to the curl of the vector field over the surface bounded by that curve. It generalizes Green’s Theorem from the plane to surfaces in three-dimensional space.

#### What is Stokes' Theorem?

Imagine you have a smooth surface, like a curved sheet, which is bounded by a closed loop (a curve that starts and ends at the same point without crossing itself). Stokes' Theorem tells us that the total "circulation" of a vector field **F** around this boundary curve is equal to the total "curl" of **F** passing through the surface.

More formally:

- Let **σ** be a piecewise smooth, oriented surface.
- Let **C** be the simple, closed, piecewise smooth curve bounding **σ**.
- Let **F(x, y, z) = f(x, y, z)i + g(x, y, z)j + h(x, y, z)k** be a vector field whose components and their first partial derivatives are continuous on an open set containing **σ**.
- Let **n** be the unit normal vector to the surface **σ**.

Then, Stokes' Theorem states:


$$
\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_\sigma (\nabla \times \mathbf{F}) \cdot \mathbf{n} \, dS
$$


This means the line integral of **F** around the curve **C** equals the surface integral of the curl of **F** over **σ**.

#### Key Concepts:

- **Line integral around C**: Measures the total "circulation" or "work done" by the vector field along the closed curve.
- **Curl of F**: A vector field that measures the tendency of **F** to rotate or swirl around a point.
- **Surface integral of curl F**: Measures the total rotation passing through the surface.

#### Why is this important?

Stokes' Theorem allows us to convert a potentially complicated line integral into a surface integral, or vice versa, often simplifying calculations. It also provides a deep connection between local rotation (curl) and global circulation.


### 2. 🔄 Examples Illustrating Stokes' Theorem

#### Example 1: Curve of Intersection of a Plane and an Ellipsoid

- **Problem**: Evaluate the line integral $\oint_C \mathbf{F} \cdot d\mathbf{r}$, where **C** is the curve formed by the intersection of the plane $x + z = 1$ and the ellipsoid $x^2 + 2y^2 + z^2 = 1$.
- **Orientation**: The curve is oriented counterclockwise as viewed from above.

**Approach**: Instead of directly evaluating the line integral, use Stokes' Theorem to convert it into a surface integral of the curl of **F** over the surface bounded by **C**.


#### Example 2: Surface Integral of Curl F over a Paraboloid

- **Problem**: Evaluate $\iint_\sigma (\nabla \times \mathbf{F}) \cdot \mathbf{n} \, dS$, where $\mathbf{F} = x\mathbf{i} + y^2 \mathbf{j} + z e^{xy} \mathbf{k}$ and $\sigma$ is the part of the surface $z = 1 - x^2 - 2y^2$ with $z \geq 0$.

**Approach**: Directly compute the curl of **F**, find the unit normal vector **n** to the surface, and evaluate the surface integral.


### 3. 🔗 Relationship Between Green's Theorem and Stokes' Theorem

Green’s Theorem is a special case of Stokes' Theorem restricted to the plane.

- Suppose **F(x, y) = f(x, y)i + g(x, y)j + 0k** is a vector field in the plane.
- Let **R** be a region in the xy-plane enclosed by a simple closed curve **C**.
- Treat **R** as a flat surface with upward orientation and **C** oriented counterclockwise.

Then, the surface integral over **R** becomes a double integral over the region, and Stokes' Theorem reduces to Green's Theorem:


$$
\oint_C (f dx + g dy) = \iint_R \left( \frac{\partial g}{\partial x} - \frac{\partial f}{\partial y} \right) dA
$$


This shows how Stokes' Theorem generalizes the planar circulation-curl relationship to curved surfaces in 3D.


### 4. 🌊 Introduction to the Divergence Theorem

The Divergence Theorem, also known as Gauss's Theorem, relates the flux of a vector field through a closed surface to the divergence of the vector field inside the volume bounded by that surface.

#### What is the Divergence Theorem?

Imagine a closed surface **σ** that encloses a solid region **R** in three-dimensional space. The Divergence Theorem states that the total outward flux of a vector field **F** through the surface **σ** equals the triple integral of the divergence of **F** over the volume **R** inside.

Formally:

- Let **σ** be a smooth, orientable closed surface enclosing a solid region **R**.
- Let **F** be a vector field with continuous partial derivatives on an open set containing **R**.
- Let **n** be the outward unit normal vector on **σ**.

Then,


$$
\iint_\sigma \mathbf{F} \cdot \mathbf{n} \, dS = \iiint_R \nabla \cdot \mathbf{F} \, dV
$$


Where:

- $\mathbf{F} \cdot \mathbf{n}$ is the flux density through the surface.
- $\nabla \cdot \mathbf{F}$ (divergence of **F**) measures the net rate of "outflow" of the vector field at a point.

#### Why is this important?

The Divergence Theorem allows us to convert a complicated surface integral into a volume integral, which is often easier to evaluate. It also provides a physical interpretation of divergence as the source or sink strength of a vector field inside a volume.


### 5. 📚 Examples Illustrating the Divergence Theorem

#### Example 3: Flux Through a Tetrahedron

- **Problem**: Evaluate $\iint_S \mathbf{F} \cdot \mathbf{n} \, dS$, where $\mathbf{F} = x^2 \mathbf{i} + xy \mathbf{j} + x^3 y^3 \mathbf{k}$ and $S$ is the surface of the tetrahedron bounded by the plane $x + y + z = 1$ and the coordinate planes.
- **Orientation**: Outward unit normal vector.

**Approach**: Use the Divergence Theorem to convert the surface integral into a triple integral of the divergence of **F** over the tetrahedron volume.


#### Example 4: Flux Through Part of a Cube

- **Problem**: Evaluate $\iint_S \mathbf{F} \cdot \mathbf{n} \, dS$, where $\mathbf{F} = xy \mathbf{i} - z^2 \mathbf{k}$ and $S$ is the upper five faces of the unit cube $[0,1]^3$.

**Approach**: Since the surface is not closed (missing the bottom face), you can either:

- Add the missing face to close the surface, apply the Divergence Theorem, then subtract the flux through the missing face, or
- Directly compute the flux through each face and sum.


### 6. 🌬️ Divergence as Flux Density: Physical Interpretation

The divergence of a vector field at a point can be understood as the "flux density" or the net rate at which the vector field is "flowing out" of an infinitesimally small volume around that point.

#### Explanation:

- Consider a small spherical region $G$ centered at a point $P_0$.
- The surface of this sphere is $\sigma(G)$, oriented outward.
- The volume of $G$ is $\text{vol}(G)$.
- The flux of **F** across $\sigma(G)$ is $\phi(G)$.

If the divergence of **F** is continuous near $P_0$, then inside this small region, $\text{div} \mathbf{F}$ is approximately constant and equal to $\text{div} \mathbf{F}(P_0)$.

Thus,


$$
\iiint_G \text{div} \mathbf{F} \, dV \approx \text{div} \mathbf{F}(P_0) \times \text{vol}(G)
$$


But by the Divergence Theorem, this volume integral equals the flux $\phi(G)$ through the surface:


$$
\phi(G) = \iint_{\sigma(G)} \mathbf{F} \cdot \mathbf{n} \, dS
$$


Therefore,


$$
\text{div} \mathbf{F}(P_0) \approx \frac{\phi(G)}{\text{vol}(G)}
$$


Taking the limit as the volume shrinks to zero:


$$
\text{div} \mathbf{F}(P_0) = \lim_{\text{vol}(G) \to 0} \frac{\phi(G)}{\text{vol}(G)}
$$


This limit defines the divergence at $P_0$ as the **outward flux per unit volume** at that point.

#### Physical Meaning:

- If **F** represents the velocity field of a fluid, then the divergence at a point measures how much fluid is "expanding" or "compressing" there.
- A positive divergence means the fluid is "flowing out" (source).
- A negative divergence means the fluid is "flowing in" (sink).
- Zero divergence means incompressible flow (no net volume change).


### Summary

- **Stokes' Theorem** connects the circulation of a vector field around a closed curve to the curl of the field over the surface bounded by that curve.
- **Green's Theorem** is a special case of Stokes' Theorem in the plane.
- **Divergence Theorem** relates the flux of a vector field through a closed surface to the divergence of the field inside the volume.
- Divergence can be interpreted as the flux density or the net outflow per unit volume at a point.
- These theorems are powerful tools for converting between line, surface, and volume integrals, simplifying calculations and providing deep geometric and physical insights.