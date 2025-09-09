## 12. Intro to Information Retrieval

## Questions

#### 1. What best describes the primary goal of Information Retrieval (IR)?  
A) To store all available data in a structured database  
B) To find relevant information resources that satisfy a user’s information need  
C) To reduce information overload by filtering irrelevant data  
D) To convert unstructured data into structured data automatically  

#### 2. Which of the following are challenges unique to Information Retrieval compared to traditional database search?  
A) Handling unstructured data such as text and multimedia  
B) Managing semantic and lexical gaps between queries and documents  
C) Ensuring ACID properties in transactions  
D) Indexing structured relational data efficiently  

#### 3. Why is information overload a critical problem that IR systems aim to solve?  
A) Because users have limited time and cognitive capacity to process large volumes of data  
B) Because structured data is always easier to search than unstructured data  
C) Because too much information can cause confusion and poor decision-making  
D) Because IR systems eliminate the need for human judgment in selecting information  

#### 4. Which of the following statements about the history of IR are true?  
A) The memex concept by Vannevar Bush inspired early ideas of associative information retrieval  
B) The Text Retrieval Conference (TREC) was established to evaluate IR systems on a large scale  
C) The vector space model was introduced in the 1990s as a new retrieval model  
D) Google’s dominance in search is unrelated to academic IR research advancements  

#### 5. What are the main components of a typical IR system?  
A) Crawler, Document Analyzer, Indexer, Repository, Query Processor, Ranking Algorithm  
B) Parser, Compiler, Interpreter, Executor  
C) User Interface, Database Management System, Transaction Manager  
D) Query Optimizer, Storage Engine, Network Interface  

#### 6. Which of the following best explain the "lexical gap" problem in IR?  
A) Different words with similar meanings used in queries and documents  
B) The inability of IR systems to process multimedia data  
C) The difference between user intent and system interpretation of queries  
D) The lack of structured metadata in documents  

#### 7. How does the "semantic gap" differ from the "lexical gap" in IR?  
A) Semantic gap refers to differences in meaning and context, while lexical gap refers to differences in word choice  
B) Semantic gap is about indexing speed, lexical gap is about query length  
C) Semantic gap only occurs in structured data, lexical gap only in unstructured data  
D) Semantic gap is a problem solved by traditional databases, lexical gap is unique to IR  

#### 8. Which of the following retrieval models were developed during the 1970s and 1980s?  
A) Vector Space Model  
B) Probabilistic Models  
C) Language Models  
D) Neural Network Models  

#### 9. What role does the Text Retrieval Conference (TREC) play in the IR community?  
A) It provides a platform for large-scale evaluation of IR methodologies  
B) It is a commercial search engine competing with Google  
C) It contributed significantly to improvements in web search engines between 1999 and 2009  
D) It focuses exclusively on multimedia retrieval research  

#### 10. Which of the following statements about web search engines are accurate?  
A) The first web search engine was developed using Perl scripts to mirror and standardize web pages  
B) Google holds the majority of the global desktop and mobile search market share  
C) Web search engines only index structured data from websites  
D) The explosion of the World Wide Web drove innovation in IR techniques  

#### 11. In what ways is Information Retrieval different from Natural Language Processing (NLP)?  
A) IR focuses on scalable retrieval of relevant documents, NLP focuses on deep semantic understanding  
B) IR deals only with structured data, NLP deals only with unstructured data  
C) IR uses statistical methods, NLP uses symbolic and cognitive approaches  
D) IR and NLP are completely unrelated fields with no overlap  

#### 12. Which of the following are examples of IR applications beyond web search?  
A) Recommendation systems based on browsing history  
B) Question answering systems like WolframAlpha  
C) Transaction processing in relational databases  
D) Enterprise search combining web and desktop data  

#### 13. What is the significance of indexing in an IR system?  
A) It organizes data to allow fast and efficient retrieval of relevant documents  
B) It converts unstructured data into structured relational tables  
C) It eliminates the need for query processing  
D) It stores user queries for future analysis only  

#### 14. Which of the following best describe the relationship between IR and machine learning?  
A) Machine learning techniques are used to improve ranking algorithms in IR  
B) IR systems do not benefit from machine learning due to the nature of unstructured data  
C) Learning to rank is a common machine learning approach applied in modern IR systems  
D) Machine learning replaces the need for indexing in IR  

