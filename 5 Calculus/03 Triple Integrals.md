## 3. Triple Integrals

## Key Points

#### 1. 📦 Definition of Triple Integrals
- The triple integral of a function $f$ over a solid region $G$ is defined as the limit of Riemann sums over subboxes partitioning $G$.
- The volume element in rectangular coordinates is $dV = dx\, dy\, dz$.
- The triple integral is denoted as $\iiint_G f(x,y,z) \, dV$.

#### 2. 🔄 Properties of Triple Integrals
- If $G$ is subdivided into two subregions $G_1$ and $G_2$, then $\iiint_G f \, dV = \iiint_{G_1} f \, dV + \iiint_{G_2} f \, dV$.
- Triple integrals are linear: constants can be factored out, and integrals of sums equal sums of integrals.

#### 3. 📐 Fubini’s Theorem for Triple Integrals
- For a rectangular box $G = \{(x,y,z) \mid a \leq x \leq b, c \leq y \leq d, k \leq z \leq l\}$, if $f$ is continuous on $G$, then:


$$
\iiint_G f(x,y,z) \, dV = \int_a^b \int_c^d \int_k^l f(x,y,z) \, dz \, dy \, dx
$$


- The order of integration can be changed arbitrarily among $dx, dy, dz$.

#### 4. 🏞️ Triple Integrals over Simple $xy$-Solids
- A simple $xy$-solid $G$ is bounded by surfaces $z = u(x,y)$ (lower) and $z = v(x,y)$ (upper), with projection $R$ on the $xy$-plane.
- The triple integral over $G$ is:


$$
\iiint_G f(x,y,z) \, dV = \iint_R \int_{u(x,y)}^{v(x,y)} f(x,y,z) \, dz \, dA
$$


- If $R$ is vertically simple (Type I), $y$ varies between $g_1(x)$ and $g_2(x)$ for $x \in [a,b]$.
- If $R$ is horizontally simple (Type II), $x$ varies between $h_1(y)$ and $h_2(y)$ for $y \in [c,d]$.

#### 5. 🔄 Triple Integrals in Cylindrical Coordinates
- Cylindrical coordinates: $x = r \cos \theta, y = r \sin \theta, z = z$.
- Volume element in cylindrical coordinates: $dV = r \, dz \, dr \, d\theta$.
- For a solid $G$ bounded by $z = u(r,\theta)$ and $z = v(r,\theta)$, with projection $R$ in the $xy$-plane:


$$
\iiint_G f(x,y,z) \, dV = \iint_R \int_{u(r,\theta)}^{v(r,\theta)} f(r \cos \theta, r \sin \theta, z) \, r \, dz \, dr \, d\theta
$$


- The limits for $r$ and $\theta$ depend on the polar region $R$.

#### 6. 🧩 Application Examples (Key Setup Facts)
- To find volume bounded by surfaces, express the solid as a triple integral with appropriate limits.
- For solids bounded by cylinders and planes, project onto the $xy$-plane and use the bounding surfaces to set $z$-limits.
- For tetrahedrons bounded by coordinate planes and a plane $ax + by + cz = d$, express $z$ in terms of $x$ and $y$ and set limits accordingly.
- For solids bounded by paraboloids and planes, set $z$-limits between the paraboloid and the plane.
- Cylindrical coordinates simplify integration for solids with circular symmetry or involving cylinders and cones.



<br>

## Study Notes

### 1. 📦 Introduction to Triple Integrals

Triple integrals extend the concept of single and double integrals to functions of three variables, allowing us to integrate over three-dimensional regions (solids). While single integrals find areas under curves and double integrals find volumes under surfaces, triple integrals help us calculate quantities like volume, mass, or charge distributed throughout a 3D region.

#### What is a Triple Integral?

Imagine a solid region $G$ in three-dimensional space. To find the integral of a function $f(x,y,z)$ over this solid, we divide $G$ into many tiny rectangular boxes (subboxes). Each subbox has a small volume $\Delta V_k$, and we pick a sample point $(x_k, y_k, z_k)$ inside it. We then approximate the integral by summing up the values of the function at these points multiplied by the volume of the subboxes:


