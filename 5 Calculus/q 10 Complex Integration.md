## 10. Complex Integration

## Questions

#### 1. Which of the following statements about the integral of a complex-valued function $f(t) = u(t) + i v(t)$ over a real interval $[a,b]$ are true?  
A) The integral can be separated into the integral of the real part plus $i$ times the integral of the imaginary part.  
B) The integral is only defined if $u(t)$ and $v(t)$ are differentiable.  
C) If $u(t)$ and $v(t)$ are continuous, the integral always exists.  
D) The integral of $f(t)$ is always a real number.


#### 2. Let $C$ be a contour in the complex plane parametrized by $z(t)$ for $t \in [a,b]$. Which of the following correctly expresses the contour integral $\int_C f(z) \, dz$?  
A) $\int_a^b f(z(t)) \, dt$  
B) $\int_a^b f(z(t)) z'(t) \, dt$  
C) $\int_a^b f(t) z(t) \, dt$  
D) $\int_a^b f(z(t)) \overline{z'(t)} \, dt$


#### 3. Consider the ML inequality for a function $f$ continuous on a contour $C$ of length $L$. Which of the following statements are correct?  
A) The inequality states $\left| \int_C f(z) \, dz \right| \leq M L$, where $M$ is the maximum of $|f(z)|$ on $C$.  
B) The inequality can be used to find exact values of integrals.  
C) The length $L$ of the contour is always finite for the inequality to hold.  
D) The ML inequality applies only if $f$ is analytic on $C$.


#### 4. Which of the following are true about the Cauchy-Goursat theorem?  
A) It requires $f$ to be analytic inside and on the contour $C$.  
B) It applies to any closed contour, even if the domain is not simply connected.  
C) It implies that the integral of $f$ over $C$ is zero.  
D) It guarantees the existence of an antiderivative of $f$ in the domain.


#### 5. Suppose $f(z) = \frac{1}{z}$ and $C$ is a simple closed contour enclosing the origin. Which of the following are true?  
A) $f$ is analytic everywhere inside $C$.  
B) $\int_C f(z) \, dz = 2 \pi i$.  
C) The value of the integral depends on the shape of $C$.  
D) The integral is zero if $C$ does not enclose the origin.


#### 6. If $C_1$ and $C_2$ are two simple closed contours such that $C_1$ lies inside $C_2$, and $f$ is analytic in the region between them, which statements are correct?  
A) $\int_{C_1} f(z) \, dz = \int_{C_2} f(z) \, dz$  
B) The integrals may differ if $f$ has singularities inside $C_1$.  
C) The deformation of contour lemma applies here.  
D) The integrals are always zero regardless of $f$.


#### 7. Which of the following statements about the integral triangle inequality are true?  
A) It states $\left| \int_a^b f(t) \, dt \right| \leq \int_a^b |f(t)| \, dt$.  
B) It can be used to estimate the magnitude of complex integrals.  
C) It requires $f$ to be analytic.  
D) It is a direct consequence of the triangle inequality for complex numbers.


#### 8. Consider the integral $\int_C z \, dz$ where $C$ is a contour from $z = -1 - i$ to $z = 3 + i$. Which of the following are true?  
A) The value of the integral depends on the path $C$.  
B) If $C$ is a line segment, the integral can be computed using parametrization.  
C) If $C$ is a parabola joining the same points, the integral value differs from the line segment case.  
D) Since $z$ is analytic everywhere, the integral depends only on the endpoints.


#### 9. Which of the following are true about the extended Cauchy-Goursat theorem?  
A) It applies to domains with multiple holes (multiply connected domains).  
B) The integral over the outer contour equals the sum of integrals over the inner contours.  
C) It requires $f$ to be analytic only on the outer contour.  
D) It generalizes the original Cauchy-Goursat theorem to more complex domains.


#### 10. Which of the following statements about contour parametrization are correct?  
A) A contour can be parametrized by a single smooth function $z(t)$ over an interval.  
B) Polygonal paths require piecewise parametrization.  
C) Parametrization is not necessary to evaluate contour integrals.  
D) The derivative $z'(t)$ must exist and be continuous for the integral formula to hold.


