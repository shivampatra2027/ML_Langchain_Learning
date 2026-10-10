# 🤖 ML_STUFF — LangChain & LLM Learning Repository

A hands-on collection of Python scripts exploring **LangChain**, **LLMs**, **Embeddings**, **Prompt Engineering**, and **Output Parsers** — built while learning modern AI/ML development.

---

## 📁 Repository Structure

```
ML_STUFF/
│
├── Chat_Models/             # Exploring LLM chat model interfaces (OpenAI, Groq, etc.)
├── Embeddings/              # Text embedding techniques and vector representations
├── LLM_DEMO/                # Basic LLM usage demonstrations
├── LangChain_Prompts/       # Prompt templates, ChatPromptTemplates, FewShot prompts
├── Output/                  # Output Parsers — StrOutput, Pydantic, JSON
│   ├── Str_Output_Parser.py
│   ├── Pydantic_Output_Parser.py
│   └── Json_Output_parser.py
├── Pydantic/                # Pydantic model definitions and validations
├── requirements.txt         # Python dependencies
├── test.py                  # Quick test/sandbox script
└── .gitignore
```

---

## 🧠 Topics Covered

| Module | What's Explored |
|---|---|
| **LLM_DEMO** | Calling LLMs, understanding completions |
| **Chat_Models** | Using `ChatOpenAI`, `ChatGroq`, message types |
| **LangChain_Prompts** | `PromptTemplate`, `ChatPromptTemplate`, `FewShotPromptTemplate` |
| **Embeddings** | `OpenAIEmbeddings`, vector similarity, use cases |
| **Output Parsers** | `StrOutputParser`, `JsonOutputParser`, `PydanticOutputParser` |
| **Pydantic** | Schema definitions, validation, integration with LangChain |

---

## ⚙️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/shivampatra2027/ML_STUFF.git
cd ML_STUFF
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/macOS
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key        # if using Groq
LANGCHAIN_API_KEY=your_langsmith_key  # optional, for tracing
LANGCHAIN_TRACING_V2=true             # optional
```

> ⚠️ Never commit your `.env` file — it's already in `.gitignore`.

---

## 🔍 Key Concepts

### Output Parsers
LangChain output parsers transform raw LLM responses into structured formats:

- **`StrOutputParser`** — Extracts plain string output from a message
- **`JsonOutputParser`** — Parses LLM output as JSON (dict/list)
- **`PydanticOutputParser`** — Validates and parses output into a Pydantic model

```python
# Example: Pydantic Output Parser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int

parser = PydanticOutputParser(pydantic_object=Person)
```

### Prompt Templates
```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}")
])
```

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-0.3.x-green?logo=chainlink)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?logo=openai)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-red)

- **Python 3.10+**
- **LangChain / LangChain-Core**
- **OpenAI / Groq** — LLM providers
- **Pydantic v2** — Data validation
- **python-dotenv** — Environment variable management

---

## 📈 Progress Tracker

- [x] LLM basic demos
- [x] Chat Models
- [x] Embeddings
- [x] Prompt Engineering
- [x] String Output Parser
- [x] JSON Output Parser
- [x] Pydantic Output Parser
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] Agents & Tools
- [ ] Memory & Conversation History
- [ ] Vector Stores (FAISS, Chroma)

---

## 📄 License

This project is for **personal learning purposes**. Feel free to fork and explore!

---

## 👤 Author

**Shivam Patra**
- GitHub: [@shivampatra2027](https://github.com/shivampatra2027)

