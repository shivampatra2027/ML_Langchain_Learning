from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
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

parser = JsonOutputParser();   #parse the json
#JsonOutputParser() converts the model's JSON-formatted text into a Python object, usually a dictionary (dict).

template=PromptTemplate(
    template="Give me the,age and city of a fictional person {name} \n{format_instructions}",
    input_variables = ['name'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

# prompt = template.format();
# print(prompt);
# response = model.invoke(prompt)   #use tokens usage.
# content = response.content;  
# result = parser.invoke(content);   #no tokens usage
# print(result);
# print("\nType of result is",type(result));

# same thing using chains..
prompt = template.format(name='Bill Gates')
print(prompt);
chain = template | model | parser
result  = chain.invoke({'name':'Bill Gates'});
print(result);
print("Type=",type(result));


#The biggest flow of Json output parser is that it donot enforces a default schema.