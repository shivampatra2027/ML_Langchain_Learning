from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq;
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pypdf import PdfReader;
load_dotenv();

model=ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5
)

prompt=PromptTemplate(
    template='Write a summary on the following poem\n {poem}',
    input_variables=['poem']
)

parser=StrOutputParser();
loader=PyPDFLoader('poem.pdf')
docs=loader.load()
print(docs[0].page_content);

#creating a chain.
chain=prompt | model | parser;
res=chain.invoke({'poem':docs[0].page_content});
print(res);
