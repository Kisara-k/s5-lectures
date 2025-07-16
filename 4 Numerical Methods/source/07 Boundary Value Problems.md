## Boundary Value Problems

[Study Notes](#study-notes)

[Questions](#questions)



### Key Points

#### 1. 📐 Boundary Value Problems (BVPs)
- BVPs involve solving differential equations with conditions specified at two distinct points (boundaries).
- The standard form of a two-point BVP is \( y'' = f(x, y, y') \) with \( y(a) = \alpha \) and \( y(b) = \beta \).
- Boundary conditions are known as boundary values, different from initial conditions in IVPs.

#### 2. ✅ Existence and Uniqueness Theorem for BVPs
- If \( f \), \( f_y \), and \( f_{y'} \) are continuous on domain \( D \), and:
  - \( f_y(x, y, y') > 0 \) for all \( (x, y, y') \in D \),
  - There exists \( M > 0 \) such that \( |f_{y'}(x, y, y')| \leq M \),
- Then the BVP has a unique solution on \( [a, b] \).

#### 3. 🎯 Linear Shooting Method
- Converts a linear BVP into two IVPs with initial conditions:
  - \( y_1(a) = \alpha, y_1'(a) = 0 \)
  - \( y_2(a) = 0, y_2'(a) = 1 \)
- The BVP solution is \( y(x) = y_1(x) + c y_2(x) \), where \( c = \frac{\beta - y_1(b)}{y_2(b)} \).
- Requires \( p(x), q(x), r(x) \) continuous on \( [a, b] \) and \( q(x) > 0 \) for existence and uniqueness.
- Numerical IVP solutions often use the fourth-order Runge-Kutta method.

#### 4. 🔄 Non-linear Shooting Method
- Approximates the BVP solution by solving a sequence of IVPs with varying initial slopes \( t_k \).
- Uses Newton's method to solve \( y(b, t) - \beta = 0 \) iteratively:
  \[
  t_{k+1} = t_k - \frac{y(b, t_k) - \beta}{\frac{\partial y}{\partial t}(b, t_k)}
  \]
- The derivative \( \frac{\partial y}{\partial t}(x, t) \) satisfies an IVP with initial conditions \( z(a, t) = 0 \), \( z'(a, t) = 1 \).
- Iteration continues until \( |y(b, t_k) - \beta| \) is sufficiently small.

#### 5. 🧮 Finite Difference Method (FDM) for Linear BVPs
- The interval \([a, b]\) is divided into \( N+1 \) subintervals with mesh points \( x_i = a + i h \), \( h = \frac{b - a}{N+1} \).
- Centered difference approximations:
  - \( y''(x_i) \approx \frac{w_{i-1} - 2 w_i + w_{i+1}}{h^2} \)
  - \( y'(x_i) \approx \frac{w_{i+1} - w_{i-1}}{2h} \)
- Leads to a tridiagonal linear system \( A \mathbf{w} = \mathbf{b} \).
- Unique solution exists if \( p, q, r \) continuous, \( q(x) \geq 0 \), and \( h < \frac{2}{L} \) where \( L = \max |p(x)| \).

#### 6. 🔧 Finite Difference Method for Non-linear BVPs
- Similar mesh and difference formulas as linear case, but results in a system of nonlinear equations:
  \[
  \frac{w_{i-1} - 2 w_i + w_{i+1}}{h^2} = f\left(x_i, w_i, \frac{w_{i+1} - w_{i-1}}{2h}\right)
  \]
- Requires \( f \), \( f_y \), and \( f_{y'} \) continuous; \( f_y(x, y, y') \geq \delta > 0 \).
- Unique solution exists if \( h < \frac{2}{L} \), with \( L \) related to bounds on derivatives.
- Newton's method is used to solve the nonlinear system iteratively.



<br>

## Study Notes

### MA3024 Numerical Methods: Boundary Value Problems (BVPs) 📚


### 1. 🧩 Introduction to Boundary Value Problems (BVPs)

When solving differential equations, you often encounter problems where the solution is required to satisfy certain conditions. In many cases, these conditions are specified at a single point, usually the start of the interval. These are called **Initial Value Problems (IVPs)**.

However, in **Boundary Value Problems (BVPs)**, the conditions are given at two distinct points, typically at the ends of the interval. For example, consider a second-order differential equation where you want to find a function \( y(x) \) such that:

\[
y'' = f(x, y, y')
\]

with boundary conditions:

\[
y(a) = \alpha, \quad y(b) = \beta
\]

Here, \( a \) and \( b \) are the boundaries of the domain, and \( \alpha \), \( \beta \) are the specified values of the solution at these points. This is fundamentally different from IVPs because the solution must satisfy conditions at two points, not just one.


### 2. 🔍 Existence and Uniqueness of Solutions for BVPs

Before attempting to solve a BVP, it is important to know whether a solution exists and whether it is unique. This is guaranteed under certain conditions.

**Theorem 1** states that if the function \( f(x, y, y') \) in the differential equation is continuous over a domain \( D \), and its partial derivatives with respect to \( y \) and \( y' \) (denoted \( f_y \) and \( f_{y'} \)) are also continuous, then:

1. \( f_y(x, y, y') > 0 \) for all points in \( D \).
2. There exists a constant \( M > 0 \) such that \( |f_{y'}(x, y, y')| \leq M \) for all points in \( D \).

Under these conditions, the BVP has a **unique solution** on the interval \( [a, b] \).

#### Example:

Consider the BVP:

\[
y'' + e^{-x} y + \sin(y') = 0, \quad 1 \leq x \leq 2, \quad y(1) = 0, \quad y(2) = 0
\]

Rearranged as:

\[
y'' = -e^{-x} y - \sin(y')
\]

Here, \( f(x, y, y') = -e^{-x} y - \sin(y') \).

- \( f_y = -e^{-x} \), which is negative but since the theorem requires \( f_y > 0 \), we check the absolute value or the specific problem context.
- \( f_{y'} = -\cos(y') \), and since \( |\cos(y')| \leq 1 \), the boundedness condition holds.

By the theorem, this BVP has a unique solution.


### 3. 🎯 Linear Shooting Method for Linear BVPs

The **Linear Shooting Method** is a technique to solve linear BVPs by converting them into initial value problems (IVPs), which are easier to solve numerically.

#### Setup:

Consider a linear second-order BVP of the form:

\[
y'' = p(x) y' + q(x) y + r(x), \quad a \leq x \leq b
\]

with boundary conditions:

\[
y(a) = \alpha, \quad y(b) = \beta
\]

#### How the method works:

1. Solve two IVPs:
   - \( y_1(x) \) solves the equation with initial conditions \( y_1(a) = \alpha \), \( y_1'(a) = 0 \).
   - \( y_2(x) \) solves the equation with initial conditions \( y_2(a) = 0 \), \( y_2'(a) = 1 \).

2. The solution to the BVP is then constructed as:

\[
y(x) = y_1(x) + c y_2(x)
\]

where the constant \( c \) is chosen so that the boundary condition at \( x = b \) is satisfied:

\[
y(b) = y_1(b) + c y_2(b) = \beta \implies c = \frac{\beta - y_1(b)}{y_2(b)}
\]

This reduces the BVP to solving two IVPs, which can be done using numerical methods like the **fourth-order Runge-Kutta method**.


### 4. 🔄 Non-linear Shooting Method

For **non-linear BVPs**, the shooting method is more complex because the relationship between the initial slope and the boundary value at \( b \) is non-linear.

#### Procedure:

1. Guess an initial slope \( t_0 = y'(a) \).
2. Solve the IVP with \( y(a) = \alpha \) and \( y'(a) = t_0 \) to get \( y(x, t_0) \).
3. Check if \( y(b, t_0) \) is close enough to \( \beta \). If not, update the guess \( t \) using **Newton's method** to solve:

\[
F(t) = y(b, t) - \beta = 0
\]

4. Newton's iteration formula is:

\[
t_{k+1} = t_k - \frac{F(t_k)}{F'(t_k)} = t_k - \frac{y(b, t_k) - \beta}{\frac{\partial y}{\partial t}(b, t_k)}
\]

5. Since \( \frac{\partial y}{\partial t}(b, t_k) \) is not known analytically, we define:

\[
z(x, t) = \frac{\partial y}{\partial t}(x, t)
\]

and derive an IVP for \( z \) by differentiating the original ODE with respect to \( t \). The initial conditions for \( z \) are:

\[
z(a, t) = 0, \quad z'(a, t) = 1
\]

6. Solve the IVP for \( z \) alongside \( y \), then update \( t \) using Newton's method until convergence.


### 5. 🧮 Finite Difference Methods for Linear BVPs

The **Finite Difference Method (FDM)** approximates derivatives by differences on a discrete grid, turning the differential equation into a system of algebraic equations.

#### Steps:

1. Partition the interval \([a, b]\) into \( N+1 \) equal subintervals with mesh points:

\[
x_i = a + i h, \quad h = \frac{b - a}{N+1}, \quad i = 0, 1, \ldots, N+1
\]

2. Approximate derivatives at interior points \( x_i \) using **centered difference formulas**:

- For the second derivative \( y''(x_i) \):

\[
y''(x_i) \approx \frac{y_{i-1} - 2 y_i + y_{i+1}}{h^2}
\]

- For the first derivative \( y'(x_i) \):

\[
y'(x_i) \approx \frac{y_{i+1} - y_{i-1}}{2h}
\]

3. Substitute these approximations into the differential equation at each interior point to get a system of linear equations in terms of \( w_i \approx y(x_i) \).

4. This system can be written in matrix form:

\[
A \mathbf{w} = \mathbf{b}
\]

where \( A \) is a tridiagonal matrix derived from the coefficients of the finite difference approximations, and \( \mathbf{b} \) includes boundary conditions and source terms.

5. Solve the linear system using standard numerical linear algebra techniques.

#### Existence and uniqueness:

- If \( p(x), q(x), r(x) \) are continuous on \([a, b]\) and \( q(x) \geq 0 \), then the finite difference system has a unique solution provided the step size \( h \) is sufficiently small (specifically, \( h < 2/L \), where \( L \) is related to the maximum of \( |p(x)| \)).


### 6. 🔧 Finite Difference Methods for Non-linear BVPs

For **non-linear BVPs**, the finite difference approach is similar but results in a system of **non-linear algebraic equations**.

#### Key points:

- The non-linear BVP is:

\[
y'' = f(x, y, y'), \quad y(a) = \alpha, \quad y(b) = \beta
\]

- Using the same mesh and centered difference formulas, substitute into the equation to get:

\[
\frac{w_{i-1} - 2 w_i + w_{i+1}}{h^2} = f\left(x_i, w_i, \frac{w_{i+1} - w_{i-1}}{2h}\right)
\]

for \( i = 1, 2, \ldots, N \).

- This forms a system of \( N \) non-linear equations in \( N \) unknowns \( w_i \).

#### Solving the system:

- Use **Newton's method** for systems of non-linear equations:
  - Start with an initial guess for \( \mathbf{w} \).
  - Linearize the system around the current guess.
  - Solve the linearized system to update the guess.
  - Repeat until convergence.

#### Conditions for uniqueness:

- The function \( f \) and its partial derivatives \( f_y \), \( f_{y'} \) are continuous.
- \( f_y(x, y, y') \geq \delta > 0 \) for some positive constant \( \delta \).
- There exist constants \( k, L \) bounding the derivatives.
- The step size \( h \) must satisfy \( h < 2/L \) for uniqueness.


### Summary

- **Boundary Value Problems (BVPs)** require solutions satisfying conditions at two points.
- Existence and uniqueness depend on continuity and positivity conditions on \( f \) and its derivatives.
- The **Shooting Method** converts BVPs into IVPs; linear problems use a direct approach, non-linear problems require iterative Newton updates.
- **Finite Difference Methods** discretize the domain and approximate derivatives, leading to linear or non-linear algebraic systems.
- Newton's method is essential for solving non-linear systems arising from non-linear BVPs.



<br>

## Questions

#### 1. Which of the following statements correctly describe a Boundary Value Problem (BVP)?  
A) The solution must satisfy conditions at two distinct points in the domain.  
B) The solution is determined solely by initial conditions at a single point.  
C) Boundary conditions specify values of the solution at the endpoints of the interval.  
D) BVPs can always be converted into initial value problems without approximation.


#### 2. For the BVP \( y'' = f(x, y, y') \) with \( y(a) = \alpha \) and \( y(b) = \beta \), which conditions on \( f \) guarantee existence and uniqueness of the solution?  
A) \( f \) and its partial derivatives \( f_y \), \( f_{y'} \) are continuous on the domain.  
B) \( f_y(x, y, y') > 0 \) for all points in the domain.  
C) \( |f_{y'}(x, y, y')| \) is bounded by some constant \( M \).  
D) \( f_y(x, y, y') \) can be negative as long as \( f_{y'} \) is bounded.


#### 3. In the linear shooting method, why is it necessary to solve two initial value problems (IVPs)?  
A) To find two independent solutions that can be combined to satisfy both boundary conditions.  
B) Because the original BVP is non-linear and requires linearization.  
C) To determine the constant that adjusts the slope at the initial point.  
D) To verify the uniqueness of the solution.


#### 4. Which of the following is true about the constant \( c \) in the linear shooting method solution \( y(x) = y_1(x) + c y_2(x) \)?  
A) It is chosen so that \( y(a) = \alpha \).  
B) It is chosen so that \( y(b) = \beta \).  
C) It depends on the value of \( y_2(b) \).  
D) It is always zero if \( y_2(x) \) is non-constant.


#### 5. When applying the non-linear shooting method, what is the role of Newton's method?  
A) To solve the original differential equation directly.  
B) To iteratively find the correct initial slope \( t \) so that the boundary condition at \( b \) is satisfied.  
C) To approximate the derivative \( \frac{\partial y}{\partial t}(b, t) \) analytically.  
D) To linearize the BVP into a system of linear equations.


#### 6. In the non-linear shooting method, the function \( z(x, t) = \frac{\partial y}{\partial t}(x, t) \) satisfies an initial value problem with initial conditions:  
A) \( z(a, t) = 1 \), \( z'(a, t) = 0 \)  
B) \( z(a, t) = 0 \), \( z'(a, t) = 1 \)  
C) \( z(a, t) = 0 \), \( z'(a, t) = 0 \)  
D) \( z(a, t) = y(a) \), \( z'(a, t) = y'(a) \)


#### 7. Which of the following statements about the finite difference method (FDM) for linear BVPs is correct?  
A) The method approximates derivatives using forward differences only.  
B) The centered difference formula for the second derivative has a truncation error of order \( O(h^2) \).  
C) The resulting system of equations is always non-linear.  
D) The method converts the differential equation into a matrix equation.


#### 8. For the finite difference method applied to a linear BVP, the step size \( h \) must satisfy which condition to guarantee uniqueness of the solution?  
A) \( h > 2L \), where \( L = \max |p(x)| \)  
B) \( h < 2L \), where \( L = \max |p(x)| \)  
C) \( h < 2/L \), where \( L = \max |p(x)| \)  
D) There is no restriction on \( h \) for uniqueness.


#### 9. In the finite difference approximation of \( y'(x_i) \), the centered difference formula is:  
A) \( \frac{y_{i+1} - y_i}{h} \)  
B) \( \frac{y_i - y_{i-1}}{h} \)  
C) \( \frac{y_{i+1} - y_{i-1}}{2h} \)  
D) \( \frac{y_{i+1} - 2 y_i + y_{i-1}}{h^2} \)


#### 10. When solving a non-linear BVP using finite difference methods, the resulting system of equations is:  
A) Linear and can be solved directly by matrix inversion.  
B) Non-linear and requires iterative methods such as Newton's method.  
C) Always guaranteed to have a unique solution regardless of step size.  
D) Independent of the initial guess for the solution.


