from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import wikipedia
from langchain_community.retrievers import WikipediaRetriever
from dotenv import load_dotenv;

load_dotenv()
model=ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.5,
    max_tokens=1000
)
print("Model connected successfully!")

prompt = PromptTemplate(
    template="Summarize the follwing \n {topic}",
    input_variables=["topic"]
)
#Identify your application to Wikimedia
wikipedia.set_user_agent(
    "MyRAGProject/1.0 (shivam@example.com)"
)

retriever = WikipediaRetriever(
    top_k_results=4,
    lang="en"
)

query = "India"
#retriever is a runnable.. runnable functions are those who are having capability of Invoke.
docs = retriever.invoke(query)

parser = StrOutputParser();
chain = prompt | model | parser
print("chaining is done..")
res=chain.invoke({"topic":docs})
print(res);

print("\n Printing Meta-data\n");

token_count = model.get_num_tokens(prompt.template);
print("\nToken count:",token_count);
print("\n Printing Output Token Count:",model.get_num_tokens(res))

# print(type(docs));
# for i, doc in enumerate(docs):
#     print(f"\n--- Result {i + 1} ---")
#     print(f"Content:\n{doc.page_content}...")
