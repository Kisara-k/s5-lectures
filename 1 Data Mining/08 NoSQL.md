## 8. NoSQL

## Key Points

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