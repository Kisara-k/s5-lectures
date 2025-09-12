## 11. Complex Integration (ctd.), Taylor and Laurent Series

## Questions

#### 1. Which of the following statements about analytic functions in a simply connected domain $D$ are true?  
A) Every analytic function in $D$ has an antiderivative in $D$.  
B) The integral of an analytic function over any closed contour in $D$ is zero.  
C) The value of an analytic function at a point inside a contour depends on the path taken.  
D) The integral of an analytic function between two points in $D$ depends only on the endpoints.


#### 2. Cauchy's Integral Formula states that for an analytic function $f$ inside a simple closed contour $C$, the value $f(z_0)$ at a point $z_0$ inside $C$ is given by  
A) $\frac{1}{2\pi i} \int_C \frac{f(z)}{z - z_0} dz$  
B) $\int_C f(z) dz$  
C) $\frac{1}{2\pi i} \int_C \frac{f(z)}{(z - z_0)^2} dz$  
D) $\frac{1}{2\pi i} \int_C \frac{f(z)}{z_0 - z} dz$


#### 3. Which of the following are true about the radius of convergence $\rho$ of a power series $\sum c_n (z - \alpha)^n$?  
A) The series converges absolutely for all $z$ such that $|z - \alpha| < \rho$.  
B) The series converges uniformly on any closed disk $|z - \alpha| \leq r < \rho$.  
C) The radius of convergence can be infinite, meaning the series converges everywhere.  
D) The series converges for all $z$ such that $|z - \alpha| \leq \rho$.


#### 4. Consider the sequence of functions $f_n(z)$ converging to $f(z)$ on a set $T$. Which of the following statements are correct?  
A) Uniform convergence implies pointwise convergence.  
B) Pointwise convergence implies uniform convergence.  
C) If $f_n$ are continuous and converge uniformly to $f$, then $f$ is continuous.  
D) If $f_n$ converge pointwise to $f$, then $f$ must be continuous.


#### 5. Which of the following are properties of the Taylor series of an analytic function $f$ centered at $\alpha$?  
A) The Taylor series converges to $f(z)$ inside the largest disk contained in the domain of analyticity.  
B) The Taylor series converges uniformly on any closed subdisk inside the radius of convergence.  
C) The Taylor series always converges for all $z \in \mathbb{C}$.  
D) The coefficients of the Taylor series are given by $\frac{f^{(n)}(\alpha)}{n!}$.


#### 6. Which of the following statements about Laurent series are true?  
A) Laurent series include terms with negative powers of $(z - \alpha)$.  
B) Laurent series converge only inside a disk centered at $\alpha$.  
C) Laurent series converge uniformly on any closed sub-annulus inside their annulus of convergence.  
D) Laurent series can represent functions analytic in annulus regions but not necessarily in disks.


#### 7. Given a function $f$ analytic in an annulus $A(r, R, \alpha)$, which of the following are true regarding its Laurent series representation?  
A) The coefficients $c_n$ can be computed by contour integrals around circles inside the annulus.  
B) The Laurent series representation is unique.  
C) The Laurent series converges only pointwise, not uniformly.  
D) The derivatives of $f$ can be obtained by term-wise differentiation of the Laurent series.


#### 8. Which of the following integrals can be evaluated using Cauchy's Integral Formula for derivatives?  
A) $\int_C \frac{e^z}{(z - z_0)^3} dz$  
B) $\int_C \frac{\sin z}{z - z_0} dz$  
C) $\int_C \frac{1}{z - z_0} dz$ where $f(z) = 1$  
D) $\int_C \frac{\cos z}{(z - z_0)^2} dz$


#### 9. Which of the following statements about power series operations are correct?  
A) The sum of two power series converges within the intersection of their radii of convergence.  
B) The product of two power series is given by the Cauchy product of their coefficients.  
C) The radius of convergence of the product series is always the minimum of the two radii.  
D) The derivative of a power series is not necessarily a power series.


