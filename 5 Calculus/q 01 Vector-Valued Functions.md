## 1. Vector-Valued Functions

## Questions

#### 1. Which of the following statements about vector-valued functions $\mathbf{r}(t) = (x(t), y(t), z(t))$ is true?  
A) The domain of $\mathbf{r}$ is the intersection of the domains of $x(t), y(t), z(t)$.  
B) The range of $\mathbf{r}$ is always a subset of $\mathbb{R}^3$.  
C) $\mathbf{r}(t)$ can only represent curves in 3D space.  
D) The components $x(t), y(t), z(t)$ must be differentiable for $\mathbf{r}(t)$ to be differentiable.


#### 2. Given $\mathbf{r}(t) = (\ln|t-1|, e^t, \sqrt{t})$, what is the natural domain of $\mathbf{r}$?  
A) $t > 1$  
B) $t \geq 0, t \neq 1$  
C) $t > 0$  
D) All real $t$ except $t=1$


#### 3. The limit $\lim_{t \to a} \mathbf{r}(t) = \mathbf{L}$ exists if and only if:  
A) Each component function $x(t), y(t), z(t)$ has a limit at $t = a$.  
B) The magnitude $\|\mathbf{r}(t)\|$ approaches $\|\mathbf{L}\|$ as $t \to a$.  
C) The limit of the dot product $\mathbf{r}(t) \cdot \mathbf{L}$ exists.  
D) The limit of the cross product $\mathbf{r}(t) \times \mathbf{L}$ exists.


#### 4. Which of the following limit properties hold for vector-valued functions $\mathbf{F}(t)$ and $\mathbf{G}(t)$ with limits at $t \to a$?  
A) $\lim_{t \to a} [\mathbf{F}(t) + \mathbf{G}(t)] = \lim_{t \to a} \mathbf{F}(t) + \lim_{t \to a} \mathbf{G}(t)$  
B) $\lim_{t \to a} [\mathbf{F}(t) \cdot \mathbf{G}(t)] = \lim_{t \to a} \mathbf{F}(t) \cdot \lim_{t \to a} \mathbf{G}(t)$  
C) $\lim_{t \to a} [\mathbf{F}(t) \times \mathbf{G}(t)] = \lim_{t \to a} \mathbf{F}(t) \times \lim_{t \to a} \mathbf{G}(t)$  
D) $\lim_{t \to a} [\mathbf{F}(t) / \mathbf{G}(t)] = \lim_{t \to a} \mathbf{F}(t) / \lim_{t \to a} \mathbf{G}(t)$


#### 5. A vector-valued function $\mathbf{r}(t)$ is continuous at $t = a$ if:  
A) $\mathbf{r}(a)$ is defined and $\lim_{t \to a} \mathbf{r}(t) = \mathbf{r}(a)$.  
B) Each component function is continuous at $t = a$.  
C) The magnitude $\|\mathbf{r}(t)\|$ is continuous at $t = a$.  
D) The derivative $\mathbf{r}'(a)$ exists.


#### 6. The derivative $\mathbf{r}'(t)$ of a vector-valued function $\mathbf{r}(t) = (x(t), y(t), z(t))$ is:  
A) $\mathbf{r}'(t) = (x'(t), y'(t), z'(t))$ if all component derivatives exist.  
B) Always orthogonal to $\mathbf{r}(t)$.  
C) The vector tangent to the curve at $\mathbf{r}(t)$ if $\mathbf{r}'(t) \neq \mathbf{0}$.  
D) The vector normal to the curve at $\mathbf{r}(t)$.


#### 7. If $\|\mathbf{r}(t)\|$ is constant for all $t$, which of the following statements is true?  
A) $\mathbf{r}(t)$ and $\mathbf{r}'(t)$ are orthogonal for all $t$.  
B) $\mathbf{r}'(t) = \mathbf{0}$ for all $t$.  
C) The curve lies on a sphere centered at the origin.  
D) The derivative $\mathbf{r}'(t)$ is parallel to $\mathbf{r}(t)$.


