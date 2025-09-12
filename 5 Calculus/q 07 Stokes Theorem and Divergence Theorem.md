## 7. Stokes Theorem and Divergence Theorem

## Questions

#### 1. Which of the following conditions are necessary for Stokes' Theorem to hold on a surface $\sigma$ bounded by a curve $C$?  
A) The surface $\sigma$ must be piecewise smooth and oriented.  
B) The vector field $\mathbf{F}$ must have continuous components but not necessarily continuous partial derivatives.  
C) The curve $C$ must be a simple, closed, piecewise smooth curve with positive orientation.  
D) The vector field $\mathbf{F}$ must be defined and have continuous first partial derivatives on an open set containing $\sigma$.


#### 2. Stokes' Theorem relates which two types of integrals?  
A) A line integral of a vector field around a closed curve and a surface integral of the curl of the vector field over the surface bounded by the curve.  
B) A surface integral of a vector field and a volume integral of the divergence of the vector field.  
C) A line integral of a scalar function and a double integral over a plane region.  
D) A volume integral of the curl of a vector field and a surface integral of the vector field.


#### 3. The curl of a vector field $\mathbf{F}$ at a point measures:  
A) The rate of change of $\mathbf{F}$ in the direction of the gradient.  
B) The tendency of $\mathbf{F}$ to rotate or swirl around that point.  
C) The net flux of $\mathbf{F}$ out of a small volume around the point.  
D) The divergence of $\mathbf{F}$ at that point.


#### 4. Which of the following statements about the orientation of the curve $C$ and surface $\sigma$ in Stokes' Theorem is true?  
A) The curve $C$ must be oriented clockwise when viewed from the direction of the unit normal vector $\mathbf{n}$.  
B) The curve $C$ must be oriented counterclockwise when viewed from the direction of the unit normal vector $\mathbf{n}$.  
C) The orientation of $C$ and $\sigma$ are unrelated.  
D) The orientation of $C$ is always clockwise regardless of $\mathbf{n}$.


#### 5. Green's Theorem can be seen as a special case of Stokes' Theorem when:  
A) The surface $\sigma$ lies in the xy-plane and the vector field has zero k-component.  
B) The surface $\sigma$ is a sphere.  
C) The vector field is constant.  
D) The curve $C$ is not closed.


#### 6. The Divergence Theorem requires which of the following conditions?  
A) The surface $\sigma$ must be closed and orientable.  
B) The vector field $\mathbf{F}$ must have continuous partial derivatives on an open set containing the volume $R$.  
C) The surface $\sigma$ can be open as long as the vector field is smooth.  
D) The volume $R$ enclosed by $\sigma$ must be bounded.


#### 7. The Divergence Theorem states that the flux of $\mathbf{F}$ through a closed surface $\sigma$ equals:  
A) The surface integral of the curl of $\mathbf{F}$ over $\sigma$.  
B) The triple integral of the divergence of $\mathbf{F}$ over the volume enclosed by $\sigma$.  
C) The line integral of $\mathbf{F}$ around the boundary of $\sigma$.  
D) The double integral of $\mathbf{F}$ over the surface $\sigma$.


#### 8. If the divergence of a vector field $\mathbf{F}$ at a point $P_0$ is positive, this implies:  
A) The vector field is swirling around $P_0$.  
B) There is a net "outflow" or source of the vector field at $P_0$.  
C) The vector field is incompressible at $P_0$.  
D) The flux of $\mathbf{F}$ through a small sphere around $P_0$ is positive.


#### 9. Which of the following best describes the physical interpretation of divergence in fluid flow?  
A) Divergence measures the rotation of fluid particles.  
B) Divergence measures the net rate of fluid volume expansion or compression at a point.  
C) Divergence measures the velocity magnitude of the fluid.  
D) Divergence measures the total circulation around a closed loop.


#### 10. When applying Stokes' Theorem, if the surface $\sigma$ is not flat, how does this affect the evaluation of the line integral around $C$?  
A) The line integral must be computed directly since the surface is curved.  
B) The line integral can still be computed by evaluating the surface integral of the curl over $\sigma$.  
C) The theorem does not apply to curved surfaces.  
D) The orientation of the surface normal vector $\mathbf{n}$ becomes irrelevant.


