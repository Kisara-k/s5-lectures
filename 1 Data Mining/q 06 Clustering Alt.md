## 6. Clustering Alt

## Questions

#### 1. What are the essential characteristics of a good clustering result?  
A) High intra-cluster similarity and low inter-cluster similarity  
B) Clusters must be of equal size  
C) Clusters should be non-overlapping and exclusive  
D) Clusters should be well separated and cohesive  

#### 2. Which of the following statements about k-means clustering are true?  
A) It requires the number of clusters k to be specified in advance  
B) It can handle categorical data without modification  
C) It is sensitive to outliers and noise  
D) It always finds the global optimal clustering  

#### 3. In hierarchical clustering, what is the main difference between agglomerative and divisive methods?  
A) Agglomerative starts with one cluster and splits it; divisive starts with individual points and merges them  
B) Agglomerative starts with individual points and merges them; divisive starts with one cluster and splits it  
C) Both require the number of clusters k as input  
D) Both produce a dendrogram representing nested clusters  

#### 4. Which distance measures can be used to define the distance between two clusters in hierarchical clustering?  
A) Single link (minimum distance between points)  
B) Complete link (maximum distance between points)  
C) Average link (average distance between points)  
D) Manhattan distance between cluster centroids  

#### 5. What are the main challenges when clustering high-dimensional data?  
A) Curse of dimensionality causing distance measures to lose meaning  
B) Scalability issues due to exponential growth of data points  
C) Difficulty in identifying meaningful subspaces for clustering  
D) High dimensionality always improves clustering quality  

#### 6. Which of the following are true about density-based clustering methods like DBSCAN?  
A) They can find clusters of arbitrary shape  
B) They require the number of clusters k as input  
C) They can identify noise points as outliers  
D) They are insensitive to the choice of parameters Eps and MinPts  

#### 7. In DBSCAN, what defines a core point?  
A) A point with at least MinPts neighbors within radius Eps  
B) A point that lies on the boundary of a cluster  
C) A point with fewer than MinPts neighbors within radius Eps  
D) A point that is density-reachable from another core point  

#### 8. Which statements about the k-medoids algorithm (PAM) are correct?  
A) It uses actual data points as cluster centers  
B) It is more robust to noise and outliers than k-means  
C) It scales well to very large datasets without modification  
D) It always produces spherical clusters  

#### 9. What is the role of the Clustering Feature (CF) vector in the BIRCH algorithm?  
A) To store summary statistics of subclusters for efficient clustering  
B) To represent the medoid of each cluster  
C) To calculate the exact distance between all pairs of points  
D) To incrementally update clusters as new data arrives  

#### 10. Which of the following are advantages of grid-based clustering methods like STING?  
A) They are query-independent and easy to parallelize  
B) They can detect clusters with diagonal boundaries accurately  
C) They scale well with the size of the dataset  
D) They require multiple scans of the data  

#### 11. What is a key limitation of the k-means clustering algorithm?  
A) It can only handle numerical data  
B) It is insensitive to the initial choice of centroids  
C) It can discover clusters with arbitrary shapes  
D) It does not require the number of clusters to be specified  

#### 12. Which of the following statements about the Hopkins statistic are true?  
A) It measures the tendency of data to form clusters  
B) A value close to 0.5 indicates strong clustering tendency  
C) It compares distances between random points and nearest neighbors in the dataset  
D) It can be used to test if data is uniformly distributed  

#### 13. In hierarchical clustering, what is the effect of using single-link versus complete-link methods?  
A) Single-link tends to produce elongated, chain-like clusters  
B) Complete-link tends to produce compact, spherical clusters  
C) Single-link is less sensitive to noise than complete-link  
D) Complete-link always merges clusters with the smallest minimum distance  

#### 14. Which of the following are true about the CHAMELEON clustering algorithm?  
A) It uses a dynamic model to measure cluster similarity  
B) It merges clusters based solely on centroid distances  
C) It first partitions data into many small sub-clusters before merging  
D) It is a purely density-based clustering method  

