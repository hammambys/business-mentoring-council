import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize the Groq model once, all agents will use it
llm = ChatGroq(
    model="llama-3.3-70b-versatile",  # example Groq model
    groq_api_key=GROQ_API_KEY,
    temperature=0.7
)

def get_strategist_advice(business_idea: str) -> str:
    prompt = PromptTemplate.from_template(
        "You are The Strategist — a business expert. Analyze this business idea: {idea}. "
        "Provide advice on business model viability, risks, and opportunities."
        "Answer in a concise manner. Don't repeat the idea."
        "Provide actionable insights and get into details other than your expertise."
        "Be specific and avoid generic statements."
    )
    response = llm.invoke(prompt.format(idea=business_idea))
    return response.content

def get_technologist_advice(business_idea: str) -> str:
    '''prompt = PromptTemplate.from_template(
        "You are The Technologist — an expert in product and AI architecture. "
        "Analyze this business idea: {idea}. Suggest a minimal tech stack and MVP plan."
        "Answer in a concise manner. Don't repeat the idea."
        "Provide actionable insights and get into details other than your expertise."
        "Be specific and avoid generic statements."
    )'''
    #return llm.invoke(prompt.format(idea=business_idea))
    return "Technology advice functionality is currently under development."

def get_marketer_advice(business_idea: str) -> str:
    '''prompt = PromptTemplate.from_template(
        "You are The Marketer — an expert in go-to-market strategy. "
        "Analyze this business idea: {idea}. Suggest target audience, acquisition channels, and positioning."
        "Answer in a concise manner. Don't repeat the idea."
        "Provide actionable insights and get into details other than your expertise."
        "Be specific and avoid generic statements."
    )'''
    #return llm.invoke(prompt.format(idea=business_idea))
    return "Marketing advice functionality is currently under development."
