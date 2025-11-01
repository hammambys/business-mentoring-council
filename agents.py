import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",  # example Groq model name
    groq_api_key=GROQ_API_KEY,
    temperature=0.7
)

def get_strategist_advice(business_idea: str) -> str:
    prompt = PromptTemplate.from_template(
        "You are The Strategist — a business expert. Analyze this business idea: {idea}. "
        "Provide advice on business model viability, risks, and opportunities."
    )
    response = llm.invoke(prompt.format(idea=business_idea))
    return response
