import os
import sys
from typing import List
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_core.documents import Document

# Add parent directory to sys.path to import shared client
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.fastmemory_client import FastMemoryClient

class SimpleRAGQuery:
    def __init__(self):
        self.client = FastMemoryClient("SEO-Simple-RAG")
        self.embeddings = OpenAIEmbeddings(api_key=self.client.llm_api_key)
        self.llm = ChatOpenAI(model="gpt-4o", api_key=self.client.llm_api_key)
        
        # Mock SEO documentation as raw text (Standard RAG input)
        self.raw_data = [
            "SEO Strategy Block covers high-level tactics and planning for rankings.",
            "Client Success Component manages the successful outcomes for SEO clients.",
            "Keyword Harvesting Function is our discovery engine for new search terms.",
            "Keyword Clusters Data contains groups of semantically relevant keywords.",
            "SEO Analyst Role has access to the keyword harvesting function.",
            "Ranking Update Event triggers when a position changes on the SERPs."
        ]
        
        self._initialize_vector_store()

    def _initialize_vector_store(self):
        """
        Initializes a mock vector store with the raw SEO data.
        """
        self.client.logger.info("Initializing vector store for standard RAG...")
        docs = [Document(page_content=t) for t in self.raw_data]
        self.vector_store = DocArrayInMemorySearch.from_documents(
            docs, self.embeddings
        )

    def run_query(self, question: str):
        """
        Performs a standard RAG search and generation.
        """
        self.client.logger.info(f"Performing standard RAG query: {question}")
        
        # 1. Similarity Search (Raw Retrieval)
        docs = self.vector_store.similarity_search(question, k=3)
        context = "\n".join([d.page_content for d in docs])
        
        # 2. Answer Generation
        system_prompt = (
            "You are a Senior SEO Consultant. Use the provided context to answer the question. "
            "Note: This is a standard RAG system with NO knowledge of system topology or relationships."
        )
        
        human_prompt = f"Question: {question}\n\nRetrieved Context:\n{context}"
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=human_prompt)
        ]
        
        response = self.llm.invoke(messages)
        
        print("\n" + "="*50)
        print("STANDARD RAG (WITHOUT FASTMEMORY)")
        print("="*50)
        print(f"QUESTION: {question}")
        print("-" * 50)
        print(f"RETRIEVED CONTEXT:\n{context}")
        print("-" * 50)
        print(f"RESPONSE:\n{response.content}")
        print("="*50 + "\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_q = " ".join(sys.argv[1:])
    else:
        user_q = "How do we handle keyword clustering and ranking updates in our SEO strategy?"
        
    rag = SimpleRAGQuery()
    rag.run_query(user_q)
