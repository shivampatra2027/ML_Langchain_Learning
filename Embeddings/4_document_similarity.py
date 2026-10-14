from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

# Load a sentence-transformer model locally
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents=[
    "Delhi is the caps of india",
    "Kolkata is the caps of west bangal",
    "Paris is the caps of France"
]
text1 = "Delhi is the caps of india";
text2 = "Kolkata is the caps of west bangal";
text3 = "Paris is the caps of France"

v1 = embedding.embed_query(text1);
v2 = embedding.embed_query(text2);
v3 = embedding.embed_query(text3);

# print(v1);
# print(cosine_similarity([v1],[v2]));
# print(cosine_similarity([v2],[v3]));

result = embedding.embed_documents(documents);
print(str(result))