## 4. Triple Integrals in Other Coordinate Systems

## Questions

#### 1. Which of the following correctly express the Cartesian coordinates $(x,y,z)$ in terms of spherical coordinates $(\rho, \phi, \theta)$?  
A) $x = \rho \cos \phi \cos \theta$  
B) $x = \rho \sin \phi \cos \theta$  
C) $y = \rho \sin \phi \sin \theta$  
D) $z = \rho \cos \phi$  


#### 2. The volume element $dV$ in spherical coordinates is given by:  
A) $dV = \rho \sin \phi \, d\rho \, d\phi \, d\theta$  
B) $dV = \rho^2 \sin \phi \, d\rho \, d\phi \, d\theta$  
C) $dV = \rho^2 \cos \phi \, d\rho \, d\phi \, d\theta$  
D) $dV = \rho^2 \sin \theta \, d\rho \, d\phi \, d\theta$  


#### 3. When converting a triple integral from Cartesian to spherical coordinates, which of the following must be included in the integrand?  
A) The Jacobian determinant $\rho^2 \sin \phi$  
B) The factor $\sin \theta$  
C) The substitution $x = \rho \sin \phi \cos \theta$  
D) The substitution $z = \rho \cos \phi$  


#### 4. For the spherical coordinate $\phi$, which of the following statements is true?  
A) $\phi$ is the angle measured from the positive $z$-axis downward.  
B) $\phi$ ranges from $0$ to $2\pi$.  
C) $\phi$ is the azimuthal angle in the $xy$-plane.  
D) $\phi$ ranges from $0$ to $\pi$.  


#### 5. The Jacobian determinant for a transformation $T: (u,v) \to (x,y)$ is zero at a point if:  
A) The transformation is locally area-preserving at that point.  
B) The transformation is not one-to-one near that point.  
C) The transformation collapses a region to a line or point near that point.  
D) The transformation is invertible at that point.  


#### 6. Which of the following correctly describe the geometric meaning of the Jacobian determinant in two variables?  
A) It measures the scaling factor of area elements under the transformation.  
B) It measures the scaling factor of volume elements under the transformation.  
C) It can be negative, indicating orientation reversal.  
D) It is always positive for any transformation.  


#### 7. Consider the transformation $x = u^2 - v^2$, $y = 2uv$. Which of the following statements about its Jacobian are true?  
A) The Jacobian is zero at $u = v = 0$.  
B) The Jacobian is constant everywhere.  
C) The transformation is one-to-one everywhere.  
D) The Jacobian can be negative depending on $u,v$.  


#### 8. When applying the change of variables formula for triple integrals, which conditions must the Jacobian satisfy?  
A) It must be non-zero everywhere in the region of integration.  
B) It must not change sign in the region of integration.  
C) It must be positive everywhere.  
D) It can be zero at isolated points without affecting the integral.  


#### 9. Which of the following are true about the limits of integration in spherical coordinates for a full sphere of radius $R$?  
A) $\rho$ ranges from 0 to $R$.  
B) $\phi$ ranges from 0 to $\pi$.  
C) $\theta$ ranges from 0 to $\pi$.  
D) $\theta$ ranges from 0 to $2\pi$.  


#### 10. The triple integral $\iiint_G f(x,y,z) \, dV$ over a spherical region $G$ can be simplified by:  
A) Expressing $f$ in terms of $\rho, \phi, \theta$.  
B) Using the volume element $\rho^2 \sin \phi \, d\rho \, d\phi \, d\theta$.  
C) Ignoring the Jacobian if $f$ is constant.  
D) Changing the order of integration arbitrarily without adjusting limits.  


#### 11. Which of the following statements about the inverse transformation $T^{-1}$ are correct?  
A) It maps points from the $xy$-plane back to the $uv$-plane.  
B) It exists only if $T$ is one-to-one.  
C) It always exists regardless of $T$.  
D) It is used to find the original variables after substitution.  


