import os
import json

# --- Configuration ---
# Replace with your actual endpoints and credentials
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "admin")
CRM_API_KEY = os.getenv("CRM_API_KEY", "crm-secret-key")

# Salesforce/HubSpot Integration
SALESFORCE_INSTANCE_URL = os.getenv("SALESFORCE_INSTANCE_URL", "https://na1.salesforce.com")

def build_crm_graph():
    """
    Demonstrates building a FastMemory CRM graph (Revenue Ops).
    """
    print("Building CRM FastMemory Graph...")
    atfs = [
        {"id": "C_Revenue_Ops", "type": "Component", "description": "Revenue operations and sales tracking"},
        {"id": "B_Sales_Pipeline", "type": "Block", "links": ["C_Revenue_Ops"]},
        {"id": "F_Lead_Scoring", "type": "Function", "links": ["B_Sales_Pipeline"]},
        {"id": "D_Prospect_Metadata", "type": "Data", "links": ["F_Lead_Scoring"]},
        {"id": "A_Role_SDR_Associate", "type": "Access", "links": ["F_Lead_Scoring"]},
        {"id": "E_Lead_Qualified", "type": "Event", "links": ["F_Lead_Scoring"]}
    ]
    return atfs

def execute_revenue_query(client_id):
    """
    Retrieves sales and invoice context for a specific client.
    """
    print(f"Retrieving context for client: {client_id}")
    # Mocking graph traversal
    return {
        "status": "In_Negotiation",
        "last_invoice": "INV-2024-001",
        "assigned_sdr": "sdr_jane_doe",
        "access_required": "Role_Finance"
    }

if __name__ == "__main__":
    crm_graph = build_crm_graph()
    print(f"CRM Graph Nodes: {len(crm_graph)}")
    
    result = execute_revenue_query("CLI-882")
    print(f"Client Context: {json.dumps(result, indent=2)}")
