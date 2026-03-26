# AWS FastMemory Deployment Template

This is a full-fledged example of deploying FastMemory on Amazon Web Services (AWS) using ECS Fargate, S3, and Amazon Neptune.

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

- **CBFDAE Ontology**: Maps cloud infrastructure components to FastMemory nodes.
- **Neo4j/Neptune Integration**: Ready-to-plugin placeholders for a graph database.
- **Production Support**: Structured logging, health checks, and IAM-aware configuration.
- **S3 Connectivity**: Demonstrates how to load Atomic Text Functions from S3.

## 🛠️ Variables to Plugin

| Variable | Description |
| --- | --- |
| `NEO4J_URI` | Your Neo4j or Neptune Bolt URL |
| `AWS_REGION` | AWS Region (e.g., `us-east-1`) |
| `AWS_S3_BUCKET` | S3 Bucket name for storing ATFs |
| `BEDROCK_MODEL_ID` | Amazon Bedrock model ID (e.g., `anthropic.claude-3-5-sonnet-20240620-v1:0`) |
