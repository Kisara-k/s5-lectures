## 6. Clustering II

## Key Points

#### 1. 🧩 Density-Based Clustering Basics  
- Two main parameters: **Eps** (maximum neighborhood radius) and **MinPts** (minimum points in Eps-neighborhood).  
- A **core point** has at least MinPts points within its Eps-neighborhood.  
- **Directly density-reachable**: point p is in the Eps-neighborhood of core point q.  
- **Density-reachable**: there exists a chain of directly density-reachable points from q to p.  
- **Density-connected**: points p and q are density-connected if both are density-reachable from some point o.

#### 2. 🌀 DBSCAN Algorithm  
- Clusters are maximal sets of density-connected points.  
- Steps: select point p → if core, retrieve all density-reachable points → form cluster → if border, assign to cluster → if noise, mark as noise.  
- Sensitive to parameters Eps and MinPts.  
- Can find clusters of arbitrary shape and handle noise.

#### 3. 🔍 OPTICS Algorithm  
- Produces an ordering of points reflecting clustering structure for a range of parameters.  
- Uses **core distance** (minimum radius for core point) and **reachability distance** (max of core distance and distance between points).  
- Maintains a priority queue ordered by reachability distance.  
- Complexity: O(N log N) with spatial index; otherwise O(N²).  
- Useful for interactive cluster analysis and visualization.

#### 4. 📈 DENCLUE Algorithm  
- Uses statistical density functions and influence functions to model data density.  
- Defines clusters by **density attractors** (local maxima of density function).  
- Assigns points to clusters based on gradient ascent to density attractors.  
- Can merge clusters via high-density paths between attractors.  
- Faster than DBSCAN but requires more parameters.

#### 5. 🗺️ Grid-Based Clustering Methods  
- Divide data space into grid cells; clustering done on cells, not points.  
- **STING**: multi-resolution grid, stores statistical info per cell, uses top-down approach.  
- **CLIQUE**: partitions each dimension into equal intervals, identifies dense cells, clusters are connected dense cells in subspaces.  
- CLIQUE uses Apriori principle: a k-dimensional cell is dense only if all (k-1)-dimensional projections are dense.  
- Grid-based methods are efficient but cluster boundaries are axis-aligned.

#### 6. 📊 Clustering Evaluation: Assessing Tendency  
- **Hopkins Statistic** tests spatial randomness:  
  - H ≈ 0.5 → uniform distribution (no clusters).  
  - H close to 0 → clustered data.

#### 7. 📊 Clustering Evaluation: Determining Number of Clusters  
- Empirical rule: number of clusters ≈ √(n/2) for n data points.  
- **Elbow method**: find turning point in within-cluster variance vs. number of clusters.  
- **Cross-validation**: split data, train on subsets, test on remaining, evaluate sum of squared distances.

#### 8. 📊 Clustering Evaluation: Quality Measures  
- **Extrinsic methods**: compare clustering to ground truth using metrics like BCubed precision and recall.  
- Essential criteria: cluster homogeneity, completeness, rag bag penalty, small cluster preservation.  
- **Intrinsic methods**: evaluate cluster compactness and separation without ground truth, e.g., Silhouette coefficient.



<br>

## Study Notes

### 1. 🧩 Introduction to Clustering and Density-Based Methods

Clustering is a fundamental technique in data analysis used to group similar data points together without prior knowledge of labels. The goal is to discover natural groupings or patterns in data. There are several clustering approaches, including partitioning, hierarchical, density-based, and grid-based methods. This note focuses on **density-based clustering methods**, which are powerful for discovering clusters of arbitrary shapes and handling noise effectively.

#### What is Density-Based Clustering?

Density-based clustering defines clusters as areas of higher density separated by areas of lower density. Unlike methods that assume spherical clusters (like k-means), density-based methods can find clusters of any shape, making them very useful for spatial data or complex datasets.

Key features of density-based clustering:
- Can discover clusters of arbitrary shape.
- Can handle noise (outliers) naturally.
- Usually requires only a few parameters.
- Often requires just one scan of the data.


### 2. 🌐 Core Concepts in Density-Based Clustering

Density-based clustering relies on two main parameters:

- **Eps (ε)**: The maximum radius of the neighborhood around a data point.
- **MinPts**: The minimum number of points required within the Eps-radius neighborhood for a point to be considered a core point.

#### Important Definitions:

- **Eps-neighborhood (NEps(p))**: For a point p, this is the set of points within distance Eps of p.
  
- **Core Point**: A point p is a core point if its Eps-neighborhood contains at least MinPts points (including p itself).

- **Directly Density-Reachable**: A point p is directly density-reachable from q if p is in q’s Eps-neighborhood and q is a core point.

- **Density-Reachable**: A point p is density-reachable from q if there is a chain of points starting at q and ending at p, where each point in the chain is directly density-reachable from the previous one.

- **Density-Connected**: Two points p and q are density-connected if there exists a point o such that both p and q are density-reachable from o.

These concepts help define clusters as maximal sets of density-connected points.


### 3. 🌀 DBSCAN: Density-Based Spatial Clustering of Applications with Noise

DBSCAN is one of the most popular density-based clustering algorithms, introduced by Ester et al. in 1996. It uses the concepts above to find clusters and noise.

#### How DBSCAN Works:

