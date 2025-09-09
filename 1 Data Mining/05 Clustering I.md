## 5. Clustering I

## Key Points

#### 1. 🧩 Cluster Analysis Basics  
- A cluster is a group of data objects similar within the group and dissimilar to objects in other groups.  
- Clustering is an unsupervised learning method with no predefined classes.  
- Good clustering has high intra-class similarity and low inter-class similarity.  
- Similarity is typically measured using distance functions, which vary by data type (numerical, categorical, ordinal, etc.).  
- Clustering applications include biology (taxonomy), information retrieval, marketing segmentation, city planning, and earthquake studies.  

#### 2. 🔢 Partitioning Methods  
- Partitioning methods divide data into $k$ clusters by minimizing the sum of squared distances to cluster centers.  
- K-means represents clusters by centroids (mean points) and iteratively assigns points to nearest centroids until convergence.  
- K-medoids (PAM) represents clusters by medoids (actual data points) and is more robust to noise and outliers than k-means.  
- K-means is efficient with time complexity $O(tkn)$, but sensitive to outliers and requires numeric data.  
- K-medoids is computationally expensive and better for small datasets; CLARA and CLARANS improve its scalability.  
- Variants include k-modes (categorical data) and k-prototypes (mixed data).  

#### 3. 🌳 Hierarchical Clustering  
- Hierarchical clustering builds a dendrogram representing nested clusters without needing $k$ upfront.  
- Agglomerative (AGNES) starts with single points and merges clusters based on minimum dissimilarity.  
- Divisive (DIANA) starts with one cluster and splits it until each point is alone.  
- Cluster distance measures include single link (min distance), complete link (max distance), average link, centroid, and medoid distances.  
- Centroid = mean of cluster points; radius = average distance to centroid; diameter = average distance between all pairs.  
- Hierarchical methods have time complexity at least $O(n^2)$ and cannot undo merges or splits.  

#### 4. 🌲 Advanced Hierarchical Methods: BIRCH and CHAMELEON  
- BIRCH builds a CF-tree summarizing data with Clustering Features (N, LS, SS) for scalable clustering.  
- BIRCH processes data in one scan, is efficient ($O(n)$), but sensitive to insertion order and only handles numeric data.  
- CHAMELEON uses a dynamic model merging clusters based on relative interconnectivity and closeness, better for arbitrary shapes.  
- CHAMELEON uses graph partitioning to create sub-clusters, then agglomerative merging.  

#### 5. 📏 Clustering Quality and Considerations  
- Good clustering maximizes intra-cluster similarity and minimizes inter-cluster similarity.  
- Quality depends on similarity/distance metrics and cluster cohesion/separation measures.  
- Clustering can be exclusive (one object per cluster) or non-exclusive (objects in multiple clusters).  
- Similarity measures can be distance-based (Euclidean) or connectivity-based (density).  
- Challenges include scalability, handling mixed data types, noise, outliers, high dimensionality, and interpretability.  
- Constraint-based clustering incorporates user/domain knowledge to guide clustering.



<br>

## Study Notes

### 1. 🧩 Introduction to Cluster Analysis: Basic Concepts

Cluster analysis is a fundamental technique in data mining and machine learning used to group a set of data objects into subsets or **clusters**. The goal is to ensure that objects within the same cluster are **similar** to each other, while objects in different clusters are **dissimilar**. This process is also called **clustering** or **data segmentation**.

#### What is a Cluster?

A **cluster** is a collection of data points that share high similarity or relatedness within the group but are quite different from points in other groups. For example, in customer data, a cluster might represent a group of customers with similar buying habits.

#### What is Cluster Analysis?

Cluster analysis is the process of partitioning a dataset into groups (clusters) such that:

- Objects in the same cluster are **similar**.
- Objects in different clusters are **dissimilar**.

This is an example of **unsupervised learning**, meaning there are no predefined labels or classes. The algorithm learns patterns purely from the data itself, without any prior examples.

#### Why Use Clustering?

Clustering is widely used for:

