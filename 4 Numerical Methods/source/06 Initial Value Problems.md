## Initial Value Problems

[Study Notes](#study-notes)

[Questions](#questions)



### Key Points

#### 1. 📐 Lipschitz Condition  
- A function \(f(t, y)\) satisfies a Lipschitz condition in \(y\) on a set \(D\) if there exists a constant \(L > 0\) such that \(|f(t, y_1) - f(t, y_2)| \leq L |y_1 - y_2|\) for all \((t, y_1), (t, y_2) \in D\).  
- The constant \(L\) is called the Lipschitz constant.  
- If \(f\) and its partial derivatives are continuous on \(D\), then \(f\) satisfies a Lipschitz condition on \(D\).

#### 2. 🔷 Convex Sets  
- A set \(D \subset \mathbb{R}^2\) is convex if for any two points \((t_1, y_1)\) and \((t_2, y_2)\) in \(D\), the line segment \(((1-\lambda)t_1 + \lambda t_2, (1-\lambda)y_1 + \lambda y_2)\) is also in \(D\) for all \(\lambda \in [0,1]\).

#### 3. ✅ Existence and Uniqueness Theorem for IVPs  
- If \(f(t, y)\) is continuous on a convex set \(D = [a,b] \times \mathbb{R}\) and satisfies a Lipschitz condition in \(y\), then the IVP \(y' = f(t,y), y(a) = y_0\) has a unique solution on \([a,b]\).

#### 4. 🔒 Well-Posedness of IVPs  
- An IVP is well-posed if:  
  1. A unique solution exists.  
  2. Small perturbations in the initial data or function \(f\) cause only small bounded changes in the solution.  
- If \(f\) is continuous and satisfies a Lipschitz condition on \(D\), then the IVP is well-posed.

#### 5. 🧮 Euler’s Method  
- Approximates solutions at discrete mesh points \(t_i = a + ih\), where \(h = \frac{b-a}{N}\).  
- Recursive formula: \(w_{i+1} = w_i + h f(t_i, w_i)\).  
- Euler’s method has a local truncation error of order \(h^2\) and a global error of order \(h\) (first order method).  
- Error bound depends on the Lipschitz constant \(L\) and the bound on the second derivative of the true solution.

#### 6. 🚀 Runge-Kutta Methods  
- Use multiple evaluations of \(f\) per step to achieve higher accuracy without computing derivatives of \(f\).  
- Midpoint method (2nd order): uses slope at midpoint for better approximation.  
- Modified Euler method (2nd order): averages slopes at start and end of interval.  
- Fourth order Runge-Kutta method: uses four slope evaluations per step, with global error order \(h^4\).

#### 7. 🔄 Multi-Step Methods  
- Use multiple previous approximations \(w_i, w_{i-1}, ..., w_{i-m+1}\) to compute \(w_{i+1}\).  
- Explicit multi-step methods: \(w_{i+1}\) defined explicitly in terms of previous values (e.g., Adams-Bashforth).  
- Implicit multi-step methods: \(w_{i+1}\) appears on both sides of the equation (e.g., Adams-Moulton).

#### 8. ✏️ Adams Methods  
- Adams-Bashforth methods are explicit multi-step methods with local error order \(O(h^{m+1})\) for \(m\)-step methods.  
- Adams-Moulton methods are implicit multi-step methods with local error order \(O(h^{m+2})\) for \(m\)-step methods.  
- Adams-Bashforth \(m\)-step and Adams-Moulton \((m-1)\)-step methods have similar computational cost and error order.

#### 9. 🔄 Predictor-Corrector Methods  
- Combine explicit (predictor) and implicit (corrector) methods to improve accuracy.  
- Step 1: Use explicit method to predict \(w_{i+1,p}\).  
- Step 2: Use implicit method with \(w_{i+1,p}\) to correct and find \(w_{i+1}\).

#### 10. 🧮 Numerical Solutions for Systems of IVPs  
- Systems of first-order IVPs have the form \(u_j' = f_j(t, u_1, ..., u_m)\) with initial conditions \(u_j(a) = \alpha_j\).  
- If each \(f_j\) is continuous and satisfies a Lipschitz condition, the system has a unique solution.  
- Runge-Kutta methods extend to systems by applying the method component-wise.

#### 11. 🔄 Converting Higher-Order IVPs to Systems  
- An \(m\)-th order IVP can be rewritten as a system of \(m\) first-order IVPs by introducing new variables for derivatives.  
- Example: For \(y'' = g(t, y, y')\), define \(u_1 = y\), \(u_2 = y'\), then system is \(u_1' = u_2\), \(u_2' = g(t, u_1, u_2)\).



<br>

## Study Notes

### 1. 🧩 Introduction to Initial Value Problems (IVPs)

When studying how things change over time, such as the swinging of a pendulum, we often use **differential equations**. These equations describe how a quantity changes at any moment. For example, the angle \(\theta(t)\) of a pendulum at time \(t\) can be described by a differential equation.

An **Initial Value Problem (IVP)** is a differential equation together with specific starting information — the initial values. For the pendulum, this means knowing the initial angle \(\theta(0)\) and the initial speed \(\theta'(0)\) at the start time \(t=0\).

- The differential equation tells us how \(\theta(t)\) changes.
- The initial values tell us where the motion starts.

Together, these form an IVP: find the function \(\theta(t)\) that satisfies the differential equation and matches the initial conditions.

**Why IVPs matter:** Many real-world problems are modeled as IVPs. However, most IVPs cannot be solved exactly with formulas (analytically). Instead, we use **numerical methods** to approximate solutions.


### 2. 📏 Theory Behind IVPs: Existence, Uniqueness, and Well-Posedness

Before approximating solutions, it’s important to know if a solution exists, if it’s unique, and if the problem is stable (well-posed).

#### Lipschitz Condition

A key concept is the **Lipschitz condition**, which controls how fast the function \(f(t, y)\) (from the differential equation \(y' = f(t, y)\)) can change with respect to \(y\).

- A function \(f(t, y)\) satisfies a **Lipschitz condition** if there is a constant \(L > 0\) such that for any two values \(y_1\) and \(y_2\), the difference in \(f\) values is at most \(L\) times the difference in \(y\) values.
- Intuitively, this means \(f\) doesn’t change too wildly as \(y\) changes.

#### Convex Sets

A set \(D\) in the plane is **convex** if, whenever you pick two points in \(D\), the entire line segment between them is also inside \(D\). This property is important for applying certain theorems about IVPs.

#### Existence and Uniqueness Theorem

If \(f(t, y)\) is continuous and satisfies the Lipschitz condition on a convex set \(D\), then the IVP has a **unique solution** on the interval \([a, b]\).

- This means the problem is well-defined: there is one and only one function \(y(t)\) that fits the differential equation and initial values.

#### Well-Posed Problems

A problem is **well-posed** if:

1. A unique solution exists.
2. Small changes in the initial data or the function \(f\) cause only small changes in the solution.

This is crucial for numerical methods because computers work with approximations and rounding errors. If the problem is not well-posed, tiny errors could cause huge differences in the solution, making numerical approximations unreliable.

**Summary:** Checking the Lipschitz condition is a practical way to verify if an IVP is well-posed.


### 3. 🧮 Euler’s Method: The Basic Numerical Approach

Euler’s method is the simplest way to approximate solutions to IVPs numerically.

#### How Euler’s Method Works

- We divide the time interval \([a, b]\) into \(N\) equal parts, called **mesh points**: \(t_0, t_1, ..., t_N\).
- The step size is \(h = \frac{b - a}{N}\).
- Starting from the initial value \(y(t_0) = y_0\), we approximate the solution at each mesh point using the formula:

\[
w_{i+1} = w_i + h f(t_i, w_i)
\]

Here, \(w_i\) approximates \(y(t_i)\).

#### Intuition Behind Euler’s Method

Euler’s method uses the idea of a **tangent line approximation**:

- At each point \((t_i, w_i)\), the slope of the solution curve is approximately \(f(t_i, w_i)\).
- We move forward a small step \(h\) along this slope to estimate the next value \(w_{i+1}\).

#### Example

For the IVP \(y' = y - t^2 + 1\), \(y(0) = 0.5\), with \(N=4\) and \(h=0.5\), Euler’s method calculates approximate values at \(t=0.5, 1.0, 1.5, 2.0\).

#### Error in Euler’s Method

- The error is proportional to the step size \(h\) (order 1).
- Smaller \(h\) means better accuracy but more computation.
- However, very small \(h\) can increase rounding errors due to finite precision in computers.


### 4. 🚀 Runge-Kutta Methods: More Accurate Numerical Solutions

Euler’s method is simple but not very accurate. Runge-Kutta methods improve accuracy by using more sophisticated approximations.

#### Why Runge-Kutta?

- Higher order Taylor expansions give better approximations but require derivatives of \(f\), which can be hard or expensive to compute.
- Runge-Kutta methods cleverly approximate these derivatives by evaluating \(f\) at several points within each step.

#### Midpoint Method (Second Order Runge-Kutta)

- Uses the slope at the midpoint of the interval to improve the estimate.
- Formula:

\[
w_{i+1} = w_i + h f\left(t_i + \frac{h}{2}, w_i + \frac{h}{2} f(t_i, w_i)\right)
\]

#### Modified Euler Method

- Averages the slope at the beginning and the end of the interval.
- Formula:

\[
w_{i+1} = w_i + \frac{h}{2} \left[f(t_i, w_i) + f(t_{i+1}, w_i + h f(t_i, w_i))\right]
\]

#### Fourth Order Runge-Kutta (Most Common)

- Uses four slope evaluations per step.
- Very accurate with error order \(h^4\).
- Formula involves calculating four intermediate slopes \(k_1, k_2, k_3, k_4\) and combining them.

#### Comparison of Methods

| Method               | Error Order | Number of \(f\) Evaluations per Step |
|----------------------|-------------|-------------------------------------|
| Euler                | 1           | 1                                   |
| Midpoint             | 2           | 2                                   |
| Modified Euler       | 2           | 2                                   |
| Fourth Order Runge-Kutta | 4       | 4                                   |

Runge-Kutta methods provide much better accuracy for the same step size compared to Euler’s method.


### 5. 🔄 Multi-Step Methods: Using More Past Information

One-step methods like Euler and Runge-Kutta use only the last point to find the next approximation. **Multi-step methods** use several previous points to improve accuracy.

#### General Form

An \(m\)-step method uses the last \(m\) approximations \(w_i, w_{i-1}, ..., w_{i-m+1}\) to compute \(w_{i+1}\).

- These methods can be **explicit** (next value depends only on known values) or **implicit** (next value appears on both sides of the equation).

#### Adams Methods

Two important families of multi-step methods:

- **Adams-Bashforth (Explicit):** Use past function values to predict the next value.
- **Adams-Moulton (Implicit):** Use past and next function values, requiring solving an equation for \(w_{i+1}\).

#### Predictor-Corrector Methods

- Combine explicit and implicit methods.
- Use an explicit method to predict \(w_{i+1}\).
- Use this prediction in an implicit method to correct and improve the estimate.
- This approach balances accuracy and computational effort.


### 6. 🔢 Numerical Solutions for Systems of IVPs

Many problems involve **systems** of differential equations, not just one equation.

#### System of IVPs

A system looks like:

\[
\begin{cases}
u_1' = f_1(t, u_1, u_2, ..., u_m) \\
u_2' = f_2(t, u_1, u_2, ..., u_m) \\
\vdots \\
u_m' = f_m(t, u_1, u_2, ..., u_m)
\end{cases}
\]

with initial conditions \(u_j(a) = \alpha_j\).

#### Existence and Uniqueness for Systems

- Similar Lipschitz conditions apply, but now for vector-valued functions.
- If each \(f_j\) and its partial derivatives are continuous and satisfy Lipschitz conditions, the system has a unique solution.

#### Numerical Methods for Systems

- Runge-Kutta methods extend naturally to systems.
- For each component \(u_j\), calculate intermediate slopes \(k_{i,1}^j, k_{i,2}^j, ...\) and update approximations.
- This allows simultaneous approximation of all functions \(u_1(t), ..., u_m(t)\).


### 7. 🔄 Converting Higher-Order IVPs to Systems

Higher-order differential equations (e.g., second order) can be rewritten as systems of first-order equations.

#### Example

For a second-order IVP:

\[
y'' = g(t, y, y')
\]

Define:

\[
u_1 = y, \quad u_2 = y'
\]

Then:

\[
\begin{cases}
u_1' = u_2 \\
u_2' = g(t, u_1, u_2)
\end{cases}
\]

This system can be solved using the methods for systems described above.


### Summary

- **Initial Value Problems (IVPs)** involve solving differential equations with given initial conditions.
- **Existence and uniqueness** of solutions depend on continuity and Lipschitz conditions.
- **Well-posedness** ensures solutions behave stably under small changes.
- **Euler’s method** is a simple numerical method but has limited accuracy.
- **Runge-Kutta methods** improve accuracy by using multiple slope evaluations.
- **Multi-step methods** use several past points to improve approximations.
- **Predictor-corrector methods** combine explicit and implicit approaches for better results.
- Systems of IVPs and higher-order IVPs can be handled by extending these methods.



<br>

## Questions

#### 1. Which of the following statements about an Initial Value Problem (IVP) are true?  
A) An IVP consists of a differential equation and initial conditions specifying the function and its derivatives at a starting point.  
B) The initial values must always include the function value and all its derivatives up to the order of the differential equation.  
C) IVPs always have closed-form analytical solutions.  
D) Numerical methods are often necessary because many IVPs cannot be solved analytically.


#### 2. A function \(f(t, y)\) satisfies a Lipschitz condition on a set \(D\) if:  
A) There exists a constant \(L > 0\) such that \(|f(t, y_1) - f(t, y_2)| \leq L |y_1 - y_2|\) for all \((t, y_1), (t, y_2) \in D\).  
B) \(f\) is differentiable with respect to \(t\) on \(D\).  
C) \(f\) is continuous on \(D\) and its partial derivative with respect to \(y\) is bounded.  
D) \(f\) is convex on \(D\).


#### 3. Which of the following sets is convex?  
A) The set \(D = \{(t, y) \mid t \in [0,1], y \in [-1,1]\}\).  
B) The set \(D = \{(t, y) \mid y = t^2, t \in [0,1]\}\).  
C) The set \(D = \{(t, y) \mid t^2 + y^2 \leq 1\}\).  
D) The set \(D = \{(t, y) \mid y \geq |t|\}\).