#### 10. Suppose $f(z) = \sum_{n=0}^\infty a_n (z - \alpha)^n$ and $g(z) = \sum_{n=0}^\infty b_n (z - \alpha)^n$ have radii of convergence $r_1$ and $r_2$ respectively. Which of the following are true?  
A) $f(z) + g(z)$ converges for $|z - \alpha| < \min(r_1, r_2)$.  
B) $f(z)g(z)$ converges for $|z - \alpha| < \min(r_1, r_2)$.  
C) The coefficients of $f(z)g(z)$ are given by $c_n = \sum_{k=0}^n a_k b_{n-k}$.  
D) The radius of convergence of $f(z) + g(z)$ is always $\max(r_1, r_2)$.


#### 11. Which of the following are true about the convergence of the geometric series $\sum_{n=0}^\infty z^n$?  
A) It converges pointwise for $|z| < 1$.  
B) It converges uniformly on the closed disk $|z| \leq r$ for any $r < 1$.  
C) It converges uniformly on the unit circle $|z| = 1$.  
D) It diverges for $|z| > 1$.


#### 12. Which of the following statements about the uniqueness of power series representations are correct?  
A) If two power series agree on a disk, their coefficients must be identical.  
B) A function can have multiple distinct power series representations in the same disk.  
C) The Taylor series of an analytic function is the unique power series representation around the center.  
D) Uniqueness fails if the function is not analytic.


#### 13. Consider the function $f(z) = \frac{\cos z - 1}{z^4}$. Which of the following are true regarding its Laurent series expansion around $z=0$?  
A) The Laurent series will contain negative powers of $z$.  
B) The Laurent series will have a finite principal part (finite number of negative powers).  
C) The function is analytic at $z=0$.  
D) The Laurent series can be obtained by dividing the Taylor series of $\cos z - 1$ by $z^4$.


#### 14. Which of the following are true about the relationship between analytic functions and power series?  
A) Every analytic function can be represented by a power series in some neighborhood of each point in its domain.  
B) Power series representations always converge to the function on the entire complex plane.  
C) Analyticity implies infinite differentiability.  
D) The converse is true: every infinitely differentiable function is analytic.


#### 15. Which of the following statements about uniform convergence of sequences of functions are true?  
A) Uniform convergence allows interchange of limit and integration.  
B) Uniform convergence guarantees continuity of the limit function if the sequence functions are continuous.  
C) Pointwise convergence is sufficient to interchange limit and integration.  
D) Uniform convergence depends on the choice of point $z$.


#### 16. Which of the following are true about the annulus $A(r, R, \alpha)$ where a Laurent series converges?  
A) The annulus can degenerate to a disk if $r=0$.  
B) The Laurent series converges inside the annulus but not on its boundary.  
C) The annulus is the region between two concentric circles centered at $\alpha$.  
D) The inner radius $r$ can be zero, but the outer radius $R$ must be finite.


#### 17. Which of the following are true about the coefficients $c_n$ of a Laurent series?  
A) They can be computed by contour integrals involving $f(z)$ and $(z - \alpha)^{-(n+1)}$.  
B) The coefficients for negative $n$ correspond to the principal part of the Laurent series.  
C) The coefficients $c_n$ for $n \geq 0$ are always zero if the function has a singularity at $\alpha$.  
D) The coefficients are unique for a given function and annulus.


#### 18. Which of the following statements about the derivatives of functions represented by power or Laurent series are true?  
A) The derivative of a power series can be obtained by term-wise differentiation inside the radius of convergence.  
B) The derivative of a Laurent series can be obtained by term-wise differentiation inside the annulus of convergence.  
C) Term-wise differentiation may change the radius of convergence of a power series.  
D) Term-wise differentiation is not valid for Laurent series.


#### 19. Which of the following are true about the integral $\int_C \frac{e^{z^2}}{(z - z_0)^3} dz$ where $C$ is a circle around $z_0$?  
A) It can be evaluated using Cauchy's Integral Formula for the second derivative of $e^{z^2}$.  
B) The integral equals $\frac{2\pi i}{2!} f^{(2)}(z_0)$.  
C) The integral depends on the radius of the circle $C$.  
D) The integral is zero if $e^{z^2}$ is analytic inside $C$.


#### 20. Which of the following are true about the convergence of Laurent series on closed sub-annuli?  
A) Laurent series converge uniformly on any closed sub-annulus strictly inside the annulus of convergence.  
B) Uniform convergence fails on the boundary circles of the annulus.  
C) Uniform convergence implies continuity of the sum function on the closed sub-annulus.  
D) Laurent series converge pointwise but not uniformly on any sub-annulus.



