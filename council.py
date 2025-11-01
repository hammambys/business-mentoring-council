from langgraph.graph import StateGraph, END
from typing import TypedDict
from agents import (
    get_strategist_advice,
    get_technologist_advice,
    get_marketer_advice,
)

# Define the shape of our data (the “state” passed through the graph)
class CouncilState(TypedDict):
    idea: str
    Strategist: str
    Technologist: str
    Marketer: str


# Define each node as a function that mutates the state
def strategist_node(state: CouncilState):
    state["Strategist"] = get_strategist_advice(state["idea"])
    return state


def technologist_node(state: CouncilState):
    state["Technologist"] = get_technologist_advice(state["idea"])
    return state


def marketer_node(state: CouncilState):
    state["Marketer"] = get_marketer_advice(state["idea"])
    return state


def run_council(business_idea: str):
    # Initialize a new state graph
    graph = StateGraph(CouncilState)

    # Add nodes
    graph.add_node("Strategist", strategist_node)
    graph.add_node("Technologist", technologist_node)
    graph.add_node("Marketer", marketer_node)

    # Set start and end points
    graph.set_entry_point("Strategist")
    graph.add_edge("Strategist", "Technologist")
    graph.add_edge("Technologist", "Marketer")
    graph.add_edge("Marketer", END)

    # Compile the graph
    app = graph.compile()

    # Run the graph with the initial state
    initial_state = {
        "idea": business_idea,
        "Strategist": "",
        "Technologist": "",
        "Marketer": ""
    }
    final_state = app.invoke(initial_state)

    return final_state
