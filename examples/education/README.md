# Education FastMemory Case Study

This is a full-fledged example of using FastMemory to manage Academic Records and Learning Operations (LearnOps).

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

- **CBFDAE Ontology**: Maps learning ops, academic blocks, and enrollment functions.
- **Neo4j Integration**: Ready-to-plugin placeholders for a graph database.
- **Production Support**: Structured logging, health checks, and environment-based configuration.
- **LMS Integration**: Demonstrates how to handle Canvas/Moodle/Blackboard API keys.

## 🛠️ Variables to Plugin

| Variable | Description |
| --- | --- |
| `NEO4J_URI` | Your Neo4j Bolt URL (e.g., `bolt://localhost:7687`) |
| `LMS_API_KEY` | Access token for the Learning Management System |
| `COURSE_DB_URI` | Connection string for the course/student database |
| `FABRIC_WORKSPACE_ID` | Microsoft Fabric workspace ID for transcript analytics |
