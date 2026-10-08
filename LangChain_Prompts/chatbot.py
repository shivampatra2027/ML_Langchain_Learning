from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv;

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=1.5,
    max_output_tokens=100,
)

while True:
    user_input = input("You:")
    if user_input.lower()=="exit":
        break
    result = model.invoke(user_input)
    print("AI:",result.content)