#### 4. The Existence and Uniqueness Theorem for IVPs requires which of the following conditions?  
A) \(f(t, y)\) must be continuous on a convex set \(D\).  
B) \(f(t, y)\) must satisfy a Lipschitz condition in \(y\) on \(D\).  
C) The initial value \(y(a)\) must be zero.  
D) The domain \(D\) must be bounded.


#### 5. What does it mean for an IVP to be well-posed?  
A) It has a unique solution.  
B) Small changes in initial conditions or the function \(f\) cause only small changes in the solution.  
C) The solution can be expressed in closed form.  
D) The solution is stable under perturbations in the differential equation and initial values.


#### 6. Which of the following statements about Euler’s method are correct?  
A) Euler’s method approximates the solution at discrete mesh points, not continuously.  
B) The step size \(h\) is defined as \(\frac{b-a}{N}\) where \(N\) is the number of steps.  
C) Euler’s method uses a second-order Taylor expansion to approximate the solution.  
D) The error in Euler’s method is proportional to the first power of \(h\).


#### 7. Regarding the error bounds of Euler’s method, which are true?  
A) The theoretical error bound depends on the Lipschitz constant \(L\) and the bound on the second derivative of the solution.  
B) The actual error is always equal to the theoretical error bound.  
C) Rounding errors can become significant as \(h\) becomes very small.  
D) Decreasing \(h\) indefinitely always decreases the total error.


