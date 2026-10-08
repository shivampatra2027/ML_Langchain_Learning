from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate;

from dotenv import load_dotenv;

load_dotenv()

chat_template = ChatPromptTemplate([
    ("system","You are a helpuful {domain} expert"),
    ("human","Explain in simple terms ,what is the {topic}")
])
prompt = chat_template.invoke({'domain':'cricket','topic':'LBW'})
print(prompt);
model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.2,
    max_output_tokens=1000,
)
result= model.invoke(prompt);
print(result.content);