#### 11. Which of the following conditions are necessary for the uniqueness of the solution to a non-linear BVP solved by finite difference methods?  
A) \( f \), \( f_y \), and \( f_{y'} \) are continuous on the domain.  
B) \( f_y(x, y, y') \geq \delta > 0 \) for some positive constant \( \delta \).  
C) The step size \( h \) satisfies \( h < 2/L \), where \( L \) bounds the derivatives of \( f \).  
D) \( f_y \) can be zero or negative as long as \( f_{y'} \) is bounded.


#### 12. In the context of BVPs, what is the main difference between initial value problems (IVPs) and boundary value problems (BVPs)?  
A) IVPs specify conditions at one point; BVPs specify conditions at two points.  
B) IVPs always have unique solutions; BVPs never do.  
C) BVPs can be solved by Runge-Kutta methods directly without modification.  
D) IVPs require solving non-linear systems; BVPs do not.


#### 13. Why is it generally not possible to determine \( \frac{\partial y}{\partial t}(b, t) \) analytically in the non-linear shooting method?  
A) Because \( y(b, t) \) is only known approximately from numerical solutions.  
B) Because \( y \) is not differentiable with respect to \( t \).  
C) Because the boundary condition at \( b \) is unknown.  
D) Because \( t \) is a constant and does not affect \( y \).


