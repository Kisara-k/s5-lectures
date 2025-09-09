## 9 NoSQL Examples

## Questions

#### 1. Which of the following are reasons behind the rise of the NoSQL movement?  
A) Need for schema rigidity and strict normalization  
B) Preference for open-source software  
C) Desire for greater scalability and throughput  
D) Object-relational mismatch in traditional databases  

#### 2. Firestore’s data model is best described as:  
A) A key-value store with fixed schemas  
B) A document model with collections and subcollections  
C) A graph database with labeled nodes and edges  
D) A relational database with tables and foreign keys  

#### 3. In Firestore, which of the following statements about subcollections is true?  
A) Subcollections can only be nested one level deep  
B) Subcollections can be nested up to 100 levels deep  
C) Subcollections must have the same schema as their parent document  
D) Subcollections are used to store hierarchical data under documents  

#### 4. What are the limitations of Firestore’s write throughput?  
A) Unlimited writes per second  
B) Maximum of 10,000 writes per second  
C) Write throughput depends on the number of indexes  
D) Write throughput is limited because Firestore only runs on Google Cloud  

#### 5. Which Firestore query methods are used to filter, sort, and limit results respectively?  
A) `where()`, `order_by()`, `limit()`  
B) `filter()`, `sort()`, `count()`  
C) `select()`, `group_by()`, `top()`  
D) `match()`, `order()`, `limit()`  

#### 6. When updating a Firestore document, which of the following are valid operations?  
A) Using `firestore.Increment()` to atomically increase a numeric field  
B) Using `firestore.DELETE_FIELD` to remove a field  
C) Using `set()` to partially update a document without overwriting  
D) Using `update()` to modify specific fields without affecting others  

#### 7. In MongoDB, what does it mean that the database is "schemaless"?  
A) MongoDB enforces a strict schema on all documents  
B) Schema is applied only when reading data, not when writing  
C) Documents in the same collection must have identical fields  
D) MongoDB does not store any metadata about document structure  

#### 8. Which of the following are true about MongoDB’s sharding mechanism?  
A) Sharding automatically balances data across shards without configuration  
B) The shard key determines how documents are partitioned into chunks  
C) Documents with the same shard key are stored in the same chunk  
D) Each shard is deployed as a replica set for high availability  

#### 9. What is the maximum size of a MongoDB document, including nested objects?  
A) 1 MB  
B) 16 MB  
C) 64 MB  
D) Unlimited  

#### 10. Which MongoDB query operators are used for range queries?  
A) `$lte` and `$gte`  
B) `$and` and `$or`  
C) `$in` and `$nin`  
D) `$eq` and `$ne`  

#### 11. In Neo4j, what does the labeled property graph model consist of?  
A) Nodes and relationships, both with labels and properties  
B) Tables and rows with foreign keys  
C) Documents with nested key-value pairs  
D) Key-value pairs with no relationships  

#### 12. Which of the following Cypher commands are used to create nodes and relationships?  
A) `CREATE`  
B) `MATCH`  
C) `MERGE`  
D) `DELETE`  

#### 13. How does Neo4j handle scalability for reads and writes?  
A) Scales reads well through distributed architecture  
B) Supports automatic sharding for writes  
C) Has limited scalability for writes due to lack of sharding  
D) Uses replication to scale writes horizontally  

#### 14. In Firestore, what happens if you run a query without the required index?  
A) The query will succeed but be slow  
B) The query will fail and return an error  
C) Firestore automatically creates the index on the fly  
D) The query returns partial results without sorting  

#### 15. Which of the following are valid Firestore data types?  
A) String, Number, Boolean, Timestamp  
B) Array, Map, Geopoint  
C) ObjectId, BSON, Binary  
D) JSON, XML, CSV  

#### 16. When modeling data in Firestore, which of the following design guidelines should be followed?  
A) Group entities based on expected access patterns  
B) Convert top-level entities into collections  
C) Use relational foreign keys to link documents  
D) Use primary key columns or concatenations as document IDs  

