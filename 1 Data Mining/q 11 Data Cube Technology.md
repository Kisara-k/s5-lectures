## 11. Data Cube Technology

## Questions

#### 1. What does a data cube primarily represent in multidimensional data analysis?  
A) A flat table with aggregated data for one dimension  
B) A lattice of cuboids representing aggregates at different dimension combinations  
C) A single aggregate value for all dimensions combined  
D) A hierarchical tree of raw data records  


#### 2. Which of the following statements about iceberg cubes is true?  
A) Iceberg cubes compute all possible aggregate cells regardless of measure values  
B) Iceberg cubes only compute cells whose measure values meet a minimum threshold  
C) Iceberg cubes reduce computation by pruning cells below the threshold early  
D) Iceberg cubes always contain fewer cells than closed cubes  


#### 3. In the context of data cubes, what is a "closed cell"?  
A) A cell that has no ancestor with the same measure value  
B) A cell that has no descendant with the same measure value  
C) A cell that contains the maximum measure value in the cube  
D) A cell that is part of the base cuboid only  


#### 4. Which of the following is NOT a benefit of using cube shells?  
A) Reducing pre-computation by focusing on low-dimensional cuboids  
B) Allowing on-the-fly computation of other cuboids from shells  
C) Eliminating the need for any online computation  
D) Managing storage by limiting the number of precomputed cuboids  


#### 5. Why is the full data cube often impractical to compute for high-dimensional data?  
A) Because the number of base cells grows exponentially with dimensions  
B) Because the number of aggregate cells grows exponentially with dimensions  
C) Because measures cannot be aggregated across multiple dimensions  
D) Because the data cube lattice becomes disconnected  


#### 6. Which of the following best describes the Bottom-Up Multi-Way Array Aggregation method?  
A) It starts from the apex cuboid and aggregates downward  
B) It partitions the cube into chunks and aggregates from base cuboid upward  
C) It prunes partitions that do not meet minimum support early  
D) It uses inverted indices to speed up aggregation  


#### 7. What is a key limitation of the Bottom-Up Multi-Way Array Aggregation method?  
A) It cannot compute full cubes for small dimensions efficiently  
B) It does not support iceberg pruning to skip low-value cells  
C) It requires all data to fit in main memory at once  
D) It cannot reuse intermediate aggregates  


#### 8. The BUC algorithm is often described as "top-down" in some contexts. What is the main reason for this?  
A) It starts aggregation from the base cuboid and moves upward  
B) It starts from the apex cuboid and recursively partitions dimensions  
C) It uses bottom-up array aggregation internally  
D) It does not support iceberg pruning  


#### 9. How does the shell-fragment approach help in handling high-dimensional OLAP?  
A) By computing the full cube offline for all dimensions  
B) By dividing dimensions into smaller groups and precomputing cubes for each  
C) By ignoring dimensions with low cardinality  
D) By storing only the apex cuboid and computing others on demand  


#### 10. When combining shell fragments online to answer a query, what is the main operation performed?  
A) Union of tuple ID lists from each fragment  
B) Intersection of tuple ID lists from each fragment  
C) Cartesian product of all fragment cuboids  
D) Aggregation of measures without considering tuple IDs  


#### 11. Which of the following is true about the relationship between ancestor and descendant cells in a data cube?  
A) An ancestor cell is more detailed than a descendant cell  
B) A descendant cell aggregates data from its ancestor cell  
C) An ancestor cell aggregates data from its descendant cells  
D) Descendant cells always have fewer dimensions than ancestor cells  


#### 12. What is the main challenge addressed by iceberg cubes compared to full cubes?  
A) Reducing the number of dimensions in the cube  
B) Avoiding computation and storage of insignificant aggregate cells  
C) Increasing the number of base cells to improve accuracy  
D) Ensuring all possible aggregates are computed regardless of value  


#### 13. Which of the following statements about closed cubes is correct?  
A) Closed cubes contain all cells with measure values above a threshold  
B) Closed cubes exclude cells that have descendants with the same measure value  
C) Closed cubes are always smaller than iceberg cubes  
D) Closed cubes only store base cuboid cells  


#### 14. In the context of cube computation, what is the purpose of "share-sorts" and "share-partitions"?  
A) To share sorting and partitioning costs across multiple cuboids  
B) To reduce the number of dimensions in the cube  
C) To increase the number of cuboids computed simultaneously  
D) To avoid caching intermediate results  


#### 15. Which of the following is NOT a typical step in the BUC algorithm?  
A) Sorting distinct values of each dimension  
B) Partitioning data into blocks that fit in memory  
C) Pruning partitions that do not meet minimum support  
D) Computing all cuboids simultaneously in one pass  


