from agents import get_strategist_advice, get_technologist_advice, get_lawyer_advice

def run_council(business_idea: str) -> dict:
    """
    Runs all agents and returns a dictionary of their advice.
    """
    results = {}
    results["Strategist"] = get_strategist_advice(business_idea)
    results["Technologist"] = get_technologist_advice(business_idea)
    results["Lawyer"] = get_lawyer_advice(business_idea)
    return results