#### 8. Consider two differentiable vector-valued functions $\mathbf{r}_1(t)$ and $\mathbf{r}_2(t)$ intersecting at $t = t_0$. The acute angle $\theta$ between their tangent lines at the intersection is given by:  
A) $\cos \theta = \frac{\mathbf{r}_1'(t_0) \cdot \mathbf{r}_2'(t_0)}{\|\mathbf{r}_1'(t_0)\| \|\mathbf{r}_2'(t_0)\|}$  
B) $\sin \theta = \frac{\|\mathbf{r}_1'(t_0) \times \mathbf{r}_2'(t_0)\|}{\|\mathbf{r}_1'(t_0)\| \|\mathbf{r}_2'(t_0)\|}$  
C) $\theta = \arccos$ of the dot product formula in (A).  
D) $\theta$ is always 90 degrees if the curves intersect.


#### 9. Which of the following are valid differentiation rules for vector-valued functions $\mathbf{r}(t)$, $\mathbf{r}_1(t)$, $\mathbf{r}_2(t)$, and scalar function $f(t)$?  
A) $\frac{d}{dt} [\mathbf{r}_1(t) + \mathbf{r}_2(t)] = \mathbf{r}_1'(t) + \mathbf{r}_2'(t)$  
B) $\frac{d}{dt} [f(t) \mathbf{r}(t)] = f'(t) \mathbf{r}(t) + f(t) \mathbf{r}'(t)$  
C) $\frac{d}{dt} [\mathbf{r}_1(t) \cdot \mathbf{r}_2(t)] = \mathbf{r}_1'(t) \cdot \mathbf{r}_2'(t)$  
D) $\frac{d}{dt} [\mathbf{r}_1(t) \times \mathbf{r}_2(t)] = \mathbf{r}_1'(t) \times \mathbf{r}_2(t) + \mathbf{r}_1(t) \times \mathbf{r}_2'(t)$


#### 10. The tangent line to the curve $\mathbf{r}(t)$ at $t = t_0$ is:  
A) The line passing through $\mathbf{r}(t_0)$ in the direction of $\mathbf{r}'(t_0)$.  
B) The line passing through the origin in the direction of $\mathbf{r}'(t_0)$.  
C) The line passing through $\mathbf{r}(t_0)$ in the direction of $\mathbf{r}(t_0)$.  
D) The line perpendicular to $\mathbf{r}'(t_0)$ at $\mathbf{r}(t_0)$.


#### 11. Which of the following statements about the definite integral of a vector-valued function $\mathbf{r}(t) = (x(t), y(t), z(t))$ over $[a,b]$ is true?  
A) $\int_a^b \mathbf{r}(t) dt = \left(\int_a^b x(t) dt, \int_a^b y(t) dt, \int_a^b z(t) dt\right)$  
B) The integral is a vector whose components are the integrals of the component functions.  
C) The integral always results in a scalar.  
D) The integral can be computed by integrating the magnitude $\|\mathbf{r}(t)\|$ over $[a,b]$.


#### 12. Suppose $\mathbf{r}(t)$ is differentiable and $\mathbf{r}'(t)$ is continuous. Which of the following is true?  
A) $\mathbf{r}$ is said to be in class $C^1$.  
B) $\mathbf{r}$ is continuous but not necessarily differentiable.  
C) $\mathbf{r}'(t)$ is integrable on any closed interval.  
D) $\mathbf{r}$ must be constant.


#### 13. If $\mathbf{r}(t) = (t^2, \sin t, e^t)$, which of the following is true about $\mathbf{r}'(t)$?  
A) $\mathbf{r}'(t) = (2t, \cos t, e^t)$  
B) $\mathbf{r}'(t)$ is always orthogonal to $\mathbf{r}(t)$.  
C) $\mathbf{r}'(t)$ gives the velocity vector if $\mathbf{r}(t)$ represents position.  
D) $\mathbf{r}'(t)$ is zero at $t=0$.


#### 14. Which of the following vector-valued functions represent a curve lying on a circle of radius $r$ in the xy-plane?  
A) $\mathbf{r}(t) = (r \cos t, r \sin t, 0)$  
B) $\mathbf{r}(t) = (r \cos t, r \sin t, t)$  
C) $\mathbf{r}(t) = (r \cos t, r \sin t, r \cos t)$  
D) $\mathbf{r}(t) = (r \cos t, r \sin t, r \sin t)$