- **Data understanding**: To explore and summarize data.
- **Preprocessing**: To prepare data for other algorithms like classification or regression.
- **Applications**:
  - **Biology**: Classifying species into taxonomic groups.
  - **Information retrieval**: Grouping similar documents.
  - **Land use**: Identifying regions with similar land characteristics.
  - **Marketing**: Segmenting customers for targeted campaigns.
  - **City planning**: Grouping houses by type or location.
  - **Earthquake studies**: Clustering epicenters along fault lines.

#### Clustering as a Preprocessing Tool

Clustering can help in:

- **Summarization**: Reducing data complexity before applying other algorithms.
- **Compression**: For example, vector quantization in image processing.
- **Finding nearest neighbors**: Localizing search to relevant clusters.
- **Outlier detection**: Identifying data points that do not belong to any cluster.

#### What Makes a Good Clustering?

A good clustering method produces:

- **High intra-class similarity**: Objects within a cluster are very similar.
- **Low inter-class similarity**: Clusters are well separated from each other.

The quality depends on:

- The **similarity measure** used.
- The **algorithm’s implementation**.
- The ability to discover meaningful patterns.

#### Measuring Similarity

Similarity is often measured using a **distance function** (e.g., Euclidean distance). Different types of data (numerical, categorical, ordinal) require different distance measures. Sometimes, weights are assigned to variables based on their importance.

#### Challenges in Clustering

- **Scalability**: Handling large datasets efficiently.
- **Data types**: Dealing with numerical, categorical, or mixed data.
- **Constraints**: Incorporating domain knowledge or user constraints.
- **Interpretability**: Making clusters understandable.
- **Arbitrary shapes**: Detecting clusters of any shape.
- **Noise and outliers**: Handling data imperfections.
- **High dimensionality**: Managing many features.


### 2. 🔢 Partitioning Methods: Dividing Data into Clusters

Partitioning methods divide the dataset into **k clusters** by optimizing a criterion, usually minimizing the sum of squared distances between points and their cluster centers.

#### Basic Idea

Given:

- A dataset $D$ with $n$ objects.
- A number $k$ (number of clusters).

The goal is to partition $D$ into $k$ clusters $C_1, C_2, ..., C_k$ such that the total within-cluster variance (sum of squared distances to cluster centers) is minimized.

#### Global vs. Heuristic Solutions

- **Global optimal**: Enumerate all possible partitions (impractical for large data).
- **Heuristic methods**: Efficient algorithms that find good (but not always optimal) solutions.

#### K-Means Algorithm

One of the most popular partitioning methods.

**How it works:**

1. **Initialize**: Choose $k$ initial centroids (seed points).
2. **Assign**: Assign each data point to the nearest centroid.
3. **Update**: Recalculate centroids as the mean of points in each cluster.
4. **Repeat**: Steps 2 and 3 until assignments no longer change.

**Key points:**

- Centroid = mean point of the cluster.
- Efficient: Time complexity $O(tkn)$, where $t$ = iterations, $k$ = clusters, $n$ = points.
- Sensitive to initial centroids and outliers.
- Works only with numerical data.
- Assumes clusters are convex and roughly spherical.

#### K-Medoids Algorithm (PAM)

An alternative to k-means that is more robust to noise and outliers.

- Instead of centroids, clusters are represented by **medoids** — actual data points that are most centrally located.
- The algorithm iteratively swaps medoids with non-medoids to reduce total cost (sum of distances).
- More computationally expensive than k-means.
- Can handle arbitrary distance metrics and categorical data.

#### Variations of K-Means

- **K-modes**: For categorical data, replaces means with modes.
- **K-prototypes**: For mixed numerical and categorical data.
- Different initialization and distance calculation strategies.

#### Limitations of Partitioning Methods

- Need to specify $k$ in advance.
- Sensitive to outliers.
- Not suitable for clusters with complex shapes.
- May converge to local optima.


### 3. 🌳 Hierarchical Clustering: Building a Tree of Clusters

Hierarchical clustering creates a **tree-like structure** (called a **dendrogram**) that represents nested groupings of data points at different levels of similarity.

#### Two Main Types

- **Agglomerative (bottom-up)**: Start with each object as its own cluster, then iteratively merge the closest clusters.
- **Divisive (top-down)**: Start with all objects in one cluster, then iteratively split clusters.

