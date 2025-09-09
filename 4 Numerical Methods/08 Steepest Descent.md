## Steepest Descent

## Study Notes

### 1. 🔍 Introduction to Steepest Descent Method

When solving systems of nonlinear equations, one common approach is to find the roots of the system — that is, the values of variables that satisfy all equations simultaneously. Newton’s method is a popular technique for this because it converges quickly when the initial guess is close to the true solution. However, Newton’s method can fail or converge to incorrect solutions if the starting point is far from the actual root.

The **Steepest Descent Method** offers a more robust alternative in such cases. Although it converges more slowly, it is much more tolerant of poor initial guesses. This makes it a useful tool to find a "good enough" starting point for faster methods like Newton’s method. Essentially, steepest descent can be used to "warm up" the solution process by moving closer to the solution before switching to a faster but less forgiving method.


### 2. 🧮 Problem Setup and Objective

We consider a system of $n$ nonlinear equations with $n$ variables:


$$
F(x) = 0
$$


where $F: \mathbb{R}^n \to \mathbb{R}^n$ is a vector-valued function.

To solve this system, we define a scalar function $g: \mathbb{R}^n \to \mathbb{R}$ that measures how far we are from satisfying the system:


$$
g(x) = \frac{1}{2} \| F(x) \|^2 = \frac{1}{2} \sum_{i=1}^n f_i(x)^2
$$


The goal is to **minimize** $g(x)$. Notice that $g(x) \geq 0$ always, and $g(x) = 0$ if and only if $F(x) = 0$. So, finding the root of the system is equivalent to finding the minimum of $g$.


### 3. 📐 Understanding the Gradient and Its Role

#### What is the Gradient?

For functions of multiple variables, the gradient is a vector that points in the direction of the greatest rate of increase of the function. For our function $g(x)$, the gradient is:


$$
\nabla g(x) = \left( \frac{\partial g}{\partial x_1}, \frac{\partial g}{\partial x_2}, \ldots, \frac{\partial g}{\partial x_n} \right)^T
$$


This vector tells us how $g$ changes as we move in each coordinate direction.

#### Gradient of $g$ in terms of $F$

Using the chain rule and the Jacobian matrix $J_F(x)$ of $F$, the gradient of $g$ can be expressed as:


$$
\nabla g(x) = J_F(x)^T F(x)
$$


where $J_F(x)$ is the matrix of partial derivatives of each $f_i$ with respect to each variable $x_j$.


### 4. ⬇️ The Steepest Descent Algorithm Explained

#### Intuition

At any point $x^{(k)}$, the steepest descent method moves in the direction where $g$ decreases the fastest. This direction is the **negative gradient** $-\nabla g(x^{(k)})$.

#### Update Rule

Starting from an initial guess $x^{(0)}$, the next point is:


$$
x^{(k+1)} = x^{(k)} - \alpha_k \nabla g(x^{(k)})
$$


where $\alpha_k > 0$ is the step size or learning rate.

#### Choosing the Step Size $\alpha$

Choosing the right $\alpha$ is crucial. Too large, and the method might overshoot the minimum; too small, and convergence will be very slow.

To find the best $\alpha$, we define a function:


$$
h(\alpha) = g(x^{(k)} - \alpha \nabla g(x^{(k)}))
$$


We want to find $\hat{\alpha}$ that minimizes $h(\alpha)$.


### 5. 🔍 Finding the Optimal Step Size $\hat{\alpha}$ Using Quadratic Interpolation

Directly minimizing $h(\alpha)$ analytically is often too expensive. Instead, we use an **interpolation technique**:

1. **Initialize**: Set $\alpha_1 = 0$ and $\alpha_3 = 1$.
2. **Check values**: Compute $h(\alpha_1)$ and $h(\alpha_3)$.
   - If $h(\alpha_3) < h(\alpha_1)$, accept $\alpha_3 = 1$.
   - Otherwise, reduce $\alpha_3$ by half repeatedly until $h(\alpha_3) < h(\alpha_1)$ or $\alpha_3$ is very small.
3. **Midpoint**: Set $\alpha_2 = \frac{\alpha_1 + \alpha_3}{2}$.
4. **Quadratic interpolation**: Use the points $(\alpha_1, h(\alpha_1))$, $(\alpha_2, h(\alpha_2))$, and $(\alpha_3, h(\alpha_3))$ to fit a quadratic polynomial $P(\alpha)$.
5. **Minimize $P(\alpha)$**: Solve $P'(\alpha) = 0$ to find the minimum $\alpha_0$.
6. **Choose $\hat{\alpha}$**: Pick the $\alpha$ in $[ \alpha_1, \alpha_3 ]$ that gives the smallest $h(\alpha)$.

This process efficiently approximates the best step size without expensive derivative calculations.


### 6. 🧩 Example Walkthrough

Consider the system:


$$
\begin{cases}
f_1(x_1, x_2, x_3) = 3x_1 - \cos(x_2 x_3) - 1 = 0 \\
f_2(x_1, x_2, x_3) = 81(x_2 + 0.1)^2 + \sin x_3 + 1.06 = 0
\end{cases}
$$


Starting with an initial guess $x^{(0)}$, we:

- Compute the gradient $\nabla g(x^{(0)})$.
- Normalize it to get the unit vector $z$ in the direction of steepest descent.
- Find the optimal step size $\hat{\alpha}$ using the interpolation method described.
- Update the guess:


$$
x^{(1)} = x^{(0)} - \hat{\alpha} z
$$


This new point $x^{(1)}$ is a better approximation and can be used as a starting point for Newton’s method.


### 7. ⏳ Convergence and Practical Considerations

- **Slow convergence**: The steepest descent method typically converges slowly. For example, it may take dozens of iterations to get close to the solution.
- **Robustness**: Despite slow convergence, it is very tolerant of poor initial guesses and will eventually approach the solution.
- **Hybrid approach**: Often, steepest descent is used for a few iterations to get a reasonable initial guess, then Newton’s method or other faster methods take over.
- **Stopping criteria**: In practice, you stop when $g(x^{(k)})$ is sufficiently close to zero or when the change in $x^{(k)}$ becomes very small.


### Summary

The **Steepest Descent Method** is a fundamental numerical technique for solving nonlinear systems by minimizing a scalar function $g$ that measures the error. It moves iteratively in the direction of the negative gradient, adjusting the step size carefully to ensure progress. While slow, it is reliable and often used to prepare a good initial guess for faster methods like Newton’s method.