#### 15. For the vector-valued function $\mathbf{r}(t) = (2 \cos t + \cos 2t, 2 \sin t - \sin 2t)$, which of the following is true?  
A) It represents a tricuspoid curve.  
B) It lies entirely in 3D space.  
C) Its components are periodic functions.  
D) The curve is a straight line.


#### 16. If $\mathbf{r}(t)$ is differentiable and $\mathbf{r}'(t) = \mathbf{0}$ for all $t$, then:  
A) $\mathbf{r}(t)$ is a constant vector function.  
B) $\mathbf{r}(t)$ represents a stationary point.  
C) $\mathbf{r}(t)$ must be zero vector for all $t$.  
D) $\mathbf{r}(t)$ is not continuous.


#### 17. Which of the following statements about the cross product of two vector-valued functions $\mathbf{F}(t)$ and $\mathbf{G}(t)$ is true?  
A) $\frac{d}{dt}[\mathbf{F}(t) \times \mathbf{G}(t)] = \mathbf{F}'(t) \times \mathbf{G}(t) + \mathbf{F}(t) \times \mathbf{G}'(t)$  
B) The cross product is commutative.  
C) The cross product is always orthogonal to both $\mathbf{F}(t)$ and $\mathbf{G}(t)$.  
D) The limit of the cross product is the cross product of the limits, if they exist.


#### 18. Consider $\mathbf{r}(t) = (a \cos t, a \sin t, c t)$. Which of the following statements are correct?  
A) $\mathbf{r}(t)$ represents a circular helix.  
B) The projection of $\mathbf{r}(t)$ onto the xy-plane is a circle of radius $a$.  
C) The curve lies on a sphere of radius $\sqrt{a^2 + c^2 t^2}$.  
D) The tangent vector $\mathbf{r}'(t)$ is always perpendicular to $\mathbf{r}(t)$.


#### 19. Which of the following are true about the derivative of the dot product of two vector-valued functions $\mathbf{F}(t)$ and $\mathbf{G}(t)$?  
A) $\frac{d}{dt}[\mathbf{F}(t) \cdot \mathbf{G}(t)] = \mathbf{F}'(t) \cdot \mathbf{G}(t) + \mathbf{F}(t) \cdot \mathbf{G}'(t)$  
B) It equals the dot product of the derivatives $\mathbf{F}'(t) \cdot \mathbf{G}'(t)$.  
C) It is a scalar function.  
D) It is a vector function.


#### 20. If $\mathbf{r}(t)$ is continuous on $[a,b]$, which of the following statements about $\int_a^b \mathbf{r}(t) dt$ is true?  
A) The integral is a vector whose components are the integrals of the component functions.  
B) The integral depends on the path traced by $\mathbf{r}(t)$.  
C) The integral can be used to find the displacement vector if $\mathbf{r}(t)$ represents velocity.  
D) The integral is always zero if $\mathbf{r}(t)$ is continuous.



<br>

## Answers

#### 1. Which of the following statements about vector-valued functions $\mathbf{r}(t) = (x(t), y(t), z(t))$ is true?  
A) ✓ The domain of $\mathbf{r}$ is the intersection of the domains of $x(t), y(t), z(t)$.  
B) ✓ The range of $\mathbf{r}$ is always a subset of $\mathbb{R}^3$.  
C) ✗ $\mathbf{r}(t)$ can represent curves in 2D or 3D, not only 3D.  
D) ✓ The components must be differentiable for $\mathbf{r}(t)$ to be differentiable.

**Correct:** A, B, D


#### 2. Given $\mathbf{r}(t) = (\ln|t-1|, e^t, \sqrt{t})$, what is the natural domain of $\mathbf{r}$?  
A) ✗ $t > 1$ excludes valid values less than 1 where $\ln|t-1|$ is defined.  
B) ✓ $t \geq 0, t \neq 1$ satisfies domain restrictions of all components.  
C) ✗ $t > 0$ excludes negative values allowed by $\ln|t-1|$.  
D) ✗ Does not exclude $t < 0$ where $\sqrt{t}$ is undefined.

