# E-commerce FastMemory Case Study

This is a full-fledged example of using FastMemory to manage E-commerce operations, from digital fronts to fulfillment.

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

- **CBFDAE Ontology**: Maps digital fronts, checkout logic, and dynamic pricing functions.
- **Neo4j Integration**: Ready-to-plugin placeholders for a graph database.
- **Production Support**: Structured logging, health checks, and environment-based configuration.
- **Shopify/Stripe Integration**: Demonstrates how to handle store APIs and payment keys.

## 🛠️ Variables to Plugin

| Variable | Description |
| --- | --- |
| `NEO4J_URI` | Your Neo4j Bolt URL (e.g., `bolt://localhost:7687`) |
| `STORE_API_BASE` | Base URL for your E-commerce platform (Shopify, Magento, etc.) |
| `STRIPE_API_KEY` | Secret key for Stripe payments |
| `INVENTORY_CSV_PATH` | Path to your inventory data (supports S3/GCS URIs) |
