# Finance FastMemory Case Study

This is a full-fledged example of using FastMemory to manage Wealth Management and Trading operations.

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

- **CBFDAE Ontology**: Maps asset management, compliance blocks, and KYC functions.
- **Neo4j Integration**: Ready-to-plugin placeholders for a graph database.
- **Production Support**: Structured logging, health checks, and environment-based configuration.
- **Market Data Integration**: Demonstrates how to handle Bloomberg/Refinitiv API endpoints.

## 🛠️ Variables to Plugin

| Variable | Description |
| --- | --- |
| `NEO4J_URI` | Your Neo4j Bolt URL (e.g., `bolt://localhost:7687`) |
| `MARKET_DATA_API` | URL for financial market data provider |
| `KYC_VERIFIER_URL` | Endpoint for internal KYC/AML verification service |
| `LEDGER_DB_URI` | URI for the immutable ledger graph database |
