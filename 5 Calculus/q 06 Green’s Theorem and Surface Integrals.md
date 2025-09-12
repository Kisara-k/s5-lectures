## 6. Green’s Theorem and Surface Integrals

## Questions

#### 1. Which of the following conditions are necessary for Green’s Theorem to hold on a region $D$ bounded by curve $C$?  
A) $D$ must be simply connected  
B) $C$ must be positively oriented  
C) $M$ and $N$ must be continuously differentiable on $D$ and its boundary  
D) $D$ can have holes as long as $C$ is smooth  

#### 2. Green’s Theorem relates a line integral around a closed curve $C$ to which of the following?  
A) A surface integral over a surface bounded by $C$  
B) A double integral over the region enclosed by $C$  
C) A triple integral over the volume enclosed by $C$  
D) The circulation of the vector field inside $C$  

#### 3. For a multiply connected region with $n$ holes, how does Green’s Theorem generalize?  
A) The line integral is taken only around the outer boundary  
B) The line integral is the sum of integrals around the outer boundary and holes, with holes oriented clockwise  
C) The double integral is taken over the entire region excluding holes  
D) The holes’ boundaries are oriented counterclockwise  

#### 4. Consider the vector field $\mathbf{F} = (x + xy^2, 2x^2 y - y^2 \sin y)$. Which of the following statements about the work done along a closed path $C$ are true?  
A) The work can be computed using Green’s Theorem if $C$ is positively oriented and simple  
B) The work depends only on the curl of $\mathbf{F}$ inside $C$  
C) The work is zero if $\mathbf{F}$ is conservative  
D) The work is independent of the path if $C$ encloses no singularities  

#### 5. Which of the following surfaces are orientable?  
A) Sphere  
B) Möbius strip  
C) Torus  
D) Klein bottle  

#### 6. The normal vector to a parametric surface $\mathbf{r}(u,v)$ is given by:  
A) $\frac{\partial \mathbf{r}}{\partial u} + \frac{\partial \mathbf{r}}{\partial v}$  
B) $\frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v}$  
C) $\nabla \cdot \mathbf{r}$  
D) $\nabla G$ if $G(\mathbf{r}) = 0$ defines the surface  

#### 7. For a surface defined implicitly by $G(x,y,z) = 0$, which of the following is true about the gradient $\nabla G$?  
A) It is tangent to the surface  
B) It is normal to the surface  
C) It points in the direction of maximum increase of $G$  
D) It is zero everywhere on the surface  

#### 8. The surface integral of a scalar function $f$ over a surface $\sigma$ is defined as:  
A) The limit of sums of $f$ evaluated at points times the area of small surface patches  
B) The integral of $f$ over the projection of $\sigma$ onto the $xy$-plane  
C) The sum of $f$ values times the volume under $\sigma$  
D) The limit of sums of $f$ times the length of curves on $\sigma$  

#### 9. When calculating the surface integral of $f$ over a parametric surface $\mathbf{r}(u,v)$, which expression correctly represents the differential surface area element $dS$?  
A) $du\, dv$  
B) $\left| \frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v} \right| du\, dv$  
C) $\left| \frac{\partial \mathbf{r}}{\partial u} + \frac{\partial \mathbf{r}}{\partial v} \right| du\, dv$  
D) $\sqrt{1 + g_x^2 + g_y^2} \, dx\, dy$  

#### 10. For a surface given by $z = g(x,y)$, the upward-pointing normal vector is:  
A) $(g_x, g_y, -1)$  
B) $(-g_x, -g_y, 1)$  
C) $(1, 1, 1)$  
D) $\nabla G$ where $G = z - g(x,y)$  

#### 11. Which of the following statements about flux through a surface are correct?  
A) Flux depends on the speed of the vector field through the surface  
B) Flux is independent of the orientation of the surface  
C) Flux is maximized when the vector field is tangent to the surface  
D) Flux is zero if the vector field is perpendicular to the normal vector everywhere  

