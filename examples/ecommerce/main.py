import os
import sys
import json
from typing import List, Dict, Any

# Add parent directory to sys.path to import shared client
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.fastmemory_client import FastMemoryClient

class EcommerceApp:
    def __init__(self):
        self.client = FastMemoryClient("Ecommerce-Platform")
        
        # Ecommerce Specific Config
        self.store_api = os.getenv("STORE_API_BASE", "https://api.mystore.com/v1")
        self.stripe_key = os.getenv("STRIPE_API_KEY", "sk_test_51P...")

    def build_graph(self) -> List[Dict[str, Any]]:
        """
        Builds the E-commerce graph using CBFDAE ontology.
        """
        self.client.logger.info("Defining E-commerce nodes...")
        atfs = [
            {"id": "C_Digital_Front", "type": "Component", "description": "Web and mobile storefronts"},
            {"id": "B_Checkout_Logic", "type": "Block", "links": ["C_Digital_Front"], "description": "Transactional workflow for carts"},
            {"id": "F_Dynamic_Pricing", "type": "Function", "links": ["B_Checkout_Logic"], "description": "Real-time price adjustment based on demand"},
            {"id": "D_Inventory_Matrix", "type": "Data", "links": ["F_Dynamic_Pricing"], "description": "Stock levels and variant metadata"},
            {"id": "A_Role_Authenticated_User", "type": "Access", "links": ["F_Dynamic_Pricing"], "description": "Customer access to pricing services"},
            {"id": "E_Cart_Updated", "type": "Event", "links": ["F_Dynamic_Pricing"], "description": "Trigger for cart recalculation"}
        ]
        return atfs

    def process_checkout(self, cart_id: str):
        """
        Retrieves fulfillment, tax, and pricing context for a cart.
        """
        self.client.logger.info(f"Processing checkout for cart: {cart_id} via {self.store_api}")
        # In production, this would query Neo4j or the Store API
        return {
            "cart_id": cart_id,
            "shipping_api": "Carrier_API_Sync",
            "fulfillment_event": "E_Package_Dispatched",
            "tax_logic": "F_Calculate_Sales_Tax"
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
        checkout_ctx = self.process_checkout("CART-449-01")
        print(f"\n[CHECKOUT CONTEXT]: {json.dumps(checkout_ctx, indent=2)}")
        
        self.client.logger.info("Ecommerce App execution completed.")

if __name__ == "__main__":
    app = EcommerceApp()
    try:
        app.run()
    finally:
        app.client.close()
