## 5. Clustering I

## Questions

#### 1. What defines a good clustering result?  
A) High similarity between clusters  
B) High intra-cluster similarity  
C) Low inter-cluster similarity  
D) Clusters with equal number of points  

#### 2. Which of the following are true about clustering as an unsupervised learning method?  
A) It requires predefined class labels  
B) It discovers patterns based on data similarity  
C) It can be used as a preprocessing step for classification  
D) It always produces hierarchical clusters  

#### 3. Which distance measures are appropriate for clustering categorical data?  
A) Euclidean distance  
B) Hamming distance  
C) Jaccard coefficient  
D) Manhattan distance  

#### 4. What are the main challenges in clustering high-dimensional data?  
A) Curse of dimensionality affecting distance measures  
B) Increased interpretability of clusters  
C) Difficulty in finding meaningful subspaces  
D) Scalability issues with large datasets  

#### 5. Which statements about the k-means algorithm are correct?  
A) It always finds the global optimum clustering  
B) It requires the number of clusters $k$ to be specified in advance  
C) It is sensitive to outliers and noise  
D) It can handle categorical data without modification  

#### 6. How does the k-medoids algorithm differ from k-means?  
A) It uses actual data points as cluster centers  
B) It is less sensitive to outliers  
C) It requires continuous numerical data only  
D) It is computationally more expensive than k-means  

#### 7. Which of the following are true about hierarchical clustering?  
A) It requires the number of clusters $k$ as input  
B) It produces a dendrogram representing nested clusters  
C) Agglomerative clustering starts with each object as a separate cluster  
D) Divisive clustering merges clusters iteratively  

#### 8. In hierarchical clustering, what does the single-link method measure?  
A) Maximum distance between points in two clusters  
B) Minimum distance between points in two clusters  
C) Average distance between points in two clusters  
D) Distance between cluster centroids  

#### 9. What are the limitations of agglomerative hierarchical clustering?  
A) It cannot undo previous merges  
B) It scales well to very large datasets  
C) It is sensitive to noise and outliers  
D) It requires specifying $k$ upfront  

#### 10. Which of the following statements about BIRCH are true?  
A) It incrementally builds a CF-tree summarizing the data  
B) It can handle categorical and numerical data equally well  
C) It is sensitive to the order of data insertion  
D) It requires multiple passes over the data  

#### 11. What does the Clustering Feature (CF) vector in BIRCH contain?  
A) Number of points in the cluster  
B) Linear sum of points  
C) Square sum of points  
D) Distance between cluster centroids  

#### 12. Which of the following are characteristics of the CHAMELEON clustering algorithm?  
A) Uses a dynamic model to measure cluster similarity  
B) Merges clusters based solely on centroid distance  
C) Uses graph partitioning to create initial sub-clusters  
D) Can discover clusters with arbitrary shapes  

#### 13. Why is k-means not suitable for discovering clusters with non-convex shapes?  
A) It uses medoids as cluster centers  
B) It assumes clusters are spherical and convex  
C) It uses a distance metric that ignores shape  
D) It cannot handle categorical data  

#### 14. Which of the following are true about outlier detection in clustering?  
A) Outliers are points far from any cluster  
B) K-means is robust to outliers  
C) Density-based methods are often better at detecting outliers  
D) Outliers always form their own clusters  

#### 15. What are the advantages of using k-modes or k-prototypes over k-means?  
A) They can handle categorical data  
B) They replace means with modes for cluster centers  
C) They require fewer iterations to converge  
D) They can handle mixed numerical and categorical data  

#### 16. Which of the following are true about similarity/distance measures in clustering?  
A) Euclidean distance is suitable for interval-scaled data  
B) Boolean data requires specialized distance functions  
C) Weights can be assigned to variables based on domain knowledge  
D) Distance functions are always symmetric  

#### 17. What is a key difference between partitioning and hierarchical clustering methods?  
A) Partitioning methods produce nested clusters  
B) Hierarchical methods do not require specifying the number of clusters upfront  
C) Partitioning methods are always more computationally expensive  
D) Hierarchical methods can be agglomerative or divisive  

#### 18. Which of the following statements about cluster evaluation are correct?  
A) Cluster quality is always objectively measurable  
B) Quality depends on the similarity measure used  
C) High intra-cluster similarity alone guarantees good clustering  
D) Subjectivity often plays a role in defining “good enough” clusters  

#### 19. Which of the following are true about constraint-based clustering?  
A) It allows user input to guide clustering  
B) It ignores domain knowledge  
C) It can incorporate obstacles or must-link/cannot-link constraints  
D) It is a type of density-based clustering  

