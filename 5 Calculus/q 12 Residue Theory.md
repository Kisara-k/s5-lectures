## 12. Residue Theory

## Questions

#### 1. Which of the following statements correctly describe an isolated singularity of a complex function $f$ at $z = \alpha$?  
A) $f$ is not analytic at $\alpha$ but analytic in some punctured neighborhood around $\alpha$.  
B) $f$ is analytic at $\alpha$ but not analytic anywhere else in the neighborhood.  
C) There exists $R > 0$ such that $f$ is analytic for all $z$ with $0 < |z - \alpha| < R$.  
D) $f$ is analytic at $\alpha$ and in the entire neighborhood $|z - \alpha| < R$.


#### 2. Which of the following functions have a removable singularity at $z=0$?  
A) $f(z) = \frac{\sin z}{z}$  
B) $g(z) = \frac{1}{z^2}$  
C) $h(z) = \cos z - 1$  
D) $k(z) = \frac{e^z - 1}{z}$


#### 3. If $f$ has a pole of order 3 at $z = \alpha$, which of the following must be true about the Laurent series of $f$ around $\alpha$?  
A) The coefficient $a_{-3} \neq 0$.  
B) All coefficients $a_k = 0$ for $k < -3$.  
C) The coefficient $a_{-1} = 0$.  
D) The principal part has exactly three terms.


#### 4. Which of the following functions have an essential singularity at $z=0$?  
A) $f(z) = e^{1/z}$  
B) $g(z) = \frac{1}{z^2}$  
C) $h(z) = z^2 \sin \frac{1}{z}$  
D) $k(z) = \frac{\sin z}{z}$


#### 5. Suppose $f$ is analytic in a neighborhood of $\alpha$ and has a zero of order 4 at $\alpha$. Which of the following statements are true?  
A) $f(\alpha) = f'(\alpha) = f''(\alpha) = f'''(\alpha) = 0$  
B) $f^{(4)}(\alpha) \neq 0$  
C) $f(z) = (z-\alpha)^4 g(z)$ where $g$ is analytic and $g(\alpha) \neq 0$  
D) $f(z)$ has a pole of order 4 at $\alpha$


#### 6. If $f$ has a zero of order $m$ at $\alpha$ and $g$ has a zero of order $n$ at $\alpha$, what is the order of the zero of $h(z) = f(z)g(z)$ at $\alpha$?  
A) $\min(m,n)$  
B) $m + n$  
C) $|m - n|$  
D) $\max(m,n)$


#### 7. Let $f$ have a pole of order $m$ at $\alpha$ and $g$ have a pole of order $n$ at $\alpha$. What is the order of the pole of $h(z) = f(z)g(z)$ at $\alpha$?  
A) $m + n$  
B) $\max(m,n)$  
C) $|m - n|$  
D) $\min(m,n)$


#### 8. Consider $h(z) = \frac{f(z)}{g(z)}$ where $f$ and $g$ have zeros of orders $m$ and $n$ at $\alpha$, respectively. Which of the following are true?  
A) If $m > n$, $h$ has a zero of order $m-n$ at $\alpha$.  
B) If $m < n$, $h$ has a pole of order $n-m$ at $\alpha$.  
C) If $m = n$, $h$ has a removable singularity at $\alpha$.  
D) If $m = n$, $h$ necessarily has a pole at $\alpha$.


#### 9. Which of the following functions have a simple pole (pole of order 1) at $z=0$?  
A) $f(z) = \frac{1}{z}$  
B) $g(z) = \frac{z}{e^z - 1}$  
C) $h(z) = \frac{1}{z^2}$  
D) $k(z) = \frac{\sin z}{z^2}$


#### 10. For a function $f$ with a pole of order $n$ at $z = \alpha$, the residue $\text{Res}[f, \alpha]$ can be computed by:  
A) $\lim_{z \to \alpha} (z-\alpha) f(z)$  
B) $\frac{1}{(n-1)!} \lim_{z \to \alpha} \frac{d^{n-1}}{dz^{n-1}} \left[ (z-\alpha)^n f(z) \right]$  
C) The coefficient $a_{-1}$ in the Taylor series expansion of $f$ at $\alpha$  
D) The coefficient $a_{-1}$ in the Laurent series expansion of $f$ at $\alpha$


