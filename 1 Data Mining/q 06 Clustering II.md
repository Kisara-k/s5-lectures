## 6. Clustering II

## Questions

#### 1. Which of the following statements about density-based clustering are true?  
A) Density-based clustering can discover clusters of arbitrary shape.  
B) Density-based clustering requires the number of clusters to be specified in advance.  
C) Density-based clustering can handle noise effectively.  
D) Density-based clustering always requires multiple scans of the dataset.


#### 2. In DBSCAN, a point p is called a core point if:  
A) The number of points in its Eps-neighborhood is at least MinPts.  
B) It is directly density-reachable from another point.  
C) It has the highest density in the dataset.  
D) It lies within the Eps radius of at least one other core point.


#### 3. Which of the following correctly describe the concept of density-reachability?  
A) It is a symmetric relation between points.  
B) It requires a chain of points where each is directly density-reachable from the previous.  
C) If p is density-reachable from q, then q is density-reachable from p.  
D) Density-reachability depends on the parameters Eps and MinPts.


#### 4. What is the difference between density-reachable and density-connected points?  
A) Density-connected points must both be density-reachable from a common core point.  
B) Density-reachable points are always density-connected.  
C) Density-connected is a symmetric relation, density-reachable is not.  
D) Density-reachable points must be within Eps distance of each other.


#### 5. Which of the following are true about the DBSCAN algorithm?  
A) It can find clusters with arbitrary shapes.  
B) It requires the number of clusters as an input parameter.  
C) It labels points that are not density-reachable from any core point as noise.  
D) It is insensitive to the choice of Eps and MinPts parameters.


#### 6. OPTICS improves upon DBSCAN by:  
A) Producing a cluster ordering that captures clustering structure for multiple parameter settings.  
B) Eliminating the need for the MinPts parameter.  
C) Using core distance and reachability distance to order points.  
D) Guaranteeing a unique clustering result regardless of parameter choice.


#### 7. In OPTICS, the reachability distance of a point p from a point o is defined as:  
A) The minimum of the core distance of o and the distance between o and p.  
B) The maximum of the core distance of o and the distance between o and p.  
C) The distance between p and its nearest core point.  
D) The average distance between p and all points in o’s Eps-neighborhood.


#### 8. Which of the following statements about DENCLUE are correct?  
A) It uses statistical density functions to model data distribution.  
B) Clusters are defined by local density maxima called density attractors.  
C) It requires fewer parameters than DBSCAN.  
D) It assigns each data point to the cluster of its density attractor.


#### 9. How does DENCLUE handle clusters of arbitrary shape?  
A) By merging density attractors connected by high-density paths.  
B) By partitioning the data space into rectangular grid cells.  
C) By using a fixed radius neighborhood for all points.  
D) By assigning points to the nearest cluster centroid.


#### 10. Which of the following are advantages of grid-based clustering methods like STING?  
A) They are easy to parallelize.  
B) They can detect clusters with diagonal boundaries.  
C) They support incremental updates efficiently.  
D) They require no parameter tuning.


#### 11. What is a major limitation of the STING clustering method?  
A) It only detects clusters with axis-aligned boundaries.  
B) It cannot handle noise in the data.  
C) It requires the number of clusters as input.  
D) It cannot be applied to high-dimensional data.


#### 12. CLIQUE is a clustering method that:  
A) Combines grid-based and density-based approaches.  
B) Automatically identifies subspaces with meaningful clusters.  
C) Requires the user to specify the number of clusters.  
D) Uses the Apriori principle to prune candidate dense cells.


#### 13. In CLIQUE, a k-dimensional cell is considered dense if:  
A) It contains at least a threshold number of points.  
B) All of its (k-1)-dimensional projections are dense.  
C) It is connected to at least one other dense cell.  
D) It contains the global maximum density point.


#### 14. Which of the following statements about the evaluation of clustering are true?  
A) The Hopkins statistic measures the tendency of data to form clusters.  
B) A Hopkins statistic close to 0.5 indicates strong clustering tendency.  
C) The elbow method uses within-cluster variance to determine the number of clusters.  
D) Cross-validation can be used to select the best number of clusters.


