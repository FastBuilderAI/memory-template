# RAG Migration Tool

This tool automates the transition from standard, flat RAG (Vector Stores) to the deterministic **FastMemory** (Graph/CBFDAE) architecture.

## How it Works
1.  **Extract**: Reads your existing RAG chunks (Text/JSON).
2.  **Analyze**: Uses **GPT-4o** and an expert Ontologist prompt to identify System Components, Functions, and Data nodes.
3.  **Transform**: Automatically creates the 1st-degree relationships (edges) in Neo4j.
4.  **Deduplicate**: Uses `MERGE` logic to ensure your graph stays clean.

## Prerequisites
- **OpenAI API Key**: Set in `.env`.
- **Neo4j Instance**: Set connection details in `.env` (or use the shared client default).

## Usage
1.  Install dependencies: `pip install -r requirements.txt`
2.  Run the migration: `python main.py`

## Benefits
- **Zero-to-Graph in Minutes**: No manual drafting of the ontology required.
- **Relational Integrity**: Turns disconnected sentences into a traversable system mesh.
- **Contextual Recall**: Enables the use of `fastllmquery.py` on your legacy RAG data immediately.
