## 6 Clustering Alt

[Study Notes](#study-notes)

[Questions](#questions)



### Key Points

#### 1. 🧩 Cluster Analysis Basics
- A cluster is a collection of data objects similar within the same group and dissimilar to objects in other groups.
- Clustering is an unsupervised learning method with no predefined classes.
- Typical applications include biology (taxonomy), information retrieval (document clustering), marketing (customer segmentation), and earth sciences (earthquake epicenters).

#### 2. 📏 Quality of Clustering
- Good clustering has high intra-class similarity and low inter-class similarity.
- Quality depends on the similarity measure, implementation, and ability to discover hidden patterns.
- Similarity is often measured by distance functions, which vary by data type (numerical, categorical, ordinal).

#### 3. ⚙️ Clustering Considerations
- Partitioning can be single-level or hierarchical.
- Clusters can be exclusive (one object per cluster) or non-exclusive (objects can belong to multiple clusters).
- Similarity measures can be distance-based or connectivity-based.
- Clustering can be done in full space or subspaces (important for high-dimensional data).
- Challenges include scalability, handling mixed data types, noise, arbitrary shapes, and high dimensionality.

#### 4. 🧮 Major Clustering Approaches
- Partitioning methods: k-means, k-medoids, CLARANS.
- Hierarchical methods: AGNES (agglomerative), DIANA (divisive), BIRCH, CHAMELEON.
- Density-based methods: DBSCAN, OPTICS, DENCLUE.
- Grid-based methods: STING, WaveCluster, CLIQUE.
- Model-based methods: EM, SOM, COBWEB.
- Other methods: frequent pattern-based, user-guided, link-based clustering.

#### 5. 🔢 K-Means Clustering
- K-means partitions data into k clusters by minimizing sum of squared distances to cluster centroids.
- Steps: initialize clusters, compute centroids, assign points to nearest centroid, repeat until stable.
- Strengths: efficient (O(tkn)), simple.
- Weaknesses: sensitive to outliers, requires numeric data, assumes spherical clusters, needs k specified.

#### 6. 🔢 K-Medoids Clustering (PAM)
- Uses medoids (actual data points) instead of means as cluster centers.
- More robust to noise and outliers than k-means.
- PAM is computationally expensive; CLARA and CLARANS improve scalability.

#### 7. 🌲 Hierarchical Clustering
- Does not require k as input; builds a dendrogram.
- Agglomerative (AGNES): merges closest clusters iteratively.
- Divisive (DIANA): splits clusters recursively.
- Cluster distance measures: single link (min), complete link (max), average link, centroid, medoid.
- BIRCH uses CF-tree for scalable hierarchical clustering.
- CHAMELEON merges clusters based on relative interconnectivity and closeness.

#### 8. 🌐 Density-Based Clustering
- Uses parameters Eps (neighborhood radius) and MinPts (minimum points).
- Core point: has ≥ MinPts neighbors within Eps.
- DBSCAN defines clusters as maximal sets of density-connected points.
- Can find arbitrarily shaped clusters and handle noise.
- OPTICS produces cluster ordering for varying density clusters.
- DENCLUE uses statistical density functions and density attractors.

#### 9. 🗺️ Grid-Based Clustering
- Divides data space into grid cells at multiple resolutions.
- STING uses statistical info of cells and a top-down approach.
- CLIQUE partitions high-dimensional space into dense units and finds clusters in subspaces.
- CLIQUE scales well and automatically finds subspace clusters.

#### 10. 📊 Clustering Evaluation
- Hopkins statistic tests cluster tendency; values near 0 indicate clustering, near 0.5 indicate randomness.
- Number of clusters can be estimated by empirical rules (≈√n/2), elbow method, or cross-validation.
- Quality measures:
  - Extrinsic: compare clustering to ground truth (homogeneity, completeness).
  - Intrinsic: evaluate cluster compactness and separation (e.g., Silhouette coefficient).



<br>

## Study Notes

### 1. 🧩 What is Cluster Analysis?

Cluster analysis is a fundamental technique in data mining used to group a collection of data objects into clusters. A **cluster** is essentially a group of objects that are similar to each other but dissimilar to objects in other groups. The goal is to discover natural groupings in data without any prior knowledge of class labels, which makes clustering an example of **unsupervised learning**.

#### Key Ideas:
- **Similarity within clusters:** Objects in the same cluster should be very similar or related.
- **Dissimilarity between clusters:** Objects in different clusters should be quite different.
- **Unsupervised learning:** Unlike supervised learning where we have labeled data, clustering finds patterns purely based on the data itself.

#### Why do we cluster data?
- To **understand data distribution** and gain insights.
- As a **preprocessing step** for other data mining tasks like classification, regression, or outlier detection.

#### Applications of Clustering:
- **Biology:** Classifying living organisms into taxonomic groups.
- **Information retrieval:** Grouping similar documents.
- **Land use:** Identifying regions with similar land use patterns.
- **Marketing:** Segmenting customers for targeted campaigns.
- **City planning:** Grouping houses by type, value, or location.
- **Earthquake studies:** Clustering epicenters along fault lines.
- **Climate science:** Finding patterns in atmospheric data.
- **Economic research:** Market segmentation and analysis.


### 2. 📏 What Makes a Good Clustering?

A good clustering method produces clusters that are:

- **Cohesive (high intra-class similarity):** Objects within the same cluster are very similar.
- **Distinctive (low inter-class similarity):** Clusters are well separated from each other.

#### Measuring Quality:
- Clustering quality depends on the **similarity or distance measure** used (e.g., Euclidean distance for numerical data).
- Different data types (numerical, categorical, ordinal) require different distance functions.
- Weights can be assigned to variables based on their importance.
- Defining "good enough" clusters is subjective and depends on the application.


### 3. ⚙️ Considerations and Challenges in Clustering

When performing cluster analysis, several important factors and challenges arise:

- **Partitioning criteria:** Should the clustering be a single-level partition or hierarchical (multi-level)?
- **Cluster exclusivity:** Should clusters be exclusive (each object belongs to one cluster) or overlapping (objects can belong to multiple clusters)?
- **Similarity measure:** Distance-based (e.g., Euclidean) or connectivity-based (e.g., density)?
- **Clustering space:** Use the full feature space or subspaces (important in high-dimensional data).
- **Scalability:** Ability to cluster large datasets efficiently.
- **Data types:** Handling numerical, categorical, binary, or mixed data.
- **Constraints:** Incorporating user/domain knowledge as constraints.
- **Cluster shape:** Ability to find clusters of arbitrary shapes.
- **Noise and outliers:** Robustness to noisy data.
- **Incremental clustering:** Ability to update clusters as new data arrives.
- **High dimensionality:** Managing the curse of dimensionality.


### 4. 🧮 Major Clustering Approaches

Clustering algorithms can be broadly categorized into several types based on their methodology:

#### 4.1 Partitioning Methods
- Divide data into **k clusters** by optimizing a criterion (e.g., minimizing sum of squared errors).
- Examples:
  - **K-means:** Clusters represented by centroids (mean points).
  - **K-medoids (PAM):** Clusters represented by actual data points (medoids).
  - **CLARANS:** A randomized approach improving k-medoids.

#### 4.2 Hierarchical Methods
- Build a hierarchy of clusters either by:
  - **Agglomerative (bottom-up):** Start with each object as a cluster and merge clusters step-by-step.
  - **Divisive (top-down):** Start with one cluster and split it recursively.
- Produces a **dendrogram** (tree diagram) showing cluster merges/splits.
- Examples: AGNES (agglomerative), DIANA (divisive), BIRCH, CHAMELEON.

#### 4.3 Density-Based Methods
- Define clusters as dense regions separated by low-density areas.
- Can find clusters of arbitrary shape and handle noise.
- Examples:
  - **DBSCAN:** Clusters based on density reachability.
  - **OPTICS:** Orders points to reveal clustering structure.
  - **DENCLUE:** Uses statistical density functions.

#### 4.4 Grid-Based Methods
- Divide data space into a grid structure and perform clustering on grid cells.
- Efficient for large datasets.
- Examples:
  - **STING:** Uses statistical info in grid cells.
  - **WaveCluster:** Uses wavelet transforms.
  - **CLIQUE:** Combines grid and subspace clustering.

#### 4.5 Model-Based Methods
- Assume a model for each cluster and fit data to these models.
- Examples:
  - **EM (Expectation-Maximization):** Fits mixture models.
  - **SOM (Self-Organizing Maps):** Neural network-based.
  - **COBWEB:** Conceptual clustering.

#### 4.6 Other Approaches
- **Frequent pattern-based:** Clustering based on frequent itemsets.
- **User-guided/constraint-based:** Incorporate user constraints.
- **Link-based:** Use object linkage information (e.g., social networks).


### 5. 🔢 Partitioning Methods in Detail: K-Means and K-Medoids

#### K-Means Algorithm:
- Input: number of clusters k.
- Steps:
  1. Randomly partition data into k clusters.
  2. Compute centroids (mean points) of clusters.
  3. Assign each object to the nearest centroid.
  4. Repeat steps 2-3 until assignments stabilize.
- Strengths:
  - Efficient (linear in number of objects).
  - Simple to implement.
- Weaknesses:
  - Sensitive to initial centroids.
  - Only works with numerical data.
  - Sensitive to outliers.
  - Assumes spherical clusters.
  - Requires k to be specified in advance.

#### K-Medoids Algorithm (PAM):
- Similar to k-means but uses medoids (actual data points) instead of means.
- More robust to noise and outliers.
- Computationally more expensive.
- Variants like CLARA and CLARANS improve scalability.


### 6. 🌲 Hierarchical Clustering Methods

Hierarchical clustering builds a tree of clusters without needing to specify k upfront.

#### Agglomerative (AGNES):
- Start with each object as a cluster.
- Iteratively merge the two closest clusters.
- Distance between clusters can be defined in several ways:
  - Single link (minimum distance between points).
  - Complete link (maximum distance).
  - Average link (average distance).
  - Centroid or medoid distance.

#### Divisive (DIANA):
- Start with all objects in one cluster.
- Recursively split clusters until each object is alone.

#### Dendrogram:
- Visual representation of hierarchical clustering.
- Cutting the dendrogram at a certain level gives the final clusters.

#### Extensions:
- **BIRCH:** Builds a CF-tree to incrementally cluster large datasets efficiently.
- **CHAMELEON:** Uses dynamic modeling and graph partitioning to merge clusters based on relative interconnectivity and closeness.


### 7. 🌐 Density-Based Clustering

Density-based methods define clusters as areas of high point density separated by low-density regions.

#### Key Concepts:
- **Eps (ε):** Radius defining neighborhood.
- **MinPts:** Minimum points required to form a dense region.
- **Core point:** A point with at least MinPts neighbors within Eps.
- **Border point:** Not a core point but within Eps of a core point.
- **Noise point:** Neither core nor border.

#### DBSCAN Algorithm:
- Starts from an arbitrary point.
- Expands cluster by including all density-reachable points.
- Can find clusters of arbitrary shape and identify noise.
- Sensitive to parameter choice.

#### OPTICS:
- Produces an ordering of points reflecting density-based clustering structure.
- Can handle varying density clusters better than DBSCAN.

#### DENCLUE:
- Uses mathematical density functions (e.g., Gaussian kernels).
- Defines clusters by density attractors (local maxima).
- Efficient and robust to noise.


### 8. 🗺️ Grid-Based Clustering

Grid-based methods partition the data space into a grid and perform clustering on these cells.

#### STING:
- Divides space into rectangular cells at multiple resolutions.
- Stores statistical info (count, mean, variance) for each cell.
- Uses a top-down approach to find clusters.
- Efficient and easy to parallelize.
- Limitation: cluster boundaries are axis-aligned (no diagonal boundaries).

#### CLIQUE:
- Designed for high-dimensional data.
- Finds dense units (cells) in subspaces.
- Uses Apriori principle to identify subspaces with clusters.
- Automatically finds clusters in subspaces.
- Scales well but may lose accuracy for simplicity.


### 9. 📊 Evaluating Clustering Quality

Evaluating clustering results is crucial but challenging because clustering is unsupervised.

#### Assessing Cluster Tendency:
- Check if data has any cluster structure or is uniformly random.
- **Hopkins Statistic:** Measures spatial randomness; values near 0.5 indicate randomness, near 0 indicate clustering tendency.

#### Determining Number of Clusters:
- Empirical rule: roughly √(n/2) clusters for n points.
- **Elbow method:** Plot sum of squared errors vs. k and look for a "knee" point.
- **Cross-validation:** Split data, train on part, test on the rest, and evaluate fit.

#### Measuring Quality:
- **Extrinsic methods:** Use ground truth labels (if available) to measure homogeneity, completeness, and other criteria.
- **Intrinsic methods:** Use internal criteria like cluster compactness and separation (e.g., Silhouette coefficient).


### 10. 📝 Summary

- Cluster analysis groups data based on similarity without prior labels.
- Many clustering algorithms exist, each suited for different data types and applications.
- Partitioning methods (k-means, k-medoids) are popular but have limitations.
- Hierarchical methods build nested clusters and do not require k upfront.
- Density-based methods find arbitrarily shaped clusters and handle noise well.
- Grid-based methods are efficient for large datasets and high dimensions.
- Evaluating clustering quality is complex and depends on the availability of ground truth and the application context.



<br>

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