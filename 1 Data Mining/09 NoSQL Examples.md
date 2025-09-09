## 9. NoSQL Examples

## Key Points

#### 1. 🚀 NoSQL Movement
- NoSQL databases address the need for greater scalability, throughput, and response time.
- They provide more expressive data models and schema flexibility compared to relational databases.
- NoSQL helps resolve the object-relational mismatch.
- Preference for open-source software is a driver behind NoSQL adoption.

#### 2. 🔥 Firestore Overview
- Firestore is a fully serverless, distributed document database running on Google Cloud.
- Supports ACID transactions using Spanner technology.
- Designed for mobile, web, and IoT applications.
- Implements a document model with collections and subcollections (max nesting depth = 100).
- Write throughput limit is approximately 10,000 writes per second.
- Documents are collections of typed key-value pairs (primitive and complex types).
- All queries require indexes; missing indexes cause query failure.

#### 3. 🔥 Firestore Data Operations
- Documents have unique string identifiers.
- `set` method converts Python dictionaries into Firestore documents.
- Batch writes can include up to 500 documents across multiple collections.
- Reading uses `get` for single documents and `stream` for collections.
- Query filtering uses `where`, sorting uses `order_by`, and limiting uses `limit`.
- Updates can increment numeric fields atomically and delete fields using `firestore.DELETE_FIELD`.
- Documents can be deleted with the `delete()` method.

#### 4. 🔥 Firestore Data Modeling Guidelines
- Identify expected access patterns before designing the schema.
- Top-level entities become collections; related entities become subcollections.
- Use primary keys or concatenated keys as unique document IDs.

#### 5. 🍃 MongoDB Overview
- MongoDB is an open-source, distributed document database using BSON format.
- Supports multi-document ACID transactions.
- Uses replication for high availability and automatic failover.
- Supports horizontal scaling via sharding based on shard keys.
- Documents have a maximum size of 16 MB.
- MongoDB is schemaless (schema-on-read).
- Rich query language supports nested queries, boolean operators, and range queries.

#### 6. 🍃 MongoDB Data Operations
- Insert operations: `insertOne()`, `insertMany()`.
- Read operations: `findOne()`, `find()` with selection and projection.
- Update operations: `update()`, `updateMany()`.
- Delete operations: `deleteOne()`, `deleteMany()`.

#### 7. 🌐 Neo4j Overview
- Neo4j is a labeled property graph database optimized for highly connected data.
- Uses Cypher, a declarative, SQL-inspired query language.
- Supports ACID transactions and distributed architecture for scaling reads.
- Limited write scalability; no sharding support.
- Provides visualization tools like Neo4j Browser and Bloom.
- Available as a cloud service (Aura).

#### 8. 🌐 Neo4j Data Model and Queries
- Nodes and relationships have labels and properties.
- Relationships represent connections like `HAS_ROLE`, `IN_GROUP`, `HAS_PERMISSION`.
- Cypher commands: `CREATE` to add nodes/relationships, `MATCH` to query, `RETURN` to output.
- Supports complex graph traversals to query permissions and roles.
- Relationships must be deleted before deleting connected nodes.



<br>

## Study Notes

### 1. 🚀 The NoSQL Movement: Why NoSQL?

The NoSQL movement emerged as a response to the limitations of traditional relational databases, especially when dealing with modern applications that require high scalability, flexibility, and performance. Here’s why NoSQL databases became popular:

- **Need for Greater Scalability:** Traditional relational databases often struggle to scale horizontally (across many servers). NoSQL databases are designed to scale out easily, handling large volumes of data and high traffic loads.
  
- **Throughput and Response Time:** Applications today demand fast read/write operations and low latency. NoSQL systems optimize for these performance metrics.
  
- **More Expressive Data Models and Schema Flexibility:** Unlike rigid relational schemas, NoSQL databases allow flexible or even schema-less data models. This flexibility helps developers evolve their data structures without costly migrations.
  
- **Object-Relational Mismatch:** Object-oriented programming languages don’t map neatly to relational tables. NoSQL databases often use document, key-value, or graph models that align better with application data structures.
  
- **Preference for Open-Source Software:** Many NoSQL systems are open-source, encouraging community contributions and adoption.


### 2. 🔥 Firestore: A Serverless Document Database

Firestore is a NoSQL document database developed by Google, designed for modern applications like mobile, web, and IoT. It is fully managed and serverless, meaning developers don’t worry about infrastructure.

#### Key Features of Firestore:

- **Distributed System:** Firestore is built on a distributed architecture, ensuring data is replicated and available globally.
  
- **Serverless:** No need to manage servers or clusters; Google Cloud handles scaling and maintenance.
  
- **Simple APIs:** Easy-to-use APIs for reading and writing data.
  
- **ACID Transactions:** Supports atomic, consistent, isolated, and durable transactions, backed by Google Spanner technology.
  
- **Document Model:** Data is stored as documents, which are collections of key-value pairs.
  
- **Change Data Capture:** Firestore can track changes to documents, useful for real-time updates.
  
- **Cost and Limits:** Runs only on Google Cloud, with write throughput limits (up to 10,000 writes per second).

#### Firestore’s Document Model Explained:

- A **document** is a set of typed key-value pairs. Keys are strings, and values can be primitive types (string, number, boolean, timestamp) or complex types (arrays, maps, geopoints).
  
- Documents are grouped into **collections**. Collections contain documents of the same conceptual type but documents can have different schemas.
  
- Each document has a **unique string identifier**.
  
- Firestore supports **hierarchical data** through **subcollections**, which are collections nested inside documents. Subcollections can be nested up to 100 levels deep.

#### Writing Data in Firestore:

- **Single Document Write:** Use the `set` method to convert a Python dictionary into a Firestore document.
  