**Correct:** B


#### 3. The limit $\lim_{t \to a} \mathbf{r}(t) = \mathbf{L}$ exists if and only if:  
A) ✓ Each component must have a limit at $t = a$.  
B) ✗ Magnitude approaching $\|\mathbf{L}\|$ is necessary but not sufficient.  
C) ✗ Dot product limit alone does not guarantee vector limit.  
D) ✗ Cross product limit alone does not guarantee vector limit.

**Correct:** A


#### 4. Which of the following limit properties hold for vector-valued functions $\mathbf{F}(t)$ and $\mathbf{G}(t)$ with limits at $t \to a$?  
A) ✓ Sum of limits equals limit of sums.  
B) ✓ Limit of dot product equals dot product of limits.  
C) ✓ Limit of cross product equals cross product of limits.  
D) ✗ Division of vectors is undefined.

**Correct:** A, B, C


#### 5. A vector-valued function $\mathbf{r}(t)$ is continuous at $t = a$ if:  
A) ✓ Definition of continuity for vector functions.  
B) ✓ Continuity of each component implies continuity of $\mathbf{r}$.  
C) ✗ Magnitude continuity alone does not guarantee vector continuity.  
D) ✗ Derivative existence is not required for continuity.

**Correct:** A, B


#### 6. The derivative $\mathbf{r}'(t)$ of a vector-valued function $\mathbf{r}(t) = (x(t), y(t), z(t))$ is:  
A) ✓ Component-wise derivative definition.  
B) ✗ Not always orthogonal; only if $\|\mathbf{r}(t)\|$ is constant.  
C) ✓ Tangent vector if nonzero.  
D) ✗ Tangent vector is not normal to the curve.

**Correct:** A, C


#### 7. If $\|\mathbf{r}(t)\|$ is constant for all $t$, which of the following statements is true?  
A) ✓ $\mathbf{r}(t)$ and $\mathbf{r}'(t)$ are orthogonal.  
B) ✗ Derivative need not be zero; vector can move on sphere.  
C) ✓ Curve lies on a sphere centered at origin.  
D) ✗ Derivative is orthogonal, not parallel.

**Correct:** A, C


#### 8. Consider two differentiable vector-valued functions $\mathbf{r}_1(t)$ and $\mathbf{r}_2(t)$ intersecting at $t = t_0$. The acute angle $\theta$ between their tangent lines at the intersection is given by:  
A) ✓ Correct formula for cosine of angle between tangent vectors.  
B) ✓ Correct formula for sine of angle using cross product magnitude.  
C) ✓ $\theta$ is arccos of cosine formula.  
D) ✗ Angle is not always 90° at intersection.

**Correct:** A, B, C


#### 9. Which of the following are valid differentiation rules for vector-valued functions $\mathbf{r}(t)$, $\mathbf{r}_1(t)$, $\mathbf{r}_2(t)$, and scalar function $f(t)$?  
A) ✓ Sum rule for derivatives.  
B) ✓ Product rule for scalar times vector.  
C) ✗ Incorrect; derivative of dot product is sum of products, not product of derivatives.  
D) ✓ Product rule for cross product.

**Correct:** A, B, D


#### 10. The tangent line to the curve $\mathbf{r}(t)$ at $t = t_0$ is:  
A) ✓ Passes through $\mathbf{r}(t_0)$ in direction $\mathbf{r}'(t_0)$.  
B) ✗ Does not necessarily pass through origin.  
C) ✗ Direction is tangent vector, not position vector.  
D) ✗ Tangent line is not perpendicular to tangent vector.

**Correct:** A


#### 11. Which of the following statements about the definite integral of a vector-valued function $\mathbf{r}(t) = (x(t), y(t), z(t))$ over $[a,b]$ is true?  
A) ✓ Integral is component-wise.  
B) ✓ Integral is vector of component integrals.  
C) ✗ Integral is vector, not scalar.  
D) ✗ Integral of magnitude is different from vector integral.

