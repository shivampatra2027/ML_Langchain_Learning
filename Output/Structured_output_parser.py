
from langchain_classic.output_parsers import (
    StructuredOutputParser,
    ResponseSchema
)
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# 1. Initialize Gemini
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

# 2. Define the expected response schema
schema = [
    ResponseSchema(
        name="fact_1",
        description="First fact about the topic",
        type="string"
    ),
    ResponseSchema(
        name="fact_2",
        description="Second fact about the topic",
        type="string"
    ),
    ResponseSchema(
        name="fact_3",
        description="Third fact about the topic",
        type="string"
    )
]

# 3. Create the parser
parser = StructuredOutputParser.from_response_schemas(schema)

# 4. Create the prompt template
template = PromptTemplate(
    template=(
        "Give 3 facts about {topic}.\n"
        "{format_instructions}"
    ),
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

# 5. Format the prompt
prompt = template.format(topic="black holes")

# 6. Call Gemini
response = model.invoke(prompt)

print("Raw response:")
print(response.content)

# 7. Parse the response
final_result = parser.parse(response.content)

print("\nParsed result:")
print(final_result)
print(type(final_result))
print(final_result["fact_1"])
