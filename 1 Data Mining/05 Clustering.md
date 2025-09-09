## 5. Clustering

## Key Points

#### 1. 🧩 Cluster Analysis Basics  
- A cluster is a group of data objects similar within the group and dissimilar to objects in other groups.  
- Clustering is an unsupervised learning method with no predefined classes.  
- Good clustering has high intra-class similarity and low inter-class similarity.  
- Similarity is typically measured by a distance function, which varies by data type (numeric, categorical, etc.).  

#### 2. 📏 Similarity and Quality Measures  
- Distance metrics include Euclidean, Manhattan, and categorical distances.  
- Quality functions measure cluster “goodness” but are subjective.  
- Weights can be assigned to variables based on application semantics.  

#### 3. 🔢 Partitioning Methods  
- Partitioning divides data into k clusters minimizing sum of squared distances.  
- K-means uses cluster centroids (mean points) as representatives.  
- K-medoids (PAM) uses actual data points (medoids) as cluster centers.  
- K-means is efficient (O(tkn)) but sensitive to outliers and requires k in advance.  
- K-medoids is more robust but computationally expensive (O(k(n-k)²)).  
- Variants: k-modes for categorical data, k-prototypes for mixed data.  

#### 4. 🌳 Hierarchical Clustering  
- Does not require specifying number of clusters k upfront.  
- Agglomerative (AGNES) merges clusters bottom-up; divisive (DIANA) splits top-down.  
- Linkage methods: single link (min distance), complete link (max distance), average link, centroid, medoid.  
- Produces dendrogram showing nested cluster structure.  
- BIRCH uses CF-tree for scalable hierarchical clustering.  
- CHAMELEON merges clusters based on relative interconnectivity and closeness.  

#### 5. 🌊 Density-Based Clustering  
- Uses parameters Eps (neighborhood radius) and MinPts (minimum points in neighborhood).  
- Core point: point with ≥ MinPts neighbors within Eps.  
- DBSCAN defines clusters as maximal sets of density-connected points, can find arbitrary shapes and noise.  
- OPTICS produces cluster ordering reflecting density structure over multiple parameters.  
- DENCLUE uses statistical density functions and density attractors (local maxima) for clustering.  

#### 6. 🗺️ Grid-Based Clustering  
- Divides data space into grid cells and clusters based on cell density.  
- STING uses hierarchical rectangular cells with stored statistics for fast querying.  
- CLIQUE identifies dense cells in subspaces of high-dimensional data using apriori principle.  
- Grid-based methods are efficient but produce axis-aligned cluster boundaries.  

#### 7. 📊 Clustering Evaluation  
- Hopkins statistic tests if data is uniformly distributed (H ≈ 0.5) or clustered (H close to 0).  
- Number of clusters can be estimated by empirical rule (~√(n/2)) or elbow method.  
- Cross-validation splits data to test clustering quality for different k values.  
- Extrinsic evaluation compares clustering to ground truth (e.g., BCubed precision/recall).  
- Intrinsic evaluation uses measures like silhouette coefficient to assess cluster compactness and separation.  
- Good clustering quality criteria: homogeneity, completeness, rag bag penalty, small cluster preservation.



<br>

## Study Notes

### 1. 🧩 What is Cluster Analysis? Basic Concepts

Cluster analysis is a fundamental technique in data mining and machine learning used to group a set of data objects into clusters. A **cluster** is defined as a collection of data points that are similar or related to each other within the same group, and dissimilar or unrelated to points in other groups.

#### Why Cluster?

- **Unsupervised learning:** Unlike classification, clustering does not rely on predefined labels or classes. It learns patterns purely from the data itself.
- **Purpose:** To partition data into meaningful groups where intra-group similarity is high and inter-group similarity is low.

#### Applications of Clustering

Clustering is widely used across many fields:

