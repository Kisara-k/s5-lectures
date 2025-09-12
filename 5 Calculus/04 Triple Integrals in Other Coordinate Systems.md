## 4. Triple Integrals in Other Coordinate Systems

## Key Points

#### 1. 🔵 Spherical Coordinate System  
- Coordinates $(\rho, \phi, \theta)$ relate to rectangular coordinates as:  

$$
  x = \rho \sin \phi \cos \theta, \quad y = \rho \sin \phi \sin \theta, \quad z = \rho \cos \phi
$$

- $\rho$ = distance from origin, $\phi$ = angle from positive $z$-axis, $\theta$ = angle in $xy$-plane from positive $x$-axis.

#### 2. 📦 Volume Element in Spherical Coordinates  
- The volume element is:  

$$
  dV = \rho^2 \sin \phi \, d\rho \, d\phi \, d\theta
$$

- This accounts for the geometry of spherical shells and angular sectors.

#### 3. 🔄 Triple Integral in Spherical Coordinates  
- A triple integral over region $G$ is:  

$$
  \iiint_G f(x,y,z) \, dV = \iiint_G f(\rho \sin \phi \cos \theta, \rho \sin \phi \sin \theta, \rho \cos \phi) \, \rho^2 \sin \phi \, d\rho \, d\phi \, d\theta
$$

- Limits of integration depend on the region $G$ expressed in spherical coordinates.

#### 4. 🧮 Jacobian for Change of Variables (Two Variables)  
- For transformation $T: (u,v) \to (x,y)$ with $x = x(u,v)$, $y = y(u,v)$, the Jacobian is:  

$$
  J(u,v) = \frac{\partial(x,y)}{\partial(u,v)} = \frac{\partial x}{\partial u} \frac{\partial y}{\partial v} - \frac{\partial x}{\partial v} \frac{\partial y}{\partial u}
$$

- The Jacobian measures the area scaling factor under the transformation.

#### 5. 🔄 Change of Variable Formula for Double Integrals  
- If $T$ maps region $S$ in $uv$-plane to $R$ in $xy$-plane, and $J(u,v)$ is non-zero and sign-consistent, then:  

$$
  \iint_R f(x,y) \, dx\, dy = \iint_S f(x(u,v), y(u,v)) \, |J(u,v)| \, du\, dv
$$


#### 6. 🧮 Jacobian for Change of Variables (Three Variables)  
- For transformation $T: (u,v,w) \to (x,y,z)$ with $x = x(u,v,w)$, $y = y(u,v,w)$, $z = z(u,v,w)$, the Jacobian is:  

$$
  J(u,v,w) = \frac{\partial(x,y,z)}{\partial(u,v,w)} = 
  \begin{vmatrix}
  \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} & \frac{\partial x}{\partial w} \\
  \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} & \frac{\partial y}{\partial w} \\
  \frac{\partial z}{\partial u} & \frac{\partial z}{\partial v} & \frac{\partial z}{\partial w}
  \end{vmatrix}
$$

- The Jacobian measures the volume scaling factor under the transformation.

#### 7. 🔄 Change of Variable Formula for Triple Integrals  
- If $T$ maps region $S$ in $uvw$-space to $R$ in $xyz$-space, and $J(u,v,w)$ is non-zero and sign-consistent, then:  

$$
  \iiint_R f(x,y,z) \, dx\, dy\, dz = \iiint_S f(x(u,v,w), y(u,v,w), z(u,v,w)) \, |J(u,v,w)| \, du\, dv\, dw
$$


#### 8. 📌 Important Conditions for Jacobians  
- The Jacobian must be **non-zero** and **not change sign** on the region of integration for the change of variables formula to hold.
- The transformation must be **one-to-one** (invertible) on the region.



<br>

## Study Notes

### 1. 🌐 Introduction to Triple Integrals in Other Coordinate Systems

When dealing with triple integrals, sometimes the rectangular (Cartesian) coordinate system $(x, y, z)$ is not the most convenient choice. This is especially true when the region of integration or the function has symmetry that aligns better with other coordinate systems, such as cylindrical or spherical coordinates. Using these alternative coordinate systems can simplify the integral setup and evaluation.

