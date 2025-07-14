## 13 Data Mining and Society

[Study Notes](#study-notes)

[Questions](#questions)



### Key Points

#### 1. 💰 Financial Data Mining  
- Financial data in banks is often complete, reliable, and high quality.  
- Data warehouses enable multidimensional analysis by month, region, sector, etc.  
- Loan payment prediction and consumer credit rating use classification and clustering.  
- Money laundering detection integrates multiple databases and uses outlier and sequential pattern analysis.  

#### 2. 🛒 Retail and Telecommunications Data Mining  
- Retail data mining identifies customer buying behaviors and shopping patterns.  
- Customer loyalty is analyzed using sequential pattern mining on loyalty card data.  
- Fraud detection in retail uses pattern analysis and visualization tools.  
- Telecommunications share similar data mining goals as retail, such as customer retention and fraud detection.  

#### 3. 🔬 Data Mining in Science and Engineering  
- Data preprocessing resolves inconsistencies from diverse data sources and times.  
- Mining complex data types includes spatiotemporal, biological, and graph/network data.  
- Visualization tools and domain knowledge are essential for interpreting results.  

#### 4. 🛡️ Intrusion Detection and Prevention  
- Signature-based detection uses predefined attack patterns.  
- Anomaly-based detection builds profiles of normal behavior and detects deviations.  
- Data mining techniques include association, correlation, outlier detection, and distributed mining.  

#### 5. 🎯 Recommender Systems  
- Content-based filtering recommends items similar to those previously liked by the user.  
- Collaborative filtering uses preferences of similar users to make recommendations.  
- Hybrid methods combine content-based and collaborative filtering for better accuracy.  
- Memory-based methods often use k-nearest neighbor; model-based methods use probabilistic models or clustering.  

#### 6. 🌐 Ubiquitous and Invisible Data Mining  
- Ubiquitous data mining is embedded in everyday applications like online shopping and CRM.  
- Invisible data mining operates behind the scenes, e.g., Google search results, without user awareness.  
- Invisible mining requires efficiency, scalability, real-time processing, and user interaction.  

#### 7. 🔒 Privacy and Security in Data Mining  
- Privacy concerns arise from unconstrained access to individual sensitive records.  
- Methods to protect privacy include removing sensitive IDs, multi-level security, and encryption.  
- Privacy-preserving data mining obtains valid results without disclosing sensitive data.  
- Techniques include randomization (adding noise), k-anonymity (each record indistinguishable among k), and l-diversity (diversity of sensitive attributes).  
- Distributed privacy preservation partitions data horizontally or vertically to protect privacy.  
- Data mining outputs may be modified to hide sensitive patterns or distort models.  

#### 8. 🚀 Data Mining Trends and Research Frontiers  
- Trends include application-specific mining, scalable and interactive methods, and integration with web, cloud, and database systems.  
- Mining complex data types like social networks, spatiotemporal data, multimedia, and biomedical data is growing.  
- Real-time data stream mining and distributed mining are important research areas.  
- Privacy protection and security remain critical challenges in data mining development.



<br>

## Study Notes

### 1. 📊 Introduction to Data Mining and Its Applications

Data mining is a relatively young but rapidly growing field that involves extracting useful patterns, knowledge, and insights from large volumes of data. It combines techniques from statistics, machine learning, database systems, and artificial intelligence to analyze data and make predictions or decisions.

Despite its broad potential, there is often a gap between generic data mining methods and the development of effective, scalable tools tailored for specific application domains. This means that while the core techniques are well-studied, applying them successfully in real-world scenarios requires domain knowledge and customized solutions.

#### Key Application Areas:
- Financial data analysis
- Retail and telecommunications industries
- Science and engineering
- Intrusion detection and prevention
- Recommender systems

Each of these areas uses data mining in unique ways to solve specific problems, improve decision-making, and enhance services.


### 2. 💰 Data Mining for Financial Data Analysis

Financial institutions like banks collect large amounts of high-quality, reliable data. This data is often stored in data warehouses designed for multidimensional analysis, allowing analysts to view financial metrics across different dimensions such as time (monthly), region, or sector.

#### What Financial Data Mining Involves:
- **Multidimensional Analysis:** Viewing debt, revenue, and other financial indicators by various factors to detect trends and patterns.
- **Statistical Summaries:** Calculating max, min, averages, totals, and trends to understand financial health.
- **Loan Payment Prediction:** Using data mining to predict whether a customer will repay a loan, which helps in credit policy decisions.
- **Customer Segmentation:** Classifying customers into groups based on behavior or credit rating using clustering and classification methods like decision trees and nearest-neighbor algorithms.
- **Fraud Detection:** Identifying suspicious activities such as money laundering by integrating data from multiple sources (bank transactions, crime databases) and applying outlier and sequential pattern analysis.
- **Tools Used:** Visualization, linkage analysis (finding relationships), classification, clustering, and outlier detection.

Financial data mining helps banks manage risk, target marketing efforts, and detect illegal activities effectively.


### 3. 🛒 Data Mining in Retail and Telecommunications

Retail and telecom industries generate massive amounts of data from sales, customer transactions, and service usage. Data mining helps these industries understand customer behavior, improve service quality, and optimize operations.

#### Retail Industry Applications:
- **Customer Buying Behavior:** Discovering what products customers buy, when, and in what combinations.
- **Shopping Patterns and Trends:** Identifying seasonal or regional trends to stock and promote products better.
- **Customer Retention:** Analyzing loyalty card data to track purchase sequences and detect changes in customer loyalty.
- **Sales Campaign Analysis:** Measuring the effectiveness of marketing campaigns by analyzing sales data.
- **Product Recommendations:** Suggesting products based on past purchases or related items.
- **Fraud Detection:** Identifying unusual purchase patterns that may indicate fraud.
- **Visualization Tools:** Used to present complex data in understandable formats for decision-makers.

#### Telecommunications:
- Shares many goals with retail, such as customer segmentation, churn prediction, and fraud detection.

Data mining in these industries helps improve customer satisfaction, increase sales, and reduce losses.


### 4. 🔬 Data Mining in Science and Engineering

In scientific and engineering fields, data mining helps analyze complex and diverse data collected from experiments, sensors, and simulations.

#### Challenges and Approaches:
- **Data Preprocessing:** Cleaning and integrating data collected from different sources and times, which may have inconsistencies.
- **Mining Complex Data Types:** Handling spatiotemporal data (data with space and time dimensions), biological data, and data with complex relationships.
- **Graph and Network Mining:** Analyzing links and relationships, such as social networks or data flow in systems.
- **Visualization and Domain Knowledge:** Using specialized visualization tools and expert knowledge to interpret results.
- **Applications:** Social sciences (text and social media analysis), computer science (monitoring software bugs, network intrusion).

This area requires combining data mining with domain expertise to extract meaningful insights from complex datasets.


### 5. 🛡️ Data Mining for Intrusion Detection and Prevention

Intrusion detection systems (IDS) protect computer networks by identifying unauthorized or malicious activities.

#### Two Main Detection Methods:
- **Signature-based Detection:** Uses known attack patterns (signatures) predefined by experts to detect intrusions.
- **Anomaly-based Detection:** Builds models of normal behavior and flags deviations as potential intrusions.

#### How Data Mining Helps:
- Developing new algorithms to detect unknown or evolving attacks.
- Using association and correlation analysis to build classifiers that distinguish normal from malicious behavior.
- Analyzing streaming data in real-time to detect outliers or shifts in patterns.
- Distributed data mining to handle data from multiple sources.
- Visualization and querying tools to help security analysts understand and respond to threats.

Data mining enhances the ability to detect sophisticated cyber-attacks that traditional methods might miss.


### 6. 🎯 Data Mining and Recommender Systems

Recommender systems personalize user experiences by suggesting products, services, or content likely to interest the user.

#### Main Approaches:
- **Content-based Filtering:** Recommends items similar to those the user liked or interacted with before.
- **Collaborative Filtering:** Uses opinions and preferences of other users with similar tastes to make recommendations.
- **Hybrid Methods:** Combine content-based and collaborative filtering to improve accuracy.

#### Data Mining Techniques Used:
- Extracting known user-item ratings to predict unknown preferences.
- Memory-based methods like k-nearest neighbors to find similar users or items.
- Model-based methods using probabilistic models, clustering, or Bayesian networks to learn user preferences.
- Ensemble methods that integrate multiple models for better performance.

Recommender systems rely heavily on data mining to analyze user behavior and improve personalization.


### 7. 🌐 Trends in Data Mining: Ubiquitous and Invisible Mining

#### Ubiquitous Data Mining:
Data mining is becoming everywhere — embedded in many daily applications like online shopping and customer relationship management (CRM). It is no longer confined to specialized tools but integrated into everyday systems.

#### Invisible Data Mining:
Many data mining processes happen behind the scenes without users realizing it. For example, Google search results are generated using data mining techniques, but users simply see the results without knowing the complex analysis behind them.

Invisible mining is highly desirable because it provides value without requiring user effort, but it must be efficient, scalable, and capable of real-time operation. It also needs to incorporate user interaction, background knowledge, and visualization to be effective.


### 8. 🔒 Privacy, Security, and Social Impacts of Data Mining

While many data mining applications use non-personal data (e.g., weather, biology), privacy concerns arise when mining involves personal or sensitive information.

#### Privacy Risks:
- Unrestricted access to individual records can expose sensitive data.
- Mining results might inadvertently reveal private information.

#### Methods to Protect Privacy:
- **Removing Sensitive Identifiers:** Stripping personal IDs from datasets.
- **Security Enhancements:** Multi-level security models restrict access based on authorization; encryption techniques protect data.
- **Privacy-Preserving Data Mining:** Techniques that allow mining useful patterns without exposing sensitive data.

#### Privacy-Preserving Techniques:
- **Randomization/Perturbation:** Adding noise to data to mask individual values.
- **k-Anonymity:** Ensuring each record is indistinguishable from at least k-1 others based on certain attributes.
- **l-Diversity:** Extends k-anonymity by ensuring diversity of sensitive attributes within groups.
- **Distributed Privacy Preservation:** Data is partitioned and distributed to prevent exposure.
- **Modifying Mining Outputs:** Hiding or distorting some results to protect privacy.

An example of k-anonymity involves generalizing or suppressing data so that any combination of attributes (like age, gender, state) appears in at least two records, preventing unique identification.


### 9. 🚀 Emerging Trends and Research Frontiers in Data Mining

Data mining continues to evolve rapidly, with new challenges and opportunities:

- **Application-Specific Solutions:** Tailoring data mining to solve domain-specific problems.
- **Scalable and Interactive Methods:** Handling massive datasets efficiently and allowing user interaction.
- **Integration with Other Technologies:** Combining data mining with web search, databases, data warehouses, and cloud computing.
- **Mining Complex Data:** Including social networks, spatiotemporal data, multimedia, text, biological data, and cyber-physical systems.
- **Real-Time and Distributed Mining:** Processing streaming data and mining across distributed systems.
- **Privacy and Security:** Developing stronger privacy-preserving methods and secure mining techniques.

These trends highlight data mining as a strategic, promising field with wide-reaching impact across industries and society.


### 10. 📌 Summary

- Data mining is a powerful tool with diverse applications in finance, retail, science, security, and personalization.
- Effective data mining requires domain knowledge and customized tools.
- Privacy and security are critical concerns, leading to the development of privacy-preserving techniques.
- Data mining is becoming ubiquitous and often invisible in daily life.
- The field is rapidly advancing, focusing on scalability, integration, complex data types, and privacy protection.
- Overall, data mining holds great promise for helping society make better decisions and understand complex data.



<br>

## Questions

#### 1. Which of the following are common challenges when applying generic data mining methods to domain-specific applications?  
A) Lack of domain knowledge integration  
B) Scalability issues with large datasets  
C) Inability to handle multidimensional data  
D) Overfitting due to too much domain-specific tuning  


