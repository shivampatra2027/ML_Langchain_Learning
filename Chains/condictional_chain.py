from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
import sys
from pathlib import Path

#These are just setups..
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from gemini_client import invoke_with_fallback

load_dotenv()


#This code is for if you want to use direct api from .env
# model = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     temperature=0.5
# )

#This code if u want to use api from gemini.client.py
model = RunnableLambda(
    lambda prompt_value: invoke_with_fallback(
        prompt_value.to_string()
    )
)

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Sentiment of the feedback: positive or negative"
    )

parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template=(
        "Classify the following feedback as positive or negative.\n"
        "{feedback}\n"
        "{format_instruction}"
    ),
    input_variables=["feedback"],
    partial_variables={
        "format_instruction": parser2.get_format_instructions()
    } 
)

classifier_chain = prompt1 | model | parser2

# result = classifier_chain.invoke({
#     "feedback": "This is a nice smartphone!"
# })

prompt2=PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3=PromptTemplate(
    template='Write an appropriate response to this Negative feedback \n {feedback}',
    input_variables=['feedback']
)
branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='positive', prompt2 | model | parser),
    (lambda x:x.sentiment=='negative',prompt3 | model | parser),
    RunnableLambda(lambda x:"Could not find sentiment") #Runnable normal lambda ko chain me convert kar deta hai.
    #Runnblae branch ke anadar har cheeze chains me hoga isilye humne default lamnda to Runnable me convert kiya.
)

chain=classifier_chain | branch_chain
result =chain.invoke({'feedback':'This is a terrible phone'});
# print(result);
print(result)
# print(result.sentiment)
# chain.get_graph().print_ascii();
