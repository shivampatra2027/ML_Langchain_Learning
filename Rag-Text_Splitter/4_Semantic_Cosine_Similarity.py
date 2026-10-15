
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re

# 1. Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# 2. Input document
text = """
Cricket Wireless offers multi-line discounts for three lines on its plans, such as the Select Unlimited and Smart Unlimited options.
• Select Unlimited: Three lines cost around $100 total (or lower depending on specific plan setup and auto-pay features).
• Terrorism is the calculated use of violence or intimidation against civilians and non-combatants to achieve political, religious, or ideological goals.
• It intentionally creates a general climate of fear and psychological distress to coerce governments or populations into meeting specific demands
Tourism is the act of traveling to different places for leisure, recreation, exploration, or business.
• It plays a vital role in boosting local and national economies by generating employment and foreign exchange revenue.
• It fosters cultural exchange, allowing people to discover new traditions, cuisines, and historical landmarks.
"""

# 3. Split into sentences
sentences = re.split(r'(?<=[.!?])\s+', text.strip())

# 4. Generate embeddings
embeddings = model.encode(sentences)

# 5. Group sentences using cosine similarity
threshold = 0.5
chunks = []
current_chunk = [sentences[0]]

for i in range(1, len(sentences)):
    similarity = cosine_similarity(
        [embeddings[i - 1]],
        [embeddings[i]]
    )[0][0]

    print(
        f"Similarity between sentence {i} and {i + 1}: "
        f"{similarity:.4f}"
    )

    if similarity < threshold:
        chunks.append(" ".join(current_chunk))
        current_chunk = [sentences[i]]
    else:
        current_chunk.append(sentences[i])

# Add the final chunk
if current_chunk:
    chunks.append(" ".join(current_chunk))  

# 6. Print chunks
print("\nTotal chunks:", len(chunks))

for i, chunk in enumerate(chunks, 1):
    print(f"\nChunk {i}:\n{chunk}")
