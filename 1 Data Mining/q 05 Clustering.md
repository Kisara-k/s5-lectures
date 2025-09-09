## 5. Clustering

## Questions

#### 1. What defines a cluster in cluster analysis?  
A) A group of data points with high similarity within the group and low similarity to points outside the group  
B) A group of data points with identical values  
C) A collection of data points that are dissimilar within the group but similar to points outside  
D) A set of data points partitioned randomly  

#### 2. Which of the following are typical applications of clustering?  
A) Taxonomy classification in biology  
B) Document retrieval and organization  
C) Supervised classification with labeled data  
D) Customer segmentation in marketing  

#### 3. Which statements about k-means clustering are true?  
A) It requires the number of clusters k to be specified in advance  
B) It can handle categorical data without modification  
C) It is sensitive to outliers and noise  
D) It always finds the global optimal clustering  

#### 4. How does k-medoids differ from k-means?  
A) K-medoids uses actual data points as cluster centers  
B) K-medoids is less sensitive to outliers than k-means  
C) K-medoids requires continuous numeric data only  
D) K-medoids is computationally more expensive than k-means  

#### 5. Which of the following are true about hierarchical clustering?  
A) It requires the number of clusters k as an input parameter  
B) It produces a dendrogram representing nested clusters  
C) Agglomerative clustering starts with each point as a cluster and merges them  
D) Divisive clustering starts with all points in one cluster and splits them  

#### 6. In hierarchical clustering, what does the single-link method measure?  
A) The smallest distance between any two points in different clusters  
B) The largest distance between any two points in different clusters  
C) The average distance between all pairs of points in different clusters  
D) The distance between cluster centroids  

#### 7. What are the main challenges of hierarchical clustering?  
A) It cannot undo previous merges or splits  
B) It scales poorly with large datasets due to high time complexity  
C) It requires specifying the number of clusters beforehand  
D) It is insensitive to the order of data points  

#### 8. Which of the following are characteristics of density-based clustering methods?  
A) They can find clusters of arbitrary shape  
B) They require the number of clusters k as input  
C) They can handle noise and outliers effectively  
D) They rely on density parameters such as Eps and MinPts  

#### 9. In DBSCAN, what is a core point?  
A) A point with at least MinPts neighbors within radius Eps  
B) A point that lies on the boundary of a cluster  
C) A point with fewer than MinPts neighbors within Eps  
D) A point that is not density-reachable from any other point  

#### 10. Which statements about density-reachable and density-connected points are correct?  
A) Density-reachable is a symmetric relation  
B) Density-connected points share a common core point from which both are density-reachable  
C) Density-reachable requires a chain of directly density-reachable points  
D) Density-connected points must be directly density-reachable from each other  

#### 11. What is the main advantage of OPTICS over DBSCAN?  
A) OPTICS produces a cluster ordering that captures clustering structure over a range of parameters  
B) OPTICS requires fewer parameters than DBSCAN  
C) OPTICS can handle varying density clusters better than DBSCAN  
D) OPTICS always produces disjoint clusters  

#### 12. Which of the following are true about DENCLUE?  
A) It uses statistical density functions and influence functions  
B) It identifies clusters based on local density maxima called density attractors  
C) It cannot handle noise in the data  
D) It merges clusters if their density attractors are connected by high-density paths  

#### 13. What is a key limitation of grid-based clustering methods like STING?  
A) They can only detect clusters with axis-aligned boundaries  
B) They are not scalable to large datasets  
C) They require the number of clusters to be specified in advance  
D) They cannot handle high-dimensional data  

#### 14. How does CLIQUE differ from other grid-based methods?  
A) It automatically identifies subspaces with dense clusters in high-dimensional data  
B) It partitions each dimension into equal-length intervals  
C) It requires user-specified cluster shapes  
D) It uses the apriori principle to prune candidate dense cells  

#### 15. Which of the following statements about cluster evaluation are correct?  
A) The Hopkins statistic tests whether data is uniformly distributed or clustered  
B) The elbow method helps determine the optimal number of clusters by analyzing within-cluster variance  
C) Silhouette coefficient requires ground truth labels to evaluate clustering quality  
D) Cross-validation can be used to select the number of clusters by testing model fit on held-out data  

#### 16. Which criteria are essential for a good clustering quality measure?  
A) Cluster homogeneity (purity)  
B) Cluster completeness (all members of a class in one cluster)  
C) Penalizing splitting of large clusters more than small clusters  
D) Penalizing placing heterogeneous objects into pure clusters more than into rag bag clusters  

