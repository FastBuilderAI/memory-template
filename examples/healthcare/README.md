# Healthcare FastMemory Case Study

This is a full-fledged example of using FastMemory to manage Clinical Workflows and Patient Data in a HIPAA-compliant manner.

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

- **CBFDAE Ontology**: Maps patient portals, clinical workflows, and appointment booking functions.
- **Neo4j Integration**: Ready-to-plugin placeholders for a graph database.
- **Production Support**: Structured logging, health checks, and HIPAA/PHI awareness.
- **HL7 FHIR Integration**: Demonstrates how to handle FHIR endpoints and Azure Key Vault URLs.

## 🛠️ Variables to Plugin

| Variable | Description |
| --- | --- |
| `NEO4J_URI` | Your Neo4j Bolt URL (e.g., `bolt://localhost:7687`) |
| `HL7_FHIR_ENDPOINT` | URL for your HL7 FHIR service |
| `AZURE_VAULT_URL` | Azure Key Vault URL for PHI encryption keys |
| `AUDIT_LOG_ENDPOINT` | Splunk/Datadog endpoint for HIPAA audit logs |
