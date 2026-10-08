from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_huggingface import HuggingFacePipeline

# Choose the model you want to run locally
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Download and load model + tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Build a local text-generation pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    temperature=0.5,
    max_new_tokens=100
)

# Wrap with LangChain
llm = HuggingFacePipeline(pipeline=pipe)

# Run inference locally
prompt = """<|system|>
You are a helpful assistant.
<|user|>
What is the capital of India?
<|assistant|>
"""

result = llm.invoke(prompt)
print(result)