#### 15. What is the main difference between intrinsic and extrinsic clustering evaluation methods?  
A) Intrinsic methods require ground truth labels  
B) Extrinsic methods evaluate clustering quality without ground truth  
C) Intrinsic methods assess cluster compactness and separation  
D) Extrinsic methods compare clustering results to known class labels  

#### 16. Which of the following statements about OPTICS are correct?  
A) It produces a cluster ordering that reveals clustering structure at multiple density levels  
B) It requires the number of clusters k as input  
C) It can handle varying density clusters better than DBSCAN  
D) It is less computationally efficient than DBSCAN for large datasets  

#### 17. What is the main purpose of the Apriori principle in the CLIQUE algorithm?  
A) To identify dense units in high-dimensional subspaces efficiently  
B) To prune subspaces that cannot contain clusters  
C) To merge clusters based on density connectivity  
D) To calculate the centroid of clusters in subspaces  

#### 18. Which of the following are true about probabilistic hierarchical clustering?  
A) It uses generative models to measure cluster similarity  
B) It can handle missing attribute values better than algorithmic methods  
C) It always produces the same clustering regardless of initialization  
D) It assumes clusters are generated from known probability distributions  

#### 19. Which of the following statements about outliers in clustering are true?  
A) Outliers are points far away from any cluster  
B) K-means is robust to outliers due to centroid averaging  
C) Density-based methods can explicitly identify noise points as outliers  
D) Outliers always form their own clusters in hierarchical clustering  

#### 20. When using k-means, which strategies can improve the quality of clustering?  
A) Using multiple random initializations and choosing the best result  
B) Applying k-modes for categorical data instead of k-means  
C) Increasing k arbitrarily to reduce within-cluster variance  
D) Normalizing data to ensure all features contribute equally



<br>

## Answers

#### 1. What are the essential characteristics of a good clustering result?  
A) ✓ High intra-cluster similarity and low inter-cluster similarity — This is the fundamental definition of good clustering.  
B) ✗ Clusters must be of equal size — Cluster sizes can vary; equal size is not required.  
C) ✗ Clusters should be non-overlapping and exclusive — Not always; some methods allow overlapping clusters.  
D) ✓ Clusters should be well separated and cohesive — Cohesion and separation are key quality criteria.  

**Correct:** A, D


#### 2. Which of the following statements about k-means clustering are true?  
A) ✓ It requires the number of clusters k to be specified in advance — k-means needs k as input.  
B) ✗ It can handle categorical data without modification — k-means only works on numerical data; k-modes is for categorical.  
C) ✓ It is sensitive to outliers and noise — Outliers can distort centroids significantly.  
D) ✗ It always finds the global optimal clustering — k-means often converges to local optima.  

**Correct:** A, C


#### 3. In hierarchical clustering, what is the main difference between agglomerative and divisive methods?  
A) ✗ Agglomerative starts with one cluster and splits it; divisive starts with individual points and merges them — This is reversed.  
B) ✓ Agglomerative starts with individual points and merges them; divisive starts with one cluster and splits it — Correct definitions.  
C) ✗ Both require the number of clusters k as input — Hierarchical methods do not require k upfront.  
D) ✓ Both produce a dendrogram representing nested clusters — Dendrograms are a key output of hierarchical clustering.  

**Correct:** B, D


#### 4. Which distance measures can be used to define the distance between two clusters in hierarchical clustering?  
A) ✓ Single link (minimum distance between points) — Common linkage method.  
B) ✓ Complete link (maximum distance between points) — Another standard linkage.  
C) ✓ Average link (average distance between points) — Also widely used.  
D) ✗ Manhattan distance between cluster centroids — Manhattan distance is a point-to-point metric, not typically used between centroids in hierarchical clustering.  

**Correct:** A, B, C


