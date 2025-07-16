## Steepest Descent

[Study Notes](#study-notes)

[Questions](#questions)



### Key Points

#### 1. 🔄 Steepest Descent Method Overview
- Steepest descent is a modified gradient descent method used to approximate solutions to nonlinear systems.
- It converges slowly but is tolerant of poor initial guesses.
- Often used to find a good initial guess for faster methods like Newton’s method.

#### 2. 🧮 Problem Setup
- The system of nonlinear equations \( F(x) = 0 \) is transformed into minimizing \( g(x) = \frac{1}{2} \|F(x)\|^2 \).
- The solution to the system corresponds to the minimum of \( g(x) \), where \( g(x) = 0 \).

#### 3. 📐 Gradient and Jacobian
- The gradient of \( g \) is given by \( \nabla g(x) = J_F(x)^T F(x) \), where \( J_F(x) \) is the Jacobian matrix of \( F \).
- The gradient points in the direction of the steepest increase of \( g \).

#### 4. ⬇️ Update Rule in Steepest Descent
- The update formula is \( x^{(k+1)} = x^{(k)} - \alpha_k \nabla g(x^{(k)}) \), where \( \alpha_k > 0 \) is the step size.
- The direction of steepest descent is the negative gradient \( -\nabla g(x^{(k)}) \).

#### 5. 🎯 Step Size Selection (α)
- The optimal step size \( \hat{\alpha} \) minimizes \( h(\alpha) = g(x^{(k)} - \alpha \nabla g(x^{(k)})) \).
- Direct analytical minimization is expensive; instead, quadratic interpolation is used.
- The interpolation uses three points \( (\alpha_1, h(\alpha_1)) \), \( (\alpha_2, h(\alpha_2)) \), and \( (\alpha_3, h(\alpha_3)) \) to approximate \( h(\alpha) \).

#### 6. 🔍 Quadratic Interpolation Steps
- Initialize \( \alpha_1 = 0 \), \( \alpha_3 = 1 \).
- Adjust \( \alpha_3 \) by bisection until \( h(\alpha_3) < h(\alpha_1) \) or tolerance is reached.
- Set \( \alpha_2 = \frac{\alpha_1 + \alpha_3}{2} \).
- Fit quadratic polynomial \( P(\alpha) \) through the three points.
- Find \( \alpha_0 \) minimizing \( P(\alpha) \) by solving \( P'(\alpha_0) = 0 \).
- Choose \( \hat{\alpha} \) as the minimizer of \( P(\alpha) \) in the interval \([ \alpha_1, \alpha_3 ]\).

#### 7. ⚠️ Convergence Characteristics
- Steepest descent converges slowly; it may require many iterations (e.g., 70) to get close to the solution.
- Despite slow convergence, it is robust to initial guesses far from the solution.
- Typically used for a few iterations to improve initial guess before applying faster methods.

#### 8. 🧩 Practical Use Case
- After one or two iterations of steepest descent, the updated point \( x^{(k)} \) can serve as a good initial guess for Newton’s method.
- Using the unit vector in the direction of the gradient instead of the raw gradient is common in practice for stability.



<br>

## Study Notes

### 1. 🔍 Introduction to Steepest Descent Method

When solving systems of nonlinear equations, one common approach is to find the roots of the system — that is, the values of variables that satisfy all equations simultaneously. Newton’s method is a popular technique for this because it converges quickly when the initial guess is close to the true solution. However, Newton’s method can fail or converge to incorrect solutions if the starting point is far from the actual root.

The **Steepest Descent Method** offers a more robust alternative in such cases. Although it converges more slowly, it is much more tolerant of poor initial guesses. This makes it a useful tool to find a "good enough" starting point for faster methods like Newton’s method. Essentially, steepest descent can be used to "warm up" the solution process by moving closer to the solution before switching to a faster but less forgiving method.


### 2. 🧮 Problem Setup and Objective

We consider a system of \( n \) nonlinear equations with \( n \) variables:

\[
F(x) = 0
\]

where \( F: \mathbb{R}^n \to \mathbb{R}^n \) is a vector-valued function.

To solve this system, we define a scalar function \( g: \mathbb{R}^n \to \mathbb{R} \) that measures how far we are from satisfying the system:

\[
g(x) = \frac{1}{2} \| F(x) \|^2 = \frac{1}{2} \sum_{i=1}^n f_i(x)^2
\]

The goal is to **minimize** \( g(x) \). Notice that \( g(x) \geq 0 \) always, and \( g(x) = 0 \) if and only if \( F(x) = 0 \). So, finding the root of the system is equivalent to finding the minimum of \( g \).


### 3. 📐 Understanding the Gradient and Its Role

#### What is the Gradient?

For functions of multiple variables, the gradient is a vector that points in the direction of the greatest rate of increase of the function. For our function \( g(x) \), the gradient is:

\[
\nabla g(x) = \left( \frac{\partial g}{\partial x_1}, \frac{\partial g}{\partial x_2}, \ldots, \frac{\partial g}{\partial x_n} \right)^T
\]

This vector tells us how \( g \) changes as we move in each coordinate direction.

#### Gradient of \( g \) in terms of \( F \)

Using the chain rule and the Jacobian matrix \( J_F(x) \) of \( F \), the gradient of \( g \) can be expressed as:

\[
\nabla g(x) = J_F(x)^T F(x)
\]

where \( J_F(x) \) is the matrix of partial derivatives of each \( f_i \) with respect to each variable \( x_j \).


### 4. ⬇️ The Steepest Descent Algorithm Explained

#### Intuition

At any point \( x^{(k)} \), the steepest descent method moves in the direction where \( g \) decreases the fastest. This direction is the **negative gradient** \( -\nabla g(x^{(k)}) \).

#### Update Rule

Starting from an initial guess \( x^{(0)} \), the next point is:

\[
x^{(k+1)} = x^{(k)} - \alpha_k \nabla g(x^{(k)})
\]

where \( \alpha_k > 0 \) is the step size or learning rate.

#### Choosing the Step Size \( \alpha \)

Choosing the right \( \alpha \) is crucial. Too large, and the method might overshoot the minimum; too small, and convergence will be very slow.

To find the best \( \alpha \), we define a function:

\[
h(\alpha) = g(x^{(k)} - \alpha \nabla g(x^{(k)}))
\]

We want to find \( \hat{\alpha} \) that minimizes \( h(\alpha) \).


### 5. 🔍 Finding the Optimal Step Size \( \hat{\alpha} \) Using Quadratic Interpolation

Directly minimizing \( h(\alpha) \) analytically is often too expensive. Instead, we use an **interpolation technique**:

1. **Initialize**: Set \( \alpha_1 = 0 \) and \( \alpha_3 = 1 \).
2. **Check values**: Compute \( h(\alpha_1) \) and \( h(\alpha_3) \).
   - If \( h(\alpha_3) < h(\alpha_1) \), accept \( \alpha_3 = 1 \).
   - Otherwise, reduce \( \alpha_3 \) by half repeatedly until \( h(\alpha_3) < h(\alpha_1) \) or \( \alpha_3 \) is very small.
3. **Midpoint**: Set \( \alpha_2 = \frac{\alpha_1 + \alpha_3}{2} \).
4. **Quadratic interpolation**: Use the points \((\alpha_1, h(\alpha_1))\), \((\alpha_2, h(\alpha_2))\), and \((\alpha_3, h(\alpha_3))\) to fit a quadratic polynomial \( P(\alpha) \).
5. **Minimize \( P(\alpha) \)**: Solve \( P'(\alpha) = 0 \) to find the minimum \( \alpha_0 \).
6. **Choose \( \hat{\alpha} \)**: Pick the \( \alpha \) in \([ \alpha_1, \alpha_3 ]\) that gives the smallest \( h(\alpha) \).

This process efficiently approximates the best step size without expensive derivative calculations.


### 6. 🧩 Example Walkthrough

Consider the system:

\[
\begin{cases}
f_1(x_1, x_2, x_3) = 3x_1 - \cos(x_2 x_3) - 1 = 0 \\
f_2(x_1, x_2, x_3) = 81(x_2 + 0.1)^2 + \sin x_3 + 1.06 = 0
\end{cases}
\]

Starting with an initial guess \( x^{(0)} \), we:

- Compute the gradient \( \nabla g(x^{(0)}) \).
- Normalize it to get the unit vector \( z \) in the direction of steepest descent.
- Find the optimal step size \( \hat{\alpha} \) using the interpolation method described.
- Update the guess:

\[
x^{(1)} = x^{(0)} - \hat{\alpha} z
\]

This new point \( x^{(1)} \) is a better approximation and can be used as a starting point for Newton’s method.


### 7. ⏳ Convergence and Practical Considerations

- **Slow convergence**: The steepest descent method typically converges slowly. For example, it may take dozens of iterations to get close to the solution.
- **Robustness**: Despite slow convergence, it is very tolerant of poor initial guesses and will eventually approach the solution.
- **Hybrid approach**: Often, steepest descent is used for a few iterations to get a reasonable initial guess, then Newton’s method or other faster methods take over.
- **Stopping criteria**: In practice, you stop when \( g(x^{(k)}) \) is sufficiently close to zero or when the change in \( x^{(k)} \) becomes very small.


### Summary

The **Steepest Descent Method** is a fundamental numerical technique for solving nonlinear systems by minimizing a scalar function \( g \) that measures the error. It moves iteratively in the direction of the negative gradient, adjusting the step size carefully to ensure progress. While slow, it is reliable and often used to prepare a good initial guess for faster methods like Newton’s method.



<br>

## Questions

#### 1. What is the primary goal when applying the steepest descent method to a system of nonlinear equations?  
A) To find the maximum of the function \( g(x) = \frac{1}{2} \|F(x)\|^2 \)  
B) To minimize the function \( g(x) = \frac{1}{2} \|F(x)\|^2 \)  
C) To solve \( F(x) = 0 \) by minimizing \( g(x) \)  
D) To maximize the norm of the gradient \( \nabla g(x) \)


