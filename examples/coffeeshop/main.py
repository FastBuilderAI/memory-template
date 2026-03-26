import os
import sys
import json
from typing import List, Dict, Any

# Add parent directory to sys.path to import shared client
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.fastmemory_client import FastMemoryClient

class CoffeeShopApp:
    def __init__(self):
        self.client = FastMemoryClient("CoffeeShop")
        
        # Coffee Shop Specific Config
        self.square_token = os.getenv("SQUARE_ACCESS_TOKEN", "sq-test-token")
        self.loyalty_url = os.getenv("LOYALTY_SERVICE_URL", "https://loyalty.coffeeshop.com")

    def build_graph(self) -> List[Dict[str, Any]]:
        """
        Builds the Counter Service graph using CBFDAE ontology.
        """
        self.client.logger.info("Defining Coffee Shop nodes...")
        atfs = [
            {"id": "C_Counter_Service", "type": "Component", "description": "Primary point of sale interaction"},
            {"id": "B_Barista_Queue", "type": "Block", "links": ["C_Counter_Service"], "description": "LIFO/FIFO queue for drinks"},
            {"id": "F_Inventory_Deduct", "type": "Function", "links": ["B_Barista_Queue"], "description": "Real-time stock adjustment"},
            {"id": "D_Stock_Levels", "type": "Data", "links": ["F_Inventory_Deduct"], "description": "Product availability registry"},
            {"id": "A_Role_Barista", "type": "Access", "links": ["F_Inventory_Deduct"], "description": "Permission to modify stock"},
            {"id": "E_Order_Pickup_Ready", "type": "Event", "links": ["F_Inventory_Deduct"], "description": "Trigger for customer notification"}
        ]
        return atfs

    def process_loyalty(self, customer_id: str):
        """
        Simulates loyalty logic verification.
        """
        self.client.logger.info(f"Checking loyalty status for {customer_id} via {self.loyalty_url}")
        # In production, this would query the loyalty microservice
        return {
            "customer": customer_id,
            "tier": "Gold",
            "eligible_for_reward": True,
            "last_interaction": "2024-03-25"
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
        customer_ctx = self.process_loyalty("CUST-102")
        print(f"\n[LOYALTY CONTEXT]: {json.dumps(customer_ctx, indent=2)}")
        
        self.client.logger.info("Coffee Shop App execution completed.")

if __name__ == "__main__":
    app = CoffeeShopApp()
    try:
        app.run()
    finally:
        app.client.close()
