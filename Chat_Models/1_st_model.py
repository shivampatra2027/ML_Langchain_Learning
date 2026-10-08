from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI;
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=1.5,
    max_output_tokens=10
)

result = llm.invoke("write 4 words on ai")

print(result.text)