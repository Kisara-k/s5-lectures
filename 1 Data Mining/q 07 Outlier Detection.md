## 7. Outlier Detection

## Questions

#### 1. Which of the following statements correctly distinguish outliers from noise?  
A) Noise is random error or variance, while outliers violate the normal data generation process.  
B) Outliers are always errors in data measurement, noise is not.  
C) Noise can obscure the detection of outliers.  
D) Outliers and noise are interchangeable terms in data analysis.


#### 2. What are the main types of outliers in data analysis?  
A) Global outliers  
B) Contextual outliers  
C) Collective outliers  
D) Temporal outliers


#### 3. Which of the following best describes a contextual outlier?  
A) A data point that deviates significantly regardless of context.  
B) A data point that is unusual only within a specific context such as time or location.  
C) A group of data points that collectively deviate from the norm.  
D) A data point that is far from all other points in the dataset.


#### 4. In proximity-based outlier detection, what is the significance of the k-distance of an object?  
A) It is the distance to the nearest neighbor.  
B) It is the distance to the k-th nearest neighbor.  
C) It defines the boundary of the k-distance neighborhood.  
D) It is always equal to the maximum distance to any neighbor.


#### 5. Which challenges are commonly faced in outlier detection?  
A) Defining a clear boundary between normal and outlier data.  
B) Handling noise that may hide outliers.  
C) Ensuring outliers always belong to small clusters.  
D) Application-specific definitions of normal behavior.


#### 6. Which of the following statements about supervised outlier detection methods are true?  
A) They require labeled examples of both normal and outlier data.  
B) They can easily handle class imbalance without any special techniques.  
C) Recall (catching as many outliers as possible) is often prioritized over accuracy.  
D) They cannot detect new types of outliers not seen in training data.


#### 7. What is a key limitation of unsupervised outlier detection methods?  
A) They require labeled data to function.  
B) They cannot effectively detect collective outliers.  
C) They assume normal data forms clusters.  
D) They always outperform supervised methods.


#### 8. Which of the following are true about statistical/model-based outlier detection methods?  
A) They assume normal data follows a known statistical distribution.  
B) Parametric methods require a fixed number of parameters.  
C) Non-parametric methods are completely parameter-free.  
D) Their effectiveness depends on how well the model fits the real data.


#### 9. In the context of kernel density estimation for outlier detection, which statements are correct?  
A) Each observed data point contributes to the estimated density in its neighborhood.  
B) The kernel function must be non-negative and symmetric.  
C) Kernel density estimation assumes data follows a normal distribution.  
D) Choosing the kernel bandwidth affects the detection sensitivity.


#### 10. Which of the following describe collective outliers?  
A) Individual points that are far from all other points.  
B) Groups of points that together deviate significantly from the norm.  
C) Points that are outliers only in certain contexts.  
D) Outliers that can be detected by examining relationships among data points.


#### 11. What is the main idea behind reconstruction-based outlier detection methods?  
A) Outliers are points that cannot be well reconstructed from a succinct representation of normal data.  
B) Outliers are points that have the highest reconstruction error.  
C) Reconstruction-based methods only apply to categorical data.  
D) Matrix factorization techniques like SVD are used for numeric data.


#### 12. Which of the following are true about the Local Outlier Factor (LOF) method?  
A) It compares the local density of a point to the densities of its neighbors.  
B) A point with a significantly lower local density than its neighbors is considered an outlier.  
C) LOF is a global outlier detection method.  
D) Reachability distance is used to smooth density estimation in LOF.


#### 13. In high-dimensional data, why does distance-based outlier detection become challenging?  
A) Data sparsity causes distances to lose meaning.  
B) The number of subspaces grows exponentially.  
C) Noise dominates the distance calculations.  
D) Outliers always become easier to detect in higher dimensions.


#### 14. Which of the following statements about one-class classification models for outlier detection are correct?  
A) They model only the normal class and detect points outside the learned boundary as outliers.  
B) They require labeled examples of both normal and outlier classes.  
C) They can detect new types of outliers not seen during training.  
D) They cannot handle multiple normal classes.


