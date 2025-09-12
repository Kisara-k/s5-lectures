## 8. Limits and Differentiation of Functions of a Complex Variable

## Questions

#### 1. Which of the following statements about a function $f(z) = u(x,y) + i v(x,y)$ of a complex variable $z = x + iy$ are true?  
A) $u$ and $v$ are always real-valued functions of two real variables $x$ and $y$.  
B) $f(z)$ can be expressed in terms of polar coordinates $(r, \theta)$ as $u(r, \theta) + i v(r, \theta)$.  
C) The domain of $f$ must be a subset of the real numbers.  
D) The value of $f$ at $z$ is always a real number.


#### 2. Consider the mapping $\omega = f(z) = i z$. Which of the following geometric transformations does this represent?  
A) Translation by one unit to the right.  
B) Rotation by 90 degrees counterclockwise about the origin.  
C) Reflection about the real axis.  
D) Scaling by a factor of $i$.


#### 3. The limit $\lim_{z \to z_0} f(z) = \omega_0$ means:  
A) For every $\epsilon > 0$, there exists $\delta > 0$ such that if $|z - z_0| < \delta$, then $|f(z) - \omega_0| < \epsilon$.  
B) $f(z)$ equals $\omega_0$ at $z = z_0$.  
C) $f(z)$ can be made arbitrarily close to $\omega_0$ by choosing $z$ close to but not equal to $z_0$.  
D) The limit is unique if it exists.


#### 4. Which of the following functions does **not** have a limit as $z \to 0$?  
A) $f(z) = \frac{z}{\bar{z}}$  
B) $f(z) = z^2$  
C) $f(z) = \frac{i z}{2}$  
D) $f(z) = e^z$


#### 5. If $f$ is continuous at $z_0$, which of the following must be true?  
A) $\lim_{z \to z_0} f(z)$ exists.  
B) $f(z_0)$ is defined.  
C) $\lim_{z \to z_0} f(z) = f(z_0)$.  
D) $f$ is differentiable at $z_0$.


#### 6. Suppose $f(z)$ is continuous and non-zero at $z_0$. Which of the following statements is true?  
A) $f(z) \neq 0$ for all $z$ in some neighborhood of $z_0$.  
B) $f(z)$ can be zero arbitrarily close to $z_0$.  
C) $f(z)$ must be analytic at $z_0$.  
D) $|f(z)|$ is bounded away from zero near $z_0$.


#### 7. The derivative of $f(z) = z^n$ for a positive integer $n$ is:  
A) $n z^{n-1}$  
B) $z^{n+1}$  
C) $n z^n$  
D) Does not exist for $n > 1$


#### 8. Which of the following functions is **not** differentiable anywhere in the complex plane?  
A) $f(z) = z^2$  
B) $f(z) = \bar{z}$  
C) $f(z) = e^z$  
D) $f(z) = \sin z$


#### 9. The Cauchy-Riemann equations at a point $z_0 = x_0 + i y_0$ are:  
A) $u_x = v_y$ and $u_y = -v_x$  
B) $u_x = -v_y$ and $u_y = v_x$  
C) $u_x = u_y$ and $v_x = v_y$  
D) $u_x = v_x$ and $u_y = v_y$


#### 10. If $f(z) = u(x,y) + i v(x,y)$ satisfies the Cauchy-Riemann equations at $z_0$ and the partial derivatives are continuous there, then:  
A) $f$ is differentiable at $z_0$.  
B) $f$ is analytic in some neighborhood of $z_0$.  
C) $f'(z_0) = u_x(x_0,y_0) + i v_x(x_0,y_0)$.  
D) $f$ must be constant near $z_0$.


#### 11. Which of the following is a necessary condition for $f$ to be analytic at $z_0$?  
A) $f$ is differentiable at $z_0$.  
B) $f$ is differentiable in some neighborhood of $z_0$.  
C) $f$ satisfies the Cauchy-Riemann equations at $z_0$.  
D) $f$ is continuous at $z_0$.


#### 12. For the function $f(z) = |z|^2 = x^2 + y^2$, which of the following is true?  
A) $f$ is differentiable everywhere in $\mathbb{C}$.  
B) $f$ is continuous everywhere but not complex differentiable anywhere except possibly at 0.  
C) $f'(z) = 2z$.  
D) $f$ satisfies the Cauchy-Riemann equations only at $z=0$.


#### 13. The polar form of the Cauchy-Riemann equations is:  
A) $r u_r = v_\theta$ and $u_\theta = -r v_r$  
B) $u_r = r v_\theta$ and $v_r = -u_\theta$  
C) $u_r = v_r$ and $u_\theta = v_\theta$  
D) $r u_\theta = v_r$ and $u_r = -r v_\theta$


#### 14. If $f$ is analytic on an open set $G$, which of the following must hold?  
A) $f'$ is continuous on $G$.  
B) $f$ is differentiable only at isolated points in $G$.  
C) $f$ satisfies the Cauchy-Riemann equations everywhere in $G$.  
D) $f$ is constant on $G$.


