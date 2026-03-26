import os
import json

# --- Configuration ---
# ERP Systems (Odoo, SAP, Oracle)
ERP_ENDPOINT = os.getenv("ERP_ENDPOINT", "https://erp.internal.company.com")
ERP_SECRET = os.getenv("ERP_SECRET", "erp-auth-token")

# Database for Inventory Graph
INVENTORY_DB_URI = os.getenv("INVENTORY_DB_URI", "bolt://inventory-graph:7687")

def build_erp_inventory_graph():
    """
    Builds FastMemory graph for Supply Chain and Inventory.
    """
    print("Building ERP Inventory FastMemory Graph...")
    atfs = [
        {"id": "C_Supply_Chain", "type": "Component"},
        {"id": "B_Inventory_Sync", "type": "Block", "links": ["C_Supply_Chain"]},
        {"id": "F_Low_Stock_Alert", "type": "Function", "links": ["B_Inventory_Sync"]},
        {"id": "D_Warehouse_Levels", "type": "Data", "links": ["F_Low_Stock_Alert"]},
        {"id": "A_Role_Warehouse_Lead", "type": "Access", "links": ["F_Low_Stock_Alert"]},
        {"id": "E_Inventory_Restocked", "type": "Event", "links": ["F_Low_Stock_Alert"]}
    ]
    return atfs

def check_stock_context(sku_id):
    """
    Finds reorder logic and supplier info for a given SKU in the graph.
    """
    print(f"Checking graph context for SKU: {sku_id}")
    return {
        "sku": sku_id,
        "reorder_point": 50,
        "supplier": "Global_Logistics_Inc",
        "p_order_function": "F_Purchase_Order_Emit"
    }

if __name__ == "__main__":
    erp_graph = build_erp_inventory_graph()
    print(f"ERP Graph initialized with {len(erp_graph)} nodes.")
    
    stock_info = check_stock_context("SKU-99012")
    print(f"Stock Context: {json.dumps(stock_info, indent=2)}")
