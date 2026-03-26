import os
import sys
import json
from typing import List, Dict, Any

# Add parent directory to sys.path to import shared client
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.fastmemory_client import FastMemoryClient

class CRMApp:
    def __init__(self):
        self.client = FastMemoryClient("CRM-RevenueOps")
        
        # CRM Specific Config
        self.sf_url = os.getenv("SALESFORCE_INSTANCE_URL", "https://na1.salesforce.com")
        self.api_key = os.getenv("CRM_API_KEY", "crm-secret-key")

    def build_graph(self) -> List[Dict[str, Any]]:
        """
        Builds the Revenue Ops graph using CBFDAE ontology.
        """
        self.client.logger.info("Defining CRM Revenue Ops nodes...")
        atfs = [
            {"id": "C_Revenue_Ops", "type": "Component", "description": "Revenue operations and sales tracking"},
            {"id": "B_Sales_Pipeline", "type": "Block", "links": ["C_Revenue_Ops"], "description": "Structured stages of the sales deal"},
            {"id": "F_Lead_Scoring", "type": "Function", "links": ["B_Sales_Pipeline"], "description": "AI-driven priority assignment"},
            {"id": "D_Prospect_Metadata", "type": "Data", "links": ["F_Lead_Scoring"], "description": "Firmographic and behavioral data"},
            {"id": "A_Role_SDR_Associate", "type": "Access", "links": ["F_Lead_Scoring"], "description": "Permission to view and score leads"},
            {"id": "E_Lead_Qualified", "type": "Event", "links": ["F_Lead_Scoring"], "description": "Trigger for Sales Representative handoff"}
        ]
        return atfs

    def execute_query(self, client_id: str):
        """
        Retrieves sales and invoice context for a specific client.
        """
        self.client.logger.info(f"Retrieving context for client: {client_id} via {self.sf_url}")
        # In production, this would query Neo4j or Salesforce
        return {
            "client_id": client_id,
            "status": "In_Negotiation",
            "last_invoice": "INV-2024-882",
            "assigned_sdr": "sdr_jane_doe",
            "access_required": "Role_Finance"
        }

    def run(self):
        """
        Main execution flow.
        """
        self.client.health_check()
        
        # 1. Build and Deploy Graph
        graph = self.build_graph()
        self.client.deploy_graph(graph)
        
        # 2. Simulate Business Logic
        client_ctx = self.execute_query("CLI-882")
        print(f"\n[CLIENT CONTEXT]: {json.dumps(client_ctx, indent=2)}")
        
        self.client.logger.info("CRM App execution completed.")

if __name__ == "__main__":
    app = CRMApp()
    try:
        app.run()
    finally:
        app.client.close()
