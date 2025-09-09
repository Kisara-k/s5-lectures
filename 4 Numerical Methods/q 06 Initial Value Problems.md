## Initial Value Problems

## Questions

#### 1. Which of the following statements about an Initial Value Problem (IVP) are true?  
A) An IVP consists of a differential equation and initial conditions specifying the function and its derivatives at a starting point.  
B) The initial values must always include the function value and all its derivatives up to the order of the differential equation.  
C) IVPs always have closed-form analytical solutions.  
D) Numerical methods are often necessary because many IVPs cannot be solved analytically.


#### 2. A function $f(t, y)$ satisfies a Lipschitz condition on a set $D$ if:  
A) There exists a constant $L > 0$ such that $|f(t, y_1) - f(t, y_2)| \leq L |y_1 - y_2|$ for all $(t, y_1), (t, y_2) \in D$.  
B) $f$ is differentiable with respect to $t$ on $D$.  
C) $f$ is continuous on $D$ and its partial derivative with respect to $y$ is bounded.  
D) $f$ is convex on $D$.


#### 3. Which of the following sets is convex?  
A) The set $D = \{(t, y) \mid t \in [0,1], y \in [-1,1]\}$.  
B) The set $D = \{(t, y) \mid y = t^2, t \in [0,1]\}$.  
C) The set $D = \{(t, y) \mid t^2 + y^2 \leq 1\}$.  
D) The set $D = \{(t, y) \mid y \geq |t|\}$.


#### 4. The Existence and Uniqueness Theorem for IVPs requires which of the following conditions?  
A) $f(t, y)$ must be continuous on a convex set $D$.  
B) $f(t, y)$ must satisfy a Lipschitz condition in $y$ on $D$.  
C) The initial value $y(a)$ must be zero.  
D) The domain $D$ must be bounded.


#### 5. What does it mean for an IVP to be well-posed?  
A) It has a unique solution.  
B) Small changes in initial conditions or the function $f$ cause only small changes in the solution.  
C) The solution can be expressed in closed form.  
D) The solution is stable under perturbations in the differential equation and initial values.


#### 6. Which of the following statements about Euler’s method are correct?  
A) Euler’s method approximates the solution at discrete mesh points, not continuously.  
B) The step size $h$ is defined as $\frac{b-a}{N}$ where $N$ is the number of steps.  
C) Euler’s method uses a second-order Taylor expansion to approximate the solution.  
D) The error in Euler’s method is proportional to the first power of $h$.


#### 7. Regarding the error bounds of Euler’s method, which are true?  
A) The theoretical error bound depends on the Lipschitz constant $L$ and the bound on the second derivative of the solution.  
B) The actual error is always equal to the theoretical error bound.  
C) Rounding errors can become significant as $h$ becomes very small.  
D) Decreasing $h$ indefinitely always decreases the total error.


#### 8. Runge-Kutta methods improve on Euler’s method by:  
A) Using multiple evaluations of $f(t, y)$ within each step.  
B) Requiring the computation of derivatives of $f$ with respect to $t$.  
C) Eliminating the need for derivative computations by approximating higher-order terms with function evaluations.  
D) Being explicit multi-step methods.


#### 9. The Midpoint method (a second-order Runge-Kutta method) approximates the solution by:  
A) Using the slope at the beginning of the interval only.  
B) Using the slope at the midpoint of the interval estimated from the initial slope.  
C) Averaging the slopes at the beginning and end of the interval.  
D) Using four slope evaluations per step.


#### 10. Which of the following statements about the fourth-order Runge-Kutta method are true?  
A) It requires four function evaluations per step.  
B) It has a local truncation error of order $h^5$.  
C) It is more accurate than Euler’s method for the same step size.  
D) It is an implicit method.


#### 11. Multi-step methods differ from one-step methods because:  
A) They use multiple previous approximations to compute the next value.  
B) They always require solving implicit equations.  
C) They can be explicit or implicit depending on the coefficients.  
D) They do not require initial values.


#### 12. In the general multi-step method formula, if the coefficient $b_m = 0$, the method is:  
A) Explicit, because $w_{i+1}$ can be computed directly.  
B) Implicit, because $w_{i+1}$ appears on both sides of the equation.  
C) Unstable for all IVPs.  
D) Requires solving nonlinear equations at each step.


#### 13. Adams-Bashforth methods are:  
A) Explicit multi-step methods.  
B) Implicit multi-step methods.  
C) Based on polynomial interpolation of $f(t, y)$ at previous points.  
D) Always more accurate than Adams-Moulton methods of the same step number.


#### 14. Adams-Moulton methods are:  
A) Implicit multi-step methods.  
B) Explicit multi-step methods.  
C) Used as correctors in predictor-corrector schemes.  
D) Require solving for $w_{i+1}$ at each step.


