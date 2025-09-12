## 13. Residue Theory (ctd.)

## Questions

#### 1. Which of the following statements about evaluating real integrals using residue theory are true?  
A) Residue theory can be used to evaluate certain improper integrals that are difficult to solve by standard calculus methods.  
B) Residue theory only applies to integrals over closed contours in the complex plane, not real integrals.  
C) Real integrals can be transformed into contour integrals by extending the integrand into the complex plane.  
D) The residue theorem is not applicable if the integrand has poles on the real axis.


#### 2. When converting a trigonometric integral over $[0, 2\pi]$ into a contour integral on the complex plane, which substitution is commonly used?  
A) $z = \cos \theta$  
B) $z = e^{i\theta}$  
C) $z = \sin \theta$  
D) $z = \tan \theta$


#### 3. For the integral $\int_{-\infty}^\infty \frac{P(x)}{Q(x)} dx$, where $P$ and $Q$ are polynomials, under which condition can residue theory be applied directly to evaluate the integral?  
A) Degree of $Q$ is less than degree of $P$  
B) Degree of $Q$ is at least two more than degree of $P$  
C) $Q(x) \neq 0$ for all real $x$  
D) $P$ and $Q$ have complex coefficients only


#### 4. The Cauchy Principal Value (P.V.) of an integral is used when:  
A) The integral converges absolutely.  
B) The integral diverges but symmetric limits exist.  
C) The integrand has poles on the real axis.  
D) The integral is over a finite interval.


#### 5. Which of the following are true about the poles of the function $f(z) = \frac{P(z)}{Q(z)}$ when applying residue theory to improper integrals?  
A) Only poles in the upper half-plane contribute to the integral over $(-\infty, \infty)$ when closing the contour in the upper half-plane.  
B) Poles on the real axis must always be included in the residue sum.  
C) Poles in the lower half-plane contribute if the contour is closed in the lower half-plane.  
D) Poles at infinity are ignored in residue calculations.


#### 6. For the integral $\int_{-\infty}^\infty \frac{P(x)}{Q(x)} \cos(\alpha x) dx$, which conditions ensure convergence?  
A) Degree of $Q$ is at least one more than degree of $P$  
B) $Q(x) \neq 0$ for all real $x$  
C) $\alpha > 0$  
D) $P$ and $Q$ must be polynomials with complex coefficients


#### 7. When evaluating $\int_{-\infty}^\infty \frac{P(x)}{Q(x)} \sin(\alpha x) dx$ using residues, the function considered in the complex plane is typically:  
A) $f(z) = \frac{P(z)}{Q(z)} e^{i \alpha z}$  
B) $f(z) = \frac{P(z)}{Q(z)} e^{-i \alpha z}$  
C) $f(z) = \frac{P(z)}{Q(z)} \cos(\alpha z)$  
D) $f(z) = \frac{P(z)}{Q(z)} \sin(\alpha z)$


#### 8. Which of the following statements about the degree conditions on polynomials $P$ and $Q$ are correct for applying residue theory to improper integrals?  
A) If $n = \deg(Q) \geq m = \deg(P) + 2$, the integral $\int_{-\infty}^\infty \frac{P(x)}{Q(x)} dx$ converges.  
B) If $n = m$, the integral always converges.  
C) If $n \geq m + 1$, integrals involving $\cos x$ or $\sin x$ multiplied by $\frac{P(x)}{Q(x)}$ converge.  
D) If $n < m$, the integral converges only if $P$ has no real roots.


#### 9. Suppose $f(z) = \frac{P(z)}{Q(z)}$ has poles at $z = i$ and $z = -i$. If the contour is closed in the upper half-plane, which poles contribute to the integral?  
A) Only $z = i$  
B) Only $z = -i$  
C) Both $z = i$ and $z = -i$  
D) Neither, because poles are on the imaginary axis


#### 10. Which of the following integrals can be evaluated using residue theory by considering the limit of a contour integral over a semicircle in the upper half-plane?  
A) $\int_0^\infty \frac{\sin x}{x} dx$  
B) $\int_{-\infty}^\infty \frac{dx}{x^2 + 1}$  
C) $\int_{-\infty}^\infty e^{-x^2} dx$  
D) $\int_{-\infty}^\infty \frac{\cos x}{x^2 + 4} dx$


#### 11. When applying residue theory to evaluate $\int_{-\infty}^\infty \frac{P(x)}{Q(x)} dx$, why is it important that $Q(x) \neq 0$ for all real $x$?  
A) To ensure the integrand is continuous on the real axis  
B) To avoid poles on the contour of integration  
C) To guarantee the integral converges absolutely  
D) To simplify the calculation of residues


