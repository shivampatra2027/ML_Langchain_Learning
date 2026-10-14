#paragraph basis split--> text based-->character ..
#Recusive text splitter is widely used and is the most famous.
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter

from dotenv import load_dotenv
load_dotenv()

text = """
My name is shivam patra.
I am in my final year.
I solved dsa and devlopment.
I am looking fwd for fde engineeer tech stacks.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)

result = splitter.split_text(text)

print("Total chunks:", len(result))
print(result[0])


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
# print(res)
# result2=splitter.split_text(res);
# print(result2);