#### 15. Predictor-corrector methods:  
A) Use an explicit method to predict the next value.  
B) Use an implicit method to correct the predicted value.  
C) Always guarantee exact solutions.  
D) Can improve accuracy without significantly increasing computational cost.


#### 16. For a system of IVPs, the Lipschitz condition:  
A) Must hold for each component function $f_j$ with respect to all variables $u_1, u_2, ..., u_m$.  
B) Is not necessary for existence and uniqueness of solutions.  
C) Can be verified by checking boundedness of partial derivatives of $f_j$.  
D) Is only required for scalar IVPs.


#### 17. When converting a higher-order IVP into a system of first-order IVPs:  
A) New variables are introduced to represent derivatives of the original function.  
B) The order of the system equals the order of the original IVP.  
C) The system can be solved using methods for first-order systems.  
D) This conversion is only possible for linear differential equations.


#### 18. Which of the following are true about the stability and error behavior of numerical methods for IVPs?  
A) Well-posedness of the IVP ensures numerical stability under small perturbations.  
B) Euler’s method has global error proportional to $h$.  
C) Runge-Kutta methods can have errors that grow exponentially with the number of steps.  
D) Multi-step methods always have smaller errors than one-step methods.


#### 19. Which of the following statements about the use of mesh points in numerical methods are correct?  
A) Mesh points are usually chosen to be equally spaced in the interval $[a, b]$.  
B) The solution is approximated only at mesh points, and values between points require interpolation.  
C) The step size $h$ can vary arbitrarily between mesh points in Euler’s method.  
D) Smaller step sizes always guarantee better approximations without exception.


#### 20. Regarding the computational cost and accuracy trade-offs in numerical methods for IVPs:  
A) Higher-order methods like fourth-order Runge-Kutta require more function evaluations per step but provide better accuracy.  
B) Multi-step methods reduce the number of function evaluations per step by reusing previous information.  
C) Implicit methods are generally easier to implement than explicit methods.  
D) Predictor-corrector methods combine the advantages of explicit and implicit methods to balance accuracy and computational effort.



<br>

## Answers

#### 1. Which of the following statements about an Initial Value Problem (IVP) are true?  
A) ✓ An IVP consists of a differential equation and initial conditions specifying the function and its derivatives at a starting point.  
B) ✗ Initial values do not always include all derivatives up to the order; only the necessary initial conditions are given.  
C) ✗ Many IVPs cannot be solved analytically, so this is false.  
D) ✓ Numerical methods are often necessary because many IVPs cannot be solved analytically.

**Correct:** A, D


#### 2. A function $f(t, y)$ satisfies a Lipschitz condition on a set $D$ if:  
A) ✓ This is the formal definition of the Lipschitz condition in $y$.  
B) ✗ Differentiability with respect to $t$ is not required for Lipschitz in $y$.  
C) ✓ Bounded partial derivative with respect to $y$ implies Lipschitz condition.  
D) ✗ Convexity is unrelated to Lipschitz condition.

**Correct:** A, C


#### 3. Which of the following sets is convex?  
A) ✓ A rectangle in $\mathbb{R}^2$ is convex.  
B) ✗ A parabola curve is not convex as a set (it’s a curve, not a filled region).  
C) ✓ A disk (circle and interior) is convex.  
D) ✗ The set $y \geq |t|$ forms a "V" shape, which is convex, but since it includes all points above, it is convex. (Tricky) Actually, this set is convex because any line segment between two points above the "V" lies above it. So this is ✓.

**Correct:** A, C, D


#### 4. The Existence and Uniqueness Theorem for IVPs requires which of the following conditions?  
A) ✓ Continuity on a convex set is required.  
B) ✓ Lipschitz condition in $y$ is required.  
C) ✗ Initial value does not have to be zero.  
D) ✗ The domain does not have to be bounded.

**Correct:** A, B


#### 5. What does it mean for an IVP to be well-posed?  
A) ✓ Unique solution exists.  
B) ✓ Small changes in initial data cause small changes in solution.  
C) ✗ Closed form solution is not required for well-posedness.  
D) ✓ Stability under perturbations is part of well-posedness.

**Correct:** A, B, D


#### 6. Which of the following statements about Euler’s method are correct?  
A) ✓ Euler’s method approximates solution only at discrete mesh points.  
B) ✓ Step size $h$ is defined as $\frac{b-a}{N}$.  
C) ✗ Euler’s method uses first-order Taylor approximation, not second-order.  
D) ✓ Error is proportional to $h$ (order 1).

**Correct:** A, B, D


#### 7. Regarding the error bounds of Euler’s method, which are true?  
A) ✓ Theoretical error bound depends on Lipschitz constant and second derivative bound.  
B) ✗ Actual error is usually smaller than the theoretical bound.  
C) ✓ Rounding errors become significant as $h$ decreases.  
D) ✗ Decreasing $h$ indefinitely can increase rounding errors, so total error may not always decrease.