#### 14. Which of the following is true about the function \( y_2(x) \) in the linear shooting method?  
A) \( y_2(x) \) is a solution to the homogeneous version of the BVP.  
B) \( y_2(b) \neq 0 \) if \( y_2(x) \) is non-constant.  
C) \( y_2(x) \) satisfies the boundary condition \( y_2(a) = 1 \).  
D) \( y_2(x) \) is always zero at \( x = b \).


#### 15. The truncation error of the centered difference formula for the second derivative is:  
A) \( O(h) \)  
B) \( O(h^2) \)  
C) \( O(h^3) \)  
D) \( O(h^4) \)


#### 16. In the finite difference method, the matrix \( A \) formed from the discretization of a linear BVP is typically:  
A) Dense and non-symmetric.  
B) Sparse and tridiagonal.  
C) Diagonal with all entries equal.  
D) Singular for all step sizes \( h \).


#### 17. When applying Newton's method to solve the nonlinear system from finite difference discretization, which of the following is true?  
A) The Jacobian matrix must be computed or approximated at each iteration.  
B) The method converges regardless of the initial guess.  
C) The system is linearized around the current approximation.  
D) The solution is updated by solving a linear system at each step.


#### 18. Which of the following statements about the function \( f(x, y, y') \) in a BVP is false?  
A) \( f \) can be non-linear in \( y \) and \( y' \).  
B) Continuity of \( f \) and its partial derivatives is required for uniqueness.  
C) \( f_y \) must always be positive for the solution to exist.  
D) \( f_{y'} \) must be bounded for the solution to be unique.


#### 19. In the shooting method, if the initial guess \( t_0 \) for the slope at \( x = a \) is poor, what is the likely outcome?  
A) The method will fail to converge to the correct solution.  
B) Newton's method may require more iterations to converge.  
C) The solution \( y(x, t_0) \) will exactly satisfy the boundary condition at \( b \).  
D) The method will produce multiple solutions.