#### 12. Which of the following are true about the behavior of the integrand at infinity for the residue method to work on improper integrals?  
A) The integrand must vanish faster than $1/|z|$ as $|z| \to \infty$ in the upper half-plane.  
B) The degree of denominator polynomial must be at least two more than numerator polynomial for the integral over the semicircle to vanish.  
C) The integrand can grow exponentially at infinity if multiplied by $e^{i \alpha z}$ with $\alpha > 0$.  
D) The integrand must be bounded on the real axis.


#### 13. The residue theorem states that the integral of a function around a closed contour is:  
A) Zero if the function is analytic inside the contour.  
B) Equal to $2\pi i$ times the sum of residues of the function inside the contour.  
C) Equal to the sum of the function values at the poles inside the contour.  
D) Equal to the integral over the real axis plus the integral over the semicircle.


#### 14. Which of the following integrals require the use of the Cauchy Principal Value for evaluation?  
A) $\int_{-\infty}^\infty \frac{dx}{x}$  
B) $\int_0^\infty e^{-x} dx$  
C) $\int_{-\infty}^\infty \frac{\sin x}{x} dx$  
D) $\int_{-\infty}^\infty \frac{dx}{x^2 + 1}$


#### 15. When evaluating integrals involving $\cos(\alpha x)$ or $\sin(\alpha x)$ multiplied by rational functions, why is the parameter $\alpha > 0$ important?  
A) It ensures the exponential factor $e^{i \alpha z}$ decays in the upper half-plane.  
B) It guarantees the integral converges absolutely.  
C) It determines the direction in which the contour should be closed.  
D) It affects the location of poles of the integrand.


#### 16. Which of the following are valid reasons for closing the contour in the upper half-plane when evaluating an integral using residues?  
A) The integrand decays sufficiently fast in the upper half-plane.  
B) The poles of the integrand lie in the upper half-plane.  
C) The integral involves $e^{i \alpha z}$ with $\alpha > 0$.  
D) The integral is over a finite interval.


#### 17. Consider the function $f(z) = \frac{z e^{i z}}{z^2 + 1}$. Which of the following statements are true regarding its poles and residues?  
A) It has simple poles at $z = i$ and $z = -i$.  
B) Only the pole at $z = i$ lies in the upper half-plane.  
C) The residue at $z = i$ can be used to evaluate $\int_{-\infty}^\infty \frac{x \sin x}{x^2 + 1} dx$.  
D) The residue at $z = -i$ contributes when closing the contour in the upper half-plane.


#### 18. Which of the following integrals cannot be evaluated directly by residue theory without additional techniques?  
A) $\int_{-\infty}^\infty \frac{dx}{x^2 + 1}$  
B) $\int_0^{2\pi} \frac{d\theta}{5 - 4 \cos \theta}$  
C) $\int_{-\infty}^\infty e^{-x^2} dx$  
D) $\int_{-\infty}^\infty \frac{\cos x}{x^2 + 1} dx$


#### 19. Which of the following are true about the integral $\int_0^{2\pi} \frac{1 + 3 \cos^2 \theta}{5 - 4 \cos \theta} d\theta$ when evaluated using residues?  
A) The integral can be converted into a contour integral around the unit circle.  
B) The substitution $z = e^{i \theta}$ transforms cosine terms into rational functions of $z$.  
C) The integral is evaluated by summing residues inside the unit circle.  
D) The integral requires closing the contour in the upper half-plane.


#### 20. Which of the following are necessary steps when using residue theory to evaluate an improper integral over the real line?  
A) Identify the poles of the integrand in the complex plane.  
B) Choose a contour that includes the real axis and closes in the upper or lower half-plane.  
C) Calculate the residues at the poles inside the chosen contour.  
D) Ensure the integral over the curved part of the contour vanishes or is manageable.



<br>

## Answers

#### 1. Which of the following statements about evaluating real integrals using residue theory are true?  
A) ✓ Residue theory can evaluate improper integrals difficult for standard methods.  
B) ✗ Residue theory applies to real integrals by extending them to complex contours.  
C) ✓ Real integrals can be transformed into contour integrals in the complex plane.  
D) ✗ Poles on the real axis complicate but do not always prevent residue application.

**Correct:** A, C


#### 2. When converting a trigonometric integral over $[0, 2\pi]$ into a contour integral on the complex plane, which substitution is commonly used?  
A) ✗ $z = \cos \theta$ is not a complex substitution.  
B) ✓ $z = e^{i\theta}$ maps the interval to the unit circle in the complex plane.  
C) ✗ $z = \sin \theta$ does not map to a simple contour.  
D) ✗ $z = \tan \theta$ is not standard for contour integrals.

