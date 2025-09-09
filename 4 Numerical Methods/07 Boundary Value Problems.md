## Boundary Value Problems

## Key Points

#### 1. 📐 Boundary Value Problems (BVPs)
- BVPs involve solving differential equations with conditions specified at two distinct points (boundaries).
- The standard form of a two-point BVP is $y'' = f(x, y, y')$ with $y(a) = \alpha$ and $y(b) = \beta$.
- Boundary conditions are known as boundary values, different from initial conditions in IVPs.

#### 2. ✅ Existence and Uniqueness Theorem for BVPs
- If $f$, $f_y$, and $f_{y'}$ are continuous on domain $D$, and:
  - $f_y(x, y, y') > 0$ for all $(x, y, y') \in D$,
  - There exists $M > 0$ such that $|f_{y'}(x, y, y')| \leq M$,
- Then the BVP has a unique solution on $[a, b]$.

#### 3. 🎯 Linear Shooting Method
- Converts a linear BVP into two IVPs with initial conditions:
  - $y_1(a) = \alpha, y_1'(a) = 0$
  - $y_2(a) = 0, y_2'(a) = 1$
- The BVP solution is $y(x) = y_1(x) + c y_2(x)$, where $c = \frac{\beta - y_1(b)}{y_2(b)}$.
- Requires $p(x), q(x), r(x)$ continuous on $[a, b]$ and $q(x) > 0$ for existence and uniqueness.
- Numerical IVP solutions often use the fourth-order Runge-Kutta method.

#### 4. 🔄 Non-linear Shooting Method
- Approximates the BVP solution by solving a sequence of IVPs with varying initial slopes $t_k$.
- Uses Newton's method to solve $y(b, t) - \beta = 0$ iteratively:

$$
  t_{k+1} = t_k - \frac{y(b, t_k) - \beta}{\frac{\partial y}{\partial t}(b, t_k)}
$$

- The derivative $\frac{\partial y}{\partial t}(x, t)$ satisfies an IVP with initial conditions $z(a, t) = 0$, $z'(a, t) = 1$.
- Iteration continues until $|y(b, t_k) - \beta|$ is sufficiently small.

#### 5. 🧮 Finite Difference Method (FDM) for Linear BVPs
- The interval $[a, b]$ is divided into $N+1$ subintervals with mesh points $x_i = a + i h$, $h = \frac{b - a}{N+1}$.
- Centered difference approximations:
  - $y''(x_i) \approx \frac{w_{i-1} - 2 w_i + w_{i+1}}{h^2}$
  - $y'(x_i) \approx \frac{w_{i+1} - w_{i-1}}{2h}$
- Leads to a tridiagonal linear system $A \mathbf{w} = \mathbf{b}$.
- Unique solution exists if $p, q, r$ continuous, $q(x) \geq 0$, and $h < \frac{2}{L}$ where $L = \max |p(x)|$.

#### 6. 🔧 Finite Difference Method for Non-linear BVPs
- Similar mesh and difference formulas as linear case, but results in a system of nonlinear equations:

$$
  \frac{w_{i-1} - 2 w_i + w_{i+1}}{h^2} = f\left(x_i, w_i, \frac{w_{i+1} - w_{i-1}}{2h}\right)
$$

- Requires $f$, $f_y$, and $f_{y'}$ continuous; $f_y(x, y, y') \geq \delta > 0$.
- Unique solution exists if $h < \frac{2}{L}$, with $L$ related to bounds on derivatives.
- Newton's method is used to solve the nonlinear system iteratively.



<br>

## Study Notes

### MA3024 Numerical Methods: Boundary Value Problems (BVPs) 📚


### 1. 🧩 Introduction to Boundary Value Problems (BVPs)

When solving differential equations, you often encounter problems where the solution is required to satisfy certain conditions. In many cases, these conditions are specified at a single point, usually the start of the interval. These are called **Initial Value Problems (IVPs)**.

However, in **Boundary Value Problems (BVPs)**, the conditions are given at two distinct points, typically at the ends of the interval. For example, consider a second-order differential equation where you want to find a function $y(x)$ such that:


$$
y'' = f(x, y, y')
$$


with boundary conditions:


$$
y(a) = \alpha, \quad y(b) = \beta
$$


Here, $a$ and $b$ are the boundaries of the domain, and $\alpha$, $\beta$ are the specified values of the solution at these points. This is fundamentally different from IVPs because the solution must satisfy conditions at two points, not just one.


### 2. 🔍 Existence and Uniqueness of Solutions for BVPs

Before attempting to solve a BVP, it is important to know whether a solution exists and whether it is unique. This is guaranteed under certain conditions.

**Theorem 1** states that if the function $f(x, y, y')$ in the differential equation is continuous over a domain $D$, and its partial derivatives with respect to $y$ and $y'$ (denoted $f_y$ and $f_{y'}$) are also continuous, then:

1. $f_y(x, y, y') > 0$ for all points in $D$.
2. There exists a constant $M > 0$ such that $|f_{y'}(x, y, y')| \leq M$ for all points in $D$.

Under these conditions, the BVP has a **unique solution** on the interval $[a, b]$.

#### Example:

Consider the BVP:


$$
y'' + e^{-x} y + \sin(y') = 0, \quad 1 \leq x \leq 2, \quad y(1) = 0, \quad y(2) = 0
$$


Rearranged as:


$$
y'' = -e^{-x} y - \sin(y')
$$


Here, $f(x, y, y') = -e^{-x} y - \sin(y')$.

- $f_y = -e^{-x}$, which is negative but since the theorem requires $f_y > 0$, we check the absolute value or the specific problem context.
- $f_{y'} = -\cos(y')$, and since $|\cos(y')| \leq 1$, the boundedness condition holds.

By the theorem, this BVP has a unique solution.


### 3. 🎯 Linear Shooting Method for Linear BVPs

The **Linear Shooting Method** is a technique to solve linear BVPs by converting them into initial value problems (IVPs), which are easier to solve numerically.

#### Setup:

Consider a linear second-order BVP of the form:


$$
y'' = p(x) y' + q(x) y + r(x), \quad a \leq x \leq b
$$


with boundary conditions:


$$
y(a) = \alpha, \quad y(b) = \beta
$$


#### How the method works:

1. Solve two IVPs:
   - $y_1(x)$ solves the equation with initial conditions $y_1(a) = \alpha$, $y_1'(a) = 0$.
   - $y_2(x)$ solves the equation with initial conditions $y_2(a) = 0$, $y_2'(a) = 1$.

2. The solution to the BVP is then constructed as:


$$
y(x) = y_1(x) + c y_2(x)
$$


where the constant $c$ is chosen so that the boundary condition at $x = b$ is satisfied:


$$
y(b) = y_1(b) + c y_2(b) = \beta \implies c = \frac{\beta - y_1(b)}{y_2(b)}
$$


This reduces the BVP to solving two IVPs, which can be done using numerical methods like the **fourth-order Runge-Kutta method**.


### 4. 🔄 Non-linear Shooting Method

For **non-linear BVPs**, the shooting method is more complex because the relationship between the initial slope and the boundary value at $b$ is non-linear.

#### Procedure:

1. Guess an initial slope $t_0 = y'(a)$.
2. Solve the IVP with $y(a) = \alpha$ and $y'(a) = t_0$ to get $y(x, t_0)$.
3. Check if $y(b, t_0)$ is close enough to $\beta$. If not, update the guess $t$ using **Newton's method** to solve:


$$
F(t) = y(b, t) - \beta = 0
$$


4. Newton's iteration formula is:


$$
t_{k+1} = t_k - \frac{F(t_k)}{F'(t_k)} = t_k - \frac{y(b, t_k) - \beta}{\frac{\partial y}{\partial t}(b, t_k)}
$$


5. Since $\frac{\partial y}{\partial t}(b, t_k)$ is not known analytically, we define:


$$
z(x, t) = \frac{\partial y}{\partial t}(x, t)
$$


and derive an IVP for $z$ by differentiating the original ODE with respect to $t$. The initial conditions for $z$ are:


$$
z(a, t) = 0, \quad z'(a, t) = 1
$$


6. Solve the IVP for $z$ alongside $y$, then update $t$ using Newton's method until convergence.


### 5. 🧮 Finite Difference Methods for Linear BVPs

The **Finite Difference Method (FDM)** approximates derivatives by differences on a discrete grid, turning the differential equation into a system of algebraic equations.

#### Steps:

1. Partition the interval $[a, b]$ into $N+1$ equal subintervals with mesh points:


$$
x_i = a + i h, \quad h = \frac{b - a}{N+1}, \quad i = 0, 1, \ldots, N+1
$$


2. Approximate derivatives at interior points $x_i$ using **centered difference formulas**:

- For the second derivative $y''(x_i)$:


$$
y''(x_i) \approx \frac{y_{i-1} - 2 y_i + y_{i+1}}{h^2}
$$


- For the first derivative $y'(x_i)$:


$$
y'(x_i) \approx \frac{y_{i+1} - y_{i-1}}{2h}
$$


3. Substitute these approximations into the differential equation at each interior point to get a system of linear equations in terms of $w_i \approx y(x_i)$.

4. This system can be written in matrix form:


$$
A \mathbf{w} = \mathbf{b}
$$


where $A$ is a tridiagonal matrix derived from the coefficients of the finite difference approximations, and $\mathbf{b}$ includes boundary conditions and source terms.

5. Solve the linear system using standard numerical linear algebra techniques.

#### Existence and uniqueness:

- If $p(x), q(x), r(x)$ are continuous on $[a, b]$ and $q(x) \geq 0$, then the finite difference system has a unique solution provided the step size $h$ is sufficiently small (specifically, $h < 2/L$, where $L$ is related to the maximum of $|p(x)|$).


### 6. 🔧 Finite Difference Methods for Non-linear BVPs

For **non-linear BVPs**, the finite difference approach is similar but results in a system of **non-linear algebraic equations**.

#### Key points:

- The non-linear BVP is:


$$
y'' = f(x, y, y'), \quad y(a) = \alpha, \quad y(b) = \beta
$$


- Using the same mesh and centered difference formulas, substitute into the equation to get:


$$
\frac{w_{i-1} - 2 w_i + w_{i+1}}{h^2} = f\left(x_i, w_i, \frac{w_{i+1} - w_{i-1}}{2h}\right)
$$


for $i = 1, 2, \ldots, N$.

- This forms a system of $N$ non-linear equations in $N$ unknowns $w_i$.

#### Solving the system:

- Use **Newton's method** for systems of non-linear equations:
  - Start with an initial guess for $\mathbf{w}$.
  - Linearize the system around the current guess.
  - Solve the linearized system to update the guess.
  - Repeat until convergence.

#### Conditions for uniqueness:

- The function $f$ and its partial derivatives $f_y$, $f_{y'}$ are continuous.
- $f_y(x, y, y') \geq \delta > 0$ for some positive constant $\delta$.
- There exist constants $k, L$ bounding the derivatives.
- The step size $h$ must satisfy $h < 2/L$ for uniqueness.


### Summary

- **Boundary Value Problems (BVPs)** require solutions satisfying conditions at two points.
- Existence and uniqueness depend on continuity and positivity conditions on $f$ and its derivatives.
- The **Shooting Method** converts BVPs into IVPs; linear problems use a direct approach, non-linear problems require iterative Newton updates.
- **Finite Difference Methods** discretize the domain and approximate derivatives, leading to linear or non-linear algebraic systems.
- Newton's method is essential for solving non-linear systems arising from non-linear BVPs.