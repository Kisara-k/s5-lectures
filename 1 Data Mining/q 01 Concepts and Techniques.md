## 1. Concepts and Techniques

## Questions

#### 1. Which of the following statements about data objects and attributes are true?  
A) Data objects represent entities and are described by attributes.  
B) Attributes correspond to rows in a database table.  
C) Data objects are also called samples, instances, or tuples.  
D) Attributes always have numeric values.

#### 2. Which attribute types can be considered nominal?  
A) Hair color (e.g., black, brown, blond)  
B) Temperature in Celsius  
C) Zip codes  
D) Military rank (e.g., private, sergeant, captain)

#### 3. What distinguishes an asymmetric binary attribute from a symmetric binary attribute?  
A) Asymmetric binary attributes have two equally important outcomes.  
B) Symmetric binary attributes have one outcome more important than the other.  
C) In asymmetric binary attributes, the presence of a feature is more significant than its absence.  
D) Gender is an example of an asymmetric binary attribute.

#### 4. Which of the following are true about ordinal attributes?  
A) They have a meaningful order but unknown magnitude between values.  
B) They can be treated exactly like nominal attributes in all analyses.  
C) Examples include grades and army rankings.  
D) The difference between "small" and "medium" is always the same as between "medium" and "large."

#### 5. Which statements about interval-scaled and ratio-scaled numeric attributes are correct?  
A) Interval-scaled attributes have a true zero point.  
B) Ratio-scaled attributes allow meaningful ratio comparisons (e.g., twice as long).  
C) Temperature in Kelvin is ratio-scaled, while temperature in Celsius is interval-scaled.  
D) Calendar dates are ratio-scaled.

#### 6. Which of the following are characteristics of continuous attributes?  
A) They can take any real value within a range.  
B) They are always represented as integers.  
C) Height and weight are examples of continuous attributes.  
D) Continuous attributes can be measured with infinite precision in practice.

#### 7. When summarizing data, which of the following statements about the median are true?  
A) The median is less sensitive to outliers than the mean.  
B) The median is the most frequently occurring value.  
C) For an even number of values, the median is the average of the two middle values.  
D) The median can be estimated by interpolation for grouped data.

#### 8. Regarding boxplots, which of the following are correct?  
A) The box represents the interquartile range (IQR).  
B) Whiskers extend to the minimum and maximum values in the data.  
C) Outliers are typically defined as points beyond 1.5 times the IQR from the quartiles.  
D) The median is shown as a line inside the box.

#### 9. Which of the following correctly describe the properties of a normal distribution?  
A) Approximately 68% of data lies within one standard deviation of the mean.  
B) The mean, median, and mode are all equal in a perfectly normal distribution.  
C) About 99.7% of data lies within two standard deviations of the mean.  
D) The distribution is symmetric around the mean.

#### 10. Which visualization techniques are suitable for very high-dimensional data?  
A) Pixel-oriented visualization  
B) Scatterplot matrices  
C) Parallel coordinates  
D) Tree-maps

#### 11. Which statements about scatterplot matrices are true?  
A) They show pairwise relationships between all attributes.  
B) They are useful for visualizing data with more than 20 dimensions without clutter.  
C) Each cell in the matrix is a scatterplot of two attributes.  
D) They can help identify clusters and outliers.

#### 12. Which of the following are true about Chernoff faces?  
A) They represent multivariate data by mapping variables to facial features.  
B) They are effective for visualizing data with more than 20 variables.  
C) Each facial feature corresponds to a single attribute.  
D) They can help humans detect patterns in complex data.

#### 13. Which of the following are properties of Minkowski distance?  
A) It satisfies the triangle inequality.  
B) It is only defined for numeric attributes.  
C) Manhattan distance is a special case with order h=1.  
D) Euclidean distance is a special case with order h=2.

#### 14. When calculating similarity for nominal attributes, which methods are valid?  
A) Simple matching coefficient counting matches over total attributes.  
B) Converting nominal attributes into multiple binary attributes.  
C) Using Euclidean distance directly on nominal values.  
D) Ignoring nominal attributes altogether.

#### 15. Which of the following statements about the Jaccard coefficient are true?  
A) It is used for symmetric binary attributes.  
B) It ignores double negatives (both attributes absent).  
C) It measures similarity between asymmetric binary attributes.  
D) It ranges from -1 to 1.