1. **Select an arbitrary point p**.
2. If p is a **core point** (has at least MinPts neighbors within Eps), retrieve all points density-reachable from p. These points form a cluster.
3. If p is a **border point** (not a core point but within the neighborhood of a core point), it is assigned to the cluster of the core point.
4. If p is **noise** (neither core nor border), it is marked as noise.
5. Repeat until all points are processed.

#### Strengths and Limitations:

- **Strengths**: Can find clusters of arbitrary shape, handles noise well.
- **Limitations**: Sensitive to the choice of Eps and MinPts parameters. Choosing these parameters incorrectly can lead to poor clustering.


### 4. 🔍 OPTICS: Ordering Points to Identify the Clustering Structure

OPTICS (Ankerst et al., 1999) extends DBSCAN by addressing the sensitivity to parameters. Instead of producing a single clustering, OPTICS creates an ordering of points that captures the clustering structure for a range of parameter values.

#### Key Concepts in OPTICS:

- **Core Distance**: The smallest radius such that a point is a core point.
- **Reachability Distance**: For a point p from another point o, it is the maximum of o’s core distance and the distance between o and p.

#### How OPTICS Works:

- Maintains a priority queue (ordered_seeds) sorted by reachability distance.
- Starts with an arbitrary point, computes its core distance and reachability distances to neighbors.
- Outputs points in an order that reflects the density-based clustering structure.
- This ordering can be visualized to identify clusters at different density levels.

#### Advantages:

- Captures clustering structure for multiple parameter settings.
- Useful for interactive and automatic cluster analysis.
- More robust than DBSCAN in parameter selection.


### 5. 📈 DENCLUE: Density-Based Clustering Using Statistical Density Functions

DENCLUE (Hinneburg & Keim, 1998) uses a mathematical approach based on **statistical density functions** to model the data distribution.

#### Core Ideas:

- Uses **influence functions** to describe the impact of each data point on the overall density.
- The overall density is the sum of influence functions of all points.
- Clusters are defined by **density attractors**, which are local maxima of the density function found by gradient ascent.
- Each data point is assigned to the cluster of its density attractor.
- Clusters of arbitrary shape are formed by connecting density attractors via high-density paths.

#### Advantages:

- Solid mathematical foundation.
- Handles noise well.
- Efficient for high-dimensional data.
- Faster than DBSCAN but requires more parameters.


### 6. 🗺️ Grid-Based Clustering Methods

Grid-based clustering divides the data space into a finite number of cells forming a grid structure. Clustering is performed on the grid cells rather than individual points, which can be computationally efficient.

#### Key Methods:

- **STING (Statistical Information Grid)**: Divides space into rectangular cells at multiple resolutions. Stores statistical info (count, mean, std dev) for each cell. Uses a top-down approach to refine clusters.
  
- **CLIQUE (Clustering In QUEst)**: Combines grid-based and density-based ideas. It partitions each dimension into equal intervals, forming rectangular cells. Cells with enough points are dense. Clusters are maximal connected sets of dense cells in subspaces.

#### STING Details:

- Uses hierarchical grid cells.
- Queries start at a coarse level and refine to finer levels.
- Advantages: Query-independent, easy to parallelize, incremental updates.
- Disadvantages: Cluster boundaries are axis-aligned (no diagonal boundaries).

#### CLIQUE Details:

- Automatically finds subspaces with meaningful clusters.
- Uses the Apriori principle: a k-dimensional cell is dense only if all its (k-1)-dimensional projections are dense.
- Clusters are formed by connecting dense cells.
- Strengths: Scales well with dimensions, insensitive to input order.
- Weaknesses: Sensitive to grid size and density threshold.


### 7. 📊 Evaluating Clustering Quality

Evaluating clustering results is crucial to understand how well the algorithm performed.

#### Assessing Clustering Tendency

Before clustering, check if the data has any meaningful structure or is just random noise.

- **Hopkins Statistic**: Measures spatial randomness.
  - Values close to 0.5 indicate uniform distribution (no clusters).
  - Values close to 0 indicate clustered data.

#### Determining Number of Clusters

- **Empirical Rule**: Number of clusters ≈ √(n/2), where n is the number of data points.
- **Elbow Method**: Plot sum of within-cluster variance vs. number of clusters; look for the "elbow" point where adding more clusters doesn’t significantly reduce variance.
- **Cross-Validation**: Split data into parts, train on some, test on others, and evaluate clustering quality to find the best number of clusters.

#### Measuring Clustering Quality

Two main approaches:

- **Extrinsic (Supervised)**: Compare clustering to ground truth labels using metrics like BCubed precision and recall.
  - Criteria include cluster homogeneity, completeness, rag bag penalty, and small cluster preservation.

- **Intrinsic (Unsupervised)**: Evaluate based on cluster compactness and separation without ground truth.
  - Example: Silhouette coefficient measures how similar a point is to its own cluster compared to other clusters.


### 8. 📝 Summary and Outlook

- Density-based clustering methods like DBSCAN, OPTICS, and DENCLUE are powerful for discovering clusters of arbitrary shape and handling noise.
- Grid-based methods like STING and CLIQUE offer efficient clustering by working on grid cells, useful for large datasets and high-dimensional data.
- Evaluating clustering quality and determining the number of clusters are essential steps to ensure meaningful results.
- Understanding the strengths and limitations of each method helps in selecting the right algorithm for a given problem.
- Future directions include improving parameter selection, scalability, and combining methods for better performance.