<br>

## Answers

#### 1. Which of the following statements about analytic functions in a simply connected domain $D$ are true?  
A) ✓ Every analytic function in $D$ has an antiderivative in $D$.  
B) ✓ The integral of an analytic function over any closed contour in $D$ is zero (Cauchy's theorem).  
C) ✗ The value inside depends only on endpoints, not path, so this is false.  
D) ✓ The integral depends only on endpoints due to existence of antiderivatives.

**Correct:** A, B, D


#### 2. Cauchy's Integral Formula states that for an analytic function $f$ inside a simple closed contour $C$, the value $f(z_0)$ at a point $z_0$ inside $C$ is given by  
A) ✓ Correct formula of Cauchy's Integral Formula.  
B) ✗ Missing denominator $z - z_0$, not correct.  
C) ✗ This formula corresponds to derivative, not function value.  
D) ✗ Wrong sign in denominator; integral depends on $z - z_0$.

**Correct:** A


#### 3. Which of the following are true about the radius of convergence $\rho$ of a power series $\sum c_n (z - \alpha)^n$?  
A) ✓ Power series converge absolutely inside radius of convergence.  
B) ✓ Uniform convergence on any closed disk inside radius.  
C) ✓ Radius can be infinite, meaning entire complex plane convergence.  
D) ✗ Convergence on boundary $|z - \alpha| = \rho$ is not guaranteed.

**Correct:** A, B, C


#### 4. Consider the sequence of functions $f_n(z)$ converging to $f(z)$ on a set $T$. Which of the following statements are correct?  
A) ✓ Uniform convergence implies pointwise convergence.  
B) ✗ Pointwise convergence does not imply uniform convergence.  
C) ✓ Uniform limit of continuous functions is continuous.  
D) ✗ Pointwise limit need not be continuous.

**Correct:** A, C


#### 5. Which of the following are properties of the Taylor series of an analytic function $f$ centered at $\alpha$?  
A) ✓ Taylor series converges inside largest disk in domain.  
B) ✓ Converges uniformly on any closed subdisk inside radius.  
C) ✗ Does not always converge everywhere in $\mathbb{C}$.  
D) ✓ Coefficients given by derivatives at center divided by factorial.

**Correct:** A, B, D


#### 6. Which of the following statements about Laurent series are true?  
A) ✓ Laurent series include negative powers.  
B) ✗ Laurent series converge in annulus, not just disk.  
C) ✓ Converge uniformly on closed sub-annuli inside annulus.  
D) ✓ Represent functions analytic in annulus but not necessarily disk.

**Correct:** A, C, D


#### 7. Given a function $f$ analytic in an annulus $A(r, R, \alpha)$, which of the following are true regarding its Laurent series representation?  
A) ✓ Coefficients computed by contour integrals inside annulus.  
B) ✓ Laurent series representation is unique.  
C) ✗ Convergence is uniform on closed sub-annuli, not just pointwise.  
D) ✓ Derivatives obtained by term-wise differentiation.

**Correct:** A, B, D


#### 8. Which of the following integrals can be evaluated using Cauchy's Integral Formula for derivatives?  
A) ✓ Integral with denominator power 3 corresponds to second derivative.  
B) ✓ Integral with denominator power 1 corresponds to function value.  
C) ✗ Integral of $1/(z - z_0)$ with constant function is $2\pi i$, not derivative formula.  
D) ✓ Denominator power 2 corresponds to first derivative.

**Correct:** A, B, D


#### 9. Which of the following statements about power series operations are correct?  
A) ✓ Sum converges within intersection of radii.  
B) ✓ Product given by Cauchy product of coefficients.  
C) ✓ Radius of product series is at least minimum of two radii.  
D) ✗ Derivative of power series is also a power series with same radius.

**Correct:** A, B, C


#### 10. Suppose $f(z) = \sum a_n (z - \alpha)^n$ and $g(z) = \sum b_n (z - \alpha)^n$ have radii $r_1, r_2$. Which are true?  
A) ✓ Sum converges on disk with radius minimum of $r_1, r_2$.  
B) ✓ Product converges on disk with radius minimum of $r_1, r_2$.  
C) ✓ Coefficients of product given by Cauchy product formula.  
D) ✗ Radius of sum is not necessarily maximum; minimum is guaranteed.