#### 11. Let $f(z) = e^z$ and $C$ be the line segment from $0$ to $2 + i$. Which of the following are true?  
A) The contour integral $\int_C e^z \, dz$ can be approximated by Riemann sums.  
B) The integral depends on the path taken between the points.  
C) Since $e^z$ is entire, the integral depends only on the endpoints.  
D) The integral can be evaluated exactly using parametrization.


#### 12. Which of the following statements about singularities and contour integrals are true?  
A) If $f$ has singularities inside a contour, the integral may not be zero.  
B) The Cauchy-Goursat theorem applies even if singularities are present inside the contour.  
C) The value of the integral can change if the contour is deformed across singularities.  
D) Singularities do not affect the integral if the function is bounded.


#### 13. Which of the following are true regarding the length $L$ of a contour $C$?  
A) $L$ is always finite for piecewise smooth contours.  
B) $L$ is used in the ML inequality to bound integrals.  
C) $L$ can be infinite for fractal-like contours.  
D) The length $L$ affects the existence of the contour integral.


#### 14. Suppose $f(z)$ is analytic in a simply connected domain $D$. Which of the following are true?  
A) The integral of $f$ over any closed contour in $D$ is zero.  
B) $f$ has an antiderivative in $D$.  
C) The integral of $f$ depends on the path between two points in $D$.  
D) The integral over two different contours with the same endpoints in $D$ are equal.


#### 15. Which of the following are true about the function $f(z) = \frac{1}{z}$ and its integrals over different paths?  
A) The integral over a semi-circular path from $-1$ to $1$ can differ from the integral over a polygonal path joining the same points.  
B) $f$ is analytic everywhere except at $z=0$.  
C) The integral over any closed contour enclosing $z=0$ is zero.  
D) The integral depends on whether the path crosses the singularity at $z=0$.


#### 16. Which of the following are true about the Riemann sum definition of contour integrals?  
A) The limit of the Riemann sum exists only if $f$ is continuous on the contour.  
B) The points $c_k$ in the sum must be chosen as the midpoint of each partition segment.  
C) The sum approximates the integral by summing $f(c_k) \Delta z_k$ over partitions.  
D) The Riemann sum approach generalizes the real integral to complex paths.


#### 17. Which of the following statements about the integral of $f(z) = z^n$ over a simple closed contour $C$ are true?  
A) If $n \neq -1$, then $\int_C z^n \, dz = 0$.  
B) If $n = -1$, then $\int_C z^n \, dz = 2 \pi i$ if $C$ encloses the origin.  
C) The integral depends on the radius of the contour.  
D) The integral is zero if $C$ does not enclose the origin.


#### 18. Which of the following are true about the polygonal path contour integral?  
A) The integral over a polygonal path can be computed by summing integrals over each linear segment.  
B) The integral depends on the number of vertices in the polygon.  
C) The polygonal path must be closed for the integral to be defined.  
D) Parametrization of each segment is necessary for evaluation.


#### 19. Which of the following are true about the continuity requirements for complex integrals?  
A) $f$ must be continuous on the contour for the integral to exist.  
B) $f$ must be analytic on the contour for the integral to exist.  
C) Discontinuities on the contour prevent the existence of the integral.  
D) Continuity of $u(t)$ and $v(t)$ (real and imaginary parts) is sufficient for integrability.


#### 20. Which of the following statements about the figure-eight contour integral are true?  
A) The integral over a figure-eight contour can be expressed as the sum of integrals over its two loops.  
B) If $f$ is analytic everywhere inside the figure-eight, the integral is zero.  
C) The orientation of each loop affects the sign of the integral.  
D) The figure-eight contour integral always equals zero regardless of $f$.



<br>

## Answers

#### 1. Which of the following statements about the integral of a complex-valued function $f(t) = u(t) + i v(t)$ over a real interval $[a,b]$ are true?  
A) ✓ The integral separates into real and imaginary parts because integration is linear.  
B) ✗ Differentiability is not required; continuity suffices for integrability.  
C) ✓ Continuity of $u$ and $v$ guarantees integrability on $[a,b]$.  
D) ✗ The integral is generally complex, not necessarily real.

