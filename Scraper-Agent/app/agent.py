import os
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()

# Load API key from env
api_key = os.getenv("OPENAI_API_KEY")

# Langchain LLM setup
llm = OpenAI(openai_api_key=api_key, temperature=0.3)

# Example summarizer
def summarize_text(text):
    template = PromptTemplate.from_template(
        "Summarize the following text in 2 lines:\n\n{text}"
    )
    prompt = template.format(text=text)
    summary = llm(prompt)
    return summary