#### 16. Which of the following are true about cosine similarity?  
A) It measures the angle between two vectors in a high-dimensional space.  
B) It is sensitive to the magnitude of the vectors.  
C) It is commonly used in text mining for term-frequency vectors.  
D) Cosine similarity values range from 0 to 1.

#### 17. When dealing with mixed attribute types in a dataset, which approaches are appropriate?  
A) Use a weighted formula combining distances for each attribute type.  
B) Convert all attributes to nominal and use simple matching.  
C) Normalize numeric attributes before combining with nominal attributes.  
D) Treat ordinal attributes as interval-scaled after rank transformation.

#### 18. Which of the following statements about hierarchical visualization techniques are correct?  
A) Tree-maps partition the screen space based on attribute values hierarchically.  
B) Dimensional stacking is suitable for datasets with more than 20 dimensions.  
C) Cone trees visualize hierarchical data in 3D space.  
D) Worlds-within-worlds assign parameters to nested visual spaces.

#### 19. Which of the following are true about data dispersion analysis?  
A) Variance measures the average squared deviation from the mean.  
B) Standard deviation is the square root of variance.  
C) Outliers are always values beyond 3 standard deviations from the mean.  
D) The interquartile range (IQR) is resistant to outliers.

#### 20. Which of the following statements about data visualization and analysis are true?  
A) Histograms differ from bar charts because the area of bars represents frequency, not just height.  
B) Quantile plots display the cumulative distribution of data values.  
C) Scatter plots can only be used for univariate data.  
D) Q-Q plots compare quantiles of two distributions to detect shifts or differences.



<br>

## Answers

#### 1. Which of the following statements about data objects and attributes are true?  
A) ✓ Data objects represent entities and are described by attributes.  
B) ✗ Attributes correspond to columns, not rows, in a database table.  
C) ✓ Data objects are also called samples, instances, or tuples.  
D) ✗ Attributes can be nominal, binary, ordinal, or numeric, not always numeric.

**Correct:** A, C


#### 2. Which attribute types can be considered nominal?  
A) ✓ Hair color is a categorical attribute with no order.  
B) ✗ Temperature in Celsius is interval-scaled, not nominal.  
C) ✓ Zip codes are categorical labels, treated as nominal.  
D) ✗ Military rank is ordinal, not nominal, because it has order.

**Correct:** A, C


#### 3. What distinguishes an asymmetric binary attribute from a symmetric binary attribute?  
A) ✗ Asymmetric binary attributes have one outcome more important, not equally important.  
B) ✗ Symmetric binary attributes have equally important outcomes.  
C) ✓ In asymmetric binary attributes, presence (1) is more significant than absence (0).  
D) ✗ Gender is symmetric binary, as both outcomes are equally important.

**Correct:** C


#### 4. Which of the following are true about ordinal attributes?  
A) ✓ They have meaningful order but unknown magnitude between values.  
B) ✗ Ordinal attributes cannot be treated exactly like nominal attributes because order matters.  
C) ✓ Grades and army rankings are examples of ordinal attributes.  
D) ✗ The difference between categories is not necessarily equal or known.

**Correct:** A, C


#### 5. Which statements about interval-scaled and ratio-scaled numeric attributes are correct?  
A) ✗ Interval-scaled attributes do not have a true zero point.  
B) ✓ Ratio-scaled attributes allow meaningful ratio comparisons.  
C) ✓ Temperature in Kelvin is ratio-scaled; Celsius is interval-scaled.  
D) ✗ Calendar dates are interval-scaled, not ratio-scaled.

**Correct:** B, C


#### 6. Which of the following are characteristics of continuous attributes?  
A) ✓ Continuous attributes can take any real value within a range.  
B) ✗ Continuous attributes are not always integers; integers are discrete.  
C) ✓ Height and weight are examples of continuous attributes.  
D) ✗ Continuous attributes cannot be measured with infinite precision in practice.

**Correct:** A, C


#### 7. When summarizing data, which of the following statements about the median are true?  
A) ✓ Median is less sensitive to outliers than mean.  
B) ✗ Mode is the most frequently occurring value, not median.  
C) ✓ For even number of values, median is average of two middle values.  
D) ✓ Median can be estimated by interpolation for grouped data.

**Correct:** A, C, D


#### 8. Regarding boxplots, which of the following are correct?  
A) ✓ The box represents the interquartile range (IQR).  
B) ✗ Whiskers extend to min and max within 1.5 × IQR, not necessarily absolute min/max.  
C) ✓ Outliers are points beyond 1.5 × IQR from quartiles.  
D) ✓ Median is shown as a line inside the box.

