import streamlit as st

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline
)

from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate


# -----------------------------
# Load model
# -----------------------------

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(model_id)


# -----------------------------
# Hugging Face pipeline
# -----------------------------

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=100,
    temperature=0.7
)


# -----------------------------
# LangChain LLM
# -----------------------------

llm = HuggingFacePipeline(
    pipeline=pipe
)


# -----------------------------
# Prompt Template
# -----------------------------

template = PromptTemplate(
    input_variables=[
        "paper_input",
        "style_input",
        "length_input"
    ],
    template="""
Summarize the research paper titled "{paper_input}".

Explanation Style:
{style_input}

Explanation Length:
{length_input}

Include important mathematical concepts and equations where applicable.

Use simple analogies to explain difficult concepts.

If information is not available, do not guess.
"""
)


# -----------------------------
# LCEL Chain
# -----------------------------

chain = template | llm


# -----------------------------
# Streamlit UI
# -----------------------------

st.header("Research Paper Summarizer")


paper_input = st.text_input(
    "Research paper"
)


style_input = st.selectbox(
    "Style",
    ["Simple", "Technical", "Mathematical"]
)


length_input = st.selectbox(
    "Length",
    ["Short", "Medium", "Detailed"]
)


if st.button("Summarize"):

    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })

    st.write(result)