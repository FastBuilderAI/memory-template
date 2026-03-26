# GCP FastMemory Deployment Template

This is a full-fledged example of deploying FastMemory on Google Cloud Platform (GCP) using GKE, GCS, and Vertex AI.

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

- **CBFDAE Ontology**: Maps GCP project structure and Vertex AI objects to FastMemory nodes.
- **Neo4j Integration**: Ready-to-plugin placeholders for a graph database on GCE.
- **Production Support**: Structured logging, health checks, and Cloud Logging awareness.
- **Vertex AI Pipeline**: Demonstrates semantic relationship extraction using Gemini.

## 🛠️ Variables to Plugin

| Variable | Description |
| --- | --- |
| `NEO4J_URI` | Your Neo4j Bolt URL on GCE |
| `GCP_PROJECT_ID` | Your Google Cloud Project ID |
| `GCS_BUCKET` | Cloud Storage bucket for ATF storage |
| `VERTEX_LOCATION` | Region for Vertex AI services (e.g., `us-central1`) |
