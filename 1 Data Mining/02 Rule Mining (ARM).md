## 02 Rule Mining (ARM)

[Study Notes](#study-notes)

[Questions](#questions)



### Key Points



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



<br>

## Questions



#### 1. What does the *downward closure property* in frequent pattern mining imply?  
A) If an itemset is frequent, all its supersets must also be frequent.  
B) If an itemset is infrequent, all its supersets must also be infrequent.  
C) If an itemset is frequent, all its subsets must also be frequent.  
D) If an itemset is infrequent, all its subsets must also be infrequent.


#### 2. Which of the following statements about *support* and *confidence* are true?  
A) Support measures how often an itemset appears in the entire database.  
B) Confidence measures the probability that the antecedent occurs given the consequent.  
C) Confidence is the conditional probability that the consequent occurs given the antecedent.  
D) Support is always greater than or equal to confidence.


#### 3. In the Apriori algorithm, what is the main reason for pruning candidate itemsets?  
A) To reduce the number of database scans.  
B) To eliminate candidates whose subsets are infrequent.  
C) To increase the confidence of the rules generated.  
D) To ensure that only maximal frequent itemsets are generated.


#### 4. Which of the following are advantages of the FP-Growth algorithm over Apriori?  
A) It requires fewer database scans.  
B) It generates candidate itemsets explicitly.  
C) It compresses the database into a compact tree structure.  
D) It uses a vertical data format for faster intersection.


#### 5. When mining multi-level association rules, why is it common to use different minimum support thresholds at different levels?  
A) Because higher-level items tend to be less frequent.  
B) Because lower-level items tend to be less frequent.  
C) To avoid redundancy in rules.  
D) To ensure uniform confidence across levels.


#### 6. Which of the following best describes a *conditional pattern base* in FP-Growth?  
A) The set of all transactions containing a particular item.  
B) The prefix paths in the FP-tree that lead to a given frequent item.  
C) The set of candidate itemsets generated from frequent itemsets.  
D) The list of transaction IDs associated with an itemset.


#### 7. Which of the following challenges are associated with the Apriori algorithm?  
A) Multiple scans of the database.  
B) Large number of candidate itemsets.  
C) Difficulty in generating association rules from frequent itemsets.  
D) Tedious support counting for candidates.


#### 8. In vertical data format mining, what is the main benefit of using *diffsets*?  
A) They reduce the size of transaction ID lists by storing only differences.  
B) They allow mining without scanning the database.  
C) They increase the number of candidates generated.  
D) They speed up support counting by set difference operations.


#### 9. Which of the following statements about *lift* as an interestingness measure are correct?  
A) Lift greater than 1 indicates a positive correlation between itemsets.  
B) Lift equal to 1 means the itemsets are independent.  
C) Lift less than 1 indicates a negative correlation.  
D) Lift is always higher than confidence.


#### 10. Why is constraint-based mining important in association rule mining?  
A) It allows mining all possible patterns autonomously.  
B) It helps focus mining on user-specified relevant patterns.  
C) It reduces computational cost by pruning irrelevant patterns.  
D) It guarantees finding all maximal frequent itemsets.


#### 11. Which of the following are true about multi-dimensional association rules?  
A) They involve only one attribute or dimension.  
B) They can include predicates on multiple attributes like age and occupation.  
C) They can have repeated predicates in hybrid-dimension rules.  
D) They are limited to categorical attributes only.


#### 12. Which of the following are true about quantitative association rules?  
A) They treat numeric attributes by discretization or clustering.  
B) They only apply to categorical data.  
C) Dynamic discretization adjusts intervals based on data distribution.  
D) They cannot handle multi-dimensional data.


#### 13. In the Apriori candidate generation step, which of the following is true?  
A) Candidates are generated by joining frequent (k-1)-itemsets with themselves.  
B) Candidates are pruned if any of their subsets are infrequent.  
C) Candidates are generated randomly to reduce computation.  
D) Candidate generation stops when no frequent itemsets are found.


#### 14. Which of the following statements about FP-tree construction are correct?  
A) Items in each transaction are sorted in ascending order of frequency.  
B) The FP-tree root is labeled with a null value.  
C) Infrequent items are removed before building the FP-tree.  
D) The FP-tree can be larger than the original database.