#### 2. In financial data mining, which techniques are typically used to detect money laundering activities?  
A) Sequential pattern analysis  
B) Clustering and classification  
C) Association rule mining without integration of external data  
D) Linkage analysis combining multiple databases  


#### 3. What is a key advantage of multidimensional data warehouses in financial data analysis?  
A) They allow viewing data only by time dimension  
B) They enable simultaneous analysis across multiple factors like region, sector, and time  
C) They eliminate the need for data preprocessing  
D) They automatically detect fraud without human intervention  


#### 4. Which of the following statements about customer segmentation in retail data mining are true?  
A) It uses nearest-neighbor and decision tree methods to classify customers  
B) It is only useful for identifying fraudulent customers  
C) It helps in targeted marketing and improving customer retention  
D) It requires real-time data streaming to be effective  


#### 5. In the context of telecommunications data mining, which goals are shared with the retail industry?  
A) Identifying customer churn  
B) Detecting network intrusions  
C) Analyzing customer buying behavior  
D) Improving customer satisfaction and retention  


#### 6. Which of the following best describes the role of visualization tools in data mining applications?  
A) They replace the need for statistical analysis  
B) They help interpret complex data and mining results for decision-makers  
C) They are only useful in scientific data mining, not in business applications  
D) They automate the entire data mining process  


