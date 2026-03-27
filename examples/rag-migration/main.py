import os
import json
import logging
from typing import List, Dict
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from ..shared.fastmemory_client import FastMemoryClient

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("RAG-Migration")

class RAGMigrator:
    """
    Migrates flat RAG data (JSON/Text) into FastMemory (Neo4j/Graph).
    Uses GPT-4o to extract CBFDAE ontology nodes and relationships.
    """

    def __init__(self):
        load_dotenv()
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0)
        self.client = FastMemoryClient()
        
        self.extraction_prompt = ChatPromptTemplate.from_template("""
        You are an expert Ontologist. Your task is to transform a flat RAG text chunk into a 
        FastMemory CBFDAE Graph structure (Component, Block, Function, Data, Access, Event).

        ONTOLOGY RULES:
        - Component (C_): High-level system modules or owners.
        - Block (B_): Functional logical units.
        - Function (F_): Executable actions or operations.
        - Data (D_): Key entities, datasets, or parameters.
        - Access (A_): Permission rules or security gates.
        - Event (E_): Triggers or side-effects.

        TASK:
        1. Extract all entities from the text that fit these categories.
        2. Identify relationships between them (e.g., F_ generates D_, C_ contains B_).
        3. Return as a clean JSON object with "nodes" and "relationships".

        TEXT CHUNK:
        {text}

        JSON OUTPUT:
        """)

    def migrate_json_export(self, json_path: str):
        """Migrates a standard vector store JSON export."""
        if not os.path.exists(json_path):
            logger.error(f"File not found: {json_path}")
            return

        with open(json_path, 'r') as f:
            data = json.load(f)

        logger.info(f"Starting migration of {len(data)} chunks...")
        
        for i, chunk in enumerate(data):
            text = chunk.get("text", chunk.get("page_content", ""))
            if not text:
                continue
            
            logger.info(f"Processing chunk {i+1}/{len(data)}...")
            self._process_chunk(text)

    def _process_chunk(self, text: str):
        """Analyzes and transforms a single text chunk into graph nodes."""
        response = self.llm.invoke(self.extraction_prompt.format(text=text))
        
        try:
            # Simple cleanup of LLM response if needed
            content = response.content.strip()
            if content.startswith("```json"):
                content = content[7:-3]
            
            graph_data = json.loads(content)
            
            # Create nodes
            for node in graph_data.get("nodes", []):
                self.client.execute_query(
                    "MERGE (n:Node {id: $id}) SET n.type = $type, n.label = $label, n.description = $desc",
                    {"id": node["id"], "type": node["type"], "label": node.get("label", node["id"]), "desc": node.get("description", "")}
                )
            
            # Create relationships
            for rel in graph_data.get("relationships", []):
                self.client.execute_query(
                    "MATCH (a:Node {id: $source}), (b:Node {id: $target}) "
                    "MERGE (a)-[r:RELATED {type: $type}]->(b)",
                    {"source": rel["source"], "target": rel["target"], "type": rel["type"]}
                )
                
            logger.info(f"Successfully migrated {len(graph_data.get('nodes', []))} nodes.")

        except Exception as e:
            logger.error(f"Failed to process chunk: {e}")

if __name__ == "__main__":
    migrator = RAGMigrator()
    
    # Mocking a RAG export for demonstration
    mock_rag_data = [
        {
            "text": "The SEO Analytics module (Component C_Analytics) contains a Keyword Harvester function (Function F_Harvest) that produces a Daily Keyword Cluster (Data D_KwdCluster)."
        },
        {
            "text": "Access to the Analytics module is governed by the Admin Role (Access A_Admin). When a harvest completes, it triggers a Slack Notification (Event E_Notify)."
        }
    ]
    
    # In production, pass a path to a real RAG export JSON
    logger.info("Running demonstration migration...")
    for chunk in mock_rag_data:
        migrator._process_chunk(chunk["text"])
    
    logger.info("Migration demo complete.")
