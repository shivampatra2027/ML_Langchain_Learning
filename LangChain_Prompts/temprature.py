from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_huggingface import HuggingFacePipeline

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Load model
model = AutoModelForCausalLM.from_pretrained(model_id)

# Create Hugging Face pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=100,
    temperature=1.5
)

# Wrap HF pipeline with LangChain
llm = HuggingFacePipeline(pipeline=pipe)

messages=[
    {
        "role":"user",
        "content":"write a 5 lines poem on India"
    }
]

prompt=tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

# Invoke using LangChain
result = llm.invoke(
    prompt
)

print(result)