#### 11. Consider a vector field $\mathbf{F} = f(x,y,z)\mathbf{i} + g(x,y,z)\mathbf{j} + h(x,y,z)\mathbf{k}$. Which of the following must be true for the Divergence Theorem to be applicable?  
A) $f, g, h$ must be continuous functions.  
B) The partial derivatives $\frac{\partial f}{\partial x}, \frac{\partial g}{\partial y}, \frac{\partial h}{\partial z}$ must exist and be continuous.  
C) The vector field must be conservative.  
D) The vector field must be divergence-free.


#### 12. The flux of a vector field $\mathbf{F}$ through a surface $S$ is zero. Which of the following can be concluded?  
A) The divergence of $\mathbf{F}$ inside the volume enclosed by $S$ is zero everywhere.  
B) The vector field $\mathbf{F}$ has no sources or sinks inside the volume enclosed by $S$.  
C) The vector field $\mathbf{F}$ is tangent to the surface $S$ everywhere.  
D) The vector field $\mathbf{F}$ is divergence-free everywhere inside the volume enclosed by $S$.


#### 13. Which of the following statements about the curl operator is true?  
A) The curl of a gradient field is always zero.  
B) The curl of a divergence-free field is always zero.  
C) The curl measures the infinitesimal rotation of a vector field.  
D) The curl is a scalar quantity.


#### 14. When using the Divergence Theorem on a region bounded by coordinate planes and a plane $x + y + z = 1$, which of the following is true?  
A) The volume integral is taken over the tetrahedron formed by these planes.  
B) The surface integral must be evaluated only on the plane $x + y + z = 1$.  
C) The outward normal vector on the coordinate planes points inward to the volume.  
D) The flux through the coordinate planes contributes to the total flux.


#### 15. If a vector field $\mathbf{F}$ has zero curl everywhere in a simply connected region, then:  
A) The line integral of $\mathbf{F}$ around any closed curve in the region is zero.  
B) $\mathbf{F}$ is conservative in that region.  
C) The divergence of $\mathbf{F}$ must be zero.  
D) Stokes' Theorem cannot be applied.


#### 16. Which of the following integrals can be converted using Stokes' Theorem?  
A) $\oint_C \mathbf{F} \cdot d\mathbf{r}$, where $C$ is a closed curve bounding a surface $\sigma$.  
B) $\iint_\sigma (\nabla \times \mathbf{F}) \cdot \mathbf{n} \, dS$, where $\sigma$ is bounded by $C$.  
C) $\iiint_R \nabla \cdot \mathbf{F} \, dV$, where $R$ is enclosed by $\sigma$.  
D) $\oint_C \mathbf{F} \cdot \mathbf{n} \, dS$, where $C$ is a closed curve.


#### 17. The limit definition of divergence at a point $P_0$ involves:  
A) The limit of the circulation per unit area around $P_0$.  
B) The limit of the flux per unit volume through a shrinking sphere centered at $P_0$.  
C) The limit of the surface integral of the curl over a shrinking surface around $P_0$.  
D) The limit of the line integral of $\mathbf{F}$ around a shrinking curve enclosing $P_0$.


#### 18. Which of the following statements about the unit normal vector $\mathbf{n}$ in surface integrals is correct?  
A) $\mathbf{n}$ must always point inward to the enclosed volume.  
B) $\mathbf{n}$ is used to define the orientation of the surface integral.  
C) The choice of $\mathbf{n}$ affects the sign of the surface integral.  
D) $\mathbf{n}$ is irrelevant in the Divergence Theorem.


#### 19. When evaluating the flux of $\mathbf{F} = xy \mathbf{i} - z^2 \mathbf{k}$ through the upper five faces of the unit cube $[0,1]^3$, which of the following is true?  
A) The surface is closed, so the Divergence Theorem applies directly.  
B) The surface is not closed, so the flux through the missing face must be accounted for.  
C) The flux through the missing face is zero because $\mathbf{F}$ has no j-component.  
D) The flux can be computed by summing the flux through each of the five faces.


#### 20. Which of the following best describes the relationship between the curl and divergence of a vector field?  
A) Curl measures rotation, divergence measures expansion or compression.  
B) Both curl and divergence are scalar quantities.  
C) A vector field can have zero curl but nonzero divergence.  
D) A vector field can have zero divergence but nonzero curl.



<br>

## Answers

