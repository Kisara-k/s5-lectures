## 1. Concepts and Techniques

## Key Points

#### 1. 🧩 Data Objects and Attributes  
- A data object represents an entity and is described by attributes.  
- Data objects are also called samples, instances, tuples, or examples.  
- Attributes correspond to columns in a database; rows correspond to data objects.

#### 2. 🏷️ Attribute Types  
- Nominal attributes represent categories without order (e.g., hair color).  
- Binary attributes have two states; symmetric binary treats both outcomes equally, asymmetric binary does not.  
- Ordinal attributes have a meaningful order but unknown magnitude between values (e.g., ranks).  
- Numeric attributes are quantitative and can be interval-scaled (no true zero) or ratio-scaled (true zero).  
- Discrete attributes have countable values; continuous attributes have real values.

#### 3. 📊 Basic Statistical Descriptions  
- Mean is the average value; median is the middle value; mode is the most frequent value.  
- Variance measures average squared deviation from the mean; standard deviation is its square root.  
- Quartiles divide data into four parts; interquartile range (IQR) = Q3 - Q1.  
- Outliers are values beyond 1.5 × IQR from quartiles.  
- Boxplots graphically display min, Q1, median, Q3, max, and outliers.

#### 4. 📈 Data Distribution  
- Symmetric data: mean ≈ median ≈ mode.  
- Positively skewed data: mean > median > mode.  
- Negatively skewed data: mean < median < mode.  
- Normal distribution contains ~68% data within ±1σ, ~95% within ±2σ, ~99.7% within ±3σ.

#### 5. 🖼️ Data Visualization Techniques  
- Pixel-oriented visualization maps attribute values to colored pixels.  
- Geometric projection includes scatterplots, scatterplot matrices, parallel coordinates.  
- Icon-based visualization uses Chernoff faces and stick figures to represent multivariate data.  
- Hierarchical visualization includes dimensional stacking, tree-maps, cone trees.  
- Tag clouds visualize text data; social networks visualize relationships.

#### 6. 🔍 Similarity and Dissimilarity  
- Similarity measures how alike two objects are; higher values mean more similar (range often [0,1]).  
- Dissimilarity (distance) measures difference; lower values mean more similar; minimum often 0.  
- Proximity can refer to either similarity or dissimilarity.

#### 7. 📏 Similarity/Dissimilarity Measures for Attribute Types  
- Nominal: simple matching counts matches; can convert to multiple binary attributes.  
- Binary: symmetric binary uses simple matching; asymmetric binary uses Jaccard coefficient.  
- Numeric: Minkowski distance generalizes Manhattan (L1), Euclidean (L2), and supremum (L∞) distances.  
- Ordinal: convert ranks to [0,1] scale, then treat as numeric.  
- Mixed types: combine distances with weighted formulas.

#### 8. ➗ Cosine Similarity  
- Measures cosine of angle between two vectors (e.g., term-frequency vectors).  
- Values range from 0 (no similarity) to 1 (identical).  
- Useful for high-dimensional sparse data like text documents.



<br>

## Study Notes

### 1. 📊 Understanding Data Objects and Attribute Types

When working with data mining, the first step is to understand the nature of the data you have. Data is made up of **data objects**, which are the individual entities or records you want to analyze. Each data object is described by **attributes** (also called features, variables, or dimensions), which represent the characteristics or properties of that object.

#### What Are Data Objects?  
- A **data object** is a single entity or instance in your dataset.  
- Examples:  
  - In a sales database, data objects could be customers, products, or transactions.  
  - In a medical database, data objects might be patients or treatments.  
  - In a university database, data objects could be students, professors, or courses.  
- Data objects are often called samples, examples, instances, or tuples.  
- In a table, each **row** corresponds to a data object.

#### What Are Attributes?  
- An **attribute** is a characteristic or property of a data object.  
- Attributes correspond to the **columns** in a database table.  
- Examples: customer ID, age, income, hair color, test results.  
- Attributes can be of different types, which affect how we analyze and process the data.

