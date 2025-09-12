## 1. Vector-Valued Functions

## Key Points

#### 1. 📐 Vector-Valued Functions - Definition & Parametric Form
- A vector-valued function $\mathbf{r}(t) = (x(t), y(t), z(t)) = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k}$ maps a real parameter $t$ to a vector in 2D or 3D space.
- Parametric equations express curves by defining each coordinate as a function of a parameter $t$.
- Examples: Circle $x = r \cos t, y = r \sin t$; Circular helix $x = a \cos t, y = a \sin t, z = c t$.

#### 2. 🔍 Limits of Vector-Valued Functions
- $\lim_{t \to a} \mathbf{r}(t) = \mathbf{L}$ exists if and only if $\lim_{t \to a} x(t) = L_1$, $\lim_{t \to a} y(t) = L_2$, and $\lim_{t \to a} z(t) = L_3$.
- Limit laws for vector functions apply component-wise and include sum, difference, scalar multiplication, dot product, and cross product.

#### 3. ✅ Continuity of Vector-Valued Functions
- $\mathbf{r}$ is continuous at $t = a$ if $\lim_{t \to a} \mathbf{r}(t) = \mathbf{r}(a)$.
- Continuity of $\mathbf{r}$ is equivalent to continuity of each component function at $a$.

#### 4. ✏️ Differentiation of Vector-Valued Functions
- $\mathbf{r}'(t) = (x'(t), y'(t), z'(t))$ exists if and only if each component is differentiable at $t$.
- Differentiation rules:
  - $(\mathbf{r}_1 + \mathbf{r}_2)' = \mathbf{r}_1' + \mathbf{r}_2'$
  - $(k \mathbf{r})' = k \mathbf{r}'$ for scalar $k$
  - $(f(t) \mathbf{r}(t))' = f'(t) \mathbf{r}(t) + f(t) \mathbf{r}'(t)$
  - $(\mathbf{F} \cdot \mathbf{G})' = \mathbf{F}' \cdot \mathbf{G} + \mathbf{F} \cdot \mathbf{G}'$
  - $(\mathbf{F} \times \mathbf{G})' = \mathbf{F}' \times \mathbf{G} + \mathbf{F} \times \mathbf{G}'$

#### 5. 📏 Tangent Vectors and Lines
- If $\mathbf{r}'(t_0)$ exists and $\mathbf{r}'(t_0) \neq \mathbf{0}$, then $\mathbf{r}'(t_0)$ is the tangent vector at $\mathbf{r}(t_0)$.
- The tangent line at $t_0$ is given by $\mathbf{L}(s) = \mathbf{r}(t_0) + s \mathbf{r}'(t_0)$.

#### 6. 🔺 Angle Between Tangent Lines
- The acute angle $\theta$ between tangent lines of $\mathbf{r}_1$ and $\mathbf{r}_2$ at a point is given by:

$$
\cos \theta = \frac{\mathbf{r}_1'(t_0) \cdot \mathbf{r}_2'(t_0)}{\|\mathbf{r}_1'(t_0)\| \|\mathbf{r}_2'(t_0)\|}
$$


#### 7. ⊥ Orthogonality Condition
- If $\|\mathbf{r}(t)\|$ is constant for all $t$, then $\mathbf{r}(t)$ and $\mathbf{r}'(t)$ are orthogonal vectors for all $t$.

#### 8. ∫ Integration of Vector-Valued Functions
- The definite integral of $\mathbf{r}(t) = (x(t), y(t), z(t))$ over $[a,b]$ is:

$$
\int_a^b \mathbf{r}(t) dt = \left( \int_a^b x(t) dt, \int_a^b y(t) dt, \int_a^b z(t) dt \right)
$$

- Integration rules for sums and scalar multiples apply component-wise.



<br>

## Study Notes

### 1. 📐 Introduction to Vector-Valued Functions

When we study functions in calculus, we often think of functions that take a real number and output another real number, like $f(t) = t^2$. However, many real-world problems involve quantities that have multiple components, such as position in space, velocity, or force, which are naturally represented as vectors. This is where **vector-valued functions** come in.

A **vector-valued function** is a function where the input is a real number (often called a parameter $t$) and the output is a vector, typically in 2D or 3D space. Instead of just one output value, you get multiple outputs bundled together as a vector.

#### Parametric Equations and Vector-Valued Functions