#### 20. Which of the following best describes the main challenge in solving nonlinear BVPs compared to linear BVPs?  
A) Nonlinear BVPs cannot be discretized using finite differences.  
B) Nonlinear BVPs require iterative methods to handle the nonlinearity in the algebraic system.  
C) Linear BVPs always have closed-form solutions.  
D) Nonlinear BVPs do not require boundary conditions at both ends.



<br>

## Answers

#### 1. Which of the following statements correctly describe a Boundary Value Problem (BVP)?  
A) ✓ The solution must satisfy conditions at two distinct points in the domain.  
B) ✗ This describes an initial value problem, not a BVP.  
C) ✓ Boundary conditions specify values of the solution at the endpoints of the interval.  
D) ✗ BVPs generally cannot be converted into IVPs without approximation or iterative methods.

**Correct:** A, C


#### 2. For the BVP \( y'' = f(x, y, y') \) with \( y(a) = \alpha \) and \( y(b) = \beta \), which conditions on \( f \) guarantee existence and uniqueness of the solution?  
A) ✓ Continuity of \( f \) and its partial derivatives is required.  
B) ✓ \( f_y > 0 \) is a key condition for uniqueness.  
C) ✓ Boundedness of \( f_{y'} \) ensures stability and uniqueness.  
D) ✗ \( f_y \) must be positive; negative values violate the theorem conditions.

**Correct:** A, B, C


#### 3. In the linear shooting method, why is it necessary to solve two initial value problems (IVPs)?  
A) ✓ To find two independent solutions that can be combined to satisfy both boundary conditions.  
B) ✗ The method applies to linear problems, not necessarily non-linear requiring linearization.  
C) ✓ The constant \( c \) adjusts the solution to meet the boundary condition at \( b \).  
D) ✗ Uniqueness is guaranteed by theory, not verified by solving two IVPs.

