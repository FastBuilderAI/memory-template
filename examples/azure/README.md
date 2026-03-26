# Azure FastMemory Deployment Template

This is a full-fledged example of deploying FastMemory on Microsoft Azure using ACI/AKS, Data Lake Gen2, and CosmosDB.

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

- **CBFDAE Ontology**: Maps Azure resources and enterprise context to FastMemory nodes.
- **Neo4j/CosmosDB Integration**: Ready-to-plugin placeholders for a graph database.
- **Production Support**: Structured logging, health checks, and Entra ID (AD) awareness.
- **Data Lake Sync**: Demonstrates how to index content from Azure Data Lake Gen2.

## 🛠️ Variables to Plugin

| Variable | Description |
| --- | --- |
| `NEO4J_URI` | Your Neo4j or CosmosDB Gremlin URL |
| `AZURE_OPENAI_KEY` | Your Azure OpenAI API Key |
| `AZURE_OPENAI_ENDPOINT` | Your Azure OpenAI Resource Endpoint |
| `AZURE_GRAPH_URI` | Cosmos DB or Neo4j endpoint on Azure |
| `AZURE_TENANT_ID` | Your Azure Active Directory Tenant ID |
