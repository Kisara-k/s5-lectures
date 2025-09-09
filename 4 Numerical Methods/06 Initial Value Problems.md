## Initial Value Problems

## Study Notes

### 1. 🧩 Introduction to Initial Value Problems (IVPs)

When studying how things change over time, such as the swinging of a pendulum, we often use **differential equations**. These equations describe how a quantity changes at any moment. For example, the angle $\theta(t)$ of a pendulum at time $t$ can be described by a differential equation.

An **Initial Value Problem (IVP)** is a differential equation together with specific starting information — the initial values. For the pendulum, this means knowing the initial angle $\theta(0)$ and the initial speed $\theta'(0)$ at the start time $t=0$.

- The differential equation tells us how $\theta(t)$ changes.
- The initial values tell us where the motion starts.

Together, these form an IVP: find the function $\theta(t)$ that satisfies the differential equation and matches the initial conditions.

**Why IVPs matter:** Many real-world problems are modeled as IVPs. However, most IVPs cannot be solved exactly with formulas (analytically). Instead, we use **numerical methods** to approximate solutions.


### 2. 📏 Theory Behind IVPs: Existence, Uniqueness, and Well-Posedness

Before approximating solutions, it’s important to know if a solution exists, if it’s unique, and if the problem is stable (well-posed).

#### Lipschitz Condition