#### 17. What are the main differences between partitioning and hierarchical clustering methods?  
A) Partitioning methods require k as input, hierarchical methods do not  
B) Hierarchical methods produce nested clusters, partitioning methods produce flat clusters  
C) Partitioning methods can handle arbitrary shaped clusters better than hierarchical methods  
D) Hierarchical methods can undo previous merges or splits  

#### 18. Which of the following statements about BIRCH are true?  
A) BIRCH incrementally builds a CF-tree summarizing clusters  
B) BIRCH scales linearly with the number of data points  
C) BIRCH can handle categorical data natively  
D) BIRCH is sensitive to the order of data insertion  

#### 19. In the context of clustering, what is a medoid?  
A) The mean point of a cluster  
B) The most centrally located actual data point in a cluster  
C) A synthetic point representing the cluster center  
D) The point farthest from the cluster centroid  

#### 20. Which of the following are challenges in cluster analysis?  
A) Scalability to large datasets  
B) Handling mixed data types (numerical, categorical, ordinal)  
C) Discovering clusters with arbitrary shapes  
D) Ensuring clusters are always convex and spherical



<br>

## Answers

#### 1. What defines a cluster in cluster analysis?  
A) ✓ A group of data points with high similarity within the group and low similarity to points outside the group  
B) ✗ Identical values are not required; similarity is relative, not exact equality  
C) ✗ Clusters should be similar within, not dissimilar  
D) ✗ Clusters are not formed randomly; they are based on similarity  

**Correct:** A


#### 2. Which of the following are typical applications of clustering?  
A) ✓ Taxonomy classification in biology is a classic clustering application  
B) ✓ Document retrieval uses clustering to group similar documents  
C) ✗ Supervised classification uses labeled data, not clustering  
D) ✓ Customer segmentation is a common clustering use case  

**Correct:** A, B, D


#### 3. Which statements about k-means clustering are true?  
A) ✓ K-means requires k to be specified beforehand  
B) ✗ K-means works only on numeric data; categorical data needs k-modes or other methods  
C) ✓ K-means is sensitive to outliers because means are affected by extreme values  
D) ✗ K-means often converges to local optima, not guaranteed global optimum  

**Correct:** A, C


#### 4. How does k-medoids differ from k-means?  
A) ✓ K-medoids uses actual data points as cluster centers (medoids)  
B) ✓ K-medoids is more robust to outliers since medoids are less influenced by extremes  
C) ✗ K-medoids can handle various data types, not limited to continuous numeric  
D) ✓ K-medoids is computationally more expensive due to pairwise distance calculations  

**Correct:** A, B, D


#### 5. Which of the following are true about hierarchical clustering?  
A) ✗ It does not require k as input; clusters are formed by cutting dendrogram  
B) ✓ Produces a dendrogram showing nested cluster structure  
C) ✓ Agglomerative clustering merges clusters starting from single points  
D) ✓ Divisive clustering splits clusters starting from all points in one cluster  

**Correct:** B, C, D


#### 6. In hierarchical clustering, what does the single-link method measure?  
A) ✓ Single link measures the smallest distance between points in different clusters  
B) ✗ Largest distance is complete link, not single link  
C) ✗ Average distance is average linkage, not single link  
D) ✗ Distance between centroids is centroid linkage, not single link  

**Correct:** A


#### 7. What are the main challenges of hierarchical clustering?  
A) ✓ Cannot undo merges or splits once done (greedy)  
B) ✓ Time complexity is at least O(n²), limiting scalability  
C) ✗ Does not require specifying k upfront  
D) ✗ Sensitive to input order in some implementations, so not always insensitive  

**Correct:** A, B


#### 8. Which of the following are characteristics of density-based clustering methods?  
A) ✓ Can find clusters of arbitrary shape due to density connectivity  
B) ✗ Do not require k as input; parameters are density-based (Eps, MinPts)  
C) ✓ Handle noise and outliers by labeling them as noise points  
D) ✓ Rely on density parameters like Eps (radius) and MinPts (min points)  

**Correct:** A, C, D


#### 9. In DBSCAN, what is a core point?  
A) ✓ A point with at least MinPts neighbors within radius Eps  
B) ✗ Border points lie on cluster edges but have fewer neighbors  
C) ✗ Points with fewer than MinPts neighbors are not core points  
D) ✗ Core points are density reachable, not isolated  