#### 5. What are the main challenges when clustering high-dimensional data?  
A) ✓ Curse of dimensionality causing distance measures to lose meaning — Distances become less meaningful in high dimensions.  
B) ✗ Scalability issues due to exponential growth of data points — Data points don’t grow exponentially, but complexity can increase.  
C) ✓ Difficulty in identifying meaningful subspaces for clustering — Subspace clustering is often needed.  
D) ✗ High dimensionality always improves clustering quality — Usually it degrades quality due to noise and irrelevant features.  

**Correct:** A, C


#### 6. Which of the following are true about density-based clustering methods like DBSCAN?  
A) ✓ They can find clusters of arbitrary shape — A key advantage of density-based methods.  
B) ✗ They require the number of clusters k as input — DBSCAN does not require k.  
C) ✓ They can identify noise points as outliers — Noise points are explicitly identified.  
D) ✗ They are insensitive to the choice of parameters Eps and MinPts — Parameter choice is critical and affects results.  

**Correct:** A, C


#### 7. In DBSCAN, what defines a core point?  
A) ✓ A point with at least MinPts neighbors within radius Eps — This is the definition of a core point.  
B) ✗ A point that lies on the boundary of a cluster — Boundary points are border points, not core points.  
C) ✗ A point with fewer than MinPts neighbors within radius Eps — Such points are not core points.  
D) ✗ A point that is density-reachable from another core point — Density-reachable points can be core or border, but this is not the definition of a core point.  

**Correct:** A


#### 8. Which statements about the k-medoids algorithm (PAM) are correct?  
A) ✓ It uses actual data points as cluster centers — Medoids are actual objects, unlike centroids.  
B) ✓ It is more robust to noise and outliers than k-means — Medoids reduce influence of outliers.  
C) ✗ It scales well to very large datasets without modification — PAM is computationally expensive for large data.  
D) ✗ It always produces spherical clusters — Like k-means, it does not guarantee cluster shape.  

**Correct:** A, B


#### 9. What is the role of the Clustering Feature (CF) vector in the BIRCH algorithm?  
A) ✓ To store summary statistics of subclusters for efficient clustering — CF summarizes cluster info (N, LS, SS).  
B) ✗ To represent the medoid of each cluster — CF is a statistical summary, not a medoid.  
C) ✗ To calculate the exact distance between all pairs of points — CF avoids pairwise distance calculations.  
D) ✓ To incrementally update clusters as new data arrives — BIRCH incrementally updates CF-tree.  

**Correct:** A, D


#### 10. Which of the following are advantages of grid-based clustering methods like STING?  
A) ✓ They are query-independent and easy to parallelize — Grid structure supports this.  
B) ✗ They can detect clusters with diagonal boundaries accurately — Boundaries are axis-aligned, no diagonal detection.  
C) ✓ They scale well with the size of the dataset — Grid-based methods are efficient.  
D) ✗ They require multiple scans of the data — STING typically uses a single scan.  

**Correct:** A, C


#### 11. What is a key limitation of the k-means clustering algorithm?  
A) ✓ It can only handle numerical data — k-means uses means, which require numeric attributes.  
B) ✗ It is insensitive to the initial choice of centroids — Initialization affects results strongly.  
C) ✗ It can discover clusters with arbitrary shapes — k-means assumes spherical clusters.  
D) ✗ It does not require the number of clusters to be specified — k must be given.  

**Correct:** A


#### 12. Which of the following statements about the Hopkins statistic are true?  
A) ✓ It measures the tendency of data to form clusters — It tests spatial randomness.  
B) ✗ A value close to 0.5 indicates strong clustering tendency — 0.5 indicates randomness, near 0 indicates clustering.  
C) ✓ It compares distances between random points and nearest neighbors in the dataset — This is how it works.  
D) ✓ It can be used to test if data is uniformly distributed — It tests uniformity vs clustering.  

**Correct:** A, C, D


