from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5
)

model2 = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5
)

prompt1 = PromptTemplate(
    template='Generate a detailed summary on the following topic: {topic}\n',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Provide a short quiz on the following topic: {topic}\n',
    input_variables=['topic']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document:\n\nNotes: {notes}\n\nQuiz: {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

chain1 = prompt1 | model1 | parser
chain2 = prompt2 | model2 | parser

parallel_chain = RunnableParallel(
    notes=chain1,
    quiz=chain2
)

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

result = chain.invoke({
    'topic': 'India'
})

print("Printing full result:\n")
# print(result) 

# chain.get_graph().print_ascii();  #Run this to see the magic.


# print('\nPrinting notes\n')
print(result['notes'])

# print('\nPrinting quiz\n')
# print(result['quiz'])