#### 12. In the context of transformations, constant $u$-curves in the $xy$-plane correspond to:  
A) Images of vertical lines in the $uv$-plane.  
B) Images of horizontal lines in the $uv$-plane.  
C) Curves where $u$ is fixed and $v$ varies.  
D) Curves where $v$ is fixed and $u$ varies.  


#### 13. Which of the following are true about the Jacobian determinant in three variables?  
A) It is a 3x3 determinant involving partial derivatives of $x,y,z$ with respect to $u,v,w$.  
B) It measures the scaling factor of volume elements under the transformation.  
C) It is always positive for spherical coordinate transformations.  
D) It can be zero if the transformation is not locally invertible.  


#### 14. When integrating over a spherical shell defined by $a \leq \rho \leq b$, $0 \leq \phi \leq \pi$, $0 \leq \theta \leq 2\pi$, which of the following are true?  
A) The volume element remains $\rho^2 \sin \phi \, d\rho \, d\phi \, d\theta$.  
B) The limits for $\phi$ can be changed to $0 \leq \phi \leq \pi/2$ without changing the region.  
C) The integral can be split into two integrals over $\rho$ and $\phi, \theta$ separately.  
D) The integral limits for $\theta$ must always be from 0 to $2\pi$ for full rotation.  


#### 15. Which of the following statements about the substitution $x = g(u)$ in single integrals are correct?  
A) The substitution requires $g$ to be differentiable and one-to-one.  
B) The integral transforms as $\int f(x) dx = \int f(g(u)) |g'(u)| du$.  
C) The substitution can be applied even if $g$ is not invertible.  
D) The limits of integration must be changed according to $g$.  


#### 16. In spherical coordinates, which of the following statements about the angle $\theta$ are true?  
A) $\theta$ is measured in the $xy$-plane from the positive $x$-axis.  
B) $\theta$ ranges from 0 to $\pi$.  
C) $\theta$ ranges from 0 to $2\pi$.  
D) $\theta$ is the angle between the radius vector and the $z$-axis.  


#### 17. Which of the following are necessary to correctly evaluate a triple integral after a change of variables?  
A) Express the integrand in terms of the new variables.  
B) Multiply the integrand by the absolute value of the Jacobian determinant.  
C) Keep the original limits of integration.  
D) Change the limits of integration to correspond to the new variables.  


#### 18. Consider the transformation $x = \rho \sin \phi \cos \theta$, $y = \rho \sin \phi \sin \theta$, $z = \rho \cos \phi$. Which of the following are true?  
A) The Jacobian determinant is $\rho^2 \sin \phi$.  
B) The transformation is one-to-one for $\rho > 0$, $0 < \phi < \pi$, $0 \leq \theta < 2\pi$.  
C) The transformation fails to be one-to-one at $\phi = 0$ or $\pi$.  
D) The volume element in Cartesian coordinates is $dV = d\rho \, d\phi \, d\theta$.  


#### 19. Which of the following statements about the image of a set $S$ under a transformation $T$ are true?  
A) The image is the set of all points $(x,y)$ obtained by applying $T$ to every point in $S$.  
B) If $T$ is one-to-one, the image uniquely corresponds to $S$.  
C) The image always has the same area as $S$.  
D) The image can be visualized by mapping vertical and horizontal lines in $S$ to curves in the image.  


#### 20. When evaluating the volume of a sphere using spherical coordinates, which of the following steps are essential?  
A) Set $\rho$ limits from 0 to the radius $R$.  
B) Set $\phi$ limits from 0 to $\pi$.  
C) Set $\theta$ limits from 0 to $2\pi$.  
D) Use the volume element $\rho \sin \phi \, d\rho \, d\phi \, d\theta$.



<br>

## Answers

#### 1. Which of the following correctly express the Cartesian coordinates $(x,y,z)$ in terms of spherical coordinates $(\rho, \phi, \theta)$?  
A) ✗ Incorrect formula; $\cos \phi$ is for $z$, not $x$.  
B) ✓ Correct formula for $x$.  
C) ✓ Correct formula for $y$.  
D) ✓ Correct formula for $z$.  

**Correct:** B, C, D