**Correct:** A, C


#### 2. Let $C$ be a contour in the complex plane parametrized by $z(t)$ for $t \in [a,b]$. Which of the following correctly expresses the contour integral $\int_C f(z) \, dz$?  
A) ✗ Missing the factor $z'(t)$, so not correct.  
B) ✓ Correct formula converting contour integral to real integral.  
C) ✗ Incorrect integrand; $f$ depends on $z(t)$, not $t$ alone.  
D) ✗ Complex conjugate of $z'(t)$ is not used in contour integrals.

**Correct:** B


#### 3. Consider the ML inequality for a function $f$ continuous on a contour $C$ of length $L$. Which of the following statements are correct?  
A) ✓ Correct statement of the ML inequality.  
B) ✗ ML inequality provides an upper bound, not exact values.  
C) ✓ Length $L$ must be finite for the inequality to hold.  
D) ✗ Analyticity is not required; continuity suffices.

**Correct:** A, C


#### 4. Which of the following are true about the Cauchy-Goursat theorem?  
A) ✓ Requires $f$ to be analytic inside and on $C$.  
B) ✗ Requires simply connected domain; not valid for all closed contours.  
C) ✓ Integral over $C$ is zero under the theorem’s conditions.  
D) ✓ Analyticity implies existence of antiderivative in the domain.

**Correct:** A, C, D


#### 5. Suppose $f(z) = \frac{1}{z}$ and $C$ is a simple closed contour enclosing the origin. Which of the following are true?  
A) ✗ $f$ is not analytic at $z=0$, so not analytic everywhere inside $C$.  
B) ✓ Integral equals $2 \pi i$ by Cauchy integral formula.  
C) ✗ Integral depends only on whether $C$ encloses the singularity, not shape.  
D) ✓ Integral is zero if $C$ does not enclose the origin.

**Correct:** B, D


#### 6. If $C_1$ and $C_2$ are two simple closed contours such that $C_1$ lies inside $C_2$, and $f$ is analytic in the region between them, which statements are correct?  
A) ✓ By deformation of contour lemma, integrals are equal.  
B) ✗ If $f$ is analytic in the region, no singularities inside $C_1$, so integrals equal.  
C) ✓ This is exactly the deformation of contour lemma.  
D) ✗ Integrals are not always zero; depends on $f$.

**Correct:** A, C


#### 7. Which of the following statements about the integral triangle inequality are true?  
A) ✓ Correct statement of the integral triangle inequality.  
B) ✓ It is used to estimate magnitudes of integrals.  
C) ✗ Analyticity is not required; continuity suffices.  
D) ✓ It follows from the triangle inequality for complex numbers.

**Correct:** A, B, D


#### 8. Consider the integral $\int_C z \, dz$ where $C$ is a contour from $z = -1 - i$ to $z = 3 + i$. Which of the following are true?  
A) ✗ Since $z$ is entire, integral depends only on endpoints, not path.  
B) ✓ Parametrization can be used to compute integral over line segment.  
C) ✗ Integral over parabola equals that over line segment due to analyticity.  
D) ✓ Path independence holds for analytic functions like $z$.

**Correct:** B, D


#### 9. Which of the following are true about the extended Cauchy-Goursat theorem?  
A) ✓ Applies to multiply connected domains with holes.  
B) ✓ Integral over outer contour equals sum of integrals over inner contours.  
C) ✗ Requires $f$ to be analytic in the entire region including all contours.  
D) ✓ It generalizes the original theorem to complex domains.

**Correct:** A, B, D


#### 10. Which of the following statements about contour parametrization are correct?  
A) ✓ A single smooth function can parametrize a smooth contour.  
B) ✓ Polygonal paths require piecewise parametrization for each segment.  
C) ✗ Parametrization is necessary to evaluate contour integrals explicitly.  
D) ✓ $z'(t)$ must exist and be continuous for integral formula to hold.

**Correct:** A, B, D


