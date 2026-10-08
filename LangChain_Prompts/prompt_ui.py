import streamlit as st

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline
)

from langchain_huggingface import HuggingFacePipeline
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_id);
model = AutoModelForCausalLM.from_pretrained(model_id)

pipe= pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=100,
    temperature=1.5
);



llm = HuggingFacePipeline(
    pipeline=pipe
)

st.header("Research tool");
user_input= st.text_input("Enter your prompt")
if st.button("Summarize"):
    messages=[
        {
            "role":"system",
            "content":"You are a helpful assistant."
        },
        {
            "role":"user",
            "content":user_input
        }
    ]
    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    result = llm.invoke(prompt)

    st.write(result)