#### 12. The flux of a vector field $\mathbf{F}$ across a surface $\sigma$ oriented by unit normal $\mathbf{n}$ is given by:  
A) $\iint_\sigma \mathbf{F} \cdot \mathbf{n} \, dS$  
B) $\iint_\sigma \mathbf{F} \times \mathbf{n} \, dS$  
C) $\oint_C \mathbf{F} \cdot d\mathbf{r}$ where $C$ is the boundary of $\sigma$  
D) $\iint_\sigma |\mathbf{F}| \, dS$  

#### 13. If a surface $\sigma$ is non-orientable, which of the following is true?  
A) It is impossible to define a continuous unit normal vector field on $\sigma$  
B) The surface integral of a vector field over $\sigma$ is always zero  
C) The surface must have only one side  
D) The surface can be parametrized by two variables  

#### 14. When using Green’s Theorem to find the area of a planar region, which of the following vector fields can be used?  
A) $\mathbf{F} = (-y, x)$  
B) $\mathbf{F} = (x, y)$  
C) $\mathbf{F} = (0, x)$  
D) $\mathbf{F} = (y, 0)$  

#### 15. Which of the following statements about the orientation of a parametric surface are true?  
A) The orientation is determined by the order of parameters $(u,v)$ in the cross product  
B) Reversing the order of parameters reverses the orientation  
C) The orientation is independent of the parametrization  
D) The negative orientation corresponds to the negative of the normal vector  

#### 16. For the vector field $\mathbf{F}(x,y,z) = z \mathbf{k}$, what is the flux through the sphere $x^2 + y^2 + z^2 = a^2$ oriented outward?  
A) Zero  
B) Proportional to the volume of the sphere  
C) Proportional to the surface area of the sphere  
D) Depends on the radius $a$  

#### 17. Which of the following surfaces can be expressed as level surfaces $G(x,y,z) = 0$ for some function $G$?  
A) $z = g(x,y)$  
B) $y = g(z,x)$  
C) $x = g(y,z)$  
D) Only surfaces defined explicitly as $z = g(x,y)$  

#### 18. When calculating the surface integral of a vector field over a surface defined by $z = g(x,y)$, which of the following integrals correctly represents the flux with positive orientation?  
A) $\iint_R \mathbf{F}(x,y,g(x,y)) \cdot (-g_x, -g_y, 1) \, dx\, dy$  
B) $\iint_R \mathbf{F}(x,y,g(x,y)) \cdot \frac{(-g_x, -g_y, 1)}{\sqrt{1 + g_x^2 + g_y^2}} \sqrt{1 + g_x^2 + g_y^2} \, dx\, dy$  
C) $\iint_R \mathbf{F}(x,y,g(x,y)) \cdot (g_x, g_y, -1) \, dx\, dy$  
D) $\iint_R \mathbf{F}(x,y,g(x,y)) \cdot \mathbf{n} \, dS$ where $\mathbf{n}$ is the unit normal  

#### 19. Which of the following are true about the proof of Green’s Theorem?  
A) It is straightforward for standard regions bounded by rectangles or simple curves  
B) It requires the region to be convex  
C) It can be extended to multiply connected regions by considering holes with opposite orientation  
D) It is based on the Fundamental Theorem of Calculus in two dimensions  

#### 20. Which of the following statements about the surface integral of a scalar function are correct?  
A) It generalizes the concept of line integrals to surfaces  
B) It requires the surface to be smooth or piecewise smooth  
C) The limit defining the surface integral depends on the choice of sample points  
D) The surface integral can be computed by projecting the surface onto a coordinate plane and adjusting by a factor involving partial derivatives



<br>

## Answers

#### 1. Which of the following conditions are necessary for Green’s Theorem to hold on a region $D$ bounded by curve $C$?  
A) ✓ $D$ must be simply connected to avoid holes that complicate the theorem.  
B) ✓ $C$ must be positively oriented (counterclockwise) for the theorem’s sign convention.  
C) ✓ $M$ and $N$ must be continuously differentiable on $D$ and its boundary for the partial derivatives to exist.  
D) ✗ $D$ cannot have holes if applying the basic form of Green’s Theorem; holes require the extended version.

