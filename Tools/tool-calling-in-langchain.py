
from langchain.messages import HumanMessage
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv;

load_dotenv()
print("LLM Connection succedded!!")

@tool
def multiply(a: int, b: int) -> int:
    """Given two numbers a and b, return their product."""
    print("multiply tool has been called!!")
    return a * b


# Direct tool execution
print(multiply.invoke({"a": 3, "b": 4}))  # 12

# Initialize the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.5,
    max_tokens=2000
)

# Bind the tool to the LLM
llm_with_tools = llm.bind_tools([multiply])

# Ask the model a question
response = llm_with_tools.invoke("What is 3 multiplied by 4?")
print(response.content)
# res = llm.invoke("What is computer?")
# print(res.content);
res = response.tool_calls[0];

# print(res)  #how tool exec


multiply.invoke({'name': 'multiply', 'args': {'a': 3, 'b': 4}, 'id': '7cf78929-5037-47c3-8647-51f29037dc7a', 'type': 'tool_call'});


query = HumanMessage(' multiply 3 and 9')
messages = [query];
result = llm_with_tools.invoke(messages);
messages.append(result);
print(messages);

