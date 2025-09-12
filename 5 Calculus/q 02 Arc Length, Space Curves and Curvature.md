## 2. Arc Length, Space Curves and Curvature

## Questions

#### 1. Which of the following statements about the arc length of a curve $\mathbf{r}(t)$ are true?  
A) The arc length is always equal to $\int_a^b \|\mathbf{r}'(t)\| dt$ regardless of differentiability.  
B) A curve is rectifiable if its arc length is finite.  
C) The arc length depends on the parameterization of the curve.  
D) The supremum of sums of chord lengths over all partitions defines the arc length.


#### 2. For a vector-valued function $\mathbf{r}(t)$, which of the following are true regarding the Mean Value Theorem (MVT)?  
A) MVT applies directly to $\mathbf{r}(t)$ in $\mathbb{R}^3$.  
B) In $\mathbb{R}^2$, there exists some $c$ such that $\mathbf{r}'(c)$ is parallel to $\mathbf{r}(b) - \mathbf{r}(a)$.  
C) MVT guarantees a point where the tangent vector equals the average velocity vector.  
D) MVT does not hold for vector-valued functions in general.


#### 3. Consider a change of parameter $t = g(\tau)$ for a curve $\mathbf{r}(t)$. Which statements are correct?  
A) The graph of $\mathbf{r}(g(\tau))$ is the same as $\mathbf{r}(t)$ but may be traced differently.  
B) The derivative $\frac{d}{d\tau} \mathbf{r}(g(\tau)) = \mathbf{r}'(g(\tau)) \cdot g'(\tau)$.  
C) The arc length of the curve changes under reparameterization.  
D) If $g(\tau)$ is not differentiable, the chain rule does not apply.


#### 4. Which of the following properties hold for the arc length parameter $s$ of a curve $\mathbf{r}(t)$?  
A) $s$ measures the distance traveled along the curve from a reference point.  
B) The derivative $\frac{d\mathbf{r}}{ds}$ always has unit length.  
C) The arc length parameterization is unique for every curve.  
D) If $\|\mathbf{r}'(t)\| = 1$, then $t$ itself is an arc length parameter.


#### 5. The unit tangent vector $\mathbf{T}(t)$ of a curve satisfies which of the following?  
A) $\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}$ if $\mathbf{r}'(t) \neq 0$.  
B) $\mathbf{T}(t)$ points in the direction of increasing parameter $t$.  
C) $\mathbf{T}(t)$ is always orthogonal to $\mathbf{r}(t)$.  
D) $\mathbf{T}(t)$ has length 1 for all $t$.


#### 6. The principal unit normal vector $\mathbf{N}(t)$ is defined as:  
A) The normalized derivative of the unit tangent vector $\mathbf{T}'(t)$.  
B) The vector pointing in the direction of the curve’s concavity.  
C) Always parallel to $\mathbf{T}(t)$.  
D) Orthogonal to $\mathbf{T}(t)$.


#### 7. Which of the following statements about the binormal vector $\mathbf{B}(t)$ are true?  
A) $\mathbf{B}(t) = \mathbf{T}(t) \times \mathbf{N}(t)$.  
B) $\mathbf{B}(t)$ is orthogonal to both $\mathbf{T}(t)$ and $\mathbf{N}(t)$.  
C) $\mathbf{B}(t)$ always lies in the osculating plane.  
D) The set $\{\mathbf{T}(t), \mathbf{N}(t), \mathbf{B}(t)\}$ forms a right-handed orthonormal basis.


#### 8. The TNB frame vectors $\mathbf{T}(t), \mathbf{N}(t), \mathbf{B}(t)$ define which of the following planes at each point on the curve?  
A) Rectifying plane (TB-plane)  
B) Osculating plane (TN-plane)  
C) Normal plane (NB-plane)  
D) Tangential plane (TB-plane)


#### 9. Which of the following are true about curvature $\kappa$ of a curve parameterized by arc length $s$?  
A) $\kappa(s) = \left\|\frac{d\mathbf{T}}{ds}\right\|$.  
B) $\kappa(s) = \|\mathbf{r}''(s)\|$.  
C) Curvature measures the rate of change of the position vector.  
D) Curvature is always non-negative.


#### 10. For a curve parameterized by a general parameter $t$, the curvature $\kappa(t)$ can be expressed as:  
A) $\kappa(t) = \frac{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|}{\|\mathbf{r}'(t)\|^3}$.  
B) $\kappa(t) = \frac{\|\mathbf{r}''(t)\|}{\|\mathbf{r}'(t)\|}$.  
C) $\kappa(t) = \|\mathbf{T}'(t)\|$.  
D) $\kappa(t) = \frac{\|\mathbf{r}'(t) \cdot \mathbf{r}''(t)\|}{\|\mathbf{r}'(t)\|^3}$.