#### Types of Attributes  
Understanding attribute types is crucial because different types require different handling in data mining.

1. **Nominal Attributes**  
   - These are categorical attributes with no inherent order.  
   - Examples: hair color (black, brown, blond), marital status, zip codes.  
   - They represent categories or names of things.

2. **Binary Attributes**  
   - Special case of nominal attributes with only two possible values (0 or 1).  
   - **Symmetric binary**: both outcomes are equally important (e.g., gender).  
   - **Asymmetric binary**: one outcome is more important (e.g., medical test results where positive is more significant than negative).  
   - Conventionally, assign 1 to the more important outcome.

3. **Ordinal Attributes**  
   - These have a meaningful order or ranking but the difference between values is not necessarily uniform.  
   - Examples: size (small, medium, large), grades (A, B, C), military ranks.  
   - We know the order but not the exact magnitude of difference.

4. **Numeric Attributes**  
   - Quantitative attributes measured on a numeric scale.  
   - Two subtypes:  
     - **Interval-scaled**: values have order and equal intervals but no true zero point (e.g., temperature in Celsius or Fahrenheit).  
     - **Ratio-scaled**: have a true zero point, allowing meaningful ratios (e.g., height, weight, income).

5. **Discrete vs. Continuous Attributes**  
   - **Discrete**: finite or countably infinite set of values (e.g., number of children, zip codes).  
   - **Continuous**: can take any real value within a range (e.g., height, temperature).  
   - Continuous attributes are often stored as floating-point numbers.


### 2. 📈 Basic Statistical Descriptions of Data

Before diving into complex analysis, it’s important to summarize and understand the basic statistical properties of your data. This helps you grasp the central tendencies, variability, and overall distribution.

#### Why Use Statistical Descriptions?  
- To get a quick overview of the data’s characteristics.  
- To identify patterns, trends, and potential anomalies like outliers.  
- To understand the spread and central values of the data.

#### Measures of Central Tendency  
These describe the "center" or typical value of the data.

- **Mean (Average)**: Sum of all values divided by the number of values.  
  - Can be weighted if some data points are more important.  
  - Trimmed mean excludes extreme values to reduce the effect of outliers.

- **Median**: The middle value when data is sorted.  
  - If there is an even number of values, it’s the average of the two middle values.  
  - More robust to outliers than the mean.

- **Mode**: The most frequently occurring value.  
  - Data can be unimodal (one mode), bimodal (two modes), or multimodal.

#### Measures of Dispersion (Spread)  
These describe how spread out the data values are.

- **Range**: Difference between the maximum and minimum values.  
- **Quartiles**: Values that divide the data into four equal parts.  
  - Q1 (25th percentile), Q2 (median), Q3 (75th percentile).  
- **Interquartile Range (IQR)**: Q3 - Q1, measures the middle 50% spread.  
- **Variance**: Average of squared differences from the mean.  
- **Standard Deviation**: Square root of variance, gives spread in original units.

#### Boxplots  
- A graphical summary showing minimum, Q1, median, Q3, and maximum.  
- Whiskers extend to min and max values within 1.5 × IQR.  
- Points outside whiskers are outliers.

#### Understanding Data Distribution  
- **Symmetric distribution**: mean, median, and mode are roughly equal.  
- **Positively skewed**: tail on the right, mean > median > mode.  
- **Negatively skewed**: tail on the left, mean < median < mode.

#### Normal Distribution  
- A bell-shaped curve describing many natural phenomena.  
- About 68% of data falls within ±1 standard deviation from the mean.  
- About 95% within ±2 standard deviations.  
- About 99.7% within ±3 standard deviations.


### 3. 📊 Data Visualization Techniques

Visualizing data helps us see patterns, trends, and outliers that might not be obvious from raw numbers alone. It also aids in communicating findings clearly.

#### Why Visualize Data?  
- To gain intuitive understanding of large and complex datasets.  
- To detect patterns, clusters, and anomalies.  
- To guide further analysis and parameter tuning.

#### Categories of Visualization Methods

