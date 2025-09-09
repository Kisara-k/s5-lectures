## 6. Clustering Alt

## Key Points

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