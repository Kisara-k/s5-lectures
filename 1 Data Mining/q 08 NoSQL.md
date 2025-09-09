## 8. NoSQL

## Questions

#### 1. What does the term "NoSQL" primarily signify?  
A) A database that completely rejects SQL and relational models  
B) A database that is not relational or uses alternative data models  
C) A database that supports only SQL queries  
D) A database designed for web-scale, distributed data storage  

#### 2. Which of the following trends contributed to the rise of NoSQL databases?  
A) Increasing data size and volume  
B) The need for strict ACID transactions in all applications  
C) The rise of semi-structured and flexible data formats  
D) Limitations of traditional RDBMS architectures in scalability  

#### 3. Which of the following are characteristics of SQL databases?  
A) Data stored in tables with rows and columns  
B) Schema defined upfront and strictly enforced  
C) Eventual consistency as a core property  
D) Support for ACID transactions  

#### 4. According to the CAP theorem, a distributed system can guarantee only two of the following three properties simultaneously. Which are they?  
A) Consistency  
B) Availability  
C) Partition Tolerance  
D) Scalability  

#### 5. The BASE model in NoSQL databases emphasizes:  
A) Strong consistency and atomic transactions  
B) Basically Available, Soft state, Eventually Consistent  
C) Immediate consistency across all nodes  
D) Complex query optimization  

#### 6. Which of the following are typical advantages of NoSQL databases?  
A) Massive horizontal scalability  
B) Strong ACID compliance  
C) Flexible, schema-less data models  
D) Predictable elasticity and high availability  

#### 7. What are common disadvantages or challenges when using NoSQL databases?  
A) Limited query capabilities compared to SQL  
B) Eventual consistency complicates application logic  
C) Standardized query language across all NoSQL systems  
D) Potential portability issues between different NoSQL implementations  

#### 8. In a column store NoSQL database, data is stored:  
A) By rows, with all columns of a row stored together  
B) By columns, with each storage block containing data from one column  
C) As key-value pairs without any column structure  
D) In documents with nested JSON or XML  

#### 9. Google BigTable’s data model includes which of the following features?  
A) Rows identified by arbitrary string keys  
B) Columns grouped into families for storage and compression  
C) Strong ACID transactions across all tablets  
D) Multiple versions of each cell identified by timestamps  

#### 10. Which of the following statements about Amazon Dynamo are true?  
A) It uses consistent hashing to distribute data  
B) It guarantees strong consistency for all reads and writes  
C) It is a peer-to-peer key-value store designed for high availability  
D) It supports complex multi-table joins  

#### 11. Document stores like CouchDB and MongoDB typically:  
A) Require a fixed schema defined before data insertion  
B) Store data as JSON or similar document formats  
C) Support joins and foreign key constraints natively  
D) Use MapReduce techniques for indexing and querying  

#### 12. Which of the following best describe the query capabilities of most NoSQL databases?  
A) Declarative, set-based query languages like SQL  
B) Procedural access paths specified by the application  
C) Query optimization engines that abstract physical storage  
D) Limited or no support for complex joins  

#### 13. What is a key difference between ACID and BASE transaction models?  
A) ACID prioritizes availability over consistency  
B) BASE allows for eventual consistency rather than immediate consistency  
C) ACID transactions are typically faster and simpler to implement  
D) BASE transactions guarantee atomicity and durability  

#### 14. Why is schema flexibility important in NoSQL databases?  
A) It allows data models to evolve without costly migrations  
B) It enforces strict data integrity constraints  
C) It simplifies the use of complex joins  
D) It supports semi-structured and sparse data  

#### 15. Which of the following are true about the physical layer abstraction in SQL databases?  
A) Applications specify what data they want, not how to get it  
B) The physical storage can be changed without modifying application code  
C) Query optimization is handled by the database engine  
D) Applications must manage data partitioning and replication manually  

#### 16. Which NoSQL database type is most suitable for managing user sessions or caching frequently accessed small data items?  
A) Column Store  
B) Key-Value Store  
C) Document Store  
D) Graph Database  