#### 15. When using the boxplot method for outlier detection, which of the following are true?  
A) Outliers are points outside Q1 - 1.5×IQR or Q3 + 1.5×IQR.  
B) The interquartile range (IQR) is Q3 - Q1.  
C) The boxplot method assumes data follows a normal distribution.  
D) The method identifies approximately 99.3% of data as non-outliers.


#### 16. Which of the following are challenges specific to contextual outlier detection?  
A) Defining meaningful contexts from data attributes.  
B) Transforming contextual outlier detection into conventional outlier detection.  
C) Ignoring behavioral attributes when detecting outliers.  
D) Handling cases where context is ambiguous or overlapping.


#### 17. In distance-based outlier detection, what does it mean if an object is a DB(p, D)-outlier?  
A) At least a fraction p of objects lie farther than distance D from it.  
B) The object is within distance D of at least p other objects.  
C) Increasing D makes the object more outlying.  
D) Increasing p makes the object less outlying.


#### 18. Which of the following statements about semi-supervised outlier detection methods are true?  
A) They can use labeled normal data to model normal behavior.  
B) They can use labeled outliers to improve detection but may struggle if outliers are rare.  
C) They do not rely on any unlabeled data.  
D) They combine clustering and classification techniques.


#### 19. Why might proximity-based methods fail to detect certain outliers?  
A) They cannot detect outliers that are close to each other (collective outliers).  
B) They require a perfect distance metric, which is always available.  
C) They always detect all global outliers.  
D) They struggle when normal data is not clustered.


#### 20. Which of the following are true about the Mahalanobis distance in multivariate outlier detection?  
A) It accounts for correlations between variables.  
B) It uses the covariance matrix of the data.  
C) It treats each dimension independently.  
D) Larger Mahalanobis distance indicates a more outlying point.



<br>

## Answers

#### 1. Which of the following statements correctly distinguish outliers from noise?  
A) ✓ Noise is random error or variance, while outliers violate the normal data generation process.  
B) ✗ Outliers are not always errors; they can be meaningful signals.  
C) ✓ Noise can obscure the detection of outliers by blurring distinctions.  
D) ✗ Outliers and noise are distinct concepts, not interchangeable.

**Correct:** A, C


#### 2. What are the main types of outliers in data analysis?  
A) ✓ Global outliers are a main type.  
B) ✓ Contextual outliers are a main type.  
C) ✓ Collective outliers are a main type.  
D) ✗ Temporal outliers are not a standard category here.

**Correct:** A, B, C


#### 3. Which of the following best describes a contextual outlier?  
A) ✗ This describes a global outlier, not contextual.  
B) ✓ Contextual outliers are unusual only within a specific context.  
C) ✗ This describes collective outliers.  
D) ✗ This describes global outliers.

**Correct:** B


#### 4. In proximity-based outlier detection, what is the significance of the k-distance of an object?  
A) ✗ It is not just the nearest neighbor but the k-th nearest neighbor.  
B) ✓ Correct definition of k-distance.  
C) ✓ k-distance defines the boundary of the k-distance neighborhood.  
D) ✗ It is not always the maximum distance to any neighbor.

**Correct:** B, C


#### 5. Which challenges are commonly faced in outlier detection?  
A) ✓ Defining clear boundaries is difficult.  
B) ✓ Noise can hide outliers.  
C) ✗ Outliers do not always belong to small clusters; this is domain-dependent.  
D) ✓ Definitions vary by application.

**Correct:** A, B, D


#### 6. Which of the following statements about supervised outlier detection methods are true?  
A) ✓ They require labeled examples for training.  
B) ✗ Class imbalance is a major challenge and requires special handling.  
C) ✓ Recall is prioritized to catch as many outliers as possible.  
D) ✗ They can struggle to detect unseen outliers but not always impossible.

**Correct:** A, C


#### 7. What is a key limitation of unsupervised outlier detection methods?  
A) ✗ They do not require labeled data.  
B) ✓ They cannot effectively detect collective outliers.  
C) ✓ They assume normal data forms clusters.  
D) ✗ They do not always outperform supervised methods.

**Correct:** B, C


#### 8. Which of the following are true about statistical/model-based outlier detection methods?  
A) ✓ They assume normal data follows a statistical model.  
B) ✓ Parametric methods have fixed parameters.  
C) ✗ Non-parametric methods are not completely parameter-free; parameters are flexible.  
D) ✓ Effectiveness depends on model fit.