**Correct:** A, C, D


#### 9. Which of the following correctly describe the properties of a normal distribution?  
A) ✓ About 68% of data lies within ±1 standard deviation.  
B) ✓ Mean, median, and mode are equal in a normal distribution.  
C) ✗ About 99.7% lies within ±3 standard deviations, not 2.  
D) ✓ The distribution is symmetric around the mean.

**Correct:** A, B, D


#### 10. Which visualization techniques are suitable for very high-dimensional data?  
A) ✓ Pixel-oriented visualization handles many dimensions.  
B) ✗ Scatterplot matrices become cluttered with many dimensions.  
C) ✓ Parallel coordinates can visualize high-dimensional data.  
D) ✗ Tree-maps are better for hierarchical data, not high-dimensional attribute spaces.

**Correct:** A, C


#### 11. Which statements about scatterplot matrices are true?  
A) ✓ They show pairwise relationships between all attributes.  
B) ✗ They become cluttered and less useful with very high dimensions.  
C) ✓ Each cell is a scatterplot of two attributes.  
D) ✓ Useful for identifying clusters and outliers.

**Correct:** A, C, D


#### 12. Which of the following are true about Chernoff faces?  
A) ✓ They map variables to facial features to visualize multivariate data.  
B) ✗ They are not effective for more than about 10 variables due to complexity.  
C) ✓ Each facial feature corresponds to one attribute.  
D) ✓ They help humans detect patterns in complex data visually.

**Correct:** A, C, D


#### 13. Which of the following are properties of Minkowski distance?  
A) ✓ It satisfies the triangle inequality (metric property).  
B) ✗ It is defined for numeric attributes only.  
C) ✓ Manhattan distance is Minkowski with h=1.  
D) ✓ Euclidean distance is Minkowski with h=2.

**Correct:** A, C, D


#### 14. When calculating similarity for nominal attributes, which methods are valid?  
A) ✓ Simple matching counts matches over total attributes.  
B) ✓ Converting nominal attributes into binary attributes is valid.  
C) ✗ Euclidean distance is not appropriate for nominal data.  
D) ✗ Ignoring nominal attributes loses important information.

**Correct:** A, B


#### 15. Which of the following statements about the Jaccard coefficient are true?  
A) ✗ It is used for asymmetric binary attributes, not symmetric.  
B) ✓ It ignores double negatives (both attributes absent).  
C) ✓ Measures similarity for asymmetric binary attributes.  
D) ✗ Jaccard coefficient ranges from 0 to 1, not -1 to 1.

**Correct:** B, C


#### 16. Which of the following are true about cosine similarity?  
A) ✓ Measures the angle between two vectors in high-dimensional space.  
B) ✗ It is insensitive to magnitude; focuses on direction.  
C) ✓ Commonly used in text mining for term-frequency vectors.  
D) ✓ Cosine similarity values range from 0 to 1.

**Correct:** A, C, D


#### 17. When dealing with mixed attribute types in a dataset, which approaches are appropriate?  
A) ✓ Use weighted formulas combining distances for each attribute type.  
B) ✗ Converting all to nominal loses numeric information.  
C) ✓ Normalize numeric attributes before combining with nominal attributes.  
D) ✓ Treat ordinal attributes as interval-scaled after rank transformation.

**Correct:** A, C, D


#### 18. Which of the following statements about hierarchical visualization techniques are correct?  
A) ✓ Tree-maps partition screen space hierarchically by attribute values.  
B) ✗ Dimensional stacking is difficult beyond about 9 dimensions.  
C) ✓ Cone trees visualize hierarchical data in 3D space.  
D) ✓ Worlds-within-worlds assign parameters to nested visual spaces.

**Correct:** A, C, D


#### 19. Which of the following are true about data dispersion analysis?  
A) ✓ Variance measures average squared deviation from the mean.  
B) ✓ Standard deviation is the square root of variance.  
C) ✗ Outliers are often defined by 1.5 × IQR, not always 3 standard deviations.  
D) ✓ Interquartile range (IQR) is resistant to outliers.

**Correct:** A, B, D


#### 20. Which of the following statements about data visualization and analysis are true?  
A) ✓ Histograms differ from bar charts because bar area represents frequency.  
B) ✓ Quantile plots display cumulative distribution of data values.  
C) ✗ Scatter plots are for bivariate data, not univariate.  
D) ✓ Q-Q plots compare quantiles of two distributions to detect shifts.


**Correct:** A, B, D