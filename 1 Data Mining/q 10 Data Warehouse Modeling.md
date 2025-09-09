## 10. Data Warehouse Modeling

## Questions

#### 1. Which of the following characteristics best define a data warehouse?  
A) Subject-oriented, volatile, integrated, time-variant  
B) Subject-oriented, integrated, time-variant, nonvolatile  
C) Application-oriented, integrated, time-variant, nonvolatile  
D) Subject-oriented, integrated, current data only, nonvolatile  

#### 2. What is the primary reason for separating a data warehouse from operational databases?  
A) To reduce data redundancy in operational systems  
B) To optimize performance for both transaction processing and analytical queries  
C) To ensure data is updated in real-time for decision making  
D) To avoid the need for data cleaning and integration  

#### 3. In a star schema, which of the following statements are true?  
A) The fact table is connected to multiple dimension tables  
B) Dimension tables are normalized into smaller tables  
C) It is optimized for complex many-to-many relationships between dimensions  
D) It provides a simple and intuitive structure for querying  

#### 4. Which of the following best describes the difference between OLTP and OLAP systems?  
A) OLTP systems are designed for complex queries and historical data analysis  
B) OLAP systems are optimized for transaction processing and concurrency control  
C) OLTP systems handle current, detailed data; OLAP systems handle historical, summarized data  
D) OLAP systems require frequent data updates and transaction recovery  

#### 5. What does the term "grain" refer to in data warehouse design?  
A) The level of detail or atomicity of the data stored in the fact table  
B) The number of dimensions in a data cube  
C) The frequency of data refresh in the warehouse  
D) The type of aggregation applied to dimension tables  

#### 6. Which of the following are typical OLAP operations?  
A) Roll-up (drill-up)  
B) Drill-down (roll-down)  
C) Slice and dice  
D) Data cleaning  

#### 7. When a data warehouse is described as "time-variant," what does this imply?  
A) It only stores data for the current day  
B) It maintains historical data over long periods for trend analysis  
C) It updates data in real-time as transactions occur  
D) It stores data without any time dimension  

#### 8. Which of the following statements about slowly changing dimensions (SCD) are correct?  
A) Type 1 overwrites old data with new data  
B) Type 2 adds a new row to track changes over time  
C) Type 3 deletes old dimension records to save space  
D) Type 3 adds a new column to store previous attribute values  

#### 9. What is the main advantage of a fact constellation schema over a star schema?  
A) It simplifies queries by reducing the number of joins  
B) It supports multiple fact tables sharing dimension tables  
C) It normalizes all dimension tables to reduce redundancy  
D) It eliminates the need for dimension tables  

#### 10. Which of the following are challenges addressed by data cleaning in the ETL process?  
A) Resolving inconsistent naming conventions across sources  
B) Converting data formats and units to a common standard  
C) Aggregating data to higher levels of granularity  
D) Ensuring transactional consistency during updates  

#### 11. Which of the following best describes the role of metadata in a data warehouse?  
A) It stores the actual business data for analysis  
B) It defines the structure, lineage, and usage of warehouse data  
C) It contains only performance statistics of the warehouse system  
D) It is used exclusively for user authentication and security  

#### 12. What is a key difference between MOLAP and ROLAP architectures?  
A) MOLAP stores data in relational tables, ROLAP uses multidimensional arrays  
B) MOLAP pre-computes and stores aggregated data for fast access  
C) ROLAP is less scalable than MOLAP for large datasets  
D) ROLAP requires specialized storage engines not found in relational DBMS  

#### 13. Which of the following statements about data marts are true?  
A) Data marts always contain data independent of the enterprise warehouse  
B) Dependent data marts draw data directly from the enterprise warehouse  
C) Data marts are designed to serve specific user groups or departments  
D) Data marts eliminate the need for an enterprise data warehouse  

#### 14. Why is a data warehouse considered "nonvolatile"?  
A) Because data is frequently updated and deleted  
B) Because data is stable and only read, not changed by operational processes  
C) Because it supports real-time transaction processing  
D) Because it automatically archives old data to external storage  

#### 15. Which of the following best explains the concept of a "data cube"?  
A) A two-dimensional table with rows and columns  
B) A multidimensional array of data organized by dimensions and measures  
C) A flat file containing raw transactional data  
D) A normalized relational schema for operational databases  

#### 16. What is the purpose of the "apex cuboid" in a data cube lattice?  
A) It stores the most detailed, atomic data  
B) It represents the highest-level summary with no dimensions  
C) It contains only the metadata of the cube  
D) It is used to store data from external sources  

