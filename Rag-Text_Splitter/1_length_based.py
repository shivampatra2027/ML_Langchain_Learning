
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_text_splitters import CharacterTextSplitter

from dotenv import load_dotenv
load_dotenv()

text = """Artificial Intelligence, commonly known as AI, is a branch of computer science that focuses on developing machines and software capable of performing tasks that typically require human intelligence. These tasks include learning, reasoning, problem-solving, understanding language, recognizing images, and making decisions. Machine Learning is a subset of Artificial Intelligence that enables computers to learn patterns from data without being explicitly programmed for every situation. Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers to learn complex patterns from large datasets. Natural Language Processing (NLP) allows computers to understand, interpret, and generate human language. It powers applications such as chatbots, language translation, sentiment analysis, and text summarization."""



splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10,
    separator=" "
)

result = splitter.split_text(text)

print("Total chunks:", len(result))
# print(result[0])




#want to view all text-->run thia
# for i, chunk in enumerate(result, start=1):
#     print(f"\nChunk {i} ({len(chunk)} characters):")
#     print(chunk)

#passing the splitted text into LLM.

model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)
prompt=PromptTemplate(
    template="Expalin the {topic} in simple Line.",
    input_variables=["topic"]
)

parser=StrOutputParser()

chain = prompt | model | parser
res=chain.invoke({"topic":result})
print(res)