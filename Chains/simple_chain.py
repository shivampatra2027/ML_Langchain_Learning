from langchain_google_genai import ChatGoogleGenerativeAI;
from dotenv import load_dotenv;
from langchain_core.prompts import PromptTemplate;
from langchain_core.output_parsers import StrOutputParser;

load_dotenv();

model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    # max_output_tokens,
    temperature=0.5
)
prompt1 = PromptTemplate(
    template='Generate 5 intresting facts on the topic {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Genearate tone of the follwing {text}. Use only positive negative or neutral',
    input_variables=['text']
)
parser = StrOutputParser()
#prompt ko model me daalo and then jo response aayega model se use parser me dalo. ise chain bolte hai.
chain = prompt1 | model | prompt2 | model | parser

result =chain.invoke({'topic':'India'});
# print(result);

print("Printing the Chain Diagram..!");
chain.get_graph().print_ascii(); #This line is for visualisze the chain..

# print(chain.get_graph().draw_mermaid())