#### 7. What are the main differences between signature-based and anomaly-based intrusion detection systems?  
A) Signature-based detects known attack patterns; anomaly-based detects deviations from normal behavior  
B) Anomaly-based requires preconfigured attack signatures  
C) Signature-based can detect zero-day attacks effectively  
D) Anomaly-based builds profiles of normal system behavior  


#### 8. Which data mining techniques are commonly used to improve recommender systems?  
A) k-nearest neighbor for memory-based collaborative filtering  
B) Bayesian networks for model-based approaches  
C) Sequential pattern mining for product recommendations  
D) Clustering to group users with similar preferences  


#### 9. What is a major challenge of invisible data mining?  
A) Making mining results visible to all users  
B) Ensuring efficiency and scalability without user awareness  
C) Preventing users from interacting with mining processes  
D) Eliminating the need for background knowledge incorporation  


#### 10. Which of the following are true about privacy-preserving data mining methods?  
A) Randomization adds noise to mask sensitive data  
B) k-anonymity ensures each record is unique in the dataset  
C) l-diversity enforces diversity of sensitive attributes within groups  
D) Distributed privacy preservation involves partitioning data across locations  


#### 11. How does k-anonymity protect privacy in data mining?  
A) By encrypting all data attributes  
B) By ensuring each record is indistinguishable from at least k-1 others based on certain attributes  
C) By removing all identifiers from the dataset  
D) By adding random noise to sensitive attributes  


