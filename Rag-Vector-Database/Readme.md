Hey, in your LangChain + Chroma Cloud project, the main APIs you'll use fall into four categories: storing vectors, searching documents, managing records, and retrieving context for RAG.

The important point is that you generally don't call a separate Chroma API for each operation. You can use LangChain's `Chroma` vector-store methods, which handle embedding generation and communicate with Chroma Cloud.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://reference.langchain.com\&sz=32)

LangChain Reference

+1



## 1. Complete API cheat sheet

Using `from langchain_chroma import Chroma`

A. Vector storage

Insert, update, and delete records.

`add_documents()` · `add_texts()` · `update_documents()` · `delete()`

B. Vector search

Find semantically similar documents.

`similarity_search()` · `similarity_search_with_score()` · `similarity_search_by_vector()`

C. Advanced retrieval

Filter by metadata and reduce redundant results.

`max_marginal_relevance_search()` · `as_retriever()` · `get_by_ids()`

D. Collection management

Inspect and manage the collection.

`get()` · `reset_collection()` · `delete_collection()`

## 2. Storage APIs

| API                                        | What it does                                     |
| ------------------------------------------ | ------------------------------------------------ |
| `add_documents(docs, ids=...)`             | Stores LangChain documents and their embeddings. |
| `add_texts(texts, metadatas=..., ids=...)` | Stores raw text with optional metadata and IDs.  |
| `update_documents(ids=..., documents=...)` | Updates existing records.                        |
| `delete(ids=...)`                          | Deletes records by ID.                           |

Example:

```
from langchain_core.documents import Documentdocs = [    Document(        page_content="Spring Boot simplifies Java backend development.",        metadata={"topic": "Java"}    )]vector_store.add_documents(    documents=docs,    ids=["spring-boot-001"])
```

What happens internally?

1. LangChain sends the text to your embedding model.
2. The embedding model generates vectors.
3. LangChain sends the vectors, text, metadata, and IDs to Chroma Cloud.
4. Chroma stores the records for future retrieval.

## 3. Search APIs

| API                                                   | When to use it                                     |
| ----------------------------------------------------- | -------------------------------------------------- |
| `similarity_search(query, k=4)`                       | Get the most relevant documents.                   |
| `similarity_search_with_score(query, k=4)`            | Inspect results and their distance scores.         |
| `similarity_search_with_relevance_scores(query, k=4)` | Retrieve results with normalized relevance scores. |
| `similarity_search_by_vector(embedding, k=4)`         | Search using a vector you've already generated.    |
| `max_marginal_relevance_search(query, k=4)`           | Get relevant, less-redundant documents.            |

Example:

```
results = vector_store.similarity_search(    query="How does Spring Boot help backend developers?",    k=3,    filter={"topic": "Java"})for doc in results:    print(doc.page_content)    print(doc.metadata)
```

For direct distance inspection:

```
results = vector_store.similarity_search_with_score(    query="Java backend development",    k=3)for doc, distance in results:    print(doc.page_content, distance)
```

Chroma's raw distance is not necessarily a cosine similarity value. The interpretation depends on the collection's distance metric.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://reference.langchain.com\&sz=32)

LangChain Reference

+1



## 4. The most important API for RAG: `as_retriever()`

Instead of manually searching the database every time, expose the vector store as a LangChain retriever.

```
retriever = vector_store.as_retriever(    search_type="similarity",    search_kwargs={"k": 3})documents = retriever.invoke(    "Explain Spring Boot dependency injection")for doc in documents:    print(doc.page_content)
```

You can then connect the retriever to a prompt and an LLM to create a complete RAG pipeline.

## 5. Native Chroma APIs versus LangChain APIs

There are two layers you should understand:

- LangChain API: `vector_store.add_documents()`, `vector_store.similarity_search()`, etc.
- Native Chroma SDK: `collection.add()`, `collection.upsert()`, `collection.query()`, `collection.get()`, etc.

Use LangChain when building an LLM or RAG application. Use the native SDK when you need lower-level database control. The native SDK also supports metadata filtering, full-text search, and hybrid retrieval.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://docs.trychroma.com\&sz=32)

Chroma Docs

+1



For your current project, I recommend mastering these six methods first:

`add_documents()` → `get_by_ids()` → `similarity_search()` → `similarity_search_with_score()` → `delete()` → `as_retriever()`.

They cover most of the day-to-day vector storage and retrieval work you'll need for a RAG application.