#### 11. Let $f(z) = e^z$ and $C$ be the line segment from $0$ to $2 + i$. Which of the following are true?  
A) ✓ Riemann sums can approximate the integral.  
B) ✗ Since $e^z$ is entire, integral depends only on endpoints, not path.  
C) ✓ Path independence holds for entire functions like $e^z$.  
D) ✓ Parametrization allows exact evaluation.

**Correct:** A, C, D


#### 12. Which of the following statements about singularities and contour integrals are true?  
A) ✓ Singularities inside a contour can cause the integral to be nonzero.  
B) ✗ Cauchy-Goursat theorem requires no singularities inside contour.  
C) ✓ Deforming contour across singularities can change integral value.  
D) ✗ Singularities generally cause unbounded behavior, affecting integrals.

**Correct:** A, C


#### 13. Which of the following are true regarding the length $L$ of a contour $C$?  
A) ✓ Piecewise smooth contours have finite length.  
B) ✓ Length $L$ is used in ML inequality to bound integrals.  
C) ✓ Fractal-like curves can have infinite length, but such contours are not piecewise smooth.  
D) ✗ Length does not affect existence of integral if contour is piecewise smooth.

**Correct:** A, B, C


#### 14. Suppose $f(z)$ is analytic in a simply connected domain $D$. Which of the following are true?  
A) ✓ Integral over any closed contour in $D$ is zero.  
B) ✓ $f$ has an antiderivative in $D$.  
C) ✗ Integral depends only on endpoints, so path independence holds.  
D) ✓ Integrals over different paths with same endpoints are equal.

**Correct:** A, B, D


#### 15. Which of the following are true about the function $f(z) = \frac{1}{z}$ and its integrals over different paths?  
A) ✓ Integral over different paths joining same points can differ if paths encircle singularity differently.  
B) ✓ $f$ is analytic everywhere except at $z=0$.  
C) ✗ Integral over closed contour enclosing $z=0$ is $2 \pi i$, not zero.  
D) ✓ Integral depends on whether path crosses or encircles singularity.

**Correct:** A, B, D


#### 16. Which of the following are true about the Riemann sum definition of contour integrals?  
A) ✓ Limit exists if $f$ is continuous on the contour.  
B) ✗ $c_k$ can be any point in the subinterval, not necessarily midpoint.  
C) ✓ Sum approximates integral by summing $f(c_k) \Delta z_k$.  
D) ✓ Riemann sums generalize real integrals to complex paths.

**Correct:** A, C, D


#### 17. Which of the following statements about the integral of $f(z) = z^n$ over a simple closed contour $C$ are true?  
A) ✓ For $n \neq -1$, integral is zero by Cauchy-Goursat.  
B) ✓ For $n = -1$, integral equals $2 \pi i$ if $C$ encloses origin.  
C) ✗ Integral does not depend on radius, only on whether contour encloses singularity.  
D) ✓ Integral is zero if $C$ does not enclose origin.

**Correct:** A, B, D


#### 18. Which of the following are true about the polygonal path contour integral?  
A) ✓ Integral over polygonal path is sum over linear segments.  
B) ✗ Integral depends on function and path, not number of vertices alone.  
C) ✗ Polygonal path need not be closed to define integral.  
D) ✓ Parametrization of each segment is necessary for evaluation.

**Correct:** A, D


#### 19. Which of the following are true about the continuity requirements for complex integrals?  
A) ✓ Continuity of $f$ on contour is necessary for integral existence.  
B) ✗ Analyticity is not required for integral to exist, only continuity.  
C) ✗ Discontinuities prevent existence of integral.  
D) ✓ Continuity of real and imaginary parts suffices for integrability.

**Correct:** A, D


#### 20. Which of the following statements about the figure-eight contour integral are true?  
A) ✓ Integral over figure-eight equals sum of integrals over loops (with orientation).  
B) ✓ If $f$ is analytic everywhere inside, integral is zero by Cauchy-Goursat.  
C) ✓ Orientation of loops affects sign of each integral.  
D) ✗ Integral is not always zero; depends on $f$ and singularities.

**Correct:** A, B, C