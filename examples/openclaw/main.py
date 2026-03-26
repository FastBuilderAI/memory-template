import os
import sys
import json
from typing import List, Dict, Any

# Add parent directory to sys.path to import shared client
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.fastmemory_client import FastMemoryClient

class OpenClawApp:
    def __init__(self):
        self.client = FastMemoryClient("OpenClaw-Integration")
        
        # OpenClaw Specific Config
        self.oc_key = os.getenv("OPENCLAW_API_KEY", "oc-secret-123")
        self.mcp_url = os.getenv("FASTMEMORY_MCP_URL", "http://localhost:8000/mcp")

    def initialize_integration(self) -> Dict[str, Any]:
        """
        Sets up the bridge between OpenClaw and FastMemory MCP.
        """
        self.client.logger.info(f"Connecting OpenClaw agent to MCP at {self.mcp_url}")
        return {
            "mcp_server": self.mcp_url,
            "status": "connected",
            "tools": ["query_memory", "get_block", "update_cluster"]
        }

    def agent_reasoning_loop(self, user_input: str):
        """
        Simulates an agent using FastMemory to retrieve context before acting.
        """
        self.client.logger.info(f"Agent received input: '{user_input}'")
        
        # 1. Build context via CBFDAE graph
        context = [
            {"id": "C_Agent_Runtime", "type": "Component", "description": "Core execution environment for the agent"},
            {"id": "B_Interactive_Buffer", "type": "Block", "links": ["C_Agent_Runtime"], "description": "Short-term memory for active conversation"},
            {"id": "F_State_Normalization", "type": "Function", "links": ["B_Interactive_Buffer"], "description": "Logic to align agent state with FastMemory"},
            {"id": "D_Taxon_Vector", "type": "Data", "links": ["F_State_Normalization"], "description": "Vector representation of taxonomic data"},
            {"id": "A_Role_Decider", "type": "Access", "links": ["F_State_Normalization"], "description": "Permission to execute decision-making functions"},
            {"id": "E_Perceptual", "type": "Event", "links": ["F_State_Normalization"], "description": "Trigger confirming perceptual input processing"}
        ]
        
        self.client.logger.debug(f"Retrieved context nodes: {len(context)}")
        self.client.deploy_graph(context)
        
        return f"Agent Logic: Processed '{user_input}' using FastMemory Context (CBFDAE)."

    def run(self):
        """
        Main execution flow.
        """
        self.client.health_check()
        
        # 1. Initialize Integration
        integ = self.initialize_integration()
        print(f"\n[INTEGRATION STATUS]: {json.dumps(integ, indent=2)}")
        
        # 2. Run Reasoning Loop
        response = self.agent_reasoning_loop("Fix the indentation bug in the deployment script")
        print(f"\n[AGENT RESPONSE]: {response}")
        
        self.client.logger.info("OpenClaw App execution completed.")

if __name__ == "__main__":
    app = OpenClawApp()
    try:
        app.run()
    finally:
        app.client.close()
