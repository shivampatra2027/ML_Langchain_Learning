from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
# Load a sentence-transformer model locally
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents=[
    "Delhi is the caps of india",
    "Kolkata is the caps of west bangal",
    "Paris is the caps of France",
]
query = "Whose caps is amristar"
doc_embedding = embedding.embed_documents(documents);
query_embedding = embedding.embed_query(query);

similarities = cosine_similarity(
    [query_embedding],doc_embedding   #the query embedding vector will be checked with all the doc vectors available inside documents.
)[0]

print(similarities);
print("Similarity scores:",similarities)

best_index=similarities.argmax();
print(documents[best_index]);