#### 12. Which of the following statements about data mining trends are correct?  
A) Integration with cloud computing systems is a current research frontier  
B) Mining multimedia and text data is considered a solved problem  
C) Real-time data stream mining is increasingly important  
D) Privacy protection is no longer a major concern due to encryption  


#### 13. In scientific data mining, what is a common challenge when dealing with data collected from diverse environments and periods?  
A) Lack of data volume  
B) Inconsistencies and incompatibilities in data  
C) Overabundance of labeled data  
D) Absence of complex data types  


#### 14. Which of the following best describes the concept of ubiquitous data mining?  
A) Data mining only applied in specialized research labs  
B) Data mining embedded in everyday applications like online shopping  
C) Data mining that requires explicit user interaction at all times  
D) Data mining that is visible and transparent to all users  


#### 15. What is the primary purpose of using sequential pattern mining in retail customer analysis?  
A) To detect fraudulent transactions only  
B) To investigate changes in customer consumption or loyalty over time  
C) To cluster customers into demographic groups  
D) To predict stock market trends  


#### 16. Which of the following are potential drawbacks of privacy-preserving data mining?  
A) Trade-off between data utility and privacy protection  
B) Increased risk of data breaches  
C) Possible distortion of mining results  
D) Complete elimination of privacy risks  


#### 17. How does distributed data mining contribute to privacy preservation?  
A) By centralizing all data in one secure location  
B) By partitioning data horizontally or vertically across multiple sites  
C) By encrypting data before mining  
D) By removing sensitive attributes from the dataset  


#### 18. Which of the following statements about recommender systems is false?  
A) Content-based filtering recommends items similar to those a user liked before  
B) Collaborative filtering relies on the preferences of similar users  
C) Hybrid approaches combine multiple recommendation techniques to improve accuracy  
D) Recommender systems do not require any user data to function  


#### 19. What is a key reason why data mining tools must be scalable and interactive?  
A) To handle increasing data volumes and allow user-driven exploration  
B) To eliminate the need for domain-specific knowledge  
C) To ensure mining results are always 100% accurate  
D) To replace human decision-making entirely  


#### 20. Which of the following best describes the relationship between data mining and social impacts?  
A) Data mining has no impact on privacy or security concerns  
B) Data mining can raise ethical issues related to unconstrained access to personal data  
C) Data mining is only used for scientific purposes and does not affect society  
D) Privacy-preserving techniques are irrelevant to social concerns



<br>

## Answers

