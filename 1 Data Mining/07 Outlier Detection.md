## 7 Outlier Detection

[Study Notes](#study-notes)

[Questions](#questions)



### Key Points

#### 1. 🌟 Outlier Types  
- There are three types of outliers: global (point anomalies), contextual, and collective outliers.  
- A global outlier significantly deviates from the entire dataset.  
- A contextual outlier deviates significantly within a specific context defined by contextual attributes.  
- A collective outlier is a group of data points that collectively deviate, even if individual points are not outliers.

#### 2. ⚠️ Outliers vs Noise  
- Noise is random error or variance in data measurement.  
- Outliers violate the normal data generation mechanism and are often meaningful.  
- Outlier detection differs from novelty detection, where novelties may later become normal.

#### 3. 🛠️ Outlier Detection Methods  
- Methods are categorized as supervised, semi-supervised, and unsupervised based on availability of labeled data.  
- Statistical, proximity-based, clustering-based, classification-based, and reconstruction-based methods are common approaches.  
- Supervised methods treat outlier detection as classification but face class imbalance challenges.  
- Unsupervised methods assume normal data forms clusters; outliers lie far from clusters.  
- Semi-supervised methods use limited labeled data combined with unlabeled data to improve detection.

#### 4. 📈 Statistical Methods  
- Assume normal data follows a statistical model; points not fitting the model are outliers.  
- Parametric methods assume a known distribution with fixed parameters; non-parametric methods estimate the model from data.  
- Univariate outliers can be detected using the normal distribution and the 3σ rule (99.7% data within μ ± 3σ).  
- Boxplot method defines outliers as points outside Q1 - 1.5×IQR or Q3 + 1.5×IQR.  
- Grubb’s test uses z-scores and t-distribution to identify outliers statistically.

#### 5. 📏 Proximity-Based Methods  
- Distance-based outliers are points with a large fraction of other points farther than a threshold distance.  
- Density-based outliers have significantly lower local density compared to neighbors.  
- k-distance is the distance to the k-th nearest neighbor.  
- Reachability distance adjusts distance to handle varying densities.  
- Local Outlier Factor (LOF) measures how isolated a point is compared to its neighbors.

#### 6. 🧮 Reconstruction-Based Methods  
- Normal data can be succinctly represented and reconstructed; poor reconstruction indicates outliers.  
- Matrix factorization (e.g., SVD) is used for numeric data.  
- Pattern-based compression is used for categorical data.

#### 7. 🧩 Clustering and Classification-Based Detection  
- Outliers do not belong to any cluster, belong to small/sparse clusters, or are far from cluster centers.  
- Classification-based methods train models to distinguish normal and outlier data.  
- One-class models learn only normal data boundaries; points outside are outliers.

#### 8. 🌍 Contextual Outliers  
- Contextual outliers depend on contextual attributes (e.g., time, location).  
- Detection involves grouping data by context and applying conventional outlier detection within groups.  
- Behavioral attributes are used to evaluate outlierness within the context.

#### 9. 🌐 Collective Outliers  
- Collective outliers are groups of data points that deviate together.  
- Detection requires understanding relationships or structures among data points.

#### 10. 📊 High-Dimensional Outlier Detection  
- High-dimensional data is sparse, making distance measures less effective.  
- Outliers may only appear in certain subspaces.  
- HilOut uses rank-based distances instead of absolute distances for better detection in high dimensions.



<br>

## Study Notes

### 1. 🌟 Introduction to Outlier Detection

Outlier detection is a crucial task in data mining and analysis that involves identifying data points that are significantly different from the majority of the data. These unusual points, called **outliers**, can reveal important insights or anomalies such as fraud, errors, or rare events.

For example, in 2017, scientists observed an object named ‘Oumuamua that originated from outside our Solar System — a true outlier in astronomical data. Similarly, in fraud detection, unusual credit card transactions in terms of amount, location, or timing can indicate fraudulent activity.

Outlier detection is important because outliers often represent **signals** rather than just noise. They can indicate fraud, system failures, or novel phenomena that require attention.


### 2. 🔍 Understanding Outliers and Noise

It’s important to distinguish **outliers** from **noise**:

- **Noise** refers to random errors or small variations in data measurement that do not carry meaningful information.
- **Outliers** are data points that violate the normal data generation process and are often interesting or important to detect.

Outlier detection is different from **novelty detection**. Novelty detection focuses on identifying new patterns that were not seen before but may later become part of the normal data model.


### 3. 🧩 Types of Outliers

Outliers can be categorized into three main types:

#### 3.1 Global Outliers (Point Anomalies)
A **global outlier** is a single data point that is very different from all other data points in the dataset. For example, a temperature reading of 10°C in a tropical city might be a global outlier.

The challenge here is to define a good measure of how much a point deviates from the rest.

#### 3.2 Contextual Outliers
A **contextual outlier** is a data point that is unusual only within a specific context. For example, 10°C in Vancouver might be normal in winter but an outlier in summer.

To detect contextual outliers, data attributes are divided into:
- **Contextual attributes**: define the context (e.g., time, location).
- **Behavioral attributes**: describe the object’s characteristics (e.g., temperature).

The challenge is to define meaningful contexts to evaluate outliers properly.

#### 3.3 Collective Outliers
A **collective outlier** is a group of data points that together deviate significantly from the norm, even if individual points are not outliers. For example, a group of computers sending denial-of-service attacks collectively form an outlier pattern.

Detecting collective outliers requires understanding relationships among data points, such as similarity or distance.


### 4. ⚠️ Challenges in Outlier Detection

Outlier detection faces several challenges:

- **Modeling normal vs. outlier behavior**: It’s hard to define all normal behaviors, and the boundary between normal and outlier is often fuzzy.
- **Application-specific definitions**: What counts as an outlier in one domain (e.g., healthcare) may not be the same in another (e.g., marketing).
- **Handling noise**: Noise can obscure the distinction between normal data and outliers.
- **Interpretability**: It’s important to explain why a data point is considered an outlier and quantify how unusual it is.


### 5. 🛠️ Methods for Outlier Detection

Outlier detection methods can be broadly classified based on whether labeled data is available and the assumptions about data:

#### 5.1 Supervised Methods
- Treat outlier detection as a classification problem.
- Use labeled examples of normal and outlier data to train models.
- Challenges include class imbalance (outliers are rare) and prioritizing recall (catching as many outliers as possible).

#### 5.2 Unsupervised Methods
- Assume normal data forms clusters; outliers lie far from these clusters.
- No labeled data is needed.
- Weakness: cannot detect collective outliers well.
- Many clustering algorithms can be adapted for this.

#### 5.3 Semi-Supervised Methods
- Use a small amount of labeled data (normal or outliers) combined with unlabeled data.
- Often model normal data and flag deviations as outliers.
- Can combine supervised and unsupervised approaches for better detection.


### 6. 📈 Statistical and Model-Based Methods

These methods assume normal data follows a statistical model, and points that don’t fit are outliers.

- **Parametric methods** assume data follows a known distribution (e.g., normal distribution) with fixed parameters.
- **Non-parametric methods** do not assume a fixed distribution but estimate the model from data (e.g., histograms, kernel density estimation).

#### Example: Univariate Outlier Detection Using Normal Distribution
- Suppose we have temperature data for a city.
- We estimate the mean (μ) and standard deviation (σ) assuming normality.
- Any value more than 3σ away from μ is considered an outlier (because 99.7% of data lies within μ ± 3σ).
- For example, a temperature of 24°C might be 4.61°C away from the mean, making it an outlier.

#### Boxplot Method
- Uses five-number summary: min, Q1, median, Q3, max.
- Defines outliers as points outside Q1 - 1.5×IQR or Q3 + 1.5×IQR, where IQR = Q3 - Q1.

#### Grubb’s Test
- Uses z-scores and t-distribution to statistically test if a point is an outlier.


### 7. 📏 Proximity-Based Outlier Detection

These methods rely on the idea that outliers are far from other points.

- **Distance-based outliers**: A point is an outlier if a large fraction of points are farther than a threshold distance.
- **Density-based outliers**: A point is an outlier if its local density is much lower than that of its neighbors.

Key concepts:
- **k-distance**: distance to the k-th nearest neighbor.
- **Reachability distance**: adjusts distance to avoid issues with varying densities.
- **Local Reachability Density (LRD)**: inverse of average reachability distance to neighbors.
- **Local Outlier Factor (LOF)**: compares LRD of a point to its neighbors to quantify outlierness.


### 8. 🧮 Reconstruction-Based Methods

These methods assume normal data can be represented or compressed succinctly, and outliers cannot be well reconstructed.

- For numeric data, matrix factorization techniques like Singular Value Decomposition (SVD) are used.
- For categorical data, pattern-based compression methods are applied.

Poor reconstruction quality indicates an outlier.


### 9. 🧩 Clustering and Classification-Based Outlier Detection

- **Clustering-based**: Outliers are points that do not belong to any cluster, belong to small clusters, or are far from cluster centers.
- **Classification-based**: Train a classifier to distinguish normal vs. outlier data.
- **One-class models**: Train only on normal data to learn its boundary; points outside are outliers. Useful for detecting new, unseen outliers.


### 10. 🌍 Contextual and Collective Outlier Detection

#### Contextual Outliers
- Outliers depend on context (e.g., time, location).
- Detect by grouping data by context and applying conventional outlier detection within each group.
- Example: Detecting unusual customer behavior within age groups or postal codes.

#### Collective Outliers
- Groups of data points collectively deviate.
- Requires understanding relationships and structures among data points.
- Example: Detecting coordinated cyber-attacks.


### 11. 📊 Outlier Detection in High-Dimensional Data

High-dimensional data presents unique challenges:

- Data becomes sparse, making distance measures less meaningful.
- Outliers may only appear in certain subspaces.
- The number of subspaces grows exponentially, making detection computationally expensive.

Methods like **HilOut** use rank-based distances instead of absolute distances to improve detection in high dimensions.


### 12. 📝 Summary

Outlier detection is a broad field with many applications, including fraud detection, healthcare, and network security. Key takeaways:

- Outliers can be global, contextual, or collective.
- Methods include statistical, proximity-based, clustering, classification, and reconstruction-based.
- Context and relationships among data points are crucial for effective detection.
- High-dimensional data requires specialized techniques.

Understanding the nature of your data and the context of outliers is essential for choosing the right detection method.



<br>

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