#### 15. What is the main reason that FP-Growth is considered more scalable than Apriori?  
A) It uses candidate generation to reduce search space.  
B) It compresses the database and avoids candidate generation.  
C) It requires more database scans but fewer candidates.  
D) It uses vertical data format exclusively.


#### 16. Which of the following are true about redundancy filtering in multi-level association rules?  
A) A rule is redundant if its support is close to the expected value based on its ancestor rule.  
B) Redundancy filtering removes all rules with low confidence.  
C) Ancestor rules are more general versions of descendant rules.  
D) Redundancy filtering is unnecessary when using uniform support thresholds.


#### 17. Which of the following statements about sampling in frequent pattern mining are correct?  
A) Sampling reduces the number of database scans to one.  
B) Frequent patterns found in the sample are always frequent in the full database.  
C) Sampling requires a verification scan to confirm frequent itemsets.  
D) Sampling can miss some frequent patterns if the sample is not representative.


#### 18. Which of the following are true about the use of *tid-lists* in vertical data format mining?  
A) Tid-lists store the list of transaction IDs containing an itemset.  
B) Intersection of tid-lists is used to find support of combined itemsets.  
C) Tid-lists are used to generate candidate itemsets in Apriori.  
D) Tid-lists can be used to identify closed frequent itemsets.


#### 19. Which of the following are examples of constraints that can be used in constraint-based mining?  
A) Minimum support and confidence thresholds.  
B) Limiting mining to specific regions or time periods.  
C) Only mining rules with consequents involving high sales.  
D) Automatically mining all possible patterns without user input.


#### 20. Which of the following statements about association rule mining applications are true?  
A) ARM can be used for web clickstream analysis.  
B) ARM is only applicable to market basket data.  
C) ARM can assist in DNA sequence pattern discovery.  
D) ARM cannot be used for classification or clustering tasks.



<br>

## Answers



#### 1. What does the *downward closure property* in frequent pattern mining imply?  
A) ✗ If an itemset is frequent, all its supersets must also be frequent. (Incorrect: supersets can be less frequent.)  
B) ✓ If an itemset is infrequent, all its supersets must also be infrequent. (Correct: infrequent subsets prune supersets.)  
C) ✓ If an itemset is frequent, all its subsets must also be frequent. (Correct: subsets of frequent itemsets are frequent.)  
D) ✗ If an itemset is infrequent, all its subsets must also be infrequent. (Incorrect: subsets can be frequent even if superset is not.)

**Correct:** B, C


#### 2. Which of the following statements about *support* and *confidence* are true?  
A) ✓ Support measures how often an itemset appears in the entire database. (Correct: support is frequency of itemset.)  
B) ✗ Confidence measures the probability that the antecedent occurs given the consequent. (Incorrect: confidence is P(consequent|antecedent).)  
C) ✓ Confidence is the conditional probability that the consequent occurs given the antecedent. (Correct: definition of confidence.)  
D) ✗ Support is always greater than or equal to confidence. (Incorrect: support ≤ confidence or unrelated.)

**Correct:** A, C


#### 3. In the Apriori algorithm, what is the main reason for pruning candidate itemsets?  
A) ✗ To reduce the number of database scans. (Incorrect: pruning reduces candidates, not scans.)  
B) ✓ To eliminate candidates whose subsets are infrequent. (Correct: Apriori pruning principle.)  
C) ✗ To increase the confidence of the rules generated. (Incorrect: pruning is about support, not confidence.)  
D) ✗ To ensure that only maximal frequent itemsets are generated. (Incorrect: Apriori finds all frequent itemsets, not just maximal.)

**Correct:** B


#### 4. Which of the following are advantages of the FP-Growth algorithm over Apriori?  
A) ✓ It requires fewer database scans. (Correct: FP-Growth scans DB twice vs. multiple for Apriori.)  
B) ✗ It generates candidate itemsets explicitly. (Incorrect: FP-Growth avoids candidate generation.)  
C) ✓ It compresses the database into a compact tree structure. (Correct: FP-tree compresses data.)  
D) ✗ It uses a vertical data format for faster intersection. (Incorrect: FP-Growth uses horizontal format.)

**Correct:** A, C