#### 2. Which of the following statements about the gradient \( \nabla g(x) \) is true?  
A) It points in the direction of the steepest increase of \( g \)  
B) It is always zero at the solution of \( F(x) = 0 \)  
C) It can be computed as \( J_F(x)^T F(x) \), where \( J_F(x) \) is the Jacobian of \( F \)  
D) It is a scalar value representing the slope of \( g \)


#### 3. Why is the steepest descent method considered more tolerant to poor initial guesses compared to Newton’s method?  
A) Because it uses the Hessian matrix to adjust steps  
B) Because it moves iteratively in the direction of the negative gradient, which always points downhill  
C) Because it converges faster than Newton’s method  
D) Because it does not require the Jacobian matrix


#### 4. Which of the following best describes the update step in the steepest descent method?  
A) \( x^{(k+1)} = x^{(k)} + \alpha_k \nabla g(x^{(k)}) \)  
B) \( x^{(k+1)} = x^{(k)} - \alpha_k \nabla g(x^{(k)}) \)  
C) \( x^{(k+1)} = x^{(k)} - \alpha_k J_F(x^{(k)}) F(x^{(k)}) \)  
D) \( x^{(k+1)} = x^{(k)} - \alpha_k \nabla F(x^{(k)}) \)


#### 5. What is the role of the step size \( \alpha \) in the steepest descent method?  
A) It controls how far we move along the negative gradient direction  
B) It determines the direction of the next step  
C) It is always fixed to 1 for simplicity  
D) It must be chosen carefully to balance convergence speed and stability


