import os;
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

load_dotenv()
embeddings_model = HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

doc1 = Document(
    page_content = "India is a Good Country",
    metadata={"team":"India"}
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
doc5=Document(
    page_content="Yuvi pa is successfull but not Underrated",
    metadata={"team":"India"}
)
docs = [doc1,doc2,doc3,doc4,doc5]

vector_store = Chroma(
    collection_name="shivam_rag_demo",
    embedding_function=embeddings_model,
    chroma_cloud_api_key=os.environ["CHROMA_API_KEY"],
    tenant=os.environ["CHROMA_TENANT"],
    database=os.environ["CHROMA_DATABASE"],
)

res = vector_store.get_by_ids(id:Sequqnce["India"])
print("Chroma is Connected!!");

vector_store.add_documents(
    documents=docs,
    ids=["ind","mi","india","srh","india1"]
)
print("document uploaded!");

results = vector_store.similarity_search(
    "Who is Successfull but Underrated??",
    k=2
)

print(results);

for i, doc in enumerate(results, start=1):
    print(f"\nResult {i}:")
    print("Content:", doc.page_content)
    print("Metadata:", doc.metadata)
