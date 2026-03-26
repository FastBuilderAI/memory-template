# Azure FastMemory Integration Template

## Architecture Map
```mermaid
graph LR
    User[End User] --> A_App[Azure App Service]
    A_App --> AOAI[Azure OpenAI Service]
    A_App --> FM_Container[FastMemory Service - ACI/AKS]
    FM_Container --> ADL[Azure Data Lake Storage Gen2]
    FM_Container --> GDB[(Neo4j / CosmosDB Graph)]
    FM_Container --> AM[Azure Monitor / Application Insights]
```

## Integration Plan
1.  **Storage**: Use OneLake or ADLS Gen2 for raw ATF Markdown storage.
2.  **Compute**: Deploy FastMemory as an Azure Container Instance (ACI) for light workloads or AKS for scale.
3.  **LLM**: Configure FastMemory to call Azure OpenAI GPT-4o models for clustering validation.
4.  **Security**: Map `A_` (Access) nodes to Azure AD Application Roles for built-in RBAC.