#### 6. Which of the following statements about the step size selection using quadratic interpolation is correct?  
A) It requires computing the second derivative of \( h(\alpha) \) explicitly  
B) It uses three points to fit a quadratic polynomial to approximate \( h(\alpha) \)  
C) It always chooses \( \alpha = 1 \) as the optimal step size  
D) It involves evaluating \( h(\alpha) \) at multiple points between 0 and 1


#### 7. In the context of steepest descent, what does the function \( h(\alpha) = g(x^{(k)} - \alpha \nabla g(x^{(k)})) \) represent?  
A) The value of \( g \) after moving a distance \( \alpha \) in the negative gradient direction  
B) The gradient of \( g \) at \( x^{(k)} \) scaled by \( \alpha \)  
C) The Jacobian of \( F \) at the new point  
D) The error in the approximation of \( F(x) = 0 \)


#### 8. Why might the steepest descent method require many iterations to converge?  
A) Because it always moves in the direction of the Hessian matrix  
B) Because the negative gradient direction may zigzag near narrow valleys of \( g \)  
C) Because it uses a fixed step size that is too large  
D) Because it does not use second-order derivative information


#### 9. Which of the following is a valid reason to use steepest descent before Newton’s method?  
A) To find a good initial guess that is close enough for Newton’s method to converge  
B) To avoid computing the Jacobian matrix altogether  
C) To guarantee global convergence in all cases  
D) To speed up the overall convergence by combining slow and fast methods


