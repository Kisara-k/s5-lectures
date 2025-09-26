## 2. Arc Length, Space Curves and Curvature

## Key Points

#### 1. 📏 Arc Length
- The arc length $s(\mathbf{r})$ of a curve $\mathbf{r}(t)$ over $[a,b]$ is defined as the supremum of sums of lengths of polygonal approximations:  

$$
  s(\mathbf{r}) = \sup \{ \sum_{k=1}^n \|\mathbf{r}(t_k) - \mathbf{r}(t_{k-1})\| P = \{t_0, ..., t_n\} \}
$$

- A curve $\mathbf{r}$ is **rectifiable** if $s(\mathbf{r}) \in \mathbb{R}$ (finite).
- If $\mathbf{r} \in C^1$, then $\mathbf{r}$ is rectifiable and  

$$
  s(\mathbf{r}) = \int_a^b \|\mathbf{r}'(t)\| \, dt
$$

- The Mean Value Theorem does **not** hold for vector-valued functions, but in $\mathbb{R}^2$, there exists $c \in (a,b)$ such that $\mathbf{r}'(c)$ is parallel to $\mathbf{r}(b) - \mathbf{r}(a)$.
- A **change of parameter** $t = g(\tau)$ reparametrizes the curve without changing its trace.
- Chain rule for vector functions under parameter change:  

$$
  \frac{d}{d\tau} \mathbf{r}(g(\tau)) = \mathbf{r}'(g(\tau)) \cdot g'(\tau)
$$

- The **arc length parameter** $s$ from reference point $t_0$ is:  

$$
  s = \int_{t_0}^t \|\mathbf{r}'(u)\| \, du
$$

- When parameterized by arc length $s$, the tangent vector satisfies $\|\frac{d\mathbf{r}}{ds}\| = 1$.


#### 2. 🧭 Unit Tangent, Normal, and Binormal Vectors
- The **unit tangent vector** is:  

$$
  \mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}
$$

- The **principal unit normal vector** is:  

$$
  \mathbf{N}(t) = \frac{\mathbf{T}'(t)}{\|\mathbf{T}'(t)\|}
$$

- $\mathbf{T}(t)$ points in the direction of motion; $\mathbf{N}(t)$ points toward the direction the curve is turning (concave side).
- The **binormal vector** is:  

$$
  \mathbf{B}(t) = \mathbf{T}(t) \times \mathbf{N}(t)
$$

- The vectors $\mathbf{T}(t), \mathbf{N}(t), \mathbf{B}(t)$ form a right-handed orthonormal basis called the **TNB frame**.
- The TNB frame defines three mutually perpendicular planes at each point on the curve:  
  - Rectifying plane (TB-plane)  
  - Osculating plane (TN-plane)  
  - Normal plane (NB-plane)


#### 3. 🔄 Curvature
- The **curvature** $\kappa(s)$ of a curve parameterized by arc length $s$ is:  

$$
  \kappa(s) = \left\| \frac{d\mathbf{T}}{ds} \right\| = \|\mathbf{r}''(s)\|
$$

- For a general parameter $t$, curvature is:  