#### 5. When mining multi-level association rules, why is it common to use different minimum support thresholds at different levels?  
A) ✗ Because higher-level items tend to be less frequent. (Incorrect: higher-level items are more general and usually more frequent.)  
B) ✓ Because lower-level items tend to be less frequent. (Correct: specific items appear less often, so lower support is used.)  
C) ✗ To avoid redundancy in rules. (Incorrect: redundancy filtering is separate.)  
D) ✗ To ensure uniform confidence across levels. (Incorrect: confidence is independent of support thresholds.)

**Correct:** B


#### 6. Which of the following best describes a *conditional pattern base* in FP-Growth?  
A) ✗ The set of all transactions containing a particular item. (Incorrect: conditional pattern base is prefix paths, not full transactions.)  
B) ✓ The prefix paths in the FP-tree that lead to a given frequent item. (Correct: conditional pattern base is the collection of prefix paths.)  
C) ✗ The set of candidate itemsets generated from frequent itemsets. (Incorrect: candidate generation is Apriori.)  
D) ✗ The list of transaction IDs associated with an itemset. (Incorrect: tid-lists are vertical format, not FP-Growth.)

**Correct:** B


#### 7. Which of the following challenges are associated with the Apriori algorithm?  
A) ✓ Multiple scans of the database. (Correct: Apriori requires many scans.)  
B) ✓ Large number of candidate itemsets. (Correct: candidate explosion is a problem.)  
C) ✗ Difficulty in generating association rules from frequent itemsets. (Incorrect: rule generation is straightforward once frequent itemsets are found.)  
D) ✓ Tedious support counting for candidates. (Correct: counting support for many candidates is costly.)

**Correct:** A, B, D


#### 8. In vertical data format mining, what is the main benefit of using *diffsets*?  
A) ✓ They reduce the size of transaction ID lists by storing only differences. (Correct: diffsets store differences to save space.)  
B) ✗ They allow mining without scanning the database. (Incorrect: initial scan is still needed.)  
C) ✗ They increase the number of candidates generated. (Incorrect: diffsets reduce overhead.)  
D) ✓ They speed up support counting by set difference operations. (Correct: diffsets speed up support counting.)

**Correct:** A, D


#### 9. Which of the following statements about *lift* as an interestingness measure are correct?  
A) ✓ Lift greater than 1 indicates a positive correlation between itemsets. (Correct: lift > 1 means items co-occur more than expected.)  
B) ✓ Lift equal to 1 means the itemsets are independent. (Correct: no correlation.)  
C) ✓ Lift less than 1 indicates a negative correlation. (Correct: items co-occur less than expected.)  
D) ✗ Lift is always higher than confidence. (Incorrect: lift and confidence measure different things; no fixed order.)

**Correct:** A, B, C


#### 10. Why is constraint-based mining important in association rule mining?  
A) ✗ It allows mining all possible patterns autonomously. (Incorrect: constraint-based mining focuses search, not exhaustive mining.)  
B) ✓ It helps focus mining on user-specified relevant patterns. (Correct: user constraints guide mining.)  
C) ✓ It reduces computational cost by pruning irrelevant patterns. (Correct: constraints prune search space.)  
D) ✗ It guarantees finding all maximal frequent itemsets. (Incorrect: constraints may exclude some patterns.)

**Correct:** B, C


#### 11. Which of the following are true about multi-dimensional association rules?  
A) ✗ They involve only one attribute or dimension. (Incorrect: multi-dimensional means multiple attributes.)  
B) ✓ They can include predicates on multiple attributes like age and occupation. (Correct: multi-dimensional rules combine attributes.)  
C) ✓ They can have repeated predicates in hybrid-dimension rules. (Correct: hybrid rules allow repeated predicates.)  
D) ✗ They are limited to categorical attributes only. (Incorrect: can include quantitative attributes with discretization.)

**Correct:** B, C


#### 12. Which of the following are true about quantitative association rules?  
A) ✓ They treat numeric attributes by discretization or clustering. (Correct: numeric data is discretized or clustered.)  
B) ✗ They only apply to categorical data. (Incorrect: they specifically handle numeric data.)  
C) ✓ Dynamic discretization adjusts intervals based on data distribution. (Correct: dynamic discretization adapts to data.)  
D) ✗ They cannot handle multi-dimensional data. (Incorrect: quantitative rules can be multi-dimensional.)