#### 10. Consider the gradient vector \( \nabla g(x) \). Why might one use the unit vector in the direction of the gradient instead of the raw gradient in the update step?  
A) To ensure the step size \( \alpha \) controls the entire step length  
B) To avoid excessively large steps when the gradient magnitude is large  
C) To simplify the computation of the Jacobian matrix  
D) To guarantee convergence in fewer iterations


#### 11. Which of the following statements about the Jacobian matrix \( J_F(x) \) is true?  
A) It is a square matrix of partial derivatives of \( F \) with respect to \( x \)  
B) It is used to compute the gradient of \( g \) as \( J_F(x)^T F(x) \)  
C) It is not needed in the steepest descent method  
D) It provides second-order derivative information


#### 12. What happens if the initial guess \( x^{(0)} \) is very far from the actual solution when using Newton’s method?  
A) Newton’s method will always converge faster than steepest descent  
B) Newton’s method may fail to converge or converge to a pseudo solution  
C) Steepest descent will also fail to converge  
D) Steepest descent can still converge, albeit slowly


#### 13. When performing the quadratic interpolation to find \( \hat{\alpha} \), what is the significance of the point \( \alpha_0 \) where \( P'(\alpha_0) = 0 \)?  
A) It is the point where the quadratic polynomial \( P(\alpha) \) attains its minimum or maximum  
B) It is always the global minimum of \( h(\alpha) \)  
C) It is used to update the guess \( x^{(k+1)} \) if it reduces \( h(\alpha) \)  
D) It corresponds to the maximum step size allowed


#### 14. Which of the following best describes the convergence behavior of the steepest descent method?  
A) It converges linearly and can be very slow near the solution  
B) It converges quadratically like Newton’s method  
C) It may never converge if the initial guess is poor  
D) It converges faster if the gradient norm is large


#### 15. In the example system given, why is it beneficial to perform one or two iterations of steepest descent before switching to Newton’s method?  
A) Because steepest descent can quickly reduce \( g(x) \) to zero  
B) Because it provides a better initial guess that improves Newton’s method convergence  
C) Because Newton’s method does not require an initial guess  
D) Because steepest descent uses less computational resources per iteration


#### 16. Which of the following is NOT a reason why the steepest descent method might be preferred in some cases?  
A) It is more robust to poor initial guesses  
B) It requires fewer iterations than Newton’s method  
C) It does not require the Hessian matrix  
D) It can be used to generate initial guesses for faster methods


#### 17. How does the steepest descent method handle the direction of movement in the solution space?  
A) It moves in the direction of the positive gradient  
B) It moves in the direction of the negative gradient  
C) It moves in a random direction at each iteration  
D) It moves in the direction of the Newton step


#### 18. What is the relationship between the function \( g(x) \) and the system \( F(x) = 0 \)?  
A) \( g(x) \) is the sum of the squares of the components of \( F(x) \)  
B) \( g(x) \) is minimized exactly when \( F(x) = 0 \)  
C) \( g(x) \) is maximized when \( F(x) = 0 \)  
D) \( g(x) \) is unrelated to \( F(x) \)


#### 19. Which of the following statements about the use of bisection in finding \( \hat{\alpha} \) is correct?  
A) Bisection is used to find an interval where \( h(\alpha) \) decreases  
B) Bisection guarantees finding the global minimum of \( h(\alpha) \)  
C) Bisection halves the step size \( \alpha \) repeatedly until \( h(\alpha) < h(0) \)  
D) Bisection is used to compute the gradient \( \nabla g(x) \)


#### 20. Why is the steepest descent method considered a "modified" version of gradient descent in this context?  
A) Because it uses the Jacobian matrix instead of the gradient  
B) Because it applies to minimizing \( g(x) \) derived from a system of nonlinear equations  
C) Because it uses quadratic interpolation to find the step size  
D) Because it updates the solution using the Hessian matrix