A **parametric equation** expresses a set of quantities as functions of one or more independent variables called parameters. For example, instead of writing $y = x^2$, you can write both $x$ and $y$ as functions of a parameter $t$:

- $x = t$
- $y = t^2$

This is a simple parametric form of the parabola $y = x^2$.

More complex shapes can also be described parametrically:

- **Circle of radius $r$**: $x = r \cos t$, $y = r \sin t$
- **Circular helix in 3D**: $x = a \cos t$, $y = a \sin t$, $z = c t$
- **Tricuspoid curve**: $x = 2 \cos t + \cos 2t$, $y = 2 \sin t - \sin 2t$

#### Formal Definition

If we have three real-valued functions $x(t), y(t), z(t)$, then the vector-valued function


$$
\mathbf{r}(t) = x(t) \mathbf{i} + y(t) \mathbf{j} + z(t) \mathbf{k}
$$


assigns a vector in 3D space to each value of $t$. Here, $\mathbf{i}, \mathbf{j}, \mathbf{k}$ are the standard unit vectors along the x, y, and z axes respectively.

**Example:** The circular helix can be written as


$$
\mathbf{r}(t) = (a \cos t, a \sin t, c t)
$$


where $t \geq 0$.

#### Domain of Vector-Valued Functions

Just like regular functions, vector-valued functions have domains — the set of all $t$ values for which the function is defined. For example,


$$
\mathbf{r}(t) = (\ln|t-1|, e^t, \sqrt{t})
$$


is defined only where each component is defined:

- $\ln|t-1|$ requires $t \neq 1$
- $e^t$ is defined for all real $t$
- $\sqrt{t}$ requires $t \geq 0$

So the natural domain is $t \geq 0$ and $t \neq 1$.


### 2. 🔍 Limits and Continuity of Vector-Valued Functions

Understanding limits and continuity is fundamental in calculus, and vector-valued functions follow similar principles as real-valued functions, but with some nuances.

#### Limits of Vector-Valued Functions

The limit of a vector-valued function $\mathbf{r}(t)$ as $t \to a$ is a vector $\mathbf{L}$ if the output vectors get arbitrarily close to $\mathbf{L}$ as $t$ approaches $a$.

Formally, for every small distance $\epsilon > 0$, there exists a small interval $\delta > 0$ such that whenever $|t - a| < \delta$, the distance between $\mathbf{r}(t)$ and $\mathbf{L}$ is less than $\epsilon$.

#### Component-wise Limit Evaluation

A key theorem states that the limit of a vector-valued function exists if and only if the limits of each of its component functions exist. That is,


$$
\lim_{t \to a} \mathbf{r}(t) = \mathbf{L} = (L_1, L_2, L_3)
$$


if and only if


$$
\lim_{t \to a} x(t) = L_1, \quad \lim_{t \to a} y(t) = L_2, \quad \lim_{t \to a} z(t) = L_3
$$


This means you can analyze each component separately using the usual limit rules from single-variable calculus.

#### Limit Laws for Vector-Valued Functions

The familiar limit laws for sums, differences, scalar multiples, dot products, and cross products also hold for vector-valued functions. For example:

- The limit of a sum is the sum of the limits.
- The limit of a scalar times a vector is the scalar limit times the vector limit.
- The limit of the dot product is the dot product of the limits.
- The limit of the cross product is the cross product of the limits.

These properties allow us to manipulate limits of vector functions just like we do with real-valued functions.

#### Continuity

A vector-valued function $\mathbf{r}$ is **continuous** at $t = a$ if


$$
\lim_{t \to a} \mathbf{r}(t) = \mathbf{r}(a)
$$


This means the function’s value at $a$ matches the limit as $t$ approaches $a$. Continuity of $\mathbf{r}$ is equivalent to continuity of each component function at $a$.


### 3. ✏️ Differentiation of Vector-Valued Functions

Just like real-valued functions, vector-valued functions can be differentiated. The derivative of a vector-valued function gives the rate of change of the vector output with respect to the parameter $t$.

#### Definition of the Derivative

The derivative of $\mathbf{r}(t)$ is defined as


$$
\mathbf{r}'(t) = \lim_{h \to 0} \frac{\mathbf{r}(t+h) - \mathbf{r}(t)}{h}
$$


provided this limit exists.

#### Component-wise Differentiation

A crucial theorem states that $\mathbf{r}$ is differentiable at $t$ if and only if each component function $x(t), y(t), z(t)$ is differentiable at $t$. Moreover,


