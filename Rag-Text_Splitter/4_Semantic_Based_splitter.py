
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings

# 1. Load the embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 2. Initialize the semantic splitter
splitter = SemanticChunker(
    embeddings=embeddings,
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=75
)

# 3. Your document
text = """Artificial Intelligence, commonly known as AI, is a branch
of computer science that focuses on developing machines and software
capable of performing tasks that typically require human intelligence.
Machine Learning is a subset of Artificial Intelligence that enables
computers to learn patterns from data without being explicitly
programmed for every situation.
Deep Learning is a subset of Machine Learning that uses neural networks
with multiple layers to learn complex patterns from large datasets.
Natural Language Processing allows computers to understand, interpret,
and generate human language."""

# 4. Split the document
result = splitter.split_text(text)

# 5. Print the chunks
print("Total chunks:", len(result))

for i, chunk in enumerate(result, start=1):
    print(f"\nChunk {i}:\n{chunk}")
