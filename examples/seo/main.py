import os
import sys
import json
from typing import List, Dict, Any

# Add parent directory to sys.path to import shared client
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.fastmemory_client import FastMemoryClient

class SEOApp:
    def __init__(self):
        self.client = FastMemoryClient("SEO-Strategy")
        
        # SEO Specific Config
        self.analytics_url = os.getenv("SEO_ANALYTICS_ENDPOINT", "https://api.semrush.com")
        self.openai_key = os.getenv("OPENAI_API_KEY", "your-api-key")

    def build_graph(self) -> List[Dict[str, Any]]:
        """
        Builds the SEO graph using CBFDAE ontology.
        """
        self.client.logger.info("Defining SEO Strategy nodes...")
        atfs = [
            {"id": "C_Client_Success", "type": "Component", "description": "Client success management for SEO"},
            {"id": "B_SEO_Strategy", "type": "Block", "links": ["C_Client_Success"], "description": "High-level SEO tactics and planning"},
            {"id": "F_Keyword_Harvesting", "type": "Function", "links": ["B_SEO_Strategy"], "description": "Semantic keyword discovery engine"},
            {"id": "D_Keyword_Clusters", "type": "Data", "links": ["F_Keyword_Harvesting"], "description": "Grouped semantically relevant search terms"},
            {"id": "A_Role_SEO_Analyst", "type": "Access", "links": ["F_Keyword_Harvesting"], "description": "Authorized access for strategy optimization"},
            {"id": "E_Ranking_Update", "type": "Event", "links": ["F_Keyword_Harvesting"], "description": "Trigger confirming ranking position changes"}
        ]
        return atfs

    def query_seo_context(self, keyword: str):
        """
        Queries the FastMemory graph for SEO context related to a keyword.
        """
        self.client.logger.info(f"Querying SEO context for: '{keyword}' via {self.analytics_url}")
        # In production, this would query Neo4j or the Analytics API
        return {
            "keyword": keyword,
            "relevant_block": "B_SEO_Strategy",
            "functions": ["F_Keyword_Harvesting", "F_Content_Mapping"],
            "data_source": "SERP_Metrics_v2"
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
        seo_ctx = self.query_seo_context("AI content strategy")
        print(f"\n[SEO CONTEXT]: {json.dumps(seo_ctx, indent=2)}")
        
        self.client.logger.info("SEO App execution completed.")

if __name__ == "__main__":
    app = SEOApp()
    try:
        app.run()
    finally:
        app.client.close()
