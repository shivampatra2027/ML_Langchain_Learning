from dotenv import load_dotenv;
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI;

load_dotenv()
@tool 
def multiply(a:int,b:int)->int:
    """Multiply a and b and get the product"""
    print("multiply tool has been called!!")
    return a*b;
@tool
def add(a:int,b:int)->int:
    """Add the two a and b and return their sum"""
    print("adding operation tool has been called!!")
    return a+b;

llm= ChatGoogleGenerativeAI(
    model = "gemini-3.8-flash",
    temperature = 0.5,
    max_tokens = 30000
)
llm_with_tools = llm.bind_tools([multiply,add]);

response = llm_with_tools.invoke(""
    "Then use the add tool to add 9 to the multiplication result.");
print(response);
