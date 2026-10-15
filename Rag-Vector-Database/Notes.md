1) Text-->Embedding -->Compare -->Store in VectorDB(chroma DB) -->Do operation

2) Find angular distance(Cosine similarity) between two vectors.

3) Text->embeddings->similarity-->VectorDB -->..

Challenges:
    a) Generate Embedding vectors;
    b) Storage for Embedding Vectors.(VectorDB)
    c) Semantic Search.(Cosine Similarity between vectors)
    d) Intellegent Semantic Search.

Vector Store:   
    1) In memory -->Ram
    2) In Harddrive -->Hard disk
    3) Indexing Concept-->Faster searching process.
    4) Crud Operations

Process of Indexing(Idea):
    1) Find Centroid of vectors;
    2) Calc similarity score
    3) Max similarity score

Use cases:
    1) Semantic Sys
    2) Rag
    3) Recommended sys
    4) Image/Multimedia search

Vector Store Vs Vector DataBase:
    a) Vector Store:
        System doing mainly 2 works:
            1) storage and retrival
        1) light weght library 
        2) ideal for prototyping
        3) FAISS(where u store vector and can query them by similarity,but you handle persistance amd scaling swprately).

    b) Vector Database:
        1) Vector Store + Distributed,BackUp and recovery, Acid Transaction , Authentication
        2) DUrability
        3) Meta deta handling
        4) Potential for ACID 
        Example:   Milvus,Qdrant, Weaviate
   Note: Every Vector DataBase is a Vector Store But Not Every Data Store is a Vector Database.
   