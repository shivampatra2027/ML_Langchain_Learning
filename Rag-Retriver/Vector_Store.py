from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# 1. Initialize the embedding model
embeddings_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 2. Create documents
doc1 = Document(
    page_content="Virat Kohli is successful.",
    metadata={"team": "RCB"}
)

doc2 = Document(
    page_content="Rohit Sharma has won multiple titles.",
    metadata={"team": "MI"}
)

doc3 = Document(
    page_content="India is a developing country.",
    metadata={"team": "India"}
)
doc4 = Document(
    page_content = "A sharam is successfull but is very Underrated!",
    metadata={"team":"SRH"}
)

docs = [doc1, doc2, doc3,doc4]

# 3. Initialize Chroma vector store
vector_store = Chroma(
    embedding_function=embeddings_model,
    persist_directory="my_chroma_db",
    collection_name="simple"
)

# 4. Add documents
ids = vector_store.add_documents(docs)

print("Documents added successfully!")
print("Document IDs:", ids)

retriever = vector_store.as_retriever(search_kwargs={"k":2})
query="Who is Underrated ??"
results = retriever.invoke(query)
for i,doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)