**Correct:** B


#### 3. For the integral $\int_{-\infty}^\infty \frac{P(x)}{Q(x)} dx$, where $P$ and $Q$ are polynomials, under which condition can residue theory be applied directly to evaluate the integral?  
A) ✗ Degree of $Q$ less than $P$ usually causes divergence.  
B) ✓ Degree of $Q$ at least two more than $P$ ensures decay at infinity.  
C) ✓ $Q(x) \neq 0$ on real axis avoids poles on contour.  
D) ✗ Coefficients can be real or complex; complex-only is not required.

**Correct:** B, C


#### 4. The Cauchy Principal Value (P.V.) of an integral is used when:  
A) ✗ P.V. is for divergent integrals, not absolutely convergent ones.  
B) ✓ P.V. handles integrals where symmetric limits exist despite divergence.  
C) ✓ Poles on the real axis often require P.V. for meaningful evaluation.  
D) ✗ P.V. is not specifically for finite intervals.

**Correct:** B, C


#### 5. Which of the following are true about the poles of the function $f(z) = \frac{P(z)}{Q(z)}$ when applying residue theory to improper integrals?  
A) ✓ Only poles inside the chosen contour (e.g., upper half-plane) contribute.  
B) ✗ Poles on the real axis complicate contour choice and may require P.V.  
C) ✓ Poles in lower half-plane contribute if contour is closed there.  
D) ✗ Poles at infinity are not treated as residues but affect contour behavior.

**Correct:** A, C


#### 6. For the integral $\int_{-\infty}^\infty \frac{P(x)}{Q(x)} \cos(\alpha x) dx$, which conditions ensure convergence?  
A) ✓ Degree condition $n \geq m + 1$ ensures decay.  
B) ✓ $Q(x) \neq 0$ on real axis avoids singularities on contour.  
C) ✗ $\alpha > 0$ is not necessary for convergence but important for contour choice.  
D) ✗ Coefficients can be real; complex-only is not required.

**Correct:** A, B


#### 7. When evaluating $\int_{-\infty}^\infty \frac{P(x)}{Q(x)} \sin(\alpha x) dx$ using residues, the function considered in the complex plane is typically:  
A) ✓ $f(z) = \frac{P(z)}{Q(z)} e^{i \alpha z}$ combines sine and cosine via Euler’s formula.  
B) ✗ $e^{-i \alpha z}$ is used if contour closes in lower half-plane.  
C) ✗ Cosine alone is not used for sine integrals.  
D) ✗ Sine alone is not analytic; exponential form is preferred.

**Correct:** A


#### 8. Which of the following statements about the degree conditions on polynomials $P$ and $Q$ are correct for applying residue theory to improper integrals?  
A) ✓ $n \geq m + 2$ ensures integral convergence for rational functions.  
B) ✗ $n = m$ generally does not guarantee convergence.  
C) ✓ $n \geq m + 1$ suffices for integrals involving sine or cosine factors.  
D) ✗ $n < m$ usually leads to divergence, regardless of roots.

**Correct:** A, C


#### 9. Suppose $f(z) = \frac{P(z)}{Q(z)}$ has poles at $z = i$ and $z = -i$. If the contour is closed in the upper half-plane, which poles contribute to the integral?  
A) ✓ Only $z = i$ lies in the upper half-plane.  
B) ✗ $z = -i$ is in the lower half-plane.  
C) ✗ Both poles do not lie in the same half-plane.  
D) ✗ Poles on imaginary axis are inside half-plane, but only $i$ is upper half-plane.

**Correct:** A


#### 10. Which of the following integrals can be evaluated using residue theory by considering the limit of a contour integral over a semicircle in the upper half-plane?  
A) ✗ $\int_0^\infty \frac{\sin x}{x} dx$ requires special techniques, not direct residue.  
B) ✓ $\int_{-\infty}^\infty \frac{dx}{x^2 + 1}$ classic example for residue method.  
C) ✗ $\int_{-\infty}^\infty e^{-x^2} dx$ is Gaussian, not rational, residue not straightforward.  
D) ✓ $\int_{-\infty}^\infty \frac{\cos x}{x^2 + 4} dx$ fits residue method with oscillatory factor.

**Correct:** B, D


#### 11. When applying residue theory to evaluate $\int_{-\infty}^\infty \frac{P(x)}{Q(x)} dx$, why is it important that $Q(x) \neq 0$ for all real $x$?  
A) ✓ Ensures integrand is continuous on real axis, avoiding singularities.  
B) ✓ Avoids poles on the contour, simplifying residue calculation.  
C) ✗ Does not guarantee absolute convergence alone.  
D) ✗ Simplifies but is not the main reason for residue calculation.