#### 15. Which of the following statements about limits in complex analysis is false?  
A) The limit of a function at a point, if it exists, is unique.  
B) The limit depends on the path taken to approach the point.  
C) If the limit exists, the function must be continuous at that point.  
D) The limit can be evaluated by considering the limits of the real and imaginary parts separately.


#### 16. Consider $f(z) = \frac{z}{\bar{z}}$ for $z \neq 0$. Which of the following is true?  
A) $\lim_{z \to 0} f(z)$ exists and equals 1.  
B) $\lim_{z \to 0} f(z)$ does not exist because it depends on the direction of approach.  
C) $f$ is continuous everywhere except at $z=0$.  
D) $f$ is differentiable everywhere except at $z=0$.


#### 17. If $f$ is differentiable at $z_0$, then which of the following must be true?  
A) $f$ is continuous at $z_0$.  
B) $f$ satisfies the Cauchy-Riemann equations at $z_0$.  
C) $f$ is analytic at $z_0$.  
D) $f$ has a derivative at every point in some neighborhood of $z_0$.


#### 18. Which of the following mappings corresponds to a reflection about the real axis?  
A) $\omega = z + 1$  
B) $\omega = i z$  
C) $\omega = \bar{z}$  
D) $\omega = -z$


#### 19. The inverse image of a point $\omega_0$ under a function $f$ is:  
A) The set of all points $z$ such that $f(z) = \omega_0$.  
B) The image of the domain under $f$.  
C) The set of points where $f$ is not defined.  
D) The set of points where $f$ is differentiable.


#### 20. Suppose $f(z) = u(r, \theta) + i v(r, \theta)$ satisfies the polar Cauchy-Riemann equations at $z_0 = r_0 e^{i \theta_0}$. Then the derivative $f'(z_0)$ is given by:  
A) $e^{i \theta_0} (u_r + i v_r)$  
B) $e^{-i \theta_0} (u_r + i v_r)$  
C) $u_r + i v_r$  
D) $r_0 (u_\theta + i v_\theta)$



<br>

## Answers

#### 1. Which of the following statements about a function $f(z) = u(x,y) + i v(x,y)$ of a complex variable $z = x + iy$ are true?  
A) ✓ $u$ and $v$ are real-valued functions of two real variables $x$ and $y$.  
B) ✓ $f(z)$ can be expressed in polar coordinates as $u(r, \theta) + i v(r, \theta)$.  
C) ✗ The domain of $f$ is a subset of complex numbers, not just real numbers.  
D) ✗ The value of $f$ is generally complex, not always real.

**Correct:** A, B


#### 2. Consider the mapping $\omega = f(z) = i z$. Which of the following geometric transformations does this represent?  
A) ✗ Translation moves points, but multiplication by $i$ rotates.  
B) ✓ Multiplying by $i$ rotates points by 90° counterclockwise.  
C) ✗ Reflection about the real axis is conjugation, not multiplication by $i$.  
D) ✗ $i$ is a complex number with magnitude 1, so it does not scale but rotates.

**Correct:** B


#### 3. The limit $\lim_{z \to z_0} f(z) = \omega_0$ means:  
A) ✗ The condition must exclude $z = z_0$ (deleted neighborhood).  
B) ✗ The limit concerns values near $z_0$, not necessarily the value at $z_0$.  
C) ✓ Correct definition: $f(z)$ approaches $\omega_0$ as $z \to z_0$, $z \neq z_0$.  
D) ✓ The limit, if it exists, is unique.

**Correct:** C, D


#### 4. Which of the following functions does **not** have a limit as $z \to 0$?  
A) ✓ $\frac{z}{\bar{z}}$ limit depends on direction, so does not exist.  
B) ✗ $z^2$ limit at 0 is 0, exists.  
C) ✗ $\frac{i z}{2}$ limit at 0 is 0, exists.  
D) ✗ $e^z$ is entire, limit at 0 is 1, exists.

**Correct:** A


#### 5. If $f$ is continuous at $z_0$, which of the following must be true?  
A) ✓ Limit exists at $z_0$.  
B) ✓ $f(z_0)$ is defined.  
C) ✓ Limit equals function value.  
D) ✗ Continuity does not imply differentiability.

**Correct:** A, B, C


#### 6. Suppose $f(z)$ is continuous and non-zero at $z_0$. Which of the following statements is true?  
A) ✓ By continuity and non-zero value, $f(z) \neq 0$ in some neighborhood.  
B) ✗ Contradicts continuity and non-zero at $z_0$.  
C) ✗ Non-zero and continuous does not guarantee analyticity.  
D) ✓ $|f(z)|$ is bounded away from zero near $z_0$.

**Correct:** A, D


#### 7. The derivative of $f(z) = z^n$ for a positive integer $n$ is:  
A) ✓ Standard power rule applies: $n z^{n-1}$.  
B) ✗ Incorrect power.  
C) ✗ Incorrect coefficient.  
D) ✗ Derivative exists for all positive integers.

