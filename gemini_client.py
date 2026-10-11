
import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Always load .env from the project root,
# regardless of the script's working directory.
PROJECT_ROOT = Path(__file__).resolve().parent
load_dotenv(PROJECT_ROOT / ".env")

API_KEYS = [
    os.getenv("GEMINI_API_KEY"),
    os.getenv("ALTER_GEMINI_API_KEY"),
    os.getenv("ALTER_GEMINI_API_KEY1"),
]

API_KEYS = [key for key in API_KEYS if key]

if not API_KEYS:
    raise RuntimeError("No Gemini API keys configured.")


def invoke_with_fallback(prompt, model_name="gemini-2.5-flash"):
    last_error = None

    for index, api_key in enumerate(API_KEYS, start=1):
        try:
            model = ChatGoogleGenerativeAI(
                model=model_name,
                api_key=api_key,
                temperature=0.5,
                max_retries=0,
            )

            result = model.invoke(prompt)
            print(f"Gemini request succeeded using key {index}")
            return result

        except Exception as error:
            last_error = error
            message = str(error).lower()

            quota_error = any(term in message for term in [
                "429",
                "resource_exhausted",
                "quota exceeded",
                "rate limit",
            ])

            if not quota_error:
                raise

            print(f"Key {index} exhausted its quota or rate limit.")

    raise RuntimeError(
        "All configured Gemini keys failed."
    ) from last_error
