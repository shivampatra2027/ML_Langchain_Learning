
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# 1. Load the document
loader = TextLoader("docs.txt", encoding="utf-8")
documents = loader.load()

# 2. Split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)

print(f"Total chunks created: {len(docs)}")

# 3. Convert chunks into embeddings and store them in FAISS
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = FAISS.from_documents(docs, embeddings)

print("Documents embedded and stored in FAISS.")

# 4. Create a retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# 5. Retrieve relevant documents
query = "What are the key takeaways from the document?"
retrieved_docs = retriever.invoke(query)

# 6. Display retrieved content
for i, doc in enumerate(retrieved_docs, start=1):
    print(f"\n--- Retrieved Document {i} ---")
    print(doc.page_content)
