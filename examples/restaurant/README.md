# Restaurant FastMemory Case Study

This is a full-fledged example of using FastMemory to manage Restaurant Kitchen Display Systems (KDS) and Table Service.

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

- **CBFDAE Ontology**: Maps table service, KDS displays, and course timing functions.
- **Neo4j Integration**: Ready-to-plugin placeholders for a graph database.
- **Production Support**: Structured logging, health checks, and kitchen-specific configuration.
- **KDS Integration**: Demonstrates how to handle KDS IP addresses and recipe database paths.

## 🛠️ Variables to Plugin

| Variable | Description |
| --- | --- |
| `NEO4J_URI` | Your Neo4j Bolt URL (e.g., `bolt://localhost:7687`) |
| `KDS_IP_ADDRESS` | IP address of the Kitchen Display System |
| `RECIPE_DB_PATH` | Path to the local or remote recipe database (JSON/SQL) |