#### 11. Which of the following statements about residues are true?  
A) The residue at a removable singularity is always zero.  
B) The residue is the coefficient of $(z-\alpha)^{-1}$ in the Laurent series expansion.  
C) Residues can only be computed if the singularity is a pole.  
D) Residues are used to evaluate contour integrals around singularities.


#### 12. According to Cauchy's Residue Theorem, the integral of $f$ around a closed contour $C$ enclosing singularities $z_1, z_2, \ldots, z_n$ is:  
A) $2\pi i \sum_{k=1}^n \text{Res}[f, z_k]$  
B) Zero if $f$ has no singularities inside $C$  
C) Equal to the sum of the residues themselves  
D) Dependent on the path taken around $C$


#### 13. Which of the following functions have a zero of order 2 at $z=0$?  
A) $f(z) = z^2 e^z$  
B) $g(z) = \sin z$  
C) $h(z) = z^2 \sin z$  
D) $k(z) = z^3 \cos z$


#### 14. If $f$ has a pole of order 2 at $z=0$, which of the following could be a valid form of $f$?  
A) $f(z) = \frac{1}{z^2} + \frac{1}{z} + 1$  
B) $f(z) = \frac{1}{z^3}$  
C) $f(z) = \frac{e^z}{z^2}$  
D) $f(z) = \frac{1}{z}$


#### 15. Which of the following statements about essential singularities are true?  
A) The Laurent series has infinitely many negative power terms.  
B) The residue at an essential singularity is always zero.  
C) The behavior near an essential singularity is highly irregular.  
D) Essential singularities can be removed by redefining the function at the singularity.


#### 16. Suppose $f(z) = \frac{\sin z}{z^3}$. What is the order of the pole at $z=0$?  
A) 1  
B) 2  
C) 3  
D) No pole, removable singularity


#### 17. If $f$ is analytic in $D_R(\alpha)$ and has a zero of order $k$ at $\alpha$, which of the following is true about the derivatives of $f$ at $\alpha$?  
A) $f^{(n)}(\alpha) = 0$ for all $n < k$  
B) $f^{(k)}(\alpha) \neq 0$  
C) $f^{(k-1)}(\alpha) \neq 0$  
D) $f(\alpha) \neq 0$


#### 18. Which of the following are true about the product of two functions $f$ and $g$ analytic at $\alpha$ with zeros of orders $m$ and $n$ respectively?  
A) The product $h = fg$ has a zero of order $m+n$ at $\alpha$.  
B) The product $h = fg$ has a zero of order $\min(m,n)$ at $\alpha$.  
C) If either $f$ or $g$ has a zero of order zero (no zero), then $h$ has zero order equal to the other function's zero order.  
D) The product $h$ can never have a pole at $\alpha$.


#### 19. Which of the following functions have poles inside the circle $|z|=3$?  
A) $f(z) = \frac{1}{z^2 - 4}$  
B) $g(z) = \frac{5z^4 + 26z^2 + 5}{z^2 - 1}$  
C) $h(z) = \tan z$  
D) $k(z) = \frac{1}{z-4}$


#### 20. Which of the following statements about the function $f(z) = \pi \cot(\pi z)$ are true?  
A) It has simple poles at all integers $z = n \in \mathbb{Z}$.  
B) The residue at each pole $z = n$ is 1.  
C) It has an essential singularity at $z=0$.  
D) It is analytic everywhere except at its poles.



<br>

## Answers

#### 1. Which of the following statements correctly describe an isolated singularity of a complex function $f$ at $z = \alpha$?  
A) ✓ $f$ is not analytic at $\alpha$ but analytic in some punctured neighborhood around $\alpha$. This is the definition of an isolated singularity.  
B) ✗ $f$ is analytic at $\alpha$ contradicts the singularity condition.  
C) ✓ There exists $R > 0$ such that $f$ is analytic for all $z$ with $0 < |z - \alpha| < R$. This is the punctured disk condition.  
D) ✗ $f$ analytic at $\alpha$ means no singularity there.

**Correct:** A, C