#### 17. Which of the following statements about MapReduce in NoSQL systems is correct?  
A) It is a built-in feature of all NoSQL databases  
B) It involves a Map phase that extracts key-value pairs and a Reduce phase that merges them  
C) It guarantees immediate consistency of query results  
D) It is typically implemented by application developers, not the database engine  

#### 18. What is a major architectural limitation of traditional RDBMS that NoSQL databases address?  
A) Lack of support for SQL queries  
B) Difficulty scaling horizontally across many servers  
C) Inability to store any structured data  
D) Lack of transaction support  

#### 19. Which of the following are true about the consistency property in CAP theorem?  
A) It means all nodes see the same data at the same time  
B) It is equivalent to availability in distributed systems  
C) It is similar to atomicity in ACID transactions  
D) It guarantees no stale data is ever read  

#### 20. Why might eventual consistency be challenging for developers using NoSQL databases?  
A) It requires applications to handle stale or out-of-date data  
B) It eliminates the need for concurrency control  
C) It simplifies client application logic  
D) It forces synchronous writes to all nodes before responding



<br>

## Answers

#### 1. What does the term "NoSQL" primarily signify?  
A) ✗ It’s not a complete rejection of SQL, but an alternative approach  
B) ✓ Correct: NoSQL means non-relational or alternative data models  
C) ✗ NoSQL databases do not only support SQL queries  
D) ✓ Correct: NoSQL was designed for web-scale, distributed data storage  

**Correct:** B, D


#### 2. Which of the following trends contributed to the rise of NoSQL databases?  
A) ✓ Correct: Data size explosion is a key driver  
B) ✗ NoSQL often relaxes ACID, so strict ACID is not a driver  
C) ✓ Correct: Semi-structured data needs flexible schemas  
D) ✓ Correct: RDBMS architecture limits scalability  

**Correct:** A, C, D


#### 3. Which of the following are characteristics of SQL databases?  
A) ✓ Correct: Tables with rows and columns are fundamental  
B) ✓ Correct: Schema is defined upfront and enforced  
C) ✗ SQL databases emphasize strong consistency, not eventual consistency  
D) ✓ Correct: ACID transactions are core to SQL databases  

**Correct:** A, B, D


#### 4. According to the CAP theorem, a distributed system can guarantee only two of the following three properties simultaneously. Which are they?  
A) ✓ Correct: Consistency is one of the three properties  
B) ✓ Correct: Availability is one of the three properties  
C) ✓ Correct: Partition tolerance is one of the three properties  
D) ✗ Scalability is important but not part of CAP theorem  

**Correct:** A, B, C


#### 5. The BASE model in NoSQL databases emphasizes:  
A) ✗ This describes ACID, not BASE  
B) ✓ Correct: BASE stands for Basically Available, Soft state, Eventually Consistent  
C) ✗ BASE allows eventual, not immediate consistency  
D) ✗ BASE does not focus on complex query optimization  

**Correct:** B


#### 6. Which of the following are typical advantages of NoSQL databases?  
A) ✓ Correct: NoSQL scales horizontally very well  
B) ✗ NoSQL usually relaxes ACID compliance  
C) ✓ Correct: Schema flexibility is a key advantage  
D) ✓ Correct: Elasticity and availability are strengths  

**Correct:** A, C, D


#### 7. What are common disadvantages or challenges when using NoSQL databases?  
A) ✓ Correct: Query capabilities are limited compared to SQL  
B) ✓ Correct: Eventual consistency complicates programming  
C) ✗ NoSQL lacks standard query languages, so this is false  
D) ✓ Correct: Portability can be an issue due to lack of standards  

**Correct:** A, B, D


#### 8. In a column store NoSQL database, data is stored:  
A) ✗ This describes row stores, not column stores  
B) ✓ Correct: Column stores store data by columns in blocks  
C) ✗ Key-value stores do this, not column stores  
D) ✗ Document stores use JSON/XML, not column stores  

**Correct:** B


