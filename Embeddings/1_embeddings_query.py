from langchain_huggingface import HuggingFaceEmbeddings

# Load a sentence-transformer model locally
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


# Example text
text = "Delhi is the capital of India"

# Generate embedding vector
vector = embedding.embed_query(text)

# Print the vector
print(vector[0])