This section focuses on **triple integrals in spherical coordinates** and the important concept of **change of variables** using Jacobians, which allows us to transform integrals from one coordinate system to another.


### 2. 🔵 Spherical Coordinate System: Definition and Conversion

The **spherical coordinate system** is a three-dimensional coordinate system where a point in space is represented by three parameters: $\rho$, $\phi$, and $\theta$.

- $\rho$ (rho) is the distance from the origin to the point.
- $\phi$ (phi) is the angle measured from the positive $z$-axis down to the point (polar angle).
- $\theta$ (theta) is the angle measured in the $xy$-plane from the positive $x$-axis (azimuthal angle).

The conversion formulas from spherical coordinates $(\rho, \phi, \theta)$ to rectangular coordinates $(x, y, z)$ are:


$$
x = \rho \sin \phi \cos \theta
$$


$$
y = \rho \sin \phi \sin \theta
$$


$$
z = \rho \cos \phi
$$


**Why use spherical coordinates?**  
Spherical coordinates are especially useful when the region of integration is a sphere, a spherical shell, or any shape with radial symmetry about the origin. They simplify the limits of integration and the integrand.


### 3. 📦 Triple Integrals in Spherical Coordinates: Definition and Evaluation

#### 3.1 Understanding the Volume Element in Spherical Coordinates

When integrating over a volume in spherical coordinates, the small volume element $dV$ is not simply $d\rho\, d\phi\, d\theta$. Because of the geometry of spherical coordinates, the volume element is:


$$
dV = \rho^2 \sin \phi \, d\rho \, d\phi \, d\theta
$$


- $\rho^2$ comes from the radial distance squared (volume grows with the square of the radius).
- $\sin \phi$ accounts for the shrinking of the "rings" as you move from the equator ($\phi = \pi/2$) towards the poles ($\phi = 0$ or $\pi$).

#### 3.2 Definition of Triple Integral in Spherical Coordinates

The triple integral of a function $f(x,y,z)$ over a region $G$ can be expressed in spherical coordinates as:


$$
\iiint_G f(x,y,z) \, dV = \iiint_G f(\rho \sin \phi \cos \theta, \rho \sin \phi \sin \theta, \rho \cos \phi) \, \rho^2 \sin \phi \, d\rho \, d\phi \, d\theta
$$


This means you substitute the rectangular coordinates with their spherical equivalents and multiply the integrand by the volume element $\rho^2 \sin \phi$.

#### 3.3 Theorems for Triple Integrals in Spherical Coordinates

- **Theorem 4.2.1:** The triple integral can be evaluated as an iterated integral with respect to $\rho$, $\phi$, and $\theta$, using the volume element $\rho^2 \sin \phi$.
  
- **Theorem 4.2.3:** Any triple integral in rectangular coordinates can be converted into spherical coordinates by substituting the coordinate transformations and including the Jacobian factor $\rho^2 \sin \phi$.

#### 3.4 Example Applications

- **Volume of a sphere:** Using spherical coordinates, the volume of a sphere of radius $R$ can be found by integrating the volume element over the appropriate limits:
  

$$
  0 \leq \rho \leq R, \quad 0 \leq \phi \leq \pi, \quad 0 \leq \theta \leq 2\pi
$$


- **Converting integrals:** Given an integral in rectangular coordinates, you can rewrite it in spherical coordinates to simplify the evaluation, especially when the region is spherical or radially symmetric.


### 4. 🔄 Change of Variables in Multiple Integrals: The Role of Jacobians

When changing variables in integrals, especially from one coordinate system to another, it is crucial to understand how the area or volume elements transform. This is where the **Jacobian** comes in.

#### 4.1 Change of Variables in Single Integrals (Review)

For a single integral, if you substitute $x = g(u)$, where $g$ is differentiable and one-to-one, the integral changes as:


$$
\int_a^b f(x) \, dx = \int_{u_1}^{u_2} f(g(u)) \left| \frac{dx}{du} \right| du
$$


The derivative $\frac{dx}{du}$ accounts for how the length element changes under the transformation.

#### 4.2 Transformations in the Plane