**Correct:** A, C


#### 4. Which of the following is true about the constant \( c \) in the linear shooting method solution \( y(x) = y_1(x) + c y_2(x) \)?  
A) ✗ \( y_1 \) already satisfies \( y(a) = \alpha \), so \( c \) is not chosen for this.  
B) ✓ \( c \) is chosen to satisfy the boundary condition at \( x = b \).  
C) ✓ \( c \) depends on \( y_2(b) \) because it appears in the denominator when solving for \( c \).  
D) ✗ \( c \) is zero only if \( y_1(b) = \beta \), not always.

**Correct:** B, C


#### 5. When applying the non-linear shooting method, what is the role of Newton's method?  
A) ✗ Newton's method is not used to solve the differential equation directly.  
B) ✓ It iteratively adjusts the initial slope \( t \) to satisfy the boundary condition at \( b \).  
C) ✗ The derivative \( \partial y/\partial t \) is approximated numerically, not analytically.  
D) ✗ Newton's method is not used to linearize the BVP itself, but to solve the nonlinear root-finding problem.

**Correct:** B


#### 6. In the non-linear shooting method, the function \( z(x, t) = \frac{\partial y}{\partial t}(x, t) \) satisfies an initial value problem with initial conditions:  
A) ✗ Incorrect initial conditions for \( z \).  
B) ✓ Correct initial conditions derived from differentiating the IVP with respect to \( t \).  
C) ✗ Both zero initial conditions would imply no sensitivity to \( t \).  
D) ✗ \( z \) is a sensitivity function, not equal to \( y \) or \( y' \).

**Correct:** B


#### 7. Which of the following statements about the finite difference method (FDM) for linear BVPs is correct?  
A) ✗ Forward differences are not used exclusively; centered differences are preferred for accuracy.  
B) ✓ Centered difference for second derivative has truncation error \( O(h^2) \).  
C) ✗ The system is linear for linear BVPs.  
D) ✓ The method converts the differential equation into a matrix equation.

