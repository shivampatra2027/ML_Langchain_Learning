from chromadb import EmbeddingFunction
from langchain_chroma import Chroma
from langchain_community.document_loaders import YoutubeLoader
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings


from langchain_core.caches import InMemoryCache
from langchain_core.globals import set_llm_cache
from langchain_text_splitters import RecursiveCharacterTextSplitter
load_dotenv();

set_llm_cache(InMemoryCache(maxsize=100))
model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.5,
    max_tokens=3000
)
#1) Indexing
video_url = "https://youtu.be/4781cGLvQUU"

loader = YoutubeLoader.from_youtube_url(
    video_url,
    language=["hi"],
    add_video_info=False
)


docs=loader.load();

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

chunks = text_splitter.split_documents(docs)

print("Transcript chunks:", len(chunks))

embeddings_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# for doc in docs:
#     print(f"\nMetadata",doc.metadata)
#     print(f"\nTranscript:")
#     print(f"\n",doc.page_content);

vector_store=Chroma(
    embedding_function=embeddings_model,
    persist_directory="my_chroma_db",
    collection_name="simple"
)
ids=vector_store.add_documents(chunks)
print("Document successfully added inside the vector Store!!")

query="What is context??"
#2) Retrival
retriever = vector_store.as_retriever(search_type="similarity",search_kwargs={"k":2})

result = retriever.invoke(query);

#3) Agumentation
#One shot Prompting
prompt = PromptTemplate(
    template=""" 
        You are a helpful YouTube video summarizer.
        Use the retrieved context to answer the user's question.

        Example:

        Context:
        Python is a programming language known for its simple syntax.
        It is widely used in AI, automation, and web development.

        Question:
        What is Python used for?

        Answer:
        Python is used for AI, automation, and web development.
        Its simple syntax makes it easy to learn.

        Now answer using the actual retrieved context.
        If you did not find any context..straight forward reply 'No Context found'

        Context:
        {topic}

        Question:
        {question}

        Answer:
""",
    input_variables=["topic","question"]
)

parser=StrOutputParser();
chain =prompt | model | parser
print("chain is created successfully!")

print("Processing started...please wait...")
context = "\n\n".join(doc.page_content for doc in result)
print(context)
print("\n\n\n")
#4) Generation
res = chain.invoke({"topic": context,"question":query})
print(res);