#### 17. Which of the following statements about MongoDB transactions is true?  
A) MongoDB does not support multi-document transactions  
B) MongoDB supports ACID transactions across multiple documents  
C) Transactions are only supported in the cloud version (Atlas)  
D) Transactions automatically shard data across clusters  

#### 18. In Neo4j, which Cypher query would you use to find all permissions associated with a person named "Ethan"?  
A) `MATCH (p:Person {name: "Ethan"})-[r*]->(m:Permission) RETURN r, m.name`  
B) `CREATE (p:Person {name: "Ethan"})-[:HAS_PERMISSION]->(m:Permission)`  
C) `DELETE (p:Person {name: "Ethan"})`  
D) `MATCH (p:Person)-[:HAS_ROLE]->(r:Role) RETURN p, r`  

#### 19. What is the role of the shard key in MongoDB sharding?  
A) It determines the physical location of the database server  
B) It is used to partition documents into chunks for distribution  
C) It is a unique identifier for each document  
D) It controls replication between nodes  

#### 20. Which of the following are true about Firestore’s batch writes?  
A) A batch can contain writes to multiple collections  
B) A batch can contain more than 1000 documents  
C) Batch writes are atomic; either all succeed or none do  
D) Batch writes can only update existing documents, not create new ones



<br>

## Answers

#### 1. Which of the following are reasons behind the rise of the NoSQL movement?  
A) ✗ NoSQL favors schema flexibility, not rigidity.  
B) ✓ Open-source preference is a key driver.  
C) ✓ Scalability and throughput needs drove NoSQL adoption.  
D) ✓ Object-relational mismatch motivated NoSQL use.  

**Correct:** B, C, D


#### 2. Firestore’s data model is best described as:  
A) ✗ Firestore is not a simple key-value store with fixed schemas.  
B) ✓ Firestore uses a document model with collections and subcollections.  
C) ✗ Neo4j is a graph database, not Firestore.  
D) ✗ Firestore is not relational.  

**Correct:** B


#### 3. In Firestore, which of the following statements about subcollections is true?  
A) ✗ Subcollections can be nested deeper than one level.  
B) ✓ Maximum nesting depth is 100 levels.  
C) ✗ Documents in subcollections can have different schemas.  
D) ✓ Subcollections store hierarchical data under documents.  

**Correct:** B, D


#### 4. What are the limitations of Firestore’s write throughput?  
A) ✗ Writes are limited, not unlimited.  
B) ✓ Max 10,000 writes per second is a known limit.  
C) ✓ Indexes affect write performance because they must be updated.  
D) ✓ Firestore only runs on Google Cloud, limiting deployment options.  

**Correct:** B, C, D


#### 5. Which Firestore query methods are used to filter, sort, and limit results respectively?  
A) ✓ `where()`, `order_by()`, `limit()` are correct Firestore methods.  
B) ✗ These are not Firestore method names.  
C) ✗ These are SQL-like but not Firestore methods.  
D) ✗ `match()` is Neo4j, not Firestore.  

**Correct:** A


#### 6. When updating a Firestore document, which of the following are valid operations?  
A) ✓ `firestore.Increment()` atomically increments numeric fields.  
B) ✓ `firestore.DELETE_FIELD` removes a field.  
C) ✗ `set()` overwrites the whole document unless merge option is used.  
D) ✓ `update()` modifies specific fields without overwriting the entire document.  

**Correct:** A, B, D


#### 7. In MongoDB, what does it mean that the database is "schemaless"?  
A) ✗ MongoDB does not enforce strict schemas on writes.  
B) ✓ Schema is applied on reads, not enforced on writes.  
C) ✗ Documents in a collection can have different fields.  
D) ✗ MongoDB stores metadata about documents internally.  

**Correct:** B


#### 8. Which of the following are true about MongoDB’s sharding mechanism?  
A) ✗ Sharding requires configuration; it’s not automatic.  
B) ✓ Shard key determines document partitioning into chunks.  
C) ✓ Documents with the same shard key are stored in the same chunk.  
D) ✓ Each shard is a replica set for high availability.  

**Correct:** B, C, D