#### 15. When using extrinsic clustering quality measures, which of the following criteria are important?  
A) Cluster homogeneity (purity).  
B) Cluster completeness (all members of a class in one cluster).  
C) Penalizing putting heterogeneous objects into pure clusters more than into rag bags.  
D) Ignoring small clusters to focus on large clusters.


#### 16. The Silhouette coefficient is an example of:  
A) An extrinsic clustering quality measure.  
B) An intrinsic clustering quality measure.  
C) A method to determine the number of clusters.  
D) A density-based clustering algorithm.


#### 17. Which of the following statements about the parameters Eps and MinPts in DBSCAN are correct?  
A) Increasing Eps generally results in fewer clusters.  
B) Increasing MinPts generally results in more noise points.  
C) Eps defines the radius of the neighborhood around a point.  
D) MinPts defines the minimum number of points required to form a dense region.


#### 18. Which of the following are true about the complexity of OPTICS?  
A) It can achieve O(N log N) complexity using spatial index structures.  
B) Without spatial indexes, its complexity is O(N²).  
C) It requires multiple passes over the data.  
D) It is always faster than DBSCAN.


#### 19. In density-based clustering, a border point is:  
A) A point that is not a core point but lies within the Eps-neighborhood of a core point.  
B) A point that has fewer than MinPts neighbors within Eps.  
C) A point that is density-reachable from multiple core points.  
D) A point that is always considered noise.


#### 20. Which of the following statements about the use of grid cells in clustering are true?  
A) Grid-based methods reduce computational complexity by summarizing data in cells.  
B) Grid cells always contain equal numbers of data points.  
C) Grid-based clustering can be combined with density-based approaches.  
D) The choice of grid size and density threshold can significantly affect clustering results.



<br>

## Answers

#### 1. Which of the following statements about density-based clustering are true?  
A) ✓ Density-based clustering can discover clusters of arbitrary shape.  
B) ✗ It does not require the number of clusters to be specified in advance.  
C) ✓ It can handle noise effectively by labeling outliers.  
D) ✗ Usually requires only one scan, not multiple scans.

**Correct:** A, C


#### 2. In DBSCAN, a point p is called a core point if:  
A) ✓ It has at least MinPts points in its Eps-neighborhood.  
B) ✗ Being directly density-reachable is a relation, not a core point definition.  
C) ✗ Core points are not necessarily the highest density points.  
D) ✗ Being within Eps of a core point does not define core points themselves.

**Correct:** A


#### 3. Which of the following correctly describe the concept of density-reachability?  
A) ✗ Density-reachability is not symmetric.  
B) ✓ It requires a chain of directly density-reachable points.  
C) ✗ If p is density-reachable from q, q is not necessarily density-reachable from p.  
D) ✓ It depends on Eps and MinPts parameters.

**Correct:** B, D


#### 4. What is the difference between density-reachable and density-connected points?  
A) ✓ Density-connected points share a common point from which both are density-reachable.  
B) ✗ Density-reachable points are not always density-connected.  
C) ✓ Density-connected is symmetric; density-reachable is not.  
D) ✗ Density-reachable does not require points to be within Eps of each other directly.

**Correct:** A, C


#### 5. Which of the following are true about the DBSCAN algorithm?  
A) ✓ It can find clusters of arbitrary shape.  
B) ✗ It does not require the number of clusters as input.  
C) ✓ Points not density-reachable from any core point are labeled noise.  
D) ✗ It is sensitive to parameter choice.

**Correct:** A, C


#### 6. OPTICS improves upon DBSCAN by:  
A) ✓ Producing a cluster ordering for multiple parameter settings.  
B) ✗ It still requires MinPts.  
C) ✓ Uses core distance and reachability distance to order points.  
D) ✗ It does not guarantee a unique clustering regardless of parameters.

**Correct:** A, C


#### 7. In OPTICS, the reachability distance of a point p from a point o is defined as:  
A) ✗ It is the maximum, not minimum.  
B) ✓ It is the maximum of core distance of o and distance between o and p.  
C) ✗ It is not simply distance to nearest core point.  
D) ✗ It is not an average distance.

**Correct:** B


#### 8. Which of the following statements about DENCLUE are correct?  
A) ✓ Uses statistical density functions to model data.  
B) ✓ Clusters defined by local density maxima (density attractors).  
C) ✗ Requires more parameters than DBSCAN.  
D) ✓ Each point assigned to cluster of its density attractor.