#### 1. Which of the following are common challenges when applying generic data mining methods to domain-specific applications?  
A) ✓ Lack of domain knowledge integration — Domain knowledge is crucial for effective application.  
B) ✓ Scalability issues with large datasets — Generic methods may not scale well for big data.  
C) ✗ Inability to handle multidimensional data — Many methods can handle multidimensional data.  
D) ✗ Overfitting due to too much domain-specific tuning — Overfitting is usually due to insufficient generalization, not excessive tuning.

**Correct:** A, B


#### 2. In financial data mining, which techniques are typically used to detect money laundering activities?  
A) ✓ Sequential pattern analysis — Used to find unusual transaction sequences.  
B) ✓ Clustering and classification — Help identify suspicious groups or behaviors.  
C) ✗ Association rule mining without integration of external data — Integration of multiple databases is essential.  
D) ✓ Linkage analysis combining multiple databases — Crucial for connecting disparate data sources.

**Correct:** A, B, D


#### 3. What is a key advantage of multidimensional data warehouses in financial data analysis?  
A) ✗ They allow viewing data only by time dimension — They support multiple dimensions, not just time.  
B) ✓ They enable simultaneous analysis across multiple factors like region, sector, and time — This is the main advantage.  
C) ✗ They eliminate the need for data preprocessing — Preprocessing is still required.  
D) ✗ They automatically detect fraud without human intervention — Fraud detection requires analysis and tools.

**Correct:** B


#### 4. Which of the following statements about customer segmentation in retail data mining are true?  
A) ✓ It uses nearest-neighbor and decision tree methods to classify customers — Common classification methods.  
B) ✗ It is only useful for identifying fraudulent customers — It serves broader marketing purposes.  
C) ✓ It helps in targeted marketing and improving customer retention — Core purpose of segmentation.  
D) ✗ It requires real-time data streaming to be effective — Not always necessary; batch analysis is common.

**Correct:** A, C


#### 5. In the context of telecommunications data mining, which goals are shared with the retail industry?  
A) ✓ Identifying customer churn — Important in both industries.  
B) ✗ Detecting network intrusions — More specific to telecom/security.  
C) ✗ Analyzing customer buying behavior — More relevant to retail.  
D) ✓ Improving customer satisfaction and retention — Common goal.

**Correct:** A, D


#### 6. Which of the following best describes the role of visualization tools in data mining applications?  
A) ✗ They replace the need for statistical analysis — Visualization complements but does not replace analysis.  
B) ✓ They help interpret complex data and mining results for decision-makers — Visualization aids understanding.  
C) ✗ They are only useful in scientific data mining, not in business applications — Used widely in business too.  
D) ✗ They automate the entire data mining process — Visualization is a support tool, not automation.

**Correct:** B


#### 7. What are the main differences between signature-based and anomaly-based intrusion detection systems?  
A) ✓ Signature-based detects known attack patterns; anomaly-based detects deviations from normal behavior — Core difference.  
B) ✗ Anomaly-based requires preconfigured attack signatures — It builds profiles of normal behavior instead.  
C) ✗ Signature-based can detect zero-day attacks effectively — It cannot detect unknown attacks well.  
D) ✓ Anomaly-based builds profiles of normal system behavior — True.

**Correct:** A, D


#### 8. Which data mining techniques are commonly used to improve recommender systems?  
A) ✓ k-nearest neighbor for memory-based collaborative filtering — Common technique.  
B) ✓ Bayesian networks for model-based approaches — Used for learning user preferences.  
C) ✗ Sequential pattern mining for product recommendations — Less common in recommender systems.  
D) ✓ Clustering to group users with similar preferences — Helps collaborative filtering.

**Correct:** A, B, D


#### 9. What is a major challenge of invisible data mining?  
A) ✗ Making mining results visible to all users — Invisible mining is about being unnoticed.  
B) ✓ Ensuring efficiency and scalability without user awareness — Key challenge for invisible mining.  
C) ✗ Preventing users from interacting with mining processes — Interaction may still be needed.  
D) ✗ Eliminating the need for background knowledge incorporation — Background knowledge is important.

**Correct:** B


#### 10. Which of the following are true about privacy-preserving data mining methods?  
A) ✓ Randomization adds noise to mask sensitive data — Correct technique.  
B) ✗ k-anonymity ensures each record is unique in the dataset — It ensures records are indistinguishable among k records.  
C) ✓ l-diversity enforces diversity of sensitive attributes within groups — Enhances privacy beyond k-anonymity.  
D) ✓ Distributed privacy preservation involves partitioning data across locations — True.