$$
  \kappa(t) = \frac{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|}{\|\mathbf{r}'(t)\|^3}
$$

- The **radius of curvature** $\rho$ at a point is the reciprocal of curvature:  

$$
  \rho = \frac{1}{\kappa}
$$

- The **osculating circle** at a point on the curve is the circle with radius $\rho$ that best approximates the curve near that point, sharing the same tangent and curvature.
- The center of the osculating circle lies on the concave side of the curve and is called the **center of curvature**.



<br>

## Study Notes

### 1. 📏 Arc Length: Measuring the Length of Curves in Space

When we talk about curves in three-dimensional space (ℝ³), one fundamental question is: **How do we measure the length of a curve?** Unlike straight lines, curves can bend and twist, so their length isn't just the distance between two points. The concept of **arc length** helps us find the exact length of a curve between two points.

#### What is Arc Length?

Imagine a curve defined by a vector-valued function $\mathbf{r}(t)$, where $t$ varies over an interval $[a, b]$. To find the length of this curve, we start by dividing the interval $[a, b]$ into smaller subintervals using a partition $P = \{t_0, t_1, ..., t_n\}$ where $a = t_0 < t_1 < ... < t_n = b$.

For each subinterval, we approximate the curve by straight line segments connecting the points $\mathbf{r}(t_k)$ and $\mathbf{r}(t_{k-1})$. The sum of the lengths of these line segments is:


$$
s(\mathbf{r}, P) = \sum_{k=1}^n \|\mathbf{r}(t_k) - \mathbf{r}(t_{k-1})\|
$$


The **arc length** $s(\mathbf{r})$ is then defined as the supremum (the least upper bound) of these sums over all possible partitions $P$:


$$
s(\mathbf{r}) = \sup \{ s(\mathbf{r}, P) \mid P \in \mathcal{P}[a,b] \}
$$


If this supremum is a finite real number, the curve is called **rectifiable**.

#### Important Theorem: Arc Length for Smooth Curves

If $\mathbf{r}(t)$ is continuously differentiable (denoted $\mathbf{r} \in C^1$), then the curve is rectifiable, and the arc length can be computed exactly by the integral:


$$
s(\mathbf{r}) = \int_a^b \|\mathbf{r}'(t)\| \, dt
$$


Here, $\mathbf{r}'(t)$ is the derivative of $\mathbf{r}(t)$, and $\|\mathbf{r}'(t)\|$ is the speed or magnitude of the velocity vector at time $t$.

#### Note on Mean Value Theorem (MVT)

Unlike real-valued functions, the Mean Value Theorem does not directly apply to vector-valued functions. However, in two dimensions ($\mathbb{R}^2$), there exists some $c \in (a,b)$ such that the derivative $\mathbf{r}'(c)$ is parallel to the vector $\mathbf{r}(b) - \mathbf{r}(a)$.

#### Change of Parameter

Sometimes, we want to reparametrize the curve, meaning we change the parameter $t$ to a new parameter $\tau$ via a differentiable function $t = g(\tau)$. This produces a new vector-valued function $\mathbf{r}(g(\tau))$ that traces the same curve but possibly at a different speed or direction.

The **chain rule** applies here: if $\mathbf{r}(t)$ is differentiable and $g(\tau)$ is differentiable, then $\mathbf{r}(g(\tau))$ is differentiable with respect to $\tau$, and its derivative is:


$$
\frac{d}{d\tau} \mathbf{r}(g(\tau)) = \mathbf{r}'(g(\tau)) \cdot g'(\tau)
$$


#### Arc Length Parameter

A special and very useful parameterization is the **arc length parameter** $s$, which measures the length along the curve from a fixed reference point $\mathbf{r}(t_0)$. It is defined as:


$$
s = \int_{t_0}^t \|\mathbf{r}'(u)\| \, du
$$


This parameter $s$ increases exactly by the length traveled along the curve, making it a natural way to describe motion along the curve.


### 2. 🧭 Unit Tangent, Normal, and Binormal Vectors: Understanding Direction and Orientation of Curves

When studying curves in space, it's important to understand not just where the curve is, but how it moves and bends. This is where the **TNB frame** (Tangent, Normal, Binormal vectors) comes in. These vectors give us a moving coordinate system along the curve that describes its direction and how it twists.

#### Unit Tangent Vector ($\mathbf{T}(t)$)

The **unit tangent vector** points in the direction the curve is moving at each point. Formally, if $\mathbf{r}(t)$ is differentiable and $\mathbf{r}'(t) \neq 0$, then:


$$
\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}
$$


This vector has length 1 and points in the direction of increasing $t$. It tells us the instantaneous direction of the curve.

#### Principal Unit Normal Vector ($\mathbf{N}(t)$)

The curve may be turning or curving, and the direction in which it turns is given by the **principal unit normal vector**. This vector is defined as the unit vector in the direction of the derivative of the tangent vector:


$$
\mathbf{N}(t) = \frac{\mathbf{T}'(t)}{\|\mathbf{T}'(t)\|}
$$


