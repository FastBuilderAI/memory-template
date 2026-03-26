import os
import sys
import json
from typing import List, Dict, Any

# Add parent directory to sys.path to import shared client
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.fastmemory_client import FastMemoryClient

class RestaurantApp:
    def __init__(self):
        self.client = FastMemoryClient("Restaurant-Kitchen")
        
        # Restaurant Specific Config
        self.kds_ip = os.getenv("KDS_IP_ADDRESS", "192.168.1.50")
        self.recipe_path = os.getenv("RECIPE_DB_PATH", "./data/recipes.json")

    def build_graph(self) -> List[Dict[str, Any]]:
        """
        Builds the Restaurant graph using CBFDAE ontology.
        """
        self.client.logger.info("Defining Restaurant Kitchen nodes...")
        atfs = [
            {"id": "C_Table_Service", "type": "Component", "description": "Dining room floor management system"},
            {"id": "B_KDS_Display", "type": "Block", "links": ["C_Table_Service"], "description": "Kitchen Display System for order tracking"},
            {"id": "F_Course_Timing", "type": "Function", "links": ["B_KDS_Display"], "description": "Logic to orchestrate appetizers vs. mains"},
            {"id": "D_Recipe_Scale", "type": "Data", "links": ["F_Course_Timing"], "description": "Standardized portions and ingredient list"},
            {"id": "A_Role_Sous_Chef", "type": "Access", "links": ["F_Course_Timing"], "description": "Authorized control over kitchen workflows"},
            {"id": "E_Ticket_Cleared", "type": "Event", "links": ["F_Course_Timing"], "description": "Trigger when an order is completed and bumped"}
        ]
        return atfs

    def calculate_table_context(self, table_number: int):
        """
        Retrieves recipe and wastage context for a specific table.
        """
        self.client.logger.info(f"Calculating context for Table: {table_number} via KDS at {self.kds_ip}")
        # In production, this would query Neo4j or the KDS
        return {
            "table_number": table_number,
            "active_order": "ORD-553",
            "waste_tracking": "F_Waste_Tracker",
            "payment_logic": "F_Split_Check"
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
        table_ctx = self.calculate_table_context(12)
        print(f"\n[TABLE CONTEXT]: {json.dumps(table_ctx, indent=2)}")
        
        self.client.logger.info("Restaurant App execution completed.")

if __name__ == "__main__":
    app = RestaurantApp()
    try:
        app.run()
    finally:
        app.client.close()