#### Agglomerative Clustering (AGNES)

- Uses a **distance matrix** to find the closest clusters.
- Merges clusters with the smallest dissimilarity.
- Continues until all points are in one cluster.
- The dendrogram can be cut at any level to get the desired number of clusters.

#### Divisive Clustering (DIANA)

- Opposite of AGNES.
- Starts with one cluster and splits it until each object is alone.
- Also produces a dendrogram.

#### Distance Between Clusters

Several ways to measure distance between clusters:

- **Single link**: Minimum distance between any two points in the clusters.
- **Complete link**: Maximum distance between any two points.
- **Average link**: Average distance between all pairs of points.
- **Centroid link**: Distance between cluster centroids.
- **Medoid link**: Distance between cluster medoids.

#### Cluster Properties

- **Centroid**: The mean point of a cluster.
- **Radius**: Average distance from points to centroid.
- **Diameter**: Average distance between all pairs of points in the cluster.

#### Strengths and Weaknesses

- Does not require specifying $k$ upfront.
- Can capture nested cluster structures.
- Computationally expensive: $O(n^2)$ or worse.
- Once merged or split, cannot undo decisions.
- Sensitive to noise and outliers.


### 4. 🌲 Advanced Hierarchical Methods: BIRCH and CHAMELEON

To address scalability and flexibility issues in hierarchical clustering, advanced methods like **BIRCH** and **CHAMELEON** were developed.

#### BIRCH (Balanced Iterative Reducing and Clustering Using Hierarchies)

- Designed for large datasets.
- Builds a **CF-tree** (Clustering Feature tree), a compact summary of the data.
- Two phases:
  1. Scan data to build CF-tree (multi-level compression).
  2. Apply another clustering algorithm on leaf nodes.
- CF vector stores:
  - $N$: Number of points.
  - $LS$: Linear sum of points.
  - $SS$: Square sum of points.
- Efficient: Processes each point once, $O(n)$.
- Limitations:
  - Only works with numerical data.
  - Sensitive to insertion order.
  - Clusters tend to be spherical.

#### CHAMELEON

- Uses a **dynamic model** to measure similarity.
- Merges clusters only if their **interconnectivity** and **closeness** are high relative to internal cluster properties.
- Two-phase approach:
  1. Graph partitioning to create many small sub-clusters.
  2. Agglomerative merging of sub-clusters based on dynamic criteria.
- Better at discovering clusters with complex shapes.
- More computationally intensive.


### 5. 📏 Evaluating Clustering Quality and Considerations

#### What Makes Clustering Good?

- **High intra-cluster similarity**: Points in the same cluster are close.
- **Low inter-cluster similarity**: Clusters are well separated.

#### Measuring Quality

- Use **distance/similarity metrics** appropriate for data type.
- Use **quality functions** to measure cluster cohesion and separation.
- Often subjective and depends on the application.

#### Important Considerations

- **Partitioning criteria**: Single-level vs. hierarchical.
- **Cluster exclusivity**: Whether objects belong to one or multiple clusters.
- **Similarity measure**: Distance-based vs. connectivity-based.
- **Clustering space**: Full feature space vs. subspaces (important in high dimensions).
- **Scalability**: Ability to handle large datasets.
- **Data types**: Numerical, categorical, mixed.
- **Constraints**: Incorporating domain knowledge.
- **Interpretability**: Making results understandable.
- **Noise and outliers**: Robustness.
- **Cluster shapes**: Ability to find arbitrary shapes.
- **Incremental clustering**: Handling streaming data or updates.


### Summary

Clustering is a powerful unsupervised learning technique used to group similar data points. The main approaches include:

- **Partitioning methods** (e.g., k-means, k-medoids) that divide data into $k$ clusters by optimizing a criterion.
- **Hierarchical methods** (e.g., AGNES, DIANA) that build nested cluster trees without needing $k$ upfront.
- **Advanced hierarchical methods** like BIRCH and CHAMELEON improve scalability and cluster shape detection.

Each method has strengths and weaknesses, and the choice depends on data type, size, and the specific application. Understanding these methods and their evaluation is crucial for applying clustering effectively in real-world problems.