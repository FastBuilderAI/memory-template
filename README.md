# FastMemory Deployment Templates

Welcome to the official deployment templates for **FastMemory**, the horizontal layer of truth for enterprise AI. This repository provides modular concept maps, integration plans, and Python examples for deploying FastMemory across various industries and cloud environments.

## 🔗 Key Resources
- **FastBuilder.AI**: [https://fastbuilder.ai](https://fastbuilder.ai)
- **Core FastMemory Repo**: [https://github.com/fastbuilderai/memory](https://github.com/fastbuilderai/memory)
- **Superfast (Agent Framework)**: [https://github.com/FastBuilderAI/superfast](https://github.com/FastBuilderAI/superfast)

## 🏗️ What is FastMemory?
> **Engine Compatibility**: Fully compatible with `FastMemory v0.2.2+` (Enterprise Telemetry Edition).

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
- [Superfast Integration](https://github.com/FastBuilderAI/superfast/tree/main/skills/fastmemory)

### 3. Python Examples (`/examples`)
Runnable Python applications for each case with production features:
- **Neo4j/GraphDB Support**: Built-in placeholders for persistence.
- **Structured Logging**: Production-ready logging system.
- **Environment Management**: Automatic `.env` support via `shared.FastMemoryClient`.
- **Requirements Specifics**: Individual `requirements.txt` for each example.

---

## 🚀 Getting Started

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/FastBuilderAI/memory-template
   cd memory-template
   ```

2. **Choose an Example (e.g., Coffee Shop)**:
   ```bash
   cd examples/coffeeshop
   pip install -r requirements.txt
   ```

3. **Configure Your Environment**:
   Copy `.env.example` and fill in your credentials:
   ```bash
   cp .env.example .env
   ```

4. **Run the App**:
   ```bash
   python main.py
   ```

---

## 🏗️ Architecture: Shared Client

All examples now inherit from a standardized production template via `examples/shared/fastmemory_client.py`. This ensures consistent behavior for:
- **Connectivity**: Graceful handling of Neo4j/LLM drivers.
- **Observability**: Health checks and structured logging.
- **Scalability**: Decoupled domain logic from infrastructure.

## 🤝 Contributing
We welcome contributions! Please map your industry use cases to the CBFDAE framework and submit a PR.