#### 11. Consider the helix $\mathbf{r}(t) = (a \cos t, a \sin t, b t)$ with $a,b \geq 0$. Which statements about its curvature are correct?  
A) The curvature depends only on $a$.  
B) The curvature depends on both $a$ and $b$.  
C) If $b=0$, the curve reduces to a circle with curvature $\frac{1}{a}$.  
D) The curvature is zero if $a=0$.


#### 12. The radius of curvature $\rho$ at a point on a curve is:  
A) The reciprocal of the curvature $\kappa$.  
B) The radius of the osculating circle at that point.  
C) Always equal to the length of the normal vector $\mathbf{N}(t)$.  
D) The distance from the point on the curve to the center of curvature.


#### 13. Which of the following statements about the osculating circle are true?  
A) It shares the same tangent line as the curve at the point of contact.  
B) Its center lies on the concave side of the curve.  
C) It is the unique circle that best approximates the curve near that point.  
D) Its radius is equal to the curvature $\kappa$.


#### 14. If a curve $\mathbf{r}(t)$ has $\|\mathbf{r}'(t)\| = 1$ for all $t$, which of the following are true?  
A) The parameter $t$ is an arc length parameter.  
B) The unit tangent vector $\mathbf{T}(t) = \mathbf{r}'(t)$.  
C) The curvature $\kappa(t) = \|\mathbf{r}''(t)\|$.  
D) The curve is necessarily a straight line.


#### 15. Which of the following are consequences of the chain rule for vector-valued functions under parameter change $t = g(\tau)$?  
A) Differentiability of $\mathbf{r}(g(\tau))$ depends on differentiability of both $\mathbf{r}$ and $g$.  
B) The speed $\|\frac{d}{d\tau} \mathbf{r}(g(\tau))\|$ equals $\|\mathbf{r}'(g(\tau))\| \cdot |g'(\tau)|$.  
C) The arc length parameter is invariant under any change of parameter.  
D) The direction of the tangent vector may reverse if $g'(\tau) < 0$.


#### 16. Which of the following statements about the TNB frame are false?  
A) The vectors $\mathbf{T}(t), \mathbf{N}(t), \mathbf{B}(t)$ are mutually orthogonal.  
B) The binormal vector $\mathbf{B}(t)$ can be expressed directly in terms of $\mathbf{r}(t)$ and its derivatives.  
C) The TNB frame is defined only for curves in $\mathbb{R}^2$.  
D) The TNB frame vectors form a right-handed coordinate system.


#### 17. For a curve $\mathbf{r}(t)$ with $\mathbf{r}'(t) \neq 0$, which of the following are true?  
A) The tangent vector $\mathbf{r}'(t)$ always has unit length.  
B) The arc length parameter $s$ can be chosen so that $\frac{d\mathbf{r}}{ds}$ has length 1.  
C) The parameter $\sigma = t - t_0$ is an arc length parameter if $\|\mathbf{r}'(t)\| = 1$.  
D) The curvature $\kappa(t)$ is zero if and only if $\mathbf{r}''(t) = \mathbf{0}$.


#### 18. Which of the following statements about the normal plane (NB-plane) are correct?  
A) It is spanned by $\mathbf{N}(t)$ and $\mathbf{B}(t)$.  
B) It contains the tangent vector $\mathbf{T}(t)$.  
C) It is perpendicular to the tangent vector $\mathbf{T}(t)$.  
D) It is the plane in which the curve lies if the curvature is zero.


#### 19. Which of the following are true about the rectifying plane (TB-plane)?  
A) It contains the tangent and binormal vectors.  
B) It is always perpendicular to the principal normal vector.  
C) It is the plane that contains the osculating circle.  
D) It changes as the curve twists in space.


#### 20. Consider a curve $\mathbf{r}(t)$ with $\mathbf{r}'(t) \neq 0$ and $\mathbf{r}''(t)$ existing. Which of the following are true?  
A) If $\mathbf{r}''(t)$ is parallel to $\mathbf{r}'(t)$, then the curvature $\kappa(t) = 0$.  
B) The curvature depends on the component of $\mathbf{r}''(t)$ orthogonal to $\mathbf{r}'(t)$.  
C) The curvature can be zero even if $\mathbf{r}''(t) \neq 0$.  
D) The curvature is invariant under reparameterization of the curve.



<br>

## Answers

#### 1. Which of the following statements about the arc length of a curve $\mathbf{r}(t)$ are true?  
A) ✗ The integral formula requires $\mathbf{r}$ to be differentiable; otherwise, it may not hold.  
B) ✓ A curve is rectifiable if its arc length is finite.  
C) ✗ Arc length is a geometric property and does not depend on parameterization, though the integral expression depends on parameterization.  
D) ✓ The arc length is defined as the supremum of sums of chord lengths over all partitions.