**Correct:** A, B, C


#### 2. Green’s Theorem relates a line integral around a closed curve $C$ to which of the following?  
A) ✗ Surface integrals are 3D; Green’s Theorem is 2D.  
B) ✓ Double integral over the region enclosed by $C$ is exactly what Green’s Theorem states.  
C) ✗ Triple integrals are not involved in Green’s Theorem.  
D) ✓ Circulation inside $C$ is represented by the curl integral, which equals the line integral.

**Correct:** B, D


#### 3. For a multiply connected region with $n$ holes, how does Green’s Theorem generalize?  
A) ✗ The holes’ boundaries must be included, not ignored.  
B) ✓ The line integral is the sum around the outer boundary (counterclockwise) minus the sum around holes (clockwise).  
C) ✓ The double integral is over the entire region excluding holes, consistent with the boundaries.  
D) ✗ Holes’ boundaries are oriented clockwise, not counterclockwise.

**Correct:** B, C


#### 4. Consider the vector field $\mathbf{F} = (x + xy^2, 2x^2 y - y^2 \sin y)$. Which of the following statements about the work done along a closed path $C$ are true?  
A) ✓ Green’s Theorem applies if $C$ is positively oriented and simple.  
B) ✓ Work depends on the curl inside $C$ by Green’s Theorem.  
C) ✗ The field is not necessarily conservative; no info given.  
D) ✗ Work depends on the path if singularities or holes exist inside $C$.

**Correct:** A, B


#### 5. Which of the following surfaces are orientable?  
A) ✓ Sphere is orientable (two-sided).  
B) ✗ Möbius strip is non-orientable (one-sided).  
C) ✓ Torus is orientable (two-sided).  
D) ✗ Klein bottle is non-orientable.

**Correct:** A, C


#### 6. The normal vector to a parametric surface $\mathbf{r}(u,v)$ is given by:  
A) ✗ Sum of partial derivatives is not normal.  
B) ✓ Cross product of partial derivatives gives a normal vector.  
C) ✗ Divergence $\nabla \cdot \mathbf{r}$ is a scalar, not a vector.  
D) ✓ Gradient of $G$ is normal if surface is implicitly defined by $G=0$.

**Correct:** B, D


#### 7. For a surface defined implicitly by $G(x,y,z) = 0$, which of the following is true about the gradient $\nabla G$?  
A) ✗ Gradient is normal, not tangent.  
B) ✓ Gradient is normal to the surface.  
C) ✓ Gradient points in direction of maximum increase of $G$.  
D) ✗ Gradient is zero only at critical points, not everywhere on surface.

**Correct:** B, C


#### 8. The surface integral of a scalar function $f$ over a surface $\sigma$ is defined as:  
A) ✓ Limit of sums of $f$ times small surface areas is the definition.  
B) ✗ Projection integral alone is not the surface integral.  
C) ✗ Volume under surface is unrelated.  
D) ✗ Length of curves is 1D, not surface integral.

**Correct:** A


#### 9. When calculating the surface integral of $f$ over a parametric surface $\mathbf{r}(u,v)$, which expression correctly represents the differential surface area element $dS$?  
A) ✗ $du\, dv$ is parameter area, not surface area.  
B) ✓ Magnitude of cross product of partial derivatives times $du\, dv$ is correct.  
C) ✗ Sum of partial derivatives is not related to area.  
D) ✗ This applies only for surfaces given as graphs $z=g(x,y)$.

**Correct:** B


#### 10. For a surface given by $z = g(x,y)$, the upward-pointing normal vector is:  
A) ✗ Incorrect sign convention.  
B) ✓ Correct formula for upward normal vector.  
C) ✗ Arbitrary vector, not normal.  
D) ✓ Gradient of $G = z - g(x,y)$ is normal, same as B up to sign.

**Correct:** B, D