A transformation $T$ maps points $(u,v)$ in the $uv$-plane to points $(x,y)$ in the $xy$-plane via:


$$
x = x(u,v), \quad y = y(u,v)
$$


- The **image** of a set $S$ in the $uv$-plane under $T$ is the set of all points $(x,y)$ obtained by applying $T$ to every point in $S$.
- If $T$ is one-to-one, each point in the $uv$-plane corresponds to a unique point in the $xy$-plane.
- The images of vertical and horizontal lines in the $uv$-plane become curves in the $xy$-plane called constant $u$-curves and constant $v$-curves, respectively.

#### 4.3 Jacobians in Two Variables

The **Jacobian determinant** measures how area scales under the transformation $T$. It is defined as:


$$
J(u,v) = \frac{\partial(x,y)}{\partial(u,v)} = 
\begin{vmatrix}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v}
\end{vmatrix}
= \frac{\partial x}{\partial u} \frac{\partial y}{\partial v} - \frac{\partial x}{\partial v} \frac{\partial y}{\partial u}
$$


This determinant tells us how a small area element $du\, dv$ in the $uv$-plane is stretched or compressed when mapped to the $xy$-plane.

#### 4.4 Change of Variable Formula for Double Integrals

If $T$ maps region $S$ in the $uv$-plane to region $R$ in the $xy$-plane, and the Jacobian $J(u,v)$ is non-zero and does not change sign on $S$, then:


$$
\iint_R f(x,y) \, dx\, dy = \iint_S f(x(u,v), y(u,v)) \, |J(u,v)| \, du\, dv
$$


This formula allows us to evaluate double integrals by changing variables, which can simplify the region or the integrand.

#### 4.5 Jacobians in Three Variables

Extending the idea to three dimensions, a transformation $T$ from $(u,v,w)$ to $(x,y,z)$ is given by:


$$
x = x(u,v,w), \quad y = y(u,v,w), \quad z = z(u,v,w)
$$


The Jacobian determinant in three variables is:


$$
J(u,v,w) = \frac{\partial(x,y,z)}{\partial(u,v,w)} = 
\begin{vmatrix}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} & \frac{\partial x}{\partial w} \\
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} & \frac{\partial y}{\partial w} \\
\frac{\partial z}{\partial u} & \frac{\partial z}{\partial v} & \frac{\partial z}{\partial w}
\end{vmatrix}
$$


This determinant measures how volume elements transform under $T$.

#### 4.6 Change of Variable Formula for Triple Integrals

If $T$ maps region $S$ in the $uvw$-space to region $R$ in the $xyz$-space, and the Jacobian $J(u,v,w)$ is non-zero and does not change sign on $S$, then:


$$
\iiint_R f(x,y,z) \, dx\, dy\, dz = \iiint_S f(x(u,v,w), y(u,v,w), z(u,v,w)) \, |J(u,v,w)| \, du\, dv\, dw
$$


This formula is fundamental for evaluating triple integrals in different coordinate systems, such as spherical or cylindrical coordinates, by expressing the integral in terms of new variables and including the Jacobian factor.


### 5. 📝 Summary and Key Takeaways

- **Spherical coordinates** are ideal for problems with spherical symmetry. The coordinates $(\rho, \phi, \theta)$ relate to $(x,y,z)$ via specific trigonometric formulas.
- The **volume element** in spherical coordinates is $\rho^2 \sin \phi \, d\rho \, d\phi \, d\theta$, which must be included when setting up triple integrals.
- **Triple integrals** can be converted from rectangular to spherical coordinates by substituting the coordinate transformations and multiplying by the volume element.
- The **Jacobian determinant** is a crucial tool for changing variables in integrals. It measures how area or volume elements scale under transformations.
- For **double integrals**, the Jacobian is a 2x2 determinant; for **triple integrals**, it is a 3x3 determinant.
- The **change of variable formulas** allow us to rewrite integrals in new variables, often simplifying the integration process.


This detailed understanding of triple integrals in spherical coordinates and the use of Jacobians for variable transformations is essential for solving complex integration problems efficiently and accurately, especially in physics, engineering, and higher mathematics.