**Correct:** A, C


#### 13. In the Apriori candidate generation step, which of the following is true?  
A) ✓ Candidates are generated by joining frequent (k-1)-itemsets with themselves. (Correct: self-join step.)  
B) ✓ Candidates are pruned if any of their subsets are infrequent. (Correct: pruning step.)  
C) ✗ Candidates are generated randomly to reduce computation. (Incorrect: candidate generation is systematic.)  
D) ✓ Candidate generation stops when no frequent itemsets are found. (Correct: termination condition.)

**Correct:** A, B, D


#### 14. Which of the following statements about FP-tree construction are correct?  
A) ✗ Items in each transaction are sorted in ascending order of frequency. (Incorrect: sorted descending by frequency.)  
B) ✓ The FP-tree root is labeled with a null value. (Correct: root is null.)  
C) ✓ Infrequent items are removed before building the FP-tree. (Correct: only frequent items included.)  
D) ✗ The FP-tree can be larger than the original database. (Incorrect: FP-tree is always equal or smaller.)

**Correct:** B, C


#### 15. What is the main reason that FP-Growth is considered more scalable than Apriori?  
A) ✗ It uses candidate generation to reduce search space. (Incorrect: FP-Growth avoids candidate generation.)  
B) ✓ It compresses the database and avoids candidate generation. (Correct: key advantage.)  
C) ✗ It requires more database scans but fewer candidates. (Incorrect: fewer scans.)  
D) ✗ It uses vertical data format exclusively. (Incorrect: FP-Growth uses horizontal format.)

**Correct:** B


#### 16. Which of the following are true about redundancy filtering in multi-level association rules?  
A) ✓ A rule is redundant if its support is close to the expected value based on its ancestor rule. (Correct: redundancy defined this way.)  
B) ✗ Redundancy filtering removes all rules with low confidence. (Incorrect: filtering is about redundancy, not confidence.)  
C) ✓ Ancestor rules are more general versions of descendant rules. (Correct: ancestor rules are higher-level.)  
D) ✗ Redundancy filtering is unnecessary when using uniform support thresholds. (Incorrect: redundancy can still occur.)

**Correct:** A, C


#### 17. Which of the following statements about sampling in frequent pattern mining are correct?  
A) ✗ Sampling reduces the number of database scans to one. (Incorrect: verification scan needed.)  
B) ✗ Frequent patterns found in the sample are always frequent in the full database. (Incorrect: sampling can miss patterns.)  
C) ✓ Sampling requires a verification scan to confirm frequent itemsets. (Correct: verification step.)  
D) ✓ Sampling can miss some frequent patterns if the sample is not representative. (Correct: sampling risk.)

**Correct:** C, D


#### 18. Which of the following are true about the use of *tid-lists* in vertical data format mining?  
A) ✓ Tid-lists store the list of transaction IDs containing an itemset. (Correct: definition.)  
B) ✓ Intersection of tid-lists is used to find support of combined itemsets. (Correct: support counting.)  
C) ✗ Tid-lists are used to generate candidate itemsets in Apriori. (Incorrect: Apriori uses horizontal format.)  
D) ✓ Tid-lists can be used to identify closed frequent itemsets. (Correct: used in CHARM algorithm.)

**Correct:** A, B, D


#### 19. Which of the following are examples of constraints that can be used in constraint-based mining?  
A) ✓ Minimum support and confidence thresholds. (Correct: common constraints.)  
B) ✓ Limiting mining to specific regions or time periods. (Correct: data constraints.)  
C) ✓ Only mining rules with consequents involving high sales. (Correct: rule constraints.)  
D) ✗ Automatically mining all possible patterns without user input. (Incorrect: opposite of constraint-based mining.)

**Correct:** A, B, C


#### 20. Which of the following statements about association rule mining applications are true?  
A) ✓ ARM can be used for web clickstream analysis. (Correct: common application.)  
B) ✗ ARM is only applicable to market basket data. (Incorrect: many other domains.)  
C) ✓ ARM can assist in DNA sequence pattern discovery. (Correct: bioinformatics application.)  
D) ✗ ARM cannot be used for classification or clustering tasks. (Incorrect: ARM supports associative classification and clustering.)

**Correct:** A, C