**Correct:** B, D


#### 2. For a vector-valued function $\mathbf{r}(t)$, which of the following are true regarding the Mean Value Theorem (MVT)?  
A) ✗ MVT does not apply directly to vector-valued functions in $\mathbb{R}^3$.  
B) ✓ In $\mathbb{R}^2$, there exists some $c$ such that $\mathbf{r}'(c)$ is parallel to $\mathbf{r}(b) - \mathbf{r}(a)$.  
C) ✗ MVT does not guarantee equality of tangent and average velocity vectors for vector functions.  
D) ✓ MVT generally does not hold for vector-valued functions.

**Correct:** B, D


#### 3. Consider a change of parameter $t = g(\tau)$ for a curve $\mathbf{r}(t)$. Which statements are correct?  
A) ✓ The graph remains the same but may be traced differently.  
B) ✓ The chain rule applies as stated.  
C) ✗ Arc length is a geometric property and does not change under reparameterization.  
D) ✓ If $g$ is not differentiable, the chain rule does not apply.

**Correct:** A, B, D


#### 4. Which of the following properties hold for the arc length parameter $s$ of a curve $\mathbf{r}(t)$?  
A) ✓ $s$ measures distance along the curve from a reference point.  
B) ✓ The derivative $\frac{d\mathbf{r}}{ds}$ has unit length by definition.  
C) ✗ Arc length parameterization is not unique; it depends on the choice of reference point and orientation.  
D) ✓ If $\|\mathbf{r}'(t)\|=1$, then $t$ is an arc length parameter.

**Correct:** A, B, D


#### 5. The unit tangent vector $\mathbf{T}(t)$ of a curve satisfies which of the following?  
A) ✓ Definition of unit tangent vector.  
B) ✓ Points in direction of increasing $t$.  
C) ✗ $\mathbf{T}(t)$ is not necessarily orthogonal to $\mathbf{r}(t)$.  
D) ✓ By definition, $\mathbf{T}(t)$ has length 1.

**Correct:** A, B, D


#### 6. The principal unit normal vector $\mathbf{N}(t)$ is defined as:  
A) ✓ It is the normalized derivative of $\mathbf{T}(t)$.  
B) ✓ Points toward the direction of curve’s concavity.  
C) ✗ $\mathbf{N}(t)$ is orthogonal, not parallel, to $\mathbf{T}(t)$.  
D) ✓ By construction, $\mathbf{N}(t)$ is orthogonal to $\mathbf{T}(t)$.

**Correct:** A, B, D


#### 7. Which of the following statements about the binormal vector $\mathbf{B}(t)$ are true?  
A) ✓ Definition of $\mathbf{B}(t)$.  
B) ✓ Cross product ensures orthogonality to $\mathbf{T}(t)$ and $\mathbf{N}(t)$.  
C) ✗ $\mathbf{B}(t)$ is perpendicular to the osculating plane, not lying in it.  
D) ✓ The TNB frame is orthonormal and right-handed.

**Correct:** A, B, D


#### 8. The TNB frame vectors $\mathbf{T}(t), \mathbf{N}(t), \mathbf{B}(t)$ define which of the following planes at each point on the curve?  
A) ✓ Rectifying plane is spanned by $\mathbf{T}$ and $\mathbf{B}$.  
B) ✓ Osculating plane is spanned by $\mathbf{T}$ and $\mathbf{N}$.  
C) ✓ Normal plane is spanned by $\mathbf{N}$ and $\mathbf{B}$.  
D) ✗ Tangential plane is not a standard term here.

**Correct:** A, B, C


#### 9. Which of the following are true about curvature $\kappa$ of a curve parameterized by arc length $s$?  
A) ✓ Curvature is the magnitude of the rate of change of the unit tangent vector.  
B) ✓ Since $\mathbf{r}''(s) = \mathbf{T}'(s)$, curvature equals $\|\mathbf{r}''(s)\|$.  
C) ✗ Curvature measures change in direction, not position vector itself.  
D) ✓ Curvature is a non-negative scalar.

**Correct:** A, B, D


#### 10. For a curve parameterized by a general parameter $t$, the curvature $\kappa(t)$ can be expressed as:  
A) ✓ Correct formula involving cross product and speed cubed.  
B) ✗ This formula does not correctly normalize curvature.  
C) ✗ $\mathbf{T}'(t)$ is not necessarily normalized; curvature requires normalization by speed cubed.  
D) ✗ Dot product does not give curvature.

**Correct:** A