#### 16. Why is the curse of dimensionality a problem for traditional data cube computation methods?  
A) Because the number of tuples grows exponentially with dimensions  
B) Because the number of cuboids grows exponentially with dimensions  
C) Because measures cannot be aggregated in high dimensions  
D) Because data cubes cannot be visualized beyond three dimensions  


#### 17. What is the main advantage of using inverted indices in shell-fragment cubing?  
A) They reduce the number of dimensions needed in the cube  
B) They allow fast intersection of tuple ID lists to reconstruct high-dimensional aggregates  
C) They eliminate the need for offline precomputation  
D) They compress the base cuboid into a single aggregate  


#### 18. In multi-feature cubes, what is a key characteristic of the queries they support?  
A) They only compute simple aggregates like sum or count  
B) They compute multiple dependent aggregates at multiple granularities simultaneously  
C) They require pre-aggregation of all possible dimension combinations  
D) They do not support filtering by attribute values  


#### 19. Which of the following best describes "discovery-driven exploration" in data cubes?  
A) Precomputing all possible aggregates for fast querying  
B) Using statistical models to highlight surprising or exceptional cells in the cube  
C) Computing only the apex cuboid and drilling down on demand  
D) Ignoring cells with low measure values to reduce cube size  


#### 20. When computing a data cube, why might one choose to order dimensions by cardinality, skew, or correlation?  
A) To maximize the number of cuboids computed  
B) To encourage pruning and reduce computation cost  
C) To ensure all cuboids have equal size  
D) To avoid computing iceberg cubes



<br>

## Answers

#### 1. What does a data cube primarily represent in multidimensional data analysis?  
A) ✗ A flat table with aggregated data for one dimension only; data cube involves multiple dimensions.  
B) ✓ A lattice of cuboids representing aggregates at different dimension combinations; this is the core concept.  
C) ✗ A single aggregate value; data cube contains many aggregates at various granularities.  
D) ✗ A hierarchical tree of raw data records; data cube stores aggregates, not raw data hierarchy.  

**Correct:** B


#### 2. Which of the following statements about iceberg cubes is true?  
A) ✗ Iceberg cubes do not compute all cells; they prune low-value cells.  
B) ✓ Iceberg cubes compute only cells meeting a minimum measure threshold.  
C) ✓ Iceberg cubes prune cells below threshold early to save computation.  
D) ✗ Iceberg cubes may be smaller but not always smaller than closed cubes; depends on data.  

**Correct:** B, C


#### 3. In the context of data cubes, what is a "closed cell"?  
A) ✗ Closed cell relates to descendants, not ancestors.  
B) ✓ Closed cell has no descendant with the same measure value; this avoids redundancy.  
C) ✗ Closed cell is not necessarily the maximum value cell.  
D) ✗ Closed cells can be at any cuboid level, not just base cuboid.  

**Correct:** B


#### 4. Which of the following is NOT a benefit of using cube shells?  
A) ✗ Reducing pre-computation by focusing on low-dimensional cuboids is a benefit.  
B) ✗ Allowing on-the-fly computation of other cuboids from shells is a benefit.  
C) ✓ Eliminating the need for any online computation is false; shells reduce precomputation but require some online computation.  
D) ✗ Managing storage by limiting precomputed cuboids is a benefit.  

**Correct:** C


#### 5. Why is the full data cube often impractical to compute for high-dimensional data?  
A) ✗ Number of base cells grows linearly or polynomially, not exponentially, with dimensions.  
B) ✓ Number of aggregate cells grows exponentially with dimensions, causing explosion.  
C) ✗ Measures can be aggregated across dimensions; this is not a limitation.  
D) ✗ The cube lattice remains connected; this is not a problem.  

**Correct:** B


#### 6. Which of the following best describes the Bottom-Up Multi-Way Array Aggregation method?  
A) ✗ It starts from the base cuboid, not apex.  
B) ✓ It partitions the cube into chunks and aggregates from base cuboid upward.  
C) ✗ It does not prune partitions early; no iceberg pruning.  
D) ✗ It does not use inverted indices; that is for shell-fragment methods.  

**Correct:** B


#### 7. What is a key limitation of the Bottom-Up Multi-Way Array Aggregation method?  
A) ✗ It is efficient for small dimensions.  
B) ✓ It does not support iceberg pruning, so cannot skip low-value cells early.  
C) ✗ It partitions data into chunks to fit memory; does not require all data at once.  
D) ✗ It reuses intermediate aggregates to improve efficiency.  

**Correct:** B


#### 8. The BUC algorithm is often described as "top-down" in some contexts. What is the main reason for this?  
A) ✗ It does not start from base cuboid upward.  
B) ✓ It starts from apex cuboid and recursively partitions dimensions downward.  
C) ✗ It is not a bottom-up array aggregation method.  
D) ✗ It supports iceberg pruning, which is a key feature.  

**Correct:** B


