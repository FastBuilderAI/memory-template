import os
import sys
import json
from typing import TypedDict, List, Annotated
try:
    from langgraph.graph import StateGraph, START, END
    from langchain_openai import ChatOpenAI
    from langchain_core.messages import HumanMessage, SystemMessage
    LANGGRAPH_AVAILABLE = True
except ImportError:
    LANGGRAPH_AVAILABLE = False

# Add parent directory to sys.path to import shared client
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.fastmemory_client import FastMemoryClient

# Define State Structure
class AgentState(TypedDict):
    question: str
    graph_context: str
    answer: str

class SEOLangGraphQuery:
    def __init__(self):
        self.client = FastMemoryClient("SEO-Agent-Query")
        self.llm = ChatOpenAI(model="gpt-4o", api_key=self.client.llm_api_key)
        
    def retrieve_graph_context(self, state: AgentState) -> AgentState:
        """
        Retrieves relevant CBFDAE nodes from Neo4j based on the user's question.
        In mock mode, it returns the static ontology defined in main.py.
        """
        self.client.logger.info(f"Retrieving graph context for question: {state['question']}")
        
        # Cypher query to find relevant nodes and their neighbors
        # In a real scenario, we'd use entity extraction first, but here we query for keywords
        query = """
        MATCH (n:MemoryNode)-[:CONNECTS_TO*1..2]-(m)
        RETURN n.id as node, m.id as neighbor, n.description as desc
        LIMIT 20
        """
        results = self.client.execute_query(query)
        
        if not results:
            # Fallback for mock mode: return the core SEO ontology
            self.client.logger.info("No Neo4j results found. Using mock SEO ontology.")
            context = {
                "Component": "C_Client_Success (SEO management)",
                "Block": "B_SEO_Strategy (Tactic planning)",
                "Function": "F_Keyword_Harvesting (Discovery engine)",
                "Data": "D_Keyword_Clusters (Search terms)",
                "Access": "A_Role_SEO_Analyst (Strategy access)",
                "Event": "E_Ranking_Update (Position changes)"
            }
            state["graph_context"] = json.dumps(context, indent=2)
        else:
            state["graph_context"] = json.dumps(results, indent=2)
            
        return state

    def generate_answer(self, state: AgentState) -> AgentState:
        """
        Synthesizes an answer using the retrieved graph context.
        """
        self.client.logger.info("Generating answer based on graph context...")
        
        system_prompt = (
            "You are a Senior SEO Architect. Use the provided FastMemory graph context "
            "(CBFDAE ontology) to answer the user's question accurately. "
            "Explain how the different components (Blocks, Functions, Data) interact "
            "to solve their problem. If the context is empty, explain the FastMemory SEO model."
        )
        
        human_prompt = f"Question: {state['question']}\n\nGraph Context:\n{state['graph_context']}"
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=human_prompt)
        ]
        
        response = self.llm.invoke(messages)
        state["answer"] = response.content
        return state

    def build_graph(self):
        """
        Builds the LangGraph workflow.
        """
        workflow = StateGraph(AgentState)
        
        # Add Nodes
        workflow.add_node("retrieve_graph", self.retrieve_graph_context)
        workflow.add_node("generate_response", self.generate_answer)
        
        # Add Edges
        workflow.add_edge(START, "retrieve_graph")
        workflow.add_edge("retrieve_graph", "generate_response")
        workflow.add_edge("generate_response", END)
        
        return workflow.compile()

def run_query(question: str):
    if not LANGGRAPH_AVAILABLE:
        print("\n[ERROR]: Missing dependencies. Please run 'pip install -r requirements.txt' first.")
        return

    agent = SEOLangGraphQuery()
    graph = agent.build_graph()
    
    initial_state = {"question": question, "graph_context": "", "answer": ""}
    final_state = graph.invoke(initial_state)
    
    print("\n" + "="*50)
    print(f"QUESTION: {question}")
    print("="*50)
    print(f"RESPONSE:\n{final_state['answer']}")
    print("="*50 + "\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_q = " ".join(sys.argv[1:])
    else:
        user_q = "How do we handle keyword clustering and ranking updates in our SEO strategy?"
        
    run_query(user_q)