#### 17. Which of the following are reasons for using a bottom-up approach in data warehouse design?  
A) Rapid prototyping and early delivery of functional components  
B) Comprehensive planning before any data is collected  
C) Building small data marts first and integrating later  
D) Avoiding the need for ETL processes  

#### 18. In the context of OLAM (Online Analytical Mining), which of the following are advantages of integrating data mining with OLAP?  
A) Ability to perform mining on high-quality, cleaned data  
B) Real-time transactional updates during mining  
C) Combining exploratory analysis with mining functions like classification  
D) Eliminating the need for metadata management  

#### 19. Which of the following statements about the "slice and dice" OLAP operation are correct?  
A) Slice reduces the dimensionality by selecting a single value for one dimension  
B) Dice selects a subcube by choosing specific values from multiple dimensions  
C) Slice rotates the data cube to change the perspective  
D) Dice aggregates data to a higher level of hierarchy  

#### 20. Which of the following best describe the differences between operational databases and data warehouses?  
A) Operational databases are subject-oriented; data warehouses are application-oriented  
B) Operational databases contain current, detailed data; data warehouses contain historical, summarized data  
C) Operational databases support transaction processing; data warehouses support complex queries and analysis  
D) Operational databases are optimized for read-only access; data warehouses are optimized for frequent updates



<br>

## Answers

#### 1. Which of the following characteristics best define a data warehouse?  
A) ✗ Volatile is incorrect; data warehouses are nonvolatile.  
B) ✓ Correct: Subject-oriented, integrated, time-variant, and nonvolatile are key characteristics.  
C) ✗ Application-oriented is incorrect; warehouses are subject-oriented.  
D) ✗ Data warehouses store historical, not just current data.  

**Correct:** B


#### 2. What is the primary reason for separating a data warehouse from operational databases?  
A) ✗ Reducing redundancy is not the main reason.  
B) ✓ Correct: To optimize performance for both transaction processing and analytical queries.  
C) ✗ Warehouses do not require real-time updates.  
D) ✗ Data cleaning is essential in warehouses, not avoided.  

**Correct:** B


#### 3. In a star schema, which of the following statements are true?  
A) ✓ Correct: Fact table connects to multiple dimension tables.  
B) ✗ Normalization of dimension tables is characteristic of snowflake schema, not star.  
C) ✗ Star schema is simple, not optimized for complex many-to-many relationships.  
D) ✓ Correct: Star schema provides a simple, intuitive structure for querying.  

**Correct:** A, D


#### 4. Which of the following best describes the difference between OLTP and OLAP systems?  
A) ✗ OLTP is for transactions, not complex queries.  
B) ✗ OLAP is for analysis, not transaction processing.  
C) ✓ Correct: OLTP handles current, detailed data; OLAP handles historical, summarized data.  
D) ✗ OLAP is mostly read-only, not requiring frequent updates or recovery.  

**Correct:** C


#### 5. What does the term "grain" refer to in data warehouse design?  
A) ✓ Correct: Grain is the level of detail or atomicity of data in the fact table.  
B) ✗ Number of dimensions is unrelated to grain.  
C) ✗ Frequency of refresh is not grain.  
D) ✗ Aggregation type is not grain.  

**Correct:** A


#### 6. Which of the following are typical OLAP operations?  
A) ✓ Correct: Roll-up is a standard OLAP operation.  
B) ✓ Correct: Drill-down is the reverse of roll-up.  
C) ✓ Correct: Slice and dice are common OLAP operations.  
D) ✗ Data cleaning is part of ETL, not OLAP operations.  

**Correct:** A, B, C


#### 7. When a data warehouse is described as "time-variant," what does this imply?  
A) ✗ Warehouses store more than just current day data.  
B) ✓ Correct: They maintain historical data over long periods.  
C) ✗ Warehouses do not update data in real-time.  
D) ✗ Time dimension is essential, so data is not stored without time.  

**Correct:** B


#### 8. Which of the following statements about slowly changing dimensions (SCD) are correct?  
A) ✓ Correct: Type 1 overwrites old data.  
B) ✓ Correct: Type 2 adds new rows to track history.  
C) ✗ Type 3 does not delete records; it adds columns.  
D) ✓ Correct: Type 3 adds columns to store previous values.  

**Correct:** A, B, D