#### 13. In hierarchical clustering, what is the effect of using single-link versus complete-link methods?  
A) ✓ Single-link tends to produce elongated, chain-like clusters — Known as chaining effect.  
B) ✓ Complete-link tends to produce compact, spherical clusters — It merges based on maximum distance.  
C) ✗ Single-link is less sensitive to noise than complete-link — Single-link is more sensitive to noise.  
D) ✗ Complete-link always merges clusters with the smallest minimum distance — It merges based on maximum distance, not minimum.  

**Correct:** A, B


#### 14. Which of the following are true about the CHAMELEON clustering algorithm?  
A) ✓ It uses a dynamic model to measure cluster similarity — It considers relative interconnectivity and closeness.  
B) ✗ It merges clusters based solely on centroid distances — It uses graph-based measures, not just centroids.  
C) ✓ It first partitions data into many small sub-clusters before merging — Two-phase approach.  
D) ✗ It is a purely density-based clustering method — It is hierarchical and graph-based, not purely density-based.  

**Correct:** A, C


#### 15. What is the main difference between intrinsic and extrinsic clustering evaluation methods?  
A) ✗ Intrinsic methods require ground truth labels — Intrinsic methods do not use ground truth.  
B) ✗ Extrinsic methods evaluate clustering quality without ground truth — Extrinsic methods require ground truth.  
C) ✓ Intrinsic methods assess cluster compactness and separation — They use internal criteria.  
D) ✓ Extrinsic methods compare clustering results to known class labels — They use external labels for evaluation.  

**Correct:** C, D


#### 16. Which of the following statements about OPTICS are correct?  
A) ✓ It produces a cluster ordering that reveals clustering structure at multiple density levels — Key feature of OPTICS.  
B) ✗ It requires the number of clusters k as input — OPTICS does not require k.  
C) ✓ It can handle varying density clusters better than DBSCAN — OPTICS handles varying densities well.  
D) ✗ It is less computationally efficient than DBSCAN for large datasets — OPTICS is generally more complex but often efficient with indexing.  

**Correct:** A, C


#### 17. What is the main purpose of the Apriori principle in the CLIQUE algorithm?  
A) ✓ To identify dense units in high-dimensional subspaces efficiently — Apriori prunes subspaces.  
B) ✓ To prune subspaces that cannot contain clusters — Reduces search space.  
C) ✗ To merge clusters based on density connectivity — CLIQUE merges based on connected dense units, not Apriori.  
D) ✗ To calculate the centroid of clusters in subspaces — Apriori is unrelated to centroid calculation.  

**Correct:** A, B


#### 18. Which of the following are true about probabilistic hierarchical clustering?  
A) ✓ It uses generative models to measure cluster similarity — Based on likelihood models.  
B) ✓ It can handle missing attribute values better than algorithmic methods — Probabilistic models can handle partial data.  
C) ✗ It always produces the same clustering regardless of initialization — Probabilistic methods can be sensitive to initialization.  
D) ✓ It assumes clusters are generated from known probability distributions — Uses assumed distributions like Gaussian.  

**Correct:** A, B, D


#### 19. Which of the following statements about outliers in clustering are true?  
A) ✓ Outliers are points far away from any cluster — Common definition of outliers.  
B) ✗ K-means is robust to outliers due to centroid averaging — K-means is sensitive to outliers.  
C) ✓ Density-based methods can explicitly identify noise points as outliers — DBSCAN and others identify noise.  
D) ✗ Outliers always form their own clusters in hierarchical clustering — Outliers may remain singletons or be merged depending on method.  

**Correct:** A, C


#### 20. When using k-means, which strategies can improve the quality of clustering?  
A) ✓ Using multiple random initializations and choosing the best result — Helps avoid poor local minima.  
B) ✓ Applying k-modes for categorical data instead of k-means — k-modes is designed for categorical data.  
C) ✗ Increasing k arbitrarily to reduce within-cluster variance — Increasing k reduces variance but may overfit and is not always better.  
D) ✓ Normalizing data to ensure all features contribute equally — Prevents dominance of features with large scales.  

**Correct:** A, B, D