**Correct:** A, B, D


#### 9. In the context of kernel density estimation for outlier detection, which statements are correct?  
A) ✓ Each data point influences density in its neighborhood.  
B) ✓ Kernel functions must be non-negative and symmetric.  
C) ✗ KDE does not assume normality; it is non-parametric.  
D) ✓ Bandwidth choice affects sensitivity.

**Correct:** A, B, D


#### 10. Which of the following describe collective outliers?  
A) ✗ This describes global outliers.  
B) ✓ Collective outliers are groups deviating together.  
C) ✗ This describes contextual outliers.  
D) ✓ Collective outliers require examining relationships.

**Correct:** B, D


#### 11. What is the main idea behind reconstruction-based outlier detection methods?  
A) ✓ Outliers cannot be well reconstructed from succinct representations.  
B) ✓ High reconstruction error indicates outliers.  
C) ✗ These methods apply to both numeric and categorical data.  
D) ✓ SVD is used for numeric data.

**Correct:** A, B, D


#### 12. Which of the following are true about the Local Outlier Factor (LOF) method?  
A) ✓ LOF compares local density to neighbors.  
B) ✓ Lower local density than neighbors indicates outlierness.  
C) ✗ LOF is a local, not global, outlier detection method.  
D) ✓ Reachability distance smooths density estimation.

**Correct:** A, B, D


#### 13. In high-dimensional data, why does distance-based outlier detection become challenging?  
A) ✓ Sparsity makes distances less meaningful.  
B) ✓ Number of subspaces grows exponentially.  
C) ✓ Noise dominates distance calculations.  
D) ✗ Outliers do not become easier to detect; usually harder.

**Correct:** A, B, C


#### 14. Which of the following statements about one-class classification models for outlier detection are correct?  
A) ✓ They model only normal data and detect deviations as outliers.  
B) ✗ They do not require labeled outlier examples.  
C) ✓ They can detect new types of outliers.  
D) ✗ They can handle multiple normal classes via extensions.

**Correct:** A, C


#### 15. When using the boxplot method for outlier detection, which of the following are true?  
A) ✓ Outliers lie outside Q1 - 1.5×IQR or Q3 + 1.5×IQR.  
B) ✓ IQR = Q3 - Q1.  
C) ✗ Boxplot does not assume normal distribution.  
D) ✓ The method identifies about 99.3% as non-outliers.

**Correct:** A, B, D


#### 16. Which of the following are challenges specific to contextual outlier detection?  
A) ✓ Defining meaningful contexts is challenging.  
B) ✓ Contextual detection can be transformed into conventional detection once context is identified.  
C) ✗ Behavioral attributes are essential, not ignored.  
D) ✓ Ambiguous or overlapping contexts complicate detection.

**Correct:** A, B, D


#### 17. In distance-based outlier detection, what does it mean if an object is a DB(p, D)-outlier?  
A) ✓ At least fraction p of objects lie farther than D from it.  
B) ✗ This is the opposite of the definition.  
C) ✓ Increasing D makes the object more outlying.  
D) ✗ Increasing p makes the object more outlying, not less.

**Correct:** A, C


#### 18. Which of the following statements about semi-supervised outlier detection methods are true?  
A) ✓ They use labeled normal data to model normal behavior.  
B) ✓ Labeled outliers help but may be insufficient if rare.  
C) ✗ They rely on both labeled and unlabeled data.  
D) ✓ They combine clustering and classification.

**Correct:** A, B, D


#### 19. Why might proximity-based methods fail to detect certain outliers?  
A) ✓ They struggle with outliers close to each other (collective outliers).  
B) ✗ Perfect distance metrics are often unavailable.  
C) ✗ They do not always detect all global outliers.  
D) ✓ They struggle when normal data is not clustered.

**Correct:** A, D


#### 20. Which of the following are true about the Mahalanobis distance in multivariate outlier detection?  
A) ✓ It accounts for correlations between variables.  
B) ✓ It uses the covariance matrix.  
C) ✗ It does not treat dimensions independently.  
D) ✓ Larger distance indicates more outlying.

**Correct:** A, B, D