#### 8. Runge-Kutta methods improve on Euler’s method by:  
A) Using multiple evaluations of \(f(t, y)\) within each step.  
B) Requiring the computation of derivatives of \(f\) with respect to \(t\).  
C) Eliminating the need for derivative computations by approximating higher-order terms with function evaluations.  
D) Being explicit multi-step methods.


#### 9. The Midpoint method (a second-order Runge-Kutta method) approximates the solution by:  
A) Using the slope at the beginning of the interval only.  
B) Using the slope at the midpoint of the interval estimated from the initial slope.  
C) Averaging the slopes at the beginning and end of the interval.  
D) Using four slope evaluations per step.


#### 10. Which of the following statements about the fourth-order Runge-Kutta method are true?  
A) It requires four function evaluations per step.  
B) It has a local truncation error of order \(h^5\).  
C) It is more accurate than Euler’s method for the same step size.  
D) It is an implicit method.


#### 11. Multi-step methods differ from one-step methods because:  
A) They use multiple previous approximations to compute the next value.  
B) They always require solving implicit equations.  
C) They can be explicit or implicit depending on the coefficients.  
D) They do not require initial values.


#### 12. In the general multi-step method formula, if the coefficient \(b_m = 0\), the method is:  
A) Explicit, because \(w_{i+1}\) can be computed directly.  
B) Implicit, because \(w_{i+1}\) appears on both sides of the equation.  
C) Unstable for all IVPs.  
D) Requires solving nonlinear equations at each step.