#### 9. What is the maximum size of a MongoDB document, including nested objects?  
A) ✗ 1 MB is too small.  
B) ✓ 16 MB is the documented max size.  
C) ✗ 64 MB is incorrect.  
D) ✗ MongoDB documents have a size limit.  

**Correct:** B


#### 10. Which MongoDB query operators are used for range queries?  
A) ✓ `$lte` (less than or equal) and `$gte` (greater than or equal) are range operators.  
B) ✗ `$and` and `$or` are boolean operators, not range.  
C) ✗ `$in` and `$nin` are membership operators.  
D) ✗ `$eq` and `$ne` are equality operators, not range.  

**Correct:** A


#### 11. In Neo4j, what does the labeled property graph model consist of?  
A) ✓ Nodes and relationships both have labels and properties.  
B) ✗ Tables and rows are relational concepts.  
C) ✗ Documents are NoSQL document stores, not graphs.  
D) ✗ Key-value pairs without relationships do not describe Neo4j.  

**Correct:** A


#### 12. Which of the following Cypher commands are used to create nodes and relationships?  
A) ✓ `CREATE` is used to add nodes and relationships.  
B) ✗ `MATCH` is for querying, not creating.  
C) ✓ `MERGE` creates or matches nodes/relationships.  
D) ✗ `DELETE` removes nodes or relationships.  

**Correct:** A, C


#### 13. How does Neo4j handle scalability for reads and writes?  
A) ✓ Scales reads well via distributed architecture.  
B) ✗ Neo4j does not support automatic sharding for writes.  
C) ✓ Write scalability is limited due to no sharding.  
D) ✗ Replication helps availability but not horizontal write scaling.  

**Correct:** A, C


#### 14. In Firestore, what happens if you run a query without the required index?  
A) ✗ Query will not succeed or be slow; it fails.  
B) ✓ Query fails with an error if index is missing.  
C) ✗ Firestore does not auto-create indexes on the fly.  
D) ✗ Partial results are not returned; query fails outright.  

**Correct:** B


#### 15. Which of the following are valid Firestore data types?  
A) ✓ String, Number, Boolean, Timestamp are primitive types.  
B) ✓ Array, Map, Geopoint are complex types supported.  
C) ✗ ObjectId and BSON are MongoDB-specific types.  
D) ✗ JSON, XML, CSV are data formats, not Firestore types.  

**Correct:** A, B


#### 16. When modeling data in Firestore, which of the following design guidelines should be followed?  
A) ✓ Group entities based on expected access patterns.  
B) ✓ Convert top-level entities into collections.  
C) ✗ Firestore does not use relational foreign keys.  
D) ✓ Use primary keys or concatenations as document IDs.  

**Correct:** A, B, D


#### 17. Which of the following statements about MongoDB transactions is true?  
A) ✗ MongoDB supports multi-document transactions.  
B) ✓ MongoDB supports ACID transactions across multiple documents.  
C) ✗ Transactions are supported both on-prem and cloud.  
D) ✗ Transactions do not shard data automatically.  

**Correct:** B


#### 18. In Neo4j, which Cypher query would you use to find all permissions associated with a person named "Ethan"?  
A) ✓ Correct pattern to traverse relationships to permissions.  
B) ✗ This creates nodes, not queries.  
C) ✗ Deletes nodes, not queries.  
D) ✗ Returns roles, not permissions.  

**Correct:** A


#### 19. What is the role of the shard key in MongoDB sharding?  
A) ✗ It does not determine physical server location directly.  
B) ✓ It partitions documents into chunks for distribution.  
C) ✗ `_id` is the unique identifier, not the shard key necessarily.  
D) ✗ Replication controls redundancy, not shard key.  

**Correct:** B


#### 20. Which of the following are true about Firestore’s batch writes?  
A) ✓ Batches can include writes to multiple collections.  
B) ✗ Maximum batch size is 500 documents, not more.  
C) ✓ Batch writes are atomic; all succeed or none do.  
D) ✗ Batches can create new documents, not just update.  

**Correct:** A, C, D