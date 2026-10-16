from langchain_classic.retrievers import MultiQueryRetriever
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

retriever = MultiQueryRetriever.from_llm(
    retriever=vector_store.as_retriever(
        search_kwargs={"k": 2}
    ),
    llm=llm,
    include_original=True
)

docs = retriever.invoke("Who is an underrated cricketer?")

for doc in docs:
    print(doc.page_content)