#### 1. Which of the following conditions are necessary for Stokes' Theorem to hold on a surface $\sigma$ bounded by a curve $C$?  
A) ✓ The surface must be piecewise smooth and oriented for the theorem to apply.  
B) ✗ Continuous components alone are not enough; continuous first partial derivatives are required.  
C) ✓ The curve must be simple, closed, piecewise smooth, and positively oriented.  
D) ✓ The vector field must have continuous first partial derivatives on an open set containing $\sigma$.

**Correct:** A, C, D


#### 2. Stokes' Theorem relates which two types of integrals?  
A) ✓ Correct: line integral around a closed curve equals surface integral of curl over the bounded surface.  
B) ✗ This describes the Divergence Theorem, not Stokes'.  
C) ✗ This is Green’s Theorem but not Stokes' Theorem in 3D.  
D) ✗ Curl is not integrated over volume in Stokes' Theorem.

**Correct:** A


#### 3. The curl of a vector field $\mathbf{F}$ at a point measures:  
A) ✗ This describes directional derivative or gradient, not curl.  
B) ✓ Correct: curl measures local rotation or swirling tendency.  
C) ✗ This describes divergence, not curl.  
D) ✗ Divergence is a different operator from curl.

**Correct:** B


#### 4. Which of the following statements about the orientation of the curve $C$ and surface $\sigma$ in Stokes' Theorem is true?  
A) ✗ Curve orientation must be counterclockwise relative to $\mathbf{n}$, not clockwise.  
B) ✓ Correct: positive orientation means counterclockwise when viewed along $\mathbf{n}$.  
C) ✗ Orientation of $C$ and $\sigma$ are linked by the right-hand rule.  
D) ✗ Orientation depends on $\mathbf{n}$, not always clockwise.

**Correct:** B


#### 5. Green's Theorem can be seen as a special case of Stokes' Theorem when:  
A) ✓ Correct: surface lies in xy-plane and vector field has zero k-component.  
B) ✗ Sphere is a curved surface, not planar, so not Green’s Theorem.  
C) ✗ Vector field being constant is not a condition for Green’s Theorem.  
D) ✗ Curve must be closed for Green’s Theorem to apply.

**Correct:** A


#### 6. The Divergence Theorem requires which of the following conditions?  
A) ✓ Surface must be closed and orientable to enclose a volume.  
B) ✓ Vector field must have continuous partial derivatives on an open set containing the volume.  
C) ✗ Surface cannot be open; theorem requires closed surface.  
D) ✓ Volume must be bounded to apply the theorem properly.

**Correct:** A, B, D


#### 7. The Divergence Theorem states that the flux of $\mathbf{F}$ through a closed surface $\sigma$ equals:  
A) ✗ This is Stokes' Theorem, not Divergence Theorem.  
B) ✓ Correct: flux equals triple integral of divergence over enclosed volume.  
C) ✗ Line integral around boundary curve is unrelated here.  
D) ✗ Surface integral of $\mathbf{F}$ alone is flux, but theorem relates it to volume integral of divergence.

**Correct:** B


#### 8. If the divergence of a vector field $\mathbf{F}$ at a point $P_0$ is positive, this implies:  
A) ✗ Curl measures rotation, not divergence.  
B) ✓ Correct: positive divergence means net outflow or source at $P_0$.  
C) ✗ Zero divergence means incompressible; positive divergence means expansion.  
D) ✓ Positive divergence implies positive flux through small sphere around $P_0$.

**Correct:** B, D


#### 9. Which of the following best describes the physical interpretation of divergence in fluid flow?  
A) ✗ Divergence measures expansion/compression, not rotation.  
B) ✓ Correct: divergence measures net volume expansion or compression rate at a point.  
C) ✗ Velocity magnitude is unrelated to divergence.  
D) ✗ Circulation relates to curl, not divergence.

**Correct:** B


#### 10. When applying Stokes' Theorem, if the surface $\sigma$ is not flat, how does this affect the evaluation of the line integral around $C$?  
A) ✗ The theorem still applies regardless of surface curvature.  
B) ✓ Correct: line integral equals surface integral of curl over curved surface.  
C) ✗ The theorem applies to piecewise smooth surfaces, curved or flat.  
D) ✗ Orientation of $\mathbf{n}$ remains important.

**Correct:** B


