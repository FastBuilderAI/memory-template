import os
import json
import logging
from typing import List, Dict
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("Ontology-Extractor")

class OntologyExtractor:
    """
    Stand-alone script to extract CBFDAE ontology from text.
    Focuses on outputting JSON for review before Dave-Base insertion.
    """

    def __init__(self):
        load_dotenv()
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0)
        
        # Load the prompt from the external file
        prompt_path = os.path.join(os.path.dirname(__file__), "prompts", "cbfdae_extraction.txt")
        with open(prompt_path, 'r') as f:
            self.prompt_template = f.read()

    def extract_from_text(self, text: str) -> Dict:
        """Invokes the AI to extract the ontology from a text chunk."""
        logger.info("Extracting ontology from text chunk...")
        
        prompt = ChatPromptTemplate.from_template(self.prompt_template)
        response = self.llm.invoke(prompt.format(text=text))
        
        try:
            content = response.content.strip()
            if content.startswith("```json"):
                content = content[7:-3]
            
            ontology = json.loads(content)
            logger.info(f"Extraction successful: {len(ontology.get('nodes', []))} nodes found.")
            return ontology

        except Exception as e:
            logger.error(f"Extraction failed: {e}")
            return {"nodes": [], "relationships": []}

    def save_ontology(self, ontology: Dict, output_path: str):
        """Saves the extracted ontology to a JSON file."""
        with open(output_path, 'w') as f:
            json.dump(ontology, f, indent=4)
        logger.info(f"Saved ontology to {output_path}")

if __name__ == "__main__":
    extractor = OntologyExtractor()
    
    # Example snippet from an SEO strategy
    sample_text = """
    The SEO Strategy (Component C_SEO) is managed by the Marketing Team and includes a Keyword Analysis Block (Block B_Analytics). 
    Inside this block, the Harvester function (Function F_Harvest) pulls data from Google Search Console (Data D_GSC_Data). 
    Only the SEO Analyst can access this (Access A_SEO_Analyst). Successful completion triggers an Email Update (Event E_Email).
    """
    
    # Process
    result = extractor.extract_from_text(sample_text)
    
    # Save for review
    extractor.save_ontology(result, "/Users/prabhatsingh/FastBuilderAI-Sales/memory-template/examples/rag-migration/sample_ontology.json")
    
    # Output for immediate review
    print(json.dumps(result, indent=2))