**Correct:** A, C, D


#### 11. How does k-anonymity protect privacy in data mining?  
A) ✗ By encrypting all data attributes — Encryption is a different method.  
B) ✓ By ensuring each record is indistinguishable from at least k-1 others based on certain attributes — Core principle of k-anonymity.  
C) ✗ By removing all identifiers from the dataset — Removing identifiers alone is insufficient.  
D) ✗ By adding random noise to sensitive attributes — This is randomization, not k-anonymity.

**Correct:** B


#### 12. Which of the following statements about data mining trends are correct?  
A) ✓ Integration with cloud computing systems is a current research frontier — True.  
B) ✗ Mining multimedia and text data is considered a solved problem — Still an active research area.  
C) ✓ Real-time data stream mining is increasingly important — Growing trend.  
D) ✗ Privacy protection is no longer a major concern due to encryption — Privacy remains a major concern.

**Correct:** A, C


#### 13. In scientific data mining, what is a common challenge when dealing with data collected from diverse environments and periods?  
A) ✗ Lack of data volume — Usually large datasets are available.  
B) ✓ Inconsistencies and incompatibilities in data — Common issue due to diverse sources.  
C) ✗ Overabundance of labeled data — Labeling is often limited.  
D) ✗ Absence of complex data types — Complex data types are common.

**Correct:** B


#### 14. Which of the following best describes the concept of ubiquitous data mining?  
A) ✗ Data mining only applied in specialized research labs — Opposite of ubiquitous.  
B) ✓ Data mining embedded in everyday applications like online shopping — Correct definition.  
C) ✗ Data mining that requires explicit user interaction at all times — Often invisible or automatic.  
D) ✗ Data mining that is visible and transparent to all users — Often invisible.

**Correct:** B


#### 15. What is the primary purpose of using sequential pattern mining in retail customer analysis?  
A) ✗ To detect fraudulent transactions only — Fraud detection is one use but not primary.  
B) ✓ To investigate changes in customer consumption or loyalty over time — Main purpose.  
C) ✗ To cluster customers into demographic groups — Clustering is a different technique.  
D) ✗ To predict stock market trends — Not related to retail customer analysis.

**Correct:** B


#### 16. Which of the following are potential drawbacks of privacy-preserving data mining?  
A) ✓ Trade-off between data utility and privacy protection — Privacy often reduces data accuracy.  
B) ✗ Increased risk of data breaches — Privacy methods aim to reduce risk.  
C) ✓ Possible distortion of mining results — Privacy techniques can distort data.  
D) ✗ Complete elimination of privacy risks — Impossible to guarantee.

**Correct:** A, C


#### 17. How does distributed data mining contribute to privacy preservation?  
A) ✗ By centralizing all data in one secure location — Opposite of distributed mining.  
B) ✓ By partitioning data horizontally or vertically across multiple sites — True.  
C) ✗ By encrypting data before mining — Encryption is separate from distribution.  
D) ✗ By removing sensitive attributes from the dataset — Not necessarily part of distributed mining.

**Correct:** B


#### 18. Which of the following statements about recommender systems is false?  
A) ✗ Content-based filtering recommends items similar to those a user liked before — True statement.  
B) ✗ Collaborative filtering relies on the preferences of similar users — True statement.  
C) ✗ Hybrid approaches combine multiple recommendation techniques to improve accuracy — True statement.  
D) ✓ Recommender systems do not require any user data to function — False; user data is essential.

**Correct:** D


#### 19. What is a key reason why data mining tools must be scalable and interactive?  
A) ✓ To handle increasing data volumes and allow user-driven exploration — Core reason.  
B) ✗ To eliminate the need for domain-specific knowledge — Domain knowledge remains important.  
C) ✗ To ensure mining results are always 100% accurate — Accuracy cannot be guaranteed.  
D) ✗ To replace human decision-making entirely — Tools assist but do not replace humans.

**Correct:** A


#### 20. Which of the following best describes the relationship between data mining and social impacts?  
A) ✗ Data mining has no impact on privacy or security concerns — Incorrect; privacy is a major concern.  
B) ✓ Data mining can raise ethical issues related to unconstrained access to personal data — True.  
C) ✗ Data mining is only used for scientific purposes and does not affect society — False; it affects many sectors.  
D) ✗ Privacy-preserving techniques are irrelevant to social concerns — They are highly relevant.

**Correct:** B