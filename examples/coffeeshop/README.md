# Coffee Shop FastMemory Case Study

This is a full-fledged example of using FastMemory to manage a Coffee Shop's cognitive graph, integrating POS systems (Square/Toast) and Loyalty programs.

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

## 📂 Features

- **CBFDAE Ontology**: Maps counter service, barista queues, and inventory functions.
- **Neo4j Integration**: Ready-to-plugin placeholders for a graph database.
- **Production Support**: Structured logging, health checks, and environment-based configuration.
- **Mock POS Integration**: Demonstrates how to handle Square/Toast access tokens.

## 🛠️ Variables to Plugin

| Variable | Description |
| --- | --- |
| `NEO4J_URI` | Your Neo4j Bolt URL (e.g., `bolt://localhost:7687`) |
| `SQUARE_ACCESS_TOKEN` | Access token for Square POS API |
| `LOYALTY_SERVICE_URL` | Endpoint for the external loyalty microservice |