$$
\sum_{k=1}^n f(x_k, y_k, z_k) \Delta V_k
$$


As the subboxes get smaller and more numerous (i.e., as $n \to \infty$), this sum approaches the exact value of the triple integral:


$$
\iiint_G f(x,y,z) \, dV = \lim_{n \to \infty} \sum_{k=1}^n f(x_k, y_k, z_k) \Delta V_k
$$


This limit, if it exists, is called the **triple integral** of $f$ over the region $G$.


### 2. 🔄 Properties and Computation of Triple Integrals

#### Key Properties

- **Additivity:** If the solid $G$ is split into two subregions $G_1$ and $G_2$, then the integral over $G$ is the sum of the integrals over $G_1$ and $G_2$:


$$
\iiint_G f \, dV = \iiint_{G_1} f \, dV + \iiint_{G_2} f \, dV
$$


- **Linearity:** The integral of a sum of functions is the sum of their integrals, and constants can be factored out.

#### Fubini’s Theorem for Triple Integrals

If $G$ is a rectangular box defined by:


$$
a \leq x \leq b, \quad c \leq y \leq d, \quad k \leq z \leq l
$$


and $f$ is continuous on $G$, then the triple integral can be computed as an **iterated integral**:


$$
\iiint_G f(x,y,z) \, dV = \int_a^b \int_c^d \int_k^l f(x,y,z) \, dz \, dy \, dx
$$


Importantly, the order of integration can be changed freely (e.g., $dx\, dy\, dz$, $dy\, dz\, dx$, etc.), which can simplify calculations depending on the function and limits.


### 3. 🏞️ Triple Integrals over General Regions

Often, the region $G$ is not a simple rectangular box but a more complicated solid bounded by surfaces.

#### Simple $xy$-Solid Regions

A **simple $xy$-solid** is a solid region $G$ bounded above and below by surfaces:


$$
z = v(x,y) \quad \text{(upper surface)}, \quad z = u(x,y) \quad \text{(lower surface)}
$$


and whose projection onto the $xy$-plane is a region $R$. The functions $u$ and $v$ are continuous on $R$, and for every point $(x,y) \in R$, $u(x,y) \leq v(x,y)$.

The triple integral over $G$ can be written as:


$$
\iiint_G f(x,y,z) \, dV = \iint_R \int_{u(x,y)}^{v(x,y)} f(x,y,z) \, dz \, dA
$$


where $dA$ is the area element in the $xy$-plane.

#### Types of Projections for $R$

- **Vertically simple (Type I):** For each fixed $x \in [a,b]$, $y$ varies between two functions $g_1(x)$ and $g_2(x)$:


$$
R = \{ (x,y) \mid a \leq x \leq b, \quad g_1(x) \leq y \leq g_2(x) \}
$$


- **Horizontally simple (Type II):** For each fixed $y \in [c,d]$, $x$ varies between two functions $h_1(y)$ and $h_2(y)$:


$$
R = \{ (x,y) \mid c \leq y \leq d, \quad h_1(y) \leq x \leq h_2(y) \}
$$


Depending on the shape of $R$, you choose the appropriate limits for the double integral.

#### Remark

The projection $R$ can also be onto the $yz$-plane or $zx$-plane, and the triple integral can be set up similarly by changing variables accordingly.


### 4. 🔄 Triple Integrals in Cylindrical Coordinates

Sometimes, the region $G$ or the function $f$ is easier to describe in **cylindrical coordinates** rather than rectangular coordinates. Cylindrical coordinates are a natural extension of polar coordinates into three dimensions.

#### Cylindrical Coordinates Definition

The coordinates $(r, \theta, z)$ relate to rectangular coordinates $(x,y,z)$ as:


$$
x = r \cos \theta, \quad y = r \sin \theta, \quad z = z
$$