#### 11. Consider the helix $\mathbf{r}(t) = (a \cos t, a \sin t, b t)$ with $a,b \geq 0$. Which statements about its curvature are correct?  
A) ✗ Curvature depends on both $a$ and $b$.  
B) ✓ True, curvature depends on both parameters.  
C) ✓ If $b=0$, the curve is a circle of radius $a$, curvature $1/a$.  
D) ✓ If $a=0$, the curve is a line along $z$-axis, curvature zero.

**Correct:** B, C, D


#### 12. The radius of curvature $\rho$ at a point on a curve is:  
A) ✓ Defined as reciprocal of curvature.  
B) ✓ Radius of the osculating circle.  
C) ✗ Normal vector length is always 1, unrelated to radius of curvature.  
D) ✓ Distance from point on curve to center of curvature.

**Correct:** A, B, D


#### 13. Which of the following statements about the osculating circle are true?  
A) ✓ Shares the same tangent line at the point.  
B) ✓ Center lies on concave side of curve.  
C) ✓ It best approximates the curve locally.  
D) ✗ Radius equals $1/\kappa$, not $\kappa$.

**Correct:** A, B, C


#### 14. If a curve $\mathbf{r}(t)$ has $\|\mathbf{r}'(t)\| = 1$ for all $t$, which of the following are true?  
A) ✓ Then $t$ is an arc length parameter.  
B) ✓ Unit tangent vector equals $\mathbf{r}'(t)$.  
C) ✓ Curvature equals $\|\mathbf{r}''(t)\|$ since parameter is arc length.  
D) ✗ Curve need not be a straight line; it can be curved with unit speed.

**Correct:** A, B, C


#### 15. Which of the following are consequences of the chain rule for vector-valued functions under parameter change $t = g(\tau)$?  
A) ✓ Differentiability depends on both $\mathbf{r}$ and $g$.  
B) ✓ Speed scales by $|g'(\tau)|$.  
C) ✗ Arc length is invariant as a geometric quantity but parameter values change.  
D) ✓ If $g'(\tau) < 0$, direction of tangent reverses.

**Correct:** A, B, D


#### 16. Which of the following statements about the TNB frame are false?  
A) ✗ Vectors are mutually orthogonal (true).  
B) ✗ Binormal can be expressed in terms of $\mathbf{r}$ and derivatives (true).  
C) ✓ TNB frame is defined only for curves in $\mathbb{R}^3$, not $\mathbb{R}^2$.  
D) ✗ They form a right-handed coordinate system (true).

**Correct:** C


#### 17. For a curve $\mathbf{r}(t)$ with $\mathbf{r}'(t) \neq 0$, which of the following are true?  
A) ✗ $\mathbf{r}'(t)$ need not have unit length.  
B) ✓ Arc length parameter $s$ can be chosen so that $\frac{d\mathbf{r}}{ds}$ has length 1.  
C) ✓ If $\|\mathbf{r}'(t)\|=1$, then $\sigma = t - t_0$ is an arc length parameter.  
D) ✓ Curvature zero iff $\mathbf{r}''(t)$ is parallel to $\mathbf{r}'(t)$, which implies zero normal acceleration.

**Correct:** B, C, D


#### 18. Which of the following statements about the normal plane (NB-plane) are correct?  
A) ✓ Spanned by $\mathbf{N}(t)$ and $\mathbf{B}(t)$.  
B) ✗ Does not contain $\mathbf{T}(t)$, which is orthogonal to it.  
C) ✓ Normal plane is perpendicular to $\mathbf{T}(t)$.  
D) ✗ If curvature is zero, curve is a straight line, and normal plane is not well-defined.

**Correct:** A, C


#### 19. Which of the following are true about the rectifying plane (TB-plane)?  
A) ✓ Contains $\mathbf{T}(t)$ and $\mathbf{B}(t)$.  
B) ✓ Perpendicular to $\mathbf{N}(t)$.  
C) ✗ Osculating circle lies in the osculating plane (TN-plane), not rectifying plane.  
D) ✓ Changes as the curve twists in space.

**Correct:** A, B, D


#### 20. Consider a curve $\mathbf{r}(t)$ with $\mathbf{r}'(t) \neq 0$ and $\mathbf{r}''(t)$ existing. Which of the following are true?  
A) ✓ If $\mathbf{r}''(t)$ is parallel to $\mathbf{r}'(t)$, curvature is zero (no bending).  
B) ✓ Curvature depends on component of $\mathbf{r}''(t)$ orthogonal to $\mathbf{r}'(t)$.  
C) ✓ Curvature can be zero even if $\mathbf{r}''(t) \neq 0$ if $\mathbf{r}''(t)$ is parallel to $\mathbf{r}'(t)$.  
D) ✓ Curvature is invariant under reparameterization.

**Correct:** A, B, C, D