$$
\mathbf{r}'(t) = (x'(t), y'(t), z'(t))
$$


This means you can differentiate each component separately using standard differentiation rules.

#### Rules of Differentiation

The differentiation rules for vector-valued functions mirror those for real-valued functions:

- **Sum rule:** $(\mathbf{r}_1 + \mathbf{r}_2)' = \mathbf{r}_1' + \mathbf{r}_2'$
- **Scalar multiple:** $(k \mathbf{r})' = k \mathbf{r}'$ where $k$ is a constant
- **Product with scalar function:** $(f(t) \mathbf{r}(t))' = f'(t) \mathbf{r}(t) + f(t) \mathbf{r}'(t)$
- **Dot product:** $(\mathbf{F} \cdot \mathbf{G})' = \mathbf{F}' \cdot \mathbf{G} + \mathbf{F} \cdot \mathbf{G}'$
- **Cross product:** $(\mathbf{F} \times \mathbf{G})' = \mathbf{F}' \times \mathbf{G} + \mathbf{F} \times \mathbf{G}'$

These rules allow us to differentiate complex vector expressions systematically.

#### Tangent Vectors and Tangent Lines

If $\mathbf{r}'(t_0)$ exists and is not the zero vector, it is called the **tangent vector** to the curve at the point $\mathbf{r}(t_0)$. The line passing through $\mathbf{r}(t_0)$ in the direction of $\mathbf{r}'(t_0)$ is called the **tangent line**.

- The equation of the tangent line at $t = t_0$ is


$$
\mathbf{L}(s) = \mathbf{r}(t_0) + s \mathbf{r}'(t_0)
$$


where $s$ is a real parameter.

#### Angle Between Tangent Lines

If two vector-valued functions $\mathbf{r}_1(t)$ and $\mathbf{r}_2(t)$ intersect at a point, the angle $\theta$ between their tangent lines at that point can be found using the dot product of their tangent vectors:


$$
\cos \theta = \frac{\mathbf{r}_1'(t_0) \cdot \mathbf{r}_2'(t_0)}{\|\mathbf{r}_1'(t_0)\| \|\mathbf{r}_2'(t_0)\|}
$$


The angle $\theta$ is then $\arccos$ of this value.

#### Orthogonality of $\mathbf{r}(t)$ and $\mathbf{r}'(t)$

If the magnitude $\|\mathbf{r}(t)\|$ is constant for all $t$, then the vector $\mathbf{r}(t)$ is always perpendicular (orthogonal) to its derivative $\mathbf{r}'(t)$. This is a useful property when dealing with motion constrained to a sphere or circle.


### 4. ∫ Integration of Vector-Valued Functions

Integration of vector-valued functions is done component-wise, just like differentiation.

#### Definite Integral

If $\mathbf{r}(t) = (x(t), y(t), z(t))$ is continuous on the interval $[a, b]$, then the definite integral of $\mathbf{r}$ over $[a, b]$ is defined as


$$
\int_a^b \mathbf{r}(t) \, dt = \left( \int_a^b x(t) \, dt, \int_a^b y(t) \, dt, \int_a^b z(t) \, dt \right)
$$


This means you integrate each component function separately.

#### Properties of Integration

The integral of sums, scalar multiples, and other linear combinations of vector-valued functions behaves as expected:

- $\int_a^b [\mathbf{r}_1(t) + \mathbf{r}_2(t)] dt = \int_a^b \mathbf{r}_1(t) dt + \int_a^b \mathbf{r}_2(t) dt$
- $\int_a^b k \mathbf{r}(t) dt = k \int_a^b \mathbf{r}(t) dt$, where $k$ is a scalar


### 5. 📝 Summary and Key Takeaways

- **Vector-valued functions** map real numbers to vectors, often representing curves or paths in space.
- Parametric equations are a natural way to describe curves using vector-valued functions.
- Limits, continuity, differentiation, and integration of vector-valued functions can be handled component-wise.
- The derivative of a vector-valued function gives the tangent vector to the curve.
- Tangent lines and angles between curves can be found using derivatives and dot products.
- If the magnitude of a vector-valued function is constant, the function and its derivative are orthogonal.
- Integration of vector-valued functions is done by integrating each component separately.


This detailed understanding of vector-valued functions is essential for many applications in physics, engineering, and computer graphics, and is a fundamental topic in multivariable calculus.