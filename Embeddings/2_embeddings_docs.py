from langchain_huggingface import HuggingFaceEmbeddings

# Load a sentence-transformer model locally
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents=[
    "Delhi is the caps of india",
    "Kolkata is the caps of west bangal",
    "Paris is the caps of France"
]

result = embedding.embed_documents(documents);
print(str(result))
# Generate embedding vector

# Print the vector

