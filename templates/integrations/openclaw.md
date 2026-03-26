# OpenClaw FastMemory Integration Template

## Workflow
```mermaid
sequenceDiagram
    participant OC as OpenClaw_Agent
    participant FM as FastMemory_MCP
    participant KB as Neo4j_Knowledge_Graph
    
    OC->>FM: query_memory(intent="user_request")
    FM->>KB: Cypher(MATCH nodes-edges)
    KB-->>FM: CBFDAE_SubGraph
    FM-->>OC: Structured_Context(ATFs)
    OC->>OC: Reason + Act
```

## Integration Steps
1.  **Expose FastMemory**: Run `fastmemory mcp` to start the Model Context Protocol server.
2.  **Plugin Configuration**: Add the FastMemory MCP endpoint to OpenClaw's `config.yaml`.
3.  **Context Injection**: OpenClaw uses the `get_block` tool to retrieve domain-specific logic before executing tasks.