- **Biology:** Classifying living organisms into taxonomic groups (kingdom, phylum, class, etc.).
- **Information retrieval:** Grouping similar documents for easier search and organization.
- **Land use:** Identifying regions with similar land characteristics from satellite data.
- **Marketing:** Segmenting customers into distinct groups for targeted campaigns.
- **City planning:** Grouping houses by type, value, or location.
- **Earthquake studies:** Clustering epicenters to identify fault lines.

#### Clustering as a Preprocessing Tool

Clustering can also be used to simplify or enhance other data mining tasks:

- **Summarization:** Reducing data complexity before regression or classification.
- **Compression:** Vector quantization in image processing.
- **Nearest neighbor search:** Limiting search to relevant clusters.
- **Outlier detection:** Identifying points far from any cluster.

#### What Makes a Good Clustering?

- **High intra-class similarity:** Points within the same cluster should be very similar.
- **Low inter-class similarity:** Clusters should be well separated.
- The quality depends on the similarity measure, the clustering algorithm, and the ability to reveal hidden patterns.


### 2. 📏 Measuring Similarity and Quality in Clustering

#### Similarity and Distance Metrics

Clustering relies on a **similarity measure** or its inverse, a **distance metric**, to decide how close or far data points are. Common distance functions include:

- **Euclidean distance:** For continuous numeric data.
- **Manhattan distance:** Sum of absolute differences.
- **Categorical distances:** Based on matching or mismatching categories.
- **Mixed data types:** Weighted combinations of different metrics.

Choosing the right metric depends on the data type and domain knowledge.

#### Quality Functions

- A **quality function** evaluates how good a clustering is.
- Defining "good enough" is subjective and depends on the application.
- Common goals: maximize similarity within clusters, minimize similarity between clusters.


### 3. 🔢 Partitioning Methods

Partitioning methods divide the dataset into a fixed number **k** of clusters, optimizing a criterion such as minimizing the sum of squared distances within clusters.

#### K-Means Algorithm

- **Goal:** Partition data into k clusters minimizing the sum of squared distances to cluster centroids.
- **Steps:**
  1. Initialize k centroids (seed points).
  2. Assign each data point to the nearest centroid.
  3. Recalculate centroids as the mean of assigned points.
  4. Repeat steps 2-3 until assignments stabilize.

- **Strengths:** Efficient (linear in number of points), simple.
- **Weaknesses:** Sensitive to outliers, requires k in advance, only works well with numeric data, tends to find spherical clusters.

#### K-Medoids (PAM)

- Similar to k-means but uses actual data points (medoids) as cluster centers.
- More robust to noise and outliers.
- Computationally expensive for large datasets.
- Variants like CLARA and CLARANS improve scalability by sampling or randomized search.

#### Variations

- **K-modes:** For categorical data, replaces means with modes.
- **K-prototypes:** Handles mixed numeric and categorical data.


### 4. 🌳 Hierarchical Clustering Methods

Hierarchical clustering builds a tree of clusters called a **dendrogram**, showing nested groupings at multiple levels.

#### Two Types

- **Agglomerative (bottom-up):** Start with each point as a cluster, merge closest clusters step-by-step.
- **Divisive (top-down):** Start with all points in one cluster, split recursively.

#### Linkage Criteria

- **Single link:** Distance between closest points of two clusters.
- **Complete link:** Distance between farthest points.
- **Average link:** Average distance between all pairs.
- **Centroid link:** Distance between cluster centroids.
- **Medoid link:** Distance between medoids.

#### Advantages and Challenges

- Does not require specifying k upfront.
- Produces a hierarchy useful for understanding data structure.
- Computationally expensive (O(n²) or worse).
- Cannot undo merges once done (greedy).

#### Advanced Hierarchical Methods

- **BIRCH:** Builds a CF-tree summarizing clusters incrementally, scalable to large datasets.
- **CHAMELEON:** Uses dynamic modeling and graph partitioning to merge clusters based on relative interconnectivity and closeness.


### 5. 🌊 Density-Based Clustering Methods