#### 9. Google BigTable’s data model includes which of the following features?  
A) ✓ Correct: Row keys are arbitrary strings  
B) ✓ Correct: Columns grouped into families for compression  
C) ✗ BigTable does not support full ACID transactions  
D) ✓ Correct: Multiple versions per cell with timestamps  

**Correct:** A, B, D


#### 10. Which of the following statements about Amazon Dynamo are true?  
A) ✓ Correct: Uses consistent hashing for data distribution  
B) ✗ Dynamo uses eventual consistency, not strong consistency  
C) ✓ Correct: Peer-to-peer key-value store designed for availability  
D) ✗ Dynamo does not support complex joins  

**Correct:** A, C


#### 11. Document stores like CouchDB and MongoDB typically:  
A) ✗ They are schema-free, no fixed schema required  
B) ✓ Correct: Store data as JSON or similar documents  
C) ✗ No native support for joins or foreign keys  
D) ✓ Correct: Use MapReduce for indexing and querying  

**Correct:** B, D


#### 12. Which of the following best describe the query capabilities of most NoSQL databases?  
A) ✗ NoSQL generally lacks declarative, set-based query languages  
B) ✓ Correct: Applications specify procedural access paths  
C) ✗ No query optimizer is typically present in NoSQL  
D) ✓ Correct: Complex joins are usually unsupported  

**Correct:** B, D


#### 13. What is a key difference between ACID and BASE transaction models?  
A) ✗ ACID prioritizes consistency over availability  
B) ✓ Correct: BASE allows eventual consistency, not immediate  
C) ✗ ACID transactions are more complex and slower  
D) ✗ BASE does not guarantee atomicity or durability  

**Correct:** B


#### 14. Why is schema flexibility important in NoSQL databases?  
A) ✓ Correct: Allows evolving data models without costly migrations  
B) ✗ Schema flexibility means less strict integrity constraints  
C) ✗ Schema flexibility does not simplify joins (which are rare)  
D) ✓ Correct: Supports semi-structured and sparse data  

**Correct:** A, D


#### 15. Which of the following are true about the physical layer abstraction in SQL databases?  
A) ✓ Correct: Applications specify *what*, not *how*  
B) ✓ Correct: Physical storage can change without app changes  
C) ✓ Correct: Query optimization is handled by the engine  
D) ✗ Applications do not manage partitioning/replication manually  

**Correct:** A, B, C


#### 16. Which NoSQL database type is most suitable for managing user sessions or caching frequently accessed small data items?  
A) ✗ Column stores are for analytical workloads, not sessions  
B) ✓ Correct: Key-value stores are ideal for fast lookups like sessions  
C) ✗ Document stores are more complex than needed for sessions  
D) ✗ Graph databases are for connected data, not sessions  

**Correct:** B


#### 17. Which of the following statements about MapReduce in NoSQL systems is correct?  
A) ✗ Not all NoSQL databases have built-in MapReduce  
B) ✓ Correct: Map extracts key-value pairs, Reduce merges them  
C) ✗ MapReduce does not guarantee immediate consistency  
D) ✓ Correct: Usually implemented by application developers  

**Correct:** B, D


#### 18. What is a major architectural limitation of traditional RDBMS that NoSQL databases address?  
A) ✗ RDBMS do support SQL queries  
B) ✓ Correct: RDBMS struggle with horizontal scaling across many servers  
C) ✗ RDBMS can store structured data well  
D) ✗ RDBMS have strong transaction support  

**Correct:** B


#### 19. Which of the following are true about the consistency property in CAP theorem?  
A) ✓ Correct: Consistency means all nodes see the same data simultaneously  
B) ✗ Consistency is different from availability  
C) ✓ Correct: Consistency is similar to atomicity in ACID  
D) ✗ Stale data can be read in eventually consistent systems  

**Correct:** A, C


#### 20. Why might eventual consistency be challenging for developers using NoSQL databases?  
A) ✓ Correct: Applications must handle stale or out-of-date data  
B) ✗ Eventual consistency requires concurrency control, not eliminates it  
C) ✗ It complicates, not simplifies, client logic  
D) ✗ Writes are asynchronous, not forced synchronous  

**Correct:** A