A key concept is the **Lipschitz condition**, which controls how fast the function $f(t, y)$ (from the differential equation $y' = f(t, y)$) can change with respect to $y$.

- A function $f(t, y)$ satisfies a **Lipschitz condition** if there is a constant $L > 0$ such that for any two values $y_1$ and $y_2$, the difference in $f$ values is at most $L$ times the difference in $y$ values.
- Intuitively, this means $f$ doesn’t change too wildly as $y$ changes.

#### Convex Sets

A set $D$ in the plane is **convex** if, whenever you pick two points in $D$, the entire line segment between them is also inside $D$. This property is important for applying certain theorems about IVPs.

#### Existence and Uniqueness Theorem

If $f(t, y)$ is continuous and satisfies the Lipschitz condition on a convex set $D$, then the IVP has a **unique solution** on the interval $[a, b]$.

- This means the problem is well-defined: there is one and only one function $y(t)$ that fits the differential equation and initial values.

#### Well-Posed Problems

A problem is **well-posed** if:

1. A unique solution exists.
2. Small changes in the initial data or the function $f$ cause only small changes in the solution.

This is crucial for numerical methods because computers work with approximations and rounding errors. If the problem is not well-posed, tiny errors could cause huge differences in the solution, making numerical approximations unreliable.

**Summary:** Checking the Lipschitz condition is a practical way to verify if an IVP is well-posed.


### 3. 🧮 Euler’s Method: The Basic Numerical Approach

Euler’s method is the simplest way to approximate solutions to IVPs numerically.

#### How Euler’s Method Works

- We divide the time interval $[a, b]$ into $N$ equal parts, called **mesh points**: $t_0, t_1, ..., t_N$.
- The step size is $h = \frac{b - a}{N}$.
- Starting from the initial value $y(t_0) = y_0$, we approximate the solution at each mesh point using the formula:


$$
w_{i+1} = w_i + h f(t_i, w_i)
$$


Here, $w_i$ approximates $y(t_i)$.

#### Intuition Behind Euler’s Method

Euler’s method uses the idea of a **tangent line approximation**:

- At each point $(t_i, w_i)$, the slope of the solution curve is approximately $f(t_i, w_i)$.
- We move forward a small step $h$ along this slope to estimate the next value $w_{i+1}$.

#### Example

For the IVP $y' = y - t^2 + 1$, $y(0) = 0.5$, with $N=4$ and $h=0.5$, Euler’s method calculates approximate values at $t=0.5, 1.0, 1.5, 2.0$.

#### Error in Euler’s Method

- The error is proportional to the step size $h$ (order 1).
- Smaller $h$ means better accuracy but more computation.
- However, very small $h$ can increase rounding errors due to finite precision in computers.


### 4. 🚀 Runge-Kutta Methods: More Accurate Numerical Solutions

Euler’s method is simple but not very accurate. Runge-Kutta methods improve accuracy by using more sophisticated approximations.

#### Why Runge-Kutta?

- Higher order Taylor expansions give better approximations but require derivatives of $f$, which can be hard or expensive to compute.
- Runge-Kutta methods cleverly approximate these derivatives by evaluating $f$ at several points within each step.

#### Midpoint Method (Second Order Runge-Kutta)

- Uses the slope at the midpoint of the interval to improve the estimate.
- Formula:


$$
w_{i+1} = w_i + h f\left(t_i + \frac{h}{2}, w_i + \frac{h}{2} f(t_i, w_i)\right)
$$


#### Modified Euler Method

- Averages the slope at the beginning and the end of the interval.
- Formula:


$$
w_{i+1} = w_i + \frac{h}{2} \left[f(t_i, w_i) + f(t_{i+1}, w_i + h f(t_i, w_i))\right]
$$


#### Fourth Order Runge-Kutta (Most Common)

- Uses four slope evaluations per step.
- Very accurate with error order $h^4$.
- Formula involves calculating four intermediate slopes $k_1, k_2, k_3, k_4$ and combining them.

#### Comparison of Methods

| Method               | Error Order | Number of $f$ Evaluations per Step |
|----------------------|-------------|-------------------------------------|
| Euler                | 1           | 1                                   |
| Midpoint             | 2           | 2                                   |
| Modified Euler       | 2           | 2                                   |
| Fourth Order Runge-Kutta | 4       | 4                                   |

Runge-Kutta methods provide much better accuracy for the same step size compared to Euler’s method.


### 5. 🔄 Multi-Step Methods: Using More Past Information

One-step methods like Euler and Runge-Kutta use only the last point to find the next approximation. **Multi-step methods** use several previous points to improve accuracy.

#### General Form

An $m$-step method uses the last $m$ approximations $w_i, w_{i-1}, ..., w_{i-m+1}$ to compute $w_{i+1}$.

- These methods can be **explicit** (next value depends only on known values) or **implicit** (next value appears on both sides of the equation).

#### Adams Methods

Two important families of multi-step methods:

- **Adams-Bashforth (Explicit):** Use past function values to predict the next value.
- **Adams-Moulton (Implicit):** Use past and next function values, requiring solving an equation for $w_{i+1}$.

#### Predictor-Corrector Methods

- Combine explicit and implicit methods.
- Use an explicit method to predict $w_{i+1}$.
- Use this prediction in an implicit method to correct and improve the estimate.
- This approach balances accuracy and computational effort.


### 6. 🔢 Numerical Solutions for Systems of IVPs

Many problems involve **systems** of differential equations, not just one equation.

#### System of IVPs

A system looks like:


$$
\begin{cases}
u_1' = f_1(t, u_1, u_2, ..., u_m) \\
u_2' = f_2(t, u_1, u_2, ..., u_m) \\
\vdots \\
u_m' = f_m(t, u_1, u_2, ..., u_m)
\end{cases}
$$


with initial conditions $u_j(a) = \alpha_j$.

#### Existence and Uniqueness for Systems

- Similar Lipschitz conditions apply, but now for vector-valued functions.
- If each $f_j$ and its partial derivatives are continuous and satisfy Lipschitz conditions, the system has a unique solution.

#### Numerical Methods for Systems

- Runge-Kutta methods extend naturally to systems.
- For each component $u_j$, calculate intermediate slopes $k_{i,1}^j, k_{i,2}^j, ...$ and update approximations.
- This allows simultaneous approximation of all functions $u_1(t), ..., u_m(t)$.


### 7. 🔄 Converting Higher-Order IVPs to Systems

Higher-order differential equations (e.g., second order) can be rewritten as systems of first-order equations.

#### Example

For a second-order IVP:


$$
y'' = g(t, y, y')
$$


Define:


$$
u_1 = y, \quad u_2 = y'
$$


Then:


$$
\begin{cases}
u_1' = u_2 \\
u_2' = g(t, u_1, u_2)
\end{cases}
$$


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