#### 11. Which of the following statements about flux through a surface are correct?  
A) ✓ Flux depends on the speed (magnitude) of the vector field.  
B) ✗ Flux depends on orientation; reversing normal reverses flux sign.  
C) ✗ Flux is zero if vector field is tangent, not maximized.  
D) ✗ Flux is zero if vector field is perpendicular to normal (i.e., tangent), not the other way.

**Correct:** A


#### 12. The flux of a vector field $\mathbf{F}$ across a surface $\sigma$ oriented by unit normal $\mathbf{n}$ is given by:  
A) ✓ Correct formula for flux.  
B) ✗ Cross product is not used for flux.  
C) ✗ Line integral around boundary is circulation, not flux.  
D) ✗ Magnitude alone does not account for direction.

**Correct:** A


#### 13. If a surface $\sigma$ is non-orientable, which of the following is true?  
A) ✓ Cannot define continuous unit normal vector field on $\sigma$.  
B) ✗ Surface integral can be defined but orientation issues arise; not always zero.  
C) ✓ Non-orientable surfaces have only one side.  
D) ✓ Can be parametrized locally, but global orientation fails.

**Correct:** A, C, D


#### 14. When using Green’s Theorem to find the area of a planar region, which of the following vector fields can be used?  
A) ✓ $\mathbf{F} = (-y, x)$ is classic for area calculation.  
B) ✗ $(x,y)$ does not yield area via Green’s Theorem.  
C) ✗ $(0,x)$ does not produce area formula.  
D) ✗ $(y,0)$ also does not produce area formula.

**Correct:** A


#### 15. Which of the following statements about the orientation of a parametric surface are true?  
A) ✓ Orientation depends on order of parameters in cross product.  
B) ✓ Reversing order reverses orientation (normal vector direction).  
C) ✗ Orientation depends on parametrization, not independent of it.  
D) ✓ Negative orientation corresponds to negative normal vector.

**Correct:** A, B, D


#### 16. For the vector field $\mathbf{F}(x,y,z) = z \mathbf{k}$, what is the flux through the sphere $x^2 + y^2 + z^2 = a^2$ oriented outward?  
A) ✗ Not zero because $\mathbf{F}$ has nonzero normal component.  
B) ✓ Flux is proportional to volume via divergence theorem.  
C) ✗ Flux depends on volume, not surface area directly.  
D) ✓ Flux depends on radius $a$ through volume or surface area.

**Correct:** B, D


#### 17. Which of the following surfaces can be expressed as level surfaces $G(x,y,z) = 0$ for some function $G$?  
A) ✓ $z = g(x,y)$ can be rewritten as $G = z - g(x,y)$.  
B) ✓ $y = g(z,x)$ can be rewritten as $G = y - g(z,x)$.  
C) ✓ $x = g(y,z)$ can be rewritten as $G = x - g(y,z)$.  
D) ✗ All explicit surfaces can be expressed as level surfaces.

**Correct:** A, B, C


#### 18. When calculating the surface integral of a vector field over a surface defined by $z = g(x,y)$, which of the following integrals correctly represents the flux with positive orientation?  
A) ✗ Missing normalization factor; not unit normal.  
B) ✓ Correct: dot product with unit normal times area element.  
C) ✗ Wrong sign convention for normal vector.  
D) ✓ General correct form using unit normal and surface element.

**Correct:** B, D


#### 19. Which of the following are true about the proof of Green’s Theorem?  
A) ✓ Proof is straightforward for standard regions like rectangles.  
B) ✗ Convexity is not required; simply connectedness suffices.  
C) ✓ Extension to multiply connected regions involves holes with opposite orientation.  
D) ✓ Proof uses 2D version of Fundamental Theorem of Calculus.

**Correct:** A, C, D


#### 20. Which of the following statements about the surface integral of a scalar function are correct?  
A) ✓ Surface integrals generalize line integrals to 2D surfaces.  
B) ✓ Surface must be smooth or piecewise smooth for integral to be well-defined.  
C) ✗ Limit defining integral does not depend on choice of sample points if integral exists.  
D) ✓ Surface integral can be computed via projection with adjustment factor involving partial derivatives.

**Correct:** A, B, D