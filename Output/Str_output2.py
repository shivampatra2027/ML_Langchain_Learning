from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

prompt = PromptTemplate(
    template="Explain {topic} in simple terms.",
    input_variables=["topic"]
)

parser=StrOutputParser() #parse the string.

prompt2 = PromptTemplate(
    template = "Write the 5 line summary on the following {text}",
    input_variables=['text']
)


chain = prompt | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "India"});

print(result)