#### 2. The volume element $dV$ in spherical coordinates is given by:  
A) ✗ Missing $\rho^2$ factor.  
B) ✓ Correct volume element formula.  
C) ✗ Incorrect factor; should be $\sin \phi$, not $\cos \phi$.  
D) ✗ Incorrect angular factor; $\sin \theta$ is not part of volume element.  

**Correct:** B


#### 3. When converting a triple integral from Cartesian to spherical coordinates, which of the following must be included in the integrand?  
A) ✓ The Jacobian factor $\rho^2 \sin \phi$ is essential.  
B) ✗ $\sin \theta$ is not part of the volume element.  
C) ✓ Correct substitution for $x$.  
D) ✓ Correct substitution for $z$.  

**Correct:** A, C, D


#### 4. For the spherical coordinate $\phi$, which of the following statements is true?  
A) ✓ $\phi$ is measured from the positive $z$-axis downward.  
B) ✗ $\phi$ ranges from 0 to $\pi$, not $2\pi$.  
C) ✗ $\theta$ is the azimuthal angle, not $\phi$.  
D) ✓ Correct range for $\phi$.  

**Correct:** A, D


#### 5. The Jacobian determinant for a transformation $T: (u,v) \to (x,y)$ is zero at a point if:  
A) ✗ Zero Jacobian means area is not preserved.  
B) ✓ Zero Jacobian implies local non-invertibility (not one-to-one).  
C) ✓ Zero Jacobian means collapse to lower dimension (line or point).  
D) ✗ Zero Jacobian means transformation is not invertible there.  

**Correct:** B, C


#### 6. Which of the following correctly describe the geometric meaning of the Jacobian determinant in two variables?  
A) ✓ Measures area scaling under transformation.  
B) ✗ Volume scaling applies to 3D Jacobian, not 2D.  
C) ✓ Can be negative, indicating orientation reversal.  
D) ✗ Jacobian can be negative; not always positive.  

**Correct:** A, C


#### 7. Consider the transformation $x = u^2 - v^2$, $y = 2uv$. Which of the following statements about its Jacobian are true?  
A) ✓ Jacobian is zero at $u=v=0$.  
B) ✗ Jacobian varies with $u,v$, not constant.  
C) ✗ Transformation is not one-to-one everywhere (e.g., at origin).  
D) ✓ Jacobian can be negative depending on $u,v$.  

**Correct:** A, D


#### 8. When applying the change of variables formula for triple integrals, which conditions must the Jacobian satisfy?  
A) ✓ Must be non-zero in the region to ensure invertibility.  
B) ✓ Must not change sign to keep orientation consistent.  
C) ✗ Jacobian can be negative but must not change sign; positivity is not mandatory.  
D) ✗ Zero Jacobian at points invalidates the formula there.  

**Correct:** A, B


#### 9. Which of the following are true about the limits of integration in spherical coordinates for a full sphere of radius $R$?  
A) ✓ $\rho$ from 0 to $R$ covers radial distance.  
B) ✓ $\phi$ from 0 to $\pi$ covers polar angle fully.  
C) ✗ $\theta$ ranges from 0 to $2\pi$, not $\pi$.  
D) ✓ $\theta$ from 0 to $2\pi$ covers full azimuthal rotation.  

**Correct:** A, B, D


#### 10. The triple integral $\iiint_G f(x,y,z) \, dV$ over a spherical region $G$ can be simplified by:  
A) ✓ Expressing $f$ in spherical coordinates.  
B) ✓ Using the correct volume element $\rho^2 \sin \phi \, d\rho \, d\phi \, d\theta$.  
C) ✗ Jacobian cannot be ignored even if $f$ is constant.  
D) ✗ Limits must be adjusted carefully when changing order.  

**Correct:** A, B


#### 11. Which of the following statements about the inverse transformation $T^{-1}$ are correct?  
A) ✓ Maps from $xy$-plane back to $uv$-plane.  
B) ✓ Exists only if $T$ is one-to-one.  
C) ✗ Does not always exist; depends on $T$.  
D) ✓ Used to revert variables after substitution.  

**Correct:** A, B, D