#### 11. Consider a vector field $\mathbf{F} = f(x,y,z)\mathbf{i} + g(x,y,z)\mathbf{j} + h(x,y,z)\mathbf{k}$. Which of the following must be true for the Divergence Theorem to be applicable?  
A) ✓ Components must be continuous for integrals to exist.  
B) ✓ Partial derivatives must exist and be continuous for divergence to be defined.  
C) ✗ Vector field need not be conservative for Divergence Theorem.  
D) ✗ Vector field need not be divergence-free; divergence is generally nonzero.

**Correct:** A, B


#### 12. The flux of a vector field $\mathbf{F}$ through a surface $S$ is zero. Which of the following can be concluded?  
A) ✗ Zero flux does not guarantee zero divergence everywhere inside.  
B) ✗ Zero flux does not guarantee no sources or sinks inside.  
C) ✗ Vector field can have normal components; zero flux is net effect.  
D) ✗ Zero flux alone does not imply divergence-free everywhere.

**Correct:** (None)


#### 13. Which of the following statements about the curl operator is true?  
A) ✓ Correct: curl of a gradient field is always zero.  
B) ✗ Curl of divergence-free field need not be zero; divergence and curl are independent.  
C) ✓ Correct: curl measures infinitesimal rotation of vector field.  
D) ✗ Curl is a vector, not scalar.

**Correct:** A, C


#### 14. When using the Divergence Theorem on a region bounded by coordinate planes and a plane $x + y + z = 1$, which of the following is true?  
A) ✓ Correct: volume integral is over tetrahedron bounded by these planes.  
B) ✗ Surface integral must be over entire closed surface, not just one plane.  
C) ✗ Outward normals on coordinate planes point outward, not inward.  
D) ✓ Flux through coordinate planes contributes to total flux.

**Correct:** A, D


#### 15. If a vector field $\mathbf{F}$ has zero curl everywhere in a simply connected region, then:  
A) ✓ Correct: line integral around any closed curve is zero.  
B) ✓ Correct: $\mathbf{F}$ is conservative in simply connected region.  
C) ✗ Zero curl does not imply zero divergence.  
D) ✗ Stokes' Theorem still applies; zero curl just simplifies integrals.

**Correct:** A, B


#### 16. Which of the following integrals can be converted using Stokes' Theorem?  
A) ✓ Correct: line integral around closed curve bounding surface.  
B) ✓ Correct: surface integral of curl over surface bounded by curve.  
C) ✗ Triple volume integral relates to Divergence Theorem, not Stokes'.  
D) ✗ Line integral of $\mathbf{F} \cdot \mathbf{n}$ is not defined; $\mathbf{n}$ is normal vector, not tangent.

**Correct:** A, B


#### 17. The limit definition of divergence at a point $P_0$ involves:  
A) ✗ Circulation per unit area relates to curl, not divergence.  
B) ✓ Correct: flux per unit volume through shrinking sphere around $P_0$.  
C) ✗ Surface integral of curl relates to circulation, not divergence.  
D) ✗ Line integral around shrinking curve relates to curl.

**Correct:** B


#### 18. Which of the following statements about the unit normal vector $\mathbf{n}$ in surface integrals is correct?  
A) ✗ $\mathbf{n}$ must point outward, not inward, for Divergence Theorem.  
B) ✓ Correct: $\mathbf{n}$ defines orientation of surface integral.  
C) ✓ Correct: changing $\mathbf{n}$ to opposite direction changes sign of integral.  
D) ✗ $\mathbf{n}$ is essential in Divergence Theorem for flux direction.

**Correct:** B, C


#### 19. When evaluating the flux of $\mathbf{F} = xy \mathbf{i} - z^2 \mathbf{k}$ through the upper five faces of the unit cube $[0,1]^3$, which of the following is true?  
A) ✗ Surface is not closed; missing bottom face.  
B) ✓ Correct: missing face must be accounted for to apply Divergence Theorem.  
C) ✗ Flux through missing face is not necessarily zero; depends on $\mathbf{F}$.  
D) ✓ Correct: flux can be computed by summing flux through each face.

**Correct:** B, D


#### 20. Which of the following best describes the relationship between the curl and divergence of a vector field?  
A) ✓ Correct: curl measures rotation; divergence measures expansion/compression.  
B) ✗ Both are vector operators; divergence is scalar, curl is vector.  
C) ✓ Correct: zero curl but nonzero divergence is possible.  
D) ✓ Correct: zero divergence but nonzero curl is possible.

**Correct:** A, C, D