#### 13. Adams-Bashforth methods are:  
A) Explicit multi-step methods.  
B) Implicit multi-step methods.  
C) Based on polynomial interpolation of \(f(t, y)\) at previous points.  
D) Always more accurate than Adams-Moulton methods of the same step number.


#### 14. Adams-Moulton methods are:  
A) Implicit multi-step methods.  
B) Explicit multi-step methods.  
C) Used as correctors in predictor-corrector schemes.  
D) Require solving for \(w_{i+1}\) at each step.


#### 15. Predictor-corrector methods:  
A) Use an explicit method to predict the next value.  
B) Use an implicit method to correct the predicted value.  
C) Always guarantee exact solutions.  
D) Can improve accuracy without significantly increasing computational cost.


#### 16. For a system of IVPs, the Lipschitz condition:  
A) Must hold for each component function \(f_j\) with respect to all variables \(u_1, u_2, ..., u_m\).  
B) Is not necessary for existence and uniqueness of solutions.  
C) Can be verified by checking boundedness of partial derivatives of \(f_j\).  
D) Is only required for scalar IVPs.


#### 17. When converting a higher-order IVP into a system of first-order IVPs:  
A) New variables are introduced to represent derivatives of the original function.  
B) The order of the system equals the order of the original IVP.  
C) The system can be solved using methods for first-order systems.  
D) This conversion is only possible for linear differential equations.