**Correct:** B, D


#### 8. For the finite difference method applied to a linear BVP, the step size \( h \) must satisfy which condition to guarantee uniqueness of the solution?  
A) ✗ Incorrect inequality direction.  
B) ✗ Incorrect inequality direction.  
C) ✓ Correct condition: \( h < 2/L \) ensures uniqueness.  
D) ✗ There is a restriction on \( h \) for uniqueness.

**Correct:** C


#### 9. In the finite difference approximation of \( y'(x_i) \), the centered difference formula is:  
A) ✗ Forward difference, less accurate.  
B) ✗ Backward difference, less accurate.  
C) ✓ Centered difference formula for first derivative.  
D) ✗ This is the formula for the second derivative.

**Correct:** C


#### 10. When solving a non-linear BVP using finite difference methods, the resulting system of equations is:  
A) ✗ The system is non-linear due to non-linearity in \( f \).  
B) ✓ Non-linear system requiring iterative methods like Newton's method.  
C) ✗ Uniqueness depends on conditions and step size, not guaranteed always.  
D) ✗ Initial guess affects convergence in iterative methods.

**Correct:** B


#### 11. Which of the following conditions are necessary for the uniqueness of the solution to a non-linear BVP solved by finite difference methods?  
A) ✓ Continuity of \( f \) and its partial derivatives is required.  
B) ✓ \( f_y \) bounded below by positive \( \delta \) ensures monotonicity and uniqueness.  
C) ✓ Step size restriction \( h < 2/L \) is necessary.  
D) ✗ \( f_y \) cannot be zero or negative for uniqueness.

