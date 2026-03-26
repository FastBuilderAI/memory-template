# OpenClaw FastMemory Integration

This is a full-fledged example of bridging **OpenClaw** agents with **FastMemory MCP** (Model Context Protocol).

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

- **CBFDAE Ontology**: Maps agent runtimes and reasoning loops to FastMemory nodes.
- **MPC Support**: Demonstrates how to connect an agent to a FastMemory MCP server.
- **Production Support**: Structured logging, health checks, and reasoning loop monitoring.
- **Agent Reasoning**: Simulates an agent retrieving context before acting.

## 🛠️ Variables to Plugin

| Variable | Description |
| --- | --- |
| `NEO4J_URI` | Your Neo4j Bolt URL (e.g., `bolt://localhost:7687`) |
| `OPENCLAW_API_KEY` | Secret key for the OpenClaw agent platform |
| `FASTMEMORY_MCP_URL` | URL for the FastMemory MCP server (e.g., `http://localhost:8000/mcp`) |
| `LLM_API_KEY` | Placeholder for the LLM provider used by the agent |
