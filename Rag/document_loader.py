from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv;

load_dotenv();

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5
)
prompt= PromptTemplate(
    template='Write a summary on the follwing poem\n {poem}',
    input_variables=['poem']
)
parser=StrOutputParser();
loader = TextLoader('ai.txt',encoding='utf-8');

docs=loader.load();



# print(docs[0].page_content);
print(docs[0].metadata);

chain=prompt | model | parser
res=chain.invoke({'poem':docs[0].page_content})
print(res);


#why we need text-loader-->text loader provides u a document objects, by which u can have the flexibility to do any thing like injetion pipeline etc.

#textloader provides 2 thing: document content and document metadata.