**Correct:** A, B


#### 12. Which of the following are true about the behavior of the integrand at infinity for the residue method to work on improper integrals?  
A) ✓ Integrand must vanish faster than $1/|z|$ on the semicircle for integral over arc to vanish.  
B) ✓ Degree condition $n \geq m + 2$ ensures this decay.  
C) ✗ Exponential growth in upper half-plane would prevent contour closure there.  
D) ✗ Boundedness on real axis is not sufficient; decay at infinity is crucial.

**Correct:** A, B


#### 13. The residue theorem states that the integral of a function around a closed contour is:  
A) ✓ Zero if function is analytic inside contour (no poles).  
B) ✓ Equal to $2\pi i$ times sum of residues inside contour.  
C) ✗ Sum of function values at poles is not the residue sum.  
D) ✗ Integral over real axis plus semicircle is a method, not the theorem itself.

**Correct:** A, B


#### 14. Which of the following integrals require the use of the Cauchy Principal Value for evaluation?  
A) ✓ $\int_{-\infty}^\infty \frac{dx}{x}$ diverges but P.V. exists.  
B) ✗ $\int_0^\infty e^{-x} dx$ converges absolutely, no P.V. needed.  
C) ✓ $\int_{-\infty}^\infty \frac{\sin x}{x} dx$ converges as P.V.  
D) ✗ $\int_{-\infty}^\infty \frac{dx}{x^2 + 1}$ converges absolutely.

**Correct:** A, C


#### 15. When evaluating integrals involving $\cos(\alpha x)$ or $\sin(\alpha x)$ multiplied by rational functions, why is the parameter $\alpha > 0$ important?  
A) ✓ Ensures $e^{i \alpha z}$ decays in upper half-plane, allowing contour closure.  
B) ✗ Does not guarantee absolute convergence alone.  
C) ✓ Determines contour closure direction (upper half-plane for $\alpha > 0$).  
D) ✗ Does not affect pole locations.

**Correct:** A, C


#### 16. Which of the following are valid reasons for closing the contour in the upper half-plane when evaluating an integral using residues?  
A) ✓ Integrand decays sufficiently fast in upper half-plane.  
B) ✓ Poles lie in upper half-plane, so residues contribute.  
C) ✓ Integral involves $e^{i \alpha z}$ with $\alpha > 0$, decaying in upper half-plane.  
D) ✗ Integral over finite interval does not require contour closure.

**Correct:** A, B, C


#### 17. Consider the function $f(z) = \frac{z e^{i z}}{z^2 + 1}$. Which of the following statements are true regarding its poles and residues?  
A) ✓ Poles at $z = i$ and $z = -i$ are simple.  
B) ✓ Only $z = i$ lies in upper half-plane.  
C) ✓ Residue at $z = i$ helps evaluate $\int_{-\infty}^\infty \frac{x \sin x}{x^2 + 1} dx$.  
D) ✗ Residue at $z = -i$ does not contribute when contour closes in upper half-plane.

**Correct:** A, B, C


#### 18. Which of the following integrals cannot be evaluated directly by residue theory without additional techniques?  
A) ✗ $\int_{-\infty}^\infty \frac{dx}{x^2 + 1}$ is classic residue example.  
B) ✗ $\int_0^{2\pi} \frac{d\theta}{5 - 4 \cos \theta}$ can be converted to contour integral.  
C) ✓ $\int_{-\infty}^\infty e^{-x^2} dx$ is Gaussian, not rational, residue not direct.  
D) ✗ $\int_{-\infty}^\infty \frac{\cos x}{x^2 + 1} dx$ fits residue method.

**Correct:** C


#### 19. Which of the following are true about the integral $\int_0^{2\pi} \frac{1 + 3 \cos^2 \theta}{5 - 4 \cos \theta} d\theta$ when evaluated using residues?  
A) ✓ Integral converts to contour integral around unit circle.  
B) ✓ Substitution $z = e^{i \theta}$ transforms cosine to rational functions.  
C) ✓ Residues inside unit circle are summed to evaluate integral.  
D) ✗ Contour is the unit circle, not necessarily closed in upper half-plane.

**Correct:** A, B, C


#### 20. Which of the following are necessary steps when using residue theory to evaluate an improper integral over the real line?  
A) ✓ Identify poles of integrand in complex plane.  
B) ✓ Choose contour including real axis and closing in half-plane.  
C) ✓ Calculate residues at poles inside contour.  
D) ✓ Ensure integral over curved part of contour vanishes or is manageable.

**Correct:** A, B, C, D