import os
import sys
import json
from typing import List, Dict, Any

# Add parent directory to sys.path to import shared client
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.fastmemory_client import FastMemoryClient

class ERPApp:
    def __init__(self):
        self.client = FastMemoryClient("ERP-SupplyChain")
        
        # ERP Specific Config
        self.erp_endpoint = os.getenv("ERP_ENDPOINT", "https://erp.internal.company.com")
        self.erp_secret = os.getenv("ERP_SECRET", "erp-auth-token")

    def build_graph(self) -> List[Dict[str, Any]]:
        """
        Builds the ERP Inventory graph using CBFDAE ontology.
        """
        self.client.logger.info("Defining ERP Inventory nodes...")
        atfs = [
            {"id": "C_Supply_Chain", "type": "Component", "description": "Global supply chain and logistics engine"},
            {"id": "B_Inventory_Sync", "type": "Block", "links": ["C_Supply_Chain"], "description": "Real-time synchronization between warehouses"},
            {"id": "F_Low_Stock_Alert", "type": "Function", "links": ["B_Inventory_Sync"], "description": "Predictive low-stock notification engine"},
            {"id": "D_Warehouse_Levels", "type": "Data", "links": ["F_Low_Stock_Alert"], "description": "Unified inventory registry across all zones"},
            {"id": "A_Role_Warehouse_Lead", "type": "Access", "links": ["F_Low_Stock_Alert"], "description": "Management access for restocking workflows"},
            {"id": "E_Inventory_Restocked", "type": "Event", "links": ["F_Low_Stock_Alert"], "description": "Trigger confirming replenishment completion"}
        ]
        return atfs

    def check_stock(self, sku_id: str):
        """
        Finds reorder logic and supplier info for a given SKU in the graph.
        """
        self.client.logger.info(f"Checking stock context for SKU: {sku_id} via {self.erp_endpoint}")
        # In production, this would query Neo4j or the ERP API
        return {
            "sku": sku_id,
            "reorder_point": 50,
            "supplier": "Global_Logistics_Inc",
            "p_order_function": "F_Purchase_Order_Emit"
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
        stock_ctx = self.check_stock("SKU-99012")
        print(f"\n[STOCK CONTEXT]: {json.dumps(stock_ctx, indent=2)}")
        
        self.client.logger.info("ERP App execution completed.")

if __name__ == "__main__":
    app = ERPApp()
    try:
        app.run()
    finally:
        app.client.close()