Density-based methods define clusters as dense regions of points separated by sparser regions, allowing discovery of clusters with arbitrary shapes and handling noise.

#### Key Concepts

- **Eps (ε):** Radius defining neighborhood around a point.
- **MinPts:** Minimum number of points required in an ε-neighborhood to form a dense region.
- **Core point:** A point with at least MinPts neighbors within ε.
- **Directly density-reachable:** A point p is directly reachable from q if p is in q’s ε-neighborhood and q is a core point.
- **Density-reachable:** A chain of directly density-reachable points.
- **Density-connected:** Two points connected through a common density-reachable point.

#### DBSCAN

- Finds clusters as maximal sets of density-connected points.
- Can find arbitrarily shaped clusters and identify noise.
- Sensitive to parameters ε and MinPts.

#### OPTICS

- Produces an ordering of points reflecting clustering structure over a range of parameters.
- Uses **core distance** and **reachability distance** to represent density connectivity.
- More flexible than DBSCAN, useful for interactive analysis.

#### DENCLUE

- Uses statistical density functions and gradient ascent to find **density attractors** (local maxima).
- Clusters are formed around these attractors.
- Can handle noise and arbitrary shapes efficiently.
- Uses influence functions to model point impact on density.


### 6. 🗺️ Grid-Based Clustering Methods

Grid-based methods divide the data space into a finite number of cells forming a grid structure, then perform clustering on these cells rather than individual points.

#### Advantages

- Fast and scalable.
- Suitable for large spatial datasets.
- Multi-resolution analysis possible.

#### Examples

- **STING:** Divides space into hierarchical rectangular cells, stores statistical info (count, mean, std dev) for each cell, and uses a top-down approach to find clusters.
- **CLIQUE:** Combines grid and density-based ideas to find dense cells in subspaces of high-dimensional data, automatically discovering relevant subspaces.
- **WaveCluster:** Uses wavelet transforms to identify dense regions at multiple resolutions.

#### Strengths and Weaknesses

- Efficient and easy to parallelize.
- Boundaries are axis-aligned (no diagonal boundaries).
- Sensitive to grid size and density thresholds.


### 7. 📊 Evaluating Clustering Quality

Evaluating clustering results is crucial to ensure meaningful groupings.

#### Assessing Cluster Tendency

- **Hopkins Statistic:** Measures whether data is uniformly distributed or has cluster structure.
- Values close to 0.5 indicate randomness; values near 0 indicate clustering tendency.

#### Determining Number of Clusters

- **Empirical rule:** Number of clusters ≈ √(n/2), where n is number of points.
- **Elbow method:** Plot sum of squared errors vs. k; choose k at the "elbow" point.
- **Cross-validation:** Split data, train on subsets, test on remaining data to find best k.

#### Quality Measures

- **Extrinsic (supervised):** Compare clustering to ground truth using precision, recall, BCubed metrics.
- **Intrinsic (unsupervised):** Use measures like silhouette coefficient to evaluate cluster compactness and separation without ground truth.

#### Essential Criteria for Good Clustering Quality

- **Homogeneity:** Clusters contain only similar objects.
- **Completeness:** Objects of the same class are in the same cluster.
- **Rag bag:** Penalize placing heterogeneous objects in pure clusters.
- **Small cluster preservation:** Avoid splitting small but meaningful clusters.


### 8. 📝 Summary and Outlook

Clustering is a versatile and powerful tool for discovering structure in data without prior labels. Different methods suit different data types and goals:

- **Partitioning methods** are simple and efficient but require specifying the number of clusters.
- **Hierarchical methods** provide rich multi-level cluster structures but can be computationally expensive.
- **Density-based methods** excel at finding arbitrarily shaped clusters and handling noise.
- **Grid-based methods** offer scalability and multi-resolution analysis, especially for spatial data.

Choosing the right clustering method depends on data characteristics, application needs, and computational resources. Evaluating clustering quality remains a challenging but essential step to ensure meaningful insights.


### End of Study Notes