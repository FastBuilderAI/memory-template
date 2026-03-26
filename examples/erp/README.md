# ERP FastMemory Case Study

This is a full-fledged example of using FastMemory to manage Enterprise Resource Planning (ERP), focusing on supply chain and inventory synchronization.

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

- **CBFDAE Ontology**: Maps supply chains, inventory sync blocks, and low-stock alert functions.
- **Neo4j Integration**: Ready-to-plugin placeholders for a graph database.
- **Production Support**: Structured logging, health checks, and environment-based configuration.
- **SAP/Odoo Integration**: Demonstrates how to handle ERP endpoints and authentication.

## 🛠️ Variables to Plugin

| Variable | Description |
| --- | --- |
| `NEO4J_URI` | Your Neo4j Bolt URL (e.g., `bolt://localhost:7687`) |
| `ERP_ENDPOINT` | URL for your ERP system (Odoo, SAP, etc.) |
| `ERP_SECRET` | Authentication token for ERP API |
| `INVENTORY_DB_URI` | Specific URI for the inventory-specific graph database |
