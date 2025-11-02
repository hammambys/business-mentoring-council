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
    temperature=0.2)

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

        Verdict: 
        [Great opportunity | Needs improvement | Not worth the risk]
        Reasoning: 
        - [1 short sentence — direct, critical, no filler.]
        Suggestions: 
        - if Verdict is "Great opportunity", provide a step-by-step business strategy/plan for the idea.
        - if Verdict is "Needs improvement", provide 1-3 specific suggestions to enhance the idea.
        - if Verdict is "Not worth the risk", provide alternative ideas that could work better in the same domain.

        Be objective and deterministic — avoid vague optimism or indecision.
        """
    )
    response = llm.invoke(prompt.format(idea=business_idea))
    return response.content

def get_technologist_advice(business_idea: str) -> str:
    """
    Evaluates a business idea from the Technologist's perspective.
    Returns one of: Easy / Challenging / Impossible
    with a clear justification and technical feasibility analysis.
    """
    prompt = PromptTemplate.from_template(
        """
        You are The Technologist — a veteran tech expert who is highly rational and critical.
        Evaluate the following business idea strictly from a technical feasibility and innovation perspective.

        Business idea: {idea}

        Your output must follow this exact format:

        Verdict: 
        [Easy | Challenging | Impossible]
        Reasoning:
        - concise summary of technical feasibility in 1 short sentence — direct, critical, no filler.
        Suggestions: 
        - if Verdict is "Easy", provide a high-level tech stack and architecture plan.
        - if Verdict is "Challenging", provide 1-3 specific technical hurdles and how to overcome them.
        - if Verdict is "Impossible", explain the fundamental technical limitations and suggest alternative approaches.

        Be objective and deterministic — avoid vague optimism or indecision.
        """
    )
    response = llm.invoke(prompt.format(idea=business_idea))
    return response.content

def get_lawyer_advice(business_idea: str) -> str:
    prompt = PromptTemplate.from_template(
        """
        You are The Lawyer — an experienced legal advisor who is highly rational and critical.
        Evaluate the following business idea strictly from a legal and regulatory compliance perspective.

        Business idea: {idea}

        Your output must follow this exact format:

        Verdict: 
        [Legal | Risky | Illegal]
        Reasoning: 
        - 1 short sentence — direct, critical, no filler.
        Suggestions: 
        - if Verdict is "Legal", provide key legal considerations to keep in mind in short sentences. 
        - if Verdict is "Risky", provide 1-3 specific legal risks and how to mitigate them in short sentences.
        - if Verdict is "Illegal", explain the legal violations and suggest compliant alternatives in short sentences.

        Be objective and deterministic — avoid vague optimism or indecision.
        """
    )
    
    response = llm.invoke(prompt.format(idea=business_idea))
    return response.content
