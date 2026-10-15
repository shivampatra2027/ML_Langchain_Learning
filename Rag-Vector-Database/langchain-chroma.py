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

docs = [doc1, doc2, doc3]

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

# 5. Test similarity search
results = vector_store.similarity_search(
    "Which team does Virat Kohli play for?",
    k=2
)

for doc in results:
    print("\nContent:", doc.page_content)
    print("Metadata:", doc.metadata)

resu = vector_store.get(include=['embeddings','documents','metadatas']);
print(resu)

res2 = vector_store.similarity_search(
    query='Who is successfull? and plays for SRH',
    k=2   #K->how similary vectors u want to show.
)
print(res2);

res3 = vector_store.similarity_search_with_score(
    query='Who is successfull? and plays for SRH',
    k=2   #K->how similary vectors u want to show.
)
print(res3);
