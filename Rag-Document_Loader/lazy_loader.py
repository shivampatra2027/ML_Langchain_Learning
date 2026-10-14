import os
from dotenv import load_dotenv

from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Set before creating the web loader
os.environ["USER_AGENT"] = "Mozilla/5.0 (compatible; LangChainLearning/1.0)"

url = "https://www.flipkart.com/puma-nova-elite-tennis-shoes-men/p/itmfbaf7758da0ce?pid=SHOHFYQC4E8HUVSC"

loader = WebBaseLoader(url)
docs = loader.load()

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.5,
    max_output_tokens=3000
)

prompt = PromptTemplate(
    template="Summarize the following product information in simple terms:\n{topics}",
    input_variables=["topics"]
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topics": docs[0].page_content})
print(result)