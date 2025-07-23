import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

load_dotenv()

# ✅ Load Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# ✅ Setup Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-pro-latest",
    google_api_key=api_key,
    temperature=0.3
)

# ✅ Summarize Function
def summarize_text(text):
    try:
        template = PromptTemplate.from_template(
            "Summarize the following text in 2 lines:\n\n{text}"
        )
        safe_input = text[:3000]  # limit input to avoid overload
        prompt = template.format(text=safe_input)
        summary = llm.invoke(prompt)
        return summary
    except Exception as e:
        return f"[❌ Gemini Error]: {str(e)}"