1. **Pixel-Oriented Visualization**  
   - Each data value is mapped to a pixel with color representing the value.  
   - Useful for very high-dimensional data.  
   - Pixels can be arranged in various layouts, including circle segments to save space.

2. **Geometric Projection Visualization**  
   - Projects high-dimensional data into 2D or 3D space.  
   - Examples: scatterplots, scatterplot matrices, landscapes, parallel coordinates.  
   - **Scatterplot matrices** show pairwise relationships between attributes.  
   - **Parallel coordinates** plot each attribute as a vertical axis; data objects are lines crossing these axes.

3. **Icon-Based Visualization**  
   - Uses icons or shapes to represent data values.  
   - Examples:  
     - **Chernoff Faces**: map variables to facial features (eye size, mouth shape) to visualize multivariate data.  
     - **Stick figures**: use limb lengths and angles to represent data.

4. **Hierarchical Visualization**  
   - Visualizes data with hierarchical structure or partitions.  
   - Examples:  
     - **Dimensional stacking**: nests lower-dimensional views inside higher-dimensional ones.  
     - **Tree-maps**: partition screen space into rectangles sized by attribute values.  
     - **Cone trees**: 3D visualization of hierarchical data.

5. **Visualizing Complex Data and Relations**  
   - For non-numeric data like text or social networks.  
   - Examples: tag clouds (font size/color shows tag importance), network graphs showing relationships.


### 4. 🔍 Measuring Data Similarity and Dissimilarity

To analyze data, especially for clustering or classification, we need to measure how similar or different data objects are.

#### What Are Similarity and Dissimilarity?  
- **Similarity**: a numerical measure of how alike two objects are. Higher values mean more similar. Usually ranges from 0 to 1.  
- **Dissimilarity (Distance)**: a numerical measure of how different two objects are. Lower values mean more similar. Minimum is often 0.

#### Data Representations  
- **Data matrix**: n objects × p attributes.  
- **Dissimilarity matrix**: n × n matrix showing pairwise distances between objects.

#### Similarity/Dissimilarity for Different Attribute Types

1. **Nominal Attributes**  
   - Use simple matching: count how many attributes match.  
   - Or convert nominal attributes into multiple binary attributes (one-hot encoding).

2. **Binary Attributes**  
   - Use contingency tables to count matches and mismatches.  
   - **Symmetric binary**: both outcomes equally important.  
   - **Asymmetric binary**: one outcome more important (e.g., presence of a disease).  
   - **Jaccard coefficient**: similarity measure for asymmetric binary data, ignoring double negatives.

3. **Numeric Attributes**  
   - Use distance measures like **Minkowski distance**, which generalizes several distances:  
     - **Manhattan distance (L1 norm)**: sum of absolute differences.  
     - **Euclidean distance (L2 norm)**: square root of sum of squared differences.  
     - **Supremum distance (L∞ norm)**: maximum difference in any attribute.

4. **Ordinal Attributes**  
   - Convert ranks to numeric values scaled between 0 and 1.  
   - Then use numeric distance measures.

5. **Mixed Attribute Types**  
   - Combine distances for different attribute types using weighted sums.

#### Cosine Similarity  
- Common for high-dimensional data like text documents.  
- Measures the cosine of the angle between two vectors (e.g., term-frequency vectors).  
- Values range from 0 (orthogonal, no similarity) to 1 (identical direction).  
- Useful when magnitude is less important than direction (pattern of attribute presence).


### 5. 📝 Summary and Key Takeaways

- Data mining starts with **knowing your data**: understanding data objects and attribute types is fundamental.  
- Different attribute types (nominal, binary, ordinal, numeric) require different handling and similarity measures.  
- Basic statistical descriptions (mean, median, variance, boxplots) help summarize and understand data distributions.  
- Visualization techniques provide intuitive insights and help detect patterns and anomalies.  
- Measuring similarity and dissimilarity is essential for many data mining tasks like clustering and classification.  
- Handling mixed data types and high-dimensional data requires careful choice of distance/similarity measures.  
- These foundational steps are part of **data preprocessing**, a critical phase before applying advanced data mining algorithms.