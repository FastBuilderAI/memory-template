import os
import sys
import json
from typing import List, Dict, Any

# Add parent directory to sys.path to import shared client
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.fastmemory_client import FastMemoryClient

class FinanceApp:
    def __init__(self):
        self.client = FastMemoryClient("Finance-WealthMgmt")
        
        # Finance Specific Config
        self.market_api = os.getenv("MARKET_DATA_API", "https://api.marketdata.com/v2")
        self.kyc_url = os.getenv("KYC_VERIFIER_URL", "https://kyc-service.internal")

    def build_graph(self) -> List[Dict[str, Any]]:
        """
        Builds the Finance graph using CBFDAE ontology.
        """
        self.client.logger.info("Defining Finance Wealth Mgmt nodes...")
        atfs = [
            {"id": "C_Asset_Mgmt", "type": "Component", "description": "Core wealth management and portolio engine"},
            {"id": "B_Immutable_Logs", "type": "Block", "links": ["C_Asset_Mgmt"], "description": "Tamper-proof audit trails for all trades"},
            {"id": "F_KYC_Verification", "type": "Function", "links": ["B_Immutable_Logs"], "description": "Automated compliance and identity verification"},
            {"id": "D_User_Compliance_Dossier", "type": "Data", "links": ["F_KYC_Verification"], "description": "Legal and financial profiles of investors"},
            {"id": "A_Role_Risk_Compliance", "type": "Access", "links": ["F_KYC_Verification"], "description": "Authorized access for risk officers"},
            {"id": "E_Transaction_Settled", "type": "Event", "links": ["F_KYC_Verification"], "description": "Trigger for final trade settlement"}
        ]
        return atfs

    def execute_trade(self, order_id: str):
        """
        Finds trading execution logic and risk constraints in the graph.
        """
        self.client.logger.info(f"Checking trade context for order: {order_id} via {self.market_api}")
        # In production, this would query Neo4j or the Trading Engine
        return {
            "order": order_id,
            "execution_function": "F_Trade_Engine",
            "compliance_checked": True,
            "portfolio_data": "Real_Time_Ticker_v4"
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
        trade_ctx = self.execute_trade("ORD-TX-0091")
        print(f"\n[TRADE CONTEXT]: {json.dumps(trade_ctx, indent=2)}")
        
        self.client.logger.info("Finance App execution completed.")

if __name__ == "__main__":
    app = FinanceApp()
    try:
        app.run()
    finally:
        app.client.close()