**Correct:** A


#### 10. Which statements about density-reachable and density-connected points are correct?  
A) ✗ Density-reachable is not symmetric; if p is reachable from q, q may not be from p  
B) ✓ Density-connected points share a common core point from which both are density-reachable  
C) ✓ Density-reachable requires a chain of directly density-reachable points  
D) ✗ Density-connected does not require direct density reachability between p and q  

**Correct:** B, C


#### 11. What is the main advantage of OPTICS over DBSCAN?  
A) ✓ OPTICS produces a cluster ordering capturing structure over multiple parameter settings  
B) ✗ OPTICS still requires parameters like Eps and MinPts, though less sensitive  
C) ✓ Handles varying density clusters better by ordering points rather than fixed clusters  
D) ✗ OPTICS does not necessarily produce disjoint clusters; it produces an ordering  

**Correct:** A, C


#### 12. Which of the following are true about DENCLUE?  
A) ✓ Uses statistical density functions and influence functions to model density  
B) ✓ Identifies clusters based on local density maxima called density attractors  
C) ✗ Can handle noise by ignoring low-density regions  
D) ✓ Merges clusters if density attractors are connected by high-density paths  

**Correct:** A, B, D


#### 13. What is a key limitation of grid-based clustering methods like STING?  
A) ✓ Cluster boundaries are axis-aligned (horizontal/vertical), no diagonal boundaries  
B) ✗ Grid-based methods are scalable and efficient for large datasets  
C) ✗ Do not require specifying number of clusters in advance  
D) ✗ Can handle high-dimensional data but may suffer from curse of dimensionality  

**Correct:** A


#### 14. How does CLIQUE differ from other grid-based methods?  
A) ✓ Automatically identifies subspaces with dense clusters in high-dimensional data  
B) ✓ Partitions each dimension into equal-length intervals  
C) ✗ Does not require user-specified cluster shapes; discovers automatically  
D) ✓ Uses apriori principle to prune candidate dense cells efficiently  

**Correct:** A, B, D


#### 15. Which of the following statements about cluster evaluation are correct?  
A) ✓ Hopkins statistic tests for spatial randomness vs clustering tendency  
B) ✓ Elbow method uses within-cluster variance to find optimal k  
C) ✗ Silhouette coefficient is intrinsic and does not require ground truth labels  
D) ✓ Cross-validation can be used to select k by testing model fit on held-out data  

**Correct:** A, B, D


#### 16. Which criteria are essential for a good clustering quality measure?  
A) ✓ Cluster homogeneity: clusters should be pure  
B) ✓ Cluster completeness: all members of a class should be in one cluster  
C) ✗ Splitting large clusters is less harmful than splitting small clusters (opposite is true)  
D) ✓ Penalize placing heterogeneous objects into pure clusters more than rag bag clusters  

**Correct:** A, B, D


#### 17. What are the main differences between partitioning and hierarchical clustering methods?  
A) ✓ Partitioning requires k as input; hierarchical does not  
B) ✓ Hierarchical produces nested clusters; partitioning produces flat clusters  
C) ✗ Partitioning methods generally find convex clusters; hierarchical can find arbitrary shapes depending on linkage  
D) ✗ Hierarchical methods cannot undo merges or splits  

**Correct:** A, B


#### 18. Which of the following statements about BIRCH are true?  
A) ✓ BIRCH incrementally builds a CF-tree summarizing cluster statistics  
B) ✓ BIRCH scales linearly with number of data points due to single scan approach  
C) ✗ BIRCH handles numeric data only, not categorical natively  
D) ✓ Sensitive to insertion order because CF-tree depends on data order  

**Correct:** A, B, D


#### 19. In the context of clustering, what is a medoid?  
A) ✗ Mean point is centroid, not medoid  
B) ✓ Medoid is the most centrally located actual data point in a cluster  
C) ✗ Medoid is an actual data point, not synthetic  
D) ✗ Medoid is central, not farthest point  

**Correct:** B


#### 20. Which of the following are challenges in cluster analysis?  
A) ✓ Scalability to large datasets is a major challenge  
B) ✓ Handling mixed data types (numeric, categorical, ordinal) is difficult  
C) ✓ Discovering clusters with arbitrary shapes requires advanced methods  
D) ✗ Clusters are not always convex or spherical; many methods struggle with non-convex shapes  

**Correct:** A, B, C