#### 15. What are some challenges when representing queries and documents in IR?  
A) Efficient data structures for fast access  
B) Bridging lexical and semantic gaps  
C) Ensuring ACID compliance for query transactions  
D) Handling ambiguous or incomplete user queries  

#### 16. Which of the following statements about the future of IR are true?  
A) Mobile search will integrate location and context beyond desktop search  
B) Interactive retrieval involves collaboration between machines and humans  
C) Personal assistants represent a form of proactive information retrieval  
D) IR will become obsolete as databases improve  

#### 17. Why is unstructured data more challenging for IR systems than structured data?  
A) It lacks a fixed schema, making indexing and retrieval more complex  
B) It is always larger in volume than structured data  
C) It contains unknown semantic meanings that are difficult to interpret automatically  
D) It cannot be stored on computers  

#### 18. Which of the following are true about the impact of TREC on web search?  
A) About one-third of the improvement in web search engines from 1999 to 2009 is attributed to TREC  
B) TREC provides infrastructure for evaluating text retrieval methodologies  
C) TREC is a commercial search engine used by millions daily  
D) TREC evaluations have saved billions of hours of user time  

#### 19. What is the role of a crawler in an IR system?  
A) To automatically collect and update documents from the web or other sources  
B) To rank documents based on relevance to queries  
C) To parse and analyze user queries  
D) To store user feedback for improving search results  

#### 20. Which of the following statements about IR’s interdisciplinary nature are correct?  
A) IR combines techniques from databases, NLP, machine learning, and human-computer interaction  
B) IR is purely a subfield of library science with no relation to computer science  
C) Advances in NLP directly contribute to improvements in IR systems  
D) IR research is isolated and does not benefit from other fields



<br>

## Answers

#### 1. What best describes the primary goal of Information Retrieval (IR)?  
A) ✗ Storing data is not the primary goal; IR focuses on finding relevant info.  
B) ✓ IR aims to find relevant information satisfying user needs.  
C) ✓ Reducing information overload by filtering irrelevant data is a key IR purpose.  
D) ✗ IR does not automatically convert unstructured data into structured data.  

**Correct:** B, C


#### 2. Which of the following are challenges unique to Information Retrieval compared to traditional database search?  
A) ✓ Handling unstructured data is a core IR challenge.  
B) ✓ Managing lexical and semantic gaps is unique to IR.  
C) ✗ ACID properties relate to databases, not IR.  
D) ✗ Efficient indexing of structured data is a database problem, not unique to IR.  

**Correct:** A, B


#### 3. Why is information overload a critical problem that IR systems aim to solve?  
A) ✓ Users have limited time and cognitive capacity.  
B) ✗ Structured data is easier to search, but this is not why overload is critical.  
C) ✓ Too much information causes confusion and poor decisions.  
D) ✗ IR assists human judgment; it does not eliminate it.  

**Correct:** A, C


#### 4. Which of the following statements about the history of IR are true?  
A) ✓ Vannevar Bush’s memex inspired associative retrieval ideas.  
B) ✓ TREC was established for large-scale IR evaluation.  
C) ✗ Vector space model was introduced earlier, in the 1970s.  
D) ✗ Google’s success is partly due to academic IR research.  

**Correct:** A, B


#### 5. What are the main components of a typical IR system?  
A) ✓ All listed components are core parts of IR systems.  
B) ✗ These are programming language components, not IR.  
C) ✗ These relate to databases, not IR.  
D) ✗ These are database internals, not IR components.  

**Correct:** A


#### 6. Which of the following best explain the "lexical gap" problem in IR?  
A) ✓ Lexical gap is about different words with similar meanings.  
B) ✗ Lexical gap is not about multimedia processing.  
C) ✗ This describes semantic gap, not lexical gap.  
D) ✗ Lack of metadata is a different issue.  

**Correct:** A


#### 7. How does the "semantic gap" differ from the "lexical gap" in IR?  
A) ✓ Semantic gap involves meaning/context differences; lexical gap is word choice.  
B) ✗ These are unrelated to indexing speed or query length.  
C) ✗ Both gaps occur mainly in unstructured data.  
D) ✗ Semantic gap is not solved by traditional databases.  

**Correct:** A


#### 8. Which of the following retrieval models were developed during the 1970s and 1980s?  
A) ✓ Vector space model was developed in this period.  
B) ✓ Probabilistic models also emerged then.  
C) ✗ Language models came later, mainly in the 1990s.  
D) ✗ Neural network models are more recent.  

