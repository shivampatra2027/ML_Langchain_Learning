from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from Tools.Creating_Tools import multiply,add

load_dotenv()
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.5,
    max_tokens=2000,
    vertexai=False,
)
agent = create_agent(
    model=llm,
    tools=[multiply,add],
    system_prompt=(
        "You are a helpful assistant. "
        "Use available tools effectively."
    )
)

result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "find multiply of 2 and 3"
            "add the result to 6 and print the final clear result"
        }
    ]
})


print("\n--- EXECUTION TRACE ---")

for message in result["messages"]:
    print(f"\nMessage type: {type(message).__name__}")
    print(f"Content: {message.content}")

    if getattr(message, "tool_calls", None):
        print("Tool calls:", message.tool_calls)

    if getattr(message, "name", None):
        print("Tool name:", message.name)