#### 18. Which of the following are true about the stability and error behavior of numerical methods for IVPs?  
A) Well-posedness of the IVP ensures numerical stability under small perturbations.  
B) Euler’s method has global error proportional to \(h\).  
C) Runge-Kutta methods can have errors that grow exponentially with the number of steps.  
D) Multi-step methods always have smaller errors than one-step methods.


#### 19. Which of the following statements about the use of mesh points in numerical methods are correct?  
A) Mesh points are usually chosen to be equally spaced in the interval \([a, b]\).  
B) The solution is approximated only at mesh points, and values between points require interpolation.  
C) The step size \(h\) can vary arbitrarily between mesh points in Euler’s method.  
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


#### 2. A function \(f(t, y)\) satisfies a Lipschitz condition on a set \(D\) if:  
A) ✓ This is the formal definition of the Lipschitz condition in \(y\).  
B) ✗ Differentiability with respect to \(t\) is not required for Lipschitz in \(y\).  
C) ✓ Bounded partial derivative with respect to \(y\) implies Lipschitz condition.  
D) ✗ Convexity is unrelated to Lipschitz condition.

**Correct:** A, C


#### 3. Which of the following sets is convex?  
A) ✓ A rectangle in \(\mathbb{R}^2\) is convex.  
B) ✗ A parabola curve is not convex as a set (it’s a curve, not a filled region).  
C) ✓ A disk (circle and interior) is convex.  
D) ✗ The set \(y \geq |t|\) forms a "V" shape, which is convex, but since it includes all points above, it is convex. (Tricky) Actually, this set is convex because any line segment between two points above the "V" lies above it. So this is ✓.

