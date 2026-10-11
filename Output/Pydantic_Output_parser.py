from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# 1. Initialize Gemini
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

# 2. Define the output schema
class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(description="Age of the person")
    city: str = Field(description="City the person belongs to")

# 3. Create the parser
parser = PydanticOutputParser(
    pydantic_object=Person
)

# 4. Create the prompt template
template = PromptTemplate(
    template=(
        "Generate the name, age and city of a fictional person "
        "from {place}.\n{format_instructions}"
    ),
    input_variables=["place"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

# 5. Format the prompt
prompt = template.format(place="India")
print(prompt);
# 6. Call Gemini
response = model.invoke(prompt)

print("Raw response:")
print(response.content)

# 7. Parse and validate the response
final_result = parser.parse(response.content)

print("\nParsed result:")
print(final_result)

print("\nName:", final_result.name)
print("Age:", final_result.age)
print("City:", final_result.city)
print("Type:", type(final_result))