**Correct:** A, B, D


#### 9. How does DENCLUE handle clusters of arbitrary shape?  
A) ✓ By merging density attractors connected by high-density paths.  
B) ✗ It does not rely on fixed rectangular grids for clustering.  
C) ✗ It does not use fixed radius neighborhoods for all points.  
D) ✗ It does not assign points to nearest centroid.

**Correct:** A


#### 10. Which of the following are advantages of grid-based clustering methods like STING?  
A) ✓ Easy to parallelize due to grid structure.  
B) ✗ Cannot detect diagonal or arbitrary boundaries, only axis-aligned.  
C) ✓ Supports incremental updates efficiently.  
D) ✗ Requires parameter tuning like grid size.

**Correct:** A, C


#### 11. What is a major limitation of the STING clustering method?  
A) ✓ Only detects clusters with axis-aligned boundaries.  
B) ✗ It can handle noise to some extent.  
C) ✗ Does not require number of clusters as input.  
D) ✗ Can be applied to high-dimensional data with some limitations.

**Correct:** A


#### 12. CLIQUE is a clustering method that:  
A) ✓ Combines grid-based and density-based approaches.  
B) ✓ Automatically identifies subspaces with meaningful clusters.  
C) ✗ Does not require number of clusters as input.  
D) ✓ Uses Apriori principle to prune candidate dense cells.

**Correct:** A, B, D


#### 13. In CLIQUE, a k-dimensional cell is considered dense if:  
A) ✓ It contains at least a threshold number of points.  
B) ✓ All its (k-1)-dimensional projections are dense (Apriori principle).  
C) ✗ Connectivity defines clusters, not density of individual cells.  
D) ✗ Density is not defined by global maximum points.

**Correct:** A, B


#### 14. Which of the following statements about the evaluation of clustering are true?  
A) ✓ Hopkins statistic measures clustering tendency.  
B) ✗ Hopkins close to 0.5 means uniform (no clusters), not strong clustering.  
C) ✓ Elbow method uses within-cluster variance to find cluster number.  
D) ✓ Cross-validation can help select number of clusters.

**Correct:** A, C, D


#### 15. When using extrinsic clustering quality measures, which of the following criteria are important?  
A) ✓ Cluster homogeneity is important.  
B) ✓ Cluster completeness is important.  
C) ✓ Penalizing heterogeneous objects in pure clusters more than rag bags.  
D) ✗ Small clusters should not be ignored; preserving them is important.

**Correct:** A, B, C


#### 16. The Silhouette coefficient is an example of:  
A) ✗ It is an intrinsic measure, not extrinsic.  
B) ✓ An intrinsic clustering quality measure.  
C) ✗ It does not determine number of clusters directly.  
D) ✗ It is not a clustering algorithm.

**Correct:** B


#### 17. Which of the following statements about the parameters Eps and MinPts in DBSCAN are correct?  
A) ✓ Increasing Eps generally results in fewer clusters (more points grouped).  
B) ✗ Increasing MinPts generally results in fewer noise points, not more.  
C) ✓ Eps defines the radius of neighborhood.  
D) ✓ MinPts defines minimum points to form a dense region.

**Correct:** A, C, D


#### 18. Which of the following are true about the complexity of OPTICS?  
A) ✓ Can achieve O(N log N) with spatial index structures.  
B) ✓ Without indexes, complexity is O(N²).  
C) ✗ Requires only one pass over data, not multiple.  
D) ✗ Not always faster than DBSCAN; depends on implementation.

**Correct:** A, B


#### 19. In density-based clustering, a border point is:  
A) ✓ Not a core point but lies within Eps of a core point.  
B) ✓ Has fewer than MinPts neighbors but reachable from core point.  
C) ✗ May be density-reachable from multiple core points but not necessarily.  
D) ✗ Border points are not noise.

**Correct:** A, B


#### 20. Which of the following statements about the use of grid cells in clustering are true?  
A) ✓ Grid-based methods reduce complexity by summarizing data in cells.  
B) ✗ Grid cells do not necessarily contain equal numbers of points; they are spatial partitions.  
C) ✓ Grid-based clustering can be combined with density-based approaches (e.g., CLIQUE).  
D) ✓ Choice of grid size and density threshold significantly affects results.

**Correct:** A, C, D