**Correct:** A, B, C


#### 12. In the context of BVPs, what is the main difference between initial value problems (IVPs) and boundary value problems (BVPs)?  
A) ✓ IVPs specify conditions at one point; BVPs specify at two points.  
B) ✗ Both IVPs and BVPs can have unique or multiple solutions depending on the problem.  
C) ✗ Runge-Kutta methods require modification or iteration for BVPs.  
D) ✗ IVPs can be linear or nonlinear; BVPs also can be either.

**Correct:** A


#### 13. Why is it generally not possible to determine \( \frac{\partial y}{\partial t}(b, t) \) analytically in the non-linear shooting method?  
A) ✓ Because \( y(b, t) \) is obtained numerically, not in closed form.  
B) ✗ \( y \) is differentiable with respect to \( t \) in theory.  
C) ✗ The boundary condition at \( b \) is known, but \( y(b, t) \) depends on \( t \).  
D) ✗ \( t \) affects \( y \), so it is not constant.

**Correct:** A


#### 14. Which of the following is true about the function \( y_2(x) \) in the linear shooting method?  
A) ✓ \( y_2 \) solves the homogeneous equation with zero initial value but unit initial slope.  
B) ✓ \( y_2(b) \neq 0 \) if \( y_2 \) is non-constant, ensuring the denominator in \( c \) is non-zero.  
C) ✗ \( y_2(a) = 0 \), not 1.  
D) ✗ \( y_2(b) \) is generally non-zero.

**Correct:** A, B


#### 15. The truncation error of the centered difference formula for the second derivative is:  
A) ✗ Too large an error order.  
B) ✓ Correct order \( O(h^2) \).  
C) ✗ Higher order than actual.  
D) ✗ Much higher order than actual.

**Correct:** B


#### 16. In the finite difference method, the matrix \( A \) formed from the discretization of a linear BVP is typically:  
A) ✗ The matrix is sparse, not dense.  
B) ✓ Tridiagonal and sparse due to local stencil.  
C) ✗ Not diagonal with equal entries.  
D) ✗ Not singular if conditions are met.

**Correct:** B


#### 17. When applying Newton's method to solve the nonlinear system from finite difference discretization, which of the following is true?  
A) ✓ The Jacobian matrix must be computed or approximated at each iteration.  
B) ✗ Convergence depends on initial guess and problem properties.  
C) ✓ The system is linearized around the current approximation.  
D) ✓ The update step requires solving a linear system.

**Correct:** A, C, D


#### 18. Which of the following statements about the function \( f(x, y, y') \) in a BVP is false?  
A) ✓ \( f \) can be nonlinear in \( y \) and \( y' \).  
B) ✓ Continuity of \( f \) and derivatives is required for uniqueness.  
C) ✗ \( f_y \) must be positive, not always true for existence but required for uniqueness in the theorem.  
D) ✓ \( f_{y'} \) must be bounded for uniqueness.

**Correct:** C (false statement)


#### 19. In the shooting method, if the initial guess \( t_0 \) for the slope at \( x = a \) is poor, what is the likely outcome?  
A) ✗ The method may still converge if Newton's method is robust.  
B) ✓ More iterations may be needed for convergence.  
C) ✗ The solution will not exactly satisfy the boundary condition initially.  
D) ✗ The method does not produce multiple solutions; it tries to find one.

**Correct:** B


#### 20. Which of the following best describes the main challenge in solving nonlinear BVPs compared to linear BVPs?  
A) ✗ Nonlinear BVPs can be discretized using finite differences.  
B) ✓ Nonlinear BVPs require iterative methods to solve nonlinear algebraic systems.  
C) ✗ Linear BVPs do not always have closed-form solutions.  
D) ✗ Nonlinear BVPs require boundary conditions at both ends, same as linear.

**Correct:** B