<br>

## Answers

#### 1. What is the primary goal when applying the steepest descent method to a system of nonlinear equations?  
A) ✗ Maximizing \( g \) is not the goal; we want to minimize it.  
B) ✓ Correct; minimizing \( g(x) = \frac{1}{2} \|F(x)\|^2 \) leads to solving \( F(x) = 0 \).  
C) ✓ Correct; solving \( F(x) = 0 \) is equivalent to minimizing \( g \).  
D) ✗ Maximizing the gradient norm is not the objective.

**Correct:** B, C


#### 2. Which of the following statements about the gradient \( \nabla g(x) \) is true?  
A) ✓ Correct; gradient points in direction of steepest increase.  
B) ✓ Correct; at solution \( F(x) = 0 \), gradient \( \nabla g = J_F^T F = 0 \).  
C) ✓ Correct; gradient can be computed as \( J_F(x)^T F(x) \).  
D) ✗ Gradient is a vector, not a scalar.

**Correct:** A, B, C


#### 3. Why is the steepest descent method considered more tolerant to poor initial guesses compared to Newton’s method?  
A) ✗ Steepest descent does not use Hessian.  
B) ✓ Correct; negative gradient always points downhill, ensuring progress.  
C) ✗ It converges slower, not faster.  
D) ✗ Jacobian is needed to compute gradient.

**Correct:** B


#### 4. Which of the following best describes the update step in the steepest descent method?  
A) ✗ Moves in positive gradient direction, which increases \( g \).  
B) ✓ Correct; moves opposite to gradient to decrease \( g \).  
C) ✗ This is Newton’s update, not steepest descent.  
D) ✗ Gradient of \( F \) is not defined; gradient applies to scalar \( g \).

**Correct:** B


#### 5. What is the role of the step size \( \alpha \) in the steepest descent method?  
A) ✓ Correct; controls how far we move along negative gradient.  
B) ✗ Direction is given by gradient, not \( \alpha \).  
C) ✗ Step size is not fixed; it must be chosen carefully.  
D) ✓ Correct; balancing speed and stability is key.

**Correct:** A, D


#### 6. Which of the following statements about the step size selection using quadratic interpolation is correct?  
A) ✗ Second derivatives are not computed explicitly.  
B) ✓ Correct; three points are used to fit a quadratic polynomial.  
C) ✗ \( \alpha = 1 \) is only accepted if it reduces \( h(\alpha) \).  
D) ✓ Correct; multiple evaluations of \( h(\alpha) \) are needed.

**Correct:** B, D


#### 7. In the context of steepest descent, what does the function \( h(\alpha) = g(x^{(k)} - \alpha \nabla g(x^{(k)})) \) represent?  
A) ✓ Correct; value of \( g \) after stepping \( \alpha \) along negative gradient.  
B) ✗ It is not the gradient scaled by \( \alpha \).  
C) ✗ Jacobian is unrelated to \( h(\alpha) \).  
D) ✗ \( h(\alpha) \) measures function value, not error directly.

**Correct:** A


#### 8. Why might the steepest descent method require many iterations to converge?  
A) ✗ It does not use Hessian.  
B) ✓ Correct; zigzagging occurs near narrow valleys causing slow progress.  
C) ✗ Step size is chosen adaptively, not fixed large.  
D) ✓ Correct; lack of second-order info slows convergence.

**Correct:** B, D


#### 9. Which of the following is a valid reason to use steepest descent before Newton’s method?  
A) ✓ Correct; it finds a better initial guess for Newton’s method.  
B) ✗ Jacobian is still needed for gradient computation.  
C) ✗ No method guarantees global convergence in all cases.  
D) ✓ Correct; combining methods can speed up overall convergence.

**Correct:** A, D


#### 10. Consider the gradient vector \( \nabla g(x) \). Why might one use the unit vector in the direction of the gradient instead of the raw gradient in the update step?  
A) ✓ Correct; step size \( \alpha \) then controls full step length.  
B) ✓ Correct; normalizing avoids overly large steps from large gradients.  
C) ✗ Unit vector does not simplify Jacobian computation.  
D) ✗ Using unit vector does not guarantee fewer iterations.