#### 2. Which of the following functions have a removable singularity at $z=0$?  
A) ✓ $\frac{\sin z}{z}$ tends to 1 as $z \to 0$, so singularity is removable.  
B) ✗ $\frac{1}{z^2}$ has a pole, not removable.  
C) ✓ $\cos z - 1$ behaves like $-\frac{z^2}{2}$, analytic at 0, so removable singularity.  
D) ✓ $\frac{e^z - 1}{z}$ tends to 1 as $z \to 0$, removable singularity.

**Correct:** A, C, D


#### 3. If $f$ has a pole of order 3 at $z = \alpha$, which of the following must be true about the Laurent series of $f$ around $\alpha$?  
A) ✓ $a_{-3} \neq 0$ defines the order of the pole.  
B) ✓ All $a_k = 0$ for $k < -3$ since order is exactly 3.  
C) ✗ $a_{-1}$ can be zero or nonzero; it is the residue but not related to order.  
D) ✗ The principal part has exactly 3 terms only if all $a_{-2}, a_{-1} \neq 0$, but some could be zero.

**Correct:** A, B


#### 4. Which of the following functions have an essential singularity at $z=0$?  
A) ✓ $e^{1/z}$ has infinitely many negative powers in Laurent expansion.  
B) ✗ $\frac{1}{z^2}$ is a pole, not essential.  
C) ✓ $z^2 \sin \frac{1}{z}$ has infinitely many negative powers due to $\sin(1/z)$.  
D) ✗ $\frac{\sin z}{z}$ has a removable singularity.

**Correct:** A, C


#### 5. Suppose $f$ is analytic in a neighborhood of $\alpha$ and has a zero of order 4 at $\alpha$. Which of the following statements are true?  
A) ✓ By definition, derivatives up to order 3 vanish at $\alpha$.  
B) ✓ The 4th derivative at $\alpha$ is nonzero.  
C) ✓ Factorization form of zero of order 4.  
D) ✗ Zero of order 4 means no pole.

**Correct:** A, B, C


#### 6. If $f$ has a zero of order $m$ at $\alpha$ and $g$ has a zero of order $n$ at $\alpha$, what is the order of the zero of $h(z) = f(z)g(z)$ at $\alpha$?  
A) ✗ Minimum is incorrect; zeros add.  
B) ✓ Orders add for product of zeros.  
C) ✗ Absolute difference is not correct here.  
D) ✗ Maximum is incorrect.

**Correct:** B


#### 7. Let $f$ have a pole of order $m$ at $\alpha$ and $g$ have a pole of order $n$ at $\alpha$. What is the order of the pole of $h(z) = f(z)g(z)$ at $\alpha$?  
A) ✓ Poles add in order for product.  
B) ✗ Maximum is incorrect.  
C) ✗ Absolute difference is incorrect.  
D) ✗ Minimum is incorrect.

**Correct:** A


#### 8. Consider $h(z) = \frac{f(z)}{g(z)}$ where $f$ and $g$ have zeros of orders $m$ and $n$ at $\alpha$, respectively. Which of the following are true?  
A) ✓ If $m > n$, zero of order $m-n$ remains.  
B) ✓ If $m < n$, pole of order $n-m$ appears.  
C) ✓ If $m = n$, removable singularity occurs.  
D) ✗ If $m = n$, pole does not necessarily occur.

**Correct:** A, B, C


#### 9. Which of the following functions have a simple pole (pole of order 1) at $z=0$?  
A) ✓ $\frac{1}{z}$ is a simple pole.  
B) ✓ $\frac{z}{e^z - 1}$ has a simple pole at 0 because denominator behaves like $z$.  
C) ✗ $\frac{1}{z^2}$ is a pole of order 2.  
D) ✗ $\frac{\sin z}{z^2}$ has a pole of order 1 or 2? Actually, $\sin z \approx z$, so $\frac{\sin z}{z^2} \approx \frac{z}{z^2} = \frac{1}{z}$, simple pole.

**Correct:** A, B, D


#### 10. For a function $f$ with a pole of order $n$ at $z = \alpha$, the residue $\text{Res}[f, \alpha]$ can be computed by:  
A) ✗ Only valid for simple poles (order 1).  
B) ✓ Correct formula for residue at pole of order $n$.  
C) ✗ Taylor series does not have negative powers.  
D) ✓ Residue is coefficient $a_{-1}$ in Laurent series.