#### 20. What are the main reasons for using clustering as a preprocessing step?  
A) To reduce data dimensionality directly  
B) To summarize data before applying classification or regression  
C) To compress data for storage or transmission  
D) To find the exact number of clusters in the data



<br>

## Answers

#### 1. What defines a good clustering result?  
A) ✗ High similarity between clusters — Clusters should be dissimilar, not similar.  
B) ✓ High intra-cluster similarity — Objects within the same cluster should be similar.  
C) ✓ Low inter-cluster similarity — Clusters should be well separated and distinct.  
D) ✗ Clusters with equal number of points — Cluster size equality is not required for good clustering.  

**Correct:** B, C


#### 2. Which of the following are true about clustering as an unsupervised learning method?  
A) ✗ It requires predefined class labels — Clustering is unsupervised, so no labels are needed.  
B) ✓ It discovers patterns based on data similarity — Clustering groups data by similarity.  
C) ✓ It can be used as a preprocessing step for classification — Clustering can help prepare data.  
D) ✗ It always produces hierarchical clusters — Clustering can be partitioning or hierarchical.  

**Correct:** B, C


#### 3. Which distance measures are appropriate for clustering categorical data?  
A) ✗ Euclidean distance — Suitable for numerical data, not categorical.  
B) ✓ Hamming distance — Measures difference between categorical attributes.  
C) ✓ Jaccard coefficient — Used for binary/categorical similarity.  
D) ✗ Manhattan distance — Like Euclidean, for numerical data.  

**Correct:** B, C


#### 4. What are the main challenges in clustering high-dimensional data?  
A) ✓ Curse of dimensionality affecting distance measures — Distances become less meaningful.  
B) ✗ Increased interpretability of clusters — High dimensions usually reduce interpretability.  
C) ✓ Difficulty in finding meaningful subspaces — Clusters may exist only in subspaces.  
D) ✓ Scalability issues with large datasets — More dimensions increase computational cost.  

**Correct:** A, C, D


#### 5. Which statements about the k-means algorithm are correct?  
A) ✗ It always finds the global optimum clustering — K-means often converges to local optima.  
B) ✓ It requires the number of clusters $k$ to be specified in advance — $k$ must be given.  
C) ✓ It is sensitive to outliers and noise — Outliers can distort cluster centers.  
D) ✗ It can handle categorical data without modification — K-means only works on numerical data.  

**Correct:** B, C


#### 6. How does the k-medoids algorithm differ from k-means?  
A) ✓ It uses actual data points as cluster centers — Medoids are real objects, not means.  
B) ✓ It is less sensitive to outliers — Medoids reduce outlier influence.  
C) ✗ It requires continuous numerical data only — K-medoids can handle arbitrary distance metrics.  
D) ✓ It is computationally more expensive than k-means — More complex distance calculations.  

**Correct:** A, B, D


#### 7. Which of the following are true about hierarchical clustering?  
A) ✗ It requires the number of clusters $k$ as input — It does not require $k$ upfront.  
B) ✓ It produces a dendrogram representing nested clusters — Dendrogram shows cluster hierarchy.  
C) ✓ Agglomerative clustering starts with each object as a separate cluster — Bottom-up approach.  
D) ✗ Divisive clustering merges clusters iteratively — Divisive splits clusters top-down.  

**Correct:** B, C


#### 8. In hierarchical clustering, what does the single-link method measure?  
A) ✗ Maximum distance between points in two clusters — That’s complete-link.  
B) ✓ Minimum distance between points in two clusters — Single-link uses the closest points.  
C) ✗ Average distance between points in two clusters — That’s average-link.  
D) ✗ Distance between cluster centroids — That’s centroid-link.  

**Correct:** B


#### 9. What are the limitations of agglomerative hierarchical clustering?  
A) ✓ It cannot undo previous merges — Once merged, clusters cannot be split.  
B) ✗ It scales well to very large datasets — It has at least $O(n^2)$ complexity, so poor scalability.  
C) ✓ It is sensitive to noise and outliers — Noise can affect cluster merges.  
D) ✗ It requires specifying $k$ upfront — $k$ is chosen by cutting dendrogram after clustering.  

**Correct:** A, C


#### 10. Which of the following statements about BIRCH are true?  
A) ✓ It incrementally builds a CF-tree summarizing the data — CF-tree compresses data hierarchically.  
B) ✗ It can handle categorical and numerical data equally well — BIRCH only handles numerical data.  
C) ✓ It is sensitive to the order of data insertion — Insertion order affects CF-tree structure.  
D) ✗ It requires multiple passes over the data — Usually one pass plus a few refinements.  

**Correct:** A, C