**Correct:** A, C, D


#### 4. The Existence and Uniqueness Theorem for IVPs requires which of the following conditions?  
A) ✓ Continuity on a convex set is required.  
B) ✓ Lipschitz condition in \(y\) is required.  
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
B) ✓ Step size \(h\) is defined as \(\frac{b-a}{N}\).  
C) ✗ Euler’s method uses first-order Taylor approximation, not second-order.  
D) ✓ Error is proportional to \(h\) (order 1).

**Correct:** A, B, D


#### 7. Regarding the error bounds of Euler’s method, which are true?  
A) ✓ Theoretical error bound depends on Lipschitz constant and second derivative bound.  
B) ✗ Actual error is usually smaller than the theoretical bound.  
C) ✓ Rounding errors become significant as \(h\) decreases.  
D) ✗ Decreasing \(h\) indefinitely can increase rounding errors, so total error may not always decrease.

**Correct:** A, C


#### 8. Runge-Kutta methods improve on Euler’s method by:  
A) ✓ Using multiple evaluations of \(f\) per step.  
B) ✗ They avoid computing derivatives of \(f\) with respect to \(t\).  
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
B) ✓ Local truncation error is order \(h^5\) (global error order \(h^4\)).  
C) ✓ More accurate than Euler’s method for same \(h\).  
D) ✗ It is an explicit method, not implicit.

**Correct:** A, B, C


#### 11. Multi-step methods differ from one-step methods because:  
A) ✓ Use multiple previous approximations.  
B) ✗ Not all multi-step methods are implicit; some are explicit.  
C) ✓ Can be explicit or implicit depending on coefficients.  
D) ✗ Initial values are required to start the method.

**Correct:** A, C


#### 12. In the general multi-step method formula, if the coefficient \(b_m = 0\), the method is:  
A) ✓ Explicit, since \(w_{i+1}\) can be computed directly.  
B) ✗ Implicit requires \(b_m \neq 0\).  
C) ✗ Stability depends on method and problem, not just \(b_m\).  
D) ✗ Explicit methods do not require solving nonlinear equations.

**Correct:** A


#### 13. Adams-Bashforth methods are:  
A) ✓ Explicit multi-step methods.  
B) ✗ They are not implicit.  
C) ✓ Based on polynomial interpolation of \(f\) at previous points.  
D) ✗ Adams-Moulton methods are generally more accurate for same step number.

**Correct:** A, C


#### 14. Adams-Moulton methods are:  
A) ✓ Implicit multi-step methods.  
B) ✗ Not explicit.  
C) ✓ Often used as correctors in predictor-corrector schemes.  
D) ✓ Require solving for \(w_{i+1}\) at each step.

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
B) ✓ Euler’s method global error is proportional to \(h\).  
C) ✗ Runge-Kutta errors do not necessarily grow exponentially; depends on problem.  
D) ✗ Multi-step methods are not always more accurate than one-step methods.

**Correct:** A, B


#### 19. Which of the following statements about the use of mesh points in numerical methods are correct?  
A) ✓ Mesh points are usually equally spaced.  
B) ✓ Solutions are approximated at mesh points; interpolation needed between points.  
C) ✗ Euler’s method typically uses fixed step size \(h\). Variable step size is possible but not standard.  
D) ✗ Smaller step size usually improves accuracy but not always due to rounding errors.

**Correct:** A, B


#### 20. Regarding the computational cost and accuracy trade-offs in numerical methods for IVPs:  
A) ✓ Higher-order methods require more function evaluations but yield better accuracy.  
B) ✓ Multi-step methods reuse previous info, reducing function evaluations per step.  
C) ✗ Implicit methods are generally harder to implement than explicit methods.  
D) ✓ Predictor-corrector methods balance accuracy and computational effort.

**Correct:** A, B, D