where:

- $r \geq 0$ is the distance from the $z$-axis,
- $\theta$ is the angle in the $xy$-plane from the positive $x$-axis,
- $z$ is the height, same as in rectangular coordinates.

#### Volume Element in Cylindrical Coordinates

The volume element $dV$ in cylindrical coordinates is:


$$
dV = r \, dz \, dr \, d\theta
$$


The extra factor $r$ accounts for the "stretching" of the area element in polar coordinates.

#### Triple Integral in Cylindrical Coordinates

If $G$ is bounded above and below by surfaces:


$$
z = v(r, \theta), \quad z = u(r, \theta)
$$


and its projection onto the $xy$-plane is a simple polar region $R$, then:


$$
\iiint_G f(x,y,z) \, dV = \iint_R \int_{u(r,\theta)}^{v(r,\theta)} f(r \cos \theta, r \sin \theta, z) \, r \, dz \, dr \, d\theta
$$


The limits for $r$ and $\theta$ depend on the shape of the projection $R$.


### 5. 🧩 Examples and Applications

#### Example 1: Evaluating a Triple Integral over a Box

Evaluate:


$$
\iiint_B z^2 y e^x \, dV
$$


where $B$ is the box defined by:


$$
0 \leq x \leq 1, \quad 0 \leq y \leq 1, \quad 0 \leq z \leq 1
$$


Since the limits are constants, use Fubini’s theorem to write the integral as an iterated integral and integrate step-by-step.


#### Example 2: Volume of a Solid in the First Octant

Find the volume of the solid $D$ in the first octant bounded by the cylinder:


$$
x^2 + y^2 = 4
$$


and the plane:


$$
2y + z = 4
$$


Here, the region is bounded by a curved surface (cylinder) and a plane. You would:

- Project the solid onto the $xy$-plane (circle $x^2 + y^2 \leq 4$),
- Express $z$ in terms of $x$ and $y$ from the plane equation,
- Set up the triple integral with limits for $z$ from 0 to $4 - 2y$,
- Integrate over the circular region in the $xy$-plane.


#### Example 3: Volume of a Tetrahedron

Find the volume of the tetrahedron bounded by the plane:


$$
2x + y + 3z = 6
$$


and the coordinate planes $x=0, y=0, z=0$.

- The region is a simple solid bounded by planes,
- Express $z$ in terms of $x$ and $y$,
- Project onto the $xy$-plane,
- Set up the triple integral accordingly.


#### Example 4: Volume Between a Paraboloid and a Plane

Find the volume of the solid bounded below by the paraboloid:


$$
z = x^2 + y^2
$$


and above by the plane:


$$
2x + z = 3
$$


- Express $z$ from the plane as $z = 3 - 2x$,
- The region is bounded between two surfaces,
- Project onto the $xy$-plane,
- Set up the triple integral with limits for $z$ between the paraboloid and the plane.


#### Example 5: Triple Integral in Cylindrical Coordinates

Find the volume of the solid in the first octant bounded by:

- The cylinder $x^2 + y^2 = 2y$,
- The half-cone $z = \sqrt{x^2 + y^2}$,
- The $xy$-plane.

Here, cylindrical coordinates simplify the problem:

- Rewrite the cylinder in cylindrical form,
- Express the cone as $z = r$,
- Set limits for $r, \theta, z$,
- Integrate using the volume element $r \, dz \, dr \, d\theta$.


### Summary

Triple integrals allow us to integrate functions over three-dimensional regions, which is essential for calculating volumes, masses, and other physical quantities in 3D space. The key steps involve:

- Understanding the region $G$ and its boundaries,
- Choosing the appropriate coordinate system (rectangular or cylindrical),
- Setting up the limits of integration carefully,
- Applying Fubini’s theorem to write the triple integral as an iterated integral,
- Evaluating the integral step-by-step.

Mastering triple integrals requires practice with different types of regions and coordinate systems, as well as understanding how to project solids onto coordinate planes to simplify the integration process.