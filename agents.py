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
    temperature=0.2
)

def get_strategist_advice(business_idea: str) -> str:
    """
    Evaluates a business idea from the Strategist's perspective.
    Returns one of: Great opportunity / Needs improvement / Not worth the risk
    with a clear justification.
    """
    prompt = PromptTemplate.from_template(
        """
        You are The Strategist — a seasoned business advisor who is highly rational and critical.
        Evaluate the following business idea strictly from a strategic and market viability perspective.

        Business idea:
        {idea}

        Your output must follow this exact format:

        Verdict: [Great opportunity | Needs improvement | Not worth the risk]
        Reasoning: [1-3 concise sentences that justify your verdict clearly and critically.]

        Be objective and deterministic — avoid vague optimism or indecision.

        Verdict rules:
            - Great opportunity → high market demand, clear monetization, competitive moat.
            - Needs improvement → partial potential, missing differentiation or unclear value.
            - Not worth the risk → weak demand, poor scalability, or fundamental flaw.
        """
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
    )
    #return llm.invoke(prompt.format(idea=business_idea))'''
    return "Technology advice functionality is currently under development."

def get_marketer_advice(business_idea: str) -> str:
    '''prompt = PromptTemplate.from_template(
        "You are The Marketer — an expert in go-to-market strategy. "
        "Analyze this business idea: {idea}. Suggest target audience, acquisition channels, and positioning."
        "Answer in a concise manner. Don't repeat the idea."
        "Provide actionable insights and get into details other than your expertise."
        "Be specific and avoid generic statements."
    )
    #return llm.invoke(prompt.format(idea=business_idea))'''
    return "Marketing advice functionality is currently under development."
