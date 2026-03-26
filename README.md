# FastMemory Deployment Templates

Welcome to the official deployment templates for **FastMemory**, the horizontal layer of truth for enterprise AI. This repository provides modular concept maps, integration plans, and Python examples for deploying FastMemory across various industries and cloud environments.

## 🔗 Key Resources
- **FastBuilder.AI**: [https://fastbuilder.ai](https://fastbuilder.ai)
- **Core FastMemory Repo**: [https://github.com/fastbuilderai/memory](https://github.com/fastbuilderai/memory)

## 🏗️ What is FastMemory?
FastMemory is an AI memory system that uses the **CBFDAE** (Component, Block, Function, Data, Access, Event) ontology to build a structured, low-hallucination cognitive graph for AI agents.

---

## 📂 Repository Structure

### 1. Domain Templates (`/templates/domains`)
Industry-specific concept maps (Mermaid) and Atomic Text Function (ATF) samples.
- [SEO](templates/domains/seo.md) | [CRM](templates/domains/crm.md) | [ERP](templates/domains/erp.md)
- [E-commerce](templates/domains/ecommerce.md) | [Healthcare](templates/domains/healthcare.md) | [Education](templates/domains/education.md)
- [Finance](templates/domains/finance.md) | [Coffee Shop](templates/domains/coffeeshop.md) | [Restaurant](templates/domains/restaurant.md)

### 2. Cloud & Framework Integrations (`/templates/cloud` & `/templates/integrations`)
Architecture maps and step-by-step setup guides for major cloud providers and agentic frameworks.
- [Azure OpenAI](templates/cloud/azure.md)
- [AWS Bedrock](templates/cloud/aws.md)
- [GCP Vertex AI](templates/cloud/gcp.md)
- [OpenClaw Integration](templates/integrations/openclaw.md)

### 3. Python Examples (`/examples`)
Runnable Python scripts for each case with configurable placeholders for database endpoints, LLM API keys, and cloud service credentials.
- Set environment variables like `OPENAI_API_KEY`, `NEO4J_URI`, `AZURE_OPENAI_KEY`, etc.
- Run any example: `python examples/seo/main.py`

---

## 🚀 Getting Started

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/FastBuilderAI/memory-template
   cd memory-template
   ```

2. **Install FastMemory**:
   Follow instructions at [FastBuilderAI/memory](https://github.com/fastbuilderai/memory).

3. **Configure Your Environment**:
   Copy `.env.example` (if provided) or export your credentials:
   ```bash
   export NEO4J_URI="bolt://your-neo4j-instance:7687"
   export OPENAI_API_KEY="sk-..."
   ```

4. **Run an Example**:
   ```bash
   python examples/healthcare/main.py
   ```

## 🤝 Contributing
We welcome contributions! Please map your industry use cases to the CBFDAE framework and submit a PR.
