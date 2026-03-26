# SEO FastMemory Case Study

This is a full-fledged example of using FastMemory to manage SEO Strategy and Client Success.

## 🚀 Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment**:
   Copy `.env.example` to `.env` and fill in your variables.
   ```bash
   cp .env.example .env
   ```

3. **Run the App**:
   ```bash
   python main.py
   ```

### 🔍 Search & Query (AI Agent)

We've provided a `llquery.py` script that uses **LangGraph** and **OpenAI** to intelligently query the FastMemory graph.

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run a Query**:
   ```bash
   python fastllmquery.py "How do we handle keyword clustering?"
   ```

The agent will:
- Retrieve the relevant **CBFDAE** context from Neo4j.
- Use GPT-4o to explain the relationships between keyword harvesting, ranking updates, and strategy optimization.

### 🆚 Standard RAG (Comparison)

We've also provided a `simplellmquery.py` script to demonstrate the difference between **Topological Recall** (FastMemory) and **Standard RAG**.

1. **Run Standard RAG**:
   ```bash
   python simplellmquery.py "How do we handle keyword clustering?"
   ```

Observe how the standard RAG response lacks the deep architectural context (Components, Blocks, Access Rules) provided by the FastMemory graph in `fastllmquery.py`.

---

## 📂 Features

- **CBFDAE Ontology**: Maps client success modules, SEO strategies, and keyword harvesting functions.
- **Neo4j Integration**: Ready-to-plugin placeholders for a graph database.
- **Production Support**: Structured logging, health checks, and environment-based configuration.
- **SEMrush/Analytics Integration**: Demonstrates how to handle SEO analytics endpoints.

## 🛠️ Variables to Plugin

| Variable | Description |
| --- | --- |
| `NEO4J_URI` | Your Neo4j Bolt URL (e.g., `bolt://localhost:7687`) |
| `SEO_ANALYTICS_ENDPOINT` | URL for the SEO analytics provider (SEMrush, Ahrefs, etc.) |
| `OPENAI_API_KEY` | Placeholder for content generation and semantic mapping |
