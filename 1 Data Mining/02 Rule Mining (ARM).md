## 2. Rule Mining (ARM)

## Key Points

#### 1. 🔑 Frequent Pattern and Association Rule Basics  
- A *frequent pattern* is a set of items or subsequences that appear frequently in a dataset.  
- An *association rule* is an implication of the form X → Y, where X and Y are itemsets with no overlap.  
- **Support** is the probability that a transaction contains X ∪ Y.  
- **Confidence** is the conditional probability that a transaction containing X also contains Y, calculated as Support(X ∪ Y) / Support(X).  
- The *downward closure property* states that all subsets of a frequent itemset must also be frequent.

#### 2. ⚙️ Apriori Algorithm  
- Apriori uses candidate generation and test: it generates candidate (k+1)-itemsets from frequent k-itemsets and prunes candidates if any subset is infrequent.  
- Apriori requires multiple scans of the database to count support for candidates.  
- The algorithm terminates when no new frequent itemsets can be generated.  
- Candidate generation involves self-joining frequent itemsets and pruning candidates whose subsets are not frequent.

#### 3. 🌲 FP-Growth Algorithm  
- FP-Growth avoids candidate generation by building an FP-tree, a compressed prefix-tree structure of the database.  
- The FP-tree is constructed by scanning the database twice: first to find frequent 1-itemsets and second to build the tree with items ordered by descending frequency.  
- Mining is done by recursively building conditional FP-trees for each frequent item.  
- FP-Growth is more scalable than Apriori because it compresses data and reduces database scans.

#### 4. 📊 Vertical Data Format Mining  
- Vertical format represents itemsets with tid-lists (transaction ID lists) showing which transactions contain the itemset.  
- Frequent itemsets are found by intersecting tid-lists.  
- Diffsets track differences in tid-lists to speed up mining.  
- Algorithms like Eclat and CHARM use vertical data formats.

#### 5. 🧩 Types of Association Rules  
- Multi-level association rules consider item hierarchies with different support thresholds at each level.  
- Multi-dimensional association rules involve multiple attributes or predicates (e.g., age and occupation).  
- Quantitative association rules handle numeric attributes using discretization or clustering.

#### 6. 📈 Interestingness Measures  
- Lift measures the correlation between itemsets: Lift(X → Y) = Confidence(X → Y) / Support(Y).  
- Lift > 1 indicates positive correlation; Lift < 1 indicates negative correlation.  
- Support and confidence alone can be misleading without considering lift.

#### 7. 🎯 Constraint-Based Mining  
- Constraint-based mining allows users to specify constraints (e.g., on support, confidence, item attributes) to focus mining on relevant patterns.  
- Constraints can be on knowledge type, data attributes, dimensions, rules, or interestingness measures.  
- This approach reduces the number of patterns and improves mining efficiency.

#### 8. 🛠️ Challenges and Solutions in Frequent Pattern Mining  
- Challenges include multiple database scans, large candidate sets, and expensive support counting.  
- Solutions include partitioning the database, sampling, FP-growth, and vertical data formats to reduce scans and candidate generation.



<br>

## Study Notes

### 1. 🔍 Introduction to Rule Mining and Frequent Pattern Analysis

**What is Rule Mining (ARM)?**  
Rule Mining, also known as Association Rule Mining (ARM), is a fundamental technique in data mining focused on discovering interesting relationships, patterns, or associations among large sets of data items. The goal is to find rules that highlight how items or events co-occur frequently in a dataset.

**Frequent Pattern Analysis** is the core of ARM. A *frequent pattern* is any set of items, subsequences, or substructures that appear often enough in the data. For example, in a supermarket database, a frequent pattern might be that customers often buy bread and butter together.

**Why is this important?**  
Frequent pattern mining reveals intrinsic regularities in data, which can be used for various applications such as:

- Market basket analysis (e.g., discovering that beer and diapers are often bought together)
- Cross-marketing and catalog design
- Web log analysis (understanding user click patterns)
- DNA sequence analysis (finding patterns related to drug sensitivity)
- Classification and clustering based on frequent patterns

This analysis forms the foundation for many other data mining tasks like correlation analysis, sequential pattern mining, and associative classification.


### 2. 📚 Basic Concepts: Frequent Patterns and Association Rules

**Itemsets and Rules**  
- An *itemset* is a collection of one or more items, e.g., {milk, bread}.  
- An *association rule* is an implication of the form X → Y, where X and Y are itemsets and X ∩ Y = ∅. For example, {diaper} → {beer} means if a customer buys diapers, they are likely to buy beer as well.

**Key Metrics: Support and Confidence**  
- **Support (s):** The proportion (or count) of transactions in the database that contain the itemset X ∪ Y. It measures how frequently the itemset appears in the data.  
- **Confidence (c):** The conditional probability that a transaction containing X also contains Y. It measures the strength of the rule X → Y.

Mathematically:  
- Support(X → Y) = P(X ∪ Y)  
- Confidence(X → Y) = P(Y | X) = Support(X ∪ Y) / Support(X)

**Example:**  
If 50% of transactions contain both diapers and beer, and 60% contain diapers, then the confidence of the rule {diaper} → {beer} is 50% / 60% = 83.3%.


### 3. ⚙️ Scalable Methods for Mining Frequent Patterns

Mining frequent patterns efficiently is challenging because datasets can be huge, and the number of possible itemsets grows exponentially with the number of items.

#### The Downward Closure Property  
This property states that *any subset of a frequent itemset must also be frequent*. For example, if {beer, diaper, nuts} is frequent, then {beer, diaper} must also be frequent. This property helps prune the search space.

#### Three Major Approaches to Frequent Pattern Mining:

1. **Apriori Algorithm (Candidate Generation and Test)**  
   - Proposed by Agrawal & Srikant (1994).  
   - Works in iterative passes over the database.  
   - First, find frequent 1-itemsets by scanning the database.  
   - Then generate candidate 2-itemsets from frequent 1-itemsets, test their support by scanning the database again.  
   - Repeat for k-itemsets until no more frequent itemsets are found.  
   - Uses the Apriori pruning principle: if any subset of an itemset is infrequent, the itemset itself cannot be frequent, so it is pruned early.

2. **FP-Growth (Frequent Pattern Growth)**  
   - Proposed by Han, Pei & Yin (2000).  
   - Avoids candidate generation by building a compact data structure called an FP-tree.  
   - The FP-tree stores the database in a compressed form, preserving itemset frequency information.  
   - Mining is done by recursively building conditional FP-trees for frequent items, enabling efficient pattern growth.

3. **Vertical Data Format Approach**  
   - Uses a vertical representation of data where each itemset is associated with a list of transaction IDs (tid-list) containing it.  
   - Frequent itemsets are found by intersecting tid-lists.  
   - Algorithms like Eclat and CHARM use this approach.  
   - Diffsets (tracking differences in tid-lists) can speed up mining.


### 4. 🛠️ The Apriori Algorithm in Detail

Apriori is a classic and intuitive algorithm for mining frequent itemsets:

- **Step 1:** Scan the database once to find all frequent 1-itemsets (items with support above the minimum threshold).  
- **Step 2:** Generate candidate 2-itemsets by joining frequent 1-itemsets.  
- **Step 3:** Scan the database again to count support for these candidates.  
- **Step 4:** Prune candidates that do not meet the minimum support.  
- **Step 5:** Repeat the process for k-itemsets until no new frequent itemsets are found.

**Candidate Generation:**  
- Join step: Combine frequent k-itemsets to form (k+1)-itemset candidates.  
- Prune step: Remove candidates if any of their subsets are not frequent.

**Challenges:**  
- Multiple database scans are expensive.  
- Huge number of candidates can be generated, leading to high computational cost.  
- Counting support for candidates is tedious.

**Improvements:**  
- Partitioning the database to reduce scans.  
- Sampling the database to find candidates in a smaller subset.  
- Using vertical data formats or FP-growth to avoid candidate generation.


### 5. 🌲 FP-Growth: Mining Frequent Patterns Without Candidate Generation

FP-Growth is a more efficient alternative to Apriori:

- **Step 1:** Scan the database once to find frequent 1-itemsets and sort them in descending order of frequency (called the f-list).  
- **Step 2:** Scan the database again to build an FP-tree, a prefix-tree structure that compresses the database by sharing common prefixes of transactions.  
- **Step 3:** Recursively mine the FP-tree by constructing conditional FP-trees for each frequent item and extracting frequent patterns.

**Benefits of FP-tree:**  
- Preserves complete information for mining without losing any frequent patterns.  
- Compresses the database by removing infrequent items and sharing prefixes.  
- Avoids candidate generation and multiple database scans.  
- Enables a divide-and-conquer approach, focusing on smaller conditional databases.


### 6. 📈 Mining Various Types of Association Rules

Association rules can be extended beyond simple itemsets:

- **Multi-level Association Rules:**  
  Items can be organized in hierarchies (e.g., milk → skim milk). Different support thresholds can be applied at different levels because lower-level items tend to be less frequent.  
  Redundancy filtering is important to avoid reporting rules that are just more specific versions of others.

- **Multi-dimensional Association Rules:**  
  Rules involving multiple attributes or dimensions, such as age, occupation, and purchase behavior.  
  Example: age(19-25) ∧ occupation(student) → buys(coke).

- **Quantitative Association Rules:**  
  Deals with numeric attributes like age or income. Techniques include discretization (dividing numeric values into intervals) and clustering to find meaningful numeric ranges that form association rules.


### 7. 📊 Interestingness Measures and Correlation

Support and confidence alone can be misleading. For example, a rule might have high confidence but actually be less interesting if the consequent is very common.

**Lift** is a measure of correlation between itemsets:  
- Lift(X → Y) = Confidence(X → Y) / Support(Y)  
- Lift > 1 indicates positive correlation (X and Y occur together more than expected by chance).  
- Lift < 1 indicates negative correlation.

Lift helps identify truly interesting and dependent associations beyond just frequency.


### 8. 🎯 Constraint-Based (Query-Directed) Mining

Mining all possible patterns autonomously is often impractical because:

- The number of patterns can be enormous.  
- Many patterns may be irrelevant or uninteresting.

**Constraint-based mining** allows users to specify constraints or queries to focus the mining process on relevant patterns. Constraints can be:

- **Knowledge type constraints:** e.g., only association rules or classification rules.  
- **Data constraints:** e.g., only items sold in Chicago in December.  
- **Dimension/level constraints:** e.g., only rules involving certain product categories.  
- **Rule constraints:** e.g., rules where the consequent has high sales.  
- **Interestingness constraints:** e.g., minimum support and confidence thresholds.

This approach makes mining interactive and efficient by pruning irrelevant patterns early.


### 9. 📝 Summary of Frequent Pattern Mining

- Frequent pattern mining is a key task in data mining, uncovering important regularities in data.  
- Apriori is a foundational algorithm based on candidate generation and pruning but can be inefficient for large datasets.  
- FP-Growth improves efficiency by compressing data and avoiding candidate generation.  
- Vertical data formats and diffsets offer alternative efficient mining methods.  
- Association rules can be extended to multi-level, multi-dimensional, and quantitative domains.  
- Interestingness measures like lift help identify meaningful patterns.  
- Constraint-based mining focuses the search and improves usability.