#### 12. In the context of transformations, constant $u$-curves in the $xy$-plane correspond to:  
A) ✓ Images of vertical lines in the $uv$-plane (where $u$ is fixed).  
B) ✗ Horizontal lines correspond to constant $v$-curves.  
C) ✓ Curves where $u$ is fixed and $v$ varies.  
D) ✗ This describes constant $v$-curves, not $u$-curves.  

**Correct:** A, C


#### 13. Which of the following are true about the Jacobian determinant in three variables?  
A) ✓ It is a 3x3 determinant of partial derivatives.  
B) ✓ Measures volume scaling under transformation.  
C) ✗ Jacobian can be negative; not always positive for spherical coordinates.  
D) ✓ Zero Jacobian means local non-invertibility.  

**Correct:** A, B, D


#### 14. When integrating over a spherical shell defined by $a \leq \rho \leq b$, $0 \leq \phi \leq \pi$, $0 \leq \theta \leq 2\pi$, which of the following are true?  
A) ✓ Volume element remains $\rho^2 \sin \phi \, d\rho \, d\phi \, d\theta$.  
B) ✗ Changing $\phi$ limits to $\pi/2$ changes the region (only hemisphere).  
C) ✗ Integral cannot be split arbitrarily; limits depend on region.  
D) ✓ $\theta$ must range 0 to $2\pi$ for full rotation.  

**Correct:** A, D


#### 15. Which of the following statements about the substitution $x = g(u)$ in single integrals are correct?  
A) ✓ $g$ must be differentiable and one-to-one for valid substitution.  
B) ✓ Integral transforms with $|g'(u)|$ factor.  
C) ✗ Substitution fails if $g$ is not invertible.  
D) ✓ Limits must be changed according to $g$.  

**Correct:** A, B, D


#### 16. In spherical coordinates, which of the following statements about the angle $\theta$ are true?  
A) ✓ $\theta$ is measured in the $xy$-plane from positive $x$-axis.  
B) ✗ $\theta$ ranges from 0 to $2\pi$, not $\pi$.  
C) ✓ Correct range for $\theta$.  
D) ✗ $\theta$ is not the angle with the $z$-axis; that is $\phi$.  

**Correct:** A, C


#### 17. Which of the following are necessary to correctly evaluate a triple integral after a change of variables?  
A) ✓ Express integrand in new variables.  
B) ✓ Multiply by absolute Jacobian determinant.  
C) ✗ Original limits must be changed to new variable limits.  
D) ✓ Change limits to correspond to new variables.  

**Correct:** A, B, D


#### 18. Consider the transformation $x = \rho \sin \phi \cos \theta$, $y = \rho \sin \phi \sin \theta$, $z = \rho \cos \phi$. Which of the following are true?  
A) ✓ Jacobian is $\rho^2 \sin \phi$.  
B) ✓ Transformation is one-to-one for $\rho > 0$, $0 < \phi < \pi$, $0 \leq \theta < 2\pi$.  
C) ✓ Not one-to-one at $\phi = 0$ or $\pi$ (poles collapse).  
D) ✗ Volume element is not simply $d\rho \, d\phi \, d\theta$; must include Jacobian.  

**Correct:** A, B, C


#### 19. Which of the following statements about the image of a set $S$ under a transformation $T$ are true?  
A) ✓ Image is all points $(x,y)$ from applying $T$ to $S$.  
B) ✓ One-to-one $T$ means unique correspondence between $S$ and image.  
C) ✗ Image area can differ from $S$ due to scaling by Jacobian.  
D) ✓ Image can be visualized by mapping lines in $S$ to curves.  

**Correct:** A, B, D


#### 20. When evaluating the volume of a sphere using spherical coordinates, which of the following steps are essential?  
A) ✓ $\rho$ limits from 0 to radius $R$.  
B) ✓ $\phi$ limits from 0 to $\pi$.  
C) ✓ $\theta$ limits from 0 to $2\pi$.  
D) ✗ Volume element must be $\rho^2 \sin \phi \, d\rho \, d\phi \, d\theta$, not $\rho \sin \phi$.  

**Correct:** A, B, C