#### 11. What does the Clustering Feature (CF) vector in BIRCH contain?  
A) ✓ Number of points in the cluster — $N$ is stored.  
B) ✓ Linear sum of points — $LS$ is stored.  
C) ✓ Square sum of points — $SS$ is stored.  
D) ✗ Distance between cluster centroids — Not part of CF vector.  

**Correct:** A, B, C


#### 12. Which of the following are characteristics of the CHAMELEON clustering algorithm?  
A) ✓ Uses a dynamic model to measure cluster similarity — Considers interconnectivity and closeness.  
B) ✗ Merges clusters based solely on centroid distance — Uses graph-based measures, not just centroids.  
C) ✓ Uses graph partitioning to create initial sub-clusters — First phase partitions graph.  
D) ✓ Can discover clusters with arbitrary shapes — Dynamic modeling allows flexible shapes.  

**Correct:** A, C, D


#### 13. Why is k-means not suitable for discovering clusters with non-convex shapes?  
A) ✗ It uses medoids as cluster centers — K-means uses means, not medoids.  
B) ✓ It assumes clusters are spherical and convex — K-means partitions space by Voronoi cells.  
C) ✗ It uses a distance metric that ignores shape — Distance metric is Euclidean, but shape assumption is key.  
D) ✗ It cannot handle categorical data — True but unrelated to shape issue.  

**Correct:** B


#### 14. Which of the following are true about outlier detection in clustering?  
A) ✓ Outliers are points far from any cluster — By definition, outliers lie away from clusters.  
B) ✗ K-means is robust to outliers — K-means is sensitive to outliers.  
C) ✓ Density-based methods are often better at detecting outliers — They identify low-density points.  
D) ✗ Outliers always form their own clusters — Outliers may be isolated or ignored, not necessarily clusters.  

**Correct:** A, C


#### 15. What are the advantages of using k-modes or k-prototypes over k-means?  
A) ✓ They can handle categorical data — K-modes replaces means with modes.  
B) ✓ They replace means with modes for cluster centers — Modes better represent categorical data.  
C) ✗ They require fewer iterations to converge — Not necessarily true; convergence depends on data.  
D) ✓ They can handle mixed numerical and categorical data — K-prototypes combines both types.  

**Correct:** A, B, D


#### 16. Which of the following are true about similarity/distance measures in clustering?  
A) ✓ Euclidean distance is suitable for interval-scaled data — Common for continuous numerical data.  
B) ✓ Boolean data requires specialized distance functions — Boolean attributes need tailored metrics.  
C) ✓ Weights can be assigned to variables based on domain knowledge — Weighting improves relevance.  
D) ✗ Distance functions are always symmetric — Some measures (e.g., asymmetric similarity) may not be symmetric.  

**Correct:** A, B, C


#### 17. What is a key difference between partitioning and hierarchical clustering methods?  
A) ✗ Partitioning methods produce nested clusters — Hierarchical methods produce nested clusters.  
B) ✓ Hierarchical methods do not require specifying the number of clusters upfront — Clusters can be chosen by cutting dendrogram.  
C) ✗ Partitioning methods are always more computationally expensive — Partitioning is usually more efficient.  
D) ✓ Hierarchical methods can be agglomerative or divisive — Both approaches exist.  

**Correct:** B, D


#### 18. Which of the following statements about cluster evaluation are correct?  
A) ✗ Cluster quality is always objectively measurable — Often subjective and application-dependent.  
B) ✓ Quality depends on the similarity measure used — Different measures affect cluster formation.  
C) ✗ High intra-cluster similarity alone guarantees good clustering — Inter-cluster separation is also needed.  
D) ✓ Subjectivity often plays a role in defining “good enough” clusters — Domain knowledge influences evaluation.  

**Correct:** B, D


#### 19. Which of the following are true about constraint-based clustering?  
A) ✓ It allows user input to guide clustering — Users can specify constraints.  
B) ✗ It ignores domain knowledge — It explicitly uses domain knowledge.  
C) ✓ It can incorporate obstacles or must-link/cannot-link constraints — Common constraints in practice.  
D) ✗ It is a type of density-based clustering — Constraint-based is a separate approach.  

**Correct:** A, C


#### 20. What are the main reasons for using clustering as a preprocessing step?  
A) ✗ To reduce data dimensionality directly — Clustering groups data but does not reduce dimensions.  
B) ✓ To summarize data before applying classification or regression — Clusters simplify data structure.  
C) ✓ To compress data for storage or transmission — Clusters can represent data compactly.  
D) ✗ To find the exact number of clusters in the data — Preprocessing is not for determining $k$.  

**Correct:** B, C