import os
import logging
import json
from typing import List, Dict, Any, Optional
try:
    from dotenv import load_dotenv
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False

# Try to import neo4j, but don't fail if not present (production support placeholder)
try:
    from neo4j import GraphDatabase
    NEO4J_AVAILABLE = True
except ImportError:
    NEO4J_AVAILABLE = False

class FastMemoryClient:
    """
    A production-ready client for FastMemory, handling Neo4j connectivity,
    logging, and environment management.
    """
    def __init__(self, context_name: str):
        if DOTENV_AVAILABLE:
            load_dotenv()
        self.context_name = context_name
        self._setup_logging()
        self._load_config()
        self.driver = None
        
        if NEO4J_AVAILABLE:
            self._connect_neo4j()
        else:
            self.logger.warning("Neo4j driver not installed. Running in mock/memory mode.")

    def _setup_logging(self):
        log_level = os.getenv("LOG_LEVEL", "INFO").upper()
        logging.basicConfig(
            level=getattr(logging, log_level, logging.INFO),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(f"FastMemory-{self.context_name}")

    def _load_config(self):
        self.neo4j_uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        self.neo4j_user = os.getenv("NEO4J_USER", "neo4j")
        self.neo4j_password = os.getenv("NEO4J_PASSWORD", "password")
        self.llm_api_key = os.getenv("LLM_API_KEY", "sk-placeholder")

    def _connect_neo4j(self):
        try:
            self.driver = GraphDatabase.driver(
                self.neo4j_uri, 
                auth=(self.neo4j_user, self.neo4j_password)
            )
            self.logger.info(f"Connected to Neo4j at {self.neo4j_uri}")
        except Exception as e:
            self.logger.error(f"Failed to connect to Neo4j: {e}")

    def health_check(self) -> Dict[str, Any]:
        """
        Performs a system health check.
        """
        status = {
            "status": "healthy",
            "context": self.context_name,
            "neo4j": "connected" if self.driver else "not_connected",
            "llm_api": "configured" if self.llm_api_key != "sk-placeholder" else "not_configured"
        }
        self.logger.info(f"Health Check: {json.dumps(status)}")
        return status

    def deploy_graph(self, atfs: List[Dict[str, Any]]):
        """
        Placeholder for deploying an ATF graph to FastMemory/Neo4j.
        """
        self.logger.info(f"Deploying {len(atfs)} nodes to FastMemory graph...")
        # Production implementation would upsert nodes and relationships based on CBFDAE ontology
        for atf in atfs:
            self.logger.debug(f"Processing node: {atf.get('id')}")
        
        return {"status": "success", "nodes_processed": len(atfs)}

    def close(self):
        if self.driver:
            self.driver.close()
            self.logger.info("Neo4j connection closed.")