**Correct:** A


#### 8. Which of the following functions is **not** differentiable anywhere in the complex plane?  
A) ✗ $z^2$ is entire (differentiable everywhere).  
B) ✓ $\bar{z}$ is not complex differentiable anywhere.  
C) ✗ $e^z$ is entire.  
D) ✗ $\sin z$ is entire.

**Correct:** B


#### 9. The Cauchy-Riemann equations at a point $z_0 = x_0 + i y_0$ are:  
A) ✓ Correct form of Cauchy-Riemann equations.  
B) ✗ Signs reversed, incorrect.  
C) ✗ Not related to Cauchy-Riemann.  
D) ✗ Not related to Cauchy-Riemann.

**Correct:** A


#### 10. If $f(z) = u(x,y) + i v(x,y)$ satisfies the Cauchy-Riemann equations at $z_0$ and the partial derivatives are continuous there, then:  
A) ✓ Sufficient condition for differentiability at $z_0$.  
B) ✗ Differentiability at a point does not guarantee analyticity in a neighborhood.  
C) ✓ Formula for derivative at $z_0$.  
D) ✗ No requirement that $f$ be constant.

**Correct:** A, C


#### 11. Which of the following is a necessary condition for $f$ to be analytic at $z_0$?  
A) ✗ Differentiability at a single point is not enough for analyticity.  
B) ✓ Differentiability in a neighborhood is required.  
C) ✓ Cauchy-Riemann equations must hold at $z_0$.  
D) ✗ Continuity alone is not sufficient.

**Correct:** B, C


#### 12. For the function $f(z) = |z|^2 = x^2 + y^2$, which of the following is true?  
A) ✗ Not complex differentiable anywhere except possibly at 0.  
B) ✓ Continuous everywhere but not complex differentiable except possibly at 0.  
C) ✗ Derivative does not exist as complex derivative.  
D) ✗ Does not satisfy Cauchy-Riemann anywhere except trivial point.

**Correct:** B


#### 13. The polar form of the Cauchy-Riemann equations is:  
A) ✓ Correct polar form.  
B) ✗ Incorrect rearrangement.  
C) ✗ Incorrect equalities.  
D) ✗ Incorrect relations.

**Correct:** A


#### 14. If $f$ is analytic on an open set $G$, which of the following must hold?  
A) ✓ $f'$ is continuous on $G$.  
B) ✗ Differentiable everywhere, not just isolated points.  
C) ✓ Cauchy-Riemann equations hold everywhere in $G$.  
D) ✗ $f$ need not be constant.

**Correct:** A, C


#### 15. Which of the following statements about limits in complex analysis is false?  
A) ✓ Limit uniqueness is true.  
B) ✗ Limit must be independent of path; if it depends on path, limit does not exist.  
C) ✓ Limit existence does not guarantee continuity; function value must match limit for continuity.  
D) ✓ Limit can be evaluated by limits of real and imaginary parts.

**Correct:** B


#### 16. Consider $f(z) = \frac{z}{\bar{z}}$ for $z \neq 0$. Which of the following is true?  
A) ✗ Limit does not exist at 0.  
B) ✓ Limit depends on direction, so does not exist.  
C) ✓ Continuous everywhere except at 0.  
D) ✗ Not differentiable anywhere.

**Correct:** B, C


#### 17. If $f$ is differentiable at $z_0$, then which of the following must be true?  
A) ✓ Differentiability implies continuity.  
B) ✓ Cauchy-Riemann equations hold at $z_0$.  
C) ✗ Differentiability at a point does not imply analyticity there.  
D) ✗ Analyticity requires differentiability in a neighborhood, not just at a point.

**Correct:** A, B


#### 18. Which of the following mappings corresponds to a reflection about the real axis?  
A) ✗ Translation, not reflection.  
B) ✗ Rotation, not reflection.  
C) ✓ Complex conjugation reflects about the real axis.  
D) ✗ Negation is rotation by 180°, not reflection.

**Correct:** C


#### 19. The inverse image of a point $\omega_0$ under a function $f$ is:  
A) ✓ Set of all $z$ such that $f(z) = \omega_0$.  
B) ✗ Image is the set of all outputs, not inverse image.  
C) ✗ Points where $f$ is undefined are not inverse images.  
D) ✗ Differentiability is unrelated to inverse image.

**Correct:** A


#### 20. Suppose $f(z) = u(r, \theta) + i v(r, \theta)$ satisfies the polar Cauchy-Riemann equations at $z_0 = r_0 e^{i \theta_0}$. Then the derivative $f'(z_0)$ is given by:  
A) ✗ Incorrect sign in exponent.  
B) ✓ Correct formula with $e^{-i \theta_0}$.  
C) ✗ Missing rotation factor $e^{-i \theta_0}$.  
D) ✗ Incorrect expression involving $u_\theta, v_\theta$.

**Correct:** B