**Correct:** A, B


#### 12. Suppose $\mathbf{r}(t)$ is differentiable and $\mathbf{r}'(t)$ is continuous. Which of the following is true?  
A) ✓ This means $\mathbf{r}$ is class $C^1$.  
B) ✗ Differentiability and continuity of derivative imply continuity of $\mathbf{r}$.  
C) ✓ Continuous derivative implies integrability.  
D) ✗ $\mathbf{r}$ need not be constant.

**Correct:** A, C


#### 13. If $\mathbf{r}(t) = (t^2, \sin t, e^t)$, which of the following is true about $\mathbf{r}'(t)$?  
A) ✓ Correct component-wise derivative.  
B) ✗ No general orthogonality between $\mathbf{r}$ and $\mathbf{r}'$.  
C) ✓ Derivative represents velocity if $\mathbf{r}$ is position.  
D) ✗ $\mathbf{r}'(0) = (0,1,1) \neq \mathbf{0}$.

**Correct:** A, C


#### 14. Which of the following vector-valued functions represent a curve lying on a circle of radius $r$ in the xy-plane?  
A) ✓ Lies on circle in xy-plane at $z=0$.  
B) ✗ Has $z = t$, so not confined to xy-plane.  
C) ✗ $z = r \cos t$ varies, so not in xy-plane.  
D) ✗ $z = r \sin t$ varies, so not in xy-plane.

**Correct:** A


#### 15. For the vector-valued function $\mathbf{r}(t) = (2 \cos t + \cos 2t, 2 \sin t - \sin 2t)$, which of the following is true?  
A) ✓ This is the parametric form of a tricuspoid.  
B) ✗ Lies in 2D plane, not 3D.  
C) ✓ Components are sums of sine and cosine, hence periodic.  
D) ✗ Curve is not a straight line.

**Correct:** A, C


#### 16. If $\mathbf{r}(t)$ is differentiable and $\mathbf{r}'(t) = \mathbf{0}$ for all $t$, then:  
A) ✓ $\mathbf{r}(t)$ is constant vector function.  
B) ✓ Represents stationary point (no change).  
C) ✗ $\mathbf{r}(t)$ need not be zero vector, just constant.  
D) ✗ Constant functions are continuous.

**Correct:** A, B


#### 17. Which of the following statements about the cross product of two vector-valued functions $\mathbf{F}(t)$ and $\mathbf{G}(t)$ is true?  
A) ✓ Product rule for cross product derivative.  
B) ✗ Cross product is anti-commutative, not commutative.  
C) ✓ Cross product is orthogonal to both vectors.  
D) ✓ Limit of cross product equals cross product of limits if limits exist.

**Correct:** A, C, D


#### 18. Consider $\mathbf{r}(t) = (a \cos t, a \sin t, c t)$. Which of the following statements are correct?  
A) ✓ This is the parametric form of a circular helix.  
B) ✓ Projection onto xy-plane is circle of radius $a$.  
C) ✓ Distance from origin is $\sqrt{a^2 + c^2 t^2}$, so lies on a helix, not sphere.  
D) ✗ Tangent vector is not always perpendicular to $\mathbf{r}(t)$.

**Correct:** A, B, C


#### 19. Which of the following are true about the derivative of the dot product of two vector-valued functions $\mathbf{F}(t)$ and $\mathbf{G}(t)$?  
A) ✓ Correct product rule for dot product derivative.  
B) ✗ Not equal to dot product of derivatives alone.  
C) ✓ Result is scalar function.  
D) ✗ Result is scalar, not vector.

**Correct:** A, C


#### 20. If $\mathbf{r}(t)$ is continuous on $[a,b]$, which of the following statements about $\int_a^b \mathbf{r}(t) dt$ is true?  
A) ✓ Integral is vector of component integrals.  
B) ✗ Integral depends on values of $\mathbf{r}(t)$, not path traced.  
C) ✓ If $\mathbf{r}(t)$ is velocity, integral gives displacement.  
D) ✗ Integral is not always zero; depends on function.

**Correct:** A, C