#### 9. How does the shell-fragment approach help in handling high-dimensional OLAP?  
A) ✗ It does not compute the full cube offline for all dimensions.  
B) ✓ It divides dimensions into smaller groups and precomputes cubes for each fragment.  
C) ✗ It does not ignore low cardinality dimensions arbitrarily.  
D) ✗ It stores multiple cuboids, not just apex cuboid.  

**Correct:** B


#### 10. When combining shell fragments online to answer a query, what is the main operation performed?  
A) ✗ Union would overcount tuples; not correct.  
B) ✓ Intersection of tuple ID lists is used to find tuples common to all fragments.  
C) ✗ Cartesian product would explode data size unnecessarily.  
D) ✗ Aggregation requires tuple IDs to correctly combine fragments.  

**Correct:** B


#### 11. Which of the following is true about the relationship between ancestor and descendant cells in a data cube?  
A) ✗ Ancestor cells are more aggregated, less detailed.  
B) ✗ Descendant cells are more detailed and aggregate to ancestor cells, not vice versa.  
C) ✓ Ancestor cells aggregate data from descendant cells.  
D) ✗ Descendant cells have equal or more dimensions, not fewer.  

**Correct:** C


#### 12. What is the main challenge addressed by iceberg cubes compared to full cubes?  
A) ✗ Iceberg cubes do not reduce dimensions.  
B) ✓ Iceberg cubes avoid computing and storing insignificant aggregate cells.  
C) ✗ Iceberg cubes do not increase base cells.  
D) ✗ Iceberg cubes do not compute all aggregates regardless of value.  

**Correct:** B


#### 13. Which of the following statements about closed cubes is correct?  
A) ✗ Closed cubes do not necessarily include all cells above a threshold.  
B) ✓ Closed cubes exclude cells that have descendants with the same measure value.  
C) ✗ Closed cubes are not always smaller than iceberg cubes; depends on data.  
D) ✗ Closed cubes include cells beyond base cuboid.  

**Correct:** B


#### 14. In the context of cube computation, what is the purpose of "share-sorts" and "share-partitions"?  
A) ✓ To share sorting and partitioning costs across multiple cuboids, improving efficiency.  
B) ✗ They do not reduce the number of dimensions.  
C) ✗ They do not increase the number of cuboids computed.  
D) ✗ They encourage caching intermediate results, not avoid it.  

**Correct:** A


#### 15. Which of the following is NOT a typical step in the BUC algorithm?  
A) ✗ Sorting distinct values is a step.  
B) ✗ Partitioning data into memory-fitting blocks is a step.  
C) ✗ Pruning partitions below minimum support is a step.  
D) ✓ Computing all cuboids simultaneously in one pass is NOT done; BUC is recursive and partitioned.  

**Correct:** D


#### 16. Why is the curse of dimensionality a problem for traditional data cube computation methods?  
A) ✗ Number of tuples does not necessarily grow exponentially with dimensions.  
B) ✓ Number of cuboids grows exponentially with dimensions, causing explosion.  
C) ✗ Measures can be aggregated in high dimensions.  
D) ✗ Visualization is a challenge but not the main computational problem.  

**Correct:** B


#### 17. What is the main advantage of using inverted indices in shell-fragment cubing?  
A) ✗ They do not reduce the number of dimensions.  
B) ✓ They allow fast intersection of tuple ID lists to reconstruct high-dimensional aggregates efficiently.  
C) ✗ They do not eliminate offline precomputation; they support it.  
D) ✗ They do not compress base cuboid into a single aggregate.  

**Correct:** B


#### 18. In multi-feature cubes, what is a key characteristic of the queries they support?  
A) ✗ They support complex aggregates, not just simple ones.  
B) ✓ They compute multiple dependent aggregates at multiple granularities simultaneously.  
C) ✗ They do not require pre-aggregation of all dimension combinations necessarily.  
D) ✗ They support filtering by attribute values (e.g., max price tuples).  

**Correct:** B


#### 19. Which of the following best describes "discovery-driven exploration" in data cubes?  
A) ✗ Precomputing all aggregates is standard cubing, not discovery-driven.  
B) ✓ Using statistical models to highlight surprising or exceptional cells guides analysis.  
C) ✗ Computing only apex cuboid is insufficient for exploration.  
D) ✗ Ignoring low-value cells is iceberg pruning, not discovery-driven exploration.  

**Correct:** B


#### 20. When computing a data cube, why might one choose to order dimensions by cardinality, skew, or correlation?  
A) ✗ Maximizing cuboids computed is not the goal.  
B) ✓ Ordering encourages pruning and reduces computation cost by early elimination of partitions.  
C) ✗ Cuboids rarely have equal size; ordering is for efficiency, not equal sizing.  
D) ✗ Ordering does not avoid iceberg cubes; it complements pruning strategies.  

**Correct:** B