Intuitively, $\mathbf{N}(t)$ points towards the center of the curve's "bend" or concavity. On a plane curve, it points toward the concave side of the curve, indicating the direction the curve is turning.

#### Binormal Vector ($\mathbf{B}(t)$)

In three dimensions, the curve can twist out of the plane, so we need a third vector to complete the frame. The **binormal vector** is defined as the cross product of the tangent and normal vectors:


$$
\mathbf{B}(t) = \mathbf{T}(t) \times \mathbf{N}(t)
$$


This vector is perpendicular to both $\mathbf{T}(t)$ and $\mathbf{N}(t)$, and together, $\{\mathbf{T}(t), \mathbf{N}(t), \mathbf{B}(t)\}$ form a right-handed orthonormal basis called the **TNB frame**.

#### Geometric Interpretation of the TNB Frame

- The **Tangent vector** points along the direction of motion.
- The **Normal vector** points towards the direction the curve is turning.
- The **Binormal vector** points perpendicular to the plane formed by $\mathbf{T}$ and $\mathbf{N}$, indicating the twisting of the curve in space.

At each point on the curve, these vectors define three mutually perpendicular planes:

- **Rectifying plane (TB-plane):** spanned by $\mathbf{T}$ and $\mathbf{B}$.
- **Osculating plane (TN-plane):** spanned by $\mathbf{T}$ and $\mathbf{N}$, the plane that best approximates the curve at that point.
- **Normal plane (NB-plane):** spanned by $\mathbf{N}$ and $\mathbf{B}$.


### 3. 🔄 Curvature: How Much Does a Curve Bend?

Curvature is a measure of how sharply a curve bends at a given point. It quantifies the rate of change of the direction of the tangent vector as you move along the curve.

#### Definition of Curvature

If the curve is parameterized by arc length $s$, the curvature $\kappa(s)$ at a point is defined as the magnitude of the derivative of the unit tangent vector with respect to $s$:


$$
\kappa(s) = \left\| \frac{d\mathbf{T}}{ds} \right\| = \|\mathbf{r}''(s)\|
$$


Here, $\mathbf{r}''(s)$ is the second derivative of the position vector with respect to arc length, which measures how quickly the curve is changing direction.

#### Curvature in Terms of a General Parameter $t$

If the curve is parameterized by a general parameter $t$, the curvature can be expressed as:


$$
\kappa(t) = \frac{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|}{\|\mathbf{r}'(t)\|^3}
$$


This formula uses the cross product of the first and second derivatives of $\mathbf{r}(t)$ and normalizes by the cube of the speed $\|\mathbf{r}'(t)\|$.

#### Example: Curvature of a Helix

Consider the curve:


$$
\mathbf{r}(t) = (a \cos t, a \sin t, b t)
$$


where $a, b \geq 0$. This is a helix winding around the $z$-axis.

- The curvature $\kappa$ depends on $a$ and $b$.
- Using the formula above, you can compute $\kappa$ explicitly in terms of $a$ and $b$.

#### Radius of Curvature and Osculating Circle

The **radius of curvature** $\rho$ at a point on the curve is the reciprocal of the curvature:


$$
\rho = \frac{1}{\kappa}
$$


Geometrically, the radius of curvature is the radius of the **osculating circle** at that point — the circle that best approximates the curve near that point and shares the same tangent and curvature.

- The osculating circle lies on the concave side of the curve.
- Its center is called the **center of curvature**.

This concept is very useful in physics and engineering, for example, when analyzing the motion of particles along curved paths or designing roads and tracks.


### Summary

- **Arc length** measures the length of a curve by summing infinitesimal distances along it, and for smooth curves, it can be computed by integrating the speed $\|\mathbf{r}'(t)\|$.
- The **TNB frame** (Tangent, Normal, Binormal vectors) provides a moving coordinate system along the curve that describes its direction, bending, and twisting.
- **Curvature** quantifies how sharply a curve bends, and the **radius of curvature** relates to the osculating circle that best fits the curve at a point.

Understanding these concepts is crucial for analyzing curves in space, whether in pure mathematics, physics, or engineering applications.