- **Nested Documents:** Subcollections allow storing related data hierarchically.
  
- **Batch Writes:** You can write multiple documents in batches (up to 500 documents per batch), even across different collections.

#### Reading Data:

- **Single Document:** Use `get` to fetch one document.
  
- **Multiple Documents:** Use `stream` to fetch all documents in a collection or subcollection.
  
- **Filtering and Sorting:** Use `where` to filter, `order_by` to sort, and `limit` to restrict the number of results.
  
- **Indexes:** All queries require indexes; if an index is missing, the query will fail.

#### Updating and Deleting:

- Use `update` to modify fields in a document.
  
- Use `firestore.Increment()` to atomically increment numeric fields.
  
- Use `firestore.DELETE_FIELD` to remove a field.
  
- Use `delete()` to remove entire documents.

#### Data Modeling in Firestore:

- Identify **access patterns** (how the data will be queried).
  
- Group entities into hierarchies: top-level entities become collections, and related entities become subcollections.
  
- Use primary keys or concatenated keys as unique document IDs.
  
- Example: Converting a college relational schema into Firestore involves creating collections for classes, students, and instructors, with subcollections for nested relationships.


### 3. 🍃 MongoDB: Flexible Document Store

MongoDB is a popular open-source NoSQL database designed for web-scale applications. It uses a document-oriented model and supports rich queries.

#### The CAP Theorem Context:

- The CAP theorem states that a distributed database can only guarantee two of the following three at the same time: Consistency, Availability, and Partition tolerance.
  
- MongoDB balances these properties to provide high availability and partition tolerance, with tunable consistency.

#### MongoDB Overview:

- **Distributed System:** Supports replication and sharding for scalability and fault tolerance.
  
- **Open Source:** Sponsored by MongoDB Inc., widely used in industry.
  
- **Document Model:** Stores data as BSON (Binary JSON) documents, which are flexible and can nest objects and arrays.
  
- **Schemaless:** MongoDB does not enforce a schema on writes; schema is applied when reading (schema-on-read).
  
- **Rich Query Language:** Supports complex queries, including nested queries, boolean operators, and range queries.
  
- **Secondary Indexes:** Supports indexes on any field to speed up queries.
  
- **Transactions:** Supports multi-document ACID transactions.
  
- **Sharding:** Data is partitioned across shards based on a shard key, which determines how documents are distributed.
  
- **Replication:** Replica sets provide high availability with automatic failover and load balancing.

#### MongoDB Data Model:

- Documents are BSON objects with unordered key-value pairs.
  
- Each document has a unique `_id` field.
  
- Supports various data types: strings, integers, doubles, booleans, dates, arrays, nested objects, and ObjectIds.
  
- Documents are grouped into collections, which are grouped into databases.

#### Basic Operations:

- **Inserts:** `insertOne()`, `insertMany()` to add documents.
  
- **Reads:** `findOne()`, `find()` with selection (filter) and projection (fields to return).
  
- **Updates:** `update()`, `updateMany()` to modify documents.
  
- **Deletes:** `deleteOne()`, `deleteMany()` to remove documents.

#### Query Examples:

- Nested queries can filter on fields inside embedded documents.
  
- Boolean operators like `$and` combine multiple conditions.
  
- Range queries use operators like `$lte` (less than or equal), `$gte` (greater than or equal).


### 4. 🌐 Neo4j: Graph Database for Connected Data

Neo4j is a graph database designed to store and query highly connected data efficiently. It uses a labeled property graph model.

#### What is a Labeled Property Graph?

- Nodes (entities) and relationships (edges) both have labels and properties (key-value pairs).
  
- This model is ideal for data where relationships are first-class citizens, such as social networks, recommendation engines, and access control.

#### Neo4j Features:

- **Declarative Query Language (Cypher):** Similar to SQL but designed for graph traversal and pattern matching.
  
- **Open Source:** Sponsored by Neo4j Inc.
  
- **ACID Transactions:** Ensures data integrity.
  
- **Distributed Architecture:** Scales reads across multiple servers.
  
- **Visualization Tools:** Neo4j Browser and Bloom help visualize graph data.
  
- **Cloud Offering:** Neo4j Aura provides managed cloud service.
  
- **Write Scalability:** Limited compared to reads; no sharding support.

#### Basic Cypher Commands:

- `CREATE` to add nodes and relationships.
  
- `MATCH` to find patterns in the graph.
  
- `RETURN` to output query results.
  
- Example: Creating a person node and a place node, then linking them with a `LIVES_IN` relationship.

#### Example: IAM Model in Neo4j

- Nodes represent entities like Person, Role, Group, Permission.
  
- Relationships represent connections like `HAS_ROLE`, `IN_GROUP`, `HAS_PERMISSION`.
  
- Example Cypher queries create nodes and relationships, then query permissions for a person by traversing these relationships.
  
- This model is powerful for access control systems where permissions depend on roles and group memberships.

#### Updating and Deleting in Neo4j:

- Add or update node properties and labels.
  
- Modify relationships and their properties.
  
- Delete relationships before deleting nodes to maintain graph integrity.
  
- Commands exist to drop all nodes and relationships if needed.


### Summary

This lecture covered three major NoSQL database systems, each with distinct data models and use cases:

- **Firestore:** A serverless, document-based database optimized for mobile and web apps, with hierarchical data support and strong consistency.
  
- **MongoDB:** A flexible, schemaless document store with rich querying, replication, and sharding for scalability.
  
- **Neo4j:** A graph database designed for highly connected data, using a labeled property graph model and Cypher query language.

Understanding these systems involves grasping their data models, how they handle scalability and consistency, and how to perform basic CRUD (Create, Read, Update, Delete) operations. Each system suits different application needs, from hierarchical document storage to complex graph traversals.