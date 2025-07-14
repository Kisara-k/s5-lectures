## 08 NoSQL

[Study Notes](#study-notes)

[Questions](#questions)



### Key Points



#### 1. 🛑 NoSQL Definition  
- NoSQL means "Not Only SQL" and refers to any database that is **not a relational database**.  
- The term originated from meetups and conferences around 2009 involving creators of emerging databases.  
- NoSQL databases are often called **non-relational databases**.

#### 2. 📈 Reasons for NoSQL Popularity  
- NoSQL addresses challenges of **massive data volumes** that traditional RDBMS cannot scale to.  
- It handles **highly connected data** and **semi-structured data** with flexible schemas.  
- NoSQL supports **scalable, distributed architectures** across many servers and geographic locations.  
- It provides **low latency, high availability, and elasticity** at low cost.  
- NoSQL relaxes ACID properties to improve scalability and availability.

#### 3. 🔄 ACID Properties in SQL Databases  
- **Atomicity:** Transactions complete fully or not at all.  
- **Consistency:** Transactions move the database from one valid state to another.  
- **Isolation:** Changes are not visible until a transaction commits.  
- **Durability:** Committed changes survive failures.

#### 4. ⚖️ CAP Theorem  
- A distributed system can only guarantee **two** of the following three:  
  - **Consistency:** All nodes see the same data simultaneously.  
  - **Availability:** Every request receives a response, even if some nodes fail.  
  - **Partition Tolerance:** The system continues to operate despite network failures.

#### 5. 🧩 BASE Model in NoSQL  
- **Basically Available:** The system guarantees availability.  
- **Soft state:** The system state may change over time without input.  
- **Eventually Consistent:** The system will become consistent over time, but not immediately.

#### 6. 🗃️ NoSQL Database Types  
- **Column Store:** Stores data by columns; efficient for queries accessing few columns (e.g., Google BigTable, HBase).  
- **Key-Value Store:** Stores data as key-value pairs; fast lookups by key but limited query capabilities (e.g., Amazon Dynamo, Project Voldemort).  
- **Document Store:** Stores schema-free documents in JSON or XML; supports nested data and replication (e.g., CouchDB, MongoDB).  
- Other types include Graph, XML, Object-Oriented, and Codasyl databases.

#### 7. 🏗️ Google BigTable Characteristics  
- Sparse, distributed, persistent multidimensional sorted map with (row, column, timestamp) keys.  
- Uses column families to group columns for storage and compression.  
- Single master server assigns tablets to many tablet servers.  
- Supports versioning with timestamps and automated garbage collection.

#### 8. 🔑 Amazon Dynamo Characteristics  
- Peer-to-peer key-value store with consistent hashing and quorum reads.  
- Supports object versioning and eventual consistency.  
- Designed for simple queries with unique keys and no complex joins.  
- Prioritizes low latency, high throughput, and decentralized architecture.

#### 9. 📝 Data Manipulation in NoSQL  
- NoSQL databases often use **procedural programming languages** (Java, C, etc.) for queries instead of declarative SQL.  
- Insert and update operations are typically **asynchronous** and **versioned**.  
- No query optimizer; applications specify exact data access paths.

#### 10. ✅ Advantages of NoSQL  
- Massive scalability across thousands of servers.  
- High availability and fault tolerance.  
- Schema flexibility for semi-structured or evolving data.  
- Lower cost and predictable elasticity.

#### 11. ❌ Disadvantages of NoSQL  
- Limited query capabilities and lack of complex joins.  
- Eventual consistency complicates application logic.  
- No standard query language or API.  
- Potential portability and security issues.

#### 12. 📊 NoSQL Adoption and Trends  
- NoSQL databases reject the overhead of ACID transactions and complex SQL.  
- They favor **simple APIs**, **schema-free design**, and **eventual consistency**.  
- Many traditional RDBMS vendors have integrated NoSQL components to remain competitive.



<br>

## Study Notes



### 1. 📚 Introduction to NoSQL Databases

In the world of data management, **NoSQL databases** have emerged as an important alternative to traditional relational databases (RDBMS). The term **NoSQL** originally meant "No SQL," implying a rejection of the SQL language and relational model. However, it has evolved to mean **"Not Only SQL"**, emphasizing that these databases are not strictly relational but can coexist with SQL databases.

NoSQL databases are defined primarily by what they are **not**: they are **non-relational databases**. This means they do not use the traditional table-based structure of relational databases. The term was popularized around 2009 during meetups and conferences involving creators of new database technologies designed to handle modern data challenges.

#### Why did NoSQL databases become popular?

Four main trends drove the rise of NoSQL:

- **Data Size:** The explosion of data volumes, especially with web-scale companies like Google and Facebook, made traditional databases struggle to scale.
- **Connectedness:** Modern applications require handling highly connected data, which relational models find cumbersome.
- **Semi-structured Data:** Unlike the rigid schemas of SQL databases, modern data is often semi-structured or unstructured, requiring flexible schemas.
- **Architecture:** Traditional RDBMS architectures have limitations in scalability, availability, and geographic distribution, which NoSQL databases address.


### 2. ⚙️ Understanding SQL Databases and Their Characteristics

Before diving deeper into NoSQL, it’s important to understand the basics of **SQL databases**:

- **Data Storage:** Data is stored in tables with rows and columns.
- **Relationships:** Relationships between data are represented explicitly using keys (primary and foreign keys).
- **Languages:** SQL databases use **Data Manipulation Language (DML)** for querying and modifying data (e.g., SELECT, INSERT, UPDATE, DELETE) and **Data Definition Language (DDL)** for defining schemas and constraints.
- **Transactions:** SQL databases support **ACID** properties to ensure reliable transactions:
  - **Atomicity:** All parts of a transaction succeed or none do.
  - **Consistency:** Transactions move the database from one valid state to another.
  - **Isolation:** Transactions do not interfere with each other.
  - **Durability:** Once committed, changes survive failures.
- **Physical Layer Abstraction:** Applications specify *what* data they want, not *how* to get it. The database engine optimizes queries and manages physical storage.


### 3. 🚀 Why NoSQL? The Limitations of RDBMS and New Requirements

Traditional relational databases were designed decades ago for different types of applications. Modern web applications have different needs:

- **Scalability:** RDBMS struggle to scale horizontally across many servers.
- **Latency:** Web apps require low and predictable response times.
- **Availability:** Systems must remain operational even if some servers fail.
- **Flexible Schemas:** Data formats evolve rapidly, and rigid schemas slow down development.
- **Geographic Distribution:** Data must be replicated across multiple data centers worldwide.

NoSQL databases address these by relaxing some traditional guarantees (like strong consistency) and focusing on **scalability, availability, and flexibility**.


### 4. 🔄 CAP Theorem and BASE Model: Trade-offs in Distributed Systems

In distributed databases, the **CAP theorem** states that a system can only guarantee two of the following three properties simultaneously:

- **Consistency:** All nodes see the same data at the same time.
- **Availability:** Every request receives a response, even if some nodes fail.
- **Partition Tolerance:** The system continues to operate despite network failures between nodes.

NoSQL databases often prioritize **Availability** and **Partition Tolerance** over strict Consistency, leading to the **BASE** model:

- **Basically Available:** The system guarantees availability.
- **Soft state:** The system state may change over time without input.
- **Eventually Consistent:** The system will become consistent over time, but not immediately.

This contrasts with the ACID model of SQL databases, which emphasizes strong consistency and transaction integrity.


### 5. 🗃️ Types of NoSQL Databases and Their Characteristics

NoSQL databases come in several types, each optimized for different use cases:

#### Column Store Databases
- Store data by columns rather than rows.
- Efficient for queries that access only a few columns.
- Example: **Google BigTable**, **HBase**, **Ingres VectorWise**.
- Data is stored in column families, compressed together for efficiency.
- Good for large-scale, sparse data.

#### Key-Value Stores
- Store data as simple key-value pairs, like a hash table.
- Very fast for lookups by key.
- Limited query capabilities (usually exact key matches only).
- Examples: **Amazon Dynamo**, **Project Voldemort**, **MemCacheDB**.
- Used for session management, user profiles, caching.

#### Document Stores
- Store data as documents, typically in JSON or XML format.
- Schema-free, allowing flexible and evolving data structures.
- Support complex nested data.
- Examples: **CouchDB**, **MongoDB**.
- Support replication and versioning.
- Use MapReduce for indexing and querying large datasets.

#### Other Types
- **Graph Databases:** Optimized for highly connected data (e.g., social networks).
- **XML Databases:** Store and query XML documents.
- **Object-Oriented Databases:** Store objects directly.
- **Codasyl Databases:** Older network database model.


### 6. 🏗️ Deep Dive: Google BigTable and Dynamo Examples

#### Google BigTable
- A **sparse, distributed, persistent multidimensional sorted map**.
- Data model includes rows, columns, and timestamps.
- Rows are sorted by key and partitioned into tablets for efficient range scans.
- Column families group related columns for storage and compression.
- Uses a single master server to assign tablets to many tablet servers.
- Designed for scalability and high availability.

#### Amazon Dynamo
- A **peer-to-peer key-value store** designed for high availability and scalability.
- Uses consistent hashing to distribute data.
- Supports object versioning and quorum reads for eventual consistency.
- Designed for simple query models with unique keys and no complex joins.
- Prioritizes low latency and fault tolerance.


### 7. 📝 Data Manipulation and Querying in NoSQL

Unlike SQL databases, NoSQL databases often:

- Use **procedural programming languages** (Java, C, etc.) for data retrieval.
- Lack a declarative query language like SQL.
- Do not have a query optimizer; applications specify exactly how to access data.
- Support **asynchronous inserts and updates**, meaning writes do not wait for confirmation.
- Use **versioning** and **optimistic concurrency** to handle conflicts.


### 8. ⚖️ Advantages and Disadvantages of NoSQL

#### Advantages
- **Massive scalability:** Can handle huge volumes of data across many servers.
- **High availability:** Designed to remain operational despite failures.
- **Lower cost:** Often cheaper to scale horizontally than traditional RDBMS.
- **Schema flexibility:** Can handle semi-structured or evolving data easily.
- **Elasticity:** Can grow or shrink capacity predictably.

#### Disadvantages
- **Limited query capabilities:** Complex queries and joins are difficult or unsupported.
- **Eventual consistency:** Programming for eventual consistency is more complex.
- **No standardization:** Each NoSQL database has its own API and query language.
- **Portability issues:** Moving data between NoSQL systems can be challenging.
- **Security:** Access control and security models may be less mature.


### 9. 🔍 Summary and Current Trends

NoSQL databases emerged to meet the demands of modern web-scale applications that require:

- Handling **big data** volumes.
- **Distributed architectures** across many servers and data centers.
- Flexible, **schema-less data models**.
- High **availability** and **scalability** at low cost.
- Relaxed consistency models (BASE) instead of strict ACID transactions.

Many traditional relational database vendors have incorporated NoSQL features to stay competitive, reflecting the growing importance of NoSQL technologies.


### 📚 Recommended Reading

- *CouchDB The Definitive Guide* by J. Chris Anderson et al.
- *Hadoop The Definitive Guide* by Tom White
- *MongoDB The Definitive Guide* by Kristina Chodorow and Michael Dirolf



<br>

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