**Correct:** A, B, C


#### 11. Which of the following are true about the convergence of the geometric series $\sum z^n$?  
A) ✓ Converges pointwise for $|z| < 1$.  
B) ✓ Converges uniformly on any closed disk $|z| \leq r < 1$.  
C) ✗ Does not converge uniformly on unit circle $|z|=1$.  
D) ✓ Diverges for $|z| > 1$.

**Correct:** A, B, D


#### 12. Which of the following statements about the uniqueness of power series representations are correct?  
A) ✓ If two power series agree on a disk, coefficients are identical.  
B) ✗ A function cannot have two distinct power series in same disk.  
C) ✓ Taylor series is unique power series representation around center.  
D) ✓ Uniqueness fails if function is not analytic (no power series).

**Correct:** A, C, D


#### 13. Consider $f(z) = \frac{\cos z - 1}{z^4}$. Which are true about its Laurent series around 0?  
A) ✓ Laurent series contains negative powers due to division by $z^4$.  
B) ✓ Principal part is finite because numerator’s Taylor series starts at $z^2$.  
C) ✗ Function is not analytic at 0 due to singularity.  
D) ✓ Laurent series obtained by dividing Taylor series of numerator by $z^4$.

**Correct:** A, B, D


#### 14. Which of the following are true about the relationship between analytic functions and power series?  
A) ✓ Every analytic function can be locally represented by a power series.  
B) ✗ Power series do not always converge on entire complex plane.  
C) ✓ Analyticity implies infinite differentiability.  
D) ✗ Not every infinitely differentiable function is analytic.

**Correct:** A, C


#### 15. Which of the following statements about uniform convergence of sequences of functions are true?  
A) ✓ Uniform convergence allows interchange of limit and integration.  
B) ✓ Uniform limit of continuous functions is continuous.  
C) ✗ Pointwise convergence alone does not guarantee interchange of limit and integral.  
D) ✗ Uniform convergence does not depend on point $z$, unlike pointwise.

**Correct:** A, B


#### 16. Which of the following are true about the annulus $A(r, R, \alpha)$ where a Laurent series converges?  
A) ✓ Annulus degenerates to disk if $r=0$.  
B) ✗ Convergence on boundary circles is not guaranteed; may fail.  
C) ✓ Annulus is region between two concentric circles centered at $\alpha$.  
D) ✗ Outer radius $R$ can be infinite; not necessarily finite.

**Correct:** A, C


#### 17. Which of the following are true about the coefficients $c_n$ of a Laurent series?  
A) ✓ Computed by contour integrals involving $(z - \alpha)^{-(n+1)}$.  
B) ✓ Negative $n$ coefficients form principal part.  
C) ✗ Coefficients $c_n$ for $n \geq 0$ need not be zero if singularity exists.  
D) ✓ Coefficients are unique for given function and annulus.

**Correct:** A, B, D


#### 18. Which of the following statements about derivatives of functions represented by power or Laurent series are true?  
A) ✓ Derivative of power series obtained by term-wise differentiation inside radius.  
B) ✓ Derivative of Laurent series obtained term-wise inside annulus.  
C) ✗ Term-wise differentiation does not change radius of convergence.  
D) ✗ Term-wise differentiation is valid for Laurent series.

**Correct:** A, B


#### 19. Which of the following are true about the integral $\int_C \frac{e^{z^2}}{(z - z_0)^3} dz$ where $C$ is a circle around $z_0$?  
A) ✓ Can be evaluated using Cauchy's formula for second derivative.  
B) ✓ Integral equals $\frac{2\pi i}{2!} f^{(2)}(z_0)$.  
C) ✗ Integral does not depend on radius as long as $C$ encloses $z_0$.  
D) ✗ Integral is not zero if $f$ is analytic inside $C$.

**Correct:** A, B


#### 20. Which of the following are true about the convergence of Laurent series on closed sub-annuli?  
A) ✓ Laurent series converge uniformly on any closed sub-annulus inside annulus.  
B) ✗ Uniform convergence may fail on boundary circles.  
C) ✓ Uniform convergence implies continuity of sum function on closed sub-annulus.  
D) ✗ Laurent series converge uniformly, not just pointwise, on sub-annuli.

**Correct:** A, C