**Correct:** A, B


#### 11. Which of the following statements about the Jacobian matrix \( J_F(x) \) is true?  
A) ✓ Correct; it is the matrix of partial derivatives of \( F \).  
B) ✓ Correct; used to compute gradient \( \nabla g = J_F^T F \).  
C) ✗ Jacobian is needed to compute gradient in steepest descent.  
D) ✗ Jacobian contains first derivatives, not second derivatives.

**Correct:** A, B


#### 12. What happens if the initial guess \( x^{(0)} \) is very far from the actual solution when using Newton’s method?  
A) ✗ Newton’s method may fail or converge incorrectly if guess is poor.  
B) ✓ Correct; poor initial guess can cause failure or pseudo solutions.  
C) ✗ Steepest descent is more tolerant and can still converge.  
D) ✓ Correct; steepest descent converges slowly but reliably.

**Correct:** B, D


#### 13. When performing the quadratic interpolation to find \( \hat{\alpha} \), what is the significance of the point \( \alpha_0 \) where \( P'(\alpha_0) = 0 \)?  
A) ✓ Correct; it is the extremum (minimum or maximum) of the quadratic fit.  
B) ✗ It may not be the global minimum of \( h(\alpha) \), only of \( P(\alpha) \).  
C) ✓ Correct; used if it reduces \( h(\alpha) \) compared to other points.  
D) ✗ It does not correspond to maximum step size.

**Correct:** A, C


#### 14. Which of the following best describes the convergence behavior of the steepest descent method?  
A) ✓ Correct; convergence is linear and can be slow near solution.  
B) ✗ Quadratic convergence is characteristic of Newton’s method, not steepest descent.  
C) ✗ Steepest descent converges eventually even from poor guesses.  
D) ✗ Large gradient norm does not guarantee faster convergence.

**Correct:** A


#### 15. In the example system given, why is it beneficial to perform one or two iterations of steepest descent before switching to Newton’s method?  
A) ✗ Steepest descent does not quickly reduce \( g \) to zero.  
B) ✓ Correct; it improves initial guess for Newton’s method.  
C) ✗ Newton’s method requires an initial guess.  
D) ✓ Correct; steepest descent iterations are computationally cheaper.

**Correct:** B, D


#### 16. Which of the following is NOT a reason why the steepest descent method might be preferred in some cases?  
A) ✗ Robustness to poor initial guesses is a reason to prefer it.  
B) ✓ Correct; it generally requires more iterations than Newton’s method.  
C) ✗ It does not require Hessian, which is an advantage.  
D) ✗ It is useful for generating initial guesses.

**Correct:** B


#### 17. How does the steepest descent method handle the direction of movement in the solution space?  
A) ✗ Moves opposite to positive gradient, not along it.  
B) ✓ Correct; moves in direction of negative gradient.  
C) ✗ Direction is not random.  
D) ✗ Newton step is different and uses Hessian.

**Correct:** B


#### 18. What is the relationship between the function \( g(x) \) and the system \( F(x) = 0 \)?  
A) ✓ Correct; \( g \) is sum of squares of \( F \) components.  
B) ✓ Correct; \( g \) minimized exactly when \( F(x) = 0 \).  
C) ✗ \( g \) is minimized, not maximized, at solution.  
D) ✗ \( g \) is directly related to \( F \).

**Correct:** A, B


#### 19. Which of the following statements about the use of bisection in finding \( \hat{\alpha} \) is correct?  
A) ✓ Correct; bisection finds interval where \( h(\alpha) \) decreases.  
B) ✗ Bisection does not guarantee global minimum, only a local decrease.  
C) ✓ Correct; step size is halved until \( h(\alpha) < h(0) \) or tolerance reached.  
D) ✗ Bisection is unrelated to gradient computation.

**Correct:** A, C


#### 20. Why is the steepest descent method considered a "modified" version of gradient descent in this context?  
A) ✗ It still uses gradient, not Hessian.  
B) ✓ Correct; it minimizes \( g \) derived from nonlinear system \( F(x) \).  
C) ✓ Correct; quadratic interpolation for step size is a modification.  
D) ✗ Hessian is not used in steepest descent.

**Correct:** B, C