**Correct:** A, C


#### 8. Runge-Kutta methods improve on Euler’s method by:  
A) ✓ Using multiple evaluations of $f$ per step.  
B) ✗ They avoid computing derivatives of $f$ with respect to $t$.  
C) ✓ Replace derivatives with function evaluations at selected points.  
D) ✗ Runge-Kutta methods are one-step, not multi-step.

**Correct:** A, C


#### 9. The Midpoint method (a second-order Runge-Kutta method) approximates the solution by:  
A) ✗ Uses more than just the slope at the beginning.  
B) ✓ Uses slope at midpoint estimated from initial slope.  
C) ✗ Averaging slopes is Modified Euler, not Midpoint method.  
D) ✗ Four slope evaluations per step is fourth-order Runge-Kutta.

**Correct:** B


#### 10. Which of the following statements about the fourth-order Runge-Kutta method are true?  
A) ✓ Requires four function evaluations per step.  
B) ✓ Local truncation error is order $h^5$ (global error order $h^4$).  
C) ✓ More accurate than Euler’s method for same $h$.  
D) ✗ It is an explicit method, not implicit.

**Correct:** A, B, C


#### 11. Multi-step methods differ from one-step methods because:  
A) ✓ Use multiple previous approximations.  
B) ✗ Not all multi-step methods are implicit; some are explicit.  
C) ✓ Can be explicit or implicit depending on coefficients.  
D) ✗ Initial values are required to start the method.

**Correct:** A, C


#### 12. In the general multi-step method formula, if the coefficient $b_m = 0$, the method is:  
A) ✓ Explicit, since $w_{i+1}$ can be computed directly.  
B) ✗ Implicit requires $b_m \neq 0$.  
C) ✗ Stability depends on method and problem, not just $b_m$.  
D) ✗ Explicit methods do not require solving nonlinear equations.

**Correct:** A


#### 13. Adams-Bashforth methods are:  
A) ✓ Explicit multi-step methods.  
B) ✗ They are not implicit.  
C) ✓ Based on polynomial interpolation of $f$ at previous points.  
D) ✗ Adams-Moulton methods are generally more accurate for same step number.

**Correct:** A, C


#### 14. Adams-Moulton methods are:  
A) ✓ Implicit multi-step methods.  
B) ✗ Not explicit.  
C) ✓ Often used as correctors in predictor-corrector schemes.  
D) ✓ Require solving for $w_{i+1}$ at each step.

**Correct:** A, C, D


#### 15. Predictor-corrector methods:  
A) ✓ Use explicit method to predict next value.  
B) ✓ Use implicit method to correct predicted value.  
C) ✗ Do not guarantee exact solutions, only better approximations.  
D) ✓ Improve accuracy without large computational cost increase.

**Correct:** A, B, D


#### 16. For a system of IVPs, the Lipschitz condition:  
A) ✓ Must hold for each component with respect to all variables.  
B) ✗ Necessary for existence and uniqueness.  
C) ✓ Can be checked via bounded partial derivatives.  
D) ✗ Lipschitz condition applies to systems, not only scalars.

**Correct:** A, C


#### 17. When converting a higher-order IVP into a system of first-order IVPs:  
A) ✓ New variables represent derivatives of the original function.  
B) ✓ The system order equals the original IVP order.  
C) ✓ The system can be solved by first-order methods.  
D) ✗ Conversion applies to nonlinear and linear equations alike.

**Correct:** A, B, C


#### 18. Which of the following are true about the stability and error behavior of numerical methods for IVPs?  
A) ✓ Well-posedness ensures stability under small perturbations.  
B) ✓ Euler’s method global error is proportional to $h$.  
C) ✗ Runge-Kutta errors do not necessarily grow exponentially; depends on problem.  
D) ✗ Multi-step methods are not always more accurate than one-step methods.

**Correct:** A, B


#### 19. Which of the following statements about the use of mesh points in numerical methods are correct?  
A) ✓ Mesh points are usually equally spaced.  
B) ✓ Solutions are approximated at mesh points; interpolation needed between points.  
C) ✗ Euler’s method typically uses fixed step size $h$. Variable step size is possible but not standard.  
D) ✗ Smaller step size usually improves accuracy but not always due to rounding errors.

**Correct:** A, B


#### 20. Regarding the computational cost and accuracy trade-offs in numerical methods for IVPs:  
A) ✓ Higher-order methods require more function evaluations but yield better accuracy.  
B) ✓ Multi-step methods reuse previous info, reducing function evaluations per step.  
C) ✗ Implicit methods are generally harder to implement than explicit methods.  
D) ✓ Predictor-corrector methods balance accuracy and computational effort.

**Correct:** A, B, D