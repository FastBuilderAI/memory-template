# CRM FastMemory Case Study

This is a full-fledged example of using FastMemory to manage CRM and Revenue Operations (RevOps).

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

- **CBFDAE Ontology**: Maps sales pipelines, lead scoring functions, and prospect data.
- **Neo4j Integration**: Ready-to-plugin placeholders for a graph database.
- **Production Support**: Structured logging, health checks, and environment-based configuration.
- **Salesforce/HubSpot Integration**: Demonstrates how to handle CRM instance URLs.

## 🛠️ Variables to Plugin

| Variable | Description |
| --- | --- |
| `NEO4J_URI` | Your Neo4j Bolt URL (e.g., `bolt://localhost:7687`) |
| `SALESFORCE_INSTANCE_URL` | Your Salesforce organization URL |
| `CRM_API_KEY` | Secret key for CRM API access |