**Correct:** B, D


#### 11. Which of the following statements about residues are true?  
A) ✓ Residue at removable singularity is zero (no negative powers).  
B) ✓ Residue is coefficient of $(z-\alpha)^{-1}$ in Laurent series.  
C) ✗ Residues exist for poles and essential singularities, not only poles.  
D) ✓ Residues are used to evaluate contour integrals.

**Correct:** A, B, D


#### 12. According to Cauchy's Residue Theorem, the integral of $f$ around a closed contour $C$ enclosing singularities $z_1, z_2, \ldots, z_n$ is:  
A) ✓ Correct formula.  
B) ✓ Integral is zero if no singularities inside $C$.  
C) ✗ Integral equals $2\pi i$ times sum of residues, not just sum.  
D) ✗ Integral depends only on singularities inside, not path shape.

**Correct:** A, B


#### 13. Which of the following functions have a zero of order 2 at $z=0$?  
A) ✓ $z^2 e^z$ zero order 2 since $e^z$ analytic and nonzero at 0.  
B) ✗ $\sin z$ has zero of order 1 at 0.  
C) ✗ $z^2 \sin z$ zero order 3 (since $\sin z \approx z$).  
D) ✗ $z^3 \cos z$ zero order 3.

**Correct:** A


#### 14. If $f$ has a pole of order 2 at $z=0$, which of the following could be a valid form of $f$?  
A) ✓ Has terms up to $\frac{1}{z^2}$, so valid.  
B) ✗ Pole order 3, not 2.  
C) ✓ $\frac{e^z}{z^2}$ has pole order 2.  
D) ✗ Simple pole only.

**Correct:** A, C


#### 15. Which of the following statements about essential singularities are true?  
A) ✓ Infinitely many negative powers in Laurent series.  
B) ✗ Residue can be nonzero; not always zero.  
C) ✓ Behavior near essential singularity is highly irregular.  
D) ✗ Essential singularities cannot be removed by redefining function.

**Correct:** A, C


#### 16. Suppose $f(z) = \frac{\sin z}{z^3}$. What is the order of the pole at $z=0$?  
A) ✗ Pole order is not 1.  
B) ✓ $\sin z \approx z - \frac{z^3}{6} + \cdots$, so $\frac{\sin z}{z^3} \approx \frac{z}{z^3} = \frac{1}{z^2}$, pole order 2.  
C) ✗ Pole order 3 is incorrect.  
D) ✗ Not removable.

**Correct:** B


#### 17. If $f$ is analytic in $D_R(\alpha)$ and has a zero of order $k$ at $\alpha$, which of the following is true about the derivatives of $f$ at $\alpha$?  
A) ✓ Derivatives up to order $k-1$ vanish.  
B) ✓ The $k$-th derivative is nonzero.  
C) ✗ $f^{(k-1)}(\alpha) = 0$, not nonzero.  
D) ✗ $f(\alpha) = 0$ due to zero of order $k$.

**Correct:** A, B


#### 18. Which of the following are true about the product of two functions $f$ and $g$ analytic at $\alpha$ with zeros of orders $m$ and $n$ respectively?  
A) ✓ Zero orders add for product.  
B) ✗ Minimum is incorrect.  
C) ✓ If one has zero order zero, product zero order equals the other’s zero order.  
D) ✓ Product of analytic functions cannot have poles.

**Correct:** A, C, D


#### 19. Which of the following functions have poles inside the circle $|z|=3$?  
A) ✓ Poles at $z = \pm 2$ inside circle.  
B) ✓ Poles at $z = \pm 1$ inside circle.  
C) ✓ $\tan z$ has poles at $z = \frac{\pi}{2} + k\pi$, some inside circle.  
D) ✗ Pole at $z=4$ outside circle.

**Correct:** A, B, C


#### 20. Which of the following statements about the function $f(z) = \pi \cot(\pi z)$ are true?  
A) ✓ Simple poles at all integers.  
B) ✓ Residue at each pole is 1.  
C) ✗ No essential singularity at 0; it is a simple pole.  
D) ✓ Analytic except at poles.

**Correct:** A, B, D