**Correct:** A, B


#### 9. What role does the Text Retrieval Conference (TREC) play in the IR community?  
A) ✓ TREC provides infrastructure for large-scale IR evaluation.  
B) ✗ TREC is not a commercial search engine.  
C) ✓ TREC contributed significantly to web search improvements.  
D) ✗ TREC covers more than just multimedia retrieval.  

**Correct:** A, C


#### 10. Which of the following statements about web search engines are accurate?  
A) ✓ The first web search engine used Perl scripts to mirror pages.  
B) ✓ Google dominates global desktop and mobile search markets.  
C) ✗ Web search engines index mostly unstructured data, not only structured.  
D) ✓ The WWW explosion drove IR innovation.  

**Correct:** A, B, D


#### 11. In what ways is Information Retrieval different from Natural Language Processing (NLP)?  
A) ✓ IR focuses on scalable retrieval; NLP on deep semantic understanding.  
B) ✗ Both deal with unstructured data, not exclusively one or the other.  
C) ✓ IR often uses statistical methods; NLP includes symbolic approaches.  
D) ✗ IR and NLP are related and increasingly overlap.  

**Correct:** A, C


#### 12. Which of the following are examples of IR applications beyond web search?  
A) ✓ Recommendation systems use IR techniques.  
B) ✓ Question answering systems are IR applications.  
C) ✗ Transaction processing is a database function, not IR.  
D) ✓ Enterprise search combines web and desktop data.  

**Correct:** A, B, D


#### 13. What is the significance of indexing in an IR system?  
A) ✓ Indexing organizes data for fast retrieval.  
B) ✗ Indexing does not convert unstructured data into relational tables.  
C) ✗ Query processing is still needed after indexing.  
D) ✗ Indexing is not just for storing queries.  

**Correct:** A


#### 14. Which of the following best describe the relationship between IR and machine learning?  
A) ✓ Machine learning improves ranking algorithms.  
B) ✗ IR benefits greatly from machine learning despite unstructured data.  
C) ✓ Learning to rank is a common ML approach in IR.  
D) ✗ Machine learning does not replace indexing.  

**Correct:** A, C


#### 15. What are some challenges when representing queries and documents in IR?  
A) ✓ Efficient data structures are needed for fast access.  
B) ✓ Bridging lexical and semantic gaps is a core challenge.  
C) ✗ ACID compliance is unrelated to IR query representation.  
D) ✓ Handling ambiguous or incomplete queries is difficult.  

**Correct:** A, B, D


#### 16. Which of the following statements about the future of IR are true?  
A) ✓ Mobile search will integrate location and context.  
B) ✓ Interactive retrieval involves human-machine collaboration.  
C) ✓ Personal assistants are proactive IR systems.  
D) ✗ IR will not become obsolete as databases improve.  

**Correct:** A, B, C


#### 17. Why is unstructured data more challenging for IR systems than structured data?  
A) ✓ Lack of fixed schema complicates indexing and retrieval.  
B) ✗ Volume alone does not define difficulty.  
C) ✓ Unknown semantic meanings are hard to interpret automatically.  
D) ✗ Unstructured data can be stored on computers.  

**Correct:** A, C


#### 18. Which of the following are true about the impact of TREC on web search?  
A) ✓ One-third of web search improvements from 1999-2009 are attributed to TREC.  
B) ✓ TREC provides infrastructure for evaluating text retrieval methods.  
C) ✗ TREC is not a commercial search engine.  
D) ✓ TREC evaluations saved billions of user hours.  

**Correct:** A, B, D


#### 19. What is the role of a crawler in an IR system?  
A) ✓ Crawlers collect and update documents automatically.  
B) ✗ Ranking is done by ranking algorithms, not crawlers.  
C) ✗ Query parsing is separate from crawling.  
D) ✗ Storing user feedback is not a crawler’s function.  

**Correct:** A


#### 20. Which of the following statements about IR’s interdisciplinary nature are correct?  
A) ✓ IR combines databases, NLP, ML, and HCI techniques.  
B) ✗ IR is not limited to library science; it is deeply connected to computer science.  
C) ✓ Advances in NLP improve IR systems.  
D) ✗ IR research benefits greatly from other fields and is not isolated.  

**Correct:** A, C