#### 9. What is the main advantage of a fact constellation schema over a star schema?  
A) ✗ Fact constellation usually involves more joins, not fewer.  
B) ✓ Correct: Supports multiple fact tables sharing dimension tables.  
C) ✗ Normalization of dimension tables is snowflake schema’s feature.  
D) ✗ Dimension tables are still required.  

**Correct:** B


#### 10. Which of the following are challenges addressed by data cleaning in the ETL process?  
A) ✓ Correct: Resolving inconsistent naming conventions is a key cleaning task.  
B) ✓ Correct: Converting formats and units is part of cleaning.  
C) ✗ Aggregation is a transformation step, not cleaning.  
D) ✗ Transactional consistency is handled by operational DBMS, not cleaning.  

**Correct:** A, B


#### 11. Which of the following best describes the role of metadata in a data warehouse?  
A) ✗ Metadata does not store business data itself.  
B) ✓ Correct: Metadata defines structure, lineage, and usage of data.  
C) ✗ Metadata includes more than performance stats.  
D) ✗ Metadata is not just for security/authentication.  

**Correct:** B


#### 12. What is a key difference between MOLAP and ROLAP architectures?  
A) ✗ MOLAP uses multidimensional arrays; ROLAP uses relational tables.  
B) ✓ Correct: MOLAP pre-computes and stores aggregated data for fast access.  
C) ✗ ROLAP is generally more scalable than MOLAP.  
D) ✗ ROLAP uses standard relational DBMS, no special storage engines needed.  

**Correct:** B


#### 13. Which of the following statements about data marts are true?  
A) ✗ Data marts can be dependent or independent; not always independent.  
B) ✓ Correct: Dependent data marts draw data from enterprise warehouse.  
C) ✓ Correct: Data marts serve specific user groups or departments.  
D) ✗ Data marts complement, not replace, enterprise warehouses.  

**Correct:** B, C


#### 14. Why is a data warehouse considered "nonvolatile"?  
A) ✗ Data is not frequently updated or deleted.  
B) ✓ Correct: Data is stable and only read, not changed by operations.  
C) ✗ Warehouses do not support real-time transaction processing.  
D) ✗ Archiving is separate from nonvolatility.  

**Correct:** B


#### 15. Which of the following best explains the concept of a "data cube"?  
A) ✗ A data cube is multidimensional, not just 2D.  
B) ✓ Correct: It is a multidimensional array organized by dimensions and measures.  
C) ✗ Raw transactional data is not a data cube.  
D) ✗ Normalized relational schema is not a data cube.  

**Correct:** B


#### 16. What is the purpose of the "apex cuboid" in a data cube lattice?  
A) ✗ Apex cuboid is the highest-level summary, not detailed data.  
B) ✓ Correct: It represents the highest-level summary with no dimensions.  
C) ✗ Metadata is separate from cuboids.  
D) ✗ External data is not stored in apex cuboid.  

**Correct:** B


#### 17. Which of the following are reasons for using a bottom-up approach in data warehouse design?  
A) ✓ Correct: Enables rapid prototyping and early delivery.  
B) ✗ Comprehensive planning is top-down approach.  
C) ✓ Correct: Builds small data marts first, then integrates.  
D) ✗ ETL is always required regardless of approach.  

**Correct:** A, C


#### 18. In the context of OLAM (Online Analytical Mining), which of the following are advantages of integrating data mining with OLAP?  
A) ✓ Correct: Mining on high-quality, cleaned data improves results.  
B) ✗ Real-time transactional updates are not typical during mining.  
C) ✓ Correct: Combines exploratory analysis with mining functions.  
D) ✗ Metadata management remains essential.  

**Correct:** A, C


#### 19. Which of the following statements about the "slice and dice" OLAP operation are correct?  
A) ✓ Correct: Slice selects a single value for one dimension, reducing dimensionality.  
B) ✓ Correct: Dice selects a subcube by choosing values from multiple dimensions.  
C) ✗ Pivot (rotate) changes perspective, not slice.  
D) ✗ Dice does not aggregate data; it filters data.  

**Correct:** A, B


#### 20. Which of the following best describe the differences between operational databases and data warehouses?  
A) ✗ Operational DBs are application-oriented; warehouses are subject-oriented.  
B) ✓ Correct: Operational DBs contain current, detailed data; warehouses contain historical, summarized data.  
C) ✓ Correct: Operational DBs support transaction processing; warehouses support complex queries.  
D) ✗ Operational DBs are optimized for updates; warehouses are optimized for read-only complex queries.  

**Correct:** B, C